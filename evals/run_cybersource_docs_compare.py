#!/usr/bin/env python3
"""Compare generated payments pages against live developer.cybersource.com docs.

Evidence only — never a PR gate. Same taxonomy as the Stripe parity eval.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
OUT_MD = ROOT / "evals" / "cybersource-docs-compare.md"
OUT_JSON = ROOT / "evals" / "runs" / "cybersource-docs-compare.json"

UPSTREAM = {
    "payments_intro": "https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md",
    "payments_basic": "https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-processing-basic-intro.md",
    "rest_getting_started": "https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started.md",
    "llms_index": "https://developer.cybersource.com/llms.txt",
}


@dataclass
class Check:
    id: str
    area: str
    result: str  # pass | partial | fail | n/a
    ours: str
    upstream: str
    notes: str


def _utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def fetch(url: str, timeout: int = 30) -> Tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "content-bench-cs-docs-compare/0.1"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return 0, f"FETCH_ERROR: {exc}"


def load_ours() -> Dict[str, str]:
    pages = {}
    for path in sorted(CONTENT.glob("*.md")):
        if path.name == "README.md":
            continue
        pages[path.name] = path.read_text(encoding="utf-8")
    return pages


def evaluate(ours: Dict[str, str], upstream: Dict[str, str]) -> List[Check]:
    checks: List[Check] = []
    create = ours.get("createPayment.md", "")
    all_ours = "\n".join(ours.values())
    payments_intro = upstream.get("payments_intro", "")
    payments_basic = upstream.get("payments_basic", "")
    rest_gs = upstream.get("rest_getting_started", "")
    llms = upstream.get("llms_index", "")

    def add(cid, area, result, ours_s, up_s, notes):
        checks.append(Check(cid, area, result, ours_s, up_s, notes))

    add(
        "create_path",
        "Payments API",
        "pass" if "/pts/v2/payments" in create else "fail",
        "POST /pts/v2/payments" if "/pts/v2/payments" in create else "missing",
        "payments processing docs reference payment services",
        "Generated createPayment path must match Payments REST surface.",
    )
    add(
        "create_auth",
        "Auth",
        "pass" if "httpSignature" in create else "fail",
        "httpSignature" if "httpSignature" in create else "missing",
        "HTTP Signature is the sandbox auth for Payments REST",
        "Page must teach httpSignature from the OpenAPI security schemes.",
    )
    add(
        "flattened_amount",
        "Request fields",
        "pass"
        if "orderInformation.amountDetails.totalAmount" in create
        else "fail",
        "flattened totalAmount field",
        "amountDetails.totalAmount in payments guides",
        "A2 flatten: nested amount fields must appear as dotted names.",
    )
    add(
        "flattened_currency",
        "Request fields",
        "pass"
        if "orderInformation.amountDetails.currency" in create
        else "fail",
        "flattened currency field",
        "currency in amountDetails",
        "Currency must be present as a flattened body field.",
    )
    add(
        "no_raw_pan",
        "Safety",
        "pass"
        if re.search(r"(?i)raw\s*pan|tokenized|do not send raw", create)
        else "fail",
        "PAN guard language",
        "sandbox / testing guides discourage raw PAN misuse",
        "Sandbox payment pages must not encourage raw PAN in production.",
    )
    add(
        "ops_coverage",
        "Coverage",
        "pass"
        if all(f"{op}.md" in ours for op in (
            "createPayment", "getPayment", "capturePayment", "createCredit",
            "createCustomer", "getCustomer", "createMppCredentialSetup",
            "checkMppEnrollment",
        ))
        else "fail",
        f"{len(ours)} pages",
        "8 payments-core operations in local OpenAPI",
        "Every registered payments operation must have a generated page.",
    )
    add(
        "upstream_payments_reachable",
        "Upstream",
        "pass" if payments_intro and "FETCH_ERROR" not in payments_intro[:40] else "fail",
        "local generated pages",
        "developer.cybersource.com payments intro",
        "Parity job must fetch live public CS docs.",
    )
    add(
        "upstream_llms_reachable",
        "Upstream",
        "pass" if llms and "FETCH_ERROR" not in llms[:40] else "partial",
        "corpus from llms.txt ingestion",
        "developer.cybersource.com/llms.txt",
        "llms.txt index should remain fetchable for ingestion freshness.",
    )
    add(
        "rest_getting_started_aligned",
        "Onboarding",
        "partial"
        if rest_gs and ("http" in all_ours.lower() or "signature" in all_ours.lower())
        else "fail",
        "auth + payments pages",
        "REST getting started",
        "Aligned at a high level: auth + first payment concepts.",
    )
    add(
        "payments_basic_concepts",
        "Onboarding",
        "pass"
        if payments_basic and ("capture" in all_ours.lower() or "Capture" in all_ours)
        else "partial",
        "capturePayment page present" if "capturePayment.md" in ours else "missing capture",
        "basic payments processing intro",
        "Capture flow should appear in generated ops when present upstream.",
    )
    add(
        "provenance",
        "Provenance",
        "pass" if "generated_from_spec" in create or "generated: true" in create else "fail",
        "lineage_origin / generated flag",
        "n/a",
        "Pages must label themselves as generated from the OpenAPI unit.",
    )
    add(
        "no_raw_dir",
        "Serve contract",
        "pass" if "raw/" not in all_ours else "fail",
        "content/ only",
        "n/a",
        "Published pages must not point readers at raw/.",
    )
    return checks


def score(checks: List[Check]) -> Dict[str, float]:
    graded = [c for c in checks if c.result in ("pass", "partial", "fail")]
    if not graded:
        return {"score": 0.0, "pass": 0, "partial": 0, "fail": 0, "n_a": 0}
    weights = {"pass": 1.0, "partial": 0.5, "fail": 0.0}
    total = sum(weights[c.result] for c in graded) / len(graded)
    return {
        "score": round(total * 100, 1),
        "pass": sum(1 for c in graded if c.result == "pass"),
        "partial": sum(1 for c in graded if c.result == "partial"),
        "fail": sum(1 for c in graded if c.result == "fail"),
        "n_a": sum(1 for c in checks if c.result == "n/a"),
    }


def render(checks: List[Check], stats: Dict[str, float], fetched: Dict[str, int]) -> str:
    lines = [
        "# CyberSource docs comparison eval",
        "",
        f"- When: `{_utc()}`",
        "- Scope: generated `content/*.md` payments pages vs live developer.cybersource.com",
        f"- Fidelity score: **{stats['score']}%** "
        f"({stats['pass']} pass / {stats['partial']} partial / {stats['fail']} fail "
        f"of {stats['pass'] + stats['partial'] + stats['fail']} graded checks)",
        "",
        "## Sources fetched",
        "",
    ]
    for key, url in UPSTREAM.items():
        lines.append(f"- `{key}` → {url} (HTTP {fetched.get(key, 0)})")
    lines.extend(
        [
            "",
            "## Checks",
            "",
            "| ID | Area | Result | Notes |",
            "| --- | --- | --- | --- |",
        ]
    )
    for c in checks:
        lines.append(f"| `{c.id}` | {c.area} | **{c.result}** | {c.notes} |")
    lines.extend(["", "## Verdict", ""])
    if stats["fail"] == 0 and stats["score"] >= 70:
        lines.append(
            f"Parity evidence **pass** at {stats['score']}% on the graded checklist. "
            "Quote as “N of N parity checks,” not “identical to CyberSource.”"
        )
    else:
        fails = [c.id for c in checks if c.result == "fail"]
        lines.append(
            f"Parity incomplete ({stats['score']}%). Failing checks: {', '.join(fails) or 'none'}."
        )
    lines.extend(
        [
            "",
            "This parity eval is nightly evidence only — it must not gate PRs.",
            "Private corpus, traces, and drop logs must never be copied to public content-bench.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evidence",
        action="store_true",
        help="Always exit 0; write report as loop evidence (never fail CI).",
    )
    args = parser.parse_args()

    ours = load_ours()
    upstream: Dict[str, str] = {}
    fetched: Dict[str, int] = {}
    for key, url in UPSTREAM.items():
        status, body = fetch(url)
        fetched[key] = status
        upstream[key] = body

    checks = evaluate(ours, upstream)
    stats = score(checks)
    md = render(checks, stats, fetched)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md, encoding="utf-8")
    payload = {
        "at": _utc(),
        "stats": stats,
        "fetched": fetched,
        "checks": [asdict(c) for c in checks],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(
        f"Score {stats['score']}% "
        f"(pass={stats['pass']} partial={stats['partial']} fail={stats['fail']})"
    )
    if args.evidence:
        return 0
    return 0 if stats["fail"] == 0 and stats["score"] >= 70 else 1


if __name__ == "__main__":
    raise SystemExit(main())
