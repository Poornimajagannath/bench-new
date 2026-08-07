#!/usr/bin/env python3
"""Content Bench Specs-to-Docs V0 — local contract compile lane.

openapi fixture
-> snapshot
-> parse contract_entity
-> compose api_reference_unit + eval seeds
-> reconcile
-> schema/content/contract-alignment gates
-> promote derived artifacts

Does NOT import docetl / tempo-evals / Harbor.
Does NOT call the network or use live credentials.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.registry import list_enabled_sources
from content_bench.content_engine.specs_pipeline import run_specs_to_docs


def main() -> int:
    openapi_sources = sorted(
        r.source_id
        for r in list_enabled_sources()
        if r.source_type == "openapi" or r.parser_strategy == "openapi_parser"
    )
    parser = argparse.ArgumentParser(description="Run Content Bench Specs-to-Docs V0")
    parser.add_argument(
        "--source",
        required=True,
        choices=openapi_sources,
        help="Registered local OpenAPI source_id",
    )
    args = parser.parse_args()

    print(f"[specs_to_docs] stage=registry source={args.source}")
    result = run_specs_to_docs(args.source)
    print(
        f"[specs_to_docs] stage=promote status={result['promotion_status']} "
        f"entities={result['entity_count']} units={result['unit_count']} "
        f"align={result['contract_alignment_passed']}"
    )
    print(f"[specs_to_docs] operations={result['operation_ids']}")
    if result["entities_path"]:
        print(f"[specs_to_docs] entities={result['entities_path']}")
    if result["units_path"]:
        print(f"[specs_to_docs] units={result['units_path']}")
    if result["reconciliation_path"]:
        print(f"[specs_to_docs] reconciliation={result['reconciliation_path']}")
    for issue in result["issues"]:
        print(f"[specs_to_docs] error {issue['code']}: {issue['message']}")

    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
