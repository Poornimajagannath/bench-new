"""Relay workflow contract / benchmark task pack builder.

Separates agent-visible TaskPack from verifier-only HiddenTruth.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple

from relay_bench.schemas import HiddenTruth, TaskPack, WorkflowCandidate

ROOT = Path(__file__).resolve().parents[1]
TASK_PACK_DIR = ROOT / "artifacts" / "task_packs"

# Verifier-private fixtures keyed by workflow. Never copied into TaskPack.
_HIDDEN: Dict[str, Dict[str, object]] = {
    "flex-token-lifecycle": {
        "fixture_id": "fixture-flex-v0",
        "oracle_answer": {
            "uses_transient_token_path": True,
            "persists_transient_jwt": False,
            "calls_tms_create_instrument": True,
            "stages_completed": [
                "capture_transient_token",
                "validate_token_type",
                "create_permanent_instrument",
                "authorize_with_instrument",
            ],
        },
        "bad_answer": {
            "uses_transient_token_path": False,
            "persists_transient_jwt": True,
            "calls_tms_create_instrument": False,
            "stages_completed": ["capture_transient_token", "authorize_with_instrument"],
            "mistake": "Treats transientTokenJwt as a reusable PAN and skips TMS persistence",
        },
        "verifier_private_checks": [
            {
                "check_id": "no_persist_transient",
                "field": "persists_transient_jwt",
                "expected": False,
            },
            {
                "check_id": "uses_flex_to_tms_path",
                "field": "uses_transient_token_path",
                "expected": True,
            },
            {
                "check_id": "creates_permanent_instrument",
                "field": "calls_tms_create_instrument",
                "expected": True,
            },
            {
                "check_id": "stage_order_includes_validate",
                "field": "stages_completed",
                "contains": "validate_token_type",
            },
        ],
        "expected_bad_failure_ids": [
            "no_persist_transient",
            "uses_flex_to_tms_path",
            "creates_permanent_instrument",
            "stage_order_includes_validate",
        ],
    },
    "http-signature-debug": {
        "fixture_id": "fixture-httpsig-v0",
        "oracle_answer": {
            "credential_fields": ["merchantKeyId", "merchantsecretKey"],
            "endpoint_host": "apitest.cybersource.com",
            "signed_headers": [
                "host",
                "date",
                "request-target",
                "digest",
                "v-c-merchant-id",
            ],
            "logs_secrets": False,
        },
        "bad_answer": {
            "credential_fields": ["keyId", "secretKey"],
            "endpoint_host": "api.cybersource.com",
            "signed_headers": ["host", "date", "digest"],
            "logs_secrets": False,
            "mistake": "Uses doc field names and production host; omits request-target and v-c-merchant-id",
        },
        "verifier_private_checks": [
            {
                "check_id": "sdk_field_names",
                "field": "credential_fields",
                "expected": ["merchantKeyId", "merchantsecretKey"],
            },
            {
                "check_id": "sandbox_host",
                "field": "endpoint_host",
                "expected": "apitest.cybersource.com",
            },
            {
                "check_id": "signed_headers_complete",
                "field": "signed_headers",
                "contains_all": [
                    "host",
                    "date",
                    "request-target",
                    "digest",
                    "v-c-merchant-id",
                ],
            },
            {
                "check_id": "no_secret_logging",
                "field": "logs_secrets",
                "expected": False,
            },
        ],
        # Known-bad answer keeps logs_secrets=False; that check must not be required.
        "expected_bad_failure_ids": [
            "sdk_field_names",
            "sandbox_host",
            "signed_headers_complete",
        ],
    },
    "microform-payer-auth-state-machine": {
        "fixture_id": "fixture-mpa-v0",
        "oracle_answer": {
            "tokenizes_with_microform": True,
            "runs_enrollment_check": True,
            "handles_challenge_and_frictionless": True,
            "passes_auth_refs_to_payment": True,
            "stages_completed": [
                "microform_tokenize",
                "payer_auth_setup",
                "enrollment_check",
                "challenge_or_frictionless",
                "validate_authentication",
                "authorize_with_auth_result",
            ],
        },
        "bad_answer": {
            "tokenizes_with_microform": True,
            "runs_enrollment_check": False,
            "handles_challenge_and_frictionless": False,
            "passes_auth_refs_to_payment": False,
            "stages_completed": ["microform_tokenize", "authorize_with_auth_result"],
            "mistake": "Authorizes immediately after Microform token; skips enrollment/challenge/validation",
        },
        "verifier_private_checks": [
            {
                "check_id": "enrollment_present",
                "field": "runs_enrollment_check",
                "expected": True,
            },
            {
                "check_id": "dual_path_handling",
                "field": "handles_challenge_and_frictionless",
                "expected": True,
            },
            {
                "check_id": "auth_refs_on_payment",
                "field": "passes_auth_refs_to_payment",
                "expected": True,
            },
            {
                "check_id": "state_machine_complete",
                "field": "stages_completed",
                "contains_all": [
                    "enrollment_check",
                    "challenge_or_frictionless",
                    "validate_authentication",
                ],
            },
        ],
        "expected_bad_failure_ids": [
            "enrollment_present",
            "dual_path_handling",
            "auth_refs_on_payment",
            "state_machine_complete",
        ],
    },
}


def build_task_pack(candidate: WorkflowCandidate) -> TaskPack:
    prompt = (
        f"Workflow: {candidate.title}\n"
        f"Goal: {candidate.goal}\n\n"
        "Using only the allowed context, produce a step-by-step integration plan "
        "that covers every workflow stage. Do not call live payment APIs. "
        "Do not include credentials, PANs, or secrets."
    )
    pack = TaskPack(
        workflow_id=candidate.workflow_id,
        title=candidate.title,
        goal=candidate.goal,
        prompt=prompt,
        allowed_context=list(candidate.api_sdk_facts),
        constraints=[
            "No network calls",
            "No live CyberSource sandbox credentials",
            "No raw PAN, secrets, or credential logging",
            "Public forum/docs seeds are frozen input only",
        ],
        expected_deliverable=(
            "A structured plan listing each stage, the API/SDK fact it depends on, "
            "and the readiness check before moving to the next stage."
        ),
        stages=list(candidate.stages),
    )
    pack.assert_agent_safe()
    return pack


def build_hidden_truth(candidate: WorkflowCandidate) -> HiddenTruth:
    raw = _HIDDEN.get(candidate.workflow_id)
    if raw is None:
        raise KeyError(f"No hidden truth for workflow_id={candidate.workflow_id!r}")
    expected_ids = list(raw["expected_bad_failure_ids"])  # type: ignore[arg-type]
    if not expected_ids:
        raise ValueError(
            f"HiddenTruth for {candidate.workflow_id!r} must declare expected_bad_failure_ids"
        )
    return HiddenTruth(
        workflow_id=candidate.workflow_id,
        oracle_answer=dict(raw["oracle_answer"]),  # type: ignore[arg-type]
        bad_answer=dict(raw["bad_answer"]),  # type: ignore[arg-type]
        verifier_private_checks=list(raw["verifier_private_checks"]),  # type: ignore[arg-type]
        fixture_id=str(raw["fixture_id"]),
        expected_bad_failure_ids=expected_ids,
    )


def to_agent_task(pack: TaskPack, candidate: WorkflowCandidate) -> Dict[str, object]:
    """Agent-visible contract. Must never include verifier_private fields."""
    evidence_ids = [
        f"api_fact:{idx + 1}" for idx, _ in enumerate(pack.allowed_context)
    ] + [f"seed:{sid}" for sid in candidate.seed_ids]
    return {
        "agent_task": {
            "instruction": pack.prompt,
            "workflow_id": pack.workflow_id,
            "title": pack.title,
            "goal": pack.goal,
            "allowed_public_evidence_ids": evidence_ids,
            "allowed_context": list(pack.allowed_context),
            "environment_mode": "local-simulated",
            "required_artifact": pack.expected_deliverable,
            "stages": list(pack.stages),
            "constraints": list(pack.constraints),
        }
    }


def to_verifier_private(hidden: HiddenTruth) -> Dict[str, object]:
    """Verifier-only contract. Never export into agent_task artifacts."""
    return {
        "verifier_private": {
            "workflow_id": hidden.workflow_id,
            "fixture_id": hidden.fixture_id,
            "oracle_summary": dict(hidden.oracle_answer),
            "bad_answer_fixture": dict(hidden.bad_answer),
            "hidden_checks": list(hidden.verifier_private_checks),
            "scoring_rubric": {
                "expected_bad_failure_ids": list(hidden.expected_bad_failure_ids),
                "oracle_must_pass": True,
                "bad_answer_must_fail_all_expected": True,
            },
        }
    }


_BANNED_AGENT_KEYS = (
    "oracle_answer",
    "oracle_summary",
    "bad_answer",
    "bad_answer_fixture",
    "verifier_private",
    "verifier_private_checks",
    "hidden_checks",
    "hidden_truth",
    "scoring_rubric",
    "expected_bad_failure_ids",
)


def assert_no_verifier_leak(agent_payload: Dict[str, object]) -> None:
    blob = json.dumps(agent_payload)
    for banned in _BANNED_AGENT_KEYS:
        if banned in agent_payload or banned in agent_payload.get("agent_task", {}):  # type: ignore[operator]
            raise ValueError(f"agent_task leaked key {banned!r}")
        # Value leak: private fixture markers must not appear in agent JSON.
        if banned in ("oracle_summary", "bad_answer_fixture", "hidden_checks", "scoring_rubric"):
            if f'"{banned}"' in blob:
                raise ValueError(f"agent_task leaked field name {banned!r}")


def materialize_contract(candidate: WorkflowCandidate) -> Tuple[TaskPack, HiddenTruth, Path, Path]:
    """Write agent_task and verifier_private as separate artifacts (plus legacy aliases)."""
    TASK_PACK_DIR.mkdir(parents=True, exist_ok=True)
    pack = build_task_pack(candidate)
    hidden = build_hidden_truth(candidate)

    agent_payload = to_agent_task(pack, candidate)
    private_payload = to_verifier_private(hidden)
    assert_no_verifier_leak(agent_payload)

    agent_path = TASK_PACK_DIR / f"{candidate.workflow_id}.agent_task.json"
    private_path = TASK_PACK_DIR / f"{candidate.workflow_id}.verifier_private.json"
    # Legacy aliases kept for plan path compatibility.
    pack_path = TASK_PACK_DIR / f"{candidate.workflow_id}.task_pack.json"
    hidden_path = TASK_PACK_DIR / f"{candidate.workflow_id}.hidden_truth.json"

    agent_path.write_text(json.dumps(agent_payload, indent=2) + "\n", encoding="utf-8")
    private_path.write_text(json.dumps(private_payload, indent=2) + "\n", encoding="utf-8")
    pack_path.write_text(json.dumps(pack.to_dict(), indent=2) + "\n", encoding="utf-8")
    hidden_path.write_text(json.dumps(hidden.to_dict(), indent=2) + "\n", encoding="utf-8")

    written_agent = json.loads(agent_path.read_text(encoding="utf-8"))
    assert_no_verifier_leak(written_agent)
    written_pack = json.loads(pack_path.read_text(encoding="utf-8"))
    for banned_key in ("oracle_answer", "bad_answer", "verifier_private_checks", "hidden_truth"):
        if banned_key in written_pack:
            raise ValueError(f"Task pack artifact leaked key {banned_key!r}")

    return pack, hidden, agent_path, private_path
