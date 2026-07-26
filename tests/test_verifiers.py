import unittest

from relay_bench.discovery import discover_workflows
from relay_bench.task_pack import build_hidden_truth
from relay_bench.verifiers import run_tempo_verification, verify_bad_answer, verify_oracle


class VerifierTests(unittest.TestCase):
    def test_oracle_passes_and_bad_answer_caught_for_all_workflows(self):
        for candidate in discover_workflows():
            with self.subTest(workflow=candidate.workflow_id):
                hidden = build_hidden_truth(candidate)
                oracle = verify_oracle(hidden)
                bad = verify_bad_answer(hidden)
                self.assertTrue(oracle.passed, oracle.caught_failures)
                self.assertTrue(bad.passed, "verifier should catch bad answer")
                self.assertGreater(len(bad.caught_failures), 0)

    def test_run_tempo_verification_bundle(self):
        candidate = discover_workflows(workflow_id="http-signature-debug")[0]
        hidden = build_hidden_truth(candidate)
        results = run_tempo_verification(hidden)
        self.assertIn("oracle_answer", results)
        self.assertIn("bad_answer", results)


if __name__ == "__main__":
    unittest.main()
