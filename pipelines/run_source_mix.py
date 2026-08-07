#!/usr/bin/env python3
"""Milestone 0: inventory OpenAPI-regenerable vs prose-only facts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.content_engine.source_mix import (  # noqa: E402
    analyze_source_mix,
    render_source_mix_markdown,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Source-mix inventory (M0)")
    parser.add_argument(
        "--openapi",
        default=str(ROOT / "data/content_engine/specs/payments-core.openapi.json"),
    )
    parser.add_argument(
        "--docs-dir",
        default=str(ROOT / "gateway-docs"),
    )
    parser.add_argument("--sample-limit", type=int, default=40)
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts/content_engine/source-mix-report.md"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "artifacts/content_engine/source-mix-report.json"),
    )
    args = parser.parse_args()

    result = analyze_source_mix(
        openapi_path=Path(args.openapi),
        docs_dir=Path(args.docs_dir),
        sample_limit=args.sample_limit,
    )
    md = render_source_mix_markdown(result)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    Path(args.json_out).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(
        f"Overall spec-backed={result['overall_spec_backed_share']:.1%} "
        f"prose-only={result['overall_prose_only_share']:.1%}"
    )
    print(f"Decision: {result['decision_rule']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
