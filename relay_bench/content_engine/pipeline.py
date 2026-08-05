"""Content Engine V0 staged pipeline (local, credential-free)."""

from __future__ import annotations

from typing import Any, Dict

from relay_bench.content_engine.extract import extract_quickstart_units
from relay_bench.content_engine.normalize import normalize_document
from relay_bench.content_engine.promote import promote_units
from relay_bench.content_engine.registry import require_source
from relay_bench.content_engine.segment import segment_document
from relay_bench.content_engine.snapshot import materialize_snapshot
from relay_bench.reporting import repo_relative


def run_content_engine(source_id: str) -> Dict[str, Any]:
    """
    local registry
    -> snapshot
    -> normalize / segment
    -> DocETL-style extract
    -> schema + content validation
    -> promote + context pack (if pass)
    """
    record = require_source(source_id)
    snapshot = materialize_snapshot(record)
    doc = normalize_document(record, snapshot)
    segments = segment_document(doc)
    units = extract_quickstart_units(record, doc, segments)
    decision, context_path = promote_units(record, doc, snapshot, units)

    return {
        "ok": decision.status == "promoted",
        "source_id": source_id,
        "snapshot_id": snapshot.snapshot_id,
        "content_hash": snapshot.content_hash,
        "segment_count": len(segments),
        "unit_count": len(units),
        "promotion_status": decision.status,
        "schema_passed": decision.schema_passed,
        "content_passed": decision.content_passed,
        "agent_use_status": decision.agent_use_status,
        "promoted_unit_ids": list(decision.promoted_unit_ids),
        "context_pack_path": decision.context_pack_path
        or (repo_relative(context_path) if context_path else None),
        "contract_bundle_path": decision.contract_bundle_path,
        "issue_count": len(decision.issues),
        "issues": [i.to_dict() for i in decision.issues if i.severity == "error"],
        "honest_label": {
            "docetl": "style-only",
            "tempo_harbor": "preview-via-linked-contract-if-present",
            "network": "denied",
        },
    }
