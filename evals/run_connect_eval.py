#!/usr/bin/env python3
"""Stripe Connect eval gate: mock (CI) or live test-mode Account + Account Link."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
RUNS = ROOT / "evals" / "runs"
LATEST = ROOT / "evals" / "latest.md"

REQUIRED_QUICKSTART_MARKERS = (
    "STRIPE_TEST_SECRET_KEY",
    "POST /v1/accounts",
    "POST /v1/account_links",
    "account_onboarding",
    "sk_test_",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _redact(text: str) -> str:
    text = re.sub(r"sk_(test|live)_[A-Za-z0-9]+", "sk_***REDACTED***", text)
    text = re.sub(r"Bearer\s+\S+", "Bearer ***REDACTED***", text)
    return text


def run_mock() -> Dict[str, Any]:
    quickstart = CONTENT / "connect-quickstart.md"
    steps: List[Dict[str, Any]] = []
    if not quickstart.exists():
        return {
            "mode": "mock",
            "gate": "fail",
            "reason": "content/connect-quickstart.md missing — run pipelines/run_stripe_connect_proof.py",
            "steps": [],
        }
    body = quickstart.read_text(encoding="utf-8")
    missing = [m for m in REQUIRED_QUICKSTART_MARKERS if m not in body]
    steps.append(
        {
            "step": "docs_gate",
            "result": "pass" if not missing else "fail",
            "detail": "ok" if not missing else f"missing markers: {missing}",
        }
    )
    pages = list(CONTENT.glob("connect-*.md"))
    steps.append(
        {
            "step": "fact_pages",
            "result": "pass" if pages else "fail",
            "detail": f"{len(pages)} connect-*.md pages",
        }
    )
    gate = "pass" if not missing and pages else "fail"
    return {
        "mode": "mock",
        "gate": gate,
        "reason": "generated Connect docs contain required onboarding facts",
        "steps": steps,
        "at": _utc_now(),
    }


def _stripe_form(
    path: str,
    secret: str,
    fields: Dict[str, str],
) -> Tuple[int, Dict[str, Any], str]:
    if not secret.startswith("sk_test_"):
        raise ValueError("Live eval requires a test-mode key (sk_test_...). Refusing other key types.")
    data = urllib.parse.urlencode(fields).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.stripe.com{path}",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {secret}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw), raw
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"error": {"message": raw[:500]}}
        return exc.code, payload, raw


def run_live(secret: str) -> Dict[str, Any]:
    steps: List[Dict[str, Any]] = []
    # Create account
    status, account, raw = _stripe_form(
        "/v1/accounts",
        secret,
        {
            "type": "express",
            "country": "US",
            "capabilities[card_payments][requested]": "true",
            "capabilities[transfers][requested]": "true",
        },
    )
    steps.append(
        {
            "step": "create_account",
            "result": "pass" if status == 200 and account.get("id", "").startswith("acct_") else "fail",
            "http_status": status,
            "account_id": account.get("id"),
            "detail": _redact(json.dumps(account.get("error", account.get("id")))) ,
        }
    )
    if steps[-1]["result"] != "pass":
        return {
            "mode": "live",
            "gate": "fail",
            "reason": "account creation failed",
            "steps": steps,
            "at": _utc_now(),
        }

    status2, link, raw2 = _stripe_form(
        "/v1/account_links",
        secret,
        {
            "account": account["id"],
            "refresh_url": "https://example.com/reauth",
            "return_url": "https://example.com/return",
            "type": "account_onboarding",
        },
    )
    ok = status2 == 200 and bool(link.get("url"))
    steps.append(
        {
            "step": "create_account_link",
            "result": "pass" if ok else "fail",
            "http_status": status2,
            "has_url": bool(link.get("url")),
            "detail": _redact(json.dumps(link.get("error", {"expires_at": link.get("expires_at")}))),
        }
    )
    return {
        "mode": "live",
        "gate": "pass" if ok else "fail",
        "reason": "created connected account + Account Link in test mode"
        if ok
        else "Account Link creation failed",
        "steps": steps,
        "at": _utc_now(),
    }


def write_outputs(result: Dict[str, Any]) -> None:
    RUNS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_path = RUNS / f"connect-{result['mode']}-{stamp}.json"
    safe = json.loads(_redact(json.dumps(result)))
    run_path.write_text(json.dumps(safe, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Connect eval latest",
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
    LATEST.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Stripe Connect eval gate")
    parser.add_argument("--mode", choices=("mock", "live"), default="mock")
    args = parser.parse_args()

    if args.mode == "mock":
        result = run_mock()
    else:
        secret = os.environ.get("STRIPE_TEST_SECRET_KEY", "").strip()
        if not secret:
            print("STRIPE_TEST_SECRET_KEY not set", file=sys.stderr)
            return 2
        try:
            result = run_live(secret)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    write_outputs(result)
    print(json.dumps({k: result[k] for k in ("mode", "gate", "reason")}, indent=2))
    print(f"Wrote {LATEST}")
    return 0 if result.get("gate") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
