"""Optional real DocETL adapter for Content Engine extraction.

Modes:
  heuristic   — local extract; does not import docetl (default)
  docetl      — imports ucbepic/docetl and runs Frame.code_map (no LLM)
  docetl-llm  — imports docetl and runs Frame.map (requires LLM API key)

Honesty: only label a run as DocETL-backed when the package actually executed.
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple

from content_bench.content_engine.extract import (
    _build_unit,
    _step_number,
    extract_quickstart_units,
    parse_segment_rows,
)
from content_bench.content_engine.schemas import (
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

# DocETL code_map executes this string. It imports shared Content Bench parsers so
# heuristic and DocETL backends stay aligned on real-doc shapes.
_CODE_MAP_TRANSFORM = r'''
def transform(doc):
    from content_bench.content_engine.extract import parse_segment_rows

    heading = doc.get("heading") or "root"
    body = doc.get("body") or ""
    rows = parse_segment_rows(heading, body)
    # code_map returns one dict per input doc; pack multi-unit results.
    return {
        "index": doc.get("index", 0),
        "source_span": doc.get("source_span") or "",
        "heading": heading,
        "parsed_rows": rows,
    }
'''


class DocETLUnavailableError(RuntimeError):
    """Raised when a DocETL-backed mode cannot run honestly."""


def normalize_extract_mode(mode: Optional[str]) -> str:
    raw = (mode or os.environ.get("RELAY_DISCOVERY") or "heuristic").strip().lower()
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


def _build_units_from_parsed(
    record: SourceRecord,
    doc: NormalizedDocument,
    packed_rows: List[Dict[str, Any]],
) -> List[QuickstartUnit]:
    ordered = sorted(packed_rows, key=lambda r: int(r.get("index", 0)))
    units: List[QuickstartUnit] = []
    seq = 0
    for packed in ordered:
        for row in packed.get("parsed_rows") or []:
            if row.get("skip"):
                continue
            unit_type = str(row["unit_type"])
            heading_for_seq = str(row.get("heading") or packed.get("heading") or "")
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

    # Ensure shared parser is importable inside DocETL workers.
    _ = parse_segment_rows

    frame = docetl.from_list(_segments_as_docs(segments), name="segments")
    packed = frame.code_map(
        name="extract_quickstart_fields",
        code=_CODE_MAP_TRANSFORM,
    ).collect()
    return _build_units_from_parsed(record, doc, packed)


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
        "If the heading is only a container (e.g. 'Steps') with no actionable "
        "content of its own, set skip=true unless the body has numbered steps "
        "(then prefer one unit summarizing the section).\n"
        "unit_type must be one of: overview, prerequisite, step, validation_check, "
        "warning, troubleshooting, next_step.\n"
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
    packed = [
        {
            "index": row.get("index", i),
            "heading": row.get("heading"),
            "parsed_rows": [row],
        }
        for i, row in enumerate(rows)
    ]
    return _build_units_from_parsed(record, doc, packed)


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
