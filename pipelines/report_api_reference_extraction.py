#!/usr/bin/env python3
"""Before/after report: API-reference endpoint_fact extraction on product roots."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.api_reference import (  # noqa: E402
    extract_api_reference_claims,
    summarize_reports,
)
from content_bench.content_engine.ingest import _extract_claims_from_text  # noqa: E402

# Legacy thin scanner (pre-api-reference) for the before count.
_THIN_EP = re.compile(
    r"\b(GET|POST|PUT|PATCH|DELETE)\b[`\s]*"
    r"((?:https?://[A-Za-z0-9.-]+)?)"
    r"[`\s]*"
    r"(/[A-Za-z0-9_{}/.-]+)"
)


def product_id(path: Path) -> str:
    name = path.name
    if name.endswith(".md.md"):
        name = name[: -len(".md.md")]
    # last path segment of the flattened name
    return name.rsplit("_", 1)[-1]


def thin_endpoint_count(text: str) -> int:
    seen = set()
    for m in _THIN_EP.finditer(text):
        method, host, path = m.group(1), m.group(2), m.group(3).rstrip(".")
        seen.add(f"{method}:{host}:{path}")
    return len(seen)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--roots-dir",
        type=Path,
        default=ROOT / "raw" / "product-roots",
    )
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "artifacts" / "content_engine" / "api_reference",
    )
    args = ap.parse_args()

    files = sorted(args.roots_dir.glob("*.md.md"))
    if not files:
        print(f"no roots in {args.roots_dir}", file=sys.stderr)
        return 1

    before_by: Counter = Counter()
    after_by: Counter = Counter()
    after_rich_by: Counter = Counter()
    reports = []
    per_product = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        pid = product_id(path)
        before = thin_endpoint_count(text)
        before_by[pid] += before

        claims, drops = _extract_claims_from_text(
            text,
            source_pointer=str(path.relative_to(ROOT))
            if path.is_relative_to(ROOT)
            else str(path),
            doc_stem=path.stem.replace(".md", ""),
        )
        eps = [c for c in claims if c.schema == "endpoint_fact"]
        rich = [
            c
            for c in eps
            if (c.extras or {}).get("pattern") == "api_reference"
        ]
        after_by[pid] += len(eps)
        after_rich_by[pid] += len(rich)

        _, report, _ = extract_api_reference_claims(
            text,
            source_pointer=path.name,
            doc_stem=path.stem.replace(".md", ""),
        )
        # Annotate soft gaps (matched but incomplete) for the skip table.
        soft = []
        if report.matched:
            missing_rf = report.matched - report.matched_with_required_fields
            missing_ex = report.matched - report.matched_with_example
            if missing_rf:
                soft.append(
                    {
                        "reason": "matched_without_required_fields",
                        "count": missing_rf,
                        "detail": "Endpoint+URL matched; no Required Fields list in span",
                    }
                )
            if missing_ex:
                soft.append(
                    {
                        "reason": "matched_without_rest_example",
                        "count": missing_ex,
                        "detail": "Endpoint+URL matched; no REST Example fences in span",
                    }
                )
        reports.append(report)
        per_product.append(
            {
                "product_id": pid,
                "file": path.name,
                "before_endpoint_fact": before,
                "after_endpoint_fact": len(eps),
                "after_api_reference": len(rich),
                "steps": sum(1 for c in claims if c.schema == "quickstart_step"),
                "scan": report.to_dict(),
                "soft_gaps": soft,
            }
        )

    summary = summarize_reports(reports)
    soft_counts: Counter = Counter()
    for row in per_product:
        for g in row["soft_gaps"]:
            soft_counts[g["reason"]] += g["count"]

    payload = {
        "denominator_source": "product_root",
        "roots_dir": str(args.roots_dir),
        "before_endpoint_fact_by_product": dict(before_by),
        "after_endpoint_fact_by_product": dict(after_by),
        "after_api_reference_by_product": dict(after_rich_by),
        "before_total": int(sum(before_by.values())),
        "after_total": int(sum(after_by.values())),
        "after_api_reference_total": int(sum(after_rich_by.values())),
        "pattern_scan": summary,
        "soft_gaps_by_reason": dict(soft_counts),
        "hard_skips_by_reason": summary.get("skipped_by_reason") or {},
        "products": per_product,
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    jp = args.out_dir / "api-reference-extraction-report.json"
    mp = args.out_dir / "api-reference-extraction-report.md"
    jp.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# API-reference extraction report",
        "",
        "Denominator: product roots in `raw/product-roots/`.",
        "",
        "## Before / after endpoint_fact counts",
        "",
        "| Product | Before (thin verb+URL) | After (all endpoint_fact) | Of which api_reference |",
        "|---|---:|---:|---:|",
    ]
    for pid in sorted(set(before_by) | set(after_by)):
        lines.append(
            f"| {pid} | {before_by[pid]} | {after_by[pid]} | {after_rich_by[pid]} |"
        )
    lines += [
        f"| **Total** | **{payload['before_total']}** | **{payload['after_total']}** | "
        f"**{payload['after_api_reference_total']}** |",
        "",
        "## Pattern match vs skip",
        "",
        f"- Endpoint headings seen: {summary['endpoint_headings']}",
        f"- Matched (verb+URL line present): {summary['matched']}",
        f"- Matched with Required Fields: {summary['matched_with_required_fields']}",
        f"- Matched with REST Example: {summary['matched_with_example']}",
        f"- Claims emitted from pattern: {summary['claims_emitted']}",
        f"- Hard skips (no claims): {summary['skipped']}",
        "",
    ]
    if summary.get("skipped_by_reason"):
        lines.append("### Hard skips (section produced no claims)")
        lines.append("")
        for reason, n in sorted(summary["skipped_by_reason"].items()):
            lines.append(f"- `{reason}`: {n}")
        lines.append("")
        # Detail lines
        for r in reports:
            for s in r.skipped:
                lines.append(
                    f"  - {r.source_pointer}:{s.line} — {s.reason}: {s.detail}"
                )
        lines.append("")
    if soft_counts:
        lines.append("### Soft gaps (matched, claim emitted, enrichment missing)")
        lines.append("")
        for reason, n in sorted(soft_counts.items()):
            lines.append(f"- `{reason}`: {n}")
        lines.append("")

    mp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {jp}")
    print(f"wrote {mp}")
    print(
        f"before={payload['before_total']} after={payload['after_total']} "
        f"api_reference={payload['after_api_reference_total']} "
        f"matched={summary['matched']}/{summary['endpoint_headings']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
