"""Parse frozen OpenAPI fixtures into contract_entity objects.

No network. Local fixtures only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from content_bench.content_engine.schemas import ContractEntity, SourceRecord, SourceSnapshot
from content_bench.content_engine.snapshot import read_snapshot_text
from content_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "artifacts" / "content_engine" / "contracts"

# Root object properties + one further recurse into nested objects
# (e.g. orderInformation.amountDetails.totalAmount).
_MAX_OBJECT_DEPTH = 2


def _ref_name(ref: str) -> str:
    if not ref:
        return ""
    return ref.rsplit("/", 1)[-1]


def _schema_refs_from_content(content: Dict[str, Any]) -> List[str]:
    refs: List[str] = []
    if not isinstance(content, dict):
        return refs
    for _mime, body in content.items():
        if not isinstance(body, dict):
            continue
        schema = body.get("schema") or {}
        ref = schema.get("$ref")
        if ref:
            refs.append(_ref_name(ref))
    return refs


def resolve_schema(
    schema: Dict[str, Any],
    components: Dict[str, Any],
) -> Dict[str, Any]:
    """Resolve a local #/components/schemas/* $ref (one hop)."""
    if not isinstance(schema, dict):
        return {}
    ref = schema.get("$ref")
    if not ref:
        return schema
    name = _ref_name(ref)
    resolved = (components.get("schemas") or {}).get(name)
    if isinstance(resolved, dict):
        return resolved
    return schema


def flatten_schema_fields(
    schema: Dict[str, Any],
    components: Dict[str, Any],
    *,
    prefix: str = "",
    depth: int = 0,
    max_depth: int = _MAX_OBJECT_DEPTH,
) -> List[Dict[str, Any]]:
    """Flatten object schema properties for docs tables.

    - Emit each property (name, type, required, description, enum).
    - When a property is an object with its own properties, recurse one further
      level (up to max_depth), prefixing names with dots.
    """
    resolved = resolve_schema(schema, components)
    props = resolved.get("properties") or {}
    if not isinstance(props, dict) or not props:
        return []

    required = set(resolved.get("required") or [])
    fields: List[Dict[str, Any]] = []

    for name, prop in props.items():
        if not isinstance(prop, dict):
            continue
        full_name = f"{prefix}.{name}" if prefix else name
        prop_resolved = resolve_schema(prop, components)
        nested_props = prop_resolved.get("properties")
        typ = prop_resolved.get("type") or prop.get("type")
        if not typ and nested_props:
            typ = "object"
        if not typ and prop_resolved.get("$ref"):
            typ = "object"

        if nested_props and isinstance(nested_props, dict) and depth < max_depth:
            fields.extend(
                flatten_schema_fields(
                    prop_resolved,
                    components,
                    prefix=full_name,
                    depth=depth + 1,
                    max_depth=max_depth,
                )
            )
            continue

        field: Dict[str, Any] = {
            "name": full_name,
            "type": typ or "string",
            "required": name in required,
            "description": str(
                prop_resolved.get("description") or prop.get("description") or ""
            ),
            "constraints": [],
        }
        enum_vals = prop_resolved.get("enum") or prop.get("enum")
        if enum_vals:
            field["enum"] = list(enum_vals)
            field["constraints"] = [f"enum: {', '.join(str(v) for v in enum_vals)}"]
        fields.append(field)

    return fields


def _fields_from_content(
    content: Dict[str, Any],
    components: Dict[str, Any],
) -> List[Dict[str, Any]]:
    fields: List[Dict[str, Any]] = []
    if not isinstance(content, dict):
        return fields
    for _mime, body in content.items():
        if not isinstance(body, dict):
            continue
        schema = body.get("schema") or {}
        fields.extend(flatten_schema_fields(schema, components))
    # De-dupe by name, keep first
    seen = set()
    unique: List[Dict[str, Any]] = []
    for f in fields:
        key = f.get("name")
        if key in seen:
            continue
        seen.add(key)
        unique.append(f)
    return unique


def parse_openapi_entities(
    record: SourceRecord,
    snapshot: SourceSnapshot,
) -> List[ContractEntity]:
    raw = json.loads(read_snapshot_text(snapshot))
    if str(raw.get("openapi", "")).startswith("3.") is False and "swagger" not in raw:
        # Still allow fixtures that omit strict openapi key if paths exist.
        if "paths" not in raw:
            raise ValueError("Fixture is not a recognizable OpenAPI document")

    components = raw.get("components") or {}
    security_schemes = list(components.get("securitySchemes") or {})
    global_auth = []
    for item in raw.get("security") or []:
        if isinstance(item, dict):
            global_auth.extend(item.keys())
    if not global_auth:
        global_auth = security_schemes

    service_name = str((raw.get("info") or {}).get("title") or record.source_id)
    entities: List[ContractEntity] = []

    for path, methods in (raw.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.lower() not in {
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "head",
                "options",
            }:
                continue
            if not isinstance(op, dict):
                continue
            operation_id = str(op.get("operationId") or f"{method}_{path}").strip()
            entity_id = f"{record.source_id}:{operation_id}"

            request_content = ((op.get("requestBody") or {}).get("content") or {})
            request_refs = _schema_refs_from_content(request_content)
            request_fields = _fields_from_content(request_content, components)

            response_refs: List[str] = []
            error_refs: List[str] = []
            response_fields: List[Dict[str, Any]] = []
            for code, resp in (op.get("responses") or {}).items():
                resp_content = (resp or {}).get("content") or {}
                refs = _schema_refs_from_content(resp_content)
                if str(code).startswith("2"):
                    response_refs.extend(refs)
                    response_fields.extend(_fields_from_content(resp_content, components))
                else:
                    error_refs.extend(refs)

            op_auth = []
            for item in op.get("security") or []:
                if isinstance(item, dict):
                    op_auth.extend(item.keys())
            auth = op_auth or list(global_auth)

            entities.append(
                ContractEntity(
                    entity_id=entity_id,
                    product=list(record.product),
                    service_name=service_name,
                    endpoint=str(path),
                    http_method=method.upper(),
                    operation_id=operation_id,
                    auth_schemes=auth,
                    request_schema_refs=sorted(set(request_refs)),
                    response_schema_refs=sorted(set(response_refs)),
                    error_schema_refs=sorted(set(error_refs)),
                    tags=list(op.get("tags") or []),
                    examples=[],
                    summary=str(op.get("summary") or ""),
                    description=str(op.get("description") or ""),
                    request_fields=request_fields,
                    response_fields=response_fields,
                )
            )

    entities.sort(key=lambda e: (e.endpoint, e.http_method, e.operation_id))
    return entities


def write_entities(
    source_id: str,
    entities: List[ContractEntity],
    snapshot: SourceSnapshot,
) -> Path:
    CONTRACT_DIR.mkdir(parents=True, exist_ok=True)
    path = CONTRACT_DIR / f"{source_id}.entities.json"
    payload = {
        "stage": "specs_to_docs_parse",
        "source_id": source_id,
        "snapshot_id": snapshot.snapshot_id,
        "content_hash": snapshot.content_hash,
        "entity_count": len(entities),
        "entities": [e.to_dict() for e in entities],
        "honest_label": {
            "network": "denied",
            "fixture": "local-openapi",
            "note": "Not a live Payment Gateway OpenAPI download",
        },
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    _ = repo_relative(path)
    return path
