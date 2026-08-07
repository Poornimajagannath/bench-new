"""A3 humanizer: customer voice for prose, fact_hash guard for templated facts.

write_prose drafts Overview (and similar) sections. humanize rewrites those
sections against style/customer-voice.md. Neither path may alter the facts
block; FactHashGuardError is raised if a rewrite would.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_STYLE_PATH = ROOT / "style" / "customer-voice.md"

FACTS_OPEN = "<!-- section:facts -->"
FACTS_CLOSE = "<!-- /section:facts -->"
PROSE_OPEN = "<!-- section:prose -->"
PROSE_CLOSE = "<!-- /section:prose -->"

# Deterministic replacements implementing customer-voice.md (offline, no LLM).
_AI_VOCAB = re.compile(
    r"\b("
    r"delve(?:s|d|ing)?|tapestry|pivotal|underscores?|showcas(?:e|es|ing)|testament|"
    r"leverage(?:s|d)?|unlock(?:s|ed|ing)?|empower(?:s|ed|ing)?|"
    r"seamless(?:ly)?|robust|cutting[- ]edge|vibrant|facilitate(?:s|d)?"
    r")\b",
    re.IGNORECASE,
)
_BOILERPLATE = re.compile(
    r"(?i)\b(?:as described in the openapi(?: fixture)?|"
    r"per the (?:openapi )?fixture|"
    r"from the reference unit|"
    r"according to the (?:local )?fixture|"
    r"facts below trace to[^.]*\.)\s*"
)
_INTERNAL_JARGON = re.compile(
    r"(?i)\b(?:lineage_origin|unit_id|normalized claim|api_reference_unit|"
    r"docetl|source_mix)\b"
)
_FILLER_OPENERS = re.compile(
    r"(?i)^(in order to|it is important to note that|additionally,|"
    r"furthermore,|at its core,?|when it comes to)\s+"
)
_SERVES_AS = re.compile(r"(?i)\bserves as\b")
_STANDS_AS = re.compile(r"(?i)\bstands as\b")
_NOT_JUST = re.compile(
    r"(?i)it'?s not just ([^;.;]+);\s*it'?s ([^.]+)\."
)


class FactHashGuardError(ValueError):
    """Raised when a prose rewrite would change templated facts."""


@dataclass(frozen=True)
class FactHash:
    digest: str
    facts_body: str

    def __str__(self) -> str:
        return self.digest


def normalize_facts_body(text: str) -> str:
    """Whitespace-stable form used for hashing."""
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    # Drop trailing empty lines; keep internal structure.
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + ("\n" if lines else "")


def extract_facts_body(markdown: str) -> str:
    """Return the templated facts block, or a heuristic fallback."""
    if FACTS_OPEN in markdown and FACTS_CLOSE in markdown:
        start = markdown.index(FACTS_OPEN) + len(FACTS_OPEN)
        end = markdown.index(FACTS_CLOSE, start)
        return markdown[start:end]
    return _heuristic_facts_body(markdown)


def _heuristic_facts_body(markdown: str) -> str:
    """Fallback when generators have not yet stamped section markers."""
    lines: List[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if re.match(r"^\*\*(Method|Path|Operation ID):\*\*", stripped):
            lines.append(stripped)
            continue
        if stripped.startswith("|") and "---" not in stripped:
            lines.append(stripped)
            continue
        if stripped.startswith("## Status codes") or re.match(
            r"^`\d{3}`", stripped
        ):
            lines.append(stripped)
            continue
        if stripped.startswith("Security:"):
            lines.append(stripped)
    return "\n".join(lines) + ("\n" if lines else "")


def fact_hash(markdown: str) -> FactHash:
    body = normalize_facts_body(extract_facts_body(markdown))
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return FactHash(digest=digest, facts_body=body)


def assert_facts_unchanged(before: str, after: str) -> FactHash:
    """Hard guard: templated facts must be byte-stable under normalization."""
    left = fact_hash(before)
    right = fact_hash(after)
    if left.digest != right.digest:
        raise FactHashGuardError(
            "humanizer/write_prose changed templated facts "
            f"(before={left.digest[:12]} after={right.digest[:12]})"
        )
    return left


def load_style_guide(path: Optional[Path] = None) -> str:
    style_path = Path(path) if path is not None else DEFAULT_STYLE_PATH
    return style_path.read_text(encoding="utf-8")


def _split_marked_sections(
    markdown: str, open_tag: str, close_tag: str
) -> List[Tuple[str, Optional[str]]]:
    """Split into (literal, body_or_none) chunks preserving order."""
    parts: List[Tuple[str, Optional[str]]] = []
    cursor = 0
    while True:
        start = markdown.find(open_tag, cursor)
        if start < 0:
            parts.append((markdown[cursor:], None))
            break
        parts.append((markdown[cursor:start], None))
        body_start = start + len(open_tag)
        end = markdown.find(close_tag, body_start)
        if end < 0:
            raise ValueError(f"Unclosed {open_tag} in markdown page")
        parts.append((open_tag, markdown[body_start:end]))
        parts.append((close_tag, None))
        cursor = end + len(close_tag)
    return parts


def iter_prose_bodies(markdown: str) -> List[str]:
    return [body for tag, body in _split_marked_sections(markdown, PROSE_OPEN, PROSE_CLOSE) if body is not None]


def replace_prose_bodies(markdown: str, new_bodies: Sequence[str]) -> str:
    bodies = list(new_bodies)
    out: List[str] = []
    idx = 0
    cursor = 0
    while True:
        start = markdown.find(PROSE_OPEN, cursor)
        if start < 0:
            out.append(markdown[cursor:])
            break
        out.append(markdown[cursor:start])
        out.append(PROSE_OPEN)
        body_start = start + len(PROSE_OPEN)
        end = markdown.find(PROSE_CLOSE, body_start)
        if end < 0:
            raise ValueError("Unclosed prose section")
        if idx >= len(bodies):
            raise ValueError("Not enough replacement prose bodies")
        out.append(bodies[idx])
        idx += 1
        out.append(PROSE_CLOSE)
        cursor = end + len(PROSE_CLOSE)
    if idx != len(bodies):
        raise ValueError("Too many replacement prose bodies")
    return "".join(out)


def ensure_prose_overview(markdown: str, draft: str) -> str:
    """Insert a prose Overview section after the H1 if none exists."""
    if PROSE_OPEN in markdown:
        return markdown
    match = re.search(r"(^# .+\n)", markdown, re.MULTILINE)
    if not match:
        raise ValueError("Page has no H1; cannot insert Overview")
    insert_at = match.end()
    block = (
        f"\n{PROSE_OPEN}\n"
        f"## Overview\n\n"
        f"{draft.strip()}\n"
        f"{PROSE_CLOSE}\n"
    )
    return markdown[:insert_at] + block + markdown[insert_at:]


def draft_overview_from_page(markdown: str) -> str:
    """Deterministic prose draft. Uncertain bits become TODO, never invented facts."""
    title = ""
    method = ""
    path = ""
    m = re.search(r"^title:\s*(.+)$", markdown, re.MULTILINE)
    if m:
        title = m.group(1).strip().strip('"')
    m = re.search(r"\*\*Method:\*\*\s*`([^`]+)`", markdown)
    if m:
        method = m.group(1)
    m = re.search(r"\*\*Path:\*\*\s*`([^`]+)`", markdown)
    if m:
        path = m.group(1)

    if method and path:
        body = (
            f"Use this endpoint when you need to {title[0].lower() + title[1:] if title else 'call the API'}.\n\n"
            f"You send a `{method}` request to `{path}`.\n\n"
            "<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->"
        )
    elif "quickstart" in (title or markdown[:200]).lower():
        body = (
            "Follow these steps to finish onboarding with your platform test key.\n\n"
            "<!-- TODO: Confirm any product-specific prerequisites with the owning team. -->"
        )
    else:
        body = (
            f"{title or 'This page'} covers the integration steps below.\n\n"
            "<!-- TODO: Replace this overview with customer-facing guidance. -->"
        )
    return body


def apply_style_rules(prose: str, style_guide: str = "") -> str:
    """Rewrite one prose section. Never touches fenced code blocks' inner facts tables."""
    _ = style_guide  # loaded so guide edits are the contract; rules encoded below track it
    text = prose
    # Protect TODO comments and fenced code
    protected: List[str] = []

    def _stash(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@PROTECT{len(protected) - 1}@@"

    text = re.sub(r"<!--.*?-->", _stash, text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", _stash, text, flags=re.DOTALL)

    text = _BOILERPLATE.sub("", text)
    text = _INTERNAL_JARGON.sub("this API", text)
    text = _SERVES_AS.sub("is", text)
    text = _STANDS_AS.sub("is", text)
    text = _NOT_JUST.sub(r"\2.", text)
    text = _AI_VOCAB.sub("", text)
    # Clean artifacts left by word removal: "a and", "a .", doubled spaces/commas.
    text = re.sub(r"\b(a|an|the)\s+(and|or)\b", r"\2", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"\s+\.", ".", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    lines_out: List[str] = []
    for line in text.splitlines():
        stripped = line.lstrip()
        m = _FILLER_OPENERS.match(stripped)
        if m:
            rest = stripped[m.end() :]
            indent = line[: len(line) - len(stripped)]
            if rest:
                rest = rest[0].upper() + rest[1:]
            line = indent + rest
        line = re.sub(r"[ \t]{2,}", " ", line)
        lines_out.append(line.rstrip())
    text = "\n".join(lines_out)

    # Second person nudge for a few passive stubs
    text = re.sub(r"(?i)\bthe client (should |must )?", "you ", text)
    text = re.sub(r"(?i)\bdevelopers (should |must )?", "you ", text)

    # One idea per paragraph: split on "; " in long prose paragraphs (not lists)
    paras = re.split(r"\n\n+", text)
    rebuilt: List[str] = []
    for para in paras:
        if para.lstrip().startswith(("-", "*", "|", "#", "1.", "<!--")):
            rebuilt.append(para.strip())
            continue
        if "; " in para and not para.strip().startswith("```"):
            bits = [b.strip() for b in para.split("; ") if b.strip()]
            if len(bits) > 1:
                # Capitalize sentence starts after split
                fixed = []
                for b in bits:
                    if b and b[0].islower():
                        b = b[0].upper() + b[1:]
                    if b and b[-1] not in ".!?":
                        b += "."
                    fixed.append(b)
                rebuilt.extend(fixed)
                continue
        rebuilt.append(para.strip())
    text = "\n\n".join(p for p in rebuilt if p)

    for i, chunk in enumerate(protected):
        text = text.replace(f"@@PROTECT{i}@@", chunk)

    # Ensure leading ## Overview stays if present
    return text.strip() + "\n"


def write_prose(markdown: str) -> str:
    """Draft prose sections. Preserves fact_hash."""
    before = markdown
    draft = draft_overview_from_page(markdown)
    page = ensure_prose_overview(markdown, draft)
    # If Overview already existed, refresh only empty/placeholder bodies
    bodies = iter_prose_bodies(page)
    refreshed: List[str] = []
    for body in bodies:
        if "TODO" in body or body.strip() in {"", "## Overview"}:
            refreshed.append("## Overview\n\n" + draft_overview_from_page(page))
        else:
            refreshed.append(body if body.endswith("\n") else body + "\n")
    if bodies:
        normalized = []
        for b in refreshed:
            body = b if b.startswith("\n") else "\n" + b
            if not body.endswith("\n"):
                body += "\n"
            normalized.append(body)
        page = replace_prose_bodies(page, normalized)
    assert_facts_unchanged(before, page)
    return page


def guarded_transform(
    markdown: str, transform: Callable[[str], str]
) -> str:
    """Run any page transform; refuse output that alters templated facts."""
    out = transform(markdown)
    assert_facts_unchanged(markdown, out)
    return out


def humanize(
    markdown: str,
    *,
    style_guide: Optional[str] = None,
    style_path: Optional[Path] = None,
    rewriter: Optional[Callable[[str, str], str]] = None,
) -> str:
    """Rewrite prose sections against the style guide; refuse fact edits.

    `rewriter` is injectable for tests (default: apply_style_rules).
    """
    guide = style_guide if style_guide is not None else load_style_guide(style_path)
    rewrite = rewriter or apply_style_rules

    page = markdown
    if PROSE_OPEN not in page:
        page = write_prose(page)
        assert_facts_unchanged(markdown, page)

    def _transform(working: str) -> str:
        bodies = iter_prose_bodies(working)
        if not bodies:
            return working
        new_bodies = [rewrite(body, guide) for body in bodies]
        normalized: List[str] = []
        for b in new_bodies:
            body = b if b.startswith("\n") else "\n" + b
            if not body.endswith("\n"):
                body += "\n"
            normalized.append(body)
        return replace_prose_bodies(working, normalized)

    return guarded_transform(page, _transform)


def humanize_path(
    path: Path,
    *,
    style_path: Optional[Path] = None,
    write: bool = True,
) -> str:
    original = path.read_text(encoding="utf-8")
    updated = humanize(original, style_path=style_path)
    if write:
        path.write_text(updated, encoding="utf-8")
    return updated
