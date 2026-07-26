import unittest

from relay_bench.discovery import discover_workflows, load_seeds, synthesize_candidates_payload


class DiscoveryTests(unittest.TestCase):
    def test_load_frozen_seeds(self):
        seeds = load_seeds()
        self.assertGreaterEqual(len(seeds), 3)
        ids = {s.workflow_id for s in seeds}
        self.assertIn("flex-token-lifecycle", ids)
        self.assertIn("http-signature-debug", ids)
        self.assertIn("microform-payer-auth-state-machine", ids)

    def test_discover_all_candidates(self):
        candidates = discover_workflows()
        self.assertEqual(len(candidates), 3)
        for c in candidates:
            self.assertTrue(c.stages)
            self.assertTrue(c.api_sdk_facts)
            self.assertTrue(c.seed_ids)

    def test_discover_filters_workflow(self):
        candidates = discover_workflows(workflow_id="microform-payer-auth-state-machine")
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].workflow_id, "microform-payer-auth-state-machine")
        self.assertIn("enrollment_check", candidates[0].stages)

    def test_synthesize_payload_shape(self):
        payload = synthesize_candidates_payload()
        self.assertEqual(payload["stage"], "docetl_workflow_discovery")
        self.assertEqual(payload["candidate_count"], 3)


if __name__ == "__main__":
    unittest.main()
