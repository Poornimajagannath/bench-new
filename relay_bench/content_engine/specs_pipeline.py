"""Specs-to-Docs V0 staged pipeline (local, credential-free)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from relay_bench.content_engine.context_pack import maybe_contract_bundle_path
from relay_bench.content_engine.registry import require_source
from relay_bench.content_engine.snapshot import materialize_snapshot
from relay_bench.content_engine.specs_compose import (
    compose_eval_seeds,
    compose_quickstart_hints,
    compose_reference_units,
    write_generated,
)
from relay_bench.content_engine.specs_parser import parse_openapi_entities, write_entities
from relay_bench.content_engine.specs_reconcile import reconcile, write_reconciliation
from relay_bench.content_engine.specs_validate import (
    validate_contract_alignment,
    validate_units_content,
    validate_units_schema,
)
from relay_bench.content_engine.schemas import SpecPromotionDecision
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
PROMOTIONS_DIR = ROOT / "artifacts" / "content_engine" / "promotions"


def run_specs_to_docs(source_id: str) -> Dict[str, Any]:
    """
    openapi registry source
    -> snapshot
    -> parse contract entities
    -> compose reference units + eval seeds + quickstart hints
    -> reconcile vs human/quickstart overlays
    -> schema + content + contract-alignment gates
    -> promote derived artifacts if pass
    """
    record = require_source(source_id)
    if record.source_type != "openapi" and record.parser_strategy != "openapi_parser":
        raise ValueError(
            f"Source {source_id!r} is not an OpenAPI source "
            f"(source_type={record.source_type!r})"
        )

    snapshot = materialize_snapshot(record)
    entities = parse_openapi_entities(record, snapshot)
    entities_path = write_entities(source_id, entities, snapshot)

    units = compose_reference_units(record, entities)
    eval_seeds = compose_eval_seeds(record, entities)
    hints = compose_quickstart_hints(record, units)
    units_path, seeds_path, hints_path = write_generated(
        source_id, units, eval_seeds, hints
    )

    report = reconcile(record, snapshot, entities, units)
    recon_path = write_reconciliation(report)

    schema_ok, schema_issues = validate_units_schema(units)
    content_ok, content_issues = validate_units_content(units)
    align_ok, align_issues = validate_contract_alignment(entities, units)
    issues = schema_issues + content_issues + align_issues

    agent_use = "deferred"
    if record.linked_workflow_id:
        contract = (
            ROOT
            / "artifacts"
            / "contracts"
            / f"{record.linked_workflow_id}.contract_bundle.json"
        )
        if contract.exists():
            agent_use = "passed"

    decision = SpecPromotionDecision(
        source_id=source_id,
        status="blocked",
        schema_passed=schema_ok,
        content_passed=content_ok,
        contract_alignment_passed=align_ok,
        agent_use_status=agent_use,
        issues=issues,
        promoted_unit_ids=[],
        linked_workflow_id=record.linked_workflow_id,
        contract_bundle_path=maybe_contract_bundle_path(record.linked_workflow_id),
        entities_path=repo_relative(entities_path),
        units_path=repo_relative(units_path),
        eval_seeds_path=repo_relative(seeds_path),
        reconciliation_path=repo_relative(recon_path),
    )

    if schema_ok and content_ok and align_ok:
        decision.status = "promoted"
        decision.promoted_unit_ids = [u.unit_id for u in units]

    PROMOTIONS_DIR.mkdir(parents=True, exist_ok=True)
    promo_path = PROMOTIONS_DIR / f"{source_id}.specs_promotion.json"
    payload = decision.to_dict()
    payload["quickstart_hints_path"] = repo_relative(hints_path)
    payload["entity_count"] = len(entities)
    payload["eval_seed_count"] = len(eval_seeds)
    payload["honest_label"] = {
        "docetl": "not-used",
        "network": "denied",
        "fixture": "local-cybersource-shaped-openapi",
        "note": (
            "Local fixture covering Payments/Captures/Credits/Customers/"
            "MPP Credential operations. Not a live CyberSource download."
        ),
    }
    promo_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    return {
        "ok": decision.status == "promoted",
        "source_id": source_id,
        "snapshot_id": snapshot.snapshot_id,
        "entity_count": len(entities),
        "unit_count": len(units),
        "eval_seed_count": len(eval_seeds),
        "promotion_status": decision.status,
        "schema_passed": schema_ok,
        "content_passed": content_ok,
        "contract_alignment_passed": align_ok,
        "agent_use_status": agent_use,
        "entities_path": decision.entities_path,
        "units_path": decision.units_path,
        "eval_seeds_path": decision.eval_seeds_path,
        "reconciliation_path": decision.reconciliation_path,
        "contract_bundle_path": decision.contract_bundle_path,
        "promotion_path": repo_relative(promo_path),
        "issues": [i.to_dict() for i in issues if i.severity == "error"],
        "operation_ids": [e.operation_id for e in entities],
    }
