"""Heuristic extraction of quickstart units from segments.

Default Content Engine path does NOT import `docetl`. For the real DocETL
package adapter (Frame.code_map / Frame.map), see `docetl_adapter.py`.

Supports:
- Fixture quickstarts with `### N. Title` + Requires/Outcome/Evidence
- Real lab docs (context/, scenarios/, templates/) with section headings
  and numbered lists under Context / Expected Behavior / etc.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

from relay_bench.content_engine.schemas import (
    DocumentSegment,
    NormalizedDocument,
    QuickstartUnit,
    SourceRecord,
)

_UNIT_TYPES = {
    "overview": "overview",
    "question": "overview",
    "purpose": "overview",
    "prerequisites": "prerequisite",
    "prerequisite": "prerequisite",
    "credential loading": "prerequisite",
    "required environment variables": "prerequisite",
    "inputs": "prerequisite",
    "sdk installation": "prerequisite",
    "validation checks": "validation_check",
    "success criteria": "validation_check",
    "warnings": "warning",
    "common gotchas": "warning",
    "error categories to track": "warning",
    "what sandbox does not simulate": "warning",
    "next steps": "next_step",
    "resources": "next_step",
    "agent instruction": "next_step",
    "auth error taxonomy": "troubleshooting",
    "sdk field names (known gap)": "troubleshooting",
    "sdk models used": "overview",
    "sandbox behavior": "overview",
    "what sandbox simulates": "overview",
    "test cards": "prerequisite",
    "sandbox testing": "prerequisite",
    "preferred patterns (from llms.txt)": "overview",
    "documentation": "overview",
    "mcp (agent toolkit)": "overview",
    "known doc gaps": "warning",
    "files": "overview",
}

# Sections that hold numbered developer actions → expand into step units.
_STEP_CONTAINER_HEADINGS = {
    "steps",
    "step",
    "context",
    "expected behavior",
    "developer needs to",
    "the developer needs to",
}

_ENTITY_TOKENS = (
    "Microform",
    "Payer Authentication",
    "enrollment",
    "challenge",
    "frictionless",
    "authorization",
    "3DS",
    "HTTP Signature",
    "Flex",
    "TMS",
    "Unified Checkout",
    "merchantKeyId",
    "merchantsecretKey",
)


def _field(pattern: str, text: str) -> Optional[str]:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else None


def _list_field(label: str, text: str) -> List[str]:
    value = _field(rf"^{label}:\s*(.+)$", text)
    if not value:
        return []
    return [part.strip() for part in re.split(r",|;", value) if part.strip()]


def _evidence(text: str) -> List[str]:
    quoted = re.findall(r'Evidence:\s*"([^"]+)"', text)
    if quoted:
        return quoted
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
    if key in _STEP_CONTAINER_HEADINGS:
        return None
    if key in _UNIT_TYPES:
        return _UNIT_TYPES[key]
    if re.match(r"^\d+\.", key):
        return "step"
    return None


def _entity_hints(title: str, body: str) -> List[str]:
    api_entities: List[str] = []
    blob = (title + " " + body).lower()
    for token in _ENTITY_TOKENS:
        if token.lower() in blob:
            api_entities.append(token)
    return api_entities


def _numbered_items(body: str) -> List[Tuple[int, str, str]]:
    """Parse `1. action` / `1. **action**` blocks into (n, title, item_body)."""
    lines = body.splitlines()
    items: List[Tuple[int, str, List[str]]] = []
    current: Optional[Tuple[int, str, List[str]]] = None
    item_re = re.compile(r"^(\d+)\.\s+(.*)$")

    for line in lines:
        match = item_re.match(line.strip())
        if match:
            if current is not None:
                items.append(current)
            num = int(match.group(1))
            rest = match.group(2).strip()
            rest = re.sub(r"^\*\*(.+?)\*\*$", r"\1", rest)
            current = (num, rest, [])
            continue
        if current is not None:
            current[2].append(line)

    if current is not None:
        items.append(current)

    out: List[Tuple[int, str, str]] = []
    for num, title, buf in items:
        item_body = "\n".join(buf).strip()
        full = title if not item_body else f"{title}\n{item_body}"
        out.append((num, title[:120] or f"Step {num}", full))
    return out


def parse_segment_rows(heading: str, body: str) -> List[Dict[str, Any]]:
    """Return zero or more raw unit field dicts for one segment.

    Used by both the heuristic extractor and DocETL code_map (via import).
    """
    body = (body or "").strip()
    if not body or heading == "root":
        return [{"skip": True, "heading": heading}]

    key = heading.strip().lower()
    rows: List[Dict[str, Any]] = []

    # Numbered heading step (quickstart fixture style).
    if re.match(r"^\d+\.", key):
        title = re.sub(r"^\d+\.\s*", "", heading).strip()
        requires = _list_field("Requires", body)
        evidence = _evidence(body)
        confidence = 0.9 if evidence and requires else 0.75
        if not requires:
            confidence = 0.55
        rows.append(
            {
                "skip": False,
                "unit_type": "step",
                "title": title,
                "body_markdown": body,
                "requires": requires,
                "outcomes": _list_field("Outcome", body),
                "failure_modes": _list_field("Failure modes", body),
                "evidence_quotes": evidence,
                "api_entities": _entity_hints(title, body),
                "confidence": confidence,
                "heading": heading,
            }
        )
        return rows

    # Container sections → one step per numbered list item.
    if key in _STEP_CONTAINER_HEADINGS or (
        _unit_type_for_heading(heading) is None and _numbered_items(body)
    ):
        items = _numbered_items(body)
        if items:
            for num, title, item_body in items:
                evidence = _evidence(item_body)
                rows.append(
                    {
                        "skip": False,
                        "unit_type": "step",
                        "title": title,
                        "body_markdown": item_body,
                        "requires": _list_field("Requires", item_body),
                        "outcomes": _list_field("Outcome", item_body),
                        "failure_modes": _list_field("Failure modes", item_body),
                        "evidence_quotes": evidence,
                        "api_entities": _entity_hints(title, item_body),
                        "confidence": 0.7 if evidence else 0.55,
                        "heading": f"{num}. {title}",
                    }
                )
            return rows
        if key in _STEP_CONTAINER_HEADINGS:
            return [{"skip": True, "heading": heading}]

    unit_type = _unit_type_for_heading(heading)
    if unit_type is None:
        # Fall back: treat unknown substantive sections as overview.
        if len(body) < 40:
            return [{"skip": True, "heading": heading}]
        unit_type = "overview"

    title = re.sub(r"^\d+\.\s*", "", heading).strip()
    requires = _list_field("Requires", body)
    evidence = _evidence(body)
    confidence = 0.85 if evidence else 0.65
    rows.append(
        {
            "skip": False,
            "unit_type": unit_type,
            "title": title,
            "body_markdown": body,
            "requires": requires,
            "outcomes": _list_field("Outcome", body),
            "failure_modes": _list_field("Failure modes", body),
            "evidence_quotes": evidence,
            "api_entities": _entity_hints(title, body),
            "confidence": confidence,
            "heading": heading,
        }
    )
    return rows


def _build_unit(
    record: SourceRecord,
    doc: NormalizedDocument,
    row: Dict[str, Any],
    sequence_number: int,
) -> QuickstartUnit:
    goal = doc.extracted_metadata.get("goal") or doc.title
    unit_type = str(row["unit_type"])
    title = str(row["title"])
    body = str(row.get("body_markdown") or "")
    return QuickstartUnit(
        unit_id=(
            f"{record.source_id}:{unit_type}:{sequence_number}:"
            f"{title.lower().replace(' ', '-')[:48]}"
        ),
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
        api_entities=list(row.get("api_entities") or []),
        requires=list(row.get("requires") or []),
        outcomes=list(row.get("outcomes") or []),
        failure_modes=list(row.get("failure_modes") or []),
        confidence=float(row.get("confidence") or 0.7),
        evidence_quotes=list(row.get("evidence_quotes") or []),
    )


def extract_quickstart_units(
    record: SourceRecord,
    doc: NormalizedDocument,
    segments: List[DocumentSegment],
) -> List[QuickstartUnit]:
    units: List[QuickstartUnit] = []
    seq = 0

    for segment in segments:
        heading = segment.heading_path[-1] if segment.heading_path else segment.source_span
        rows = parse_segment_rows(heading, segment.markdown)
        for row in rows:
            if row.get("skip"):
                continue
            unit_type = str(row["unit_type"])
            heading_for_seq = str(row.get("heading") or heading)
            if unit_type == "step":
                hinted = _step_number(heading_for_seq, seq + 1)
                # Nested lists often restart at 1; keep global monotonic sequence.
                seq = hinted if hinted > seq else seq + 1
                sequence_number = seq
            else:
                sequence_number = (
                    0 if unit_type in {"overview", "prerequisite"} else seq + 1
                )
            units.append(_build_unit(record, doc, row, sequence_number))

    return units
