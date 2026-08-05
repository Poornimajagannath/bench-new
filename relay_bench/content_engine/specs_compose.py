"""Compose api_reference_unit drafts and eval seeds from contract entities."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from relay_bench.content_engine.schemas import (
    ApiReferenceUnit,
    ContractEntity,
    SourceRecord,
)
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
GENERATED_DIR = ROOT / "artifacts" / "content_engine" / "generated"


def compose_reference_units(
    record: SourceRecord,
    entities: List[ContractEntity],
) -> List[ApiReferenceUnit]:
    units: List[ApiReferenceUnit] = []
    for entity in entities:
        path_params = []
        for part in entity.endpoint.split("/"):
            if part.startswith("{") and part.endswith("}"):
                name = part[1:-1]
                path_params.append(
                    {
                        "name": name,
                        "type": "string",
                        "required": True,
                        "description": f"Path parameter {name}",
                    }
                )

        request_fields = [
            {
                "name": ref,
                "type": "object",
                "required": True,
                "constraints": [],
            }
            for ref in entity.request_schema_refs
        ]
        response_fields = [
            {
                "name": ref,
                "type": "object",
                "description": f"Success schema {ref}",
            }
            for ref in entity.response_schema_refs
        ]
        error_cases = [
            {
                "code": "error_schema",
                "meaning": f"Error payload shaped by {ref}",
                "recovery": "Inspect reason/details; fix request or auth; retry in sandbox only",
            }
            for ref in entity.error_schema_refs
        ]
        if not error_cases:
            error_cases = [
                {
                    "code": "unspecified",
                    "meaning": "No explicit error schema in fixture",
                    "recovery": "Treat non-2xx as failure; do not log secrets",
                }
            ]

        evidence = []
        if entity.summary:
            evidence.append(entity.summary)
        if entity.description:
            evidence.append(entity.description[:180])
        if not evidence:
            evidence.append(f"{entity.http_method} {entity.endpoint}")

        workflows = []
        if record.linked_workflow_id:
            workflows.append(record.linked_workflow_id)
        # Lightweight tag → workflow hint
        tag_blob = " ".join(entity.tags).lower()
        if "mpp" in tag_blob or "authentication" in (entity.summary + entity.description).lower():
            workflows.append("microform-payer-auth-state-machine")
        workflows = sorted(set(workflows))

        units.append(
            ApiReferenceUnit(
                unit_id=f"{record.source_id}:ref:{entity.operation_id}",
                doc_id=f"doc-{record.source_id}",
                api_name=entity.service_name,
                endpoint=entity.endpoint,
                http_method=entity.http_method,
                summary=entity.summary or entity.operation_id,
                auth_requirements=list(entity.auth_schemes)
                or ["httpSignature-via-env-vars"],
                path_params=path_params,
                query_params=[],
                request_fields=request_fields,
                response_fields=response_fields,
                error_cases=error_cases,
                workflows=workflows,
                code_examples=[],
                evidence_quotes=evidence,
                operation_id=entity.operation_id,
                lineage_origin="generated_from_spec",
            )
        )
    return units


def compose_eval_seeds(
    record: SourceRecord,
    entities: List[ContractEntity],
) -> List[Dict[str, Any]]:
    seeds: List[Dict[str, Any]] = []
    for entity in entities:
        seeds.append(
            {
                "seed_id": f"{entity.operation_id}-happy-path",
                "kind": "happy_path",
                "operation_id": entity.operation_id,
                "user_query": f"Call {entity.http_method} {entity.endpoint} successfully in sandbox",
                "expected_doc_types": ["api_reference", "quickstart"],
                "success_criteria": [
                    "Uses sandbox host only",
                    "Does not include raw PAN or secrets",
                    "Mentions required auth scheme",
                ],
            }
        )
        if entity.auth_schemes:
            seeds.append(
                {
                    "seed_id": f"{entity.operation_id}-missing-auth",
                    "kind": "missing_auth",
                    "operation_id": entity.operation_id,
                    "user_query": f"What happens if auth is missing for {entity.operation_id}?",
                    "expected_doc_types": ["api_reference", "auth_guide"],
                    "success_criteria": [
                        "Identifies required auth scheme",
                        "Does not invent credential values",
                    ],
                }
            )
        if entity.error_schema_refs:
            seeds.append(
                {
                    "seed_id": f"{entity.operation_id}-error-recovery",
                    "kind": "error_recovery",
                    "operation_id": entity.operation_id,
                    "user_query": f"How do I recover from errors on {entity.operation_id}?",
                    "expected_doc_types": ["api_reference", "troubleshooting"],
                    "success_criteria": [
                        "References error schema or status handling",
                        "Keeps recovery support-safe",
                    ],
                }
            )
    return seeds


def compose_quickstart_hints(
    record: SourceRecord,
    units: List[ApiReferenceUnit],
) -> List[Dict[str, Any]]:
    hints = []
    for unit in units:
        hints.append(
            {
                "operation_id": unit.operation_id,
                "endpoint": unit.endpoint,
                "http_method": unit.http_method,
                "suggested_workflows": list(unit.workflows),
                "linked_quickstart_source": (
                    "microform-payer-auth-quickstart"
                    if "microform-payer-auth-state-machine" in unit.workflows
                    else None
                ),
                "note": "Hint only — OpenAPI alone does not author a full quickstart",
            }
        )
    return hints


def write_generated(
    source_id: str,
    units: List[ApiReferenceUnit],
    eval_seeds: List[Dict[str, Any]],
    hints: List[Dict[str, Any]],
) -> Tuple[Path, Path, Path]:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    units_path = GENERATED_DIR / f"{source_id}.api_reference_units.json"
    seeds_path = GENERATED_DIR / f"{source_id}.eval_seeds.json"
    hints_path = GENERATED_DIR / f"{source_id}.quickstart_hints.json"

    units_path.write_text(
        json.dumps(
            {
                "stage": "specs_to_docs_compose",
                "source_id": source_id,
                "lineage_origin": "generated_from_spec",
                "units": [u.to_dict() for u in units],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    seeds_path.write_text(
        json.dumps(
            {
                "stage": "specs_to_docs_eval_seeds",
                "source_id": source_id,
                "seeds": eval_seeds,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    hints_path.write_text(
        json.dumps(
            {
                "stage": "specs_to_docs_quickstart_hints",
                "source_id": source_id,
                "hints": hints,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    for p in (units_path, seeds_path, hints_path):
        _ = repo_relative(p)
    return units_path, seeds_path, hints_path
