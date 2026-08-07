#!/usr/bin/env python3
"""Corpus census: classify downloaded docs; publish counts + quarantine list."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.corpus_census import (  # noqa: E402
    render_census_markdown,
    render_quarantine_markdown,
    run_corpus_census,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify corpus docs by kind; write counts + quarantine list"
    )
    parser.add_argument(
        "--docs-dir",
        default=str(ROOT / "cybersource-docs"),
        help="Downloaded corpus directory (default: cybersource-docs)",
    )
    parser.add_argument(
        "--policy",
        default=str(ROOT / "data/content_engine/corpus_quarantine_policy.json"),
        help="Quarantine policy JSON (exclude_kinds)",
    )
    parser.add_argument(
        "--out-dir",
        default=str(ROOT / "artifacts/content_engine/corpus"),
        help="Directory for census + quarantine reports",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    result = run_corpus_census(
        Path(args.docs_dir),
        policy_path=Path(args.policy) if args.policy else None,
    )

    census_md = out_dir / "census-report.md"
    census_json = out_dir / "census-report.json"
    quar_md = out_dir / "quarantine-list.md"
    quar_json = out_dir / "quarantine-list.json"

    census_md.write_text(render_census_markdown(result), encoding="utf-8")
    census_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    quar_md.write_text(render_quarantine_markdown(result), encoding="utf-8")
    # Compact quarantine artifact for ingest consumers
    quar_payload = {
        "generated_at": result["generated_at"],
        "docs_dir": result["docs_dir"],
        "exclude_kinds": result["quarantine_policy"]["exclude_kinds"],
        "quarantine_count": result["quarantine_count"],
        "paths": [row["path"] for row in result["quarantine_list"]],
        "by_kind": {},
        "entries": result["quarantine_list"],
    }
    by_kind: dict = {}
    for row in result["quarantine_list"]:
        by_kind.setdefault(row["kind"], []).append(row["path"])
    quar_payload["by_kind"] = {k: v for k, v in sorted(by_kind.items())}
    quar_json.write_text(json.dumps(quar_payload, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {census_md}")
    print(f"Wrote {quar_md}")
    print(
        f"docs={result['doc_count']} eligible={result['eligible_count']} "
        f"quarantined={result['quarantine_count']}"
    )
    for kind, n in result["counts_by_kind"].items():
        if n:
            print(f"  {kind}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
