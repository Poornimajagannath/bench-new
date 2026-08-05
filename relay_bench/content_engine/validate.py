"""Schema + content validation gates before promotion."""

from __future__ import annotations

import re
from typing import List, Tuple

from relay_bench.content_engine.schemas import QuickstartUnit, ValidationIssue

_SECRETISH = re.compile(
    r"(?i)\b(password\s*[:=]|merchantsecretkey\s*[:=]\s*\S+|shared[_-]?secret\s*[:=]\s*\S+)\b"
)
_RAW_CARDISH = re.compile(r"\b(?:\d[ -]*?){13,19}\b")

# Public CyberSource sandbox test PANs — allowed in lab docs.
_ALLOWED_TEST_PANS = {
    "4111111111111111",
    "4000000000000002",
    "5555555555554444",
}

ALLOWED_UNIT_TYPES = {
    "overview",
    "prerequisite",
    "credential",
    "dependency",
    "step",
    "decision",
    "code_sample",
    "validation_check",
    "warning",
    "troubleshooting",
    "next_step",
}


def validate_schema(units: List[QuickstartUnit]) -> Tuple[bool, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    if not units:
        issues.append(
            ValidationIssue(
                code="no_units",
                severity="error",
                message="Extractor produced zero quickstart units",
            )
        )
        return False, issues

    seen_ids = set()
    step_numbers = []
    for unit in units:
        if not unit.unit_id:
            issues.append(
                ValidationIssue("missing_unit_id", "error", "unit_id is required", None)
            )
        if unit.unit_id in seen_ids:
            issues.append(
                ValidationIssue(
                    "duplicate_unit_id",
                    "error",
                    f"duplicate unit_id {unit.unit_id}",
                    unit.unit_id,
                )
            )
        seen_ids.add(unit.unit_id)

        if unit.unit_type not in ALLOWED_UNIT_TYPES:
            issues.append(
                ValidationIssue(
                    "invalid_unit_type",
                    "error",
                    f"invalid unit_type {unit.unit_type}",
                    unit.unit_id,
                )
            )
        if not unit.title or not unit.goal:
            issues.append(
                ValidationIssue(
                    "missing_title_or_goal",
                    "error",
                    "title and goal are required",
                    unit.unit_id,
                )
            )
        if unit.unit_type == "step":
            step_numbers.append(unit.sequence_number)
            if unit.sequence_number < 1:
                issues.append(
                    ValidationIssue(
                        "invalid_sequence",
                        "error",
                        "step sequence_number must be >= 1",
                        unit.unit_id,
                    )
                )

    if step_numbers and len(step_numbers) != len(set(step_numbers)):
        issues.append(
            ValidationIssue(
                "duplicate_sequence",
                "error",
                "step sequence_number values must be unique",
            )
        )

    passed = not any(i.severity == "error" for i in issues)
    return passed, issues


def _contains_disallowed_pan(text: str) -> bool:
    for match in _RAW_CARDISH.finditer(text):
        digits = re.sub(r"\D", "", match.group(0))
        if digits not in _ALLOWED_TEST_PANS:
            return True
    return False


def validate_content(units: List[QuickstartUnit]) -> Tuple[bool, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []
    steps = [u for u in units if u.unit_type == "step"]
    if not steps:
        grounded = [u for u in units if u.evidence_quotes]
        if grounded:
            issues.append(
                ValidationIssue(
                    "no_steps",
                    "warning",
                    "no step units; promoting reference-style units with evidence",
                )
            )
        else:
            issues.append(
                ValidationIssue(
                    "no_steps",
                    "error",
                    "must include at least one step unit or grounded reference unit",
                )
            )

    check_units = steps or units
    for unit in check_units:
        if not unit.evidence_quotes:
            issues.append(
                ValidationIssue(
                    "missing_evidence",
                    "error",
                    "units require evidence_quotes for grounding",
                    unit.unit_id,
                )
            )
        if unit.unit_type == "step" and not unit.requires:
            issues.append(
                ValidationIssue(
                    "missing_requires",
                    "warning",
                    "step has no requires dependencies",
                    unit.unit_id,
                )
            )

        blob = " ".join(
            [unit.title, unit.body_markdown, " ".join(unit.evidence_quotes)]
        )
        if _SECRETISH.search(blob) or _contains_disallowed_pan(blob):
            issues.append(
                ValidationIssue(
                    "secret_or_pan_material",
                    "error",
                    "unit appears to contain secret or non-test PAN-like material",
                    unit.unit_id,
                )
            )

    # Sequence integrity: sorted step numbers should be contiguous-ish starting at 1.
    nums = sorted(u.sequence_number for u in steps)
    if nums and nums[0] != 1:
        issues.append(
            ValidationIssue(
                "sequence_must_start_at_1",
                "error",
                f"first step sequence_number is {nums[0]}, expected 1",
            )
        )
    for prev, cur in zip(nums, nums[1:]):
        if cur < prev:
            issues.append(
                ValidationIssue(
                    "sequence_out_of_order",
                    "error",
                    "step sequence_number values are not ordered",
                )
            )
            break

    passed = not any(i.severity == "error" for i in issues)
    return passed, issues
