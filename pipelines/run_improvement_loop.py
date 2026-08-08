#!/usr/bin/env python3
"""Improvement loop: evidence -> candidates -> re-check -> capped proposals.

Reads only evidence artifacts and normalized/ (never raw/). Each candidate
names the evidence it was drawn from and is re-checked against the current
repo state before it may become a proposal; failures are recorded, not
discarded silently.

Code paths (reported honestly — never a requested mode that did nothing):
  deterministic_rules — C1–C5 rule generators only; no model call.
  local_spark_qwen_draft — generative half ran against local Spark Qwen.
  refused_local_unreachable — generative requested/auto but Qwen was down;
    fell back to deterministic_rules and said so.

Provider policy:
  Local Spark Qwen (http://127.0.0.1:8000/v1, nvidia/Qwen3.6-35B-A3B-NVFP4,
  Hermes provider spark-qwen) is the default generative backend.
  Cloud keys are an optional fallback that MUST NOT receive corpus content —
  any generative prompt that includes evidence/claims is local-only.

No-invention rule:
  The loop may rephrase, restructure, and assemble existing claims. It may
  never author a fact absent from the claim set. Missing step outcomes become
  gap markers, not invented results.

Caps: --max-prs (default 3), --max-completion-tokens (default 8000),
--timeout-seconds (default 180). --budget-usd retained for cloud metering
compatibility (local spend is always $0).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.ingest import (  # noqa: E402
    _extract_claims_from_text,
)

DEFAULT_SPARK_QWEN_BASE = "http://127.0.0.1:8000/v1"
DEFAULT_SPARK_QWEN_MODEL = "nvidia/Qwen3.6-35B-A3B-NVFP4"
HERMES_PROVIDER = "spark-qwen"

# Explicit contract: missing outcomes are gaps, never authored facts.
GAP_MARKER_NO_OUTCOME = "[gap: no stated outcome in source claims]"
NO_INVENTION_RULE = (
    "The loop may rephrase, restructure, and assemble existing claims, and "
    "may never author a fact absent from the claim set. A step with no "
    "stated outcome must receive a gap marker, not an invented result."
)

_INVENTION_PATTERNS = (
    re.compile(r"\bauthor (?:expected )?outcomes?\b", re.I),
    re.compile(r"\bwrite outcomes?\b", re.I),
    # Positive invent/fabricate — not "cannot invent" / "never invent".
    re.compile(r"(?<!\bcannot )(?<!\bnever )(?<!\bnot )(?<!\bwithout )\binvent\b", re.I),
    re.compile(r"(?<!\bcannot )(?<!\bnever )(?<!\bnot )\bfabricate\b", re.I),
    re.compile(r"\bfill in (?:the )?missing outcomes?\b", re.I),
    re.compile(r"\bgenerate (?:expected )?outcomes?\b", re.I),
    re.compile(r"\bcreate (?:expected )?outcomes? for\b", re.I),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _read_text(rel: str, limit: int = 4000) -> str:
    path = ROOT / rel
    if not path.is_file():
        return f"(missing: {rel})"
    text = path.read_text(encoding="utf-8", errors="replace")
    return text if len(text) <= limit else text[:limit] + "\n…(truncated)\n"


def is_loopback_url(url: str) -> bool:
    """True only for localhost / 127.0.0.1 / ::1 — corpus stays on machine."""
    try:
        host = (urlparse(url).hostname or "").lower()
    except ValueError:
        return False
    return host in {"127.0.0.1", "localhost", "::1"}


def proposal_invents_facts(
    proposal: str, *, change_type: str = ""
) -> Optional[str]:
    """Return a refusal reason if the proposal would invent product facts."""
    if change_type in {"invent_facts", "author_outcomes"}:
        return "change_type forbids inventing facts"
    text = proposal or ""
    # Explicit gap-marker proposals are the approved refusal path (C4 class).
    if change_type == "gap_marker" or (
        "gap marker" in text.lower() and "outcome" in text.lower()
    ):
        # Still reject if it also tries to author outcome text.
        if re.search(r"\bauthor (?:expected )?outcomes?\b", text, re.I):
            return "gap_marker proposal still authors outcomes"
        return None
    for pat in _INVENTION_PATTERNS:
        if pat.search(text):
            return f"matches invention pattern: {pat.pattern}"
    return None


def propose_for_missing_outcome(
    step: Dict[str, Any],
    available_claims: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    """Assemble an outcome from claims, or emit a gap marker.

    Never invents. Looks for an outcome/result claim whose text is already
    present in ``available_claims`` and tied to the step; otherwise returns
    ``GAP_MARKER_NO_OUTCOME``.
    """
    step_text = str(step.get("text") or step.get("title") or "").strip()
    extras = step.get("extras") or {}
    # Explicit outcome already on the step claim.
    for key in ("outcome", "expected_outcome", "result"):
        val = extras.get(key)
        if isinstance(val, str) and val.strip():
            return {
                "kind": "assembled_from_claims",
                "text": val.strip(),
                "source_claim_ids": [step.get("claim_id") or step.get("id") or ""],
                "status": "proposed",
            }

    # Search claim set for an outcome fact that quotes/covers this step.
    for claim in available_claims:
        schema = str(claim.get("schema") or "")
        ctext = str(claim.get("text") or "")
        cextras = claim.get("extras") or {}
        outcome = cextras.get("outcome") or cextras.get("expected_outcome")
        if not outcome:
            # Only accept schemas that are explicitly outcome-bearing.
            if schema not in {"step_outcome", "expected_outcome"}:
                continue
            outcome = ctext
        if not isinstance(outcome, str) or not outcome.strip():
            continue
        if step_text and step_text.lower() not in ctext.lower() and ctext.lower() not in step_text.lower():
            # Require some grounding link between step and outcome claim.
            if step.get("claim_id") and claim.get("step_claim_id") != step.get("claim_id"):
                continue
        return {
            "kind": "assembled_from_claims",
            "text": outcome.strip(),
            "source_claim_ids": [str(claim.get("claim_id") or claim.get("id") or "")],
            "status": "proposed",
        }

    return {
        "kind": "gap_marker",
        "text": GAP_MARKER_NO_OUTCOME,
        "source_claim_ids": [],
        "status": "proposed_gap",
        "why": NO_INVENTION_RULE,
    }


def resolve_local_spark_qwen() -> Optional[Dict[str, str]]:
    """Return local Spark Qwen endpoint dict, or None if unreachable."""
    spark_base = os.environ.get("SPARK_QWEN_BASE_URL", DEFAULT_SPARK_QWEN_BASE).rstrip(
        "/"
    )
    if not is_loopback_url(spark_base):
        # Misconfiguration: refused — would send corpus off-box.
        return None
    spark_model = os.environ.get("SPARK_QWEN_MODEL", DEFAULT_SPARK_QWEN_MODEL)
    try:
        req = urllib.request.Request(
            spark_base + "/models",
            headers={"Accept": "application/json"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=2) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        models = [m.get("id") for m in payload.get("data") or [] if m.get("id")]
        if not models:
            return None
        model = spark_model if spark_model in models else models[0]
        return {
            "base_url": spark_base,
            "model": model,
            "api_key": os.environ.get("SPARK_QWEN_API_KEY") or "local",
            "source": "spark-qwen-local",
            "hermes_provider": HERMES_PROVIDER,
        }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None


def chat_completion_local(
    endpoint: Dict[str, str],
    messages: List[Dict[str, str]],
    *,
    max_tokens: int = 1800,
    timeout_seconds: int = 180,
) -> Tuple[str, Dict[str, Any]]:
    """Call a local OpenAI-compatible chat endpoint. Refuses non-loopback."""
    if not is_loopback_url(endpoint["base_url"]):
        raise RuntimeError(
            "corpus egress refused: generative prompts may only call loopback "
            f"(got {endpoint['base_url']})"
        )
    payload_body: Dict[str, Any] = {
        "model": endpoint["model"],
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.2,
        # Qwen3.6 burns tokens on a reasoning channel; disable for JSON drafts.
        "chat_template_kwargs": {"enable_thinking": False},
    }
    body = json.dumps(payload_body).encode("utf-8")
    req = urllib.request.Request(
        endpoint["base_url"] + "/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {endpoint['api_key']}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    msg = payload["choices"][0]["message"]
    content = (msg.get("content") or "").strip()
    if not content and msg.get("reasoning"):
        reason = msg["reasoning"]
        m = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])\s*$", reason)
        content = m.group(1) if m else reason[-500:]
    return content, payload.get("usage") or {}


def gather_evidence_bundle() -> str:
    parts = [
        "# Evidence bundle for improvement proposals",
        "",
        f"NO-INVENTION RULE: {NO_INVENTION_RULE}",
        "",
        "Propose only extractor/schema/pipeline changes grounded in cited "
        "evidence. Prefer re-runs of already-fetched content. Cap 3 proposals.",
        "If a step lacks a stated outcome, propose a gap marker — never invent.",
        "",
        "## WAVE2 closeout",
        _read_text("evals/evidence/WAVE2-CLOSEOUT.md", 2500),
        "",
        "## Boarding gap report (headlines)",
        _read_text("artifacts/content_engine/boarding/gap-report.md", 2500),
        "",
        "## Soft-gap findings (API reference)",
        _read_text("artifacts/content_engine/wave_rerun/soft-gap-findings.md", 2000),
        "",
        "## C3 sibling triage",
        _read_text("evals/evidence/wave1-payments/c3-payments-reingest.md", 2500),
        "",
        "## L1 Qwen proposals (already merged — do not re-propose)",
        _read_text("evals/evidence/improvement-loop/l1-qwen-proposals.md", 2000),
        "",
        "## Manual test log",
    ]
    manual = ROOT / "evals/manual-runs.jsonl"
    if manual.is_file() and manual.stat().st_size > 0:
        parts.append(_read_text("evals/manual-runs.jsonl", 2000))
    else:
        parts.append("(empty or missing — no hand-test evidence this run)")
    return "\n".join(parts)


_EVIDENCE_ALIASES = {
    "wave2 closeout": "evals/evidence/WAVE2-CLOSEOUT.md",
    "wave2-closeout": "evals/evidence/WAVE2-CLOSEOUT.md",
    "boarding gap report": "artifacts/content_engine/boarding/gap-report.md",
    "gap report": "artifacts/content_engine/boarding/gap-report.md",
    "soft-gap findings": "artifacts/content_engine/wave_rerun/soft-gap-findings.md",
    "soft gap findings": "artifacts/content_engine/wave_rerun/soft-gap-findings.md",
    "c3 sibling triage": "evals/evidence/wave1-payments/c3-payments-reingest.md",
    "c3 payments": "evals/evidence/wave1-payments/c3-payments-reingest.md",
    "l1 qwen": "evals/evidence/improvement-loop/l1-qwen-proposals.md",
    "manual test log": "evals/manual-runs.jsonl",
}


def _resolve_evidence_path(entry: str) -> Optional[str]:
    raw = entry.split(" — ")[0].strip().strip("'\"")
    if not raw:
        return None
    if (ROOT / raw).exists():
        return raw
    key = raw.lower()
    for alias, path in _EVIDENCE_ALIASES.items():
        if key.startswith(alias) or alias in key:
            return path if (ROOT / path).exists() else None
    name = Path(raw).name
    for fold in (
        ROOT / "evals/evidence",
        ROOT / "evals/evidence/wave1-payments",
        ROOT / "evals/evidence/improvement-loop",
        ROOT / "artifacts/content_engine/boarding",
        ROOT / "artifacts/content_engine/wave_rerun",
    ):
        hit = fold / name
        if hit.is_file():
            return str(hit.relative_to(ROOT))
    return None


def recheck_llm_candidate(cand: Dict[str, Any]) -> Dict[str, Any]:
    """Re-check: no invention, evidence exists, skip stale already-fixed classes."""
    reason = proposal_invents_facts(
        cand.get("proposal") or "", change_type=str(cand.get("change_type") or "")
    )
    if reason:
        cand["status"] = "discarded"
        cand["recheck"] = f"fail: would invent facts ({reason})"
        cand["why_discarded"] = NO_INVENTION_RULE
        return cand

    proposal = (cand.get("proposal") or "").lower()

    if "backticked full-url" in proposal or "full-url endpoint" in proposal:
        sample = (
            ROOT
            / "data/products/boarding/guides/"
            / (
                "en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_"
                "boarding-reg-create-merch-api.md.md"
            )
        )
        if sample.is_file():
            claims, _ = _extract_claims_from_text(
                sample.read_text(encoding="utf-8"),
                source_pointer=sample.name,
                doc_stem=sample.stem,
            )
            if any(c.schema == "endpoint_fact" for c in claims):
                cand["status"] = "discarded"
                cand["recheck"] = "fail: C1 defect already repaired"
                cand["why_discarded"] = "Stale relative to current extractor."
                return cand
    if "llms.txt" in proposal or "merchant-boarding" in proposal:
        cand["status"] = "discarded"
        cand["recheck"] = "fail: upstream docs-site defect (same class as C5)"
        cand["why_discarded"] = "Production docs-site defect; not fixable here."
        return cand
    if "field_table" in proposal and (
        "implement" in proposal or "add a `field_table`" in proposal
        or "add the `field_table`" in proposal
    ):
        if (ROOT / "tests/test_field_table.py").is_file():
            cand["status"] = "discarded"
            cand["recheck"] = "fail: field_table already implemented"
            cand["why_discarded"] = "Stale relative to current extractor."
            return cand
    if "rest_example" in proposal or (
        "json code block" in proposal and "rest" in proposal
    ):
        if (ROOT / "tests/test_rest_example.py").is_file():
            cand["status"] = "discarded"
            cand["recheck"] = "fail: rest_example already implemented (L1)"
            cand["why_discarded"] = "Stale relative to current extractor."
            return cand
    if "prereq" in proposal and (
        "before you can" in proposal or "prerequisite_pattern" in proposal.replace("-", "_")
        or "_prerequisite_pattern" in proposal
    ):
        from content_bench.content_engine import triage as _triage

        if (
            _triage.constraint_kind(
                "Before you can implement payer authentication services, "
                "your business team must contact your acquirer."
            )
            == "prerequisite"
        ):
            cand["status"] = "discarded"
            cand["recheck"] = "fail: prerequisite pattern already expanded (L1)"
            cand["why_discarded"] = "Stale relative to current extractor."
            return cand

    resolved: List[str] = []
    unresolved: List[str] = []
    for e in cand.get("evidence") or []:
        path = _resolve_evidence_path(e)
        if path:
            resolved.append(path)
        else:
            unresolved.append(e)
    cand["evidence_resolved"] = resolved
    if not resolved:
        cand["status"] = "discarded"
        cand["recheck"] = f"fail: evidence missing: {unresolved[:3]}"
        return cand
    cand["status"] = "proposed"
    cand["recheck"] = (
        f"pass: {len(resolved)} evidence path(s) resolve; proposal is non-inventive"
    )
    return cand


def generate_llm_candidates(
    endpoint: Dict[str, str],
    *,
    max_prs: int,
    max_completion_tokens: int,
    timeout_seconds: int,
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Draft candidates via local Spark Qwen. Corpus never leaves loopback."""
    bundle = gather_evidence_bundle()
    system = (
        "You are the content-bench improvement loop running on local Spark Qwen. "
        f"{NO_INVENTION_RULE} "
        "Propose concrete, re-checkable extractor/schema/pipeline changes. "
        "Output ONLY JSON: "
        '{"candidates":[{"id":"L1-...","proposal":"...","change_type":'
        '"extractor|schema|pipeline|docs_upstream|gap_marker","evidence":['
        '"evals/evidence/...md — note"]}]}. '
        "Every evidence entry MUST start with a real repo-relative path. "
        "For missing step outcomes, propose change_type=gap_marker — never "
        "author the outcome text."
    )
    user = (
        f"Propose up to {max_prs} NEW candidates. Do NOT re-propose: "
        f"backticked full-URL endpoints (fixed), step anchors (fixed), "
        f"C3 payments bin-lookup re-ingest (merged), field_table (merged), "
        f"rest_example (merged), prerequisite pattern tune (merged), "
        f"authoring step outcomes (invents facts), "
        f"or CyberSource llms.txt / merchant-boarding 500 (upstream).\n\n"
        f"{bundle}"
    )
    t0 = time.monotonic()
    content, usage = chat_completion_local(
        endpoint,
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_tokens=max_completion_tokens,
        timeout_seconds=timeout_seconds,
    )
    elapsed = time.monotonic() - t0
    meta: Dict[str, Any] = {
        "endpoint_source": endpoint["source"],
        "hermes_provider": endpoint.get("hermes_provider"),
        "model": endpoint["model"],
        "base_url": endpoint["base_url"],
        "usage": usage,
        "elapsed_seconds": round(elapsed, 3),
        "raw_response_chars": len(content),
        "llm_called": True,
    }
    m = re.search(r"\{[\s\S]*\}", content)
    if not m:
        return (
            [
                {
                    "id": "L0-parse-failure",
                    "proposal": "LLM response was not parseable JSON",
                    "evidence": ["artifacts/improvement_loop/run-report.json"],
                    "status": "discarded",
                    "recheck": "fail: no JSON object in model response",
                    "why_discarded": content[:300],
                    "source": "llm",
                }
            ],
            meta,
        )
    try:
        data = json.loads(m.group(0))
    except json.JSONDecodeError as exc:
        return (
            [
                {
                    "id": "L0-parse-failure",
                    "proposal": "LLM JSON parse error",
                    "evidence": ["artifacts/improvement_loop/run-report.json"],
                    "status": "discarded",
                    "recheck": f"fail: {exc}",
                    "why_discarded": content[:300],
                    "source": "llm",
                }
            ],
            meta,
        )
    out: List[Dict[str, Any]] = []
    for i, raw in enumerate(data.get("candidates") or []):
        cand = {
            "id": str(raw.get("id") or f"L{i+1}"),
            "proposal": str(raw.get("proposal") or "").strip(),
            "change_type": str(raw.get("change_type") or "extractor"),
            "evidence": list(raw.get("evidence") or []),
            "source": "llm",
        }
        if not cand["proposal"]:
            cand["status"] = "discarded"
            cand["recheck"] = "fail: empty proposal"
            out.append(cand)
            continue
        out.append(recheck_llm_candidate(cand))
    return out, meta


