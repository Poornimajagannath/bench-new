import unittest

from relay_bench.discovery import (
    discover_suggestions,
    discover_workflows,
    extract_from_question,
    load_raw_questions,
    suggest_workflow,
    synthesize_candidates_payload,
)
from relay_bench.pm_gate import apply_pm_decisions, load_pm_decisions


class DiscoveryTests(unittest.TestCase):
    def test_raw_questions_have_no_workflow_labels(self):
        questions = load_raw_questions()
        self.assertGreaterEqual(len(questions), 3)
        channels = {q.channel for q in questions}
        self.assertTrue({"forum", "docs", "support"} & channels)
        for q in questions:
            self.assertTrue(q.question)
            self.assertFalse(hasattr(q, "workflow_id") and getattr(q, "workflow_id"))

    def test_extract_goal_symptoms_entities(self):
        questions = {q.seed_id: q for q in load_raw_questions()}
        flex = extract_from_question(questions["seed-flex-01"])
        self.assertTrue(flex.goal)
        self.assertTrue(flex.symptoms)
        self.assertTrue({"Flex", "TMS", "Microform"} & set(flex.entities))

        mpa = extract_from_question(questions["seed-mpa-01"])
        self.assertIn("Payer Authentication", mpa.entities)
        self.assertIn("enrollment", mpa.entities)

    def test_suggest_workflow_id_and_stages(self):
        rows = discover_suggestions()
        by_seed = {q.seed_id: (e, s) for q, e, s in rows}
        self.assertEqual(
            by_seed["seed-flex-01"][1].suggested_workflow_id, "flex-token-lifecycle"
        )
        self.assertEqual(
            by_seed["seed-httpsig-01"][1].suggested_workflow_id, "http-signature-debug"
        )
        self.assertEqual(
            by_seed["seed-mpa-01"][1].suggested_workflow_id,
            "microform-payer-auth-state-machine",
        )
        self.assertIn("enrollment_check", by_seed["seed-mpa-01"][1].stages)

    def test_pm_gate_required_before_candidates(self):
        rows = discover_suggestions()
        # Without PM decisions, nothing is task-pack-ready.
        self.assertEqual(apply_pm_decisions(rows, {}), [])
        approved = apply_pm_decisions(rows, load_pm_decisions())
        self.assertEqual(len(approved), 3)
        mpa = next(c for c in approved if c.workflow_id == "microform-payer-auth-state-machine")
        self.assertEqual(mpa.pm_decision, "edit")
        self.assertIn("enrollment_check", mpa.stages)

    def test_discover_workflows_returns_pm_approved_only(self):
        candidates = discover_workflows()
        self.assertEqual(len(candidates), 3)
        filtered = discover_workflows(workflow_id="microform-payer-auth-state-machine")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].workflow_id, "microform-payer-auth-state-machine")

    def test_synthesize_payload_includes_pipeline_stages(self):
        payload = synthesize_candidates_payload()
        self.assertEqual(payload["stage"], "docetl_extract_suggest_pm")
        self.assertEqual(
            payload["pipeline"],
            [
                "raw_forum_docs_support_questions",
                "docetl_extract_goal_symptoms_entities",
                "suggest_workflow_id_and_stages",
                "pm_approve_or_edit",
                "relay_bench_task_pack_and_verifier",
            ],
        )
        self.assertEqual(payload["suggestion_count"], 3)
        self.assertEqual(payload["approved_candidate_count"], 3)


if __name__ == "__main__":
    unittest.main()
