import json
import unittest
from pathlib import Path

from content_bench.discovery import (
    catalog_entry,
    discover_suggestions,
    discover_workflows,
    extract_from_question,
    load_raw_questions,
    synthesize_candidates_payload,
)
from content_bench.pm_gate import (
    apply_pm_decisions,
    load_pm_decisions,
    require_pm_approved_candidate,
)
from content_bench.schemas import (
    Extraction,
    PmDecision,
    RawQuestion,
    WorkflowSuggestion,
)

ROOT = Path(__file__).resolve().parents[1]


class DiscoveryTests(unittest.TestCase):
    def test_raw_questions_have_no_workflow_labels(self):
        questions = load_raw_questions()
        self.assertEqual(len(questions), 20)
        channels = {q.channel for q in questions}
        self.assertTrue({"forum", "docs", "support"} & channels)
        for q in questions:
            self.assertTrue(q.question)

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
            by_seed["seed-flex-02"][1].suggested_workflow_id, "flex-token-lifecycle"
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
        # 20 approved seeds reduce to 3 workflow contracts.
        self.assertEqual(len(approved), 3)
        mpa = next(c for c in approved if c.workflow_id == "microform-payer-auth-state-machine")
        self.assertEqual(mpa.pm_decision, "edit")
        self.assertIn("enrollment_check", mpa.stages)

    def test_multiple_seeds_reduce_to_one_workflow_candidate(self):
        """DocETL value: many confused inputs → one richer workflow contract."""
        stages = [
            "capture_transient_token",
            "validate_token_type",
            "create_permanent_instrument",
            "authorize_with_instrument",
        ]
        rows = [
            (
                RawQuestion(
                    seed_id="syn-flex-a",
                    source="test",
                    channel="forum",
                    question="Flex TMS transient token confusion A",
                    public_refs=[],
                ),
                Extraction(
                    seed_id="syn-flex-a",
                    goal="How do I move Flex tokens into TMS?",
                    symptoms=["createInstrument rejects JWT as pan"],
                    entities=["Flex", "TMS"],
                    confidence=0.8,
                ),
                WorkflowSuggestion(
                    seed_id="syn-flex-a",
                    suggested_workflow_id="flex-token-lifecycle",
                    title="Flex Token Lifecycle",
                    stages=stages,
                    rationale=["entity_hit:flex"],
                    confidence=0.8,
                ),
            ),
            (
                RawQuestion(
                    seed_id="syn-flex-b",
                    source="test",
                    channel="support",
                    question="Flex TMS transient token confusion B",
                    public_refs=[],
                ),
                Extraction(
                    seed_id="syn-flex-b",
                    goal="Why does transientTokenJwt expire before TMS?",
                    symptoms=["JWT expires before permanent instrument create"],
                    entities=["Flex", "transientTokenJwt", "TMS"],
                    confidence=0.7,
                ),
                WorkflowSuggestion(
                    seed_id="syn-flex-b",
                    suggested_workflow_id="flex-token-lifecycle",
                    title="Flex Token Lifecycle",
                    stages=stages,
                    rationale=["entity_hit:tms"],
                    confidence=0.7,
                ),
            ),
        ]
        decisions = {
            "syn-flex-a": PmDecision(
                seed_id="syn-flex-a",
                decision="approve",
                approved_workflow_id="flex-token-lifecycle",
                edited_stages=None,
                edited_goal=None,
                pm_notes="approve A",
            ),
            "syn-flex-b": PmDecision(
                seed_id="syn-flex-b",
                decision="edit",
                approved_workflow_id="flex-token-lifecycle",
                edited_stages=stages,
                edited_goal="Move from Flex transient token to permanent TMS instrument safely.",
                pm_notes="edit B stages/goal at workflow level",
            ),
        }

        approved = apply_pm_decisions(rows, decisions)
        self.assertEqual(len(approved), 1)
        candidate = approved[0]
        self.assertEqual(candidate.workflow_id, "flex-token-lifecycle")
        self.assertEqual(sorted(candidate.seed_ids), ["syn-flex-a", "syn-flex-b"])
        self.assertEqual(candidate.pm_decision, "edit")
        self.assertEqual(candidate.stages, stages)
        self.assertEqual(
            candidate.goal,
            "Move from Flex transient token to permanent TMS instrument safely.",
        )
        self.assertIn("createInstrument rejects JWT as pan", candidate.confusion_points)
        self.assertIn("JWT expires before permanent instrument create", candidate.confusion_points)
        self.assertIn("entity:transientTokenJwt", candidate.confusion_points)
        self.assertEqual(candidate.extraction["merged_from_seed_count"], 2)

        # Frozen seed fixture merges all Flex questions into one contract.
        flex = require_pm_approved_candidate("flex-token-lifecycle")
        self.assertEqual(len(flex.seed_ids), 7)
        self.assertIn("seed-flex-01", flex.seed_ids)
        self.assertIn("seed-flex-07", flex.seed_ids)
        self.assertEqual(flex.extraction["merged_from_seed_count"], 7)

    def test_pm_remap_uses_approved_catalog_stages_not_suggestion(self):
        """PM can correct workflow_id; stages must follow the approved catalog."""
        flex_stages = [
            "capture_transient_token",
            "validate_token_type",
            "create_permanent_instrument",
            "authorize_with_instrument",
        ]
        httpsig_stages = list(catalog_entry("http-signature-debug")["stages"])
        rows = [
            (
                RawQuestion(
                    seed_id="syn-remap",
                    source="test",
                    channel="forum",
                    question="Looks like Flex but PM says HTTP Signature",
                    public_refs=[],
                ),
                Extraction(
                    seed_id="syn-remap",
                    goal="Why does auth fail after Flex token create?",
                    symptoms=["Authentication Failed after Flex setup"],
                    entities=["Flex", "Authentication Failed"],
                    confidence=0.5,
                ),
                WorkflowSuggestion(
                    seed_id="syn-remap",
                    suggested_workflow_id="flex-token-lifecycle",
                    title="Flex Token Lifecycle",
                    stages=flex_stages[:2],
                    rationale=["entity_hit:flex"],
                    confidence=0.5,
                ),
            )
        ]
        decisions = {
            "syn-remap": PmDecision(
                seed_id="syn-remap",
                decision="approve",
                approved_workflow_id="http-signature-debug",
                edited_stages=None,
                edited_goal=None,
                pm_notes="Correct mapping away from Flex suggestion",
            )
        }
        approved = apply_pm_decisions(rows, decisions)
        self.assertEqual(len(approved), 1)
        candidate = approved[0]
        self.assertEqual(candidate.workflow_id, "http-signature-debug")
        self.assertEqual(candidate.stages, httpsig_stages)
        self.assertNotEqual(candidate.stages, flex_stages[:2])
        self.assertTrue(candidate.suggestion["remapped_from_suggestion"])
        self.assertEqual(
            candidate.suggestion["original_suggested_workflow_ids"],
            ["flex-token-lifecycle"],
        )

    def test_discover_workflows_returns_pm_approved_only(self):
        candidates = discover_workflows()
        self.assertEqual(len(candidates), 3)
        filtered = discover_workflows(workflow_id="microform-payer-auth-state-machine")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].workflow_id, "microform-payer-auth-state-machine")

    def test_synthesize_payload_includes_pipeline_stages(self):
        payload = synthesize_candidates_payload()
        self.assertEqual(payload["stage"], "docetl_inspired_extract_suggest_pm")
        self.assertEqual(
            payload["pipeline"],
            [
                "raw_forum_docs_support_questions",
                "docetl_inspired_extract_goal_symptoms_entities",
                "suggest_workflow_id_and_stages",
                "pm_approve_or_edit",
                "content_bench_task_pack_and_stable_bench_inspired_verifier",
            ],
        )
        self.assertIn("ucbepic/docetl", payload["inspired_by"]["discovery"])
        self.assertIn("tempo-evals", payload["inspired_by"]["verifier"])
        self.assertEqual(payload["suggestion_count"], 20)
        # Reduced by workflow_id, not one candidate per seed.
        self.assertEqual(payload["approved_candidate_count"], 3)

    def test_candidates_artifact_is_fresh(self):
        artifact = json.loads(
            (ROOT / "artifacts" / "candidates.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, synthesize_candidates_payload())


if __name__ == "__main__":
    unittest.main()
