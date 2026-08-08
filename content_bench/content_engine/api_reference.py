"""CyberSource guide API-reference pattern → endpoint_fact claims.

Shape (boarding.md and siblings):
  * Operation heading
  * ``Endpoint`` section with Production / Test lines
    ``POST https://apitest.cybersource.com/boarding/v1/registrations``
  * ``Required Fields`` definition list — each term links to api-fields;
    some carry instructions like ``Set the value to MERCHANT``
  * ``REST Example`` with fenced JSON request and response

Emits ``endpoint_fact`` (not quickstart_step). UI procedures stay on the
step extractor; a page can yield both.
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

_FENCE = re.compile(r"(?m)^```([^\n]*)\n(.*?)^```\s*$", re.S)


@dataclass
class ApiRefSkip:
    reason: str
    line: int
    detail: str = ""


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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_pointer": self.source_pointer,
            "endpoint_headings": self.endpoint_headings,
            "matched": self.matched,
            "matched_with_required_fields": self.matched_with_required_fields,
            "matched_with_example": self.matched_with_example,
            "claims_emitted": self.claims_emitted,
            "skipped": [asdict(s) for s in self.skipped],
        }


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


def _parse_required_fields(block: str) -> List[Dict[str, str]]:
    fields: List[Dict[str, str]] = []
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        m = _DL_TERM.match(lines[i].strip())
        if not m:
            i += 1
            continue
        name = m.group(1).strip()
        raw_url = m.group(2).strip()
        # Drop empty title from the URL side: 'url ""' → 'url'
        url = re.sub(r'\s+""\s*$', "", raw_url).strip()
        i += 1
        # Optional lone ':' line
        if i < len(lines) and lines[i].strip() == ":":
            i += 1
        instr_parts: List[str] = []
        while i < len(lines):
            s = lines[i]
            if _DL_TERM.match(s.strip()):
                break
            if re.match(r"^(?:#{1,6}\s+|\S.+\n[=-]{3,})", s):
                break
            if re.match(r"^(?:Endpoint|Required Fields|REST Example)\b", s):
                break
            if s.strip() == ":":
                i += 1
                continue
            if s.strip():
                instr_parts.append(s.strip())
            elif instr_parts:
                # blank after instruction ends this term
                i += 1
                break
            i += 1
        instruction = " ".join(instr_parts).strip()
        # Clean anchors / empty titles out of instruction text.
        instruction, _ = clean_claim_text(instruction)
        fields.append(
            {
                "name": name,
                "instruction": instruction,
                "field_url": url,
            }
        )
    return fields


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
) -> Tuple[List[Any], ApiRefReport, set]:
    """Extract rich endpoint_fact claims from the API-reference pattern.

    Returns (claims, report, covered_endpoint_keys) where covered keys are
    ``METHOD:host:path`` strings already emitted — the thin C1 scanner should
    skip them to avoid duplicates.
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

        # Required Fields block inside this span (if any).
        req_fields: List[Dict[str, str]] = []
        req_m = _REQ_FIELDS_HEADING.search(block)
        if req_m:
            req_start = req_m.end()
            rest_m = _REST_EXAMPLE_HEADING.search(block, req_start)
            req_end = rest_m.start() if rest_m else len(block)
            req_fields = _parse_required_fields(block[req_start:req_end])

        example_request: Optional[str] = None
        example_response: Optional[str] = None
        rest_m = _REST_EXAMPLE_HEADING.search(block)
        if rest_m:
            example_request, example_response = _parse_examples(block[rest_m.start() :])

        op_title, op_anchor = _operation_context(text, match.start())
        report.matched += 1
        if req_fields:
            report.matched_with_required_fields += 1
        if example_request is not None or example_response is not None:
            report.matched_with_example += 1

        # Prefer the operation anchor for deep links; fall back to Endpoint.
        primary_anchor = op_anchor or ep_anchor or f"ep-{block_start}"

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
