#!/usr/bin/env python3
"""Compile a durable Workflow Contract Bundle from one PM-approved candidate.

messy sources
-> DocETL-style extraction
-> PM-approved workflow contract
-> Relay task pack + hidden truth
-> Tempo/Harbor-shaped eval export (preview)
-> verifier receipt
-> failure class / product action
-> (rerun via run_bench_v0)

Does NOT import docetl, tempo-evals, Harbor, or Docker.
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

from relay_bench.contract_compiler import compile_and_write
from relay_bench.pm_gate import require_pm_approved_candidate


SUPPORTED = {
    "flex-token-lifecycle",
    "http-signature-debug",
    "microform-payer-auth-state-machine",
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile a Relay workflow contract bundle"
    )
    parser.add_argument(
        "--workflow",
        required=True,
        choices=sorted(SUPPORTED),
        help="PM-approved workflow id to compile",
    )
    args = parser.parse_args()

    try:
        candidate = require_pm_approved_candidate(args.workflow)
    except LookupError as exc:
        print(f"[compile_contract] {exc}", file=sys.stderr)
        return 1

    print(
        f"[compile_contract] stage=compile "
        f"workflow={candidate.workflow_id!r} pm_decision={candidate.pm_decision}"
    )
    bundle, json_path, md_path = compile_and_write(candidate)
    receipt = bundle["hidden_truth_receipt"]
    harbor = bundle["harbor_shape_preview"]

    print(f"[compile_contract] contract_json={json_path}")
    print(f"[compile_contract] contract_md={md_path}")
    print(
        f"[compile_contract] hidden_truth_receipt "
        f"oracle_present={receipt['oracle_present']} "
        f"agent_pack_omits_oracle={receipt['agent_pack_omits_oracle']}"
    )
    print(
        f"[compile_contract] harbor_shape_preview "
        f"preview_only={harbor['preview_only']} "
        f"runner_integration={harbor['runner_integration']!r}"
    )

    summary = {
        "ok": True,
        "workflow_id": candidate.workflow_id,
        "schema_version": bundle["schema_version"],
        "contract_json": str(json_path),
        "contract_md": str(md_path),
        "task_pack_path": bundle["task_pack_path"],
        "verifier_result_path": bundle.get("verifier_result_path"),
        "harbor_shape_preview": {
            "preview_only": harbor["preview_only"],
            "runner_integration": harbor["runner_integration"],
        },
        "hidden_truth_separated": True,
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
