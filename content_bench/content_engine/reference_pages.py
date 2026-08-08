"""A2: render api_reference_unit drafts into content/*.md pages."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content"
ARTIFACT_DIR = ROOT / "artifacts" / "content_engine" / "a2"


def default_units_path() -> Path:
    """Prefer registered payments OpenAPI units; fall back to local fixture units."""
    generated = ROOT / "artifacts" / "content_engine" / "generated"
    candidates: List[Path] = []
    payments = ROOT / "registry" / "payments.json"
    if payments.is_file():
        try:
            sid = json.loads(payments.read_text(encoding="utf-8")).get(
                "openapi_source_id"
            )
            if sid:
                candidates.append(generated / f"{sid}.api_reference_units.json")
        except json.JSONDecodeError:
            pass
    candidates.extend(
        [
            generated / "payments-core-openapi.api_reference_units.json",
            generated / "cybersource-payments-core-openapi.api_reference_units.json",
        ]
    )
    for path in candidates:
        if path.is_file():
            return path
    return candidates[0]


DEFAULT_UNITS_PATH = default_units_path()


def load_reference_units(path: Optional[Path] = None) -> List[Dict[str, Any]]:
    path = path or default_units_path()
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    units = data.get("units") or data.get("items") or []
    if not isinstance(units, list):
        raise ValueError(f"No units list in {path}")
    return units


def _field_table(rows: Sequence[Dict[str, Any]], kind: str) -> List[str]:
    if not rows:
        return ["_None listed_", ""]
    lines = ["| Name | Type | Required | Notes |", "| --- | --- | --- | --- |"]
    for row in rows:
        required = row.get("required")
        req = "" if required is None else ("yes" if required else "no")
        notes = row.get("description") or ", ".join(row.get("constraints") or []) or ""
        lines.append(
            f"| {row.get('name', '')} | {row.get('type', '')} | {req} | {notes} |"
        )
    lines.append("")
    return lines


def render_reference_page(unit: Dict[str, Any]) -> str:
    op = unit.get("operation_id") or "unknown"
    method = unit.get("http_method") or ""
    endpoint = unit.get("endpoint") or ""
    summary = unit.get("summary") or op
    auth = unit.get("auth_requirements") or []
    lineage = unit.get("lineage_origin") or "generated_from_spec"
    source = unit.get("doc_id") or "payments-core-openapi"

    lines: List[str] = [
        "---",
        f"title: {summary}",
        "generated: true",
        f"source: {source}",
        f"operation_id: {op}",
        f"lineage_origin: {lineage}",
        "---",
        "",
        f"# {summary}",
        "",
        "<!-- section:prose -->",
        "## Overview",
        "",
        f"You use this endpoint to {summary[0].lower() + summary[1:] if summary else 'call the API'}.",
        "",
        "<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->",
        "<!-- /section:prose -->",
        "",
        "<!-- section:facts -->",
        f"**Method:** `{method}`  ",
        f"**Path:** `{endpoint}`  ",
        f"**Operation ID:** `{op}`",
        "",
        "## Auth",
        "",
    ]
    platform_auth = any(
        "getting-started" in str(a).lower() or "http-signature-or-jwt" in str(a).lower()
        for a in auth
    )
    if auth and not platform_auth:
        lines.append(
            "Required scheme(s) from the OpenAPI security section: "
            + ", ".join(f"`{a}`" for a in auth)
            + "."
        )
    else:
        lines.append(
            "This OpenAPI document does not declare `security` / `securityDefinitions` "
            "for the operation. Authenticate with HTTP Signature or JWT per CyberSource "
            "REST getting started (sandbox: `apitest.cybersource.com`)."
        )
    # Safety: never encourage raw PAN even when field catalogs mention card data.
    req_names = " ".join(
        str(f.get("name") or "") for f in (unit.get("request_fields") or [])
    )
    if re.search(r"(?i)card\.number|paymentInformation\.card", req_names):
        lines.extend(
            [
                "",
                "## Safety",
                "",
                "Use tokenized instruments or sandbox test values only. "
                "Do not send raw PAN in production.",
            ]
        )
    lines.extend(["", "## Request", ""])

    path_params = unit.get("path_params") or []
    query_params = unit.get("query_params") or []
    if path_params:
        lines.append("### Path parameters")
        lines.append("")
        lines.extend(_field_table(path_params, "path"))
    if query_params:
        lines.append("### Query parameters")
        lines.append("")
        lines.extend(_field_table(query_params, "query"))
    lines.append("### Body fields")
    lines.append("")
    lines.extend(_field_table(unit.get("request_fields") or [], "body"))

    lines.extend(["## Response", ""])
    lines.extend(_field_table(unit.get("response_fields") or [], "response"))

    lines.extend(["## Errors", ""])
    errors = unit.get("error_cases") or []
    if not errors:
        lines.extend(["_None listed_", ""])
    else:
        for err in errors:
            lines.append(
                f"- `{err.get('code', '')}`: {err.get('meaning', '')} "
                f"— recovery: {err.get('recovery', '')}"
            )
        lines.append("")

    quotes = unit.get("evidence_quotes") or []
    lines.extend(["## Evidence (from spec)", ""])
    if quotes:
        for q in quotes:
            lines.append(f'> "{q}"')
            lines.append("")
    else:
        lines.extend(["_No evidence quotes attached._", ""])

    workflows = unit.get("workflows") or []
    if workflows:
        lines.extend(
            [
                "## Related workflows",
                "",
                ", ".join(f"`{w}`" for w in workflows),
                "",
            ]
        )

    lines.extend(
        [
            "## Provenance",
            "",
            f"- `lineage_origin`: `{lineage}`",
            f"- `unit_id`: `{unit.get('unit_id', '')}`",
            f"- `api_name`: {unit.get('api_name', '')}",
            "",
            "Every fact on this page traces to the OpenAPI-derived reference unit. "
            "Sandbox only — do not use production credentials from these docs.",
            "",
            "<!-- /section:facts -->",
            "",
        ]
    )
    return "\n".join(lines)


def page_filename(unit: Dict[str, Any]) -> str:
    op = unit.get("operation_id")
    if not op:
        raise ValueError(f"unit missing operation_id: {unit.get('unit_id')}")
    return f"{op}.md"


def _slug_op(method: str, path: str, anchor: str = "") -> str:
    base = anchor or f"{method}_{path}".strip("_")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", base).strip("_")
    return slug or "operation"


def endpoint_fact_to_unit(claim: Dict[str, Any]) -> Dict[str, Any]:
    """Project an endpoint_fact claim into the reference-page unit shape."""
    ex = claim.get("extras") or {}
    method = ex.get("method") or ""
    path = ex.get("path") or ""
    anchor = ex.get("anchor") or ""
    op_id = _slug_op(method, path, anchor)
    fields = []
    for f in ex.get("required_fields") or []:
        fields.append(
            {
                "name": f.get("name") or "",
                "type": "",
                "required": True,
                "description": f.get("instruction") or "",
                "constraints": [],
            }
        )
    examples = []
    if ex.get("example_request") is not None:
        examples.append({"label": "request", "body": ex.get("example_request")})
    if ex.get("example_response") is not None:
        examples.append({"label": "response", "body": ex.get("example_response")})
    return {
        "unit_id": claim.get("claim_id") or op_id,
        "operation_id": op_id,
        "http_method": method,
        "endpoint": path,
        "summary": claim.get("title") or f"{method} {path}",
        "auth_requirements": [],
        "path_params": [],
        "query_params": [],
        "request_fields": fields,
        "response_fields": [],
        "error_cases": [],
        "workflows": [],
        "code_examples": examples,
        "evidence_quotes": [],
        "lineage_origin": "generated_from_endpoint_fact",
        "doc_id": claim.get("source_pointer") or "",
        "api_name": "payments",
        "deep_link": ex.get("deep_link"),
        "host": ex.get("host"),
        "environment": ex.get("environment"),
    }


def render_endpoint_fact_page(unit: Dict[str, Any]) -> str:
    """Reference page rendered from a guide endpoint_fact (not the OpenAPI fixture)."""
    method = unit.get("http_method") or ""
    endpoint = unit.get("endpoint") or ""
    summary = unit.get("summary") or f"{method} {endpoint}"
    lineage = unit.get("lineage_origin") or "generated_from_endpoint_fact"
    source = unit.get("doc_id") or ""
    deep = unit.get("deep_link") or ""
    host = unit.get("host") or ""
    env = unit.get("environment") or ""

    lines: List[str] = [
        "---",
        f"title: {summary}",
        "generated: true",
        f"source: {source}",
        f"operation_id: {unit.get('operation_id')}",
        f"lineage_origin: {lineage}",
        "---",
        "",
        f"# {summary}",
        "",
        "<!-- section:prose -->",
        "## Overview",
        "",
        f"Guide-derived reference for `{method} {endpoint}`.",
        "",
        "<!-- /section:prose -->",
        "",
        "<!-- section:facts -->",
        f"**Method:** `{method}`  ",
        f"**Path:** `{endpoint}`  ",
    ]
    if host:
        label = f"{env} host" if env else "Host"
        lines.append(f"**{label}:** `{host}`  ")
    if deep:
        lines.append(f"**Source:** [{deep}]({deep})  ")
    lines.extend(["", "## Request body fields", ""])
    req = unit.get("request_fields") or []
    if not req:
        lines.extend(
            [
                "_**Gap:** no Required Fields list in the product-root guide for this endpoint._",
                "",
            ]
        )
    else:
        lines.extend(_field_table(req, "body"))

    examples = unit.get("code_examples") or []
    req_ex = next((e for e in examples if e.get("label") == "request"), None)
    resp_ex = next((e for e in examples if e.get("label") == "response"), None)
    lines.extend(["## Example request", ""])
    if req_ex and req_ex.get("body") is not None:
        lines.extend(["```json", str(req_ex["body"]), "```", ""])
    else:
        lines.extend(
            ["_**Gap:** no REST Example request in the product-root guide._", ""]
        )
    lines.extend(["## Example response", ""])
    if resp_ex and resp_ex.get("body") is not None:
        lines.extend(["```json", str(resp_ex["body"]), "```", ""])
    else:
        lines.extend(
            ["_**Gap:** no REST Example response in the product-root guide._", ""]
        )

    lines.extend(
        [
            "## Provenance",
            "",
            f"- `lineage_origin`: `{lineage}`",
            f"- `unit_id`: `{unit.get('unit_id', '')}`",
            f"- `claim source`: `{source}`",
            "",
            "Every fact on this page traces to an `endpoint_fact` extracted from "
            "the payments product root. Not the OpenAPI fixture path.",
            "",
            "<!-- /section:facts -->",
            "",
        ]
    )
    return "\n".join(lines)


def write_reference_pages(
    units: Optional[Sequence[Dict[str, Any]]] = None,
    *,
    content_dir: Path = CONTENT_DIR,
    artifact_dir: Path = ARTIFACT_DIR,
    clear_existing: bool = True,
    allow_endpoint_fact_lineage: bool = False,
) -> Dict[str, Any]:
    units = list(units if units is not None else load_reference_units())
    content_dir.mkdir(parents=True, exist_ok=True)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    if clear_existing:
        for stale in content_dir.glob("*.md"):
            if stale.name.lower() == "readme.md":
                continue
            # Keep boarding/ tree intact — only clear top-level reference pages.
            stale.unlink()

    written: List[str] = []
    lineage_set = set()
    for unit in units:
        lineage = unit.get("lineage_origin") or "generated_from_spec"
        lineage_set.add(lineage)
        if lineage == "generated_from_endpoint_fact":
            if not allow_endpoint_fact_lineage and units is None:
                raise ValueError("endpoint_fact lineage requires explicit units")
            name = page_filename(unit)
            path = content_dir / name
            path.write_text(render_endpoint_fact_page(unit), encoding="utf-8")
            written.append(name)
            continue
        if lineage != "generated_from_spec":
            raise ValueError(
                f"{unit.get('operation_id')}: expected lineage_origin=generated_from_spec, "
                f"got {lineage!r}"
            )
        name = page_filename(unit)
        path = content_dir / name
        path.write_text(render_reference_page(unit), encoding="utf-8")
        written.append(name)

    try:
        artifact_rel = str(artifact_dir.relative_to(ROOT))
    except ValueError:
        artifact_rel = str(artifact_dir)
    summary = {
        "ok": True,
        "pages_written": written,
        "count": len(written),
        "lineage_origin": sorted(lineage_set),
        "artifact_dir": artifact_rel,
    }
    (artifact_dir / "reference-pages-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def write_reference_pages_from_endpoint_facts(
    claims: Sequence[Dict[str, Any]],
    *,
    content_dir: Path = CONTENT_DIR,
    artifact_dir: Path = ARTIFACT_DIR,
    path_prefix: str = "/pts/",
) -> Dict[str, Any]:
    """Wave 1: publish payments reference pages from endpoint_fact claims."""
    selected = []
    seen = set()
    for c in claims:
        if c.get("schema") != "endpoint_fact":
            continue
        ex = c.get("extras") or {}
        path = ex.get("path") or ""
        if path_prefix and not path.startswith(path_prefix):
            continue
        # Prefer api_reference pattern + test host.
        key = f"{ex.get('anchor')}:{ex.get('method')}:{path}"
        prev = next((u for u in selected if u.get("_key") == key), None)
        unit = endpoint_fact_to_unit(c)
        unit["_key"] = key
        if prev is None:
            selected.append(unit)
            seen.add(key)
        elif ex.get("environment") == "test":
            selected = [u for u in selected if u.get("_key") != key] + [unit]
    for u in selected:
        u.pop("_key", None)
    return write_reference_pages(
        selected,
        content_dir=content_dir,
        artifact_dir=artifact_dir,
        clear_existing=True,
        allow_endpoint_fact_lineage=True,
    )
