"""Immutable local snapshots — no network fetch in V0."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from relay_bench.content_engine.schemas import SourceRecord, SourceSnapshot
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_ARTIFACT_DIR = ROOT / "artifacts" / "content_engine" / "snapshots"


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def materialize_snapshot(record: SourceRecord) -> SourceSnapshot:
    """Copy a registered local fixture into an immutable hashed snapshot artifact."""
    source_path = ROOT / record.repo_path
    if not source_path.exists():
        raise FileNotFoundError(f"Registered source path missing: {record.repo_path}")

    text = source_path.read_text(encoding="utf-8")
    content_hash = _sha256_text(text)
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    snapshot_id = f"{record.source_id}-{content_hash[:12]}"

    SNAPSHOT_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = SNAPSHOT_ARTIFACT_DIR / f"{snapshot_id}.md"
    meta_path = SNAPSHOT_ARTIFACT_DIR / f"{snapshot_id}.json"
    raw_path.write_text(text, encoding="utf-8")

    snapshot = SourceSnapshot(
        snapshot_id=snapshot_id,
        source_id=record.source_id,
        fetched_at=fetched_at,
        content_hash=content_hash,
        version_tag=content_hash[:12],
        mime_type="text/markdown",
        raw_bytes_location=repo_relative(raw_path),
        canonical_url=record.canonical_url,
        upstream_last_modified="",
    )
    meta_path.write_text(json.dumps(snapshot.to_dict(), indent=2) + "\n", encoding="utf-8")
    return snapshot


def read_snapshot_text(snapshot: SourceSnapshot) -> str:
    path = ROOT / snapshot.raw_bytes_location
    return path.read_text(encoding="utf-8")
