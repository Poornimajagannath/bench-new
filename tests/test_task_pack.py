import json
import unittest

from relay_bench.discovery import discover_workflows
from relay_bench.task_pack import (
    assert_no_verifier_leak,
    build_hidden_truth,
    build_task_pack,
    materialize_contract,
    to_agent_task,
    to_verifier_private,
)


class TaskPackTests(unittest.TestCase):
    def setUp(self):
        self.candidates = {
            c.workflow_id: c for c in discover_workflows()
        }
        self.candidate = self.candidates["microform-payer-auth-state-machine"]

    def test_agent_pack_has_no_hidden_fields(self):
        pack = build_task_pack(self.candidate)
        data = pack.to_dict()
        for banned in ("oracle_answer", "bad_answer", "verifier_private_checks", "hidden_truth"):
            self.assertNotIn(banned, data)
        pack.assert_agent_safe()

    def test_hidden_truth_contains_oracle_and_bad_answer(self):
        hidden = build_hidden_truth(self.candidate)
        self.assertIn("runs_enrollment_check", hidden.oracle_answer)
        self.assertFalse(hidden.bad_answer["runs_enrollment_check"])
        self.assertTrue(hidden.verifier_private_checks)
        self.assertEqual(
            sorted(hidden.expected_bad_failure_ids),
            [
                "auth_refs_on_payment",
                "dual_path_handling",
                "enrollment_present",
                "state_machine_complete",
            ],
        )

    def test_agent_task_verifier_private_separation_for_all_workflows(self):
        for workflow_id, candidate in self.candidates.items():
            with self.subTest(workflow=workflow_id):
                pack, hidden, agent_path, private_path = materialize_contract(candidate)
                self.assertTrue(str(agent_path).endswith(".agent_task.json"))
                self.assertTrue(str(private_path).endswith(".verifier_private.json"))

                agent_payload = json.loads(agent_path.read_text(encoding="utf-8"))
                private_payload = json.loads(private_path.read_text(encoding="utf-8"))
                assert_no_verifier_leak(agent_payload)

                self.assertIn("agent_task", agent_payload)
                self.assertIn("verifier_private", private_payload)
                agent_task = agent_payload["agent_task"]
                self.assertEqual(agent_task["workflow_id"], workflow_id)
                self.assertEqual(agent_task["environment_mode"], "local-simulated")
                self.assertIn("instruction", agent_task)
                self.assertIn("allowed_public_evidence_ids", agent_task)

                private = private_payload["verifier_private"]
                self.assertIn("oracle_summary", private)
                self.assertIn("bad_answer_fixture", private)
                self.assertIn("hidden_checks", private)
                self.assertIn("scoring_rubric", private)

                agent_blob = json.dumps(agent_payload)
                for banned in (
                    "oracle_summary",
                    "bad_answer_fixture",
                    "hidden_checks",
                    "scoring_rubric",
                    "expected_bad_failure_ids",
                ):
                    self.assertNotIn(f'"{banned}"', agent_blob)

                # Distinctive oracle/bad values must not leak into agent JSON.
                mistake = str(hidden.bad_answer.get("mistake", ""))
                if mistake:
                    self.assertNotIn(mistake, agent_blob)

                # Legacy aliases still written for plan path compatibility.
                legacy_pack = agent_path.with_name(f"{workflow_id}.task_pack.json")
                legacy_hidden = agent_path.with_name(f"{workflow_id}.hidden_truth.json")
                self.assertTrue(legacy_pack.exists())
                self.assertTrue(legacy_hidden.exists())
                self.assertEqual(build_task_pack(candidate).workflow_id, pack.workflow_id)
                self.assertEqual(
                    to_agent_task(pack, candidate)["agent_task"]["workflow_id"],
                    workflow_id,
                )
                self.assertEqual(
                    to_verifier_private(hidden)["verifier_private"]["fixture_id"],
                    hidden.fixture_id,
                )


if __name__ == "__main__":
    unittest.main()
