"""Reconcile generated contract docs against human/quickstart overlays."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from content_bench.content_engine.schemas import (
    ApiReferenceUnit,
    ContractEntity,
    ReconciliationReport,
    SourceRecord,
    SourceSnapshot,
)
from content_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
RECON_DIR = ROOT / "artifacts" / "content_engine" / "reconciliation"
OBJECTS_DIR = ROOT / "artifacts" / "content_engine" / "objects"


def reconcile(
    record: SourceRecord,
    snapshot: SourceSnapshot,
    entities: List[ContractEntity],
    units: List[ApiReferenceUnit],
) -> ReconciliationReport:
    compared: List[str] = []
    known_ops_from_quickstart: List[str] = []

    if record.linked_workflow_id:
        contract = (
            ROOT
            / "artifacts"
            / "contracts"
            / f"{record.linked_workflow_id}.contract_bundle.json"
        )
        if contract.exists():
            compared.append(repo_relative(contract))

    quickstart_objects = OBJECTS_DIR / "microform-payer-auth-quickstart.quickstart_units.json"
    if quickstart_objects.exists():
        compared.append(repo_relative(quickstart_objects))
        payload = json.loads(quickstart_objects.read_text(encoding="utf-8"))
        blob = json.dumps(payload).lower()
        for token in (
            "enrollment",
            "microform",
            "authorization",
            "challenge",
            "frictionless",
        ):
            if token in blob:
                known_ops_from_quickstart.append(token)

    entity_ids = [e.entity_id for e in entities]
    missing_links: List[str] = []
    for unit in units:
        if not unit.workflows:
            missing_links.append(unit.operation_id)

    # MPP/auth operations should link to the microform workflow when present.
    for unit in units:
        tags_or_summary = (unit.summary + " " + " ".join(unit.workflows)).lower()
        if any(k in tags_or_summary for k in ("payer auth", "enrollment", "mpp", "authentication")):
            if "microform-payer-auth-state-machine" not in unit.workflows:
                missing_links.append(unit.operation_id)

    stale_claims: List[str] = []
    # If quickstart mentions tokenize-as-complete-3ds anti-pattern absence is fine;
    # flag only if linked workflow missing while MPP ops exist.
    mpp_ops = [e.operation_id for e in entities if "MPP" in " ".join(e.tags)]
    if mpp_ops and not record.linked_workflow_id:
        stale_claims.append(
            "MPP credential operations present but no linked_workflow_id on source record"
        )

    decisions = []
    for entity in entities:
        action = "generate"
        if entity.operation_id in missing_links:
            action = "flag"
        decisions.append({"entity_id": entity.entity_id, "action": action})

    return ReconciliationReport(
        source_id=record.source_id,
        spec_snapshot_id=snapshot.snapshot_id,
        compared_against=compared,
        added_entities=entity_ids,
        removed_entities=[],
        changed_entities=[],
        missing_quickstart_links=sorted(set(missing_links)),
        stale_human_claims=stale_claims,
        decisions=decisions,
    )


def write_reconciliation(report: ReconciliationReport) -> Path:
    RECON_DIR.mkdir(parents=True, exist_ok=True)
    path = RECON_DIR / f"{report.source_id}.report.json"
    path.write_text(json.dumps(report.to_dict(), indent=2) + "\n", encoding="utf-8")
    return path
