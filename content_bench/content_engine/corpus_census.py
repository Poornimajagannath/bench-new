"""Corpus census: classify downloaded docs by kind before ingestion.

Kinds are a decision surface — counts + quarantine list — not a silent filter.
Engine module: heuristics are generic; quarantine policy is repo config.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

DOC_KINDS = (
    "api_reference",
    "how_to_guide",
    "release_note",
    "index_navigation",
    "legal",
    "marketing",
    "other",
)

KIND_LABELS = {
    "api_reference": "API reference",
    "how_to_guide": "How-to guide",
    "release_note": "Release note",
    "index_navigation": "Index / navigation",
    "legal": "Legal",
    "marketing": "Marketing",
    "other": "Other / unclassified",
}

# Default policy kinds excluded from ingestion (overridable via policy JSON).
DEFAULT_QUARANTINE_KINDS = ("release_note", "legal", "index_navigation")

_MD_SUFFIXES = {".md", ".markdown", ".txt"}


@dataclass
class Classification:
    path: str
    kind: str
    confidence: str
    reasons: List[str] = field(default_factory=list)
    bytes: int = 0
    title: str = ""
    quarantined: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_doc(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name.endswith(".meta.json"):
        return False
    if path.name.startswith("."):
        return False
    name = path.name.lower()
    # CyberSource downloads often use `.md.md`
    if name.endswith(".md") or name.endswith(".markdown") or name.endswith(".txt"):
        return True
    return path.suffix.lower() in _MD_SUFFIXES


def _read_head(path: Path, limit: int = 6000) -> str:
    try:
        data = path.read_bytes()[:limit]
    except OSError:
        return ""
    return data.decode("utf-8", errors="replace")


def _read_sample(path: Path, *, head: int = 8000, mid: int = 4000) -> str:
    """Head + a mid-file window so large guide shells still show procedures."""
    try:
        raw = path.read_bytes()
    except OSError:
        return ""
    chunks = [raw[:head]]
    if len(raw) > head + mid:
        center = max(len(raw) // 3, head)
        chunks.append(raw[center : center + mid])
    return b"\n".join(chunks).decode("utf-8", errors="replace")


def _title_from_text(text: str) -> str:
    for line in text.splitlines():
        s = line.strip().lstrip("#").strip()
        if not s or s.lower() in {"icon", "on this page", "markdown"}:
            continue
        # Strip trailing DITA-ish anchors
        s = re.sub(r"\s*\{#[^}]+\}\s*$", "", s).strip()
        if s:
            return s[:160]
    return ""


# Shared triage heuristics live in triage.py — the one definition used by both
# census and ingest. Do not re-implement locally.
from content_bench.content_engine.triage import (  # noqa: E402
    has_constraint_signals as _has_constraint_signals,
    link_density as _link_density,
)


def classify_document(
    path: Path,
    *,
    root: Optional[Path] = None,
    text: Optional[str] = None,
) -> Classification:
    """Classify one doc using filename + content heuristics."""
    rel = str(path.relative_to(root)) if root else str(path)
    name = path.name.lower()
    stem = path.stem.lower()
    size = path.stat().st_size if path.is_file() else 0
    body = text if text is not None else (
        _read_sample(path) if size >= 20_000 else _read_head(path)
    )
    if text is not None and size == 0:
        size = len(text.encode("utf-8", errors="replace"))
    head = body[:4000]
    head_l = head.lower()
    title = _title_from_text(head)
    reasons: List[str] = []

    def hit(kind: str, reason: str, confidence: str = "high") -> Classification:
        reasons.append(reason)
        return Classification(
            path=rel,
            kind=kind,
            confidence=confidence,
            reasons=list(reasons),
            bytes=size,
            title=title,
        )

    # --- release note (filename first; policy-sensitive) ---
    if re.search(
        r"(relnote|release[-_]?notes?|doc-rel|_rn-\d{4}|/rn-\d{4})",
        name,
    ) or re.search(r"\brelease[- ]notes?\b", stem):
        return hit("release_note", "filename matches release-note pattern")
    if re.search(
        r"(?m)^(#+)?\s*(release notes|what'?s new|document release notes)\b",
        head,
        re.I,
    ) and size < 50_000:
        return hit("release_note", "heading indicates release notes", "medium")

    # --- legal ---
    if re.search(
        r"(privacy|terms[-_]?of[-_]?use|terms[-_]?of[-_]?service|cookie|legal[-_]|"
        r"gdpr|license-agreement|copyright-notice)",
        name,
    ):
        return hit("legal", "filename matches legal pattern")
    if re.search(
        r"(?m)^(#+)?\s*(privacy policy|terms of (use|service)|cookie policy|"
        r"legal notice|copyright)\b",
        head,
        re.I,
    ):
        return hit("legal", "heading indicates legal page", "medium")

    # --- marketing ---
    if re.search(r"(home-merch|why[-_]?choose|benefits|marketing|promo)", name):
        return hit("marketing", "filename matches marketing pattern", "medium")
    if re.search(
        r"\b(transform your|grow your business|why (merchants|customers) choose)\b",
        head_l,
    ) and not re.search(r"\b(api|request|endpoint|http)\b", head_l):
        return hit("marketing", "promotional prose without API surface", "low")

    # --- index / navigation ---
    # CyberSource tree names almost always contain `developer`; do not use that
    # token as a how-to signal. Prefer -intro / overview shells as index unless
    # the body clearly teaches a procedure.
    index_name = bool(
        re.search(
            r"(-intro(?:-|$|\.)|_intro(?:-|$|\.)|home-merch|jumplink|"
            r"about-guide|overview(?:-intro)?(?:-|$|\.)|"
            r"getting-started-intro)",
            name,
        )
    )
    procedural = bool(
        re.search(
            r"(?i)\b(follow these steps|before you begin|step\s*1\b|"
            r"request field|reply field|"
            r"(post|get|put|patch|delete)\s+/[a-z0-9_{}/-]+)\b",
            body,
        )
    )
    # Constraint facts (TTL, PCI, headers, reuse) count as substantive content.
    # Length alone is not emptiness — short constraint pages must stay eligible.
    constraint_rich = _has_constraint_signals(body)
    substantive = procedural or constraint_rich
    link_d = _link_density(head)
    mostly_nav = (
        size < 4000
        and not constraint_rich
        and (
            link_d >= 0.035
            or "on this page" in head_l
            or "{#jumplink-list}" in head_l
            or re.search(r"\bsee these topics\b", head_l)
            or re.search(r"\brelated documentation\b", head_l)
            or re.search(r"\bto understand .{0,40}see these topics\b", head_l)
        )
    )
    intro_stub = (
        size < 3500
        and bool(re.search(r"\bintroduction to\b", head_l))
        and not substantive
    )
    revision_only = bool(
        re.search(r"recent revisions to this document", head_l)
    ) and size < 4000 and not substantive
    if index_name and not substantive and (mostly_nav or size < 3500 or intro_stub):
        return hit(
            "index_navigation",
            "filename looks like intro/index and content is navigation-heavy",
            "high" if mostly_nav or size < 800 else "medium",
        )
    if (mostly_nav or intro_stub) and not substantive:
        return hit(
            "index_navigation",
            "short page dominated by links / jumplist",
            "medium",
        )
    if revision_only and not re.search(r"_reference_", name):
        return hit(
            "index_navigation",
            "revision/history shell without procedural content",
            "low",
        )

    # --- API reference ---
    if re.search(r"(_reference_|api-fields|field-reference|-ref-intro|codes[-_])", name):
        # *-ref-intro without procedure already handled above; catalogs stay here
        if not (index_name and not substantive and size < 3500):
            return hit("api_reference", "filename matches API reference pattern")
    if re.search(
        r"(?i)\b(rest api field reference|api field reference|request and reply fields|"
        r"field reference)\b",
        head,
    ):
        return hit("api_reference", "heading/body indicates field reference", "medium")
    if re.search(r"(?i)\b(status codes?|error codes?|avs codes?)\b", title) and size > 2000:
        return hit("api_reference", "title is a codes/reference catalog", "medium")

    # --- how-to guide ---
    # Note: do not match bare `developer` — it appears in nearly every CS path.
    if re.search(
        r"(getting[-_]?started|integration|req-task|[-_]task(?:-|$|\.)|"
        r"how[-_]?to|quickstart|walkthrough|tutorial)",
        name,
    ):
        return hit("how_to_guide", "filename matches how-to / task guide", "medium")
    if procedural or re.search(
        r"(?i)\b(to (create|request|send|configure)\b|developer guide)\b",
        body,
    ):
        return hit("how_to_guide", "procedural how-to signals in content", "medium")
    if constraint_rich:
        return hit(
            "how_to_guide",
            "constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length",
            "medium",
        )
    if re.search(
        r"(?i)\bthis (section|guide) (describes|is for|explains|provides)\b",
        head,
    ) and size >= 8_000:
        return hit(
            "how_to_guide",
            "long-form product guide shell with audience/purpose framing",
            "medium",
        )
    if re.search(r"(?i)\b(post|get|put|patch|delete)\s+/[a-z0-9_{}/-]+", body) and size > 1500:
        return hit("how_to_guide", "contains HTTP API call patterns", "low")

    # Tiny stubs are navigation placeholders, not ingestible guides.
    # Constraint-rich short pages are not stubs (length is not emptiness).
    if size < 400 and not substantive:
        return hit(
            "index_navigation",
            "tiny stub without procedural content",
            "medium",
        )

    return hit("other", "no strong filename/content signal", "low")


def load_quarantine_policy(path: Optional[Path]) -> Dict[str, Any]:
    if path is None or not path.is_file():
        return {
            "version": 1,
            "exclude_kinds": list(DEFAULT_QUARANTINE_KINDS),
            "notes": "Default engine policy when no policy file is present.",
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    kinds = data.get("exclude_kinds") or list(DEFAULT_QUARANTINE_KINDS)
    data["exclude_kinds"] = list(kinds)
    return data


def run_corpus_census(
    docs_dir: Path,
    *,
    policy_path: Optional[Path] = None,
    policy: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    docs_dir = Path(docs_dir)
    if not docs_dir.is_dir():
        raise FileNotFoundError(f"docs_dir not found: {docs_dir}")

    pol = policy if policy is not None else load_quarantine_policy(policy_path)
    exclude = set(pol.get("exclude_kinds") or DEFAULT_QUARANTINE_KINDS)

    classifications: List[Classification] = []
    for path in sorted(docs_dir.rglob("*")):
        if not _is_doc(path):
            continue
        # Skip nested noise
        if any(part.startswith(".") for part in path.parts):
            continue
        c = classify_document(path, root=docs_dir)
        c.quarantined = c.kind in exclude
        classifications.append(c)

    counts = Counter(c.kind for c in classifications)
    quarantine = [c for c in classifications if c.quarantined]
    eligible = [c for c in classifications if not c.quarantined]

    return {
        "generated_at": _utc_now(),
        "docs_dir": str(docs_dir),
        "doc_count": len(classifications),
        "counts_by_kind": {k: counts.get(k, 0) for k in DOC_KINDS},
        "quarantine_policy": {
            "exclude_kinds": sorted(exclude),
            "policy_path": str(policy_path) if policy_path else None,
            "notes": pol.get("notes") or pol.get("rationale") or "",
        },
        "quarantine_count": len(quarantine),
        "eligible_count": len(eligible),
        "classifications": [c.to_dict() for c in classifications],
        "quarantine_list": [c.to_dict() for c in quarantine],
    }


def render_census_markdown(result: Dict[str, Any]) -> str:
    counts = result["counts_by_kind"]
    total = result["doc_count"] or 1
    lines = [
        "# Corpus census",
        "",
        f"- When: `{result['generated_at']}`",
        f"- Corpus: `{result['docs_dir']}`",
        f"- Documents classified: **{result['doc_count']}**",
        f"- Eligible for ingestion: **{result['eligible_count']}**",
        f"- Quarantined (policy): **{result['quarantine_count']}**",
        "",
        "## Counts by kind",
        "",
        "| Kind | Count | Share | Quarantined by policy? |",
        "| --- | ---: | ---: | --- |",
    ]
    exclude = set(result["quarantine_policy"]["exclude_kinds"])
    for kind in DOC_KINDS:
        n = int(counts.get(kind, 0))
        share = f"{(n / total):.1%}"
        q = "yes" if kind in exclude else "no"
        lines.append(f"| {KIND_LABELS[kind]} (`{kind}`) | {n} | {share} | {q} |")

    lines.extend(
        [
            "",
            "## Policy (exclusions on paper)",
            "",
            "Kinds excluded from ingestion by policy:",
            "",
        ]
    )
    for kind in result["quarantine_policy"]["exclude_kinds"]:
        lines.append(f"- `{kind}` — {KIND_LABELS.get(kind, kind)}")
    notes = (result["quarantine_policy"].get("notes") or "").strip()
    if notes:
        lines.extend(["", f"_Rationale:_ {notes}"])

    lines.extend(
        [
            "",
            "## Sample classifications (first 25)",
            "",
            "| Path | Kind | Confidence | Reasons |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["classifications"][:25]:
        reasons = "; ".join(row.get("reasons") or [])
        lines.append(
            f"| `{row['path']}` | {row['kind']} | {row['confidence']} | {reasons} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_quarantine_markdown(result: Dict[str, Any]) -> str:
    lines = [
        "# Quarantine list — excluded from ingestion by policy",
        "",
        f"- When: `{result['generated_at']}`",
        f"- Corpus: `{result['docs_dir']}`",
        f"- Excluded kinds: {', '.join(f'`{k}`' for k in result['quarantine_policy']['exclude_kinds'])}",
        f"- Quarantined docs: **{result['quarantine_count']}** of {result['doc_count']}",
        "",
        "This list is the decision record. Ingestion must not pull these paths",
        "unless policy is amended and the census re-run.",
        "",
        "| # | Kind | Path | Title | Reasons |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for i, row in enumerate(result["quarantine_list"], 1):
        title = (row.get("title") or "").replace("|", "\\|")
        reasons = "; ".join(row.get("reasons") or []).replace("|", "\\|")
        lines.append(
            f"| {i} | `{row['kind']}` | `{row['path']}` | {title} | {reasons} |"
        )
    lines.append("")
    return "\n".join(lines)


def quarantine_path_set(result: Dict[str, Any]) -> set[str]:
    """Basenames + relative paths for ingest skip matching."""
    out: set[str] = set()
    for row in result.get("quarantine_list") or []:
        p = row["path"]
        out.add(p)
        out.add(Path(p).name)
    return out
