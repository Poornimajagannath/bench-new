"""Segment normalized markdown into semantically typed blocks."""

from __future__ import annotations

import re
from typing import List, Tuple

from content_bench.content_engine.schemas import DocumentSegment, NormalizedDocument

_HEADING_RE = re.compile(r"^(#{2,4})\s+(.+)$")


def _classify_heading(heading: str, source_type: str) -> Tuple[str, str]:
    h = heading.lower().strip()
    if h == "overview" or h.startswith("overview"):
        return "paragraph", "concept"
    if "prerequisite" in h:
        return "metadata", "quickstart"
    if re.match(r"^\d+\.", h):
        return "step", "quickstart"
    if h in {"steps", "step"}:
        return "metadata", "quickstart"
    if "validation" in h:
        return "step", "quickstart"
    if "warning" in h:
        return "warning", "troubleshooting"
    if "next step" in h:
        return "paragraph", "quickstart"
    if source_type == "quickstart":
        return "paragraph", "quickstart"
    return "paragraph", "concept"


def segment_document(doc: NormalizedDocument) -> List[DocumentSegment]:
    lines = doc.normalized_markdown.splitlines()
    segments: List[DocumentSegment] = []
    current_heading = "root"
    current_level_path = ["root"]
    buf: List[str] = []
    order = 0

    def flush() -> None:
        nonlocal order, buf
        body = "\n".join(buf).strip()
        if not body and current_heading == "root":
            buf = []
            return
        segment_type, classification = _classify_heading(current_heading, doc.page_type)
        if body.startswith("- ") or "Failure modes:" in body:
            if "failure" in body.lower() or "warning" in current_heading.lower():
                segment_type = "warning"
        segments.append(
            DocumentSegment(
                segment_id=f"{doc.doc_id}:seg-{order:03d}",
                doc_id=doc.doc_id,
                heading_path=list(current_level_path),
                segment_type=segment_type,
                classification=classification,
                order_index=order,
                markdown=body,
                source_span=current_heading,
            )
        )
        order += 1
        buf = []

    for line in lines:
        heading = _HEADING_RE.match(line)
        if heading:
            flush()
            hashes, title = heading.group(1), heading.group(2).strip()
            level = len(hashes)
            current_heading = title
            # Keep a shallow path: H2 resets, deeper appends.
            if level <= 2:
                current_level_path = [title]
            else:
                current_level_path = current_level_path[:1] + [title]
            continue
        buf.append(line)
    flush()
    return segments
