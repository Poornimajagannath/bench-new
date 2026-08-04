#!/usr/bin/env python3
"""Relay Content Engine V0 — local compiled-content prototype.

source registry
-> local snapshot
-> normalize / segment
-> DocETL-style extract (quickstart_unit)
-> schema + content validation
-> promote + context-pack stub

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

from relay_bench.content_engine.pipeline import run_content_engine
from relay_bench.content_engine.registry import list_enabled_sources


def main() -> int:
    enabled = sorted(r.source_id for r in list_enabled_sources())
    parser = argparse.ArgumentParser(description="Run Relay Content Engine V0")
    parser.add_argument(
        "--source",
        required=True,
        choices=enabled,
        help="Registered local source_id to compile",
    )
    args = parser.parse_args()

    print(f"[content_engine] stage=registry source={args.source}")
    result = run_content_engine(args.source)
    print(
        f"[content_engine] stage=promote status={result['promotion_status']} "
        f"units={result['unit_count']} schema={result['schema_passed']} "
        f"content={result['content_passed']} agent_use={result['agent_use_status']}"
    )
    if result["context_pack_path"]:
        print(f"[content_engine] context_pack={result['context_pack_path']}")
    if result["contract_bundle_path"]:
        print(f"[content_engine] linked_contract={result['contract_bundle_path']}")
    for issue in result["issues"]:
        print(f"[content_engine] error {issue['code']}: {issue['message']}")

    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
