"""Parse frozen OpenAPI fixtures into contract_entity objects.

No network. Local fixtures only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from relay_bench.content_engine.schemas import ContractEntity, SourceRecord, SourceSnapshot
from relay_bench.content_engine.snapshot import read_snapshot_text
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "artifacts" / "content_engine" / "contracts"


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


def parse_openapi_entities(
    record: SourceRecord,
    snapshot: SourceSnapshot,
) -> List[ContractEntity]:
    raw = json.loads(read_snapshot_text(snapshot))
    if str(raw.get("openapi", "")).startswith("3.") is False and "swagger" not in raw:
        # Still allow fixtures that omit strict openapi key if paths exist.
        if "paths" not in raw:
            raise ValueError("Fixture is not a recognizable OpenAPI document")

    security_schemes = list((raw.get("components") or {}).get("securitySchemes") or {})
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

            request_refs = _schema_refs_from_content(
                ((op.get("requestBody") or {}).get("content") or {})
            )
            response_refs: List[str] = []
            error_refs: List[str] = []
            for code, resp in (op.get("responses") or {}).items():
                refs = _schema_refs_from_content((resp or {}).get("content") or {})
                if str(code).startswith("2"):
                    response_refs.extend(refs)
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
            "note": "Not a live CyberSource OpenAPI download",
        },
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    _ = repo_relative(path)
    return path
