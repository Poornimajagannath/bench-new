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

from relay_bench.content_engine.ingest import (  # noqa: E402
    render_ingestion_report,
    run_ingestion_snapshot,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingestion snapshot (M0.5)")
    parser.add_argument("--docs-dir", default=str(ROOT / "cybersource-docs"))
    parser.add_argument("--raw-root", default=str(ROOT / "raw"))
    parser.add_argument("--normalized-root", default=str(ROOT / "normalized"))
    parser.add_argument(
        "--openapi",
        default=str(ROOT / "data/content_engine/specs/cybersource-payments-core.openapi.json"),
    )
    parser.add_argument("--stamp-date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--sample-limit", type=int, default=60)
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts/content_engine/ingestion-report.md"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "artifacts/content_engine/ingestion-report.json"),
    )
    args = parser.parse_args()

    report = run_ingestion_snapshot(
        docs_dir=Path(args.docs_dir),
        raw_root=Path(args.raw_root),
        normalized_root=Path(args.normalized_root),
        openapi_path=Path(args.openapi),
        stamp_date=args.stamp_date,
        sample_limit=args.sample_limit,
    )
    md = render_ingestion_report(report)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    Path(args.json_out).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(
        f"Fetched={report['docs_fetched']} claims={report['claims_extracted']} "
        f"drops={report['drop_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