def candidate_endpoint_url_style() -> Dict[str, Any]:
    sample = (
        ROOT
        / "data/products/boarding/guides/"
        "en-us_boarding_developer_all_rest_boarding_boarding-reg-intro_"
        "boarding-reg-create-merch-api.md.md"
    )
    cand: Dict[str, Any] = {
        "id": "C1-endpoint-url-style",
        "proposal": (
            "Extend endpoint_fact extraction to match CyberSource's backticked "
            "full-URL endpoint style (`POST ``https://host``/path`), not only "
            "bare 'VERB /path'."
        ),
        "evidence": [
            "evals/evidence/WAVE2-CLOSEOUT.md — remaining-48 shape list",
            "artifacts/content_engine/boarding/ingestion-report.json — drop log",
            str(sample.relative_to(ROOT)),
        ],
        "source": "deterministic",
    }
    if not sample.is_file():
        cand["recheck"] = "fail: sample page missing"
        cand["status"] = "discarded"
        return cand
    text = sample.read_text(encoding="utf-8")
    claims, _ = _extract_claims_from_text(
        text, source_pointer=sample.name, doc_stem=sample.stem
    )
    endpoints = [c for c in claims if c.schema == "endpoint_fact"]
    has_url_line = bool(
        re.search(r"(GET|POST|PUT|PATCH|DELETE)\s*`+\s*https?://", text)
    )
    if has_url_line and not endpoints:
        cand["recheck"] = (
            "pass: page contains a backticked full-URL endpoint line and the "
            "current extractor yields 0 endpoint_fact claims"
        )
        cand["status"] = "proposed"
    else:
        cand["recheck"] = (
            f"fail: endpoint_facts={len(endpoints)} url_line={has_url_line} — "
            "defect no longer reproduces"
        )
        cand["status"] = "discarded"
    return cand


def candidate_step_anchor_noise() -> Dict[str, Any]:
    comp = ROOT / "artifacts/content_engine/boarding/composition-report.json"
    cand: Dict[str, Any] = {
        "id": "C2-step-anchor-noise",
        "proposal": (
            "Strip trailing {#anchor} tokens from quickstart_step titles/text "
            "at extraction so identical steps match across mega-guide and "
            "child pages."
        ),
        "evidence": [str(comp.relative_to(ROOT)) + " — mega_residual_samples"],
        "source": "deterministic",
    }
    if not comp.is_file():
        cand["recheck"] = "fail: composition report missing"
        cand["status"] = "discarded"
        return cand
    data = json.loads(comp.read_text(encoding="utf-8"))
    anchored = [
        s
        for s in data.get("mega_residual_samples", [])
        if s["schema"] == "quickstart_step" and "{#" in s["text"]
    ]
    if anchored:
        cand["recheck"] = (
            f"pass: {len(anchored)} residual step samples still carry "
            "{#anchor} tokens in claim text"
        )
        cand["status"] = "proposed"
    else:
        cand["recheck"] = "fail: no anchored residual steps remain"
        cand["status"] = "discarded"
    return cand


def candidate_payments_still_dropped() -> Dict[str, Any]:
    cand: Dict[str, Any] = {
        "id": "C3-payments-still-dropped",
        "proposal": (
            "Re-run payments ingestion: extractor upgrades since Wave 1 close "
            "(constraint classes, field_table) may recover still-dropped pages."
        ),
        "evidence": [
            "evals/evidence/wave1-payments/extraction-recall-fix.md — "
            "still-dropped names",
            "evals/evidence/wave1-payments/c3-payments-reingest.md",
        ],
        "source": "deterministic",
    }
    merged = ROOT / "evals/evidence/wave1-payments/c3-payments-reingest.md"
    names = [
        "en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md",
        "en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md",
        "en-us_payments_developer_ctv_rest_payments_payments-intro.md.md",
        "en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md",
        "en-us_tms_developer_all_rest_tms_tms-bin-lookup-service.md.md",
        "en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md",
        "en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md",
        "en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn.md.md",
        "en-us_tms_developer_all_rest_tms_tms-ii-tkn.md.md",
        "en-us_tms_developer_all_rest_tms_tms-onboarding.md.md",
        "en-us_tms_developer_all_rest_tms_tms-wallet-tkn.md.md",
        "sandbox.md",
    ]
    guides = ROOT / "data/products/payments/guides"
    now_claiming: List[str] = []
    still: List[str] = []
    for n in names:
        p = guides / n
        if not p.is_file():
            continue
        claims, _ = _extract_claims_from_text(
            p.read_text(encoding="utf-8", errors="replace"),
            source_pointer=n,
            doc_stem=p.stem,
        )
        (now_claiming if claims else still).append(n)
    cand["recheck_detail"] = {
        "would_now_claim": now_claiming,
        "still_zero": still,
    }
    if merged.is_file() and "Status: MERGED" in merged.read_text(encoding="utf-8"):
        cand["recheck"] = (
            f"fail: already merged — recovered "
            f"{len(now_claiming)} claiming page(s); see c3-payments-reingest.md"
        )
        cand["status"] = "discarded"
        cand["why_discarded"] = "C3 already executed and recorded as MERGED."
        return cand
    if now_claiming:
        cand["recheck"] = (
            f"pass: {len(now_claiming)}/{len(names)} previously dropped "
            "payments pages now yield claims under the current extractor"
        )
        cand["status"] = "proposed"
    else:
        cand["recheck"] = "fail: no previously dropped page yields claims"
        cand["status"] = "discarded"
    return cand


