#!/usr/bin/env python3
"""Integration Success OS V0 — assemble guided pack from Content Bench compile lanes.

quickstart compile + specs-to-docs
-> guided steps
-> API reference ops
-> test scenario seeds
-> go-live checklist
-> integration_success_pack.json/.md

No network. No live credentials. No DocETL/Tempo imports.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.integration_success import (
    DEFAULT_OPENAPI_SOURCE,
    DEFAULT_QUICKSTART_SOURCE,
    DEFAULT_WORKFLOW_ID,
    assemble_integration_success_pack,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble Integration Success OS V0 pack")
    parser.add_argument(
        "--quickstart-source",
        default=DEFAULT_QUICKSTART_SOURCE,
        help="Registered quickstart source_id",
    )
    parser.add_argument(
        "--openapi-source",
        default=DEFAULT_OPENAPI_SOURCE,
        help="Registered OpenAPI source_id",
    )
    parser.add_argument(
        "--workflow",
        default=DEFAULT_WORKFLOW_ID,
        help="Linked workflow contract id",
    )
    parser.add_argument(
        "--skip-compile",
        action="store_true",
        help="Use existing artifacts only; do not recompile lanes",
    )
    args = parser.parse_args()

    print(
        f"[integration_success] assemble quickstart={args.quickstart_source} "
        f"openapi={args.openapi_source} workflow={args.workflow}"
    )
    result = assemble_integration_success_pack(
        quickstart_source=args.quickstart_source,
        openapi_source=args.openapi_source,
        workflow_id=args.workflow,
        ensure_compiled=not args.skip_compile,
    )
    print(
        f"[integration_success] steps={result['step_count']} "
        f"ops={result['operation_count']} "
        f"scenarios={result['test_scenario_count']} "
        f"checklist={result['checklist_count']}"
    )
    print(f"[integration_success] pack_json={result['pack_json']}")
    print(f"[integration_success] pack_md={result['pack_md']}")
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
