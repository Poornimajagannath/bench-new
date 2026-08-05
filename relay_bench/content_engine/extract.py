"""DocETL-style extraction of quickstart units from segments.

V0 does NOT import `docetl`. This is a local heuristic extractor that emits
the same typed `quickstart_unit` shapes a real DocETL map could produce later.
"""

from __future__ import annotations

import re
from typing import List, Optional

from relay_bench.content_engine.schemas import (
    DocumentSegment,
    NormalizedDocument,
    QuickstartUnit,
    SourceRecord,
)

_UNIT_TYPES = {
    "overview": "overview",
    "prerequisites": "prerequisite",
    "prerequisite": "prerequisite",
    "validation checks": "validation_check",
    "warnings": "warning",
    "next steps": "next_step",
}


def _field(pattern: str, text: str) -> Optional[str]:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else None


def _list_field(label: str, text: str) -> List[str]:
    # Supports "Requires: a, b" and "Requires: a"
    value = _field(rf"^{label}:\s*(.+)$", text)
    if not value:
        return []
    return [part.strip() for part in re.split(r",|;", value) if part.strip()]


def _evidence(text: str) -> List[str]:
    quoted = re.findall(r'Evidence:\s*"([^"]+)"', text)
    if quoted:
        return quoted
    # Fall back to a short grounded snippet from the segment body.
    compact = " ".join(text.split())
    if len(compact) > 160:
        compact = compact[:157] + "..."
    return [compact] if compact else []


def _step_number(heading: str, fallback: int) -> int:
    match = re.match(r"^(\d+)\.", heading.strip())
    if match:
        return int(match.group(1))
    return fallback


def _unit_type_for_heading(heading: str) -> Optional[str]:
    key = heading.strip().lower()
    # Container headings hold child steps; they are not units themselves.
    if key in {"steps", "step"}:
        return None
    if key in _UNIT_TYPES:
        return _UNIT_TYPES[key]
    if re.match(r"^\d+\.", key):
        return "step"
    return None


def extract_quickstart_units(
    record: SourceRecord,
    doc: NormalizedDocument,
    segments: List[DocumentSegment],
) -> List[QuickstartUnit]:
    goal = doc.extracted_metadata.get("goal") or doc.title
    units: List[QuickstartUnit] = []
    seq = 0

    for segment in segments:
        heading = segment.heading_path[-1] if segment.heading_path else segment.source_span
        # Skip pure metadata preface without a section heading.
        if heading == "root":
            continue

        unit_type = _unit_type_for_heading(heading)
        if unit_type is None:
            continue

        body = segment.markdown.strip()
        if not body:
            continue

        if unit_type == "step":
            seq = _step_number(heading, seq + 1)
            sequence_number = seq
        else:
            sequence_number = 0 if unit_type in {"overview", "prerequisite"} else seq + 1

        title = re.sub(r"^\d+\.\s*", "", heading).strip()
        requires = _list_field("Requires", body)
        outcomes = _list_field("Outcome", body)
        failure_modes = _list_field("Failure modes", body)
        evidence = _evidence(body)

        # Lightweight entity hints from known vocabulary.
        api_entities = []
        for token in (
            "Microform",
            "Payer Authentication",
            "enrollment",
            "challenge",
            "frictionless",
            "authorization",
            "3DS",
        ):
            if token.lower() in (title + " " + body).lower():
                api_entities.append(token)

        confidence = 0.9 if evidence and (requires or unit_type != "step") else 0.75
        if unit_type == "step" and not requires:
            confidence = 0.55

        units.append(
            QuickstartUnit(
                unit_id=f"{record.source_id}:{unit_type}:{sequence_number}:{title.lower().replace(' ', '-')[:48]}",
                source_page_id=doc.doc_id,
                unit_type=unit_type,
                title=title,
                goal=goal,
                product=list(record.product),
                audience=list(record.audience),
                task=[record.linked_workflow_id or record.source_id],
                sequence_number=sequence_number,
                body_markdown=body,
                commands=[],
                api_entities=api_entities,
                requires=requires,
                outcomes=outcomes,
                failure_modes=failure_modes,
                confidence=confidence,
                evidence_quotes=evidence,
            )
        )

    return units
