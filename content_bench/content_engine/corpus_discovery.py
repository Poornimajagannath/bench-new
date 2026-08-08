"""Discover family-root corpus from llms.txt with docs.md cross-check.

llms.txt is the primary discovery index: subtopic URLs are grouped by product
family, candidate roots are generated (family-repeat, guide-dir, bare family
path), HTTP-probed, and the best response (most {#anchor} headings, then bytes)
becomes the family root. docs.md supplements any families llms.txt missed.

Unfetchable roots are split before reporting — trap two from the handoff:
a 404 on every constructed candidate is ``derivation_error`` (ours); a 500 on a
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
    CandidateProbe,
    base_url_for_path,
    family_from_path,
    family_group_key,
    generate_root_candidates,
    parse_docs_md_products,
    pick_candidate_offline,
    probe_and_pick_root,
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
REASON_DERIVATION_MISS = REASON_DERIVATION_ERROR  # alias
REASON_SITE_DEFECT = "site_defect"  # 500 / broken on URL the site exposes — theirs
REASON_HUB_PAGE = "hub_page"  # top-level hub, not a family mega-guide
REASON_HTML_ONLY = "html_only"  # .md URL returns HTML — markdown twin missing

# Top-level paths that are hubs, not compendium guides.
_HUB_PATHS = frozenset({
    "/accept-payments.md",
    "/api/reference.md",
    "/technology-partners.md",
})


@dataclass
class RootRecord:
    root_path: str
    product_id: str
    family: Optional[str]
    family_key: str
    winning_shape: str  # family_repeat | guide_dir | bare_family | ...
    derivation: str  # alias for winning_shape (backward compat)
    source: str  # llms.txt | docs.md
    sample_urls: int = 0
    listed_as_root_in_llms: bool = False
    http_status: Optional[int] = None
    html_status: Optional[int] = None
    bytes: int = 0
    anchor_count: int = 0
    fetch_status: str = "pending"  # ok | unfetchable
    unfetchable_reason: Optional[str] = None
    unfetchable_bucket: Optional[str] = None  # ours | theirs | structural
    candidate_probes: List[dict] = field(default_factory=list)
    candidates: List[Tuple[str, str]] = field(default_factory=list)


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


def _probe_html(root_path: str, *, user_agent: str) -> int:
    html_path = root_path[:-3] + ".html" if root_path.endswith(".md") else root_path + ".html"
    base = base_url_for_path(root_path)
    try:
        code, body, _ = http_get(
            f"{base.rstrip('/')}{html_path}",
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
    body_sample: str = "",
) -> Tuple[str, str]:
    """Return (reason_code, bucket) where bucket is ours|theirs|structural."""
    if root_path.lower().endswith(".pdf"):
        return REASON_PDF, "structural"

    if root_path in _HUB_PATHS or (
        not root_path.startswith("/docs/") and root_path.count("/") <= 1
    ):
        return REASON_HUB_PAGE, "structural"

    if md_status == 500:
        return REASON_SITE_DEFECT, "theirs"

    if derivation in ("unresolved", "not_md"):
        return REASON_UNRESOLVED, "ours"

    head = body_sample.lstrip()[:400].lower()
    if md_status == 200 and (head.startswith("<!doctype") or head.startswith("<html")):
        return REASON_HTML_ONLY, "theirs"

    if md_status == 200 and (md_bytes == 0 or not looks_like_markdown(body_sample)):
        if md_bytes == 0:
            return REASON_EMPTY_200, "theirs" if listed_as_root_in_llms else "ours"
        return REASON_EMPTY_200, "theirs" if (html_status == 200 or listed_as_root_in_llms) else "ours"

    if md_status == 404:
        if listed_as_root_in_llms:
            return REASON_SITE_DEFECT, "theirs"
        if html_status == 200:
            return REASON_DERIVATION_MISS, "ours"
        return REASON_DERIVATION_MISS, "ours"

    if md_status != 200:
        if listed_as_root_in_llms or html_status == 200:
            return REASON_SITE_DEFECT, "theirs"
        return REASON_DERIVATION_MISS, "ours"

    return REASON_UNRESOLVED, "ours"


def _candidate_probes_to_dict(probes: Sequence[CandidateProbe]) -> List[dict]:
    return [
        {
            "path": p.path,
            "shape": p.shape,
            "http_status": p.http_status,
            "bytes": p.bytes,
            "anchor_count": p.anchor_count,
            "valid": p.valid,
            "discard_reason": p.discard_reason,
        }
        for p in probes
    ]


def _merge_candidates(
    urls: Sequence[str],
    llms_root_paths: Set[str],
) -> List[Tuple[str, str]]:
    seen: Set[str] = set()
    merged: List[Tuple[str, str]] = []
    for path in urls:
        for cand_path, shape in generate_root_candidates(path, listed_roots=llms_root_paths):
            if cand_path not in seen:
                seen.add(cand_path)
                merged.append((cand_path, shape))
    return merged


def discover_roots_from_llms(
    llms_text: str,
    *,
    docs_text: Optional[str] = None,
) -> Tuple[Dict[str, RootRecord], List[str], List[str]]:
    """Build deduped root map from llms.txt (+ docs.md supplement).

    Groups subtopics by family, unions candidate root URLs, and picks one root
    per family (offline priority when not yet probed).

    Returns (roots_by_path, md_urls, pdf_urls).
    """
    md_urls, pdf_urls = extract_llms_urls(llms_text)
    llms_root_paths: Set[str] = set()
    for u in md_urls:
        path = _url_to_path(u)
        if path.endswith(".md"):
            llms_root_paths.add(path)

    # Group subtopic URLs by family
    family_urls: Dict[str, List[str]] = {}
    family_source: Dict[str, str] = {}

    for u in md_urls:
        path = _url_to_path(u)
        fkey = family_group_key(path)
        family_urls.setdefault(fkey, []).append(path)
        family_source.setdefault(fkey, "llms.txt")

    # docs.md cross-check — union families llms missed
    docs_only_fkeys: Set[str] = set()
    if docs_text:
        for p in parse_docs_md_products(docs_text):
            fkey = family_group_key(p.intro_path)
            if fkey not in family_urls:
                docs_only_fkeys.add(fkey)
                family_urls[fkey] = [p.intro_path]
                family_source[fkey] = "docs.md"
            else:
                family_urls[fkey].append(p.intro_path)

    roots: Dict[str, RootRecord] = {}
    docs_only: List[str] = []
    for fkey, urls in sorted(family_urls.items()):
        candidates = _merge_candidates(urls, llms_root_paths)
        if not candidates:
            continue

        chosen, shape = pick_candidate_offline(candidates)
        if not chosen:
            continue

        listed = any(c[0] in llms_root_paths for c in candidates)
        rec = RootRecord(
            root_path=chosen,
            product_id=product_id_from_root(chosen),
            family=family_from_path(chosen) or family_from_path(urls[0]),
            family_key=fkey,
            winning_shape=shape,
            derivation=shape,
            source=family_source.get(fkey, "llms.txt"),
            sample_urls=len(urls),
            listed_as_root_in_llms=listed,
            candidates=candidates,
        )
        if fkey in docs_only_fkeys:
            docs_only.append(chosen)
        roots[chosen] = rec

    return roots, md_urls, pdf_urls, sorted(docs_only)


def probe_roots(
    roots: Dict[str, RootRecord],
    *,
    base_url: str = DEFAULT_BASE,
    user_agent: str = DEFAULT_UA,
    sleep_s: float = 0.08,
    only_product_ids: Optional[Set[str]] = None,
) -> None:
    """HTTP-probe candidate roots per family; pick best by anchors then bytes."""
    # Re-key by family_key so probe-and-pick runs once per family
    by_family: Dict[str, RootRecord] = {}
    for rec in roots.values():
        prev = by_family.get(rec.family_key)
        if prev is None or len(rec.candidates) > len(prev.candidates):
            by_family[rec.family_key] = rec

    for rec in by_family.values():
        if only_product_ids and rec.product_id not in only_product_ids:
            rec.fetch_status = "skipped"
            continue

        if rec.root_path.lower().endswith(".pdf"):
            rec.fetch_status = "unfetchable"
            rec.unfetchable_reason = REASON_PDF
            rec.unfetchable_bucket = "structural"
            continue

        if not rec.candidates:
            rec.fetch_status = "unfetchable"
            rec.unfetchable_reason = REASON_UNRESOLVED
            rec.unfetchable_bucket = "ours"
            continue

        chosen, shape, probes = probe_and_pick_root(
            rec.candidates,
            base_url=base_url_for_path(rec.candidates[0][0]),
            user_agent=user_agent,
            sleep_s=sleep_s,
        )
        rec.candidate_probes = _candidate_probes_to_dict(probes)
        rec.winning_shape = shape
        rec.derivation = shape

        if chosen:
            old_key = rec.root_path
            rec.root_path = chosen
            rec.product_id = product_id_from_root(chosen)
            if old_key != chosen and old_key in roots:
                del roots[old_key]
            roots[chosen] = rec

            winning = next((p for p in probes if p.path == chosen), None)
            if winning and winning.valid:
                rec.http_status = winning.http_status
                rec.bytes = winning.bytes
                rec.anchor_count = winning.anchor_count
                rec.fetch_status = "ok"
                rec.html_status = _probe_html(chosen, user_agent=user_agent)
                time.sleep(sleep_s)
                continue

        # No valid candidate — classify from probe attempts
        statuses = [p.http_status for p in probes]
        rec.http_status = 500 if 500 in statuses else (probes[0].http_status if probes else 0)
        rec.bytes = max((p.bytes for p in probes), default=0)
        rec.html_status = _probe_html(rec.root_path, user_agent=user_agent) if rec.root_path else 0
        time.sleep(sleep_s)

        body_text = ""
        if rec.http_status == 200 and rec.bytes > 0:
            try:
                base = base_url_for_path(rec.root_path)
                _, body, _ = http_get(
                    f"{base.rstrip('/')}{rec.root_path}",
                    user_agent=user_agent,
                )
                body_text = body.decode("utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                pass

        reason, bucket = classify_unfetchable(
            rec.root_path,
            md_status=rec.http_status or 0,
            md_bytes=rec.bytes,
            html_status=rec.html_status,
            listed_as_root_in_llms=rec.listed_as_root_in_llms,
            derivation=rec.winning_shape,
            body_sample=body_text,
        )
        rec.fetch_status = "unfetchable"
        rec.unfetchable_reason = reason
        rec.unfetchable_bucket = bucket
        time.sleep(sleep_s)


def _derivation_stats(roots: Sequence[RootRecord]) -> Dict[str, Dict[str, int]]:
    stats: Dict[str, Dict[str, int]] = {}
    for rec in roots:
        d = rec.winning_shape or rec.derivation
        if d not in stats:
            stats[d] = {"discovered": 0, "fetched_ok": 0, "unfetchable": 0}
        stats[d]["discovered"] += 1
        if rec.fetch_status == "ok":
            stats[d]["fetched_ok"] += 1
        elif rec.fetch_status == "unfetchable":
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
    only_product_ids: Optional[Set[str]] = None,
) -> DiscoveryReport:
    code, body, _ = http_get(llms_url, user_agent=user_agent)
    if code != 200:
        raise RuntimeError(f"llms.txt fetch failed: HTTP {code}")
    llms_text = body.decode("utf-8", errors="replace")

    docs_text: Optional[str] = None
    dcode, dbody, _ = http_get(docs_md_url, user_agent=user_agent)
    if dcode == 200:
        docs_text = dbody.decode("utf-8", errors="replace")

    roots_map, md_urls, pdf_urls, docs_only = discover_roots_from_llms(llms_text, docs_text=docs_text)

    if probe:
        probe_roots(
            roots_map,
            base_url=base_url,
            user_agent=user_agent,
            sleep_s=sleep_s,
            only_product_ids=only_product_ids,
        )

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
            "Corpus denominator is the deduped set of family-root paths chosen "
            "by probe-and-pick over candidate URLs (family-repeat, guide-dir, "
            "bare family path) per llms.txt family (+ docs.md supplements). "
            "Unfetchable roots remain in the denominator. Unfetchable reasons "
            "split derivation_error (ours) from site_defect (theirs)."
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
