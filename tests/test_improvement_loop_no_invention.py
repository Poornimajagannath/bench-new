"""No-invention guard for the improvement loop.

The loop may rephrase/restructure/assemble existing claims. It may never
author a fact absent from the claim set. A step with no stated outcome must
get a gap marker — not an invented result. This is the C4 refusal, made
machine-checkable once a model is attached.
"""

from __future__ import annotations

import unittest

from pipelines.run_improvement_loop import (
    GAP_MARKER_NO_OUTCOME,
    NO_INVENTION_RULE,
    is_loopback_url,
    propose_for_missing_outcome,
    proposal_invents_facts,
    recheck_llm_candidate,
)


class NoInventionTests(unittest.TestCase):
    def test_rule_text_is_explicit(self):
        self.assertIn("never author a fact absent from the claim set", NO_INVENTION_RULE)

    def test_missing_outcome_proposes_gap_marker_not_invention(self):
        step = {
            "claim_id": "wf:step:1",
            "text": "Click + Add Merchant",
            "schema": "quickstart_step",
            "extras": {},
        }
        # Claim set has the step itself and unrelated prose — no outcome fact.
        claims = [
            step,
            {
                "claim_id": "wf:prose:1",
                "schema": "prose_claim",
                "text": "Merchants belong to a portfolio organization.",
            },
        ]
        result = propose_for_missing_outcome(step, claims)
        self.assertEqual(result["kind"], "gap_marker")
        self.assertEqual(result["text"], GAP_MARKER_NO_OUTCOME)
        self.assertEqual(result["status"], "proposed_gap")
        # Must not invent a success/result narrative.
        invented = "merchant was created successfully"
        self.assertNotIn(invented, result["text"].lower())
        self.assertNotIn("succeeded", result["text"].lower())

    def test_assembles_outcome_when_present_in_claim_set(self):
        step = {
            "claim_id": "wf:step:2",
            "text": "Click Submit",
            "schema": "quickstart_step",
            "extras": {},
        }
        claims = [
            step,
            {
                "claim_id": "wf:outcome:2",
                "schema": "step_outcome",
                "step_claim_id": "wf:step:2",
                "text": "Click Submit",
                "extras": {"outcome": "The registration status becomes SUCCESS."},
            },
        ]
        result = propose_for_missing_outcome(step, claims)
        self.assertEqual(result["kind"], "assembled_from_claims")
        self.assertEqual(result["text"], "The registration status becomes SUCCESS.")
        self.assertIn("wf:outcome:2", result["source_claim_ids"])

    def test_c4_style_proposal_is_rejected(self):
        reason = proposal_invents_facts("Author expected outcomes for 220 steps")
        self.assertIsNotNone(reason)
        cand = recheck_llm_candidate(
            {
                "id": "L-bad-outcomes",
                "proposal": "Author expected outcomes for 220 steps",
                "change_type": "pipeline",
                "evidence": [
                    "artifacts/content_engine/boarding/gap-report.md — headline 1"
                ],
            }
        )
        self.assertEqual(cand["status"], "discarded")
        self.assertIn("invent", cand["recheck"])

    def test_gap_marker_proposal_is_allowed(self):
        reason = proposal_invents_facts(
            "Insert gap markers for steps that lack stated outcomes; "
            "the pipeline cannot invent outcomes.",
            change_type="gap_marker",
        )
        self.assertIsNone(reason)
        cand = recheck_llm_candidate(
            {
                "id": "L-gap-outcomes",
                "proposal": (
                    "Insert gap markers for workflow steps that lack stated "
                    "outcomes; do not invent results."
                ),
                "change_type": "gap_marker",
                "evidence": [
                    "artifacts/content_engine/boarding/gap-report.md — headline 1"
                ],
            }
        )
        self.assertEqual(cand["status"], "proposed")

    def test_corpus_egress_only_loopback(self):
        self.assertTrue(is_loopback_url("http://127.0.0.1:8000/v1"))
        self.assertTrue(is_loopback_url("http://localhost:8000/v1"))
        self.assertFalse(is_loopback_url("https://api.openai.com/v1"))
        self.assertFalse(is_loopback_url("http://10.0.0.5:8000/v1"))


if __name__ == "__main__":
    unittest.main()
