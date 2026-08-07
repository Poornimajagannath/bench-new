"""Serving stub: assemble a compact context pack from promoted units."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from content_bench.content_engine.schemas import (
    ContextPack,
    NormalizedDocument,
    QuickstartUnit,
    SourceRecord,
    SourceSnapshot,
)
from content_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
CONTEXT_PACK_DIR = ROOT / "artifacts" / "content_engine" / "context_packs"


def build_context_pack(
    record: SourceRecord,
    doc: NormalizedDocument,
    snapshot: SourceSnapshot,
    units: List[QuickstartUnit],
) -> ContextPack:
    summaries = []
    for unit in units:
        summaries.append(
            {
                "unit_id": unit.unit_id,
                "unit_type": unit.unit_type,
                "title": unit.title,
                "sequence_number": unit.sequence_number,
                "requires": list(unit.requires),
                "outcomes": list(unit.outcomes),
                "failure_modes": list(unit.failure_modes),
                "evidence_quote_count": len(unit.evidence_quotes),
            }
        )

    goal = doc.extracted_metadata.get("goal") or doc.title
    pack = ContextPack(
        pack_id=f"ctx-{record.source_id}",
        source_id=record.source_id,
        product=list(record.product),
        audience=list(record.audience),
        title=doc.title,
        goal=goal,
        unit_ids=[u.unit_id for u in units],
        units_summary=summaries,
        provenance={
            "source_id": record.source_id,
            "snapshot_id": snapshot.snapshot_id,
            "content_hash": snapshot.content_hash,
            "canonical_url": record.canonical_url,
            "doc_id": doc.doc_id,
        },
        constraints=[
            "Derived Content Bench context pack — does not rewrite source docs",
            "No live credentials, PAN, or secrets",
            "Extraction backend recorded in provenance / honest_label "
            "(heuristic default; optional real DocETL via --discovery)",
        ],
        linked_workflow_id=record.linked_workflow_id,
    )
    return pack


def write_context_pack(pack: ContextPack) -> Path:
    CONTEXT_PACK_DIR.mkdir(parents=True, exist_ok=True)
    path = CONTEXT_PACK_DIR / f"{pack.source_id}.context_pack.json"
    path.write_text(json.dumps(pack.to_dict(), indent=2) + "\n", encoding="utf-8")
    return path


def maybe_contract_bundle_path(workflow_id: Optional[str]) -> Optional[str]:
    if not workflow_id:
        return None
    path = ROOT / "artifacts" / "contracts" / f"{workflow_id}.contract_bundle.json"
    if path.exists():
        return repo_relative(path)
    return None
