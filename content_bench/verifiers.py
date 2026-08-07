"""Stable Bench-inspired verifier over simulated fixtures.

V0 does NOT import or depend on `tempo-evals`, Harbor, Docker isolation,
or the Stable Bench task/runtime format. This is a local deterministic
prototype inspired by oracle/verifier separation patterns from
tempoxyz/tempo-evals (Stable Bench).

Stage boundary: HiddenTruth (+ optional candidate answer) → VerifierResult.
No network.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from content_bench.schemas import CheckResult, HiddenTruth, VerifierResult

ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "artifacts" / "verifier_results"


def _eval_check(check: Dict[str, Any], answer: Dict[str, Any]) -> CheckResult:
    check_id = str(check["check_id"])
    field = str(check["field"])
    actual = answer.get(field)

    if "expected" in check:
        expected = check["expected"]
        passed = actual == expected
        detail = f"{field}: expected={expected!r} actual={actual!r}"
        return CheckResult(check_id=check_id, passed=passed, detail=detail, private=True)

    if "contains" in check:
        needle = check["contains"]
        passed = isinstance(actual, list) and needle in actual
        detail = f"{field} contains {needle!r}: {passed}"
        return CheckResult(check_id=check_id, passed=passed, detail=detail, private=True)

    if "contains_all" in check:
        needles = list(check["contains_all"])
        passed = isinstance(actual, list) and all(n in actual for n in needles)
        detail = f"{field} contains_all {needles!r}: {passed}"
        return CheckResult(check_id=check_id, passed=passed, detail=detail, private=True)

    return CheckResult(
        check_id=check_id,
        passed=False,
        detail=f"Unknown check shape for {check_id}",
        private=True,
    )


def verify_answer(
    hidden: HiddenTruth,
    answer: Dict[str, Any],
    subject: str,
) -> VerifierResult:
    checks = [_eval_check(c, answer) for c in hidden.verifier_private_checks]
    failed = [c.check_id for c in checks if not c.passed]
    return VerifierResult(
        workflow_id=hidden.workflow_id,
        subject=subject,
        passed=len(failed) == 0,
        checks=checks,
        caught_failures=failed,
    )


def bad_answer_probe_passed(hidden: HiddenTruth, caught_failures: List[str]) -> bool:
    """Bad-answer probe succeeds only when the full expected failure set is caught."""
    expected = set(hidden.expected_bad_failure_ids)
    if not expected:
        return False
    return expected.issubset(set(caught_failures))


def missing_expected_failures(hidden: HiddenTruth, caught_failures: List[str]) -> List[str]:
    return sorted(set(hidden.expected_bad_failure_ids) - set(caught_failures))


def verify_bad_answer(hidden: HiddenTruth) -> VerifierResult:
    """Prove the verifier catches the full expected bad-answer failure set."""
    result = verify_answer(hidden, hidden.bad_answer, subject="bad_answer")
    passed = bad_answer_probe_passed(hidden, result.caught_failures)
    return VerifierResult(
        workflow_id=result.workflow_id,
        subject="bad_answer",
        passed=passed,
        checks=result.checks,
        caught_failures=result.caught_failures,
    )


def verify_oracle(hidden: HiddenTruth) -> VerifierResult:
    return verify_answer(hidden, hidden.oracle_answer, subject="oracle_answer")


def run_stable_bench_inspired_verification(hidden: HiddenTruth) -> Dict[str, VerifierResult]:
    """Run oracle (must pass) and bad-answer (must catch full expected set) probes."""
    oracle = verify_oracle(hidden)
    bad = verify_bad_answer(hidden)
    if not oracle.passed:
        raise AssertionError(
            f"Oracle failed verification for {hidden.workflow_id}: {oracle.caught_failures}"
        )
    if not bad.passed:
        missing = missing_expected_failures(hidden, bad.caught_failures)
        raise AssertionError(
            f"Verifier failed to catch full expected bad-answer set for "
            f"{hidden.workflow_id}: missing={missing} caught={bad.caught_failures} "
            f"expected={list(hidden.expected_bad_failure_ids)}"
        )
    return {"oracle_answer": oracle, "bad_answer": bad}


def write_verifier_results(
    workflow_id: str,
    results: Dict[str, VerifierResult],
) -> Path:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULT_DIR / f"{workflow_id}.result.json"
    payload = {
        "stage": "stable_bench_inspired_verifier",
        "inspired_by": "tempoxyz/tempo-evals Stable Bench (not imported in V0)",
        "workflow_id": workflow_id,
        "results": {k: v.to_dict() for k, v in results.items()},
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path
