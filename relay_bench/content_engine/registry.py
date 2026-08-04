"""Source registry loader for Content Engine V0."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from relay_bench.content_engine.schemas import SourceRecord

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = ROOT / "data" / "content_engine" / "source_registry.json"


def load_registry(path: Optional[Path] = None) -> Dict[str, SourceRecord]:
    registry_path = path or DEFAULT_REGISTRY
    raw = json.loads(registry_path.read_text(encoding="utf-8"))
    records: Dict[str, SourceRecord] = {}
    for item in raw:
        record = SourceRecord(
            source_id=item["source_id"],
            source_type=item["source_type"],
            canonical_url=item["canonical_url"],
            repo_path=item["repo_path"],
            owning_team=item["owning_team"],
            product=list(item.get("product", [])),
            audience=list(item.get("audience", [])),
            refresh_cadence=item.get("refresh_cadence", "manual-fixture"),
            trust_level=item.get("trust_level", "experimental"),
            parser_strategy=item.get("parser_strategy", "markdown_native"),
            enabled=bool(item.get("enabled", True)),
            linked_workflow_id=item.get("linked_workflow_id"),
        )
        records[record.source_id] = record
    return records


def require_source(source_id: str, path: Optional[Path] = None) -> SourceRecord:
    records = load_registry(path)
    record = records.get(source_id)
    if record is None:
        raise LookupError(f"Unknown source_id={source_id!r}")
    if not record.enabled:
        raise LookupError(f"Source {source_id!r} is disabled in the registry")
    return record


def list_enabled_sources(path: Optional[Path] = None) -> List[SourceRecord]:
    return [r for r in load_registry(path).values() if r.enabled]
