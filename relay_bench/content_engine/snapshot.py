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
    snapshot_id = f"{record.source_id}-{content_hash[:12]}"
    suffix = source_path.suffix or ".txt"
    mime_type = {
        ".md": "text/markdown",
        ".markdown": "text/markdown",
        ".json": "application/json",
        ".yaml": "application/yaml",
        ".yml": "application/yaml",
    }.get(suffix.lower(), "text/plain")

    SNAPSHOT_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = SNAPSHOT_ARTIFACT_DIR / f"{snapshot_id}{suffix}"
    # Avoid clobbering JSON raw snapshots: meta uses .meta.json for .json sources.
    if suffix.lower() == ".json":
        meta_path = SNAPSHOT_ARTIFACT_DIR / f"{snapshot_id}.meta.json"
    else:
        meta_path = SNAPSHOT_ARTIFACT_DIR / f"{snapshot_id}.json"
    raw_path.write_text(text, encoding="utf-8")

    # Reuse prior metadata for the same content-addressed snapshot so reruns
    # stay deterministic (fetched_at must not churn the artifact).
    if meta_path.exists():
        prior = json.loads(meta_path.read_text(encoding="utf-8"))
        if prior.get("content_hash") == content_hash:
            return SourceSnapshot(**prior)

    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    snapshot = SourceSnapshot(
        snapshot_id=snapshot_id,
        source_id=record.source_id,
        fetched_at=fetched_at,
        content_hash=content_hash,
        version_tag=content_hash[:12],
        mime_type=mime_type,
        raw_bytes_location=repo_relative(raw_path),
        canonical_url=record.canonical_url,
        upstream_last_modified="",
    )
    meta_path.write_text(json.dumps(snapshot.to_dict(), indent=2) + "\n", encoding="utf-8")
    return snapshot


def read_snapshot_text(snapshot: SourceSnapshot) -> str:
    path = ROOT / snapshot.raw_bytes_location
    return path.read_text(encoding="utf-8")
