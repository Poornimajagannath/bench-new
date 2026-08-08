"""Document triage — the one definition of constraint page, shell, and heading.

Deep module: census (pre-ingest classification/quarantine) and ingest
(claim extraction / drop triage) both call this interface. They must never
re-implement these heuristics locally — census and ingest disagreeing on
whether a short constraint page is a shell is exactly how the transient-token
TTL fact vanished from Wave 1.

Interface:
    constraint_kind(sentence)      -> Optional[str]   # per-sentence detector
    has_constraint_signals(text)   -> bool            # page-level detector
    iter_sentences(text)           -> List[str]
    first_heading(text)            -> str
    link_density(text)             -> float
    looks_like_shell(text, bytes)  -> bool

Constraint pages (TTLs, validity windows, rate/reuse limits, PCI/compliance
statements, mandatory headers, device/E2E encryption) are the class that keeps
getting lost — and exactly what an integrating developer needs. Length is not
a signal of emptiness.
"""

from __future__ import annotations

import re
from typing import List, Optional

# --- Constraint-page detector (explicit, single source of truth) -----------

# Page-level signals: any of these makes a page substantive regardless of size.
CONSTRAINT_PAGE_PATTERN = re.compile(
    r"(?i)\b("
    r"\d+\s*-?\s*(?:minute|minutes|hour|hours|second|seconds|day|days)\b|"
    r"\bTTL\b|time[- ]to[- ]live|"
    r"valid(?:ity)?\s+(?:for|until|window)|expires?\s+(?:in|after|within)\b|"
    r"limited[- ]use|reuse|multiple times|rate[- ]limit|once only|"
    r"\bPCI\b|\bSAQ\b|PCI DSS|compliance|"
    r"requires?\s+header|header information|mandatory header|"
    r"encrypt(?:ed|ion)? on (?:the )?(?:customer'?s )?device|"
    r"device[- ]side encryption|end-to-end encryption"
    r")"
)

_TTL_PATTERN = re.compile(
    r"\b\d+\s*-?\s*(minute|hour|second|day)s?\b|\bttl\b|time[- ]to[- ]live|"
    r"valid(?:ity)?\s+(?:for|until|window)|expires?\s+(?:in|after|within)\b"
)
_REUSE_PATTERN = re.compile(
    r"reuse|multiple times|rate[- ]limit|once only|limited-use|limited use"
)
_PCI_PATTERN = re.compile(r"\bpci\b|\bsaq\b|compliance")
_HEADER_PATTERN = re.compile(
    r"header information|requires? header|mandatory header"
)
_ENCRYPTION_PATTERN = re.compile(
    r"encrypt(?:ed|ion)? on .{0,40}device|device-side encryption|"
    r"end-to-end encryption"
)

# Boarding's own constraint classes — organization/ID format rules, hierarchy
# limits, status transitions, and prerequisites. Same loss class as TTLs:
# facts an integrating partner gets wrong without docs.
_ID_FORMAT_PATTERN = re.compile(
    r"\b(id|identifier)s?\b[^.]{0,80}\bmust be\b|"
    r"\bmust be unique\b|"
    r"\b(?:from\s+)?\d+\s*to\s*\d+\s*(?:alphanumeric\s+)?characters\b"
)
_HIERARCHY_PATTERN = re.compile(
    r"only\s+(?:be\s+)?one\b[^.]{0,60}\b(?:branch|hierarchy)\b|"
    r"levels? of (?:the )?hierarchy|"
    r"\bhierarchy\b[^.]{0,60}\b(?:cannot|must|only)\b"
)
_STATUS_TRANSITION_PATTERN = re.compile(
    r"\bstatus\b[^.]{0,60}\b(?:can only|cannot|must be|transition)\b|"
    r"\b(?:can only|cannot) (?:be )?(?:change|revert|move)\w*[^.]{0,40}\bstatus\b"
)
_PREREQUISITE_PATTERN = re.compile(
    r"\bprerequisite\b|\bmust have\b|\byou must include\b|"
    r"\brequires that\b|\bmust be in the format\b|"
    # Soft-gap shapes from still-dropped intros (C3 sibling triage):
    # "Before you can…", "must contact …", "This implementation requires…"
    r"\bbefore you can\b|"
    r"\bmust contact\b|"
    r"\bthis implementation requires\b|"
    r"\brequires the use of\b|"
    r"\bnotify your account representative\b"
)


