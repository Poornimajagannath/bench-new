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
    load_reference_units,
    write_reference_pages,
)
from content_bench.content_engine.workflow_pages import (  # noqa: E402
    BOARDING_WORKFLOWS,
    compose_all,
    dedupe_prefer_child,
    _claims_for,
    _dedupe_endpoints,
)

# Wave 1 registered denominator (30 /pts/ ops). Fixture is engine-tests only.
OPENAPI_REGISTERED = (
    ROOT / "data" / "content_engine" / "specs" / "cybersource-payments.openapi.json"
)
OPENAPI_FIXTURE = ROOT / "data" / "content_engine" / "specs" / "payments-core.openapi.json"
REGISTERED_UNITS = (
    ROOT
    / "artifacts"
    / "content_engine"
    / "generated"
    / "cybersource-payments-openapi.api_reference_units.json"
)
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
    return path.rstrip("/")


def _pts_ops_from_spec(spec_path: Path) -> List[Dict[str, Any]]:
    oa = json.loads(spec_path.read_text(encoding="utf-8"))
    pts_ops: List[Dict[str, Any]] = []
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
    return pts_ops


def _guide_covers(op: Dict[str, Any], guide_keys: set) -> bool:
    m, p = op["method"], _normalize_pts_path(op["path"])
    if (m, p) in guide_keys:
        return True
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


def wave1_payments() -> Dict[str, Any]:
    """Regenerate reference pages from the registered OpenAPI (30 /pts/ ops).

    The prior wave-rerun mistakenly used the engine-test fixture
    ``payments-core.openapi.json`` (4 ops) and rendered pages from the
    payments *guide* endpoint_facts. Wave 1 closeout denominator is the
    registered spec — restore that path and report both numbers.
    """
    registered_ops = _pts_ops_from_spec(OPENAPI_REGISTERED)
    fixture_ops = _pts_ops_from_spec(OPENAPI_FIXTURE)

    units = load_reference_units(REGISTERED_UNITS)
    summary = write_reference_pages(
        units,
        content_dir=ROOT / "content",
        artifact_dir=ROOT / "artifacts" / "content_engine" / "a2",
        clear_existing=True,
        allow_endpoint_fact_lineage=False,
    )

    # Secondary: how many registered ops the payments product-root guide covers.
    payments_root = PRODUCT_ROOTS / "en-us_payments_developer_ctv_rest_payments.md.md"
    guide_keys: set = set()
    guide_pts_facts = 0
    if payments_root.is_file():
        claims, _ = _extract_claims_from_text(
            payments_root.read_text(encoding="utf-8", errors="replace"),
            source_pointer=payments_root.name,
            doc_stem="payments",
        )
        pts_eps = [
            c
            for c in claims
            if c.schema == "endpoint_fact"
            and (c.extras or {}).get("path", "").startswith("/pts/")
        ]
        guide_pts_facts = len(pts_eps)
        guide_keys = {
            (
                (c.extras or {}).get("method"),
                _normalize_pts_path((c.extras or {}).get("path") or ""),
            )
            for c in pts_eps
        }

    coverage = [
        {**op, "covered_by_guide_endpoint_fact": _guide_covers(op, guide_keys)}
        for op in registered_ops
    ]
    guide_covered = sum(1 for c in coverage if c["covered_by_guide_endpoint_fact"])

    return {
        "generated_at": _utc(),
        "explanation": (
            "The wave-rerun 3/4 figure used the engine-test fixture "
            f"({OPENAPI_FIXTURE.name}, {len(fixture_ops)} /pts/ ops) and generated "
            "pages from the payments product-root guide endpoint_facts — not the "
            "registered Wave 1 OpenAPI. Nothing was dropped from the real spec; "
            "the denominator source changed. This rerun restores the registered "
            f"spec ({OPENAPI_REGISTERED.name}, {len(registered_ops)} /pts/ ops) and "
            "regenerates reference pages from cybersource-payments-openapi units."
        ),
        "side_by_side": {
            "wave1_closeout": {
                "ratio": "30/30",
                "pages": 30,
                "denominator": 30,
                "source_file": str(OPENAPI_REGISTERED.relative_to(ROOT)),
                "evidence": "evals/evidence/wave1-payments/denominator-and-gaps.md",
                "registered_source_id": "cybersource-payments-openapi",
            },
            "mistaken_wave_rerun": {
                "ratio": "3/4",
                "pages": 38,
                "denominator": 4,
                "source_file": str(OPENAPI_FIXTURE.relative_to(ROOT)),
                "scope": "fixture /pts/ ops; pages from payments guide endpoint_facts",
                "note": (
                    "payments-core.openapi.json is labeled engine-tests only in "
                    "registry/payments.json — not the Wave 1 denominator."
                ),
            },
            "this_correction": {
                "ratio": f"{summary['count']}/{len(registered_ops)}",
                "pages": summary["count"],
                "denominator": len(registered_ops),
                "source_file": str(OPENAPI_REGISTERED.relative_to(ROOT)),
                "units_file": str(REGISTERED_UNITS.relative_to(ROOT)),
                "lineage": summary.get("lineage_origin"),
            },
        },
        "pages_written": summary["count"],
        "page_names": summary["pages_written"],
        "guide_secondary_coverage": {
            "registered_ops_covered_by_guide_endpoint_fact": guide_covered,
            "registered_ops_denominator": len(registered_ops),
            "ratio": f"{guide_covered}/{len(registered_ops)}",
            "guide_pts_endpoint_facts": guide_pts_facts,
            "guide_source": str(payments_root.relative_to(ROOT))
            if payments_root.is_file()
            else None,
            "note": (
                "Secondary metric only — Wave 1 gate remains pages vs registered "
                "OpenAPI ops, not guide coverage."
            ),
            "operations": coverage,
        },
    }


