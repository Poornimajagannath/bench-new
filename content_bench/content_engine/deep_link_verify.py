"""Verify markdown {#anchor} ids resolve on live HTML pages.

Before generating thousands of deep links, spot-check that HTML fragment
ids on rendered pages match markdown anchor ids.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from content_bench.content_engine.source_noise import DEFAULT_DOCS_BASE
from content_bench.content_engine.toc_fetch import http_get

DEFAULT_UA = "Content-Bench/1.0 (deep-link-verify)"

# HTML id/name attribute patterns
_ID_ATTR = re.compile(
    r"""(?:\sid=["']([^"']+)["']|\sname=["']([^"']+)["'])""",
    re.I,
)


@dataclass
class DeepLinkCheck:
    product_id: str
    root_path: str
    anchor: str
    deep_link: str
    html_url: str
    html_status: int
    anchor_found_in_html: bool
    matched_attr: Optional[str] = None


def html_url_from_root(root_path: str, *, base_url: str = DEFAULT_DOCS_BASE) -> str:
    live = root_path
    if live.endswith(".md"):
        live = live[:-3] + ".html"
    return f"{base_url.rstrip('/')}{live}"


def deep_link_url(root_path: str, anchor: str, *, base_url: str = DEFAULT_DOCS_BASE) -> str:
    return f"{html_url_from_root(root_path, base_url=base_url)}#{anchor}"


def extract_html_fragment_ids(html: str) -> set[str]:
    ids: set[str] = set()
    for m in _ID_ATTR.finditer(html):
        val = m.group(1) or m.group(2)
        if val:
            ids.add(val)
    return ids


def verify_deep_link(
    root_path: str,
    anchor: str,
    *,
    product_id: str = "",
    base_url: str = DEFAULT_DOCS_BASE,
    user_agent: str = DEFAULT_UA,
) -> DeepLinkCheck:
    html_url = html_url_from_root(root_path, base_url=base_url)
    link = deep_link_url(root_path, anchor, base_url=base_url)
    try:
        code, body, _ = http_get(
            html_url,
            user_agent=user_agent,
            headers={"User-Agent": user_agent, "Accept": "text/html,*/*"},
        )
        html = body.decode("utf-8", errors="replace") if body else ""
    except Exception:  # noqa: BLE001
        code, html = 0, ""

    frag_ids = extract_html_fragment_ids(html)
    found = anchor in frag_ids
    matched = "id" if found else None
    # Some DITA pages use prefixed section ids; check suffix match as fallback.
    if not found:
        for fid in frag_ids:
            if fid == anchor or fid.endswith(anchor) or anchor.endswith(fid):
                found = True
                matched = fid
                break

    return DeepLinkCheck(
        product_id=product_id or root_path.split("/")[-1].replace(".md", ""),
        root_path=root_path,
        anchor=anchor,
        deep_link=link,
        html_url=html_url,
        html_status=code,
        anchor_found_in_html=found,
        matched_attr=matched,
    )


def spot_check_deep_links(
    checks: Sequence[Tuple[str, str, str]],
    *,
    base_url: str = DEFAULT_DOCS_BASE,
    user_agent: str = DEFAULT_UA,
) -> List[DeepLinkCheck]:
    """Verify a list of (product_id, root_path, anchor) tuples."""
    out: List[DeepLinkCheck] = []
    for product_id, root_path, anchor in checks:
        out.append(
            verify_deep_link(
                root_path,
                anchor,
                product_id=product_id,
                base_url=base_url,
                user_agent=user_agent,
            )
        )
    return out


def spot_check_report(results: Sequence[DeepLinkCheck]) -> Dict[str, object]:
    found = sum(1 for r in results if r.anchor_found_in_html)
    return {
        "checked": len(results),
        "anchors_found": found,
        "anchors_missing": len(results) - found,
        "pass": found == len(results),
        "results": [asdict(r) for r in results],
    }
