"""Typed schemas for Content Engine V0 (subset of the Relay SDD)."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class SourceRecord:
    source_id: str
    source_type: str
    canonical_url: str
    repo_path: str
    owning_team: str
    product: List[str]
    audience: List[str]
    refresh_cadence: str
    trust_level: str
    parser_strategy: str
    enabled: bool = True
    linked_workflow_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SourceSnapshot:
    snapshot_id: str
    source_id: str
    fetched_at: str
    content_hash: str
    version_tag: str
    mime_type: str
    raw_bytes_location: str
    canonical_url: str
    upstream_last_modified: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NormalizedDocument:
    doc_id: str
    source_id: str
    snapshot_id: str
    title: str
    canonical_url: str
    source_format: str
    product: List[str]
    audience: List[str]
    page_type: str
    freshness_date: str
    normalized_markdown: str
    extracted_metadata: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DocumentSegment:
    segment_id: str
    doc_id: str
    heading_path: List[str]
    segment_type: str
    classification: str
    order_index: int
    markdown: str
    source_span: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class QuickstartUnit:
    unit_id: str
    source_page_id: str
    unit_type: str
    title: str
    goal: str
    product: List[str]
    audience: List[str]
    task: List[str]
    sequence_number: int
    body_markdown: str
    commands: List[str] = field(default_factory=list)
    api_entities: List[str] = field(default_factory=list)
    requires: List[str] = field(default_factory=list)
    outcomes: List[str] = field(default_factory=list)
    failure_modes: List[str] = field(default_factory=list)
    confidence: float = 0.0
    evidence_quotes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ValidationIssue:
    code: str
    severity: str  # error | warning
    message: str
    unit_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PromotionDecision:
    source_id: str
    status: str  # promoted | blocked | draft
    schema_passed: bool
    content_passed: bool
    agent_use_status: str  # passed | deferred | failed
    issues: List[ValidationIssue] = field(default_factory=list)
    promoted_unit_ids: List[str] = field(default_factory=list)
    linked_workflow_id: Optional[str] = None
    contract_bundle_path: Optional[str] = None
    context_pack_path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "status": self.status,
            "schema_passed": self.schema_passed,
            "content_passed": self.content_passed,
            "agent_use_status": self.agent_use_status,
            "issues": [i.to_dict() for i in self.issues],
            "promoted_unit_ids": list(self.promoted_unit_ids),
            "linked_workflow_id": self.linked_workflow_id,
            "contract_bundle_path": self.contract_bundle_path,
            "context_pack_path": self.context_pack_path,
        }


@dataclass
class ContextPack:
    pack_id: str
    source_id: str
    product: List[str]
    audience: List[str]
    title: str
    goal: str
    unit_ids: List[str]
    units_summary: List[Dict[str, Any]]
    provenance: Dict[str, str]
    constraints: List[str]
    linked_workflow_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
