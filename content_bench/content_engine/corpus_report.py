"""Render corpus build reports with denominators and split unfetchable buckets."""

from __future__ import annotations

from typing import Any, Dict, List, Sequence


def render_corpus_report_md(payload: Dict[str, Any]) -> str:
    disc = payload.get("discovery", {})
    fetch = payload.get("fetch", {})
    toc = payload.get("toc", {})
    sanitize = payload.get("sanitize", {})
    deep = payload.get("deep_link_spot_check", {})

    lines = [
        "# Developer corpus build report",
        "",
        f"Generated: {payload.get('generated_at', '—')}",
        f"Stamp date: `{payload.get('stamp_date', '—')}`",
        "",
        "## Discovery (denominator)",
        "",
        f"Source: `{disc.get('denominator_source', 'llms.txt_derived_roots')}`",
        "",
        str(disc.get("denominator_rule", "")),
        "",
        f"- llms.txt `.md` URLs: **{disc.get('llms_md_urls', 0)}**",
        f"- llms.txt `.pdf` URLs: **{disc.get('llms_pdf_urls', 0)}** (recorded unfetchable)",
        f"- Roots discovered (denominator): **{disc.get('roots_discovered', 0)}**",
        f"- From llms.txt: **{disc.get('roots_from_llms', 0)}**",
        f"- docs.md-only supplements: **{len(disc.get('roots_from_docs_only') or [])}**",
        "",
    ]

    docs_only = disc.get("roots_from_docs_only") or []
    if docs_only:
        lines += ["### Families docs.md added that llms.txt missed", ""]
        for r in docs_only:
            lines.append(f"- `{r}`")
        lines.append("")

    # Derivation accuracy
    lines += [
        "## Derivation rule accuracy",
        "",
        "Separate success rates for family-repeat vs guide-dir fallback.",
        "",
        "| Rule | Discovered | Fetched OK | Unfetchable | Success rate |",
        "|---|---:|---:|---:|---:|",
    ]
    stats = disc.get("derivation_stats") or {}
    for rule, s in sorted(stats.items()):
        discovered = s.get("discovered", 0)
        ok = s.get("fetched_ok", 0)
        bad = s.get("unfetchable", 0)
        rate = f"{100 * ok / discovered:.1f}%" if discovered else "—"
        lines.append(f"| `{rule}` | {discovered} | {ok} | {bad} | {rate} |")
    lines.append("")

    # Split unfetchable
    lines += [
        "## Unfetchable roots (split buckets)",
        "",
        "404 on a constructed URL is **derivation_error** (ours). "
        "500 on an exposed URL is **site_defect** (theirs). "
        "**empty_200** is its own diagnosis.",
        "",
        "| Bucket | Count |",
        "|---|---:|",
    ]
    for bucket, n in sorted((disc.get("unfetchable_by_bucket") or {}).items()):
        lines.append(f"| {bucket} | {n} |")
    lines += ["", "| Reason | Count |", "|---|---:|"]
    for reason, n in sorted((disc.get("unfetchable_by_reason") or {}).items()):
        lines.append(f"| `{reason}` | {n} |")
    lines.append("")

    unfetchable = fetch.get("unfetchable") or []
    if unfetchable:
        lines += ["### Unfetchable detail", ""]
        for row in unfetchable[:30]:
            lines.append(
                f"- `{row.get('root_path')}` — **{row.get('unfetchable_reason')}** "
                f"({row.get('unfetchable_bucket')}) derivation=`{row.get('derivation')}` "
                f"HTTP {row.get('http_status')}"
            )
        if len(unfetchable) > 30:
            lines.append(f"- … and {len(unfetchable) - 30} more (see corpus-report.json)")
        lines.append("")

    # Deep link spot check
    if deep:
        lines += [
            "## Deep link spot check",
            "",
            f"Checked: **{deep.get('checked', 0)}** — "
            f"anchors found: **{deep.get('anchors_found', 0)}** / "
            f"{deep.get('checked', 0)} — "
            f"{'PASS' if deep.get('pass') else 'FAIL'}",
            "",
        ]
        for r in deep.get("results") or []:
            status = "ok" if r.get("anchor_found_in_html") else "MISSING"
            lines.append(
                f"- `{r.get('product_id')}` #{r.get('anchor')} → {status} "
                f"(HTML {r.get('html_status')})"
            )
        lines.append("")

    # Fetch totals
    lines += [
        "## Fetch",
        "",
        f"- Roots fetched OK: **{fetch.get('roots_fetched', 0)}** / "
        f"{disc.get('roots_discovered', 0)} (source: `raw/{payload.get('stamp_date')}/`)",
        f"- Total bytes: **{fetch.get('total_bytes', 0)}**",
        "",
    ]

    # Per product table
    products: List[Dict[str, Any]] = payload.get("products") or []
    if products:
        lines += [
            "## Per product",
            "",
            "| Product | Root fetched | Bytes | Sections | Quarantined | Code blocks | "
            "TOC topics | TOC covered | TOC missed |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
        for p in products:
            quar = sum((p.get("quarantined_by_kind") or {}).values())
            lines.append(
                f"| {p.get('product_id')} | "
                f"{'yes' if p.get('fetched') else 'no'} | "
                f"{p.get('bytes', 0)} | "
                f"{p.get('sections_total', 0)} | "
                f"{quar} | "
                f"{p.get('code_blocks', 0)} | "
                f"{p.get('toc_topics', 0)} | "
                f"{p.get('toc_covered', 0)} | "
                f"{len(p.get('toc_missed') or [])} |"
            )
        lines.append("")

    # TOC totals
    if toc:
        t = toc.get("totals") or {}
        lines += [
            "## TOC completeness",
            "",
            f"- Products checked: **{t.get('done', 0)}** / {t.get('products', 0)}",
            f"- TOC topics: **{t.get('toc_topics', 0)}**",
            f"- Covered: **{t.get('toc_covered', 0)}** / {t.get('toc_topics', 0)}",
            f"- Missed: **{t.get('toc_missed', 0)}**",
            "",
        ]

    # Sanitize totals
    if sanitize:
        lines += [
            "## Sanitize",
            "",
            f"- Sections total: **{sanitize.get('sections_total', 0)}**",
            f"- Sections clean: **{sanitize.get('sections_clean', 0)}** / "
            f"{sanitize.get('sections_total', 0)}",
            f"- Code blocks preserved: **{sanitize.get('code_blocks', 0)}**",
            "",
        ]
        by_kind = sanitize.get("quarantined_by_kind") or {}
        if by_kind:
            lines += ["| Quarantine kind | Sections |", "|---|---:|"]
            for k, n in sorted(by_kind.items()):
                lines.append(f"| `{k}` | {n} |")
            lines.append("")

    lines += [
        "## Source files",
        "",
        f"- Discovery: `artifacts/content_engine/corpus_build/discovery.json`",
        f"- Raw: `raw/{payload.get('stamp_date')}/`",
        f"- Cleaned: `cleaned/{payload.get('stamp_date')}/`",
        f"- Quarantine: `quarantine/{payload.get('stamp_date')}/`",
        f"- TOC checkpoint: `artifacts/content_engine/corpus_build/toc-checkpoint/`",
        "",
    ]
    return "\n".join(lines)
