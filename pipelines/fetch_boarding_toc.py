#!/usr/bin/env python3
"""Fetch boarding docs from the site TOC — thin CLI over the engine module.

Depth lives in content_bench.content_engine.toc_fetch: the family TOC is the
denominator; llms.txt is a discovery hint; .md is fetched verbatim with an
HTML→markdown fallback reserved for broken endpoints.

This file holds only the CyberSource-specific configuration: family seeds,
the merchant-boarding alias probe, and report rendering.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.toc_fetch import (  # noqa: E402
    FamilySeed,
    fetch_family_corpus,
    http_get,
    llms_hint_urls,
)

BASE = "https://developer.cybersource.com"
UA = "CyberSource-Relay/1.0 (boarding-toc-fetch)"

FAMILY_SEEDS = (
    FamilySeed(
        family_id="boarding_rest",
        label="Boarding REST API",
        seed_url=f"{BASE}/docs/cybs/en-us/boarding/developer/all/rest/boarding.html",
        path_must_contain="/docs/cybs/en-us/boarding/developer/all/rest/boarding",
    ),
    FamilySeed(
        family_id="boarding_user",
        label="Boarding Business Center",
        seed_url=f"{BASE}/docs/cybs/en-us/boarding/user/all/ebc/boarding-user.html",
        path_must_contain="/docs/cybs/en-us/boarding/user/all/ebc/boarding-user",
    ),
    FamilySeed(
        family_id="boarding_template_mgmt",
        label="Boarding Template Management",
        seed_url=(
            f"{BASE}/docs/cybs/en-us/boarding-template-management/user/all/ada/"
            "boarding-template-mgmt.html"
        ),
        path_must_contain="/docs/cybs/en-us/boarding-template-management/",
    ),
)

# Agent-readiness probe — records production defects; never a TOC source.
MERCHANT_BOARDING = {
    "md_url": (
        f"{BASE}/docs/cybs/en-us/merchant-boarding/developer/all/rest/"
        "merchant-boarding.md"
    ),
    "html_url": (
        f"{BASE}/docs/cybs/en-us/merchant-boarding/developer/all/rest/"
        "merchant-boarding.html"
    ),
}


def probe_merchant_boarding(sleep_s: float) -> Dict[str, object]:
    out: Dict[str, object] = {
        "family_id": "merchant_boarding_alias",
        "label": "Merchant Boarding (path alias)",
        "md_url": MERCHANT_BOARDING["md_url"],
        "html_url": MERCHANT_BOARDING["html_url"],
        "in_llms_txt": False,
        "md": {},
        "html": {},
        "finding": "",
    }
    try:
        code, body, final = http_get(MERCHANT_BOARDING["md_url"], user_agent=UA)
        out["md"] = {
            "http_status": code,
            "bytes": len(body),
            "final_url": final,
            "body_preview": body[:80].decode("utf-8", errors="replace"),
        }
    except Exception as e:  # noqa: BLE001
        out["md"] = {"error": str(e)}
    time.sleep(sleep_s)
    try:
        code, body, final = http_get(
            MERCHANT_BOARDING["html_url"],
            headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
            },
        )
        out["html"] = {
            "http_status": code,
            "bytes": len(body),
            "final_url": final,
            "redirected": final.rstrip("/")
            != MERCHANT_BOARDING["html_url"].rstrip("/"),
        }
    except Exception as e:  # noqa: BLE001
        out["html"] = {"error": str(e)}

    md_status = (out.get("md") or {}).get("http_status")
    html_redirect = (out.get("html") or {}).get("redirected")
    out["finding"] = (
        f"merchant-boarding.md returns HTTP {md_status}; HTML "
        + (
            f"redirects to {(out.get('html') or {}).get('final_url')}"
            if html_redirect
            else "serves without redirect"
        )
        + ". Path alias is not a separate fetchable markdown family; "
        "programmatic surface lives under /boarding/developer/all/rest/boarding/."
    )
    return out


def render_report_md(report: Dict[str, object]) -> str:
    t = report["totals"]  # type: ignore[index]
    probe = report["merchant_boarding_probe"]  # type: ignore[index]
    lines = [
        "# Boarding TOC fetch report",
        "",
        f"- When: `{report['generated_at']}`",
        f"- Denominator rule: {report['denominator_rule']}",
        "",
        "## Headline finding (production docs site)",
        "",
        "**CyberSource `llms.txt` — the file that exists so AI agents can discover docs — "
        "does not list a distinct Merchant Boarding API family under `/merchant-boarding/`, "
        "and that path’s `.md` endpoint returns HTTP 500 while HTML redirects into the "
        "Business Center boarding guide.** Any agent that trusts the site’s own "
        "agent-readiness surface cannot reliably discover or read boarding via that alias.",
        "",
        f"- Probe: `{probe.get('finding')}`",
        f"- `merchant-boarding` listed in llms.txt: **{probe.get('in_llms_txt')}**",
        f"- llms.txt boarding-related `.md` URLs found: **{report['llms_txt']['boarding_related_md_urls']}**",  # type: ignore[index]
        "",
        "## Denominator vs fetch (site TOC)",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Topics in site TOC (denominator) | {t['toc_topics']} |",
        f"| Fetched OK | {t['fetched_ok']} |",
        f"| Via `.md` | {t['fetched_md']} |",
        f"| Via HTML→markdown fallback | {t['fetched_html_fallback']} |",
        f"| Failed | {t['failed']} |",
        f"| Usable (≥40 bytes) | {t['usable']} |",
        "",
        "## Families",
        "",
        "| Family | TOC topics | Fetched | `.md` | HTML fallback | Failed | Usable |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for f in report["families"]:  # type: ignore[index]
        lines.append(
            f"| {f['label']} (`{f['family_id']}`) | {f['toc_topics']} | "
            f"{f['fetched_ok']} | {f['fetched_md']} | {f['fetched_html_fallback']} | "
            f"{f['failed']} | {f['usable']} |"
        )
    lines += [
        "",
        "## Invariant",
        "",
        "A coverage denominator must come from the source of truth. `llms.txt` is not "
        "one — the site’s own navigation/TOC tree is. Every future family census must "
        "state where its denominator came from.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", default=str(ROOT / "data/products/boarding/guides"))
    parser.add_argument(
        "--report-dir", default=str(ROOT / "artifacts/content_engine/boarding")
    )
    parser.add_argument("--sleep", type=float, default=0.08)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    report_dir = Path(args.report_dir)
    out_dir = out_dir if out_dir.is_absolute() else ROOT / out_dir
    report_dir = report_dir if report_dir.is_absolute() else ROOT / report_dir

    llms_urls = llms_hint_urls(
        BASE, contains=("/boarding", "merchant-boarding"), user_agent=UA
    )
    probe = probe_merchant_boarding(args.sleep)
    probe["in_llms_txt"] = any("merchant-boarding" in u for u in llms_urls)

    report = fetch_family_corpus(
        FAMILY_SEEDS,
        base_url=BASE,
        out_dir=out_dir,
        root=ROOT,
        strip_prefix="/docs/cybs/",
        sleep_s=args.sleep,
        limit=args.limit,
        user_agent=UA,
    )
    report["llms_txt"] = {
        "boarding_related_md_urls": len(llms_urls),
        "urls": llms_urls,
        "merchant_boarding_listed": probe["in_llms_txt"],
    }
    report["merchant_boarding_probe"] = probe
    report["totals"]["prior_local_corpus_files"] = 9  # historical llms slice

    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "toc-fetch-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    md = render_report_md(report)
    (report_dir / "toc-fetch-report.md").write_text(md, encoding="utf-8")

    t = report["totals"]
    print(f"Wrote {report_dir / 'toc-fetch-report.md'}")
    print(
        f"TOC={t['toc_topics']} fetched={t['fetched_ok']} usable={t['usable']} "
        f"html_fallback={t['fetched_html_fallback']} llms_boarding_urls={len(llms_urls)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
