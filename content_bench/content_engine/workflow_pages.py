"""Boarding workflow pages — composed from normalized claims only.

Reads `normalized/<stamp>.claims.json`; never reads `raw/`. Pages are
generated: fix the source and regenerate, never hand-edit.

Dedupe rule (architect ruling): when a family mega-guide and a child page
carry the same claim text, the child page wins, always — the child has the
more specific source pointer and the better anchor. No hash tie-breaks.
Mega-guide claims with no matching child claim are *residuals*, reported not
merged: each is either genuinely unique content or a sign the child page
failed to ingest.

Workflow schema per step: actor, precondition, action, expected outcome,
failure modes. Missing pieces are stated as gaps, never invented.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[2]

FACTS_OPEN = "<!-- section:facts -->"
FACTS_CLOSE = "<!-- /section:facts -->"
PROSE_OPEN = "<!-- section:prose -->"
PROSE_CLOSE = "<!-- /section:prose -->"

# Family mega-guides: the whole-guide compendium files at each family root.
MEGA_GUIDE_NAMES = (
    "en-us_boarding_user_all_ebc_boarding-user.md.md",
    "en-us_boarding_developer_all_rest_boarding.md.md",
    "en-us_boarding-template-management_user_all_ada_boarding-template-mgmt.md.md",
)


@dataclass
class WorkflowSpec:
    workflow_id: str
    title: str
    goal: str
    # Doc-name substrings whose claims belong to this workflow, in step order.
    doc_matchers: Sequence[str]


BOARDING_WORKFLOWS: Tuple[WorkflowSpec, ...] = (
    WorkflowSpec(
        workflow_id="create-merchant-organization",
        title="Create a Merchant Organization",
        goal="Register a new merchant (organization + transacting org) via the Boarding Registration Service.",
        doc_matchers=(
            "boarding-reg-intro",
            "boarding-reg-create-merch-api",
            "boarding-reg-create-transacting-api",
            "boarding-reg-create-new-transacting-api",
            "merchants-v2-add-merchant",
            "merchants-v2-add-to-existing",
        ),
    ),
    WorkflowSpec(
        workflow_id="extend-hierarchy",
        title="Extend the Organization Hierarchy",
        goal="Add structural organizations to model a portfolio's business structure.",
        doc_matchers=(
            "boarding-extend-hierarchy",
            "boarding-reg-create-structural-api",
            "merchants-v2-add-structural",
        ),
    ),
    WorkflowSpec(
        workflow_id="enable-configure-products",
        title="Enable and Configure Products",
        goal="Enable products for a merchant during or after onboarding (BRS invokes PECS; PECS updates after).",
        doc_matchers=(
            "boarding-products",
            "boarding-pecs",
            "pecs-",
            "boarding-payer-auth",
            "boarding-tms",
            "boarding-enablement-products",
            "boarding-enable-products",
            "boarding-config-",
            "boarding-update-product-api",
        ),
    ),
    WorkflowSpec(
        workflow_id="search-organizations",
        title="Search for Organizations",
        goal="Find organizations and view hierarchy from the Business Center.",
        doc_matchers=(
            "merchants-v2-search",
            "boarding-retrieve-an-organization",
            "boarding-retrieve-organizations",
            "boarding-update-information-api",
        ),
    ),
    WorkflowSpec(
        workflow_id="change-organization-status",
        title="Change an Organization's Status",
        goal="Move an organization between statuses after boarding.",
        doc_matchers=(
            "boarding-change-org-status",
            "merchants-v2-status-chang",
        ),
    ),
    WorkflowSpec(
        workflow_id="send-registration-email",
        title="Send a Registration Email",
        goal="Send the merchant a registration email to create Business Center credentials.",
        doc_matchers=("merchants-v2-email",),
    ),
)


def _norm_text(text: str) -> str:
    t = re.sub(r"\{#[^}]+\}", "", text)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def _doc_name(claim: Dict[str, Any]) -> str:
    return Path(str(claim.get("source_pointer") or "")).name


def _citation(claim: Dict[str, Any]) -> str:
    """Claim id + optional working deep link (never a raw brace anchor)."""
    cid = claim.get("claim_id") or ""
    link = (claim.get("extras") or {}).get("deep_link")
    if link:
        return f"<sub>[`{cid}`]({link})</sub>"
    return f"<sub>`{cid}`</sub>"


def _render_endpoint_block(claim: Dict[str, Any]) -> List[str]:
    """Render one endpoint_fact (API-reference or thin verb_path) into facts."""
    ex = claim.get("extras") or {}
    method = ex.get("method") or ""
    path = ex.get("path") or ""
    host = ex.get("host") or ""
    env = ex.get("environment") or ""
    title = claim.get("title") or f"{method} {path}"
    lines = [
        f"### {title}",
        "",
        f"- **Method:** `{method}`",
        f"- **Path:** `{path}`",
    ]
    if host:
        label = f"{env} host" if env else "Host"
        lines.append(f"- **{label}:** `{host}`")
    fields = ex.get("required_fields") or []
    if fields:
        lines += ["", "#### Required fields", ""]
        for f in fields:
            name = f.get("name") or ""
            instr = (f.get("instruction") or "").strip()
            url = f.get("field_url") or ""
            name_md = f"[`{name}`]({url})" if url else f"`{name}`"
            if instr:
                lines.append(f"- {name_md} — {instr}")
            else:
                lines.append(f"- {name_md}")
    req = ex.get("example_request")
    resp = ex.get("example_response")
    if req is not None:
        lines += ["", "#### Example request", "", "```json", req, "```"]
    if resp is not None:
        lines += ["", "#### Example response", "", "```json", resp, "```"]
    lines += ["", f"- {_citation(claim)}", ""]
    return lines


def _actor_for_doc(doc: str) -> str:
    if "_developer_all_rest_" in doc or "_developer_ctv_rest_" in doc:
        return "Partner system (REST API)"
    if "_user_all_ebc_" in doc or "_user_all_ada_" in doc:
        return "Partner admin (Business Center)"
    return "Partner"


def _expected_outcome(action: str) -> Optional[str]:
    m = re.search(
        r"(?:The|A|An)\s+[^.]*\b(?:page|window|dialog|menu|list)\b[^.]*\bappears[^.]*\.",
        action,
    )
    if m:
        return m.group(0).strip()
    m = re.search(r"[^.]*\bis displayed\b[^.]*\.", action)
    if m:
        return m.group(0).strip()
    return None


def _endpoint_outcome(claim: Dict[str, Any]) -> Optional[str]:
    """Outcome from the REST example response when the UI prose states none."""
    ex = claim.get("extras") or {}
    resp = ex.get("example_response")
    if resp is None:
        return None
    resp_s = str(resp).strip()
    if not resp_s:
        return None
    # Prefer a compact status signal when present.
    m = re.search(r'"status"\s*:\s*"([^"]+)"', resp_s)
    if m:
        return f'Response status `{m.group(1)}` (see example response).'
    if re.match(r"^\d{3}\b", resp_s):
        return f"HTTP {resp_s.splitlines()[0].strip()} (see example response)."
    return "Successful response body documented in the REST example."


def dedupe_prefer_child(
    claims: Sequence[Dict[str, Any]],
    *,
    mega_names: Sequence[str] = MEGA_GUIDE_NAMES,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Child page wins, always. Returns (kept_claims, mega_residuals).

    A mega-guide claim whose normalized text matches any child claim is
    dropped (child carries the fact with the specific pointer). Mega claims
    with no child match are residuals: kept out of pages, reported for
    review — unique content or a failed child ingest, never silently merged.

    Exception: ``endpoint_fact`` claims with ``pattern=api_reference`` stay.
    The Endpoint + Required Fields + REST Example shape only survives intact
    on the product-root mega-guide; child TOC pages split it apart.
    """
    mega = set(mega_names)
    child_texts = {
        _norm_text(c["text"])
        for c in claims
        if _doc_name(c) not in mega
    }
    kept: List[Dict[str, Any]] = []
    residuals: List[Dict[str, Any]] = []
    for c in claims:
        if _doc_name(c) not in mega:
            kept.append(c)
            continue
        if (
            c.get("schema") == "endpoint_fact"
            and (c.get("extras") or {}).get("pattern") == "api_reference"
        ):
            kept.append(c)
            continue
        if _norm_text(c["text"]) in child_texts:
            continue  # child wins
        residuals.append(c)
    return kept, residuals


