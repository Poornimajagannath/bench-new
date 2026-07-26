import unittest
from dataclasses import replace

from relay_bench.discovery import discover_workflows
from relay_bench.task_pack import build_hidden_truth
from relay_bench.verifiers import (
    bad_answer_probe_passed,
    run_tempo_verification,
    verify_answer,
    verify_bad_answer,
    verify_oracle,
)

# Exact failure sets the known-bad answer must trigger per workflow.
EXPECTED_BAD_FAILURES = {
    "flex-token-lifecycle": [
        "no_persist_transient",
        "uses_flex_to_tms_path",
        "creates_permanent_instrument",
        "stage_order_includes_validate",
    ],
    "http-signature-debug": [
        "sdk_field_names",
        "sandbox_host",
        "signed_headers_complete",
    ],
    "microform-payer-auth-state-machine": [
        "enrollment_present",
        "dual_path_handling",
        "auth_refs_on_payment",
        "state_machine_complete",
    ],
}


class VerifierTests(unittest.TestCase):
    def test_oracle_passes_and_bad_answer_caught_for_all_workflows(self):
        for candidate in discover_workflows():
            with self.subTest(workflow=candidate.workflow_id):
                hidden = build_hidden_truth(candidate)
                oracle = verify_oracle(hidden)
                bad = verify_bad_answer(hidden)
                self.assertTrue(oracle.passed, oracle.caught_failures)
                self.assertTrue(bad.passed, "verifier should catch full expected bad set")
                self.assertEqual(
                    sorted(bad.caught_failures),
                    sorted(EXPECTED_BAD_FAILURES[candidate.workflow_id]),
                )
                self.assertEqual(
                    sorted(hidden.expected_bad_failure_ids),
                    sorted(EXPECTED_BAD_FAILURES[candidate.workflow_id]),
                )

    def test_exact_bad_failures_per_workflow(self):
        for workflow_id, expected in EXPECTED_BAD_FAILURES.items():
            with self.subTest(workflow=workflow_id):
                candidate = discover_workflows(workflow_id=workflow_id)[0]
                hidden = build_hidden_truth(candidate)
                bad = verify_bad_answer(hidden)
                self.assertEqual(sorted(bad.caught_failures), sorted(expected))
                self.assertTrue(bad.passed)

    def test_partial_near_oracle_does_not_pass_bad_answer_probe(self):
        """Regression: catching only one failure must not report bad_answer_caught."""
        candidate = discover_workflows(workflow_id="microform-payer-auth-state-machine")[0]
        hidden = build_hidden_truth(candidate)
        near_oracle = dict(hidden.oracle_answer)
        near_oracle["runs_enrollment_check"] = False

        partial = verify_answer(hidden, near_oracle, subject="candidate")
        self.assertEqual(partial.caught_failures, ["enrollment_present"])
        self.assertFalse(
            bad_answer_probe_passed(hidden, partial.caught_failures),
            "partial catch must fail the bad-answer probe",
        )

        # Even if we temporarily treat that near-oracle as the bad_answer fixture,
        # verify_bad_answer must not pass.
        weakened = replace(hidden, bad_answer=near_oracle)
        probe = verify_bad_answer(weakened)
        self.assertFalse(probe.passed)
        with self.assertRaises(AssertionError) as ctx:
            run_tempo_verification(weakened)
        self.assertIn("missing=", str(ctx.exception))
        self.assertIn("dual_path_handling", str(ctx.exception))

    def test_run_tempo_verification_bundle(self):
        candidate = discover_workflows(workflow_id="http-signature-debug")[0]
        hidden = build_hidden_truth(candidate)
        results = run_tempo_verification(hidden)
        self.assertIn("oracle_answer", results)
        self.assertIn("bad_answer", results)
        self.assertTrue(results["bad_answer"].passed)


if __name__ == "__main__":
    unittest.main()
