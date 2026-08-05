"""Optional real DocETL adapter for confusion → extraction discovery.

Modes mirror content-engine discovery:
  heuristic   — local regex extract (default; no docetl import)
  docetl      — docetl Frame.code_map over raw questions (no LLM)
  docetl-llm  — docetl Frame.map (requires LLM API key)
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Tuple

from relay_bench.content_engine.docetl_adapter import (
    EXTRACT_MODES,
    DocETLUnavailableError,
    docetl_available,
    honesty_label,
    llm_api_key_present,
    normalize_extract_mode,
)
from relay_bench.discovery import (
    extract_from_question,
    load_raw_questions,
    suggest_workflow,
)
from relay_bench.schemas import Extraction, RawQuestion, WorkflowSuggestion

_CODE_MAP_TRANSFORM = r'''
def transform(doc):
    import re

    ENTITY_PATTERNS = [
        (r"\bflex\b", "Flex"),
        (r"\bmicroform\b", "Microform"),
        (r"\btms\b", "TMS"),
        (r"\btransienttokenjwt\b", "transientTokenJwt"),
        (r"\bcreateinstrument\b", "createInstrument"),
        (r"\bhttp signature\b", "HTTP Signature"),
        (r"\bauthentication failed\b", "Authentication Failed"),
        (r"\bkeyid\b", "keyId"),
        (r"\bsecretkey\b", "secretKey"),
        (r"\bmerchantkeyid\b", "merchantKeyId"),
        (r"\bv-c-merchant-id\b", "v-c-merchant-id"),
        (r"\bapitest(?:\.cybersource\.com)?\b", "apitest.cybersource.com"),
        (r"\bpayer authentication\b", "Payer Authentication"),
        (r"\b3ds\b", "3DS"),
        (r"\benrollment\b", "enrollment"),
        (r"\bchallenge\b", "challenge"),
        (r"\bfrictionless\b", "frictionless"),
        (r"\bauthorization\b", "authorization"),
    ]

    text = doc.get("question") or ""
    lower = text.lower()
    entities = []
    for pattern, label in ENTITY_PATTERNS:
        if re.search(pattern, lower) and label not in entities:
            entities.append(label)

    parts = re.split(r"[.!?]+\s+|\s+[—\-]\s+|\s+and\s+I\b|\s+and\s+I'?m\b", text)
    symptoms = []
    for part in parts:
        clause = part.strip(" .?—-")
        if len(clause) < 24:
            continue
        low = clause.lower()
        if any(
            marker in low
            for marker in (
                "reject",
                "fail",
                "wrong",
                "miss",
                "not sure",
                "immediately",
                "persist",
                "returns",
                "authorize",
            )
        ):
            if clause not in symptoms:
                symptoms.append(clause)
    symptoms = symptoms[:5] or [text.strip()]

    goal_match = re.search(
        r"((?:where|what|can|am i|how|which)[^?]+\?)",
        text,
        flags=re.IGNORECASE,
    )
    if goal_match:
        goal = goal_match.group(1).strip()
    elif entities:
        goal = f"Resolve developer confusion involving {', '.join(entities[:4])}"
    else:
        goal = text.strip().split("?")[0].strip() + "?"

    confidence = min(0.95, 0.45 + 0.1 * len(entities) + 0.05 * len(symptoms))
    return {
        "seed_id": doc.get("seed_id"),
        "goal": goal,
        "symptoms": symptoms,
        "entities": entities,
        "confidence": round(confidence, 2),
    }
'''


def _extract_via_code_map(questions: List[RawQuestion]) -> List[Extraction]:
    try:
        import docetl
    except ImportError as exc:
        raise DocETLUnavailableError(
            "docetl package is not installed; pip install docetl "
            "or use --discovery heuristic"
        ) from exc

    docs = [
        {
            "seed_id": q.seed_id,
            "question": q.question,
            "source": q.source,
            "channel": q.channel,
        }
        for q in questions
    ]
    rows = (
        docetl.from_list(docs, name="questions")
        .code_map(name="extract_goal_symptoms_entities", code=_CODE_MAP_TRANSFORM)
        .collect()
    )
    by_id = {str(r["seed_id"]): r for r in rows}
    extractions: List[Extraction] = []
    for question in questions:
        row = by_id[question.seed_id]
        extractions.append(
            Extraction(
                seed_id=question.seed_id,
                goal=str(row["goal"]),
                symptoms=list(row.get("symptoms") or []),
                entities=list(row.get("entities") or []),
                confidence=float(row.get("confidence") or 0.0),
            )
        )
    return extractions


def _extract_via_llm_map(questions: List[RawQuestion]) -> List[Extraction]:
    if not llm_api_key_present():
        raise DocETLUnavailableError(
            "docetl-llm requires an LLM API key; none are set"
        )
    try:
        import docetl
    except ImportError as exc:
        raise DocETLUnavailableError(
            "docetl package is not installed; pip install docetl "
            "or use --discovery heuristic"
        ) from exc

    docs = [
        {
            "seed_id": q.seed_id,
            "question": q.question,
            "source": q.source,
            "channel": q.channel,
        }
        for q in questions
    ]
    prompt = (
        "From this developer support/docs question, extract:\n"
        "- goal: the developer's intent as a short question or statement\n"
        "- symptoms: concrete failure/confusion clauses\n"
        "- entities: product/API terms (Flex, Microform, TMS, 3DS, etc.)\n"
        "- confidence: 0-1\n\n"
        "Question: {{ input.question }}"
    )
    rows = (
        docetl.from_list(docs, name="questions")
        .map(
            name="extract_goal_symptoms_entities_llm",
            prompt=prompt,
            output={
                "schema": {
                    "goal": "str",
                    "symptoms": "list[str]",
                    "entities": "list[str]",
                    "confidence": "float",
                }
            },
        )
        .collect()
    )
    by_id = {str(r.get("seed_id", docs[i]["seed_id"])): r for i, r in enumerate(rows)}
    extractions: List[Extraction] = []
    for question in questions:
        row = by_id[question.seed_id]
        extractions.append(
            Extraction(
                seed_id=question.seed_id,
                goal=str(row["goal"]),
                symptoms=list(row.get("symptoms") or []),
                entities=list(row.get("entities") or []),
                confidence=float(row.get("confidence") or 0.0),
            )
        )
    return extractions


def extract_questions_with_backend(
    questions: List[RawQuestion],
    mode: Optional[str] = None,
    *,
    fallback_on_error: bool = False,
) -> Tuple[List[Extraction], Dict[str, str]]:
    resolved = normalize_extract_mode(mode)
    if resolved == "heuristic":
        return (
            [extract_from_question(q) for q in questions],
            honesty_label("heuristic", executed=False),
        )
    try:
        if resolved == "docetl":
            return (
                _extract_via_code_map(questions),
                honesty_label("docetl", executed=True),
            )
        return (
            _extract_via_llm_map(questions),
            honesty_label("docetl-llm", executed=True),
        )
    except DocETLUnavailableError as exc:
        if not fallback_on_error:
            raise
        return (
            [extract_from_question(q) for q in questions],
            honesty_label(
                resolved,
                executed=False,
                detail=f"fallback-to-heuristic: {exc}",
            ),
        )


def discover_suggestions_with_backend(
    questions: Optional[Iterable[RawQuestion]] = None,
    mode: Optional[str] = None,
    *,
    fallback_on_error: bool = False,
) -> Tuple[List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]], Dict[str, str]]:
    qlist = list(questions) if questions is not None else load_raw_questions()
    extractions, label = extract_questions_with_backend(
        qlist, mode=mode, fallback_on_error=fallback_on_error
    )
    rows: List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]] = []
    for question, extraction in zip(qlist, extractions):
        rows.append((question, extraction, suggest_workflow(extraction)))
    return rows, label


__all__ = [
    "EXTRACT_MODES",
    "DocETLUnavailableError",
    "discover_suggestions_with_backend",
    "docetl_available",
    "extract_questions_with_backend",
    "normalize_extract_mode",
]
