#!/usr/bin/env python3
"""Fetch boarding docs from the site TOC — not llms.txt alone.

Denominator = unique topic paths listed in each family's HTML table of contents.
For each topic: try `.md` first; on 4xx/5xx fall back to HTML→markdown.

Families:
  - Boarding REST API  (/boarding/developer/all/rest/boarding)
  - Boarding Business Center (/boarding/user/all/ebc/boarding-user)
  - Boarding Template Management (/boarding-template-management/...)
  - Merchant Boarding alias (/merchant-boarding/...) — probed for agent-readiness
    defects (llms omission / .md 500 / HTML redirect).
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BASE = "https://developer.cybersource.com"
UA = {
    "User-Agent": "CyberSource-Relay/1.0 (boarding-toc-fetch)",
    "Accept": "text/markdown, text/plain;q=0.9, */*;q=0.1",
}

FAMILY_SEEDS = (
    {
        "family_id": "boarding_rest",
        "label": "Boarding REST API",
        "seed_url": f"{BASE}/docs/cybs/en-us/boarding/developer/all/rest/boarding.html",
        "path_must_contain": "/docs/cybs/en-us/boarding/developer/all/rest/boarding",
    },
    {
        "family_id": "boarding_user",
        "label": "Boarding Business Center",
        "seed_url": f"{BASE}/docs/cybs/en-us/boarding/user/all/ebc/boarding-user.html",
        "path_must_contain": "/docs/cybs/en-us/boarding/user/all/ebc/boarding-user",
    },
    {
        "family_id": "boarding_template_mgmt",
        "label": "Boarding Template Management",
        "seed_url": (
            f"{BASE}/docs/cybs/en-us/boarding-template-management/user/all/ada/"
            "boarding-template-mgmt.html"
        ),
        "path_must_contain": "/docs/cybs/en-us/boarding-template-management/",
    },
)

# Agent-readiness probe — not a TOC source of truth; records production defects.
MERCHANT_BOARDING_PROBE = {
    "family_id": "merchant_boarding_alias",
    "label": "Merchant Boarding (path alias)",
    "md_url": (
        f"{BASE}/docs/cybs/en-us/merchant-boarding/developer/all/rest/"
        "merchant-boarding.md"
    ),
    "html_url": (
        f"{BASE}/docs/cybs/en-us/merchant-boarding/developer/all/rest/"
        "merchant-boarding.html"
    ),
}


@dataclass
class FetchResult:
    topic_path: str
    family_id: str
    status: str  # ok_md | ok_html_fallback | fail
    http_status_md: Optional[int] = None
    http_status_html: Optional[int] = None
    final_url: Optional[str] = None
    bytes: int = 0
    local_path: Optional[str] = None
    error: Optional[str] = None


@dataclass
class FamilyReport:
    family_id: str
    label: str
    seed_url: str
    final_seed_url: str
    denominator_source: str
    toc_topics: int
    fetched_ok: int
    fetched_md: int
    fetched_html_fallback: int
    failed: int
    usable: int
    topics: List[str] = field(default_factory=list)


class _MainTextExtractor(HTMLParser):
    """Minimal HTML→markdown for docs pages (stdlib only)."""

    SKIP = {"script", "style", "noscript", "svg", "head"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip_depth = 0
        self._parts: List[str] = []
        self._in_a = False
        self._a_href = ""
        self._a_text: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        t = tag.lower()
        if t in self.SKIP:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if t in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(t[1])
            self._parts.append("\n\n" + "#" * level + " ")
        elif t == "p":
            self._parts.append("\n\n")
        elif t in {"li"}:
            self._parts.append("\n- ")
        elif t == "br":
            self._parts.append("\n")
        elif t == "a":
            self._in_a = True
            self._a_href = dict(attrs).get("href") or ""
            self._a_text = []
        elif t in {"code", "pre"}:
            self._parts.append("`")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if t in self.SKIP and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if t == "a" and self._in_a:
            text = "".join(self._a_text).strip()
            if text and self._a_href:
                self._parts.append(f"[{text}]({self._a_href})")
            elif text:
                self._parts.append(text)
            self._in_a = False
        elif t in {"code", "pre"}:
            self._parts.append("`")
        elif t in {"h1", "h2", "h3", "h4", "h5", "h6", "p"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._in_a:
            self._a_text.append(data)
        else:
            self._parts.append(data)

    def text(self) -> str:
        raw = "".join(self._parts)
        raw = html_lib.unescape(raw)
        raw = re.sub(r"[ \t]+\n", "\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip() + "\n"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _http_get(
    url: str,
    *,
    timeout: int = 30,
    headers: Optional[Dict[str, str]] = None,
) -> Tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers=headers or UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            final = resp.geturl()
            code = getattr(resp, "status", 200) or 200
            return int(code), body, final
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return int(e.code), body, url
    except Exception as e:
        raise RuntimeError(str(e)) from e


def _looks_like_markdown(text: str) -> bool:
    head = text.lstrip()[:400].lower()
    if head.startswith("<!doctype") or head.startswith("<html"):
        return False
    if "skip to login" in head and "skip to content" in head:
        return False
    # CyberSource DITA-ish markdown signals
    if "{#" in text[:500] or re.search(r"(?m)^[=-]{3,}\s*$", text[:800]):
        return True
    if text.lstrip().startswith("#") and "<nav" not in head:
        return True
    # Short declarative pages without heading markers still count
    return len(text.strip()) >= 40 and "<html" not in head


def _topic_id(path: str) -> str:
    if path.endswith(".md"):
        return path[:-3]
    if path.endswith(".html"):
        return path[:-5]
    return path


def extract_toc_topics(html: str, path_must_contain: str) -> List[str]:
    topics: Set[str] = set()
    for href in re.findall(r'href=["\']([^"\'#]+)["\']', html, re.I):
        if href.startswith("//") or href.startswith("mailto:"):
            continue
        full = urljoin(BASE, href)
        path = urlparse(full).path
        if path_must_contain not in path:
            continue
        if not (path.endswith(".html") or path.endswith(".md")):
            continue
        topics.add(_topic_id(path))
    return sorted(topics)


def url_to_local_name(topic_path: str) -> str:
    # /docs/cybs/en-us/boarding/... → en-us_boarding_....md.md (legacy twin-suffix)
    rel = topic_path
    if rel.startswith("/docs/cybs/"):
        rel = rel[len("/docs/cybs/") :]
    elif rel.startswith("/"):
        rel = rel[1:]
    return rel.replace("/", "_") + ".md.md"


def html_to_markdown(html: str, *, source_url: str) -> str:
    parser = _MainTextExtractor()
    parser.feed(html)
    body = parser.text()
    return f"<!-- source: {source_url} (html-fallback) -->\n\n{body}"


def fetch_topic(
    topic_path: str,
    *,
    family_id: str,
    out_dir: Path,
    sleep_s: float,
) -> FetchResult:
    md_url = f"{BASE}{topic_path}.md"
    html_url = f"{BASE}{topic_path}.html"
    local_name = url_to_local_name(topic_path)
    dest = out_dir / local_name
    result = FetchResult(topic_path=topic_path, family_id=family_id, status="fail")
    md_errors: List[str] = []

    # Prefer .md; retry once on transient failure (rate limits / flaky 5xx).
    for attempt in range(2):
        try:
            code, body, final = _http_get(md_url)
            result.http_status_md = code
            result.final_url = final
            if code == 200 and body and body.strip().lower() not in {b"error", b""}:
                text = body.decode("utf-8", errors="replace")
                if not _looks_like_markdown(text):
                    md_errors.append(f"attempt{attempt+1}: not markdown (HTTP {code})")
                    time.sleep(0.35)
                    continue
                dest.write_text(
                    text if text.endswith("\n") else text + "\n", encoding="utf-8"
                )
                result.status = "ok_md"
                result.bytes = len(body)
                result.local_path = str(dest.relative_to(ROOT))
                result.error = None
                time.sleep(sleep_s)
                return result
            md_errors.append(f"attempt{attempt+1}: HTTP {code}")
        except Exception as e:
            md_errors.append(f"attempt{attempt+1}: {e}")
        time.sleep(0.35)

    result.error = "md: " + "; ".join(md_errors)

    # HTML fallback — only when .md is broken (e.g. merchant-boarding 500).
    html_headers = {
        "User-Agent": UA["User-Agent"],
        "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    }
    try:
        code, body, final = _http_get(html_url, headers=html_headers)
        result.http_status_html = code
        result.final_url = final
        if code == 200 and body:
            md = html_to_markdown(
                body.decode("utf-8", errors="replace"), source_url=final
            )
            # Reject chrome-only conversions (nav shell without topic body).
            if md.count("\n") < 8 or (
                "skip to login" in md.lower() and "{#" not in md and len(md) < 2000
            ):
                result.error = (result.error or "") + "; html: chrome-only conversion"
            else:
                dest.write_text(md, encoding="utf-8")
                result.status = "ok_html_fallback"
                result.bytes = len(md.encode("utf-8"))
                result.local_path = str(dest.relative_to(ROOT))
                time.sleep(sleep_s)
                return result
        else:
            result.error = (result.error or "") + f"; html HTTP {code}"
    except Exception as e:
        result.error = (result.error or "") + f"; html: {e}"

    time.sleep(sleep_s)
    return result


def probe_merchant_boarding(sleep_s: float) -> Dict[str, object]:
    probe = dict(MERCHANT_BOARDING_PROBE)
    out: Dict[str, object] = {
        "family_id": probe["family_id"],
        "label": probe["label"],
        "md_url": probe["md_url"],
        "html_url": probe["html_url"],
        "in_llms_txt": False,
        "md": {},
        "html": {},
        "finding": "",
    }
    try:
        code, body, final = _http_get(probe["md_url"])
        out["md"] = {
            "http_status": code,
            "bytes": len(body),
            "final_url": final,
            "body_preview": body[:80].decode("utf-8", errors="replace"),
        }
    except Exception as e:
        out["md"] = {"error": str(e)}
    time.sleep(sleep_s)
    try:
        code, body, final = _http_get(probe["html_url"])
        out["html"] = {
            "http_status": code,
            "bytes": len(body),
            "final_url": final,
            "redirected": final.rstrip("/") != probe["html_url"].rstrip("/"),
        }
    except Exception as e:
        out["html"] = {"error": str(e)}

    md_status = (out.get("md") or {}).get("http_status")
    html_redirect = (out.get("html") or {}).get("redirected")
    out["finding"] = (
        "merchant-boarding.md returns HTTP "
        f"{md_status}; HTML "
        + (
            f"redirects to {(out.get('html') or {}).get('final_url')}"
            if html_redirect
            else "serves without redirect"
        )
        + ". Path alias is not a separate fetchable markdown family; "
        "programmatic surface lives under /boarding/developer/all/rest/boarding/."
    )
    return out


def llms_boarding_urls() -> List[str]:
    code, body, _ = _http_get(f"{BASE}/llms.txt")
    if code != 200:
        return []
    text = body.decode("utf-8", errors="replace")
    urls = re.findall(
        r"https://developer\.cybersource\.com/docs/cybs/[^\s\)\"]+?\.md", text
    )
    return sorted(
        {
            u
            for u in urls
            if "/boarding" in u or "merchant-boarding" in u
        }
    )


def run(
    *,
    out_dir: Path,
    report_dir: Path,
    sleep_s: float = 0.08,
    limit: Optional[int] = None,
) -> Dict[str, object]:
    out_dir = out_dir if out_dir.is_absolute() else (ROOT / out_dir)
    report_dir = report_dir if report_dir.is_absolute() else (ROOT / report_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    llms_urls = llms_boarding_urls()
    merchant_probe = probe_merchant_boarding(sleep_s)
    merchant_probe["in_llms_txt"] = any("merchant-boarding" in u for u in llms_urls)

    family_reports: List[FamilyReport] = []
    all_results: List[FetchResult] = []
    all_topics: List[Tuple[str, str]] = []  # (family_id, topic)

    for fam in FAMILY_SEEDS:
        code, body, final = _http_get(fam["seed_url"])
        if code != 200:
            raise RuntimeError(f"seed fetch failed {fam['seed_url']}: HTTP {code}")
        html = body.decode("utf-8", errors="replace")
        topics = extract_toc_topics(html, fam["path_must_contain"])
        if limit is not None:
            topics = topics[:limit]
        fr = FamilyReport(
            family_id=fam["family_id"],
            label=fam["label"],
            seed_url=fam["seed_url"],
            final_seed_url=final,
            denominator_source="site_html_toc",
            toc_topics=len(topics),
            fetched_ok=0,
            fetched_md=0,
            fetched_html_fallback=0,
            failed=0,
            usable=0,
            topics=topics,
        )
        print(f"{fam['family_id']}: TOC topics={len(topics)} (denominator=site HTML TOC)")
        for topic in topics:
            res = fetch_topic(
                topic, family_id=fam["family_id"], out_dir=out_dir, sleep_s=sleep_s
            )
            all_results.append(res)
            all_topics.append((fam["family_id"], topic))
            if res.status.startswith("ok"):
                fr.fetched_ok += 1
                if res.status == "ok_md":
                    fr.fetched_md += 1
                else:
                    fr.fetched_html_fallback += 1
                if res.bytes >= 40:
                    fr.usable += 1
            else:
                fr.failed += 1
            print(f"  {res.status:18} {res.bytes:7} {topic.split('/')[-1]}")
        family_reports.append(fr)

    toc_total = sum(f.toc_topics for f in family_reports)
    fetched_ok = sum(f.fetched_ok for f in family_reports)
    usable = sum(f.usable for f in family_reports)
    html_fallback = sum(f.fetched_html_fallback for f in family_reports)

    report = {
        "generated_at": _utc_now(),
        "denominator_rule": (
            "Coverage denominator is the site's own HTML navigation/TOC tree "
            "for each family — not llms.txt. llms.txt is an incomplete discovery aid."
        ),
        "llms_txt": {
            "boarding_related_md_urls": len(llms_urls),
            "urls": llms_urls,
            "merchant_boarding_listed": merchant_probe["in_llms_txt"],
        },
        "merchant_boarding_probe": merchant_probe,
        "totals": {
            "toc_topics": toc_total,
            "fetched_ok": fetched_ok,
            "fetched_md": sum(f.fetched_md for f in family_reports),
            "fetched_html_fallback": html_fallback,
            "failed": sum(f.failed for f in family_reports),
            "usable": usable,
            "prior_local_corpus_files": 9,
        },
        "families": [asdict(f) for f in family_reports],
        "results": [asdict(r) for r in all_results],
        "out_dir": str(out_dir.relative_to(ROOT)),
    }

    report_json = report_dir / "toc-fetch-report.json"
    report_md = report_dir / "toc-fetch-report.md"
    report_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    report_md.write_text(render_report_md(report), encoding="utf-8")
    print(f"Wrote {report_md}")
    print(
        f"TOC={toc_total} fetched={fetched_ok} usable={usable} "
        f"html_fallback={html_fallback} llms_boarding_urls={len(llms_urls)}"
    )
    return report


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
        f"| Prior local corpus (llms/filename slice) | {t['prior_local_corpus_files']} |",
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
    parser.add_argument(
        "--out-dir",
        default=str(ROOT / "data/products/boarding/guides"),
    )
    parser.add_argument(
        "--report-dir",
        default=str(ROOT / "artifacts/content_engine/boarding"),
    )
    parser.add_argument("--sleep", type=float, default=0.08)
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional per-family topic cap (for smoke tests)",
    )
    args = parser.parse_args()
    run(
        out_dir=Path(args.out_dir),
        report_dir=Path(args.report_dir),
        sleep_s=args.sleep,
        limit=args.limit,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