def candidate_missing_outcomes() -> Dict[str, Any]:
    """C4 — missing outcomes. Deterministic refuse; also exercises gap marker."""
    step = {
        "claim_id": "demo:step:add-merchant",
        "text": "Click + Add Merchant",
        "schema": "quickstart_step",
        "extras": {},
    }
    # No outcome-bearing claims in the set — must be a gap.
    gap = propose_for_missing_outcome(step, available_claims=[step])
    return {
        "id": "C4-missing-outcomes",
        "proposal": "Author expected outcomes for 220 steps",
        "evidence": [
            "artifacts/content_engine/boarding/gap-report.md — headline 1",
        ],
        "source": "deterministic",
        "recheck": "n/a",
        "status": "discarded",
        "why_discarded": (
            "Outcomes are facts about the product; generating them without a "
            "source would invent facts. Upstream docs-team work, tracked in "
            "the gap report."
        ),
        "gap_marker_demo": gap,
    }


def candidate_llms_txt() -> Dict[str, Any]:
    return {
        "id": "C5-llms-txt-defect",
        "proposal": "Fix llms.txt omission and merchant-boarding.md HTTP 500",
        "evidence": [
            "artifacts/content_engine/boarding/gap-report.md — headline 3",
            "artifacts/content_engine/boarding/toc-fetch-report.md — probe",
        ],
        "source": "deterministic",
        "recheck": "n/a",
        "status": "discarded",
        "why_discarded": (
            "Production docs-site defect; not fixable from this repo. Bug "
            "already raised externally."
        ),
    }


