"""DocETL-style discovery stages over raw forum/docs/support questions.

Flow (pre-PM):
  raw questions → extract goal/symptoms/entities → suggest workflow_id + stages

No task packs, no verifiers, no network.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from relay_bench.schemas import Extraction, RawQuestion, WorkflowSuggestion

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SEEDS_PATH = ROOT / "data" / "seeds" / "hard_questions.json"

# Catalog used only for suggestion (not pre-labels on raw questions).
_WORKFLOW_CATALOG: Dict[str, Dict[str, object]] = {
    "flex-token-lifecycle": {
        "title": "Flex Token Lifecycle",
        "stages": [
            "capture_transient_token",
            "validate_token_type",
            "create_permanent_instrument",
            "authorize_with_instrument",
        ],
        "api_sdk_facts": [
            "Flex Microform returns a short-lived transientTokenJwt",
            "TMS createInstrument accepts a Flex token via a dedicated transient-token path, not as raw pan",
            "Transient tokens must not be persisted as long-lived customer credentials",
        ],
        "surface_hints": ["docs", "sdk", "vap_cli"],
        "entity_signals": [
            "flex",
            "microform",
            "transienttokenjwt",
            "tms",
            "createinstrument",
            "permanent instrument",
        ],
    },
    "http-signature-debug": {
        "title": "HTTP Signature Debug",
        "stages": [
            "load_sandbox_env_vars",
            "build_digest",
            "build_signature_base",
            "attach_vc_headers",
            "interpret_auth_failure",
        ],
        "api_sdk_facts": [
            "Sandbox host is apitest.cybersource.com",
            "SDK expects merchantKeyId and merchantsecretKey (not keyId/secretKey)",
            "Signed headers typically include host, date, request-target, digest, v-c-merchant-id",
        ],
        "surface_hints": ["docs", "sdk", "vap_cli"],
        "entity_signals": [
            "http signature",
            "authentication failed",
            "keyid",
            "secretkey",
            "merchantkeyid",
            "v-c-merchant-id",
            "apitest",
        ],
    },
    "microform-payer-auth-state-machine": {
        "title": "Microform + Payer Auth State Machine",
        "stages": [
            "microform_tokenize",
            "payer_auth_setup",
            "enrollment_check",
            "challenge_or_frictionless",
            "validate_authentication",
            "authorize_with_auth_result",
        ],
        "api_sdk_facts": [
            "Microform tokenization is not itself a Payer Auth / 3DS completion",
            "Enrollment may return FRICTIONLESS, CHALLENGE, or UNAVAILABLE paths",
            "Authorization must carry authentication transaction references when 3DS was performed",
        ],
        "surface_hints": ["docs", "vap_cli", "mcp"],
        "entity_signals": [
            "payer authentication",
            "3ds",
            "enrollment",
            "challenge",
            "microform",
            "authentication transaction",
        ],
    },
}

_ENTITY_PATTERNS: List[Tuple[str, str]] = [
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


def load_raw_questions(path: Optional[Path] = None) -> List[RawQuestion]:
    seeds_path = path or DEFAULT_SEEDS_PATH
    raw = json.loads(seeds_path.read_text(encoding="utf-8"))
    questions: List[RawQuestion] = []
    for item in raw:
        # Refuse pre-labeled workflow seeds — suggestion must come from extraction.
        if "workflow_id" in item:
            raise ValueError(
                f"Raw question {item.get('seed_id')!r} must not include workflow_id; "
                "DocETL suggests workflow_id after extraction"
            )
        questions.append(
            RawQuestion(
                seed_id=item["seed_id"],
                source=item["source"],
                channel=item.get("channel", "docs"),
                question=item["question"],
                public_refs=list(item.get("public_refs", [])),
            )
        )
    return questions


# Backward-compatible alias used by older imports/tests.
load_seeds = load_raw_questions


def _split_symptom_clauses(text: str) -> List[str]:
    parts = re.split(r"[.!?]+\s+|\s+[—\-]\s+|\s+and\s+I\b|\s+and\s+I'?m\b", text)
    symptoms: List[str] = []
    for part in parts:
        clause = part.strip(" .?—-")
        if len(clause) < 24:
            continue
        lower = clause.lower()
        if any(
            marker in lower
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
    return symptoms[:5]


def extract_from_question(question: RawQuestion) -> Extraction:
    """DocETL-style map: raw question → goal / symptoms / entities."""
    text = question.question
    lower = text.lower()

    entities: List[str] = []
    for pattern, label in _ENTITY_PATTERNS:
        if re.search(pattern, lower):
            if label not in entities:
                entities.append(label)

    symptoms = _split_symptom_clauses(text)
    if not symptoms:
        symptoms = [text.strip()]

    # Goal: first interrogative clause, else a normalized summary from entities.
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
    return Extraction(
        seed_id=question.seed_id,
        goal=goal,
        symptoms=symptoms,
        entities=entities,
        confidence=round(confidence, 2),
    )


def suggest_workflow(extraction: Extraction) -> WorkflowSuggestion:
    """Suggest workflow_id + stages from extracted entities/symptoms."""
    blob = " ".join(
        [extraction.goal] + extraction.symptoms + extraction.entities
    ).lower()

    scored: List[Tuple[float, str, List[str]]] = []
    for workflow_id, catalog in _WORKFLOW_CATALOG.items():
        signals = list(catalog["entity_signals"])  # type: ignore[arg-type]
        hits = [s for s in signals if s in blob]
        score = float(len(hits))
        # Light tie-breakers for overlapping Microform mentions.
        if workflow_id == "microform-payer-auth-state-machine" and "payer" in blob:
            score += 1.5
        if workflow_id == "flex-token-lifecycle" and "tms" in blob:
            score += 1.0
        if workflow_id == "http-signature-debug" and "signature" in blob:
            score += 1.0
        scored.append((score, workflow_id, hits))

    scored.sort(key=lambda row: (-row[0], row[1]))
    best_score, workflow_id, hits = scored[0]
    if best_score <= 0:
        raise ValueError(f"No workflow suggestion for seed {extraction.seed_id!r}")

    catalog = _WORKFLOW_CATALOG[workflow_id]
    max_signals = max(len(c["entity_signals"]) for c in _WORKFLOW_CATALOG.values())  # type: ignore[arg-type]
    confidence = round(min(0.99, best_score / max(max_signals, 1)), 2)
    rationale = [f"entity_hit:{h}" for h in hits] or ["fallback:highest_catalog_score"]

    return WorkflowSuggestion(
        seed_id=extraction.seed_id,
        suggested_workflow_id=workflow_id,
        title=str(catalog["title"]),
        stages=list(catalog["stages"]),  # type: ignore[arg-type]
        rationale=rationale,
        confidence=confidence,
    )


def catalog_entry(workflow_id: str) -> Dict[str, object]:
    if workflow_id not in _WORKFLOW_CATALOG:
        raise KeyError(f"Unknown workflow_id={workflow_id!r}")
    return _WORKFLOW_CATALOG[workflow_id]


def discover_suggestions(
    questions: Optional[Iterable[RawQuestion]] = None,
) -> List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]]:
    """Run extract → suggest for each raw question."""
    qlist = list(questions) if questions is not None else load_raw_questions()
    rows: List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]] = []
    for question in qlist:
        extraction = extract_from_question(question)
        suggestion = suggest_workflow(extraction)
        rows.append((question, extraction, suggestion))
    return rows


def synthesize_candidates_payload(
    workflow_id: Optional[str] = None,
) -> Dict[str, object]:
    """Artifact for the pre-PM discovery stage (suggestions, not approved candidates)."""
    from relay_bench.pm_gate import load_pm_decisions, apply_pm_decisions

    rows = discover_suggestions()
    suggestions = []
    for question, extraction, suggestion in rows:
        if workflow_id and suggestion.suggested_workflow_id != workflow_id:
            # Still include if PM later maps it; filter on suggestion for synthesize view.
            continue
        suggestions.append(
            {
                "raw_question": question.to_dict(),
                "extraction": extraction.to_dict(),
                "suggestion": suggestion.to_dict(),
            }
        )

    approved = apply_pm_decisions(rows, load_pm_decisions())
    if workflow_id:
        approved = [c for c in approved if c.workflow_id == workflow_id]

    return {
        "stage": "docetl_extract_suggest_pm",
        "pipeline": [
            "raw_forum_docs_support_questions",
            "docetl_extract_goal_symptoms_entities",
            "suggest_workflow_id_and_stages",
            "pm_approve_or_edit",
            "relay_bench_task_pack_and_verifier",
        ],
        "suggestion_count": len(suggestions),
        "suggestions": suggestions,
        "approved_candidate_count": len(approved),
        "approved_candidates": [c.to_dict() for c in approved],
    }


def discover_workflows(
    seeds: Optional[Iterable[RawQuestion]] = None,
    workflow_id: Optional[str] = None,
):
    """Return PM-approved workflow candidates (task-pack-ready)."""
    from relay_bench.pm_gate import apply_pm_decisions, load_pm_decisions

    rows = discover_suggestions(questions=seeds)
    approved = apply_pm_decisions(rows, load_pm_decisions())
    if workflow_id:
        approved = [c for c in approved if c.workflow_id == workflow_id]
    return approved
