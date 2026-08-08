"""Lift source markup noise into claim metadata; keep claim text readable.

Anchor ids like ``{#merchants-v2-add-merchant_step1}`` are the live site's
deep-link targets — data, not junk. Image references and source line ranges
belong in metadata too. Claim ``text`` stays clean for dedupe and reading;
``extras`` carries the anchors, images, line span, and a working deep link.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DEFAULT_DOCS_BASE = "https://developer.cybersource.com"

_ANCHOR_RE = re.compile(r"\{#([^}]+)\}")
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
# Markdown links with an empty title: [label](url "") → keep url, drop ""
_EMPTY_LINK_TITLE_RE = re.compile(r"\]\(([^)\s]+)\s+\"\"\)")
# A line that is only an anchor (duplicate of one already on the heading/step).
_ANCHOR_ONLY_LINE_RE = re.compile(r"^\s*\{#[^}]+\}\s*$")


def extract_anchors(text: str) -> List[str]:
    return _ANCHOR_RE.findall(text)


def extract_image_refs(text: str) -> List[str]:
    return _IMAGE_RE.findall(text)


def live_html_url_from_pointer(
    source_pointer: str,
    *,
    base_url: str = DEFAULT_DOCS_BASE,
) -> Optional[str]:
    """Invert the flattened local name back to a live HTML docs URL.

    ``en-us_boarding_developer_all_rest_boarding.md.md`` →
    ``https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html``
    """
    name = Path(source_pointer).name
    if name.endswith(".md.md"):
        bare = name[: -len(".md.md")]
    elif name.endswith(".md"):
        bare = name[: -len(".md")]
    else:
        bare = name
    if not bare.startswith("en-us"):
        return None
    # Path segments use hyphens, never underscores, so '_' ↔ '/' is safe.
    rel = bare.replace("_", "/")
    return f"{base_url.rstrip('/')}/docs/cybs/{rel}.html"


def deep_link_for(
    source_pointer: str,
    anchor: Optional[str],
    *,
    base_url: str = DEFAULT_DOCS_BASE,
) -> Optional[str]:
    if not anchor:
        return None
    html = live_html_url_from_pointer(source_pointer, base_url=base_url)
    if not html:
        return None
    return f"{html}#{anchor}"


def line_range_for_span(text: str, start: int, end: int) -> Tuple[int, int]:
    """1-based inclusive line numbers covering [start, end) in text."""
    line_start = text.count("\n", 0, start) + 1
    line_end = text.count("\n", 0, max(start, end - 1)) + 1
    return line_start, line_end


def clean_claim_text(text: str) -> Tuple[str, Dict[str, Any]]:
    """Remove noise from claim text; return (clean_text, metadata).

    Metadata keys: ``anchors`` (all), ``anchor`` (primary/first), ``image_refs``.
    """
    anchors = extract_anchors(text)
    images = extract_image_refs(text)

    # Drop duplicate lines that are only an anchor id.
    lines = []
    for line in text.splitlines():
        if _ANCHOR_ONLY_LINE_RE.match(line):
            continue
        lines.append(line)
    cleaned = "\n".join(lines)

    # Anchors out of the body text (kept in metadata).
    cleaned = _ANCHOR_RE.sub("", cleaned)
    # Empty link titles out of the body text.
    cleaned = _EMPTY_LINK_TITLE_RE.sub(r"](\1)", cleaned)
    # Collapse leftover whitespace around former anchors.
    cleaned = re.sub(r"[ \t]+\n", "\n", cleaned)
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)
    cleaned = cleaned.strip()

    meta: Dict[str, Any] = {}
    if anchors:
        meta["anchors"] = anchors
        meta["anchor"] = anchors[0]
    if images:
        meta["image_refs"] = images
    return cleaned, meta


def attach_source_meta(
    extras: Dict[str, Any],
    *,
    source_pointer: str,
    raw_span_text: str,
    full_text: str,
    span_start: int,
    span_end: int,
    base_url: str = DEFAULT_DOCS_BASE,
) -> Dict[str, Any]:
    """Merge noise metadata + line range + deep link into extras."""
    _, noise = clean_claim_text(raw_span_text)
    out = dict(extras)
    out.update(noise)
    line_start, line_end = line_range_for_span(full_text, span_start, span_end)
    out["line_start"] = line_start
    out["line_end"] = line_end
    anchor = out.get("anchor")
    link = deep_link_for(source_pointer, anchor, base_url=base_url)
    if link:
        out["deep_link"] = link
    return out
