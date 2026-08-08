#!/usr/bin/env python3
"""Improvement loop: evidence -> candidates -> re-check -> capped proposals.

Reads only evidence artifacts and normalized/ (never raw/). Each candidate
names the evidence it was drawn from and is re-checked against the current
repo state before it may become a proposal; failures are recorded, not
discarded silently.

Modes:
  deterministic (default) — rule-based candidate generators; cost $0.00.
  llm — requires ANTHROPIC_API_KEY; refuses to pretend otherwise.

Caps: --max-prs (default 3), --budget-usd (default 2.00).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.ingest import (  # noqa: E402
    _extract_claims_from_text,
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


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
    files offline.
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
        ],
    }
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
        "--out",
        default=str(ROOT / "artifacts/improvement_loop/run-report.md"),
    )
    parser.add_argument(
        "--json-out",
        default=str(ROOT / "artifacts/improvement_loop/run-report.json"),
    )
    args = parser.parse_args()

    llm_key = any(
        os.environ.get(k)
        for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "LITELLM_API_KEY")
    )
    mode = "llm" if llm_key else "deterministic"

    candidates = [
        candidate_endpoint_url_style(),
        candidate_step_anchor_noise(),
        candidate_payments_still_dropped(),
        candidate_missing_outcomes(),
        candidate_llms_txt(),
    ]
    proposed = [c for c in candidates if c["status"] == "proposed"]
    capped = proposed[: args.max_prs]
    for c in proposed[args.max_prs :]:
        c["status"] = "deferred_over_pr_cap"

    report = {
        "generated_at": _utc_now(),
        "mode": mode,
        "llm_key_present": llm_key,
        "spend_usd": 0.0,
        "budget_usd": args.budget_usd,
        "max_prs": args.max_prs,
        "candidates": candidates,
        "proposed_within_cap": [c["id"] for c in capped],
    }
    out_json = Path(args.json_out)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Improvement loop — run report",
        "",
        f"- When: `{report['generated_at']}`",
        f"- Mode: **{mode}**"
        + (
            ""
            if llm_key
            else " — no LLM API key present in the environment; the LLM path "
            "did not run and no key was extracted from credential stores."
        ),
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
    print(f"mode={mode} spend=$0.00 proposed={len(proposed)} capped={len(capped)}")
    for c in candidates:
        print(f"  {c['id']}: {c['status']} — {c.get('recheck','')[:80]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