def constraint_kind(sentence: str) -> Optional[str]:
    """Classify one sentence's constraint type, or None.

    Kinds: ttl_and_reuse, ttl_or_validity, reuse_or_rate_limit,
    pci_compliance, mandatory_header, device_encryption, constraint.
    """
    s = sentence.lower()
    ttl = bool(_TTL_PATTERN.search(s))
    reuse = bool(_REUSE_PATTERN.search(s))
    if ttl and reuse:
        return "ttl_and_reuse"
    if ttl:
        return "ttl_or_validity"
    if reuse:
        return "reuse_or_rate_limit"
    if _PCI_PATTERN.search(s):
        return "pci_compliance"
    if _HEADER_PATTERN.search(s):
        return "mandatory_header"
    if _ENCRYPTION_PATTERN.search(s):
        return "device_encryption"
    if _ID_FORMAT_PATTERN.search(s):
        return "id_format_rule"
    if _HIERARCHY_PATTERN.search(s):
        return "hierarchy_limit"
    if _STATUS_TRANSITION_PATTERN.search(s):
        return "status_transition"
    if _PREREQUISITE_PATTERN.search(s):
        return "prerequisite"
    if CONSTRAINT_PAGE_PATTERN.search(sentence):
        return "constraint"
    return None


def has_constraint_signals(text: str) -> bool:
    """Page-level detector — must agree with the sentence-level classes.

    TTL/reuse/PCI/header/encryption plus boarding's own constraint classes
    (ID format rules, hierarchy limits, status transitions, prerequisites).
    A page carrying any of these is substantive regardless of size.
    """
    if CONSTRAINT_PAGE_PATTERN.search(text):
        return True
    s = text.lower()
    return bool(
        _ID_FORMAT_PATTERN.search(s)
        or _HIERARCHY_PATTERN.search(s)
        or _STATUS_TRANSITION_PATTERN.search(s)
        or _PREREQUISITE_PATTERN.search(s)
    )


# --- Sentence / heading helpers --------------------------------------------


def iter_sentences(text: str) -> List[str]:
    """Split body into sentence-like units (short pages included)."""
    cleaned = re.sub(r"(?m)^[=-]{3,}\s*$", " ", text)
    cleaned = re.sub(r"!\[.*?\]\([^)]+\)", " ", cleaned)
    cleaned = re.sub(r"\{#[^}]+\}", " ", cleaned)
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n+", "\n", cleaned)
    sentences: List[str] = []
    for block in re.split(r"\n+", cleaned):
        block = block.strip()
        if not block or block.startswith("#") or set(block) <= {"=", "-", "*", " "}:
            continue
        if block.startswith(">"):
            block = re.sub(r"^>\s*", "", block)
            block = re.sub(r"^IMPORTANT\s*", "", block, flags=re.I)
        for part in re.split(r"(?<=[.!?])\s+(?=[A-Z`\"'])", block):
            s = part.strip().strip("`")
            if len(s) >= 24:
                sentences.append(s)
    return sentences


def first_heading(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            return re.sub(r"\s*\{#[^}]+\}\s*$", "", s.lstrip("#").strip())[:160]
        cleaned = re.sub(r"\s*\{#[^}]+\}\s*$", "", s).strip()
        if cleaned and not cleaned.startswith(("!", "[", "<", ">")):
            return cleaned[:160]
    return ""


def link_density(text: str) -> float:
    if not text.strip():
        return 0.0
    links = len(re.findall(r"\[[^\]]+\]\([^)]+\)|href\s*=", text, re.I))
    words = max(len(re.findall(r"\w+", text)), 1)
    return links / words


# --- Shell detector ----------------------------------------------------------


def looks_like_shell(text: str, byte_len: int) -> bool:
    """Shell = nav/stub with no extractable constraints — never 'short file' alone."""
    sentences = iter_sentences(text)
    if any(constraint_kind(s) for s in sentences):
        return False
    links = len(re.findall(r"\[[^\]]+\]\([^)]+\)", text))
    words = max(len(re.findall(r"\w+", text)), 1)
    density = links / words
    if density >= 0.05 and byte_len < 2500:
        return True
    if byte_len < 80 and not sentences:
        return True
    if re.search(r"(?i)see these topics|on this page|jumplink", text) and byte_len < 2000:
        return True
    return False