def run_loop(
    *,
    path: str = "auto",
    max_prs: int = 3,
    max_completion_tokens: int = 8000,
    timeout_seconds: int = 180,
    budget_usd: float = 2.0,
) -> Dict[str, Any]:
    """Execute one improvement-loop pass; return the report dict.

    ``path``:
      auto — local Qwen if reachable, else deterministic (honest).
      deterministic — rules only; never call a model.
      local-llm — require local Qwen; refuse (exit semantics via code_path)
                  rather than pretend if unreachable.
    """
    cloud_key_present = any(
        os.environ.get(k)
        for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "LITELLM_API_KEY")
    )
    # Cloud keys are recorded but never used for corpus-bearing prompts.
    local = resolve_local_spark_qwen()

    llm_meta: Dict[str, Any] = {"llm_called": False}
    code_path = "deterministic_rules"
    path_note = ""

    if path == "deterministic":
        code_path = "deterministic_rules"
        path_note = "requested deterministic; no model call."
        local = None
    elif path == "local-llm":
        if local is None:
            code_path = "refused_local_unreachable"
            path_note = (
                "local-llm requested but Spark Qwen unreachable at "
                f"{os.environ.get('SPARK_QWEN_BASE_URL', DEFAULT_SPARK_QWEN_BASE)}; "
                "refusing to pretend. Running deterministic_rules only. "
                "Cloud keys are not used for corpus-bearing prompts."
            )
        else:
            code_path = "local_spark_qwen_draft"
            path_note = (
                f"called local Spark Qwen `{local['model']}` at "
                f"`{local['base_url']}` (Hermes provider {HERMES_PROVIDER})."
            )
    else:  # auto
        if local is not None:
            code_path = "local_spark_qwen_draft"
            path_note = (
                f"auto → local Spark Qwen `{local['model']}` at "
                f"`{local['base_url']}` (Hermes provider {HERMES_PROVIDER})."
            )
        else:
            code_path = "deterministic_rules"
            path_note = (
                "auto → local Spark Qwen unreachable; generative half skipped. "
                "Cloud keys ignored for corpus-bearing prompts "
                f"(cloud_key_present={cloud_key_present})."
            )

    candidates = [
        candidate_endpoint_url_style(),
        candidate_step_anchor_noise(),
        candidate_payments_still_dropped(),
        candidate_missing_outcomes(),
        candidate_llms_txt(),
    ]

    if code_path == "local_spark_qwen_draft" and local is not None:
        llm_cands, llm_meta = generate_llm_candidates(
            local,
            max_prs=max_prs,
            max_completion_tokens=max_completion_tokens,
            timeout_seconds=timeout_seconds,
        )
        candidates.extend(llm_cands)
        if not llm_meta.get("llm_called"):
            # Defend against silent no-op.
            code_path = "refused_local_unreachable"
            path_note = "local endpoint resolved but LLM call did not run."

    proposed = [c for c in candidates if c["status"] == "proposed"]
    capped = proposed[:max_prs]
    for c in proposed[max_prs:]:
        c["status"] = "deferred_over_pr_cap"

    report = {
        "generated_at": _utc_now(),
        "code_path": code_path,
        "code_path_note": path_note,
        "requested_path": path,
        "llm_called": bool(llm_meta.get("llm_called")),
        "llm_key_present": cloud_key_present,
        "cloud_corpus_egress": "forbidden",
        "no_invention_rule": NO_INVENTION_RULE,
        "llm_endpoint": (
            {
                "source": local["source"],
                "base_url": local["base_url"],
                "model": local["model"],
                "hermes_provider": local.get("hermes_provider"),
            }
            if local and code_path == "local_spark_qwen_draft"
            else None
        ),
        "llm_meta": llm_meta,
        "spend_usd": 0.0,
        "budget_usd": budget_usd,
        "max_prs": max_prs,
        "max_completion_tokens": max_completion_tokens,
        "timeout_seconds": timeout_seconds,
        "candidates": candidates,
        "proposed_within_cap": [c["id"] for c in capped],
    }
    return report


