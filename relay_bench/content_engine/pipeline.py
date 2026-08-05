"""Content Engine V0 staged pipeline (local by default; optional DocETL)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from relay_bench.content_engine.docetl_adapter import (
    extract_quickstart_units_with_backend,
    normalize_extract_mode,
)
from relay_bench.content_engine.normalize import normalize_document
from relay_bench.content_engine.promote import build_objects_payload, promote_units
from relay_bench.content_engine.registry import require_source
from relay_bench.content_engine.segment import segment_document
from relay_bench.content_engine.snapshot import materialize_snapshot
from relay_bench.reporting import repo_relative


def synthesize_quickstart_units_payload(
    source_id: str,
    *,
    discovery: Optional[str] = None,
    fallback_on_error: bool = False,
) -> Dict[str, Any]:
    """Rebuild the objects artifact payload without writing (freshness checks).

    Defaults match the CLI: heuristic extract unless discovery/env selects DocETL.
    """
    mode = normalize_extract_mode(discovery)
    record = require_source(source_id)
    snapshot = materialize_snapshot(record)
    doc = normalize_document(record, snapshot)
    segments = segment_document(doc)
    units, honest = extract_quickstart_units_with_backend(
        record,
        doc,
        segments,
        mode=mode,
        fallback_on_error=fallback_on_error,
    )
    return build_objects_payload(
        source_id,
        units,
        extractor_label=honest.get("docetl", "style-only"),
    )


def run_content_engine(
    source_id: str,
    *,
    discovery: Optional[str] = None,
    fallback_on_error: bool = False,
) -> Dict[str, Any]:
    """
    local registry
    -> snapshot
    -> normalize / segment
    -> extract (heuristic | docetl code_map | docetl llm map)
    -> schema + content validation
    -> promote + context pack (if pass)
    """
    mode = normalize_extract_mode(discovery)
    record = require_source(source_id)
    snapshot = materialize_snapshot(record)
    doc = normalize_document(record, snapshot)
    segments = segment_document(doc)
    units, honest = extract_quickstart_units_with_backend(
        record,
        doc,
        segments,
        mode=mode,
        fallback_on_error=fallback_on_error,
    )
    decision, context_path = promote_units(
        record,
        doc,
        snapshot,
        units,
        extractor_label=honest.get("docetl", "style-only"),
    )

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
        "honest_label": honest,
    }
