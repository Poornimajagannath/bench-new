#!/usr/bin/env python3
"""Lightweight per-workflow demo (pre-V0 path).

Keeps discovery + task-pack materialization runnable without the full bench report.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.discovery import discover_workflows
from relay_bench.task_pack import materialize_contract


SUPPORTED = {
    "flex-token-lifecycle",
    "http-signature-debug",
    "microform-payer-auth-state-machine",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Relay Bench workflow demo")
    parser.add_argument(
        "--workflow",
        required=True,
        choices=sorted(SUPPORTED),
        help="Workflow id to demo",
    )
    args = parser.parse_args()

    candidates = discover_workflows(workflow_id=args.workflow)
    if not candidates:
        print(f"[run_demo] no candidate for {args.workflow}", file=sys.stderr)
        return 1

    candidate = candidates[0]
    pack, hidden, pack_path, hidden_path = materialize_contract(candidate)

    print(f"[run_demo] workflow={candidate.workflow_id}")
    print(f"[run_demo] title={candidate.title}")
    print(f"[run_demo] stages={candidate.stages}")
    print(f"[run_demo] task_pack={pack_path}")
    print(f"[run_demo] hidden_truth={hidden_path} (verifier-only)")
    print(f"[run_demo] agent_prompt_chars={len(pack.prompt)}")
    print(f"[run_demo] fixture_id={hidden.fixture_id}")
    print(json.dumps({"ok": True, "workflow_id": candidate.workflow_id}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
