"""Sanitize product-root mega-guides: lift anchors, split sections, quarantine.

Code blocks are scanned from raw section bytes — never from cleaned body —
so fence content stays byte-exact.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from content_bench.content_engine.product_roots import (
    DEFAULT_BASE,
    Section,
    split_root_sections,
)
from content_bench.content_engine.source_noise import (
    _ANCHOR_ONLY_LINE_RE,
    _ANCHOR_RE,
    _EMPTY_LINK_TITLE_RE,
    _IMAGE_RE,
    clean_claim_text,
    extract_anchors,
    extract_image_refs,
)
from content_bench.content_engine.triage import has_constraint_signals, link_density

QUARANTINE_KINDS = (
    "revision_history",
    "about_guide_boilerplate",
    "support_center",
    "navigation_list",
)

_REVISION_RE = re.compile(
    r"(?i)(recent revisions|doc-revisions|revision history|document history)"
)
_ABOUT_GUIDE_RE = re.compile(
    r"(?i)(about this guide|audience|conventions|document conventions|"
    r"who should read|typographical conventions)"
)
_SUPPORT_CENTER_RE = re.compile(r"(?i)support center")

# Fenced code block: language tag optional
_CODE_FENCE = re.compile(
    r"(?ms)^```([^\n]*)\n(.*?)^```\s*$",
    re.MULTILINE,
)


@dataclass
class CodeBlockRecord:
    language: str
    raw_bytes: str
    byte_start: int
    byte_end: int
    nearest_anchor: str


@dataclass
class CleanSection:
    anchor: str
    title: str
    parent_product: str
    root_path: str
    deep_link: str
    byte_start: int
    byte_end: int
    anchors_lifted: List[str]
    image_refs_removed: List[str]
    body: str
    quarantined: bool = False
    quarantine_kind: Optional[str] = None
    quarantine_reason: Optional[str] = None


@dataclass
class SanitizeProductReport:
    product_id: str
    root_path: str
    bytes_in: int
    sections_total: int
    sections_clean: int
    sections_quarantined: int
    quarantined_by_kind: Dict[str, int]
    code_blocks: int


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def classify_section_quarantine(
    title: str,
    anchor: str,
    body: str,
) -> Tuple[Optional[str], Optional[str]]:
    """Return (kind, reason) or (None, None) if section stays in cleaned corpus."""
    title_anchor = f"{title} {anchor}"
    if _REVISION_RE.search(title_anchor):
        return "revision_history", "revision/changelog section"
    if _ABOUT_GUIDE_RE.search(title_anchor) or _ABOUT_GUIDE_RE.search(body[:1200]):
        return "about_guide_boilerplate", "about-guide or audience/conventions boilerplate"
    if _SUPPORT_CENTER_RE.search(body) and not has_constraint_signals(body):
        return "support_center", "support-center block without procedural content"
    if link_density(body) > 0.55 and not has_constraint_signals(body) and len(body) < 4000:
        return "navigation_list", "pure navigation / link list"
    return None, None


def sanitize_section_body(raw_section: str) -> Tuple[str, List[str], List[str]]:
    """Lift anchors and strip noise from section body."""
    anchors = extract_anchors(raw_section)
    images = extract_image_refs(raw_section)
    cleaned, _ = clean_claim_text(raw_section)
    return cleaned, anchors, images


def extract_code_blocks(
    raw_text: str,
    *,
    section_anchor: str,
    file_byte_offset: int = 0,
) -> List[CodeBlockRecord]:
    """Scan raw bytes for fenced blocks; tag with nearest section anchor."""
    blocks: List[CodeBlockRecord] = []
    for m in _CODE_FENCE.finditer(raw_text):
        lang = (m.group(1) or "").strip()
        content = m.group(2)
        # Preserve exact fence inner bytes (exclude surrounding ``` lines)
        inner_start = m.start(2)
        inner_end = m.end(2)
        blocks.append(
            CodeBlockRecord(
                language=lang,
                raw_bytes=content,
                byte_start=file_byte_offset + inner_start,
                byte_end=file_byte_offset + inner_end,
                nearest_anchor=section_anchor,
            )
        )
    return blocks


def sanitize_root(
    text: str,
    *,
    root_path: str,
    product_id: str,
    base_url: str = DEFAULT_BASE,
) -> Tuple[List[CleanSection], List[CodeBlockRecord], SanitizeProductReport]:
    raw_bytes = text.encode("utf-8")
    sections_meta = split_root_sections(text, root_path=root_path, base_url=base_url)
    clean_sections: List[CleanSection] = []
    all_blocks: List[CodeBlockRecord] = []
    quarantined_by_kind: Dict[str, int] = {}

    if not sections_meta:
        # Single-document fallback: treat whole file as one section
        sections_meta = [
            Section(
                anchor="root",
                title=product_id,
                byte_start=0,
                byte_end=len(raw_bytes),
                deep_link=f"{base_url.rstrip('/')}{root_path.replace('.md', '.html')}",
                heading_level=1,
            )
        ]

    for sec in sections_meta:
        raw_section = text[sec.byte_start : sec.byte_end] if sec.byte_end <= len(text) else text[sec.byte_start:]
        body, anchors_lifted, images = sanitize_section_body(raw_section)
        q_kind, q_reason = classify_section_quarantine(sec.title, sec.anchor, raw_section)

        blocks = extract_code_blocks(
            raw_section,
            section_anchor=sec.anchor,
            file_byte_offset=sec.byte_start,
        )
        all_blocks.extend(blocks)

        rec = CleanSection(
            anchor=sec.anchor,
            title=sec.title,
            parent_product=product_id,
            root_path=root_path,
            deep_link=sec.deep_link,
            byte_start=sec.byte_start,
            byte_end=sec.byte_end,
            anchors_lifted=anchors_lifted,
            image_refs_removed=images,
            body=body,
            quarantined=q_kind is not None,
            quarantine_kind=q_kind,
            quarantine_reason=q_reason,
        )
        clean_sections.append(rec)
        if q_kind:
            quarantined_by_kind[q_kind] = quarantined_by_kind.get(q_kind, 0) + 1

    n_quar = sum(1 for s in clean_sections if s.quarantined)
    report = SanitizeProductReport(
        product_id=product_id,
        root_path=root_path,
        bytes_in=len(raw_bytes),
        sections_total=len(clean_sections),
        sections_clean=len(clean_sections) - n_quar,
        sections_quarantined=n_quar,
        quarantined_by_kind=quarantined_by_kind,
        code_blocks=len(all_blocks),
    )
    return clean_sections, all_blocks, report


def write_sanitized_product(
    sections: Sequence[CleanSection],
    blocks: Sequence[CodeBlockRecord],
    report: SanitizeProductReport,
    *,
    cleaned_dir: Path,
    quarantine_dir: Path,
) -> None:
    prod_clean = cleaned_dir / report.product_id
    prod_quar = quarantine_dir / report.product_id
    prod_clean.mkdir(parents=True, exist_ok=True)

    manifest_sections: List[Dict[str, Any]] = []
    for sec in sections:
        entry = {
            "anchor": sec.anchor,
            "title": sec.title,
            "deep_link": sec.deep_link,
            "byte_start": sec.byte_start,
            "byte_end": sec.byte_end,
            "anchors_lifted": sec.anchors_lifted,
            "image_refs_removed": sec.image_refs_removed,
            "quarantined": sec.quarantined,
        }
        if sec.quarantined:
            entry["quarantine_kind"] = sec.quarantine_kind
            entry["quarantine_reason"] = sec.quarantine_reason
            prod_quar.mkdir(parents=True, exist_ok=True)
            qpath = prod_quar / f"{sec.anchor}.json"
            qpath.write_text(
                json.dumps({**entry, "body": sec.body}, indent=2) + "\n",
                encoding="utf-8",
            )
        else:
            spath = prod_clean / "sections" / f"{sec.anchor}.md"
            spath.parent.mkdir(parents=True, exist_ok=True)
            spath.write_text(sec.body + "\n" if sec.body and not sec.body.endswith("\n") else sec.body, encoding="utf-8")
        manifest_sections.append(entry)

    blocks_path = prod_clean / "code_blocks.json"
    blocks_path.write_text(
        json.dumps([asdict(b) for b in blocks], indent=2) + "\n",
        encoding="utf-8",
    )
    manifest = {
        "generated_at": _utc_now(),
        "product_id": report.product_id,
        "root_path": report.root_path,
        "bytes_in": report.bytes_in,
        "sections_total": report.sections_total,
        "sections_clean": report.sections_clean,
        "sections_quarantined": report.sections_quarantined,
        "quarantined_by_kind": report.quarantined_by_kind,
        "code_blocks": report.code_blocks,
        "sections": manifest_sections,
    }
    (prod_clean / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def validate_clean_body(body: str) -> List[str]:
    """Return list of validation errors (empty = pass)."""
    errors: List[str] = []
    if _ANCHOR_RE.search(body):
        errors.append("raw brace anchor in cleaned body")
    if _EMPTY_LINK_TITLE_RE.search(body):
        errors.append("empty link title in cleaned body")
    return errors


def validate_all_sections(sections: Sequence[CleanSection]) -> Dict[str, List[str]]:
    """Validate non-quarantined sections; return {anchor: [errors]}."""
    failures: Dict[str, List[str]] = {}
    for sec in sections:
        if sec.quarantined:
            continue
        errs = validate_clean_body(sec.body)
        if errs:
            failures[sec.anchor] = errs
    return failures
