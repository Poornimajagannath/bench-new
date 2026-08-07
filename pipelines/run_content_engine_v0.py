#!/usr/bin/env python3
"""Content Bench Content Engine V0 — local compiled-content prototype.

source registry
-> local snapshot
-> normalize / segment
-> extract (heuristic | real DocETL code_map | DocETL LLM map)
-> schema + content validation
-> promote + context-pack stub

Default extract is heuristic (no docetl import).
Pass --discovery docetl to run the real DocETL package via code_map.
Pass --discovery docetl-llm only when an LLM API key is configured.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.docetl_adapter import EXTRACT_MODES
from content_bench.content_engine.pipeline import run_content_engine
from content_bench.content_engine.registry import list_enabled_sources


def main() -> int:
    enabled = sorted(r.source_id for r in list_enabled_sources())
    parser = argparse.ArgumentParser(description="Run Content Bench Content Engine V0")
    parser.add_argument(
        "--source",
        required=True,
        choices=enabled,
        help="Registered local source_id to compile",
    )
    parser.add_argument(
        "--discovery",
        default=None,
        choices=list(EXTRACT_MODES),
        help=(
            "Extract backend: heuristic (default), docetl (real package code_map), "
            "or docetl-llm (real package LLM map; needs API key). "
            "If omitted, reads RELAY_DISCOVERY, else heuristic."
        ),
    )
    parser.add_argument(
        "--fallback-on-error",
        action="store_true",
        help="If DocETL mode cannot run, fall back to heuristic and label honesty",
    )
    args = parser.parse_args()

    discovery = args.discovery  # None => env RELAY_DISCOVERY => heuristic
    print(
        f"[content_engine] stage=registry source={args.source} "
        f"discovery={discovery or 'auto'}"
    )
    try:
        result = run_content_engine(
            args.source,
            discovery=discovery,
            fallback_on_error=args.fallback_on_error,
        )
    except Exception as exc:
        print(f"[content_engine] error: {exc}", file=sys.stderr)
        return 2

    print(
        f"[content_engine] stage=promote status={result['promotion_status']} "
        f"units={result['unit_count']} schema={result['schema_passed']} "
        f"content={result['content_passed']} agent_use={result['agent_use_status']} "
        f"docetl={result['honest_label'].get('docetl')}"
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
