"""Schema, content, and contract-alignment gates for specs-to-docs."""

from __future__ import annotations

from typing import List, Tuple

from relay_bench.content_engine.schemas import (
    ApiReferenceUnit,
    ContractEntity,
    ValidationIssue,
)


def validate_units_schema(
    units: List[ApiReferenceUnit],
) -> Tuple[bool, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    if not units:
        issues.append(
            ValidationIssue("no_units", "error", "No api_reference_unit drafts produced")
        )
        return False, issues

    seen = set()
    for unit in units:
        if not unit.unit_id or not unit.operation_id:
            issues.append(
                ValidationIssue(
                    "missing_ids",
                    "error",
                    "unit_id and operation_id are required",
                    unit.unit_id,
                )
            )
        if unit.unit_id in seen:
            issues.append(
                ValidationIssue(
                    "duplicate_unit_id",
                    "error",
                    f"duplicate unit_id {unit.unit_id}",
                    unit.unit_id,
                )
            )
        seen.add(unit.unit_id)
        if not unit.endpoint or not unit.http_method:
            issues.append(
                ValidationIssue(
                    "missing_endpoint",
                    "error",
                    "endpoint and http_method are required",
                    unit.unit_id,
                )
            )
        if not unit.auth_requirements:
            issues.append(
                ValidationIssue(
                    "missing_auth",
                    "error",
                    "auth_requirements required for reference units",
                    unit.unit_id,
                )
            )
        if not unit.evidence_quotes:
            issues.append(
                ValidationIssue(
                    "missing_evidence",
                    "error",
                    "evidence_quotes required",
                    unit.unit_id,
                )
            )

    return (not any(i.severity == "error" for i in issues), issues)


def validate_units_content(
    units: List[ApiReferenceUnit],
) -> Tuple[bool, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    banned = ("shared_secret_value", "merchantsecretkey=", "4111111111111111")
    for unit in units:
        blob = json_safe(unit)
        lower = blob.lower()
        for token in banned:
            if token in lower:
                issues.append(
                    ValidationIssue(
                        "secret_or_pan_material",
                        "error",
                        "generated unit appears to contain secret/PAN material",
                        unit.unit_id,
                    )
                )
        if not unit.error_cases:
            issues.append(
                ValidationIssue(
                    "missing_error_cases",
                    "error",
                    "reference unit missing error_cases",
                    unit.unit_id,
                )
            )
        if unit.lineage_origin != "generated_from_spec":
            issues.append(
                ValidationIssue(
                    "bad_lineage",
                    "error",
                    "expected lineage_origin=generated_from_spec",
                    unit.unit_id,
                )
            )
    return (not any(i.severity == "error" for i in issues), issues)


def validate_contract_alignment(
    entities: List[ContractEntity],
    units: List[ApiReferenceUnit],
) -> Tuple[bool, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    by_op = {e.operation_id: e for e in entities}
    unit_ops = {u.operation_id: u for u in units}

    missing = sorted(set(by_op) - set(unit_ops))
    extra = sorted(set(unit_ops) - set(by_op))
    for op in missing:
        issues.append(
            ValidationIssue(
                "missing_generated_unit",
                "error",
                f"No api_reference_unit for operation_id={op}",
            )
        )
    for op in extra:
        issues.append(
            ValidationIssue(
                "orphan_generated_unit",
                "error",
                f"api_reference_unit has no contract_entity for operation_id={op}",
                unit_ops[op].unit_id,
            )
        )

    for op, entity in by_op.items():
        unit = unit_ops.get(op)
        if unit is None:
            continue
        if unit.endpoint != entity.endpoint or unit.http_method != entity.http_method:
            issues.append(
                ValidationIssue(
                    "endpoint_mismatch",
                    "error",
                    "generated unit endpoint/method drifted from contract entity",
                    unit.unit_id,
                )
            )
        if sorted(unit.auth_requirements) != sorted(entity.auth_schemes) and entity.auth_schemes:
            # Allow composer fallback only when entity has no schemes.
            issues.append(
                ValidationIssue(
                    "auth_mismatch",
                    "error",
                    "auth_requirements drifted from contract entity",
                    unit.unit_id,
                )
            )

    return (not any(i.severity == "error" for i in issues), issues)


def json_safe(unit: ApiReferenceUnit) -> str:
    import json

    return json.dumps(unit.to_dict())
