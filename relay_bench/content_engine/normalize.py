"""Normalize local markdown snapshots into Relay-ready documents."""

from __future__ import annotations

import json
import re
from pathlib import Path

from relay_bench.content_engine.schemas import NormalizedDocument, SourceRecord, SourceSnapshot
from relay_bench.content_engine.snapshot import read_snapshot_text
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = ROOT / "artifacts" / "content_engine" / "normalized"


def _meta_line(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else ""


def normalize_document(
    record: SourceRecord,
    snapshot: SourceSnapshot,
) -> NormalizedDocument:
    raw = read_snapshot_text(snapshot)
    # Strip obvious boilerplate markers; keep structure.
    lines = []
    for line in raw.splitlines():
        if line.strip().lower().startswith("copyright"):
            continue
        lines.append(line.rstrip())
    markdown = "\n".join(lines).strip() + "\n"

    title_match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else record.source_id
    freshness = _meta_line(r"^Freshness:\s*(.+)$", markdown) or "unknown"
    goal = _meta_line(r"^Goal:\s*(.+)$", markdown)
    if not goal:
        # Real scenario docs often put the intent under ## Question.
        q = re.search(
            r"^##\s+Question\s*\n+(.+?)(?:\n##|\Z)",
            markdown,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if q:
            goal = " ".join(q.group(1).split())
    if not goal:
        goal = title

    doc = NormalizedDocument(
        doc_id=f"doc-{record.source_id}",
        source_id=record.source_id,
        snapshot_id=snapshot.snapshot_id,
        title=title,
        canonical_url=record.canonical_url,
        source_format="markdown",
        product=list(record.product),
        audience=list(record.audience),
        page_type=record.source_type,
        freshness_date=freshness,
        normalized_markdown=markdown,
        extracted_metadata={"goal": goal},
    )

    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)
    out = NORMALIZED_DIR / f"{record.source_id}.normalized.json"
    out.write_text(json.dumps(doc.to_dict(), indent=2) + "\n", encoding="utf-8")
    # Keep a sidecar markdown for human inspection.
    md_out = NORMALIZED_DIR / f"{record.source_id}.normalized.md"
    md_out.write_text(markdown, encoding="utf-8")
    _ = repo_relative(out)
    return doc