def write_report(
    report: Dict[str, Any], *, out_md: Path, out_json: Path
) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Improvement loop — run report",
        "",
        f"- When: `{report['generated_at']}`",
        f"- Code path taken: **{report['code_path']}** — {report['code_path_note']}",
        f"- Requested path: `{report['requested_path']}`",
        f"- LLM called: `{report['llm_called']}`",
        f"- Cloud corpus egress: `{report['cloud_corpus_egress']}`",
        f"- Spend: ${report['spend_usd']:.2f} of ${report['budget_usd']:.2f} "
        f"(local Qwen is $0; limiter is tokens/time)",
        f"- PR cap: {report['max_prs']}",
        f"- Completion-token budget: {report['max_completion_tokens']}",
        f"- Timeout: {report['timeout_seconds']}s",
        "",
        f"No-invention rule: {report['no_invention_rule']}",
        "",
        "| Candidate | Status | Re-check | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    for c in report["candidates"]:
        ev = "; ".join(c.get("evidence") or [])
        lines.append(
            f"| {c['id']}: {str(c.get('proposal', ''))[:80]} | {c['status']} | "
            f"{str(c.get('recheck'))[:90]} | {ev[:110]} |"
        )
    lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-prs", type=int, default=3)
    parser.add_argument("--budget-usd", type=float, default=2.00)
    parser.add_argument(
        "--max-completion-tokens",
        type=int,
        default=8000,
        help="Token budget for the local generative call (spend is $0 locally).",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=180,
        help="Wall-clock budget for the local generative call.",
    )
    parser.add_argument(
        "--path",
        choices=("auto", "deterministic", "local-llm"),
        default="auto",
        help=(
            "auto: local Spark Qwen if reachable else deterministic; "
            "deterministic: rules only; local-llm: require local Qwen"
        ),
    )
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts/improvement_loop/run-report.md"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "artifacts/improvement_loop/run-report.json"),
    )
    args = parser.parse_args()

    report = run_loop(
        path=args.path,
        max_prs=args.max_prs,
        max_completion_tokens=args.max_completion_tokens,
        timeout_seconds=args.timeout_seconds,
        budget_usd=args.budget_usd,
    )
    write_report(
        report, out_md=Path(args.out), out_json=Path(args.json_out)
    )

    print(
        f"code_path={report['code_path']} llm_called={report['llm_called']} "
        f"proposed={len(report['proposed_within_cap'])} "
        f"capped_ids={report['proposed_within_cap']}"
    )
    for c in report["candidates"]:
        print(
            f"  {c['id']}: {c['status']} — {str(c.get('recheck', ''))[:80]}"
        )
    if report["code_path"] == "refused_local_unreachable" and args.path == "local-llm":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
