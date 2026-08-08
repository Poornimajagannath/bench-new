"""outcome_missing is a machine-readable per-step flag (L2 gap-marker)."""

from __future__ import annotations

import re
import unittest

from content_bench.content_engine.workflow_pages import (
    BOARDING_WORKFLOWS,
    compose_workflow_page,
)


class OutcomeMissingFlagTests(unittest.TestCase):
    def test_ui_step_without_outcome_gets_flag(self):
        claims = [
            {
                "claim_id": "t:1",
                "schema": "quickstart_step",
                "title": "Add Merchant",
                "text": "Click + Add Merchant.",
                "source_pointer": "boarding-reg-create-merch.md",
                "extras": {"sequence": 1, "doc_name": "boarding-reg-create-merch.md"},
            }
        ]
        # Use create-merchant workflow matchers
        spec = next(w for w in BOARDING_WORKFLOWS if w.workflow_id == "create-merchant-organization")
        # Ensure matcher hits
        claims[0]["source_pointer"] = (
            "en-us_boarding_developer_all_rest_boarding_"
            "boarding-reg-intro_boarding-reg-create-merch.md.md"
        )
        md = compose_workflow_page(spec, claims, stamp="test")
        self.assertIn("outcome_missing: true", md)
        self.assertIn("Expected outcome: **Gap:** not stated in source.", md)
        m = re.search(
            r"<!-- sequence_stats: steps=(\d+) outcome_gaps=(\d+) "
            r"outcome_missing=(\d+)",
            md,
        )
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), m.group(2))
        self.assertEqual(m.group(2), m.group(3))

    def test_stated_outcome_is_not_flagged(self):
        claims = [
            {
                "claim_id": "t:2",
                "schema": "quickstart_step",
                "title": "Open",
                "text": "Click Merchants. The Merchants page appears.",
                "source_pointer": (
                    "en-us_boarding_developer_all_rest_boarding_"
                    "boarding-reg-intro_boarding-reg-create-merch.md.md"
                ),
                "extras": {"sequence": 1},
            }
        ]
        spec = next(w for w in BOARDING_WORKFLOWS if w.workflow_id == "create-merchant-organization")
        md = compose_workflow_page(spec, claims, stamp="test")
        self.assertIn("outcome_missing: false", md)
        self.assertNotIn(
            "Click Merchants. The Merchants page appears.\n   - outcome_missing: true",
            md,
        )


if __name__ == "__main__":
    unittest.main()
