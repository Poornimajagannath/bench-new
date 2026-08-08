#!/usr/bin/env python3
"""Prompt A + B: soft-gap findings, product-root census, Wave 1+2 rerun reports.

Stops after the reports. Does not start Wave 3.
Every number carries its denominator and source.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.api_reference import (  # noqa: E402
    extract_api_reference_claims,
    summarize_reports,
)
from content_bench.content_engine.humanizer import (  # noqa: E402
    assert_facts_unchanged,
    humanize,
)
from content_bench.content_engine.ingest import _extract_claims_from_text  # noqa: E402
from content_bench.content_engine.reference_pages import (  # noqa: E402
    write_reference_pages_from_endpoint_facts,
)
from content_bench.content_engine.workflow_pages import compose_all  # noqa: E402

OPENAPI = ROOT / "data" / "content_engine" / "specs" / "payments-core.openapi.json"
PRODUCT_ROOTS = ROOT / "raw" / "product-roots"
PRODUCT_ROOTS_REPORT = (
    ROOT / "artifacts" / "content_engine" / "product_roots" / "product-roots-report.json"
)
BOARDING_CLAIMS = ROOT / "normalized" / "2026-08-08-boarding.claims.json"
OUT_DIR = ROOT / "artifacts" / "content_engine" / "wave_rerun"


def _utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def collect_soft_gaps() -> Dict[str, Any]:
    reports = []
    findings: List[Dict[str, Any]] = []
    for path in sorted(PRODUCT_ROOTS.glob("*.md.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        _, report, _ = extract_api_reference_claims(
            text,
            source_pointer=path.name,
            doc_stem=path.stem.replace(".md", ""),
        )
        reports.append(report)
        for g in report.soft_gaps:
            findings.append(g.to_dict())

    findings.sort(key=lambda r: (r["product_id"], r["path"], r["method"]))
    no_rf = [f for f in findings if f["missing_required_fields"]]
    no_ex = [f for f in findings if f["missing_rest_example"]]
    both = [
        f
        for f in findings
        if f["missing_required_fields"] and f["missing_rest_example"]
    ]
    summary = summarize_reports(reports)
    return {
        "generated_at": _utc(),
        "denominator": {
            "matched_endpoint_sections": summary["matched"],
            "source": "api_reference.extract_api_reference_claims over raw/product-roots",
        },
        "counts": {
            "missing_required_fields": len(no_rf),
            "missing_rest_example": len(no_ex),
            "missing_both": len(both),
        },
        "by_product_missing_required_fields": dict(
            Counter(f["product_id"] for f in no_rf)
        ),
        "by_product_missing_rest_example": dict(Counter(f["product_id"] for f in no_ex)),
        "findings_missing_required_fields": no_rf,
        "findings_missing_rest_example": no_ex,
        "findings_missing_both": both,
        "pattern_scan": summary,
    }


def render_soft_gap_md(payload: Dict[str, Any]) -> str:
    d = payload["denominator"]["matched_endpoint_sections"]
    src = payload["denominator"]["source"]
    lines = [
        "# Developers can see the endpoint and still cannot call it",
        "",
        "Matched Endpoint sections that document a verb+URL but omit the "
        "Required Fields list and/or a REST Example leave a partner unable to "
        "form a valid request. These are gap-report findings, not extractor warnings.",
        "",
        f"Denominator: **{d}** matched Endpoint sections "
        f"(source: `{src}`).",
        "",
        f"- Missing Required Fields: **{payload['counts']['missing_required_fields']}** / {d}",
        f"- Missing REST Example: **{payload['counts']['missing_rest_example']}** / {d}",
        f"- Missing both: **{payload['counts']['missing_both']}** / {d}",
        "",
        "## Endpoints with no Required Fields list",
        "",
        "| Product | Method | Path | Deep link |",
        "|---|---|---|---|",
    ]
    for f in payload["findings_missing_required_fields"]:
        link = f.get("deep_link") or ""
        lines.append(
            f"| {f['product_id']} | `{f['method']}` | `{f['path']}` | {link} |"
        )
    lines += [
        "",
        "## Endpoints with no REST Example",
        "",
        "| Product | Method | Path | Deep link |",
        "|---|---|---|---|",
    ]
    for f in payload["findings_missing_rest_example"]:
        link = f.get("deep_link") or ""
        lines.append(
            f"| {f['product_id']} | `{f['method']}` | `{f['path']}` | {link} |"
        )
    lines += [
        "",
        "## Endpoints missing both",
        "",
        "| Product | Method | Path | Deep link |",
        "|---|---|---|---|",
    ]
    for f in payload["findings_missing_both"]:
        link = f.get("deep_link") or ""
        lines.append(
            f"| {f['product_id']} | `{f['method']}` | `{f['path']}` | {link} |"
        )
    lines.append("")
    return "\n".join(lines)


def product_roots_summary() -> Dict[str, Any]:
    data = json.loads(PRODUCT_ROOTS_REPORT.read_text(encoding="utf-8"))
    products = data.get("products") or []
    derivations = data.get("derivations") or []
    return {
        "generated_at": data.get("generated_at"),
        "denominator_source": data.get("denominator_source"),
        "totals": data.get("totals"),
        "resolved": [
            {
                "title": p.get("title"),
                "product_id": p.get("product_id"),
                "root_path": p.get("root_path"),
                "bytes": p.get("bytes"),
                "sections_split": p.get("sections_split"),
                "toc_topics": p.get("toc_topics"),
                "toc_covered": p.get("toc_covered"),
                "toc_gaps": len(p.get("toc_uncovered") or []),
                "toc_uncovered": p.get("toc_uncovered") or [],
            }
            for p in products
            if p.get("local_path")
        ],
        "failed_derivation": [
            {
                "title": d.get("title"),
                "intro_path": d.get("intro_path"),
                "derivation": d.get("derivation"),
                "family_repeat_root": d.get("family_repeat_root"),
                "guide_dir_root": d.get("guide_dir_root"),
            }
            for d in derivations
            if not d.get("resolves")
        ],
        "source": str(PRODUCT_ROOTS_REPORT.relative_to(ROOT)),
    }


def render_product_roots_md(summary: Dict[str, Any]) -> str:
    totals = summary["totals"] or {}
    lines = [
        "# Prompt 1 — product-root fetch across docs.md",
        "",
        f"Generated (original fetch): {summary.get('generated_at')}",
        f"Denominator source: `{summary.get('denominator_source')}` "
        f"(source file: `{summary['source']}`).",
        "",
        f"- Products listed: **{totals.get('products_listed')}**",
        f"- Roots resolved/fetched: **{totals.get('roots_fetched')}** / "
        f"{totals.get('products_listed')}",
        f"- Bytes (sum of roots): **{totals.get('bytes')}**",
        f"- Sections split: **{totals.get('sections_split')}**",
        f"- TOC topics checked: **{totals.get('toc_topics')}** "
        f"(covered {totals.get('toc_covered')}, gaps {totals.get('toc_uncovered')})",
        "",
        "## Per product",
        "",
        "| Product | Root | Bytes | Sections | TOC covered | TOC gaps |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for p in summary["resolved"]:
        lines.append(
            f"| {p['title']} | `{p['root_path']}` | {p['bytes']} | "
            f"{p['sections_split']} | {p['toc_covered']}/{p['toc_topics']} | "
            f"{p['toc_gaps']} |"
        )
    lines += ["", "## Failed derivation", ""]
    if not summary["failed_derivation"]:
        lines.append("None.")
    else:
        for d in summary["failed_derivation"]:
            lines.append(
                f"- **{d['title']}** (`{d['derivation']}`): intro `{d['intro_path']}`"
            )
    lines += ["", "## TOC pages not covered by root", ""]
    any_gap = False
    for p in summary["resolved"]:
        if not p["toc_uncovered"]:
            continue
        any_gap = True
        lines.append(f"### {p['title']}")
        lines.append("")
        for t in p["toc_uncovered"]:
            lines.append(f"- `{t}`")
        lines.append("")
    if not any_gap:
        lines.append("None.")
        lines.append("")
    return "\n".join(lines)


def _normalize_pts_path(path: str) -> str:
    p = path.rstrip("/")
    # Collapse trailing empty segment variants for coverage compare.
    return p


def wave1_payments() -> Dict[str, Any]:
    payments_root = PRODUCT_ROOTS / "en-us_payments_developer_ctv_rest_payments.md.md"
    text = payments_root.read_text(encoding="utf-8", errors="replace")
    claims, _ = _extract_claims_from_text(
        text,
        source_pointer=payments_root.name,
        doc_stem="payments",
    )
    claim_dicts = [c.to_dict() for c in claims]
    eps = [c for c in claim_dicts if c["schema"] == "endpoint_fact"]
    pts_eps = [
        c
        for c in eps
        if (c.get("extras") or {}).get("path", "").startswith("/pts/")
    ]

    summary = write_reference_pages_from_endpoint_facts(
        claim_dicts,
        content_dir=ROOT / "content",
        artifact_dir=ROOT / "artifacts" / "content_engine" / "a2",
        path_prefix="/pts/",
    )

    oa = json.loads(OPENAPI.read_text(encoding="utf-8"))
    pts_ops = []
    for path, methods in (oa.get("paths") or {}).items():
        if not str(path).startswith("/pts/"):
            continue
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.startswith("x-") or not isinstance(op, dict):
                continue
            pts_ops.append(
                {
                    "method": method.upper(),
                    "path": path,
                    "operation_id": op.get("operationId"),
                }
            )

    guide_keys = {
        (
            (c.get("extras") or {}).get("method"),
            _normalize_pts_path((c.get("extras") or {}).get("path") or ""),
        )
        for c in pts_eps
    }

    def covered(op: Dict[str, Any]) -> bool:
        m, p = op["method"], _normalize_pts_path(op["path"])
        if (m, p) in guide_keys:
            return True
        # Allow guide paths that omit `{id}` segments when the stem matches.
        stem = re.sub(r"\{[^}]+\}", "", p).rstrip("/")
        for gm, gp in guide_keys:
            if gm != m:
                continue
            if _normalize_pts_path(gp) == p:
                return True
            gstem = re.sub(r"\{[^}]+\}", "", gp).rstrip("/")
            if stem and (stem == gstem or stem.startswith(gstem) or gstem.startswith(stem)):
                return True
        return False

    coverage = []
    for op in pts_ops:
        coverage.append({**op, "covered_by_endpoint_fact": covered(op)})

    covered_n = sum(1 for c in coverage if c["covered_by_endpoint_fact"])
    return {
        "generated_at": _utc(),
        "source_root": str(payments_root.relative_to(ROOT)),
        "endpoint_facts_in_root": len(eps),
        "endpoint_facts_pts": len(pts_eps),
        "pages_written": summary["count"],
        "page_names": summary["pages_written"],
        "lineage": summary["lineage_origin"],
        "pts_denominator": {
            "count": len(pts_ops),
            "source": str(OPENAPI.relative_to(ROOT)),
            "rule": "OpenAPI paths under /pts/",
        },
        "pts_covered": covered_n,
        "pts_coverage_ratio": f"{covered_n}/{len(pts_ops)}",
        "operations": coverage,
        "guide_unique_pts_method_path": sorted(
            {f"{m} {p}" for m, p in guide_keys if m and p}
        ),
    }


def wave2_boarding() -> Dict[str, Any]:
    # Ensure mega-guide in boarding raw is current, re-normalize, compose.
    from content_bench.content_engine.ingest import normalize_raw_dir

    raw = ROOT / "raw" / "2026-08-08-boarding"
    src = PRODUCT_ROOTS / "en-us_boarding_developer_all_rest_boarding.md.md"
    if src.is_file() and raw.is_dir():
        (raw / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    claims, drops = normalize_raw_dir(raw, openapi_path=None)
    result = compose_all(
        BOARDING_CLAIMS,
        out_dir=ROOT / "content" / "boarding" / "workflows",
    )
    # Humanize with fact-hash guard
    for page in result["pages"]:
        path = ROOT / page["path"]
        original = path.read_text(encoding="utf-8")
        updated = humanize(original)
        assert_facts_unchanged(original, updated)
        path.write_text(updated, encoding="utf-8")
        page["fact_hash_guard"] = "pass"

    seq = result["sequence_totals"]
    return {
        "generated_at": _utc(),
        "claims_file": str(BOARDING_CLAIMS.relative_to(ROOT)),
        "claims_total": result["claims_total"],
        "claims_after_prefer_child": result["claims_after_prefer_child"],
        "mega_residuals": result["mega_residuals"],
        "drops_on_renormalize": len(drops),
        "endpoint_facts": sum(1 for c in claims if c.schema == "endpoint_fact"),
        "api_reference_facts": sum(
            1
            for c in claims
            if c.schema == "endpoint_fact"
            and (c.extras or {}).get("pattern") == "api_reference"
        ),
        "sequence": seq,
        "outcome_gap": {
            "numerator": seq["outcome_gaps"],
            "denominator": seq["steps"],
            "ratio": f"{seq['outcome_gaps']}/{seq['steps']}",
            "source": "composed workflow sequence_stats "
            "(API ops + UI steps; expected outcome Gap markers)",
            "prior_wave2": {
                "ratio": "220/257",
                "note": "Measured before endpoint extraction; UI-only step count.",
            },
        },
        "pages": result["pages"],
    }


def patch_boarding_gap_report(
    soft: Dict[str, Any], wave2: Dict[str, Any]
) -> Path:
    gap_path = ROOT / "artifacts" / "content_engine" / "boarding" / "gap-report.md"
    soft_md = render_soft_gap_md(soft)
    og = wave2["outcome_gap"]
    seq = wave2["sequence"]
    headline = (
        f"**1. Stated outcomes are still mostly missing after API extraction.** "
        f"Of **{og['denominator']}** sequence steps across the six composed "
        f"workflows (API operations + UI steps), **{og['numerator']}** have no "
        f"stated outcome "
        f"(denominator: {og['denominator']} steps; source: `{og['source']}`). "
        f"Prior Wave 2 figure was {og['prior_wave2']['ratio']} "
        f"({og['prior_wave2']['note']}). "
        f"Sequence mix: {seq['api_ops']} API ops + {seq['ui_steps']} UI steps."
    )
    # Prepend soft-gap section + replace headline 1 outcome text.
    existing = gap_path.read_text(encoding="utf-8") if gap_path.is_file() else ""
    # Write a wave-rerun gap addendum that stands alone + update main gap report head.
    addendum = ROOT / "artifacts" / "content_engine" / "boarding" / "gap-report-wave-rerun.md"
    body = [
        "# Wave 2 boarding — gap report (post endpoint extraction)",
        "",
        f"Generated: {wave2['generated_at']}",
        "",
        "## The headline finding that changed shape",
        "",
        headline,
        "",
        f"- API ops in sequence: **{seq['api_ops']}** "
        f"(source: composition sequence_stats)",
        f"- UI steps in sequence: **{seq['ui_steps']}**",
        f"- Outcome gaps: **{og['ratio']}**",
        "",
        "## Per workflow",
        "",
        "| Workflow | Steps | Outcome gaps | API ops | UI steps |",
        "|---|---:|---:|---:|---:|",
    ]
    for p in wave2["pages"]:
        body.append(
            f"| {p['workflow_id']} | {p['steps']} | {p['outcome_gaps']} | "
            f"{p['api_ops']} | {p['ui_steps']} |"
        )
    body += ["", "---", "", soft_md]
    addendum.write_text("\n".join(body), encoding="utf-8")

    # Also splice soft-gap section into the standing gap-report.
    marker = "## Developers can see the endpoint and still cannot call it"
    if marker in existing:
        pre = existing.split(marker)[0].rstrip()
        # drop old soft section through next ## or end — simpler: append at end if missing structure
        new_existing = pre + "\n\n" + soft_md
    else:
        new_existing = existing.rstrip() + "\n\n---\n\n" + soft_md
    # Update the 220/257 sentence if present.
    new_existing = re.sub(
        r"Of 257 procedural steps in the six composed workflows, \*\*220 have no\nstated outcome\*\*[^\n]*",
        f"Of {og['denominator']} sequence steps in the six composed workflows "
        f"(API + UI), **{og['numerator']} have no stated outcome**",
        new_existing,
    )
    gap_path.write_text(new_existing + "\n", encoding="utf-8")
    return addendum


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    soft = collect_soft_gaps()
    (OUT_DIR / "soft-gap-findings.json").write_text(
        json.dumps(soft, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "soft-gap-findings.md").write_text(
        render_soft_gap_md(soft), encoding="utf-8"
    )

    roots = product_roots_summary()
    (OUT_DIR / "product-roots-all-products.md").write_text(
        render_product_roots_md(roots), encoding="utf-8"
    )
    (OUT_DIR / "product-roots-all-products.json").write_text(
        json.dumps(roots, indent=2) + "\n", encoding="utf-8"
    )

    w1 = wave1_payments()
    (OUT_DIR / "wave1-payments-report.json").write_text(
        json.dumps(w1, indent=2) + "\n", encoding="utf-8"
    )
    w1_md = [
        "# Wave 1 payments rerun — reference pages from endpoint_facts",
        "",
        f"Generated: {w1['generated_at']}",
        "",
        f"Source root: `{w1['source_root']}`",
        f"endpoint_fact claims in root: **{w1['endpoint_facts_in_root']}**",
        f"of which path `/pts/…`: **{w1['endpoint_facts_pts']}**",
        f"Pages written: **{w1['pages_written']}** (lineage: {w1['lineage']})",
        "",
        "## /pts/ coverage",
        "",
        f"Denominator: **{w1['pts_denominator']['count']}** OpenAPI operations "
        f"under `/pts/` (source: `{w1['pts_denominator']['source']}`).",
        f"Covered by guide `endpoint_fact`: **{w1['pts_coverage_ratio']}**.",
        "",
        "| Method | Path | operationId | Covered |",
        "|---|---|---|---|",
    ]
    for op in w1["operations"]:
        w1_md.append(
            f"| `{op['method']}` | `{op['path']}` | `{op['operation_id']}` | "
            f"{'yes' if op['covered_by_endpoint_fact'] else 'no'} |"
        )
    w1_md += [
        "",
        "Guide unique `/pts/` method+path keys "
        f"(source: payments product root extraction): **{len(w1['guide_unique_pts_method_path'])}**",
        "",
    ]
    for k in w1["guide_unique_pts_method_path"]:
        w1_md.append(f"- `{k}`")
    w1_md.append("")
    (OUT_DIR / "wave1-payments-report.md").write_text(
        "\n".join(w1_md), encoding="utf-8"
    )

    w2 = wave2_boarding()
    (OUT_DIR / "wave2-boarding-report.json").write_text(
        json.dumps(w2, indent=2) + "\n", encoding="utf-8"
    )
    addendum = patch_boarding_gap_report(soft, w2)

    og = w2["outcome_gap"]
    w2_md = [
        "# Wave 2 boarding rerun — one-sequence workflows",
        "",
        f"Generated: {w2['generated_at']}",
        "",
        f"Claims file: `{w2['claims_file']}` "
        f"(**{w2['claims_total']}** claims; source: renormalize + compose).",
        f"api_reference endpoint_facts in boarding raw: **{w2['api_reference_facts']}**",
        "",
        "## Outcome gap (the number)",
        "",
        f"**{og['ratio']}** sequence steps lack a stated outcome.",
        f"Denominator: **{og['denominator']}** steps "
        f"({w2['sequence']['api_ops']} API + {w2['sequence']['ui_steps']} UI); "
        f"source: `{og['source']}`.",
        f"Prior figure: {og['prior_wave2']['ratio']} — {og['prior_wave2']['note']}",
        "",
        "## Per workflow",
        "",
        "| Workflow | Steps | Outcome gaps | API | UI |",
        "|---|---:|---:|---:|---:|",
    ]
    for p in w2["pages"]:
        w2_md.append(
            f"| {p['workflow_id']} | {p['steps']} | {p['outcome_gaps']} | "
            f"{p['api_ops']} | {p['ui_steps']} |"
        )
    w2_md += ["", f"Gap addendum: `{addendum.relative_to(ROOT)}`", ""]
    (OUT_DIR / "wave2-boarding-report.md").write_text(
        "\n".join(w2_md), encoding="utf-8"
    )

    # Index
    index = [
        "# Wave rerun reports (stop — no Wave 3)",
        "",
        f"Generated: {_utc()}",
        "",
        "## Numbers",
        "",
        f"- Soft gaps missing Required Fields: "
        f"**{soft['counts']['missing_required_fields']}** / "
        f"{soft['denominator']['matched_endpoint_sections']} matched Endpoint sections",
        f"- Soft gaps missing REST Example: "
        f"**{soft['counts']['missing_rest_example']}** / "
        f"{soft['denominator']['matched_endpoint_sections']}",
        f"- Soft gaps missing both: **{soft['counts']['missing_both']}** / "
        f"{soft['denominator']['matched_endpoint_sections']}",
        f"- Product roots fetched: **{roots['totals']['roots_fetched']}** / "
        f"{roots['totals']['products_listed']} docs.md products",
        f"- Wave 1 /pts/ coverage: **{w1['pts_coverage_ratio']}** "
        f"(denominator: OpenAPI `/pts/` ops)",
        f"- Wave 2 outcome gaps: **{og['ratio']}** "
        f"(denominator: composed API+UI sequence steps)",
        "",
        "## Artifacts",
        "",
        "- `soft-gap-findings.md`",
        "- `product-roots-all-products.md`",
        "- `wave1-payments-report.md`",
        "- `wave2-boarding-report.md`",
        "- `../boarding/gap-report-wave-rerun.md`",
        "",
    ]
    (OUT_DIR / "README.md").write_text("\n".join(index), encoding="utf-8")

    print(f"soft_gaps rf={soft['counts']['missing_required_fields']} "
          f"ex={soft['counts']['missing_rest_example']} "
          f"both={soft['counts']['missing_both']} "
          f"/ {soft['denominator']['matched_endpoint_sections']}")
    print(f"product_roots {roots['totals']['roots_fetched']}/"
          f"{roots['totals']['products_listed']}")
    print(f"wave1 pts {w1['pts_coverage_ratio']} pages={w1['pages_written']}")
    print(f"wave2 outcome_gap {og['ratio']} "
          f"(api={w2['sequence']['api_ops']} ui={w2['sequence']['ui_steps']})")
    print("STOP — no Wave 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
