#!/usr/bin/env python3
"""Build clean developer-site markdown corpus: fetch, verify, sanitize, report.

Phases:
  1. Discover family roots from llms.txt (+ docs.md cross-check)
  2. Verbatim fetch to raw/<date>/
  3. Deep-link spot check (5 products) before bulk sanitize
  4. Sanitize + section split → cleaned/<date>/ + quarantine/<date>/
  5. Resumable TOC cross-check (hours; uses local guides cache)

Unfetchable roots stay in the denominator. Reasons split derivation_miss
(ours) from site_defect (theirs). empty_200 is its own code.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.corpus_discovery import (  # noqa: E402
    discovery_to_dict,
    run_discovery,
)
from content_bench.content_engine.corpus_report import render_corpus_report_md  # noqa: E402
from content_bench.content_engine.corpus_sanitize import (  # noqa: E402
    sanitize_root,
    validate_all_sections,
    write_sanitized_product,
)
from content_bench.content_engine.corpus_toc import cross_check_toc_resumable  # noqa: E402
from content_bench.content_engine.deep_link_verify import (  # noqa: E402
    spot_check_deep_links,
    spot_check_report,
)
from content_bench.content_engine.product_roots import (  # noqa: E402
    DEFAULT_BASE,
    fetch_product_root,
    product_id_from_root,
    split_root_sections,
)
from content_bench.content_engine.toc_fetch import http_get  # noqa: E402

UA = "CyberSource-Relay/1.0 (corpus-build)"
ARTIFACTS = ROOT / "artifacts" / "content_engine" / "corpus_build"

# Spot-check anchors across different products before bulk deep-link generation
DEFAULT_SPOT_CHECKS = [
    (
        "boarding",
        "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
        "boarding-intro-overview",
    ),
    (
        "payments",
        "/docs/cybs/en-us/payments/developer/ctv/rest/payments.md",
        "payments-intro",
    ),
    (
        "tms",
        "/docs/cybs/en-us/tms/developer/all/rest/tms.md",
        "tms-overview",
    ),
    (
        "security-keys",
        "/docs/cybs/en-us/security-keys/user/all/ada/security-keys.md",
        "keys-intro",
    ),
    (
        "unified-checkout",
        "/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.md",
        "uc-getting-started",
    ),
]


def _today_stamp() -> str:
    return date.today().isoformat()


def _local_guides_dirs() -> List[Path]:
    dirs = [
        ROOT / "cybersource-docs",
        ROOT / "gateway-docs",
        ROOT / "data" / "products" / "boarding" / "guides",
        ROOT / "data" / "products" / "payments" / "guides",
    ]
    return [d for d in dirs if d.is_dir()]


def phase_discover(args: argparse.Namespace) -> dict:
    only_ids = set(args.only) if args.only else None
    report = run_discovery(
        base_url=args.base_url,
        user_agent=UA,
        probe=not args.skip_probe,
        sleep_s=args.sleep,
        only_product_ids=only_ids,
    )
    payload = discovery_to_dict(report)
    out = ARTIFACTS / "discovery.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    print(
        f"discovered {report.roots_discovered} roots "
        f"({sum(1 for r in report.roots if r.fetch_status == 'ok')} fetchable)"
    )
    return payload


def phase_fetch(discovery: dict, args: argparse.Namespace) -> dict:
    raw_dir = ROOT / "raw" / args.stamp_date
    raw_dir.mkdir(parents=True, exist_ok=True)
    unfetchable: List[dict] = []
    fetched: List[dict] = []
    total_bytes = 0

    roots = discovery.get("roots") or []
    only = set(args.only) if args.only else None

    for rec in roots:
        root_path = rec["root_path"]
        pid = rec.get("product_id") or product_id_from_root(root_path)
        if only and pid not in only:
            continue

        if rec.get("fetch_status") != "ok" and not args.force_fetch:
            unfetchable.append(rec)
            continue

        code, body, local, err = fetch_product_root(
            root_path,
            base_url=args.base_url,
            out_dir=raw_dir,
            root=ROOT,
            user_agent=UA,
        )
        time.sleep(args.sleep)
        if local and not err:
            nbytes = len(body) if body else 0
            total_bytes += nbytes
            fetched.append(
                {
                    "product_id": pid,
                    "root_path": root_path,
                    "local_path": local,
                    "bytes": nbytes,
                    "http_status": code,
                }
            )
        else:
            rec = dict(rec)
            rec["fetch_error"] = err
            unfetchable.append(rec)

    manifest = {
        "stamp_date": args.stamp_date,
        "roots_fetched": len(fetched),
        "total_bytes": total_bytes,
        "fetched": fetched,
        "unfetchable": unfetchable,
    }
    manifest_path = raw_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # PDFs and other structural unfetchables
    pdf_manifest = raw_dir / "manifest-unfetchable.json"
    pdf_manifest.write_text(
        json.dumps(
            {
                "pdfs": discovery.get("pdfs") or [],
                "unfetchable_roots": [
                    r
                    for r in (discovery.get("roots") or [])
                    if r.get("fetch_status") == "unfetchable"
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {manifest_path}")
    print(f"fetched {len(fetched)} roots, {total_bytes} bytes")
    return manifest


def phase_deep_link_check(args: argparse.Namespace) -> dict:
    checks = DEFAULT_SPOT_CHECKS
    if args.only:
        checks = [c for c in checks if c[0] in args.only]
    results = spot_check_deep_links(checks, base_url=args.base_url, user_agent=UA)
    report = spot_check_report(results)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    out = ARTIFACTS / "deep-link-spot-check.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"deep link spot check: {report['anchors_found']}/{report['checked']} found")
    if not report["pass"] and args.require_deep_links:
        print("ERROR: deep link spot check failed — aborting before bulk sanitize", file=sys.stderr)
        sys.exit(1)
    return report


def phase_sanitize(fetch_manifest: dict, args: argparse.Namespace) -> dict:
    cleaned_dir = ROOT / "cleaned" / args.stamp_date
    quarantine_dir = ROOT / "quarantine" / args.stamp_date
    raw_dir = ROOT / "raw" / args.stamp_date

    totals = {
        "sections_total": 0,
        "sections_clean": 0,
        "code_blocks": 0,
        "quarantined_by_kind": {},
    }
    product_reports: List[dict] = []
    validation_failures: Dict[str, dict] = {}

    for item in fetch_manifest.get("fetched") or []:
        pid = item["product_id"]
        if args.only and pid not in args.only:
            continue
        local = ROOT / item["local_path"]
        if not local.is_file():
            # Fallback: file may be recorded relative to raw_dir only
            alt = raw_dir / Path(item["local_path"]).name
            local = alt if alt.is_file() else local
        if not local.is_file():
            continue
        text = local.read_text(encoding="utf-8", errors="replace")
        sections, blocks, report = sanitize_root(
            text,
            root_path=item["root_path"],
            product_id=pid,
            base_url=args.base_url,
        )
        fails = validate_all_sections(sections)
        if fails:
            validation_failures[pid] = fails

        write_sanitized_product(
            sections,
            blocks,
            report,
            cleaned_dir=cleaned_dir,
            quarantine_dir=quarantine_dir,
        )

        totals["sections_total"] += report.sections_total
        totals["sections_clean"] += report.sections_clean
        totals["code_blocks"] += report.code_blocks
        for k, n in report.quarantined_by_kind.items():
            totals["quarantined_by_kind"][k] = (
                totals["quarantined_by_kind"].get(k, 0) + n
            )
        product_reports.append(
            {
                "product_id": pid,
                "fetched": True,
                "bytes": report.bytes_in,
                "sections_total": report.sections_total,
                "sections_clean": report.sections_clean,
                "quarantined_by_kind": report.quarantined_by_kind,
                "code_blocks": report.code_blocks,
            }
        )

    if validation_failures:
        vf_path = ARTIFACTS / "sanitize-validation-failures.json"
        vf_path.write_text(json.dumps(validation_failures, indent=2) + "\n", encoding="utf-8")
        print(f"ERROR: sanitize validation failures: {vf_path}", file=sys.stderr)
        if args.strict:
            sys.exit(1)

    out = {"totals": totals, "products": product_reports}
    (ARTIFACTS / "sanitize-summary.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"sanitized {len(product_reports)} products, "
        f"{totals['sections_clean']}/{totals['sections_total']} clean sections"
    )
    return out


def phase_toc(fetch_manifest: dict, args: argparse.Namespace) -> dict:
    if args.skip_toc:
        print("skipping TOC cross-check (--skip-toc)")
        return {}

    checkpoint_dir = ARTIFACTS / "toc-checkpoint"
    raw_dir = ROOT / "raw" / args.stamp_date
    products: List[dict] = []
    for item in fetch_manifest.get("fetched") or []:
        pid = item["product_id"]
        if args.only and pid not in args.only:
            continue
        local_path = item["local_path"]
        local_file = ROOT / local_path
        if not local_file.is_file():
            local_file = raw_dir / Path(local_path).name
        root_text = None
        if local_file.is_file():
            root_text = local_file.read_text(encoding="utf-8", errors="replace")
        products.append(
            {
                "root_path": item["root_path"],
                "local_path": str(local_file.relative_to(ROOT)) if local_file.is_relative_to(ROOT) else str(local_file),
                "text": root_text,
            }
        )
    report = cross_check_toc_resumable(
        products,
        base_url=args.base_url,
        checkpoint_dir=checkpoint_dir,
        local_guides_dirs=_local_guides_dirs(),
        raw_dir=raw_dir,
        sleep_s=args.sleep,
        user_agent=UA,
        limit=args.toc_limit,
    )
    out = ARTIFACTS / "toc-completeness.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    t = report.get("totals") or {}
    print(
        f"TOC: {t.get('toc_covered', 0)}/{t.get('toc_topics', 0)} covered "
        f"({t.get('done', 0)} products)"
    )
    return report


def _merge_product_rows(
    discovery: dict,
    fetch_manifest: dict,
    sanitize_summary: dict,
    toc_report: dict,
    *,
    only: Optional[set] = None,
) -> List[dict]:
    by_id: Dict[str, dict] = {}
    for rec in discovery.get("roots") or []:
        pid = rec.get("product_id") or product_id_from_root(rec["root_path"])
        if only and pid not in only:
            continue
        by_id[pid] = {
            "product_id": pid,
            "root_path": rec["root_path"],
            "fetched": False,
            "derivation": rec.get("derivation"),
            "unfetchable_reason": rec.get("unfetchable_reason"),
            "unfetchable_bucket": rec.get("unfetchable_bucket"),
        }
    for item in fetch_manifest.get("fetched") or []:
        pid = item["product_id"]
        row = by_id.setdefault(pid, {"product_id": pid})
        row.update({"fetched": True, "bytes": item.get("bytes", 0)})
    for item in sanitize_summary.get("products") or []:
        pid = item["product_id"]
        row = by_id.setdefault(pid, {"product_id": pid})
        row.update(item)
    for item in (toc_report.get("products") or []):
        pid = item["product_id"]
        row = by_id.setdefault(pid, {"product_id": pid})
        row.update(
            {
                "toc_topics": item.get("toc_topics", 0),
                "toc_covered": item.get("toc_covered", 0),
                "toc_missed": item.get("toc_missed", []),
            }
        )
    return sorted(by_id.values(), key=lambda r: r.get("product_id", ""))


def phase_report(
    discovery: dict,
    fetch_manifest: dict,
    deep_check: dict,
    sanitize_summary: dict,
    toc_report: dict,
    args: argparse.Namespace,
) -> None:
    payload = {
        "generated_at": discovery.get("generated_at"),
        "stamp_date": args.stamp_date,
        "discovery": discovery,
        "fetch": {
            "roots_fetched": fetch_manifest.get("roots_fetched", 0),
            "total_bytes": fetch_manifest.get("total_bytes", 0),
            "unfetchable": fetch_manifest.get("unfetchable", []),
        },
        "deep_link_spot_check": deep_check,
        "sanitize": sanitize_summary.get("totals", {}),
        "sanitize_products": sanitize_summary.get("products", []),
        "toc": toc_report,
        "products": _merge_product_rows(
            discovery,
            fetch_manifest,
            sanitize_summary,
            toc_report,
            only=set(args.only) if args.only else None,
        ),
    }
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    jp = ARTIFACTS / "corpus-report.json"
    mp = ARTIFACTS / "corpus-report.md"
    jp.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    mp.write_text(render_corpus_report_md(payload), encoding="utf-8")
    print(f"wrote {mp}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stamp-date", default=_today_stamp())
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--sleep", type=float, default=0.08)
    ap.add_argument("--only", nargs="*", help="Product-id filter (root stem)")
    ap.add_argument("--skip-probe", action="store_true", help="Discovery only, no HTTP probe")
    ap.add_argument("--skip-fetch", action="store_true")
    ap.add_argument("--skip-sanitize", action="store_true")
    ap.add_argument("--skip-toc", action="store_true")
    ap.add_argument("--skip-deep-link-check", action="store_true")
    ap.add_argument("--require-deep-links", action="store_true", default=True)
    ap.add_argument("--no-require-deep-links", action="store_false", dest="require_deep_links")
    ap.add_argument("--force-fetch", action="store_true", help="Attempt fetch even if probe failed")
    ap.add_argument("--strict", action="store_true", help="Exit non-zero on validation failures")
    ap.add_argument("--toc-limit", type=int, default=None, help="Cap TOC topics per product (debug)")
    ap.add_argument(
        "--phase",
        choices=("all", "discover", "fetch", "deep-links", "sanitize", "toc", "report"),
        default="all",
    )
    args = ap.parse_args()

    discovery: dict = {}
    if args.phase in ("all", "discover", "fetch", "report") and not args.skip_probe:
        disc_path = ARTIFACTS / "discovery.json"
        if args.phase != "discover" and disc_path.is_file() and args.phase == "all":
            discovery = json.loads(disc_path.read_text(encoding="utf-8"))
            print(f"loaded {disc_path}")
        else:
            discovery = phase_discover(args)
    elif (ARTIFACTS / "discovery.json").is_file():
        discovery = json.loads((ARTIFACTS / "discovery.json").read_text(encoding="utf-8"))

    fetch_manifest: dict = {"fetched": [], "unfetchable": [], "roots_fetched": 0, "total_bytes": 0}
    if args.phase in ("all", "fetch", "sanitize", "toc", "report") and not args.skip_fetch:
        manifest_path = ROOT / "raw" / args.stamp_date / "manifest.json"
        if args.phase not in ("fetch", "all") and manifest_path.is_file():
            fetch_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        else:
            fetch_manifest = phase_fetch(discovery, args)
    elif (ROOT / "raw" / args.stamp_date / "manifest.json").is_file():
        fetch_manifest = json.loads(
            (ROOT / "raw" / args.stamp_date / "manifest.json").read_text(encoding="utf-8")
        )

    deep_check: dict = {}
    if args.phase in ("all", "deep-links") and not args.skip_deep_link_check:
        deep_check = phase_deep_link_check(args)
    elif (ARTIFACTS / "deep-link-spot-check.json").is_file():
        deep_check = json.loads(
            (ARTIFACTS / "deep-link-spot-check.json").read_text(encoding="utf-8")
        )

    sanitize_summary: dict = {"totals": {}, "products": []}
    sanitize_path = ARTIFACTS / "sanitize-summary.json"
    if args.phase in ("all", "sanitize") and not args.skip_sanitize:
        sanitize_summary = phase_sanitize(fetch_manifest, args)
    elif sanitize_path.is_file():
        sanitize_summary = json.loads(sanitize_path.read_text(encoding="utf-8"))

    toc_report: dict = {}
    toc_path = ARTIFACTS / "toc-completeness.json"
    if args.phase in ("all", "toc"):
        toc_report = phase_toc(fetch_manifest, args)
    elif toc_path.is_file():
        toc_report = json.loads(toc_path.read_text(encoding="utf-8"))

    if args.phase in ("all", "report"):
        phase_report(discovery, fetch_manifest, deep_check, sanitize_summary, toc_report, args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