def _claims_for(spec: WorkflowSpec, claims: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out = []
    for c in claims:
        doc = _doc_name(c)
        if any(m in doc for m in spec.doc_matchers):
            out.append(c)
            continue
        # Mega-guide API refs: match on operation anchor / title (the root
        # filename is just ``…_boarding.md.md`` and lacks the section slug).
        if c.get("schema") == "endpoint_fact":
            ex = c.get("extras") or {}
            blob = " ".join(
                [
                    doc,
                    str(c.get("title") or ""),
                    str(ex.get("anchor") or ""),
                    str(ex.get("operation_title") or ""),
                ]
            )
            if any(m in blob for m in spec.doc_matchers):
                out.append(c)
    return out


def _endpoint_richness(claim: Dict[str, Any]) -> tuple:
    """Prefer claims that still carry Required Fields + REST Example.

    Child TOC pages often hold only the Endpoint stub; the product-root
    mega-guide holds the full pattern. Never let the stub win the dedupe.
    """
    ex = claim.get("extras") or {}
    return (
        1 if ex.get("required_fields") else 0,
        1 if ex.get("example_request") is not None else 0,
        1 if ex.get("example_response") is not None else 0,
        1 if ex.get("environment") == "test" else 0,
    )


def _dedupe_endpoints(endpoints: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rich = [
        c
        for c in endpoints
        if (c.get("extras") or {}).get("pattern") == "api_reference"
    ]
    show = list(rich or endpoints)
    # One claim per operation: richest extras win (fields/example over stub).
    by_anchor: Dict[str, Dict[str, Any]] = {}
    for c in show:
        ex = c.get("extras") or {}
        key = f"{ex.get('anchor')}:{ex.get('method')}:{ex.get('path')}"
        prev = by_anchor.get(key)
        if prev is None or _endpoint_richness(c) > _endpoint_richness(prev):
            by_anchor[key] = c
    return list(by_anchor.values())


def _render_sequence_api_step(step_no: int, claim: Dict[str, Any]) -> List[str]:
    """One numbered sequence entry for an API-reference endpoint_fact."""
    ex = claim.get("extras") or {}
    method = ex.get("method") or ""
    path = ex.get("path") or ""
    host = ex.get("host") or ""
    env = ex.get("environment") or ""
    title = claim.get("title") or f"{method} {path}"
    lines = [
        f"{step_no}. **API:** `{method} {path}` — {title}",
        "   - Actor: Partner system (REST API)",
    ]
    if host:
        label = f"{env} host" if env else "host"
        lines.append(f"   - {label}: `{host}`")
    fields = ex.get("required_fields") or []
    if fields:
        lines.append("   - Required fields:")
        for f in fields:
            name = f.get("name") or ""
            instr = (f.get("instruction") or "").strip()
            url = f.get("field_url") or ""
            name_md = f"[`{name}`]({url})" if url else f"`{name}`"
            if instr:
                lines.append(f"     - {name_md} — {instr}")
            else:
                lines.append(f"     - {name_md}")
    else:
        lines.append(
            "   - Required fields: **Gap:** not listed for this endpoint in the source."
        )
    req = ex.get("example_request")
    resp = ex.get("example_response")
    if req is not None:
        lines.append("   - Example request:")
        lines.append("     ```json")
        for jl in str(req).splitlines() or [str(req)]:
            lines.append(f"     {jl}")
        lines.append("     ```")
    else:
        lines.append(
            "   - Example request: **Gap:** no REST Example request in the source."
        )
    outcome = _endpoint_outcome(claim)
    if outcome:
        lines.append(f"   - Expected outcome: {outcome}")
        lines.append("   - outcome_missing: false")
    else:
        lines.append("   - Expected outcome: **Gap:** not stated in source.")
        # Machine-readable flag for portal/eval (L2 gap-marker proposal).
        lines.append("   - outcome_missing: true")
    if resp is not None and outcome:
        lines.append("   - Example response:")
        lines.append("     ```json")
        for jl in str(resp).splitlines() or [str(resp)]:
            lines.append(f"     {jl}")
        lines.append("     ```")
    lines.append(f"   - {_citation(claim)}")
    return lines


def compose_workflow_page(
    spec: WorkflowSpec,
    claims: Sequence[Dict[str, Any]],
    *,
    stamp: str,
) -> str:
    wf_claims = _claims_for(spec, claims)
    steps = [c for c in wf_claims if c["schema"] == "quickstart_step"]
    prose = [c for c in wf_claims if c["schema"] == "prose_claim"]
    errors = [c for c in wf_claims if c["schema"] == "error_case"]
    endpoints = _dedupe_endpoints(
        [c for c in wf_claims if c["schema"] == "endpoint_fact"]
    )

    prereqs = [
        c for c in prose if c.get("extras", {}).get("claim_kind") == "prerequisite"
    ]
    constraints = [
        c
        for c in prose
        if c.get("extras", {}).get("claim_kind")
        not in (None, "guidance", "prerequisite")
    ]

    # One continuous sequence: API operations first (callable path), then UI
    # steps — single numbering, never restarting at 1 per source fragment.
    steps_sorted = sorted(
        steps,
        key=lambda c: (_doc_name(c), int(c.get("extras", {}).get("sequence") or 0)),
    )

    lines: List[str] = [
        f"# {spec.title}",
        "",
        PROSE_OPEN,
        f"{spec.goal}",
        PROSE_CLOSE,
        "",
        f"_Generated from `normalized/{stamp}.claims.json`; do not hand-edit. "
        "Fix the source and regenerate._",
        "",
        FACTS_OPEN,
        "",
        "## Preconditions",
        "",
    ]
    if prereqs:
        for c in prereqs:
            lines.append(f"- {c['text'].strip()}  ")
            lines.append(f"  {_citation(c)} · {c['source_pointer']}")
    else:
        lines.append("- **Gap:** no prerequisite is specified in the source docs.")

    lines += ["", "## Steps", ""]

    step_no = 0
    outcome_gaps = 0
    sequence_len = 0

    if not endpoints and not steps_sorted:
        lines.append(
            "- **Gap:** the source docs describe this workflow but list no "
            "API operations or procedural steps."
        )
    else:
        if endpoints:
            lines.append("### REST API path")
            lines.append("")
            for c in endpoints:
                step_no += 1
                sequence_len += 1
                block = _render_sequence_api_step(step_no, c)
                if any("Expected outcome: **Gap:**" in ln for ln in block):
                    outcome_gaps += 1
                lines.extend(block)
                lines.append("")
        if steps_sorted:
            lines.append("### Business Center UI path")
            lines.append("")
            for c in steps_sorted:
                step_no += 1
                sequence_len += 1
                doc = _doc_name(c)
                action = re.sub(r"\{#[^}]+\}", "", c["text"]).strip()
                outcome = _expected_outcome(action)
                if not outcome:
                    outcome_gaps += 1
                lines.append(f"{step_no}. **Action:** {action}")
                lines.append(f"   - Actor: {_actor_for_doc(doc)}")
                if outcome:
                    lines.append(f"   - Expected outcome: {outcome}")
                    lines.append("   - outcome_missing: false")
                else:
                    lines.append(
                        "   - Expected outcome: **Gap:** not stated in source."
                    )
                    lines.append("   - outcome_missing: true")
                lines.append(f"   - {_citation(c)}")
                lines.append("")

    # Stash counts for composition report consumers (HTML comment, machine-readable).
    # Denominator = this page's continuous API+UI sequence (recomputed each run).
    lines.append(
        f"<!-- sequence_stats: steps={sequence_len} outcome_gaps={outcome_gaps} "
        f"outcome_missing={outcome_gaps} "
        f"api_ops={len(endpoints)} ui_steps={len(steps_sorted)} -->"
    )

    lines += ["", "## Constraints", ""]
    if constraints:
        for c in constraints:
            kind = c.get("extras", {}).get("claim_kind")
            body = re.sub(r"\{#[^}]+\}", "", c["text"]).strip()
            lines.append(f"- [{kind}] {body}  ")
            lines.append(f"  {_citation(c)} · {c['source_pointer']}")
    else:
        lines.append("- **Gap:** no constraint-kind claims found for this workflow.")
    lines += ["", "## Failure modes", ""]
    if errors:
        seen = set()
        for c in errors:
            t = re.sub(r"\{#[^}]+\}", "", c["text"]).strip()
            if _norm_text(t) in seen:
                continue
            seen.add(_norm_text(t))
            lines.append(f"- {t}  ")
            lines.append(f"  {_citation(c)} · {c['source_pointer']}")
    else:
        lines.append(
            "- **Gap:** no error cases documented for this workflow in the source docs."
        )
    lines += ["", FACTS_CLOSE, ""]
    return "\n".join(lines)


def compose_all(
    claims_file: Path,
    *,
    out_dir: Path,
    workflows: Sequence[WorkflowSpec] = BOARDING_WORKFLOWS,
) -> Dict[str, Any]:
    payload = json.loads(claims_file.read_text(encoding="utf-8"))
    stamp = Path(payload["raw_dir"]).name
    claims = payload["claims"]
    kept, residuals = dedupe_prefer_child(claims)

    out_dir.mkdir(parents=True, exist_ok=True)
    pages: List[Dict[str, Any]] = []
    total_steps = 0
    total_outcome_gaps = 0
    total_api = 0
    total_ui = 0
    for spec in workflows:
        md = compose_workflow_page(spec, kept, stamp=stamp)
        path = out_dir / f"{spec.workflow_id}.md"
        path.write_text(md, encoding="utf-8")
        m = re.search(
            r"<!-- sequence_stats: steps=(\d+) outcome_gaps=(\d+) "
            r"(?:outcome_missing=(\d+) )?"
            r"api_ops=(\d+) ui_steps=(\d+) -->",
            md,
        )
        if m:
            n_steps = int(m.group(1))
            n_og = int(m.group(2))
            # groups: 1 steps, 2 outcome_gaps, 3 outcome_missing?, 4 api, 5 ui
            n_api = int(m.group(4))
            n_ui = int(m.group(5))
        else:
            n_steps = md.count("**Action:**") + md.count("**API:**")
            n_og = md.count("outcome_missing: true")
            n_api = md.count("**API:**")
            n_ui = md.count("**Action:**")
        n_flag = md.count("outcome_missing: true")
        total_steps += n_steps
        total_outcome_gaps += n_og
        total_api += n_api
        total_ui += n_ui
        pages.append(
            {
                "workflow_id": spec.workflow_id,
                "path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
                "steps": n_steps,
                "outcome_gaps": n_og,
                "outcome_missing": n_flag,
                "api_ops": n_api,
                "ui_steps": n_ui,
                "gaps": md.count("**Gap:**"),
            }
        )

    return {
        "claims_total": len(claims),
        "claims_after_prefer_child": len(kept),
        "mega_residuals": len(residuals),
        "sequence_totals": {
            "steps": total_steps,
            "outcome_gaps": total_outcome_gaps,
            "outcome_missing": sum(p["outcome_missing"] for p in pages),
            "api_ops": total_api,
            "ui_steps": total_ui,
            "ratio": (
                f"{total_outcome_gaps}/{total_steps}" if total_steps else "0/0"
            ),
            "denominator_source": (
                "composed workflow sequence (API ops + UI steps); "
                "recounted each compose from outcome_missing flags — "
                "not the stale 222/277 headline in gap-report.md"
            ),
            "note": (
                "LLM proposal cited 222/277 from gap-report.md headline; "
                "wave-rerun measured 215/278. Live number is recomputed here."
            ),
        },
        "mega_residual_samples": [
            {
                "claim_id": c["claim_id"],
                "schema": c["schema"],
                "text": c["text"][:120],
            }
            for c in residuals[:15]
        ],
        "pages": pages,
    }
