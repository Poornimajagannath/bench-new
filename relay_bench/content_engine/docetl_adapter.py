"""Optional real DocETL adapter for Content Engine extraction.

Modes:
  heuristic   — local regex extract; does not import docetl (default)
  docetl      — imports ucbepic/docetl and runs Frame.code_map (no LLM)
  docetl-llm  — imports docetl and runs Frame.map (requires LLM API key)

Honesty: only label a run as DocETL-backed when the package actually executed.
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple

from relay_bench.content_engine.extract import (
    _step_number,
    extract_quickstart_units,
)
from relay_bench.content_engine.schemas import (
    DocumentSegment,
    NormalizedDocument,
    QuickstartUnit,
    SourceRecord,
)

EXTRACT_MODES = ("heuristic", "docetl", "docetl-llm")

_LLM_KEY_ENVS = (
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "AZURE_OPENAI_API_KEY",
    "LITELLM_API_KEY",
)

_CODE_MAP_TRANSFORM = r'''
def transform(doc):
    """Per-segment field extract via DocETL code_map (no LLM)."""
    import re

    UNIT_TYPES = {
        "overview": "overview",
        "prerequisites": "prerequisite",
        "prerequisite": "prerequisite",
        "validation checks": "validation_check",
        "warnings": "warning",
        "next steps": "next_step",
    }

    def field(pattern, text):
        match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
        return match.group(1).strip() if match else None

    def list_field(label, text):
        value = field(rf"^{label}:\s*(.+)$", text)
        if not value:
            return []
        return [part.strip() for part in re.split(r",|;", value) if part.strip()]

    def evidence(text):
        quoted = re.findall(r'Evidence:\s*"([^"]+)"', text)
        if quoted:
            return quoted
        compact = " ".join(text.split())
        if len(compact) > 160:
            compact = compact[:157] + "..."
        return [compact] if compact else []

    def unit_type_for_heading(heading):
        key = heading.strip().lower()
        if key in {"steps", "step"}:
            return None
        if key in UNIT_TYPES:
            return UNIT_TYPES[key]
        if re.match(r"^\d+\.", key):
            return "step"
        return None

    heading = doc.get("heading") or "root"
    body = (doc.get("body") or "").strip()
    unit_type = unit_type_for_heading(heading)
    if unit_type is None or not body or heading == "root":
        return {"skip": True}

    title = re.sub(r"^\d+\.\s*", "", heading).strip()
    api_entities = []
    blob = (title + " " + body).lower()
    for token in (
        "Microform",
        "Payer Authentication",
        "enrollment",
        "challenge",
        "frictionless",
        "authorization",
        "3DS",
    ):
        if token.lower() in blob:
            api_entities.append(token)

    requires = list_field("Requires", body)
    confidence = 0.9 if evidence(body) and (requires or unit_type != "step") else 0.75
    if unit_type == "step" and not requires:
        confidence = 0.55

    return {
        "skip": False,
        "unit_type": unit_type,
        "title": title,
        "body_markdown": body,
        "requires": requires,
        "outcomes": list_field("Outcome", body),
        "failure_modes": list_field("Failure modes", body),
        "evidence_quotes": evidence(body),
        "api_entities": api_entities,
        "confidence": confidence,
        "heading": heading,
        "source_span": doc.get("source_span") or "",
        "index": doc.get("index", 0),
    }
'''


class DocETLUnavailableError(RuntimeError):
    """Raised when a DocETL-backed mode cannot run honestly."""


def normalize_extract_mode(mode: Optional[str]) -> str:
    raw = (mode or os.environ.get("RELAY_DISCOVERY") or "heuristic").strip().lower()
    # Accept plan alias "--discovery docetl"
    aliases = {
        "style": "heuristic",
        "style-only": "heuristic",
        "local": "heuristic",
        "code_map": "docetl",
        "docetl-code": "docetl",
        "llm": "docetl-llm",
        "docetl_llm": "docetl-llm",
    }
    resolved = aliases.get(raw, raw)
    if resolved not in EXTRACT_MODES:
        raise ValueError(
            f"Unknown extract mode {mode!r}; expected one of {EXTRACT_MODES}"
        )
    return resolved


def docetl_available() -> bool:
    try:
        import docetl  # noqa: F401
    except ImportError:
        return False
    return True


def llm_api_key_present() -> bool:
    return any(os.environ.get(name) for name in _LLM_KEY_ENVS)


def honesty_label(mode: str, *, executed: bool, detail: str = "") -> Dict[str, str]:
    if mode == "heuristic" or not executed:
        label = {
            "docetl": "style-only",
            "extract_mode": mode,
            "tempo_harbor": "preview-via-linked-contract-if-present",
            "network": "denied",
        }
    elif mode == "docetl":
        label = {
            "docetl": "imported-code_map",
            "extract_mode": mode,
            "tempo_harbor": "preview-via-linked-contract-if-present",
            "network": "denied",
        }
    else:
        label = {
            "docetl": "imported-llm-map",
            "extract_mode": mode,
            "tempo_harbor": "preview-via-linked-contract-if-present",
            "network": "llm-provider-via-docetl",
        }
    if detail:
        label["detail"] = detail
    return label


def _segments_as_docs(segments: List[DocumentSegment]) -> List[Dict[str, Any]]:
    docs: List[Dict[str, Any]] = []
    for index, segment in enumerate(segments):
        heading = segment.heading_path[-1] if segment.heading_path else segment.source_span
        docs.append(
            {
                "index": index,
                "heading": heading,
                "heading_path": list(segment.heading_path),
                "source_span": segment.source_span,
                "body": segment.markdown,
            }
        )
    return docs


def _entity_hints(title: str, body: str) -> List[str]:
    api_entities: List[str] = []
    blob = (title + " " + body).lower()
    for token in (
        "Microform",
        "Payer Authentication",
        "enrollment",
        "challenge",
        "frictionless",
        "authorization",
        "3DS",
    ):
        if token.lower() in blob:
            api_entities.append(token)
    return api_entities


def _build_units_from_rows(
    record: SourceRecord,
    doc: NormalizedDocument,
    rows: List[Dict[str, Any]],
) -> List[QuickstartUnit]:
    goal = doc.extracted_metadata.get("goal") or doc.title
    # Preserve document order.
    ordered = sorted(rows, key=lambda r: int(r.get("index", 0)))
    units: List[QuickstartUnit] = []
    seq = 0
    for row in ordered:
        if row.get("skip"):
            continue
        unit_type = str(row["unit_type"])
        title = str(row["title"])
        body = str(row.get("body_markdown") or "")
        heading = str(row.get("heading") or title)

        if unit_type == "step":
            seq = _step_number(heading, seq + 1)
            sequence_number = seq
        else:
            sequence_number = 0 if unit_type in {"overview", "prerequisite"} else seq + 1

        requires = list(row.get("requires") or [])
        outcomes = list(row.get("outcomes") or [])
        failure_modes = list(row.get("failure_modes") or [])
        evidence = list(row.get("evidence_quotes") or [])
        api_entities = list(row.get("api_entities") or _entity_hints(title, body))
        confidence = float(row.get("confidence") or 0.75)

        units.append(
            QuickstartUnit(
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
                api_entities=api_entities,
                requires=requires,
                outcomes=outcomes,
                failure_modes=failure_modes,
                confidence=confidence,
                evidence_quotes=evidence,
            )
        )
    return units


def _extract_via_code_map(
    record: SourceRecord,
    doc: NormalizedDocument,
    segments: List[DocumentSegment],
) -> List[QuickstartUnit]:
    try:
        import docetl
    except ImportError as exc:
        raise DocETLUnavailableError(
            "docetl package is not installed; pip install docetl "
            "or use --discovery heuristic"
        ) from exc

    frame = docetl.from_list(_segments_as_docs(segments), name="segments")
    rows = frame.code_map(
        name="extract_quickstart_fields",
        code=_CODE_MAP_TRANSFORM,
    ).collect()
    return _build_units_from_rows(record, doc, rows)


def _extract_via_llm_map(
    record: SourceRecord,
    doc: NormalizedDocument,
    segments: List[DocumentSegment],
) -> List[QuickstartUnit]:
    if not llm_api_key_present():
        raise DocETLUnavailableError(
            "docetl-llm requires an LLM API key "
            f"(one of {', '.join(_LLM_KEY_ENVS)}); none are set"
        )
    try:
        import docetl
    except ImportError as exc:
        raise DocETLUnavailableError(
            "docetl package is not installed; pip install docetl "
            "or use --discovery heuristic"
        ) from exc

    goal = doc.extracted_metadata.get("goal") or doc.title
    prompt = (
        "Extract a quickstart knowledge unit from this documentation segment.\n"
        f"Overall goal: {goal}\n"
        "Heading: {{ input.heading }}\n"
        "Body:\n{{ input.body }}\n\n"
        "If the heading is only a container (e.g. 'Steps') or the segment has no "
        "actionable content, set skip=true.\n"
        "unit_type must be one of: overview, prerequisite, step, validation_check, "
        "warning, next_step.\n"
        "evidence_quotes must be short grounded snippets copied from the body."
    )
    output_schema = {
        "skip": "bool",
        "unit_type": "str",
        "title": "str",
        "body_markdown": "str",
        "requires": "list[str]",
        "outcomes": "list[str]",
        "failure_modes": "list[str]",
        "evidence_quotes": "list[str]",
        "api_entities": "list[str]",
        "confidence": "float",
    }
    frame = docetl.from_list(_segments_as_docs(segments), name="segments")
    rows = frame.map(
        name="extract_quickstart_llm",
        prompt=prompt,
        output={"schema": output_schema},
    ).collect()
    return _build_units_from_rows(record, doc, rows)


def extract_quickstart_units_with_backend(
    record: SourceRecord,
    doc: NormalizedDocument,
    segments: List[DocumentSegment],
    mode: Optional[str] = None,
    *,
    fallback_on_error: bool = False,
) -> Tuple[List[QuickstartUnit], Dict[str, str]]:
    """Run extraction for the requested backend.

    Returns (units, honest_label).
    """
    resolved = normalize_extract_mode(mode)
    if resolved == "heuristic":
        units = extract_quickstart_units(record, doc, segments)
        return units, honesty_label("heuristic", executed=False)

    try:
        if resolved == "docetl":
            units = _extract_via_code_map(record, doc, segments)
            return units, honesty_label("docetl", executed=True)
        units = _extract_via_llm_map(record, doc, segments)
        return units, honesty_label("docetl-llm", executed=True)
    except DocETLUnavailableError as exc:
        if not fallback_on_error:
            raise
        units = extract_quickstart_units(record, doc, segments)
        return units, honesty_label(
            resolved,
            executed=False,
            detail=f"fallback-to-heuristic: {exc}",
        )


__all__ = [
    "EXTRACT_MODES",
    "DocETLUnavailableError",
    "docetl_available",
    "extract_quickstart_units_with_backend",
    "honesty_label",
    "llm_api_key_present",
    "normalize_extract_mode",
]