def _composition_eligibility(claims: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Explain 952 (all products) vs boarding-eligible vs used in the 6 workflows."""
    # Cross-product denominator from the extraction report (all product roots).
    extract_report = (
        ROOT
        / "artifacts"
        / "content_engine"
        / "api_reference"
        / "api-reference-extraction-report.json"
    )
    cross_product_total = None
    if extract_report.is_file():
        cross_product_total = json.loads(extract_report.read_text()).get(
            "after_api_reference_total"
        )

    kept, _ = dedupe_prefer_child(claims)
    boarding_api_ref = [
        c
        for c in kept
        if c.get("schema") == "endpoint_fact"
        and (c.get("extras") or {}).get("pattern") == "api_reference"
    ]

    # Unique operations by anchor (richest claim wins).
    by_anchor: Dict[str, Dict[str, Any]] = {}
    for c in boarding_api_ref:
        ex = c.get("extras") or {}
        a = ex.get("anchor") or c.get("claim_id")
        score = (
            1 if ex.get("required_fields") else 0,
            1 if ex.get("example_request") is not None else 0,
        )
        prev = by_anchor.get(a)
        if prev is None:
            by_anchor[a] = c
            continue
        prev_ex = prev.get("extras") or {}
        prev_score = (
            1 if prev_ex.get("required_fields") else 0,
            1 if prev_ex.get("example_request") is not None else 0,
        )
        if score > prev_score:
            by_anchor[a] = c

    per_wf = []
    used_anchors = set()
    matched_claim_instances = 0
    used_after_dedupe = 0
    for spec in BOARDING_WORKFLOWS:
        wf = _claims_for(spec, kept)
        api = [
            c
            for c in wf
            if c.get("schema") == "endpoint_fact"
            and (c.get("extras") or {}).get("pattern") == "api_reference"
        ]
        deduped = _dedupe_endpoints(api)
        matched_claim_instances += len(api)
        used_after_dedupe += len(deduped)
        for c in deduped:
            used_anchors.add((c.get("extras") or {}).get("anchor"))
        per_wf.append(
            {
                "workflow_id": spec.workflow_id,
                "matched_api_reference_claims": len(api),
                "used_after_dedupe": len(deduped),
                "doc_matchers": list(spec.doc_matchers),
            }
        )

    orphans = []
    for a, c in sorted(by_anchor.items()):
        if a in used_anchors:
            continue
        ex = c.get("extras") or {}
        orphans.append(
            {
                "anchor": a,
                "method": ex.get("method"),
                "path": ex.get("path"),
                "title": c.get("title"),
                "reason": "no_workflow_doc_matcher",
            }
        )

    excluded_claim_instances = matched_claim_instances - used_after_dedupe
    return {
        "cross_product_api_reference_claims": cross_product_total,
        "cross_product_source": str(extract_report.relative_to(ROOT))
        if extract_report.is_file()
        else None,
        "cross_product_note": (
            "952 spans every product root (payments, tms, …). It is not the "
            "boarding workflow eligibility pool."
        ),
        "boarding_api_reference_claims": len(boarding_api_ref),
        "boarding_unique_ops_by_anchor": len(by_anchor),
        "boarding_claims_source": "normalized/2026-08-08-boarding.claims.json "
        "(after prefer-child; api_reference pattern only)",
        "eligible_matched_claim_instances": matched_claim_instances,
        "used_in_sequence_after_dedupe": used_after_dedupe,
        "unique_ops_used": len(used_anchors),
        "unique_ops_orphan": len(orphans),
        "exclusion_breakdown": {
            "not_boarding_product": {
                "count": (cross_product_total or 0) - len(boarding_api_ref)
                if cross_product_total is not None
                else None,
                "reason": "api_reference claims on non-boarding product roots",
            },
            "duplicate_host_or_stub_collapsed": {
                "count": excluded_claim_instances,
                "reason": (
                    "prod+test host pairs and child Endpoint-stub pages collapsed "
                    "to one richest claim per operation anchor"
                ),
            },
            "no_workflow_doc_matcher": {
                "count": len(orphans),
                "reason": "boarding api_reference op whose anchor matched no workflow",
                "orphans": orphans,
            },
        },
        "per_workflow": per_wf,
        "composer_note": (
            "Composer already renders endpoint_fact as sequence API entries "
            "(method/path/required fields/example), not only quickstart_step. "
            "Underuse vs 952 was mostly cross-product scope + host/stub dedupe, "
            "not a step-only filter."
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
    claim_dicts = [c.to_dict() for c in claims]
    eligibility = _composition_eligibility(claim_dicts)

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
        "composition_eligibility": eligibility,
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
    sb = w1["side_by_side"]
    w1_md = [
        "# Wave 1 payments — denominator correction",
        "",
        f"Generated: {w1['generated_at']}",
        "",
        w1["explanation"],
        "",
        "## Side by side",
        "",
        "| Run | Ratio | Pages | Denominator | Source file |",
        "|---|---|---:|---:|---|",
        f"| Wave 1 closeout | {sb['wave1_closeout']['ratio']} | "
        f"{sb['wave1_closeout']['pages']} | {sb['wave1_closeout']['denominator']} | "
        f"`{sb['wave1_closeout']['source_file']}` |",
        f"| Mistaken wave rerun | {sb['mistaken_wave_rerun']['ratio']} | "
        f"{sb['mistaken_wave_rerun']['pages']} | {sb['mistaken_wave_rerun']['denominator']} | "
        f"`{sb['mistaken_wave_rerun']['source_file']}` |",
        f"| This correction | {sb['this_correction']['ratio']} | "
        f"{sb['this_correction']['pages']} | {sb['this_correction']['denominator']} | "
        f"`{sb['this_correction']['source_file']}` |",
        "",
        f"Evidence for closeout 30/30: `{sb['wave1_closeout']['evidence']}`.",
        f"Units used for correction: `{sb['this_correction']['units_file']}`.",
        "",
        "## Secondary: registered ops covered by payments guide endpoint_facts",
        "",
        f"**{w1['guide_secondary_coverage']['ratio']}** "
        f"(denominator: registered `/pts/` ops; source: "
        f"`{w1['guide_secondary_coverage']['guide_source']}`). "
        f"{w1['guide_secondary_coverage']['note']}",
        "",
        "| Method | Path | operationId | Guide endpoint_fact |",
        "|---|---|---|---|",
    ]
    for op in w1["guide_secondary_coverage"]["operations"]:
        w1_md.append(
            f"| `{op['method']}` | `{op['path']}` | `{op['operation_id']}` | "
            f"{'yes' if op['covered_by_guide_endpoint_fact'] else 'no'} |"
        )
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
    el = w2["composition_eligibility"]
    w2_md = [
        "# Wave 2 boarding rerun — one-sequence workflows",
        "",
        f"Generated: {w2['generated_at']}",
        "",
        f"Claims file: `{w2['claims_file']}` "
        f"(**{w2['claims_total']}** claims; source: renormalize + compose).",
        f"api_reference endpoint_facts in boarding corpus: **{w2['api_reference_facts']}**",
        "",
        "## Composition eligibility (952 vs 20)",
        "",
        el["composer_note"],
        "",
        f"- Cross-product api_reference claims: **{el['cross_product_api_reference_claims']}** "
        f"(source: `{el['cross_product_source']}`). {el['cross_product_note']}",
        f"- Boarding api_reference claims: **{el['boarding_api_reference_claims']}** "
        f"(source: `{el['boarding_claims_source']}`)",
        f"- Unique boarding ops (by anchor): **{el['boarding_unique_ops_by_anchor']}**",
        f"- Eligible matched claim instances (doc_matchers): "
        f"**{el['eligible_matched_claim_instances']}**",
        f"- Used in sequence after dedupe: **{el['used_in_sequence_after_dedupe']}**",
        f"- Unique ops used: **{el['unique_ops_used']}** / "
        f"{el['boarding_unique_ops_by_anchor']}",
        f"- Orphan ops (no matcher): **{el['unique_ops_orphan']}**",
        "",
        "### Why claims were excluded",
        "",
    ]
    for key, row in el["exclusion_breakdown"].items():
        w2_md.append(
            f"- `{key}`: **{row.get('count')}** — {row.get('reason')}"
        )
    if el["exclusion_breakdown"]["no_workflow_doc_matcher"].get("orphans"):
        w2_md.append("")
        w2_md.append("Orphans:")
        for o in el["exclusion_breakdown"]["no_workflow_doc_matcher"]["orphans"]:
            w2_md.append(
                f"  - `{o['anchor']}` — `{o['method']} {o['path']}` ({o['title']})"
            )
    w2_md += [
        "",
        "### Per workflow",
        "",
        "| Workflow | Matched api_reference claims | Used after dedupe |",
        "|---|---:|---:|",
    ]
    for row in el["per_workflow"]:
        w2_md.append(
            f"| {row['workflow_id']} | {row['matched_api_reference_claims']} | "
            f"{row['used_after_dedupe']} |"
        )
    w2_md += [
        "",
        "## Outcome gap (the number)",
        "",
        f"**{og['ratio']}** sequence steps lack a stated outcome.",
        f"Denominator: **{og['denominator']}** steps "
        f"({w2['sequence']['api_ops']} API + {w2['sequence']['ui_steps']} UI); "
        f"source: `{og['source']}`.",
        f"Prior figure: {og['prior_wave2']['ratio']} — {og['prior_wave2']['note']}",
        "",
        "## Per workflow (sequence)",
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
        f"- Wave 1 pages vs registered OpenAPI: "
        f"**{sb['this_correction']['ratio']}** "
        f"(source: `{sb['this_correction']['source_file']}`; "
        f"mistaken rerun was {sb['mistaken_wave_rerun']['ratio']} from fixture)",
        f"- Wave 2 outcome gaps: **{og['ratio']}** "
        f"(denominator: composed API+UI sequence steps)",
        f"- Boarding api_reference used in sequence: "
        f"**{el['used_in_sequence_after_dedupe']}** / "
        f"{el['boarding_unique_ops_by_anchor']} unique boarding ops "
        f"(cross-product pool was {el['cross_product_api_reference_claims']})",
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
    print(
        f"wave1 registered {sb['this_correction']['ratio']} "
        f"(mistaken was {sb['mistaken_wave_rerun']['ratio']})"
    )
    print(
        f"wave2 outcome_gap {og['ratio']} "
        f"(api={w2['sequence']['api_ops']} ui={w2['sequence']['ui_steps']}); "
        f"api_ref used {el['used_in_sequence_after_dedupe']}/"
        f"{el['boarding_unique_ops_by_anchor']} boarding ops"
    )
    print("STOP — no Wave 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
