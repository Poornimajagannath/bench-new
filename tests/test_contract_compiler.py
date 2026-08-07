"""Tests for the Workflow Contract Compiler and hidden-truth firewall."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from content_bench.contract_compiler import (
    SCHEMA_VERSION,
    assert_receipt_firewall,
    build_harbor_shape_preview,
    build_hidden_truth_receipt,
    compile_and_write,
    compile_contract_bundle,
    render_contract_markdown,
)
from content_bench.discovery import discover_workflows
from content_bench.routing import classify_failure
from content_bench.task_pack import (
    assert_no_verifier_leak,
    build_hidden_truth,
    materialize_contract,
)
from content_bench.verifiers import (
    run_stable_bench_inspired_verification,
    write_verifier_results,
)

ROOT = Path(__file__).resolve().parents[1]


class ContractCompilerTests(unittest.TestCase):
    def setUp(self):
        self.candidates = {c.workflow_id: c for c in discover_workflows()}
        self.candidate = self.candidates["microform-payer-auth-state-machine"]

    def test_compile_bundle_has_required_fields(self):
        pack, hidden, agent_path, private_path = materialize_contract(self.candidate)
        results = run_stable_bench_inspired_verification(hidden)
        result_path = write_verifier_results(self.candidate.workflow_id, results)
        classification = classify_failure(self.candidate, results["bad_answer"])

        bundle, json_path, md_path = compile_and_write(
            self.candidate,
            agent_visible_path=agent_path,
            hidden_truth_path=private_path,
            verifier_result_path=result_path,
            improvement_actions=classification.actions,
        )

        self.assertEqual(bundle["schema_version"], SCHEMA_VERSION)
        for key in (
            "workflow_id",
            "title",
            "goal",
            "stages",
            "api_sdk_facts",
            "confusion_points",
            "source_seed_ids",
            "pm_decision",
            "task_pack_path",
            "hidden_truth_receipt",
            "harbor_shape_preview",
            "verifier_result_path",
            "improvement_actions",
        ):
            self.assertIn(key, bundle)

        self.assertEqual(bundle["workflow_id"], self.candidate.workflow_id)
        self.assertEqual(bundle["source_seed_ids"], self.candidate.seed_ids)
        self.assertTrue(json_path.exists())
        self.assertTrue(md_path.exists())
        self.assertTrue(str(json_path).endswith(".contract_bundle.json"))
        self.assertTrue(str(md_path).endswith(".contract_bundle.md"))
        self.assertEqual(pack.workflow_id, self.candidate.workflow_id)

    def test_harbor_shape_preview_is_preview_only(self):
        _, _, agent_path, _ = materialize_contract(self.candidate)
        preview = build_harbor_shape_preview(
            self.candidate,
            agent_visible_path=agent_path,
        )
        self.assertTrue(preview["preview_only"])
        self.assertEqual(preview["runner_integration"], "not implemented")
        for key in (
            "instruction",
            "environment",
            "test_ref",
            "expected_artifact",
            "required_receipts",
            "isolation_note",
        ):
            self.assertIn(key, preview)

        bundle = compile_contract_bundle(self.candidate)
        self.assertTrue(bundle["harbor_shape_preview"]["preview_only"])
        self.assertEqual(
            bundle["harbor_shape_preview"]["runner_integration"],
            "not implemented",
        )

    def test_hidden_truth_receipt_firewall(self):
        _, hidden, agent_path, private_path = materialize_contract(self.candidate)
        receipt = build_hidden_truth_receipt(
            agent_visible_path=agent_path,
            hidden_truth_path=private_path,
        )

        self.assertTrue(receipt["oracle_present"])
        self.assertTrue(receipt["bad_answer_present"])
        self.assertTrue(receipt["private_checks_present"])
        self.assertTrue(receipt["agent_pack_omits_oracle"])
        self.assertTrue(receipt["agent_pack_omits_bad_answer"])
        self.assertTrue(receipt["agent_pack_omits_private_checks"])
        self.assertGreater(receipt["oracle_field_count"], 0)
        self.assertGreater(receipt["private_check_count"], 0)

        blob = json.dumps(receipt)
        mistake = str(hidden.bad_answer.get("mistake", ""))
        self.assertTrue(mistake)
        self.assertNotIn(mistake, blob)

        for banned in (
            "oracle_answer",
            "oracle_summary",
            "bad_answer_fixture",
            "verifier_private_checks",
            "hidden_checks",
            "scoring_rubric",
            "expected_bad_failure_ids",
        ):
            self.assertNotIn(f'"{banned}"', blob)

        # Distinctive oracle field values must not appear.
        self.assertNotIn("runs_enrollment_check", blob)
        self.assertNotIn("passes_auth_refs_to_payment", blob)

        assert_receipt_firewall(receipt, hidden_truth_path=private_path)

    def test_receipt_firewall_rejects_leaked_content(self):
        leaky = {
            "hidden_truth_path": "artifacts/task_packs/x.verifier_private.json",
            "agent_visible_path": "artifacts/task_packs/x.agent_task.json",
            "oracle_present": True,
            "bad_answer_present": True,
            "private_checks_present": True,
            "agent_pack_omits_oracle": True,
            "agent_pack_omits_bad_answer": True,
            "agent_pack_omits_private_checks": True,
            "oracle_answer": {"runs_enrollment_check": True},  # forbidden
        }
        with self.assertRaises(ValueError) as ctx:
            assert_receipt_firewall(leaky)
        self.assertIn("disallowed keys", str(ctx.exception))

    def test_receipt_firewall_rejects_mistake_content(self):
        _, hidden, agent_path, private_path = materialize_contract(self.candidate)
        receipt = build_hidden_truth_receipt(
            agent_visible_path=agent_path,
            hidden_truth_path=private_path,
        )
        # Inject forbidden content into an allowed string field.
        poisoned = dict(receipt)
        poisoned["hidden_truth_path"] = (
            f"{receipt['hidden_truth_path']} :: {hidden.bad_answer['mistake']}"
        )
        with self.assertRaises(ValueError) as ctx:
            assert_receipt_firewall(poisoned, hidden_truth_path=private_path)
        self.assertIn("mistake", str(ctx.exception).lower())

    def test_bundle_does_not_leak_hidden_truth(self):
        _, hidden, agent_path, private_path = materialize_contract(self.candidate)
        bundle = compile_contract_bundle(
            self.candidate,
            agent_visible_path=agent_path,
            hidden_truth_path=private_path,
        )
        blob = json.dumps(bundle)
        mistake = str(hidden.bad_answer.get("mistake", ""))
        self.assertNotIn(mistake, blob)
        for banned in (
            "oracle_summary",
            "bad_answer_fixture",
            "hidden_checks",
            "scoring_rubric",
        ):
            self.assertNotIn(f'"{banned}"', blob)

        # Agent pack artifact remains clean.
        agent_payload = json.loads(agent_path.read_text(encoding="utf-8"))
        assert_no_verifier_leak(agent_payload)
        agent_blob = json.dumps(agent_payload)
        self.assertNotIn(mistake, agent_blob)
        self.assertNotIn('"oracle_summary"', agent_blob)
        self.assertNotIn('"bad_answer_fixture"', agent_blob)
        self.assertNotIn('"hidden_checks"', agent_blob)

    def test_markdown_answers_six_questions(self):
        bundle = compile_contract_bundle(self.candidate)
        md = render_contract_markdown(bundle)
        for heading in (
            "What source confusion became this contract?",
            "What did PM approve or edit?",
            "What agent-visible task pack was created?",
            "What hidden truth exists, without showing it?",
            "How would this map to a future Harbor/Tempo-style eval task?",
            "What verifier result or product action exists now?",
        ):
            self.assertIn(heading, md)
        self.assertIn("preview_only", md)
        self.assertIn("not implemented", md)
        # Must not dump oracle/bad content into the markdown narrative.
        hidden = build_hidden_truth(self.candidate)
        mistake = str(hidden.bad_answer.get("mistake", ""))
        self.assertNotIn(mistake, md)

    def test_all_workflows_compile(self):
        for workflow_id, candidate in self.candidates.items():
            with self.subTest(workflow=workflow_id):
                bundle, json_path, md_path = compile_and_write(candidate)
                self.assertEqual(bundle["workflow_id"], workflow_id)
                self.assertTrue(bundle["harbor_shape_preview"]["preview_only"])
                self.assertTrue(bundle["hidden_truth_receipt"]["oracle_present"])
                self.assertTrue(
                    bundle["hidden_truth_receipt"]["agent_pack_omits_oracle"]
                )
                self.assertTrue(json_path.exists())
                self.assertTrue(md_path.exists())
                written = json.loads(json_path.read_text(encoding="utf-8"))
                self.assertEqual(
                    written["task_pack_path"],
                    f"artifacts/task_packs/{workflow_id}.agent_task.json",
                )
                self.assertFalse(written["task_pack_path"].startswith("/"))


if __name__ == "__main__":
    unittest.main()
