"""CyberSource guide API-reference pattern → endpoint_fact claims.

Shape (boarding.md and siblings):
  * Operation heading
  * ``Endpoint`` section with Production / Test lines
    ``POST https://apitest.cybersource.com/boarding/v1/registrations``
  * ``Required Fields`` definition list — link-style ``[field](url)`` or
    plain ``field.name`` terms with a following ``:``
  * ``REST Example`` with fenced JSON request and response

Emits ``endpoint_fact`` (not quickstart_step). UI procedures stay on the
step extractor; a page can yield both.

Required-fields derivation contract (L2 — cleared):
  Recover fields only from authoritative sources, and tag every field with
  exactly one of:
    * ``api_fields_link`` — term is a markdown link (usually into api-fields)
    * ``required_fields_section`` — plain DL term under a same-document
      Required Fields heading
    * ``sibling_req_fields_page`` — Required Fields page joined by operation
      anchor (``{op}-req-fields``)
  If none of those exist, leave ``required_fields`` empty and keep the soft
  gap. Never infer required-ness from REST Example JSON keys — a key in an
  example is not a required field.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from content_bench.content_engine.source_noise import (
    attach_source_meta,
    clean_claim_text,
    extract_anchors,
)

_ENDPOINT_HEADING = re.compile(
    r"(?m)^(?:"
    r"#{1,6}\s+Endpoint\s*\{#([^}]+)\}\s*$"
    r"|"
    r"Endpoint\s*\{#([^}]+)\}\s*\n(=+|-+)\s*$"
    r")"
)

_VERB_URL = re.compile(
    r"\b(GET|POST|PUT|PATCH|DELETE)\b[`\s]*"
    r"((?:https?://[A-Za-z0-9.-]+)?)"
    r"[`\s]*"
    r"(/[A-Za-z0-9_{}/.?-]+)"
)

_ENV_LINE = re.compile(
    r"(?i)\*\*\s*(Production|Test)\s*:\*\*"
)

_REQ_FIELDS_HEADING = re.compile(
    r"(?m)^(?:#{1,6}\s+)?Required Fields\b[^\n{]*\{#([^}]+)\}"
)

_REST_EXAMPLE_HEADING = re.compile(
    r"(?m)^(?:#{1,6}\s+)?REST Example:[^\n{]*\{#([^}]+)\}"
)

_OPERATION_HEADING = re.compile(
    r"(?m)^(?!"
    r"(?:Endpoint|Required Fields|REST Example|Using |When |After |Before )"
    r")"
    r"(.+?)\s*\{#([^}]+)\}\s*\n(=+|-+)\s*$"
)

_DL_TERM = re.compile(
    r"^\[([^\]]+)\]\(([^)]+)\)\s*$"
)
# Plain definition-list term: dotted field path, optional backticks, then `:`.
_PLAIN_DL_TERM = re.compile(
    r"^`?([A-Za-z][A-Za-z0-9_.]*)`?\s*$"
)

_FENCE = re.compile(r"(?m)^```([^\n]*)\n(.*?)^```\s*$", re.S)

# Authoritative derivation sources — never example JSON.
DERIVATION_API_FIELDS_LINK = "api_fields_link"
DERIVATION_REQUIRED_FIELDS_SECTION = "required_fields_section"
DERIVATION_SIBLING_REQ_FIELDS_PAGE = "sibling_req_fields_page"
DERIVATION_SOURCES = frozenset(
    {
        DERIVATION_API_FIELDS_LINK,
        DERIVATION_REQUIRED_FIELDS_SECTION,
        DERIVATION_SIBLING_REQ_FIELDS_PAGE,
    }
)


@dataclass
class ApiRefSkip:
    reason: str
    line: int
    detail: str = ""


@dataclass
class SoftGapFinding:
    """Matched Endpoint section missing Required Fields and/or REST Example.

    A finding, not a warning: the developer can see the verb+URL and still
    cannot call the endpoint without fields or an example payload.
    """

    product_id: str
    method: str
    path: str
    operation_title: str
    deep_link: Optional[str]
    missing_required_fields: bool
    missing_rest_example: bool
    line: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ApiRefReport:
    """Per-document scan of the API-reference pattern."""

    source_pointer: str
    endpoint_headings: int = 0
    matched: int = 0
    matched_with_required_fields: int = 0
    matched_with_example: int = 0
    claims_emitted: int = 0
    skipped: List[ApiRefSkip] = field(default_factory=list)
    soft_gaps: List[SoftGapFinding] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_pointer": self.source_pointer,
            "endpoint_headings": self.endpoint_headings,
            "matched": self.matched,
            "matched_with_required_fields": self.matched_with_required_fields,
            "matched_with_example": self.matched_with_example,
            "claims_emitted": self.claims_emitted,
            "skipped": [asdict(s) for s in self.skipped],
            "soft_gaps": [g.to_dict() for g in self.soft_gaps],
        }


def _product_id_from_pointer(source_pointer: str, doc_stem: str) -> str:
    name = source_pointer.rsplit("/", 1)[-1]
    if name.endswith(".md.md"):
        name = name[: -len(".md.md")]
    elif name.endswith(".md"):
        name = name[: -len(".md")]
    if "_" in name:
        return name.rsplit("_", 1)[-1]
    return doc_stem.rsplit("_", 1)[-1] if "_" in doc_stem else doc_stem


def _heading_end(match: re.Match) -> int:
    return match.end()


def _next_major_heading(text: str, start: int) -> int:
    """Index of the next setext/ATX heading at/after start, or len(text)."""
    m = re.search(
        r"(?m)^(?:#{1,6}\s+\S|.+\n[=-]{3,}\s*$)",
        text[start:],
    )
    if not m:
        return len(text)
    return start + m.start()


def _is_field_term_line(line: str) -> bool:
    s = line.strip()
    return bool(_DL_TERM.match(s) or _PLAIN_DL_TERM.match(s))


def _parse_required_fields(
    block: str,
    *,
    default_derivation: str = DERIVATION_REQUIRED_FIELDS_SECTION,
) -> List[Dict[str, str]]:
    """Parse Required Fields definition-list body into tagged field dicts.

    Accepts link-style ``[name](url)`` and plain ``name`` / ``:`` terms.
    Every emitted field carries ``derivation_source`` ∈ DERIVATION_SOURCES.
    Does not read JSON examples.
    """
    if default_derivation not in DERIVATION_SOURCES:
        raise ValueError(f"invalid derivation_source: {default_derivation}")
    fields: List[Dict[str, str]] = []
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i].strip()
        # Skip setext underlines left over after the heading match.
        if raw and set(raw) <= {"=", "-"}:
            i += 1
            continue
        link_m = _DL_TERM.match(raw)
        plain_m = _PLAIN_DL_TERM.match(raw) if not link_m else None
        if not link_m and not plain_m:
            i += 1
            continue
        # Plain terms must be followed by a definition ``:`` (alone or inline).
        if plain_m:
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if not (nxt == ":" or nxt.startswith(":")):
                i += 1
                continue
            name = plain_m.group(1).strip()
            url = ""
            derivation = default_derivation
        else:
            assert link_m is not None
            name = link_m.group(1).strip()
            url = re.sub(r'\s+""\s*$', "", link_m.group(2).strip()).strip()
            # Link into api-fields (or any field URL) is the api_fields_link source.
            derivation = (
                DERIVATION_API_FIELDS_LINK
                if url
                else default_derivation
            )
        i += 1
        if i < len(lines) and lines[i].strip() in {":", ""}:
            if lines[i].strip() == ":":
                i += 1
            elif i + 1 < len(lines) and lines[i + 1].strip() == ":":
                i += 2
        # Inline ": instruction" on the term line is rare; handle ": foo" next.
        instr_parts: List[str] = []
        while i < len(lines):
            s = lines[i]
            st = s.strip()
            if _is_field_term_line(st):
                # Peek: plain term without following ":" is not a new field.
                if _PLAIN_DL_TERM.match(st) and not _DL_TERM.match(st):
                    nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
                    if nxt != ":" and not nxt.startswith(":"):
                        if st:
                            instr_parts.append(st)
                        i += 1
                        continue
                break
            if re.match(r"^(?:Endpoint|Required Fields|REST Example)\b", st):
                break
            if st and set(st) <= {"=", "-"}:
                break
            if st == ":":
                i += 1
                continue
            if st.startswith(":") and len(st) > 1:
                instr_parts.append(st.lstrip(":").strip())
                i += 1
                continue
            if st:
                instr_parts.append(st)
            elif instr_parts:
                i += 1
                break
            i += 1
        instruction = " ".join(instr_parts).strip()
        instruction, _ = clean_claim_text(instruction)
        field: Dict[str, str] = {
            "name": name,
            "instruction": instruction,
            "field_url": url,
            "derivation_source": derivation,
        }
        fields.append(field)
    return fields


def _rf_body_after_heading(text: str, heading_match: re.Match) -> str:
    """Slice Required Fields body until REST Example / next Endpoint / EOF."""
    start = heading_match.end()
    rest_m = _REST_EXAMPLE_HEADING.search(text, start)
    next_ep = _ENDPOINT_HEADING.search(text, start)
    end = len(text)
    if rest_m:
        end = min(end, rest_m.start())
    if next_ep:
        end = min(end, next_ep.start())
    return text[start:end]


def load_sibling_req_field_pages(near: Path) -> Dict[str, str]:
    """Load ``*req-fields*`` markdown siblings next to ``near`` (file or dir)."""
    folder = near if near.is_dir() else near.parent
    if not folder.is_dir():
        return {}
    out: Dict[str, str] = {}
    for path in folder.glob("*req-fields*"):
        if not path.is_file():
            continue
        try:
            out[path.name] = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
    return out


def _resolve_required_fields(
    text: str,
    block: str,
    *,
    op_anchor: Optional[str],
    sibling_pages: Optional[Dict[str, str]] = None,
) -> List[Dict[str, str]]:
    """Resolve required fields under the derivation contract.

    Order: same-block RF section → same-document RF by op anchor → sibling
    ``*-req-fields*`` page. Refuse (return []) if none yield fields.
    """
    req_m = _REQ_FIELDS_HEADING.search(block)
    if req_m:
        fields = _parse_required_fields(
            _rf_body_after_heading(block, req_m),
            default_derivation=DERIVATION_REQUIRED_FIELDS_SECTION,
        )
        if fields:
            return fields

    # Same document, outside the Endpoint block (setext sibling section).
    if op_anchor:
        for rm in _REQ_FIELDS_HEADING.finditer(text):
            rf_anchor = rm.group(1) or ""
            if op_anchor in rf_anchor or rf_anchor.startswith(op_anchor):
                fields = _parse_required_fields(
                    _rf_body_after_heading(text, rm),
                    default_derivation=DERIVATION_REQUIRED_FIELDS_SECTION,
                )
                if fields:
                    return fields

    # Sibling Required Fields page joined by operation anchor.
    if op_anchor and sibling_pages:
        needle = f"{op_anchor}-req-fields"
        for key, page_text in sibling_pages.items():
            key_l = key.lower()
            if op_anchor not in key_l and needle not in key_l:
                continue
            rm = _REQ_FIELDS_HEADING.search(page_text)
            body = _rf_body_after_heading(page_text, rm) if rm else page_text
            fields = _parse_required_fields(
                body,
                default_derivation=DERIVATION_SIBLING_REQ_FIELDS_PAGE,
            )
            if not fields:
                fields = _parse_required_fields(
                    page_text,
                    default_derivation=DERIVATION_SIBLING_REQ_FIELDS_PAGE,
                )
            if fields:
                # Join path is the sibling page; keep field_url, retag source.
                for f in fields:
                    f["derivation_source"] = DERIVATION_SIBLING_REQ_FIELDS_PAGE
                return fields

    return []


def _parse_examples(block: str) -> Tuple[Optional[str], Optional[str]]:
    """Return (request_body, response_body) from REST Example fences."""
    request: Optional[str] = None
    response: Optional[str] = None
    # Split on Request / Response labels to assign fences.
    lower = block
    req_idx = re.search(r"(?im)^Request\s*$", lower)
    resp_idx = re.search(r"(?im)^Response\b[^\n]*$", lower)
    fences = list(_FENCE.finditer(block))
    if not fences:
        return None, None

    def body_of(m: re.Match) -> str:
        return m.group(2).strip()

    if req_idx and resp_idx:
        for m in fences:
            if m.start() >= resp_idx.start():
                if response is None:
                    response = body_of(m)
            elif m.start() >= req_idx.start():
                if request is None:
                    request = body_of(m)
    elif req_idx:
        for m in fences:
            if m.start() >= req_idx.start() and request is None:
                request = body_of(m)
            elif request is not None and response is None:
                response = body_of(m)
    else:
        # No labels — first fence = request, second = response.
        request = body_of(fences[0])
        if len(fences) > 1:
            response = body_of(fences[1])
    return request, response


def _operation_context(text: str, endpoint_start: int) -> Tuple[str, Optional[str]]:
    """Nearest preceding operation heading title + anchor."""
    preceding = text[:endpoint_start]
    matches = list(_OPERATION_HEADING.finditer(preceding))
    if not matches:
        return "", None
    m = matches[-1]
    title, _ = clean_claim_text(m.group(1).strip())
    return title, m.group(2).strip()


def _endpoint_block_bounds(text: str, match: re.Match) -> Tuple[int, int]:
    """Span from this Endpoint heading through the following REST Example (if any)."""
    start = match.start()
    after = match.end()
    # Extend through Required Fields + REST Example belonging to this endpoint.
    rest = _REST_EXAMPLE_HEADING.search(text, after)
    next_ep = _ENDPOINT_HEADING.search(text, after)
    next_ep_at = next_ep.start() if next_ep else len(text)
    if rest and rest.start() < next_ep_at:
        # End at next endpoint or next operation-level heading after the example fences.
        example_start = rest.start()
        # Consume fences after the example heading.
        fence_end = example_start
        for fm in _FENCE.finditer(text, example_start):
            if next_ep and fm.start() >= next_ep_at:
                break
            fence_end = fm.end()
        end = min(next_ep_at, max(fence_end, _next_major_heading(text, fence_end + 1)))
        # Prefer ending at next Endpoint.
        end = min(end, next_ep_at)
        return start, end
    # No REST Example — stop at next Endpoint or next Required Fields of another op.
    return start, next_ep_at


def extract_api_reference_claims(
    text: str,
    *,
    source_pointer: str,
    doc_stem: str,
    sibling_pages: Optional[Dict[str, str]] = None,
) -> Tuple[List[Any], ApiRefReport, set]:
    """Extract rich endpoint_fact claims from the API-reference pattern.

    Returns (claims, report, covered_endpoint_keys) where covered keys are
    ``METHOD:host:path`` strings already emitted — the thin C1 scanner should
    skip them to avoid duplicates.

    ``sibling_pages`` maps a page key (filename or anchor) to markdown text for
    ``{op}-req-fields`` joins. Example JSON is never consulted for fields.
    """
    # Late import to avoid circular typing with NormalizedClaim.
    from content_bench.content_engine.ingest import NormalizedClaim

    report = ApiRefReport(source_pointer=source_pointer)
    claims: List[NormalizedClaim] = []
    covered: set = set()

    for match in _ENDPOINT_HEADING.finditer(text):
        report.endpoint_headings += 1
        line_no = text.count("\n", 0, match.start()) + 1
        ep_anchor = (match.group(1) or match.group(2) or "").strip()
        block_start, block_end = _endpoint_block_bounds(text, match)
        block = text[block_start:block_end]

        # Verb/URL lines (Production / Test).
        env_endpoints: List[Tuple[str, str, str, str]] = []  # env, method, host, path
        for lm in re.finditer(r"(?m)^.+$", block):
            line = lm.group(0)
            vm = _VERB_URL.search(line)
            if not vm:
                continue
            method, host, path = vm.group(1), vm.group(2), vm.group(3).rstrip(".,;")
            # Trim trailing anchor glued to path: /registrations`{#x} already
            # handled because path charset excludes `{`.
            env_m = _ENV_LINE.search(line)
            if env_m:
                env = env_m.group(1).lower()
            elif host and "test" in host:
                env = "test"
            elif host:
                env = "production"
            else:
                env = ""
            if not host:
                # Bare verb+path under Endpoint — still a match, host empty.
                pass
            env_endpoints.append((env, method, host, path))

        if not env_endpoints:
            report.skipped.append(
                ApiRefSkip(
                    reason="no_verb_url_line",
                    line=line_no,
                    detail=f"Endpoint {{#{ep_anchor}}} has no GET/POST/… URL line",
                )
            )
            continue

        example_request: Optional[str] = None
        example_response: Optional[str] = None
        rest_m = _REST_EXAMPLE_HEADING.search(block)
        if rest_m:
            example_request, example_response = _parse_examples(block[rest_m.start() :])

        op_title, op_anchor = _operation_context(text, match.start())
        # Derivation contract: RF section / sibling page / api-fields link only.
        # example_request is intentionally not passed into field resolution.
        req_fields = _resolve_required_fields(
            text,
            block,
            op_anchor=op_anchor or ep_anchor or None,
            sibling_pages=sibling_pages,
        )
        report.matched += 1
        if req_fields:
            report.matched_with_required_fields += 1
        if example_request is not None or example_response is not None:
            report.matched_with_example += 1

        # Prefer the operation anchor for deep links; fall back to Endpoint.
        primary_anchor = op_anchor or ep_anchor or f"ep-{block_start}"

        # Soft-gap findings (per matched Endpoint section, not per host line).
        missing_rf = not bool(req_fields)
        missing_ex = example_request is None and example_response is None
        if missing_rf or missing_ex:
            # Representative verb+path from the first env line.
            _env, method0, _host0, path0 = env_endpoints[0]
            from content_bench.content_engine.source_noise import deep_link_for

            report.soft_gaps.append(
                SoftGapFinding(
                    product_id=_product_id_from_pointer(source_pointer, doc_stem),
                    method=method0,
                    path=path0,
                    operation_title=op_title or f"{method0} {path0}",
                    deep_link=deep_link_for(source_pointer, primary_anchor),
                    missing_required_fields=missing_rf,
                    missing_rest_example=missing_ex,
                    line=line_no,
                )
            )

        # One claim per host/env line, sharing fields + examples.
        # Distinct operations often reuse the same verb+path (e.g. several
        # boarding flows POST /boarding/v1/registrations) — key claims by
        # operation anchor so each section keeps its own fields/example.
        for env, method, host, path in env_endpoints:
            thin_key = f"{method}:{host}:{path}"
            covered.add(thin_key)  # tell the C1 scanner to skip these URL lines
            claim_key = f"{thin_key}:{primary_anchor}"
            label = f"{method} {host}{path}" if host else f"{method} {path}"
            # Claim text: readable summary without brace anchors / empty titles.
            text_parts = [label]
            if req_fields:
                with_instr = [
                    f"{f['name']}"
                    + (f" — {f['instruction']}" if f["instruction"] else "")
                    for f in req_fields
                ]
                text_parts.append("Required: " + "; ".join(with_instr[:12]))
                if len(with_instr) > 12:
                    text_parts[-1] += f"; … +{len(with_instr) - 12} more"
            if example_request:
                text_parts.append("Example request present")
            claim_text, _ = clean_claim_text(" | ".join(text_parts))

            extras: Dict[str, Any] = {
                "method": method,
                "path": path,
                "pattern": "api_reference",
                "required_fields": req_fields,
            }
            if host:
                extras["host"] = host
            if env:
                extras["environment"] = (
                    "test" if env == "test" else "production"
                )
            if op_title:
                extras["operation_title"] = op_title
            if example_request is not None:
                extras["example_request"] = example_request
            if example_response is not None:
                extras["example_response"] = example_response

            span_text = block
            if primary_anchor not in extract_anchors(span_text):
                span_text = f"{{#{primary_anchor}}}\n" + span_text

            extras = attach_source_meta(
                extras,
                source_pointer=source_pointer,
                raw_span_text=span_text,
                full_text=text,
                span_start=block_start,
                span_end=block_end,
            )
            extras["anchor"] = primary_anchor
            from content_bench.content_engine.source_noise import deep_link_for

            link = deep_link_for(source_pointer, primary_anchor)
            if link:
                extras["deep_link"] = link

            digest = hashlib.sha1(claim_key.encode()).hexdigest()[:8]
            claims.append(
                NormalizedClaim(
                    claim_id=f"{doc_stem}:endpoint:{method.lower()}:{digest}",
                    schema="endpoint_fact",
                    title=(op_title or f"{method} {path}")[:120],
                    text=claim_text[:800],
                    source_pointer=source_pointer,
                    extras=extras,
                )
            )
            report.claims_emitted += 1

    return claims, report, covered


def summarize_reports(reports: Sequence[ApiRefReport]) -> Dict[str, Any]:
    skip_counts: Dict[str, int] = {}
    for r in reports:
        for s in r.skipped:
            skip_counts[s.reason] = skip_counts.get(s.reason, 0) + 1
    return {
        "documents": len(reports),
        "endpoint_headings": sum(r.endpoint_headings for r in reports),
        "matched": sum(r.matched for r in reports),
        "matched_with_required_fields": sum(
            r.matched_with_required_fields for r in reports
        ),
        "matched_with_example": sum(r.matched_with_example for r in reports),
        "claims_emitted": sum(r.claims_emitted for r in reports),
        "skipped": sum(len(r.skipped) for r in reports),
        "skipped_by_reason": skip_counts,
    }
