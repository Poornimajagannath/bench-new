#!/usr/bin/env python3
"""Relay Bench V0 staged pipeline runner.

Local prototype inspired by DocETL and Tempo Stable Bench.
Does NOT import `docetl`, `tempo-evals`, Harbor, or Docker isolation.

raw forum/docs/support questions
-> DocETL-inspired extract of goal/symptoms/entities
-> suggests workflow_id + stages
-> PM approves/edits
-> Relay Bench creates task pack + Stable Bench-inspired verifier
-> failure classifier
-> product-surface improvement action
-> PM-readable report
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.discovery import discover_suggestions
from relay_bench.pm_gate import require_pm_approved_candidate
from relay_bench.reporting import build_report, write_report
from relay_bench.routing import classify_failure
from relay_bench.task_pack import materialize_contract
from relay_bench.verifiers import (
    run_stable_bench_inspired_verification,
    write_verifier_results,
)


SUPPORTED = {
    "flex-token-lifecycle",
    "http-signature-debug",
    "microform-payer-auth-state-machine",
}


def run_pipeline(workflow_id: str) -> int:
    print("[bench_v0] stage=raw_questions_extract_suggest")
    rows = discover_suggestions()
    for question, extraction, suggestion in rows:
        print(
            f"[bench_v0] seed={question.seed_id} channel={question.channel} "
            f"suggest={suggestion.suggested_workflow_id} "
            f"entities={extraction.entities}"
        )

    print("[bench_v0] stage=pm_approve_or_edit")
    try:
        candidate = require_pm_approved_candidate(workflow_id, rows=rows)
    except LookupError as exc:
        print(f"[bench_v0] {exc}", file=sys.stderr)
        return 1
    print(
        f"[bench_v0] pm_decision={candidate.pm_decision} "
        f"workflow={candidate.workflow_id!r} seeds={candidate.seed_ids}"
    )

    print("[bench_v0] stage=task_pack_and_verifier")
    pack, hidden, pack_path, hidden_path = materialize_contract(candidate)
    pack.assert_agent_safe()
    print(f"[bench_v0] task_pack={pack_path}")
    print(f"[bench_v0] hidden_truth={hidden_path} (not agent-facing)")

    results = run_stable_bench_inspired_verification(hidden)
    result_path = write_verifier_results(workflow_id, results)
    print(f"[bench_v0] verifier_results={result_path}")
    print(
        f"[bench_v0] oracle_passed={results['oracle_answer'].passed} "
        f"bad_answer_caught={results['bad_answer'].passed}"
    )

    print("[bench_v0] stage=failure_classifier")
    classification = classify_failure(candidate, results["bad_answer"])
    print(
        f"[bench_v0] category={classification.category} "
        f"actions={len(classification.actions)}"
    )

    print("[bench_v0] stage=report")
    report = build_report(
        candidate=candidate,
        classification=classification,
        bad_result=results["bad_answer"],
        task_pack_path=pack_path,
        verifier_result_path=result_path,
        bad_answer_mistake=str(hidden.bad_answer.get("mistake", "")),
    )
    md_path, json_path = write_report(report)
    print(f"[bench_v0] report_md={md_path}")
    print(f"[bench_v0] report_json={json_path}")

    summary = {
        "ok": True,
        "workflow_id": workflow_id,
        "pm_decision": candidate.pm_decision,
        "task_pack": str(pack_path),
        "hidden_truth": str(hidden_path),
        "verifier_results": str(result_path),
        "report_md": str(md_path),
        "report_json": str(json_path),
        "hidden_truth_separated": True,
        "pm_open": str(md_path),
    }
    print(json.dumps(summary, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Relay Bench V0 staged pipeline")
    parser.add_argument(
        "--workflow",
        required=True,
        choices=sorted(SUPPORTED),
        help="PM-approved workflow id to benchmark",
    )
    args = parser.parse_args()
    return run_pipeline(args.workflow)


if __name__ == "__main__":
    raise SystemExit(main())
