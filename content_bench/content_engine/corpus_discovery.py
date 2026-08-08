"""Discover family-root corpus from llms.txt with docs.md cross-check.

llms.txt is the primary discovery index: each listed subtopic URL is mined
for its family root (``derive_product_root``). The deduped root set is the
corpus denominator. docs.md supplements any family roots llms.txt missed.

Unfetchable roots are split before reporting — trap two from the handoff:
a 404 on a URL we constructed is ``derivation_error`` (ours); a 500 on a
URL the site exposes is ``site_defect`` (theirs). ``empty_200`` is its own
diagnosis (valid URL, no markdown body).
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple
from urllib.parse import urlparse

from content_bench.content_engine.product_roots import (
    DEFAULT_BASE,
    DEFAULT_DOCS_MD,
    derive_product_root,
    family_from_path,
    parse_docs_md_products,
    probe_root,
    product_id_from_root,
)
from content_bench.content_engine.toc_fetch import http_get, looks_like_markdown

DEFAULT_LLMS_URL = f"{DEFAULT_BASE}/llms.txt"
DEFAULT_UA = "Content-Bench/1.0 (corpus-discovery)"

# Domains indexed in llms.txt
_LLMS_DOMAINS = (
    "https://developer.cybersource.com",
    "https://developer.visaacceptance.com",
)

# Unfetchable reason codes — never lump derivation bugs with site defects.
REASON_PDF = "pdf"
REASON_UNRESOLVED = "unresolved_derivation"
REASON_EMPTY_200 = "empty_200"
REASON_DERIVATION_ERROR = "derivation_error"  # 404 on URL we constructed — ours
REASON_DERIVATION_MISS = REASON_DERIVATION_ERROR  # alias; plan name is derivation_error
REASON_SITE_DEFECT = "site_defect"  # 500 / broken on URL the site exposes — theirs


@dataclass
class RootRecord:
    root_path: str
    product_id: str
    family: Optional[str]
    derivation: str  # family_repeat | guide_dir | already_root | ...
    source: str  # llms.txt | docs.md
    sample_urls: int = 0
    listed_as_root_in_llms: bool = False
    http_status: Optional[int] = None
    html_status: Optional[int] = None
    bytes: int = 0
    fetch_status: str = "pending"  # ok | unfetchable
    unfetchable_reason: Optional[str] = None
    unfetchable_bucket: Optional[str] = None  # ours | theirs | structural


@dataclass
class DiscoveryReport:
    generated_at: str
    llms_md_urls: int
    llms_pdf_urls: int
    roots_discovered: int
    roots_from_llms: int
    roots_from_docs_only: List[str]
    derivation_stats: Dict[str, Dict[str, int]]
    unfetchable_by_reason: Dict[str, int]
    unfetchable_by_bucket: Dict[str, int]
    roots: List[RootRecord] = field(default_factory=list)
    pdfs: List[str] = field(default_factory=list)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _url_to_path(url: str) -> str:
    for dom in _LLMS_DOMAINS:
        if url.startswith(dom):
            path = url[len(dom) :]
            return path if path.startswith("/") else "/" + path
    parsed = urlparse(url)
    return parsed.path or url


def extract_llms_urls(text: str) -> Tuple[List[str], List[str]]:
    """Return (md_urls, pdf_urls) from llms.txt body."""
    md: Set[str] = set()
    pdf: Set[str] = set()
    for dom in _LLMS_DOMAINS:
        for u in re.findall(re.escape(dom) + r"/[^\s\)\"]+?\.md", text):
            md.add(u)
        for u in re.findall(re.escape(dom) + r"/[^\s\)\"]+?\.pdf", text):
            pdf.add(u)
    return sorted(md), sorted(pdf)


def _probe_html(root_path: str, *, base_url: str, user_agent: str) -> int:
    html_path = root_path[:-3] + ".html" if root_path.endswith(".md") else root_path + ".html"
    try:
        code, body, _ = http_get(
            f"{base_url.rstrip('/')}{html_path}",
            user_agent=user_agent,
            headers={"User-Agent": user_agent, "Accept": "text/html,*/*"},
        )
        return code
    except Exception:  # noqa: BLE001
        return 0


def classify_unfetchable(
    root_path: str,
    *,
    md_status: int,
    md_bytes: int,
    html_status: Optional[int],
    listed_as_root_in_llms: bool,
    derivation: str,
) -> Tuple[str, str]:
    """Return (reason_code, bucket) where bucket is ours|theirs|structural."""
    if root_path.lower().endswith(".pdf"):
        return REASON_PDF, "structural"

    if derivation in ("unresolved", "not_md"):
        return REASON_UNRESOLVED, "ours"

    if md_status == 200 and (md_bytes == 0 or not _body_is_markdown(md_bytes, md_status)):
        # Empty or non-markdown 200 — URL may be valid, content served elsewhere.
        return REASON_EMPTY_200, "theirs" if (html_status == 200 or listed_as_root_in_llms) else "ours"

    if md_status == 500:
        return REASON_SITE_DEFECT, "theirs"

    if md_status == 404:
        if listed_as_root_in_llms:
            return REASON_SITE_DEFECT, "theirs"
        if html_status == 200:
            # HTML exists at sibling path but derived .md 404 — likely wrong derivation.
            return REASON_DERIVATION_MISS, "ours"
        return REASON_DERIVATION_MISS, "ours"

    if md_status != 200:
        if listed_as_root_in_llms or html_status == 200:
            return REASON_SITE_DEFECT, "theirs"
        return REASON_DERIVATION_MISS, "ours"

    return REASON_UNRESOLVED, "ours"


def _body_is_markdown(md_bytes: int, md_status: int) -> bool:
    return md_status == 200 and md_bytes > 100


def discover_roots_from_llms(
    llms_text: str,
    *,
    docs_text: Optional[str] = None,
) -> Tuple[Dict[str, RootRecord], List[str], List[str]]:
    """Build deduped root map from llms.txt (+ docs.md supplement).

    Returns (roots_by_path, md_urls, pdf_urls).
    """
    md_urls, pdf_urls = extract_llms_urls(llms_text)
    llms_root_paths: Set[str] = set()
    for u in md_urls:
        path = _url_to_path(u)
        if path.endswith(".md"):
            llms_root_paths.add(path)

    # Mine subtopic URLs → family roots
    root_samples: Dict[str, List[str]] = {}
    root_derivation: Dict[str, str] = {}

    for u in md_urls:
        path = _url_to_path(u)
        chosen, how, _, _ = derive_product_root(path)
        if not chosen:
            continue
        root_samples.setdefault(chosen, []).append(u)
        if chosen not in root_derivation:
            root_derivation[chosen] = how

    roots: Dict[str, RootRecord] = {}
    for root_path, samples in sorted(root_samples.items()):
        roots[root_path] = RootRecord(
            root_path=root_path,
            product_id=product_id_from_root(root_path),
            family=family_from_path(root_path),
            derivation=root_derivation.get(root_path, "unknown"),
            source="llms.txt",
            sample_urls=len(samples),
            listed_as_root_in_llms=root_path in llms_root_paths,
        )

    # docs.md cross-check — union families llms missed
    docs_only: List[str] = []
    if docs_text:
        for p in parse_docs_md_products(docs_text):
            chosen, how, _, _ = derive_product_root(p.intro_path)
            if not chosen:
                continue
            if chosen not in roots:
                docs_only.append(chosen)
                roots[chosen] = RootRecord(
                    root_path=chosen,
                    product_id=product_id_from_root(chosen),
                    family=family_from_path(chosen),
                    derivation=how,
                    source="docs.md",
                    sample_urls=1,
                    listed_as_root_in_llms=chosen in llms_root_paths,
                )
            elif roots[chosen].source == "llms.txt" and p.intro_path not in [
                _url_to_path(u) for u in md_urls
            ]:
                pass  # already covered

    return roots, md_urls, pdf_urls


def probe_roots(
    roots: Dict[str, RootRecord],
    *,
    base_url: str = DEFAULT_BASE,
    user_agent: str = DEFAULT_UA,
    sleep_s: float = 0.08,
) -> None:
    """HTTP-probe each root in place; set fetch_status and unfetchable fields."""
    for rec in roots.values():
        if rec.root_path.lower().endswith(".pdf"):
            rec.fetch_status = "unfetchable"
            rec.unfetchable_reason = REASON_PDF
            rec.unfetchable_bucket = "structural"
            continue

        md_status, md_bytes = probe_root(rec.root_path, base_url=base_url, user_agent=user_agent)
        html_status = _probe_html(rec.root_path, base_url=base_url, user_agent=user_agent)
        time.sleep(sleep_s)

        rec.http_status = md_status
        rec.html_status = html_status
        rec.bytes = md_bytes

        if md_status == 200 and md_bytes > 100:
            # Verify markdown-ish
            try:
                _, body, _ = http_get(
                    f"{base_url.rstrip('/')}{rec.root_path}",
                    user_agent=user_agent,
                )
                text = body.decode("utf-8", errors="replace")
                if looks_like_markdown(text):
                    rec.fetch_status = "ok"
                    rec.bytes = len(body)
                    time.sleep(sleep_s)
                    continue
            except Exception:  # noqa: BLE001
                pass

        reason, bucket = classify_unfetchable(
            rec.root_path,
            md_status=md_status,
            md_bytes=md_bytes,
            html_status=html_status,
            listed_as_root_in_llms=rec.listed_as_root_in_llms,
            derivation=rec.derivation,
        )
        rec.fetch_status = "unfetchable"
        rec.unfetchable_reason = reason
        rec.unfetchable_bucket = bucket
        time.sleep(sleep_s)


def _derivation_stats(roots: Sequence[RootRecord]) -> Dict[str, Dict[str, int]]:
    stats: Dict[str, Dict[str, int]] = {}
    for rec in roots:
        d = rec.derivation
        if d not in stats:
            stats[d] = {"discovered": 0, "fetched_ok": 0, "unfetchable": 0}
        stats[d]["discovered"] += 1
        if rec.fetch_status == "ok":
            stats[d]["fetched_ok"] += 1
        else:
            stats[d]["unfetchable"] += 1
    return stats


def run_discovery(
    *,
    llms_url: str = DEFAULT_LLMS_URL,
    docs_md_url: str = DEFAULT_DOCS_MD,
    base_url: str = DEFAULT_BASE,
    user_agent: str = DEFAULT_UA,
    probe: bool = True,
    sleep_s: float = 0.08,
) -> DiscoveryReport:
    code, body, _ = http_get(llms_url, user_agent=user_agent)
    if code != 200:
        raise RuntimeError(f"llms.txt fetch failed: HTTP {code}")
    llms_text = body.decode("utf-8", errors="replace")

    docs_text: Optional[str] = None
    dcode, dbody, _ = http_get(docs_md_url, user_agent=user_agent)
    if dcode == 200:
        docs_text = dbody.decode("utf-8", errors="replace")

    roots_map, md_urls, pdf_urls = discover_roots_from_llms(llms_text, docs_text=docs_text)
    docs_only = [r.root_path for r in roots_map.values() if r.source == "docs.md"]

    if probe:
        probe_roots(roots_map, base_url=base_url, user_agent=user_agent, sleep_s=sleep_s)

    roots = sorted(roots_map.values(), key=lambda r: r.root_path)
    by_reason: Dict[str, int] = {}
    by_bucket: Dict[str, int] = {}
    for r in roots:
        if r.fetch_status == "unfetchable" and r.unfetchable_reason:
            by_reason[r.unfetchable_reason] = by_reason.get(r.unfetchable_reason, 0) + 1
            if r.unfetchable_bucket:
                by_bucket[r.unfetchable_bucket] = by_bucket.get(r.unfetchable_bucket, 0) + 1

    return DiscoveryReport(
        generated_at=_utc_now(),
        llms_md_urls=len(set(md_urls)),
        llms_pdf_urls=len(pdf_urls),
        roots_discovered=len(roots),
        roots_from_llms=sum(1 for r in roots if r.source == "llms.txt"),
        roots_from_docs_only=sorted(docs_only),
        derivation_stats=_derivation_stats(roots),
        unfetchable_by_reason=by_reason,
        unfetchable_by_bucket=by_bucket,
        roots=roots,
        pdfs=pdf_urls,
    )


def discovery_to_dict(report: DiscoveryReport) -> Dict[str, object]:
    return {
        "generated_at": report.generated_at,
        "denominator_source": "llms.txt_derived_roots",
        "denominator_rule": (
            "Corpus denominator is the deduped set of family-root paths derived "
            "from llms.txt subtopic URLs (plus docs.md supplements). Unfetchable "
            "roots remain in the denominator. Unfetchable reasons split "
            "derivation_error (ours) from site_defect (theirs)."
        ),
        "llms_md_urls": report.llms_md_urls,
        "llms_pdf_urls": report.llms_pdf_urls,
        "roots_discovered": report.roots_discovered,
        "roots_from_llms": report.roots_from_llms,
        "roots_from_docs_only": report.roots_from_docs_only,
        "derivation_stats": report.derivation_stats,
        "unfetchable_by_reason": report.unfetchable_by_reason,
        "unfetchable_by_bucket": report.unfetchable_by_bucket,
        "pdfs": report.pdfs,
        "roots": [asdict(r) for r in report.roots],
    }


def write_discovery(report: DiscoveryReport, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(discovery_to_dict(report), indent=2) + "\n", encoding="utf-8")
    return path
