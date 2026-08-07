"""Typed artifacts that join DocETL-inspired discovery and Stable Bench-inspired verification.

V0 is a local prototype. It does not import `docetl` or `tempo-evals`.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class RawQuestion:
    """Frozen raw forum/docs/support question — input only, no workflow labels."""

    seed_id: str
    source: str
    channel: str  # forum | docs | support
    question: str
    public_refs: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Extraction:
    """DocETL-inspired extract: goal / symptoms / entities from a raw question."""

    seed_id: str
    goal: str
    symptoms: List[str]
    entities: List[str]
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class WorkflowSuggestion:
    """Suggested workflow_id + stages from extraction (pre-PM)."""

    seed_id: str
    suggested_workflow_id: str
    title: str
    stages: List[str]
    rationale: List[str]
    confidence: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PmDecision:
    """PM approve/edit gate over a suggestion."""

    seed_id: str
    decision: str  # approve | edit | reject
    approved_workflow_id: str
    edited_stages: Optional[List[str]]
    edited_goal: Optional[str]
    pm_notes: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class WorkflowCandidate:
    """PM-approved workflow candidate ready for task pack + verifier creation."""

    workflow_id: str
    title: str
    goal: str
    stages: List[str]
    api_sdk_facts: List[str]
    confusion_points: List[str]
    seed_ids: List[str]
    surface_hints: List[str] = field(default_factory=list)
    pm_decision: str = "approve"
    extraction: Optional[Dict[str, Any]] = None
    suggestion: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TaskPack:
    """Agent-visible benchmark task. Must NOT contain oracle / bad answer / private checks."""

    workflow_id: str
    title: str
    goal: str
    prompt: str
    allowed_context: List[str]
    constraints: List[str]
    expected_deliverable: str
    stages: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def assert_agent_safe(self) -> None:
        banned = ("oracle", "bad_answer", "bad answer", "verifier_private", "hidden_truth")
        blob = " ".join(
            [
                self.prompt,
                self.expected_deliverable,
                " ".join(self.allowed_context),
                " ".join(self.constraints),
            ]
        ).lower()
        for token in banned:
            if token in blob:
                raise ValueError(f"TaskPack leaked hidden-truth token: {token!r}")


@dataclass
class HiddenTruth:
    """Verifier-only material. Never written into agent-facing task packs."""

    workflow_id: str
    oracle_answer: Dict[str, Any]
    bad_answer: Dict[str, Any]
    verifier_private_checks: List[Dict[str, Any]]
    fixture_id: str
    # Check IDs the known-bad answer must fail. Bad-answer probe passes only
    # when every ID in this list appears in caught_failures.
    expected_bad_failure_ids: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CheckResult:
    check_id: str
    passed: bool
    detail: str
    private: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class VerifierResult:
    workflow_id: str
    subject: str  # "bad_answer" | "oracle_answer" | "candidate"
    passed: bool
    checks: List[CheckResult]
    caught_failures: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "workflow_id": self.workflow_id,
            "subject": self.subject,
            "passed": self.passed,
            "checks": [c.to_dict() for c in self.checks],
            "caught_failures": list(self.caught_failures),
        }


@dataclass
class ContentCliDescriptor:
    """Content CLI as a workflow verifier — not a thin command wrapper."""

    goal: str
    command: str
    api_sdk_facts: List[str]
    readiness_checks: List[str]
    recovery_path: List[str]
    support_safe_evidence: List[str]
    telemetry_eval_hints: List[str]
    future_mcp_metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ImprovementAction:
    action_id: str
    product_surface: str  # docs | sdk | content_cli | mcp | sandbox_fixture
    severity: str  # low | medium | high
    summary: str
    rationale: str
    content_cli: Optional[ContentCliDescriptor] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FailureClassification:
    workflow_id: str
    category: str
    summary: str
    evidence: List[str]
    actions: List[ImprovementAction]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "workflow_id": self.workflow_id,
            "category": self.category,
            "summary": self.summary,
            "evidence": list(self.evidence),
            "actions": [a.to_dict() for a in self.actions],
        }


@dataclass
class BenchReport:
    workflow_id: str
    developer_confusion: List[str]
    relay_discovered: List[str]
    bad_answer_errors: List[str]
    verifier_caught: List[str]
    next_product_improvements: List[str]
    classification: FailureClassification
    task_pack_path: str
    verifier_result_path: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "workflow_id": self.workflow_id,
            "developer_confusion": list(self.developer_confusion),
            "relay_discovered": list(self.relay_discovered),
            "bad_answer_errors": list(self.bad_answer_errors),
            "verifier_caught": list(self.verifier_caught),
            "next_product_improvements": list(self.next_product_improvements),
            "classification": self.classification.to_dict(),
            "task_pack_path": self.task_pack_path,
            "verifier_result_path": self.verifier_result_path,
        }
