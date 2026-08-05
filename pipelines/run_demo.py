#!/usr/bin/env python3
"""Lightweight per-workflow demo (pre-V0 path).

Requires PM approve/edit before task-pack materialization.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.pm_gate import require_pm_approved_candidate
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

    try:
        candidate = require_pm_approved_candidate(args.workflow)
    except LookupError as exc:
        print(f"[run_demo] {exc}", file=sys.stderr)
        return 1

    pack, hidden, agent_path, private_path = materialize_contract(candidate)

    print(f"[run_demo] workflow={candidate.workflow_id}")
    print(f"[run_demo] pm_decision={candidate.pm_decision}")
    print(f"[run_demo] title={candidate.title}")
    print(f"[run_demo] stages={candidate.stages}")
    print(f"[run_demo] agent_task={agent_path}")
    print(f"[run_demo] verifier_private={private_path} (verifier-only)")
    print(f"[run_demo] agent_prompt_chars={len(pack.prompt)}")
    print(f"[run_demo] fixture_id={hidden.fixture_id}")
    print(json.dumps({"ok": True, "workflow_id": candidate.workflow_id}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
