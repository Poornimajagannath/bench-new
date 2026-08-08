"""Family TOC fetch — cross-check adapter against the product root.

Deep module: interface = family seeds -> TOC topic list -> local paths +
fetch report. The **product root** (see ``product_roots.py``) is the corpus
source of truth and coverage denominator. This module remains the TOC
walker used as a cross-check: any TOC page whose content does not appear in
its product root is a real gap.

Two adapters justify the seam:

  * **Site HTML TOC** — navigation tree used for the cross-check topic list.
  * **llms.txt** — a discovery *hint*, never a denominator. Demonstrated:
    3 boarding entries listed vs 80+ pages in the family TOC.

Fidelity rule: a paraphrase must never enter raw/. Topics are fetched with a
plain HTTP client, `.md` first, byte-for-byte (trailing newline normalized
only). HTML->markdown conversion is a *fallback* reserved for broken `.md`
endpoints, and its output is marked in-band as html-fallback.
"""

from __future__ import annotations

import html as html_lib
import json
import re
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple
from urllib.parse import urljoin, urlparse

DEFAULT_UA = "Content-Bench/1.0 (toc-fetch)"


@dataclass
class FamilySeed:
    """One documentation family: where its TOC lives, which paths belong."""

    family_id: str
    label: str
    seed_url: str
    path_must_contain: str


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
    """Minimal HTML->markdown for docs pages (stdlib only)."""

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
            self._parts.append("\n\n" + "#" * int(t[1]) + " ")
        elif t == "p":
            self._parts.append("\n\n")
        elif t == "li":
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


def http_get(
    url: str,
    *,
    timeout: int = 30,
    headers: Optional[Dict[str, str]] = None,
    user_agent: str = DEFAULT_UA,
) -> Tuple[int, bytes, str]:
    hdrs = headers or {
        "User-Agent": user_agent,
        "Accept": "text/markdown, text/plain;q=0.9, */*;q=0.1",
    }
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return int(getattr(resp, "status", 200) or 200), body, resp.geturl()
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return int(e.code), body, url
    except Exception as e:  # noqa: BLE001 - callers record the failure
        raise RuntimeError(str(e)) from e


def topic_id(path: str) -> str:
    if path.endswith(".md"):
        return path[:-3]
    if path.endswith(".html"):
        return path[:-5]
    return path


def extract_toc_topics(html: str, base_url: str, path_must_contain: str) -> List[str]:
    """The denominator: unique topic paths in the family's own TOC."""
    topics: Set[str] = set()
    for href in re.findall(r'href=["\']([^"\'#]+)["\']', html, re.I):
        if href.startswith("//") or href.startswith("mailto:"):
            continue
        path = urlparse(urljoin(base_url, href)).path
        if path_must_contain not in path:
            continue
        if not (path.endswith(".html") or path.endswith(".md")):
            continue
        topics.add(topic_id(path))
    return sorted(topics)


def url_to_local_name(topic_path: str, *, strip_prefix: str = "") -> str:
    rel = topic_path
    if strip_prefix and rel.startswith(strip_prefix):
        rel = rel[len(strip_prefix):]
    if rel.startswith("/"):
        rel = rel[1:]
    return rel.replace("/", "_") + ".md.md"


def looks_like_markdown(text: str) -> bool:
    head = text.lstrip()[:400].lower()
    if head.startswith("<!doctype") or head.startswith("<html"):
        return False
    if "skip to login" in head and "skip to content" in head:
        return False
    if "{#" in text[:500] or re.search(r"(?m)^[=-]{3,}\s*$", text[:800]):
        return True
    if text.lstrip().startswith("#") and "<nav" not in head:
        return True
    return len(text.strip()) >= 40 and "<html" not in head


def html_to_markdown(html: str, *, source_url: str) -> str:
    parser = _MainTextExtractor()
    parser.feed(html)
    return f"<!-- source: {source_url} (html-fallback) -->\n\n{parser.text()}"


