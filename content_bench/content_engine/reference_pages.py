"""A2: render api_reference_unit drafts into content/*.md pages."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_UNITS_PATH = (
    ROOT
    / "artifacts"
    / "content_engine"
    / "generated"
    / "cybersource-payments-core-openapi.api_reference_units.json"
)
CONTENT_DIR = ROOT / "content"
ARTIFACT_DIR = ROOT / "artifacts" / "content_engine" / "a2"


def load_reference_units(path: Path = DEFAULT_UNITS_PATH) -> List[Dict[str, Any]]:
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
    if auth:
        lines.append(
            "Required scheme(s) from the OpenAPI fixture: "
            + ", ".join(f"`{a}`" for a in auth)
            + "."
        )
    else:
        lines.append("_Auth not stated in the reference unit._")
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


def write_reference_pages(
    units: Optional[Sequence[Dict[str, Any]]] = None,
    *,
    content_dir: Path = CONTENT_DIR,
    artifact_dir: Path = ARTIFACT_DIR,
) -> Dict[str, Any]:
    units = list(units if units is not None else load_reference_units())
    content_dir.mkdir(parents=True, exist_ok=True)
    artifact_dir.mkdir(parents=True, exist_ok=True)

    written: List[str] = []
    for unit in units:
        if unit.get("lineage_origin") and unit["lineage_origin"] != "generated_from_spec":
            raise ValueError(
                f"{unit.get('operation_id')}: expected lineage_origin=generated_from_spec, "
                f"got {unit.get('lineage_origin')!r}"
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
        "lineage_origin": "generated_from_spec",
        "artifact_dir": artifact_rel,
    }
    (artifact_dir / "reference-pages-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary
