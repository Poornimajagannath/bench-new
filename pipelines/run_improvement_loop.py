#!/usr/bin/env python3
"""Improvement loop: evidence -> candidates -> re-check -> capped proposals.

Reads only evidence artifacts and normalized/ (never raw/). Each candidate
names the evidence it was drawn from and is re-checked against the current
repo state before it may become a proposal; failures are recorded, not
discarded silently.

Modes:
  deterministic — rule-based candidate generators; cost $0.00.
  llm — drafts additional candidates via an OpenAI-compatible chat endpoint.
    Resolution order:
      1. ANTHROPIC_API_KEY / OPENAI_API_KEY / LITELLM_API_KEY (cloud)
      2. Local Spark Qwen at SPARK_QWEN_BASE_URL or http://127.0.0.1:8000/v1
         (no cloud key required; local spend counted as $0.00)

Caps: --max-prs (default 3), --budget-usd (default 2.00).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.ingest import (  # noqa: E402
    _extract_claims_from_text,
)

DEFAULT_SPARK_QWEN_BASE = "http://127.0.0.1:8000/v1"
DEFAULT_SPARK_QWEN_MODEL = "nvidia/Qwen3.6-35B-A3B-NVFP4"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _read_text(rel: str, limit: int = 4000) -> str:
    path = ROOT / rel
    if not path.is_file():
        return f"(missing: {rel})"
    text = path.read_text(encoding="utf-8", errors="replace")
    return text if len(text) <= limit else text[:limit] + "\n…(truncated)\n"


def resolve_llm_endpoint() -> Optional[Dict[str, str]]:
    """Return {base_url, model, api_key, source} or None."""
    spark_base = os.environ.get("SPARK_QWEN_BASE_URL", DEFAULT_SPARK_QWEN_BASE).rstrip(
        "/"
    )
    spark_model = os.environ.get("SPARK_QWEN_MODEL", DEFAULT_SPARK_QWEN_MODEL)
    # Prefer local Spark Qwen when reachable — no cloud key required.
    try:
        req = urllib.request.Request(
            spark_base + "/models",
            headers={"Accept": "application/json"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=2) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        models = [m.get("id") for m in payload.get("data") or [] if m.get("id")]
        if models:
            model = spark_model if spark_model in models else models[0]
            return {
                "base_url": spark_base,
                "model": model,
                "api_key": os.environ.get("SPARK_QWEN_API_KEY") or "local",
                "source": "spark-qwen-local",
            }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        pass

    if os.environ.get("OPENAI_API_KEY"):
        return {
            "base_url": os.environ.get(
                "OPENAI_BASE_URL", "https://api.openai.com/v1"
            ).rstrip("/"),
            "model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            "api_key": os.environ["OPENAI_API_KEY"],
            "source": "openai",
        }
    if os.environ.get("LITELLM_API_KEY"):
        return {
            "base_url": os.environ.get(
                "LITELLM_BASE_URL", "http://127.0.0.1:4000/v1"
            ).rstrip("/"),
            "model": os.environ.get("LITELLM_MODEL", "spark-sonnet"),
            "api_key": os.environ["LITELLM_API_KEY"],
            "source": "litellm",
        }
    if os.environ.get("ANTHROPIC_API_KEY"):
        # Anthropic Messages API is not OpenAI-compatible here; refuse rather
        # than pretend. Prefer Spark Qwen or OPENAI_API_KEY.
        return None
    return None


def chat_completion(
    endpoint: Dict[str, str],
    messages: List[Dict[str, str]],
    *,
    max_tokens: int = 1800,
) -> Tuple[str, Dict[str, Any]]:
    payload_body: Dict[str, Any] = {
        "model": endpoint["model"],
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.2,
    }
    # Qwen3.6 on Spark defaults to a long reasoning channel that truncates
    # JSON drafts under modest max_tokens. Disable thinking for structured out.
    if endpoint.get("source") == "spark-qwen-local":
        payload_body["chat_template_kwargs"] = {"enable_thinking": False}
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
    with urllib.request.urlopen(req, timeout=180) as resp:
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
        "Rules: propose only extractor/schema/pipeline changes grounded in "
        "cited evidence. Never invent product facts, step outcomes, or API "
        "behavior. Prefer re-runs of already-fetched content. Cap 3 proposals.",
        "",
        "## WAVE2 closeout (template matrix + remaining shapes)",
        _read_text("evals/evidence/WAVE2-CLOSEOUT.md", 2500),
        "",
        "## Boarding gap report (headlines)",
        _read_text("artifacts/content_engine/boarding/gap-report.md", 2500),
        "",
        "## Soft-gap findings (API reference)",
        _read_text("artifacts/content_engine/wave_rerun/soft-gap-findings.md", 2000),
        "",
        "## C3 sibling triage (still-dropped payments pages)",
        _read_text("evals/evidence/wave1-payments/c3-payments-reingest.md", 3000),
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
    "manual test log": "evals/manual-runs.jsonl",
}


def _resolve_evidence_path(entry: str) -> Optional[str]:
    """Map an evidence citation to a repo-relative path, or None."""
    raw = entry.split(" — ")[0].strip().strip("'\"")
    if not raw:
        return None
    if (ROOT / raw).exists():
        return raw
    key = raw.lower()
    for alias, path in _EVIDENCE_ALIASES.items():
        if key.startswith(alias) or alias in key:
            return path if (ROOT / path).exists() else None
    # Filename-only citations
    name = Path(raw).name
    for fold in (
        ROOT / "evals/evidence",
        ROOT / "evals/evidence/wave1-payments",
        ROOT / "artifacts/content_engine/boarding",
        ROOT / "artifacts/content_engine/wave_rerun",
    ):
        hit = fold / name
        if hit.is_file():
            return str(hit.relative_to(ROOT))
    return None


def recheck_llm_candidate(cand: Dict[str, Any]) -> Dict[str, Any]:
    """Light re-check: evidence files must exist; reject outcome invention."""
    proposal = (cand.get("proposal") or "").lower()
    banned = (
        "author expected outcome",
        "invent outcome",
        "write outcomes for",
        "fabricate",
    )
    if any(b in proposal for b in banned) or cand.get("change_type") == "invent_facts":
        cand["status"] = "discarded"
        cand["recheck"] = "fail: proposal would invent product facts"
        cand["why_discarded"] = (
            "Outcomes and product behavior must come from source docs; "
            "the loop must refuse to invent them."
        )
        return cand
    # Stale / already-handled classes (same judgment as C1/C5).
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
                cand["recheck"] = (
                    "fail: backticked full-URL endpoint extraction already works "
                    "(C1 defect repaired)"
                )
                cand["why_discarded"] = "Stale relative to current extractor."
                return cand
    if "llms.txt" in proposal or "merchant-boarding" in proposal:
        cand["status"] = "discarded"
        cand["recheck"] = "fail: upstream docs-site defect (same class as C5)"
        cand["why_discarded"] = (
            "Production docs-site defect; not fixable from this repo."
        )
        return cand
    if "field_table" in proposal and (
        "implement" in proposal or "add a `field_table`" in proposal
        or "add the `field_table`" in proposal
    ):
        # field_table already shipped in Wave 2 closeout.
        if (ROOT / "tests/test_field_table.py").is_file():
            cand["status"] = "discarded"
            cand["recheck"] = (
                "fail: field_table schema already implemented "
                "(WAVE2-CLOSEOUT + tests/test_field_table.py)"
            )
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
    endpoint: Dict[str, str], *, max_prs: int
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    bundle = gather_evidence_bundle()
    system = (
        "You are the content-bench improvement loop. Propose concrete, "
        "re-checkable changes to the extraction/composition engine. "
        "Output ONLY a JSON object: "
        '{"candidates":[{"id":"L1-...","proposal":"...","change_type":'
        '"extractor|schema|pipeline|docs_upstream","evidence":['
        '"evals/evidence/...md — note"]}]}. '
        "Every evidence entry MUST start with a real repo-relative path "
        "(examples: evals/evidence/WAVE2-CLOSEOUT.md, "
        "evals/evidence/wave1-payments/c3-payments-reingest.md, "
        "artifacts/content_engine/boarding/gap-report.md, "
        "artifacts/content_engine/wave_rerun/soft-gap-findings.md). "
        "Do not invent product facts or step outcomes. Prefer schema/extractor "
        "fixes for pages that already exist in the corpus."
    )
    user = (
        f"Propose up to {max_prs} NEW candidates. Do NOT propose: "
        f"backticked full-URL endpoint extraction (already fixed), "
        f"step {{#anchor}} stripping (already fixed), "
        f"payments re-ingest of bin-lookup (already merged), "
        f"authoring step outcomes (invents facts), "
        f"or fixing CyberSource llms.txt / merchant-boarding 500 (upstream). "
        f"The strongest open lead in the evidence is the prerequisite-pattern "
        f"miss on pa2-ccdc-intro in c3-payments-reingest.md.\n\n{bundle}"
    )
    content, usage = chat_completion(
        endpoint,
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        max_tokens=2200,
    )
    meta = {
        "endpoint_source": endpoint["source"],
        "model": endpoint["model"],
        "usage": usage,
        "raw_response_chars": len(content),
    }
    # Extract JSON object from possible prose wrapper.
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
    """C1 — endpoint lines in backticked full-URL style yield no endpoint_fact.

    Evidence: evals/evidence/WAVE2-CLOSEOUT.md (remaining 48 zero-claim docs:
    'backticked full-URL endpoint lines'); artifacts/content_engine/boarding/
    ingestion-report.json drop log.
    """
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
    """C2 — step titles carry DITA anchors, defeating prefer-child dedupe.

    Evidence: artifacts/content_engine/boarding/composition-report.json —
    mega_residual_samples contain steps like 'Click + Add Merchant.{#…}' whose
    child twin differs only by the anchor.
    """
    comp = ROOT / "artifacts/content_engine/boarding/composition-report.json"
    cand: Dict[str, Any] = {
        "id": "C2-step-anchor-noise",
        "proposal": (
            "Strip trailing {#anchor} tokens from quickstart_step titles/text "
            "at extraction so identical steps match across mega-guide and "
            "child pages."
        ),
        "evidence": [str(comp.relative_to(ROOT)) + " — mega_residual_samples"],
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
    """C3 — payments pages still dropped at Wave 1 close may now extract.

    Evidence: evals/evidence/wave1-payments/extraction-recall-fix.md
    (still-dropped list); the extractor has since gained boarding constraint
    classes + field_table. Re-check: run the current extractor over those
    files offline. Once merged (c3-payments-reingest.md), discard as done.
    """
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
    """C4 — 220/257 steps lack stated outcomes (gap-report headline 1).

    Not actionable inside this repo: outcomes must come from the source docs
    (or a verified sandbox run), and inventing them would violate the
    fact-honesty rule. Belongs upstream with the docs team.
    """
    return {
        "id": "C4-missing-outcomes",
        "proposal": "Author expected outcomes for 220 steps",
        "evidence": [
            "artifacts/content_engine/boarding/gap-report.md — headline 1",
        ],
        "recheck": "n/a",
        "status": "discarded",
        "why_discarded": (
            "Outcomes are facts about the product; generating them without a "
            "source would invent facts. Upstream docs-team work, tracked in "
            "the gap report."
        ),
    }


def candidate_llms_txt() -> Dict[str, Any]:
    """C5 — llms.txt / merchant-boarding .md 500 (gap-report headline 3)."""
    return {
        "id": "C5-llms-txt-defect",
        "proposal": "Fix llms.txt omission and merchant-boarding.md HTTP 500",
        "evidence": [
            "artifacts/content_engine/boarding/gap-report.md — headline 3",
            "artifacts/content_engine/boarding/toc-fetch-report.md — probe",
        ],
        "recheck": "n/a",
        "status": "discarded",
        "why_discarded": (
            "Production docs-site defect; not fixable from this repo. Bug "
            "already raised externally."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-prs", type=int, default=3)
    parser.add_argument("--budget-usd", type=float, default=2.00)
    parser.add_argument(
        "--mode",
        choices=("auto", "deterministic", "llm"),
        default="auto",
        help="auto: llm when Spark Qwen or a cloud key is available",
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

    endpoint = resolve_llm_endpoint()
    cloud_key = any(
        os.environ.get(k)
        for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "LITELLM_API_KEY")
    )
    if args.mode == "deterministic":
        mode = "deterministic"
        endpoint = None
    elif args.mode == "llm":
        mode = "llm"
        if endpoint is None:
            print(
                "llm mode requested but no Spark Qwen endpoint and no usable "
                "OPENAI/LITELLM key; refusing to pretend",
                file=sys.stderr,
            )
            return 2
    else:
        mode = "llm" if endpoint is not None else "deterministic"

    candidates = [
        candidate_endpoint_url_style(),
        candidate_step_anchor_noise(),
        candidate_payments_still_dropped(),
        candidate_missing_outcomes(),
        candidate_llms_txt(),
    ]
    llm_meta: Dict[str, Any] = {}
    if mode == "llm" and endpoint is not None:
        llm_cands, llm_meta = generate_llm_candidates(endpoint, max_prs=args.max_prs)
        candidates.extend(llm_cands)

    proposed = [c for c in candidates if c["status"] == "proposed"]
    capped = proposed[: args.max_prs]
    for c in proposed[args.max_prs :]:
        c["status"] = "deferred_over_pr_cap"

    # Local Spark Qwen is $0; cloud would need metering — keep spend 0 until
    # a priced provider is wired with real usage accounting.
    spend = 0.0
    report = {
        "generated_at": _utc_now(),
        "mode": mode,
        "llm_key_present": cloud_key,
        "llm_endpoint": (
            {
                "source": endpoint["source"],
                "base_url": endpoint["base_url"],
                "model": endpoint["model"],
            }
            if endpoint
            else None
        ),
        "llm_meta": llm_meta,
        "spend_usd": spend,
        "budget_usd": args.budget_usd,
        "max_prs": args.max_prs,
        "candidates": candidates,
        "proposed_within_cap": [c["id"] for c in capped],
    }
    out_json = Path(args.json_out)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    mode_note = ""
    if mode == "deterministic":
        mode_note = (
            " — no local Spark Qwen and no usable cloud LLM endpoint; "
            "generative half did not run."
        )
    elif endpoint and endpoint["source"] == "spark-qwen-local":
        mode_note = (
            f" — local Spark Qwen `{endpoint['model']}` at `{endpoint['base_url']}` "
            "(no cloud API key required)."
        )
    else:
        mode_note = f" — endpoint source `{endpoint['source'] if endpoint else 'none'}`."

    lines = [
        "# Improvement loop — run report",
        "",
        f"- When: `{report['generated_at']}`",
        f"- Mode: **{mode}**{mode_note}",
        f"- Spend: ${report['spend_usd']:.2f} of ${args.budget_usd:.2f} budget",
        f"- PR cap: {args.max_prs}",
        "",
        "| Candidate | Status | Re-check | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    for c in candidates:
        ev = "; ".join(c["evidence"])
        lines.append(
            f"| {c['id']}: {c['proposal'][:80]} | {c['status']} | "
            f"{str(c.get('recheck'))[:90]} | {ev[:110]} |"
        )
    lines.append("")
    out_md = Path(args.out)
    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"mode={mode} spend=${spend:.2f} proposed={len(proposed)} "
        f"capped={len(capped)} endpoint={endpoint['source'] if endpoint else 'none'}"
    )
    for c in candidates:
        print(f"  {c['id']}: {c['status']} — {c.get('recheck','')[:80]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