def fetch_topic(
    topic_path: str,
    *,
    base_url: str,
    family_id: str,
    out_dir: Path,
    root: Path,
    strip_prefix: str = "",
    sleep_s: float = 0.08,
    user_agent: str = DEFAULT_UA,
) -> FetchResult:
    """Fetch one topic: `.md` verbatim first; HTML fallback only if .md is broken."""
    md_url = f"{base_url}{topic_path}.md"
    html_url = f"{base_url}{topic_path}.html"
    dest = out_dir / url_to_local_name(topic_path, strip_prefix=strip_prefix)
    result = FetchResult(topic_path=topic_path, family_id=family_id, status="fail")
    md_errors: List[str] = []

    for attempt in range(2):
        try:
            code, body, final = http_get(md_url, user_agent=user_agent)
            result.http_status_md = code
            result.final_url = final
            if code == 200 and body and body.strip().lower() not in {b"error", b""}:
                text = body.decode("utf-8", errors="replace")
                if not looks_like_markdown(text):
                    md_errors.append(f"attempt{attempt + 1}: not markdown (HTTP {code})")
                    time.sleep(0.35)
                    continue
                dest.write_text(
                    text if text.endswith("\n") else text + "\n", encoding="utf-8"
                )
                result.status = "ok_md"
                result.bytes = len(body)
                result.local_path = str(
                    dest.relative_to(root) if dest.is_relative_to(root) else dest
                )
                result.error = None
                time.sleep(sleep_s)
                return result
            md_errors.append(f"attempt{attempt + 1}: HTTP {code}")
        except Exception as e:  # noqa: BLE001
            md_errors.append(f"attempt{attempt + 1}: {e}")
        time.sleep(0.35)

    result.error = "md: " + "; ".join(md_errors)

    html_headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    }
    try:
        code, body, final = http_get(html_url, headers=html_headers)
        result.http_status_html = code
        result.final_url = final
        if code == 200 and body:
            md = html_to_markdown(body.decode("utf-8", errors="replace"), source_url=final)
            if md.count("\n") < 8 or (
                "skip to login" in md.lower() and "{#" not in md and len(md) < 2000
            ):
                result.error = (result.error or "") + "; html: chrome-only conversion"
            else:
                dest.write_text(md, encoding="utf-8")
                result.status = "ok_html_fallback"
                result.bytes = len(md.encode("utf-8"))
                result.local_path = str(
                    dest.relative_to(root) if dest.is_relative_to(root) else dest
                )
                time.sleep(sleep_s)
                return result
        else:
            result.error = (result.error or "") + f"; html HTTP {code}"
    except Exception as e:  # noqa: BLE001
        result.error = (result.error or "") + f"; html: {e}"

    time.sleep(sleep_s)
    return result


def llms_hint_urls(base_url: str, *, contains: Sequence[str], user_agent: str = DEFAULT_UA) -> List[str]:
    """llms.txt adapter — a discovery hint. Never the denominator."""
    code, body, _ = http_get(f"{base_url}/llms.txt", user_agent=user_agent)
    if code != 200:
        return []
    text = body.decode("utf-8", errors="replace")
    urls = re.findall(re.escape(base_url) + r"/[^\s\)\"]+?\.md", text)
    return sorted({u for u in urls if any(c in u for c in contains)})


def fetch_family_corpus(
    seeds: Sequence[FamilySeed],
    *,
    base_url: str,
    out_dir: Path,
    root: Path,
    strip_prefix: str = "",
    sleep_s: float = 0.08,
    limit: Optional[int] = None,
    user_agent: str = DEFAULT_UA,
) -> Dict[str, object]:
    """Fetch every topic in each family's TOC. Returns the coverage report.

    Report always carries the denominator rule and per-family
    ``denominator_source: site_html_toc`` — every number arrives with its
    denominator and its source.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    family_reports: List[FamilyReport] = []
    all_results: List[FetchResult] = []

    for fam in seeds:
        code, body, final = http_get(fam.seed_url, user_agent=user_agent)
        if code != 200:
            raise RuntimeError(f"seed fetch failed {fam.seed_url}: HTTP {code}")
        topics = extract_toc_topics(
            body.decode("utf-8", errors="replace"), base_url, fam.path_must_contain
        )
        if limit is not None:
            topics = topics[:limit]
        fr = FamilyReport(
            family_id=fam.family_id,
            label=fam.label,
            seed_url=fam.seed_url,
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
        for topic in topics:
            res = fetch_topic(
                topic,
                base_url=base_url,
                family_id=fam.family_id,
                out_dir=out_dir,
                root=root,
                strip_prefix=strip_prefix,
                sleep_s=sleep_s,
                user_agent=user_agent,
            )
            all_results.append(res)
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
        family_reports.append(fr)

    return {
        "generated_at": _utc_now(),
        "denominator_rule": (
            "Coverage denominator is the site's own HTML navigation/TOC tree "
            "for each family — not llms.txt. llms.txt is an incomplete "
            "discovery hint."
        ),
        "totals": {
            "toc_topics": sum(f.toc_topics for f in family_reports),
            "fetched_ok": sum(f.fetched_ok for f in family_reports),
            "fetched_md": sum(f.fetched_md for f in family_reports),
            "fetched_html_fallback": sum(
                f.fetched_html_fallback for f in family_reports
            ),
            "failed": sum(f.failed for f in family_reports),
            "usable": sum(f.usable for f in family_reports),
        },
        "families": [asdict(f) for f in family_reports],
        "results": [asdict(r) for r in all_results],
        "out_dir": str(out_dir),
    }


def write_report(report: Dict[str, object], report_dir: Path, *, stem: str = "toc-fetch-report") -> Path:
    report_dir.mkdir(parents=True, exist_ok=True)
    out = report_dir / f"{stem}.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return out
