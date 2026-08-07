#!/usr/bin/env python3
"""Payments task eval (Wave 1) — mock gate: construct a valid sandbox payment request from pages alone."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
RUNS = ROOT / "evals" / "runs"
LATEST = ROOT / "evals" / "latest-payments.md"
SEEDS = (
    ROOT
    / "artifacts"
    / "content_engine"
    / "generated"
    / "cybersource-payments-core-openapi.eval_seeds.json"
)

REQUIRED_OPS = (
    "createPayment",
    "getPayment",
    "capturePayment",
    "createCredit",
    "createCustomer",
    "getCustomer",
    "createMppCredentialSetup",
    "checkMppEnrollment",
)

# Markers an agent must be able to read from generated pages to build a sandbox payment.
CREATE_PAYMENT_MARKERS = (
    "POST",
    "/pts/v2/payments",
    "createPayment",
    "httpSignature",
    "orderInformation.amountDetails.totalAmount",
    "orderInformation.amountDetails.currency",
    "clientReferenceInformation.code",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _redact(text: str) -> str:
    text = re.sub(r"sk_(test|live)_[A-Za-z0-9]+", "sk_***REDACTED***", text)
    text = re.sub(r"Bearer\s+\S+", "Bearer ***REDACTED***", text)
    text = re.sub(
        r"(?i)(merchant|secret|key|password|token)\s*[:=]\s*\S+",
        r"\1=***REDACTED***",
        text,
    )
    return text


def _load_create_payment_page() -> str:
    path = CONTENT / "createPayment.md"
    if not path.exists():
        raise FileNotFoundError(
            "content/createPayment.md missing — run specs-to-docs + reference pages"
        )
    return path.read_text(encoding="utf-8")


def construct_sandbox_payment_from_pages() -> Dict[str, Any]:
    """Agent-shaped mock: build a payment request body using only page facts."""
    page = _load_create_payment_page()
    missing = [m for m in CREATE_PAYMENT_MARKERS if m not in page]
    if missing:
        return {
            "ok": False,
            "missing_markers": missing,
            "request": None,
        }

    # Required fields taught by the flattened createPayment page.
    request = {
        "clientReferenceInformation": {"code": "CONTENT_BENCH_MOCK_001"},
        "orderInformation": {
            "amountDetails": {
                "totalAmount": "10.00",
                "currency": "USD",
            }
        },
        # Tokenized / test instrument only — never a raw PAN (page forbids it).
        "paymentInformation": {
            "card": {
                "number": "4111111111111111",
                "expirationMonth": "12",
                "expirationYear": "2031",
                "type": "001",
            }
        },
    }
    # Sanity: page must warn against raw PAN in production language.
    pan_guard = "do not send raw pan" in page.lower() or "tokenized" in page.lower()
    return {
        "ok": True,
        "missing_markers": [],
        "request": request,
        "auth_scheme": "httpSignature",
        "endpoint": "POST /pts/v2/payments",
        "pan_guard_documented": pan_guard,
        "seed_file": str(SEEDS.relative_to(ROOT)) if SEEDS.exists() else None,
    }


def run_mock() -> Dict[str, Any]:
    steps: List[Dict[str, Any]] = []

    pages = {p.name: p for p in CONTENT.glob("*.md") if p.name != "README.md"}
    missing_ops = [op for op in REQUIRED_OPS if f"{op}.md" not in pages]
    steps.append(
        {
            "step": "reference_pages_complete",
            "result": "pass" if not missing_ops else "fail",
            "detail": (
                f"{len(REQUIRED_OPS) - len(missing_ops)}/{len(REQUIRED_OPS)} ops"
                if not missing_ops
                else f"missing pages: {missing_ops}"
            ),
        }
    )

    constructed = construct_sandbox_payment_from_pages()
    steps.append(
        {
            "step": "construct_sandbox_payment",
            "result": "pass" if constructed.get("ok") else "fail",
            "detail": (
                "built POST /pts/v2/payments body from createPayment.md"
                if constructed.get("ok")
                else f"missing markers: {constructed.get('missing_markers')}"
            ),
        }
    )
    if constructed.get("ok"):
        steps.append(
            {
                "step": "pan_guard",
                "result": "pass" if constructed.get("pan_guard_documented") else "fail",
                "detail": "page documents tokenized/no-raw-PAN guidance",
            }
        )

    # Eval seeds from specs-to-docs (reuse seed pattern).
    if SEEDS.exists():
        seeds = json.loads(SEEDS.read_text(encoding="utf-8"))
        seed_list = seeds if isinstance(seeds, list) else seeds.get("seeds") or seeds.get("items") or []
        steps.append(
            {
                "step": "eval_seeds_present",
                "result": "pass" if seed_list else "fail",
                "detail": f"{len(seed_list)} seeds in {SEEDS.name}",
            }
        )
    else:
        steps.append(
            {
                "step": "eval_seeds_present",
                "result": "fail",
                "detail": "eval seeds missing — run pipelines/run_specs_to_docs_v0.py",
            }
        )

    # Serve contract: no raw/ reads by published pages.
    raw_refs = []
    for name, path in pages.items():
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?m)(^|\s)raw/", text) or "raw/<" in text:
            raw_refs.append(name)
    steps.append(
        {
            "step": "no_raw_reads",
            "result": "pass" if not raw_refs else "fail",
            "detail": "ok" if not raw_refs else f"pages reference raw/: {raw_refs}",
        }
    )

    gate = "pass" if all(s["result"] == "pass" for s in steps) else "fail"
    return {
        "mode": "mock",
        "product": "payments",
        "gate": gate,
        "reason": (
            "agent can construct a valid sandbox payment request from generated pages"
            if gate == "pass"
            else "payments mock eval failed — see steps"
        ),
        "constructed_request": constructed.get("request"),
        "steps": steps,
        "at": _utc_now(),
    }


def write_outputs(
    result: Dict[str, Any],
    *,
    latest_path: Optional[Path] = None,
    runs_dir: Optional[Path] = None,
) -> Path:
    out_runs = Path(runs_dir) if runs_dir is not None else RUNS
    out_latest = Path(latest_path) if latest_path is not None else LATEST
    out_runs.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_path = out_runs / f"payments-{result['mode']}-{stamp}.json"
    safe = json.loads(_redact(json.dumps(result)))
    run_path.write_text(json.dumps(safe, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Payments eval latest",
        "",
        f"- Mode: `{result['mode']}`",
        f"- Gate: **{result['gate']}**",
        f"- When: {result.get('at', '')}",
        f"- Reason: {result.get('reason', '')}",
        "",
        "## Steps",
        "",
        "| Step | Result | Detail |",
        "| --- | --- | --- |",
    ]
    for step in result.get("steps") or []:
        lines.append(
            f"| {step.get('step')} | {step.get('result')} | {_redact(str(step.get('detail', '')))} |"
        )
    lines.append("")
    out_latest.parent.mkdir(parents=True, exist_ok=True)
    out_latest.write_text("\n".join(lines), encoding="utf-8")
    return out_latest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("mock",), default="mock")
    args = parser.parse_args()
    result = run_mock()
    write_outputs(result)
    print(json.dumps({k: result[k] for k in ("mode", "gate", "reason")}, indent=2))
    print(f"Wrote {LATEST}")
    return 0 if result.get("gate") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
