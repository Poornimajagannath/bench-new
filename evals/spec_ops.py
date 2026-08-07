"""Runtime operation lists from the registered payments OpenAPI — no hard-coding."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.registry import (  # noqa: E402
    load_registry,
    require_source,
)

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def payments_openapi_source_id(
    registry_path: Optional[Path] = None,
) -> str:
    """Prefer registry/payments.json openapi_source_id; else first trusted openapi."""
    payments_file = ROOT / "registry" / "payments.json"
    if payments_file.is_file():
        raw = json.loads(payments_file.read_text(encoding="utf-8"))
        sid = raw.get("openapi_source_id")
        if sid:
            return str(sid)
    records = load_registry(registry_path)
    for rec in records.values():
        if not rec.enabled:
            continue
        if rec.source_type != "openapi":
            continue
        if "payments" not in [p.lower() for p in rec.product]:
            continue
        if rec.refresh_cadence == "manual-fixture":
            continue
        return rec.source_id
    raise LookupError("No non-fixture payments OpenAPI source in registry")


def load_openapi_document(source_id: Optional[str] = None) -> Tuple[str, Path, Dict[str, Any]]:
    sid = source_id or payments_openapi_source_id()
    record = require_source(sid)
    path = ROOT / record.repo_path
    if not path.is_file():
        raise FileNotFoundError(f"OpenAPI missing for {sid}: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    return sid, path, data


def list_operations(
    source_id: Optional[str] = None,
    *,
    exclude: Optional[Sequence[str]] = None,
) -> List[Dict[str, str]]:
    """Return [{operation_id, method, path}, ...] from the registered spec."""
    sid, _path, data = load_openapi_document(source_id)
    blocked = {x for x in (exclude or []) if x}
    # Optional deliberate exclusions file next to evidence
    excl_path = ROOT / "data" / "content_engine" / "payments_op_exclusions.json"
    if excl_path.is_file():
        excl_data = json.loads(excl_path.read_text(encoding="utf-8"))
        for item in excl_data.get("exclude_operation_ids") or []:
            blocked.add(str(item))

    ops: List[Dict[str, str]] = []
    for path, methods in (data.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            op_id = str(op.get("operationId") or f"{method}_{path}").strip()
            if op_id in blocked:
                continue
            ops.append(
                {
                    "source_id": sid,
                    "operation_id": op_id,
                    "method": method.upper(),
                    "path": str(path),
                    "summary": str(op.get("summary") or ""),
                }
            )
    ops.sort(key=lambda o: (o["path"], o["method"], o["operation_id"]))
    return ops


def operation_ids(source_id: Optional[str] = None) -> List[str]:
    return [o["operation_id"] for o in list_operations(source_id)]


def auth_schemes_for_operation(
    operation_id: str,
    source_id: Optional[str] = None,
) -> List[str]:
    sid, _path, data = load_openapi_document(source_id)
    global_auth: List[str] = []
    for item in data.get("security") or []:
        if isinstance(item, dict):
            global_auth.extend(item.keys())
    schemes = data.get("securityDefinitions") or (data.get("components") or {}).get(
        "securitySchemes"
    ) or {}
    if not global_auth and isinstance(schemes, dict):
        global_auth = list(schemes.keys())

    for path, methods in (data.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if not isinstance(op, dict):
                continue
            if str(op.get("operationId") or "") != operation_id:
                continue
            op_auth: List[str] = []
            for item in op.get("security") or []:
                if isinstance(item, dict):
                    op_auth.extend(item.keys())
            return op_auth or list(global_auth)
    return list(global_auth)


def exclusion_report(source_id: Optional[str] = None) -> Dict[str, Any]:
    excl_path = ROOT / "data" / "content_engine" / "payments_op_exclusions.json"
    if not excl_path.is_file():
        return {
            "exclude_operation_ids": [],
            "notes": "No deliberate exclusions file; all ops in registered spec are in scope.",
            "path": None,
        }
    data = json.loads(excl_path.read_text(encoding="utf-8"))
    data["path"] = str(excl_path.relative_to(ROOT))
    return data


def eval_seeds_path(source_id: Optional[str] = None) -> Path:
    sid = source_id or payments_openapi_source_id()
    return (
        ROOT
        / "artifacts"
        / "content_engine"
        / "generated"
        / f"{sid}.eval_seeds.json"
    )
