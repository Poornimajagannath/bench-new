"""Source registry loader — per-product config files under registry/.

Engine upstream: content-bench. This private repo configures products here;
do not fork engine modules for product-specific lists.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Union

from content_bench.content_engine.schemas import SourceRecord

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY_DIR = ROOT / "registry"
# Legacy single-file path kept for one release as a fallback.
LEGACY_REGISTRY = ROOT / "data" / "content_engine" / "source_registry.json"


def _record_from_item(item: dict) -> SourceRecord:
    return SourceRecord(
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


def _load_items_from_file(path: Path) -> List[dict]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        items = raw.get("sources") or raw.get("items") or []
        if not isinstance(items, list):
            raise ValueError(f"No sources list in {path}")
        return items
    raise ValueError(f"Unsupported registry shape in {path}")


def load_registry(path: Optional[Union[Path, str]] = None) -> Dict[str, SourceRecord]:
    """Load all product registries, or a single file if path is given."""
    records: Dict[str, SourceRecord] = {}

    if path is not None:
        items = _load_items_from_file(Path(path))
        for item in items:
            rec = _record_from_item(item)
            records[rec.source_id] = rec
        return records

    registry_dir = DEFAULT_REGISTRY_DIR
    if registry_dir.is_dir():
        json_files = sorted(registry_dir.glob("*.json"))
        for file_path in json_files:
            for item in _load_items_from_file(file_path):
                rec = _record_from_item(item)
                if rec.source_id in records:
                    raise ValueError(
                        f"Duplicate source_id={rec.source_id!r} in {file_path.name}"
                    )
                records[rec.source_id] = rec
        if records:
            return records

    if LEGACY_REGISTRY.exists():
        for item in _load_items_from_file(LEGACY_REGISTRY):
            rec = _record_from_item(item)
            records[rec.source_id] = rec
        return records

    raise FileNotFoundError(
        f"No registry JSON in {registry_dir}/ and no legacy {LEGACY_REGISTRY}"
    )


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


def list_product_sources(product: str, path: Optional[Path] = None) -> List[SourceRecord]:
    needle = product.lower()
    return [
        r
        for r in list_enabled_sources(path)
        if needle in [p.lower() for p in r.product]
    ]
