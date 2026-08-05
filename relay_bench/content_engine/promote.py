"""Eval-gated promotion of typed quickstart units."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional, Tuple

from relay_bench.content_engine.context_pack import (
    build_context_pack,
    maybe_contract_bundle_path,
    write_context_pack,
)
from relay_bench.content_engine.schemas import (
    NormalizedDocument,
    PromotionDecision,
    QuickstartUnit,
    SourceRecord,
    SourceSnapshot,
    ValidationIssue,
)
from relay_bench.content_engine.validate import validate_content, validate_schema
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
OBJECTS_DIR = ROOT / "artifacts" / "content_engine" / "objects"
PROMOTIONS_DIR = ROOT / "artifacts" / "content_engine" / "promotions"


def _agent_use_status(record: SourceRecord) -> str:
    """V0: defer unless a linked workflow contract bundle already exists."""
    if not record.linked_workflow_id:
        return "deferred"
    contract = (
        ROOT
        / "artifacts"
        / "contracts"
        / f"{record.linked_workflow_id}.contract_bundle.json"
    )
    if contract.exists():
        # Presence of a compiled, receipt-bearing contract counts as linked
        # agent-use evidence for this local prototype.
        return "passed"
    return "deferred"


def write_objects(
    source_id: str,
    units: List[QuickstartUnit],
    *,
    extractor_label: str = "style-only",
) -> Path:
    OBJECTS_DIR.mkdir(parents=True, exist_ok=True)
    path = OBJECTS_DIR / f"{source_id}.quickstart_units.json"
    if extractor_label == "style-only":
        inspired_by = "ucbepic/docetl (not imported; heuristic extract)"
    elif extractor_label == "imported-code_map":
        inspired_by = "ucbepic/docetl (imported; Frame.code_map, no LLM)"
    elif extractor_label == "imported-llm-map":
        inspired_by = "ucbepic/docetl (imported; Frame.map with LLM)"
    else:
        inspired_by = f"ucbepic/docetl ({extractor_label})"
    payload = {
        "stage": "content_engine_extract",
        "inspired_by": inspired_by,
        "extractor_label": extractor_label,
        "source_id": source_id,
        "units": [u.to_dict() for u in units],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def promote_units(
    record: SourceRecord,
    doc: NormalizedDocument,
    snapshot: SourceSnapshot,
    units: List[QuickstartUnit],
    *,
    extractor_label: str = "style-only",
) -> Tuple[PromotionDecision, Optional[Path]]:
    schema_passed, schema_issues = validate_schema(units)
    content_passed, content_issues = validate_content(units)
    issues: List[ValidationIssue] = schema_issues + content_issues
    agent_use = _agent_use_status(record)

    objects_path = write_objects(
        record.source_id, units, extractor_label=extractor_label
    )

    decision = PromotionDecision(
        source_id=record.source_id,
        status="blocked",
        schema_passed=schema_passed,
        content_passed=content_passed,
        agent_use_status=agent_use,
        issues=issues,
        promoted_unit_ids=[],
        linked_workflow_id=record.linked_workflow_id,
        contract_bundle_path=maybe_contract_bundle_path(record.linked_workflow_id),
        context_pack_path=None,
    )

    context_path: Optional[Path] = None
    if schema_passed and content_passed:
        pack = build_context_pack(record, doc, snapshot, units)
        context_path = write_context_pack(pack)
        decision.status = "promoted"
        decision.promoted_unit_ids = [u.unit_id for u in units]
        decision.context_pack_path = repo_relative(context_path)
    else:
        decision.status = "blocked"

    PROMOTIONS_DIR.mkdir(parents=True, exist_ok=True)
    promo_path = PROMOTIONS_DIR / f"{record.source_id}.promotion.json"
    payload = decision.to_dict()
    payload["objects_path"] = repo_relative(objects_path)
    promo_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return decision, context_path
