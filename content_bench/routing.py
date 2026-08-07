"""Failure classifier → product-surface improvement actions.

Content CLI actions treat the CLI as a workflow verifier descriptor, not a wrapper.
"""

from __future__ import annotations

from typing import Dict, List

from content_bench.schemas import (
    FailureClassification,
    ImprovementAction,
    ContentCliDescriptor,
    VerifierResult,
    WorkflowCandidate,
)


_CATEGORY_BY_WORKFLOW: Dict[str, str] = {
    "flex-token-lifecycle": "token-lifecycle-confusion",
    "http-signature-debug": "auth-mechanism",
    "microform-payer-auth-state-machine": "state-machine-gap",
}


def _content_cli_for(candidate: WorkflowCandidate) -> ContentCliDescriptor:
    return ContentCliDescriptor(
        goal=candidate.goal,
        command=f"content workflow verify --id {candidate.workflow_id} --fixture local",
        api_sdk_facts=list(candidate.api_sdk_facts),
        readiness_checks=[
            "Frozen seeds present under data/seeds/",
            "No live credentials exported",
            "Local fixture id resolved for workflow",
            *[f"Stage ready: {stage}" for stage in candidate.stages],
        ],
        recovery_path=[
            "Re-run discovery to refresh typed candidate",
            "Compare agent plan stages against workflow contract stages",
            "Apply verifier-private checks to the candidate answer only",
            "Emit support-safe evidence without secrets or PAN",
        ],
        support_safe_evidence=[
            "workflow_id",
            "failed check ids",
            "stage list",
            "public doc refs from seeds",
        ],
        telemetry_eval_hints=[
            "track:enrollment_skip_rate",
            "track:field_name_mismatch_rate",
            "track:transient_token_persist_attempts",
            "eval:verifier_catch_rate_on_bad_answer",
        ],
        future_mcp_metadata={
            "mcp_tool": "content.verify_workflow",
            "inputs": ["workflow_id", "candidate_answer_ref"],
            "outputs": ["check_results", "improvement_actions"],
            "auth": "none-local-fixture",
        },
    )


def classify_failure(
    candidate: WorkflowCandidate,
    bad_result: VerifierResult,
) -> FailureClassification:
    category = _CATEGORY_BY_WORKFLOW.get(candidate.workflow_id, "unclassified")
    evidence = [
        f"check_failed:{cid}" for cid in bad_result.caught_failures
    ] + list(candidate.confusion_points[:5])

    actions: List[ImprovementAction] = [
        ImprovementAction(
            action_id=f"{candidate.workflow_id}-docs",
            product_surface="docs",
            severity="high",
            summary=f"Clarify {candidate.title} stage ordering in public docs",
            rationale="Developers confused adjacent APIs and skipped required stages.",
        ),
        ImprovementAction(
            action_id=f"{candidate.workflow_id}-content-cli",
            product_surface="content_cli",
            severity="high",
            summary="Ship a Content CLI workflow verifier for this contract",
            rationale=(
                "CLI should verify readiness, recovery, and support-safe evidence — "
                "not only wrap an API call."
            ),
            content_cli=_content_cli_for(candidate),
        ),
    ]

    if candidate.workflow_id == "http-signature-debug":
        actions.insert(
            1,
            ImprovementAction(
                action_id=f"{candidate.workflow_id}-sdk",
                product_surface="sdk",
                severity="high",
                summary="Align SDK credential field names with docs (or docs with SDK)",
                rationale="keyId/secretKey vs merchantKeyId/merchantsecretKey drift causes auth failures.",
            ),
        )

    return FailureClassification(
        workflow_id=candidate.workflow_id,
        category=category,
        summary=(
            f"Bad answer for {candidate.workflow_id} failed "
            f"{len(bad_result.caught_failures)} verifier check(s)."
        ),
        evidence=evidence,
        actions=actions,
    )
