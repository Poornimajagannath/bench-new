#!/usr/bin/env python3
"""Milestone 0.5: immutable raw/<date>/ + schema-gated normalized/."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.ingest import (  # noqa: E402
    render_ingestion_report,
    run_ingestion_snapshot,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingestion snapshot (M0.5)")
    parser.add_argument(
        "--docs-dir", default=str(ROOT / "data/products/payments/guides")
    )
    parser.add_argument("--raw-root", default=str(ROOT / "raw"))
    parser.add_argument("--normalized-root", default=str(ROOT / "normalized"))
    parser.add_argument(
        "--openapi",
        default=str(
            ROOT / "data/content_engine/specs/cybersource-payments-core.openapi.json"
        ),
    )
    parser.add_argument("--stamp-date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument(
        "--sample-limit",
        type=int,
        default=500,
        help="Wave 1: cover the full payments guide set (not a sample)",
    )
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts/content_engine/payments/ingestion-report.md"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "artifacts/content_engine/payments/ingestion-report.json"),
    )
    parser.add_argument(
        "--quarantine-list",
        default=str(ROOT / "artifacts/content_engine/corpus/quarantine-list.json"),
        help="Census quarantine-list.json; paths listed are skipped (policy)",
    )
    parser.add_argument(
        "--recall-baseline",
        default=None,
        help=(
            "Named frozen baseline (markdown drop list) for the recall "
            "section; 'none' to skip. Default: Wave 1 payments evidence, "
            "auto-skipped for boarding docs dirs."
        ),
    )
    parser.add_argument(
        "--census-report",
        default=None,
        help=(
            "census-report.json — when given, the census-eligible set is the "
            "single ingestion input (one corpus definition); the quarantine "
            "list flag is ignored"
        ),
    )
    args = parser.parse_args()

    quar = Path(args.quarantine_list)
    census = Path(args.census_report) if args.census_report else None
    report = run_ingestion_snapshot(
        docs_dir=Path(args.docs_dir),
        raw_root=Path(args.raw_root),
        normalized_root=Path(args.normalized_root),
        openapi_path=Path(args.openapi),
        stamp_date=args.stamp_date,
        sample_limit=args.sample_limit,
        quarantine_list_path=None if census else (quar if quar.is_file() else None),
        census_report_path=census,
    )

    # Recall vs a NAMED frozen baseline. The default baseline is Wave 1
    # payments evidence — only meaningful for the payments corpus. Pass
    # --recall-baseline for other products, or "none" to skip; a recall number
    # against the wrong product's baseline is worse than no number.
    prior_paths: set[str] = set()
    if args.recall_baseline == "none":
        evidence_drops = Path("/nonexistent")
    elif args.recall_baseline:
        evidence_drops = Path(args.recall_baseline)
        if not evidence_drops.is_absolute():
            evidence_drops = ROOT / evidence_drops
    else:
        evidence_drops = ROOT / "evals/evidence/wave1-payments/top-20-drops.md"
        if "boarding" in str(args.docs_dir):
            evidence_drops = Path("/nonexistent")  # wrong-product default guard
    if evidence_drops.is_file():
        for line in evidence_drops.read_text(encoding="utf-8").splitlines():
            # e.g. `1. `2026-08-07/….md` — no_schema_match — …`
            if "no_schema_match" not in line:
                continue
            for part in line.split("`"):
                if part.endswith(".md") or part.endswith(".md.md"):
                    prior_paths.add(Path(part).name)
                    break
    prior_json = ROOT / "artifacts/content_engine/payments/prior-no-schema-match.json"
    if not prior_paths and prior_json.is_file():
        prior_paths = set(json.loads(prior_json.read_text(encoding="utf-8")))
    if prior_paths:
        claims_file = Path(report["normalized_file"])
        if not claims_file.is_absolute():
            claims_file = ROOT / claims_file
        claimed: set[str] = set()
        if claims_file.is_file():
            payload = json.loads(claims_file.read_text(encoding="utf-8"))
            for c in payload.get("claims") or []:
                claimed.add(Path(str(c.get("source_pointer") or "")).name)
        recovered = sorted(prior_paths & claimed)
        still_names = sorted(prior_paths - claimed)
        report["recall"] = {
            "prior_no_schema_match": len(prior_paths),
            "recovered": len(recovered),
            "still_dropped": len(still_names),
            "recovered_names": recovered,
            "still_dropped_names": still_names,
            "baseline": str(
                evidence_drops.relative_to(ROOT)
                if evidence_drops.is_file()
                else prior_json
            ),
        }

    # Human-check sample: up to 10 drops with triage fields (not filename labels).
    # Prefer shell, then no_schema_match, then other — always include bytes/heading.
    drops_all = list(report.get("drops") or [])
    preferred = [d for d in drops_all if d.get("reason") == "shell"]
    preferred += [d for d in drops_all if d.get("reason") == "no_schema_match" and d not in preferred]
    preferred += [d for d in drops_all if d not in preferred]
    report["human_check_sample"] = [
        {
            "path": d.get("path"),
            "reason": d.get("reason"),
            "bytes": d.get("bytes"),
            "first_heading": d.get("first_heading"),
            "detail": d.get("detail"),
        }
        for d in preferred[:10]
    ]

    md = render_ingestion_report(report)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    Path(args.json_out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    # Top drops skim with shell triage columns
    top = out.parent / "top-drops.md"
    lines = [
        "# Ingestion top drops (skim)",
        "",
        f"Total drops: {report['drop_count']}",
        "",
        "## Reason counts",
        "",
    ]
    from collections import Counter

    reasons = Counter(d["reason"] for d in report.get("drops") or [])
    for k, v in reasons.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "## Drops", ""]
    for i, d in enumerate((report.get("drops") or [])[:20], 1):
        extra = ""
        if d.get("reason") == "shell":
            extra = f" — bytes={d.get('bytes')} — heading={d.get('first_heading')!r}"
        lines.append(
            f"{i}. `{d['path']}` — {d['reason']} — {d.get('detail') or ''}{extra}"
        )
    if report.get("recall"):
        r = report["recall"]
        lines += [
            "",
            "## Recall vs prior no_schema_match",
            "",
            f"Recovered **{r['recovered']}** / {r['prior_no_schema_match']} previously empty pages.",
        ]
    top.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {out}")
    print(
        f"Fetched={report['docs_fetched']} claims={report['claims_extracted']} "
        f"drops={report['drop_count']}"
    )
    if report.get("recall"):
        print(
            f"Recall: recovered {report['recall']['recovered']}/"
            f"{report['recall']['prior_no_schema_match']} prior no_schema_match"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
