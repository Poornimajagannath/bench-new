"""DocETL-style workflow discovery over frozen hard-question seeds.

Stage boundary: seeds → typed WorkflowCandidate artifacts.
No verification, no oracles, no network.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from relay_bench.schemas import HardQuestionSeed, WorkflowCandidate

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SEEDS_PATH = ROOT / "data" / "seeds" / "hard_questions.json"

# Deterministic workflow templates keyed by workflow_id.
# Discovery maps/reduces seeds into these typed candidates.
_WORKFLOW_TEMPLATES: Dict[str, Dict[str, object]] = {
    "flex-token-lifecycle": {
        "title": "Flex Token Lifecycle",
        "goal": "Move from a Flex Microform transient token to a correctly scoped permanent TMS instrument without treating the JWT as a reusable PAN.",
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
    },
    "http-signature-debug": {
        "title": "HTTP Signature Debug",
        "goal": "Produce a sandbox-safe HTTP Signature request using SDK-correct credential field names and a canonical signed-headers set.",
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
    },
    "microform-payer-auth-state-machine": {
        "title": "Microform + Payer Auth State Machine",
        "goal": "Sequence Microform tokenization with Payer Authentication enrollment, challenge/frictionless handling, and authorization using the authentication result.",
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
    },
}


def load_seeds(path: Optional[Path] = None) -> List[HardQuestionSeed]:
    seeds_path = path or DEFAULT_SEEDS_PATH
    raw = json.loads(seeds_path.read_text(encoding="utf-8"))
    return [HardQuestionSeed(**item) for item in raw]


def _reduce_seed_group(workflow_id: str, seeds: List[HardQuestionSeed]) -> WorkflowCandidate:
    template = _WORKFLOW_TEMPLATES.get(workflow_id)
    if template is None:
        raise KeyError(f"No discovery template for workflow_id={workflow_id!r}")

    confusion: List[str] = []
    for seed in seeds:
        for theme in seed.confusion_themes:
            if theme not in confusion:
                confusion.append(theme)
        for symptom in seed.symptoms:
            marker = f"symptom:{symptom}"
            if marker not in confusion:
                confusion.append(marker)

    return WorkflowCandidate(
        workflow_id=workflow_id,
        title=str(template["title"]),
        goal=str(template["goal"]),
        stages=list(template["stages"]),  # type: ignore[arg-type]
        api_sdk_facts=list(template["api_sdk_facts"]),  # type: ignore[arg-type]
        confusion_points=confusion,
        seed_ids=[s.seed_id for s in seeds],
        surface_hints=list(template.get("surface_hints", [])),  # type: ignore[arg-type]
    )


def discover_workflows(
    seeds: Optional[Iterable[HardQuestionSeed]] = None,
    workflow_id: Optional[str] = None,
) -> List[WorkflowCandidate]:
    """Map seeds by workflow_id, then reduce into typed candidates (DocETL-style)."""
    seed_list = list(seeds) if seeds is not None else load_seeds()
    grouped: Dict[str, List[HardQuestionSeed]] = {}
    for seed in seed_list:
        if workflow_id and seed.workflow_id != workflow_id:
            continue
        grouped.setdefault(seed.workflow_id, []).append(seed)

    candidates = [_reduce_seed_group(wid, group) for wid, group in sorted(grouped.items())]
    return candidates


def synthesize_candidates_payload(
    workflow_id: Optional[str] = None,
) -> Dict[str, object]:
    candidates = discover_workflows(workflow_id=workflow_id)
    return {
        "stage": "docetl_workflow_discovery",
        "candidate_count": len(candidates),
        "candidates": [c.to_dict() for c in candidates],
    }
