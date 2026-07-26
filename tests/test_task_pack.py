import json
import unittest

from relay_bench.discovery import discover_workflows
from relay_bench.task_pack import build_hidden_truth, build_task_pack, materialize_contract


class TaskPackTests(unittest.TestCase):
    def setUp(self):
        self.candidate = discover_workflows(workflow_id="microform-payer-auth-state-machine")[0]

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

    def test_materialize_writes_separate_artifacts(self):
        pack, hidden, pack_path, hidden_path = materialize_contract(self.candidate)
        self.assertTrue(pack_path.exists())
        self.assertTrue(hidden_path.exists())
        written_pack = json.loads(pack_path.read_text(encoding="utf-8"))
        written_hidden = json.loads(hidden_path.read_text(encoding="utf-8"))
        self.assertEqual(written_pack["workflow_id"], pack.workflow_id)
        self.assertIn("oracle_answer", written_hidden)
        self.assertNotIn("oracle_answer", written_pack)
        self.assertNotIn("bad_answer", written_pack)
        self.assertNotIn("verifier_private_checks", written_pack)


if __name__ == "__main__":
    unittest.main()
