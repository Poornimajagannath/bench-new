import unittest

from relay_bench.discovery import discover_workflows
from relay_bench.reporting import build_report, render_markdown, write_report
from relay_bench.routing import classify_failure
from relay_bench.task_pack import build_hidden_truth, materialize_contract
from relay_bench.verifiers import (
    run_stable_bench_inspired_verification,
    write_verifier_results,
)


class ReportingTests(unittest.TestCase):
    def test_report_answers_five_questions(self):
        candidate = discover_workflows(workflow_id="microform-payer-auth-state-machine")[0]
        pack, hidden, pack_path, _hidden_path = materialize_contract(candidate)
        results = run_stable_bench_inspired_verification(hidden)
        result_path = write_verifier_results(candidate.workflow_id, results)
        classification = classify_failure(candidate, results["bad_answer"])
        report = build_report(
            candidate=candidate,
            classification=classification,
            bad_result=results["bad_answer"],
            task_pack_path=pack_path,
            verifier_result_path=result_path,
            bad_answer_mistake=str(hidden.bad_answer.get("mistake", "")),
        )
        md = render_markdown(report)
        for heading in (
            "What developers were confused about",
            "What Relay discovered",
            "What the bad answer got wrong",
            "How the verifier caught it",
            "What product surface improves next",
        ):
            self.assertIn(heading, md)
        self.assertIn("Relay CLI workflow verifier", md)
        self.assertTrue(report.developer_confusion)
        self.assertTrue(report.verifier_caught)

        # Portable repo-relative artifact paths (no absolute /workspace or machine roots).
        self.assertEqual(
            report.task_pack_path,
            "artifacts/task_packs/microform-payer-auth-state-machine.agent_task.json",
        )
        self.assertEqual(
            report.verifier_result_path,
            "artifacts/verifier_results/microform-payer-auth-state-machine.result.json",
        )
        self.assertFalse(report.task_pack_path.startswith("/"))
        self.assertFalse(report.verifier_result_path.startswith("/"))
        self.assertNotIn("/workspace/", md)

        md_path, json_path = write_report(report)
        self.assertTrue(md_path.exists())
        self.assertTrue(json_path.exists())
        # Agent pack must remain separate from report oracle details
        self.assertNotIn("oracle_answer", pack.to_dict())


if __name__ == "__main__":
    unittest.main()
