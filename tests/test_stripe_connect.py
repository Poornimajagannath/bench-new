"""Tests for Stripe Connect proof lane."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from evals.run_connect_eval import REQUIRED_QUICKSTART_MARKERS, run_mock, write_outputs  # noqa: E402
from relay_bench.content_engine.stripe_connect import (  # noqa: E402
    OPENAPI_PATH,
    build_quickstart_steps,
    render_quickstart,
    run_stripe_connect_proof,
)


class StripeConnectTests(unittest.TestCase):
    def test_openapi_fixture_has_accounts_and_links(self):
        data = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
        paths = data["paths"]
        self.assertIn("/v1/accounts", paths)
        self.assertIn("/v1/account_links", paths)
        self.assertIn("post", paths["/v1/accounts"])
        self.assertIn("post", paths["/v1/account_links"])

    def test_quickstart_schema_and_word_cap(self):
        openapi = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
        steps = build_quickstart_steps(openapi)
        self.assertGreaterEqual(len(steps), 3)
        for step in steps:
            for key in ("goal", "prerequisites", "actions", "expected_outcome", "common_errors"):
                self.assertIn(key, step)
            self.assertLessEqual(len(" ".join(step["actions"]).split()), 300)
        md = render_quickstart(steps)
        for marker in REQUIRED_QUICKSTART_MARKERS:
            self.assertIn(marker, md)

    def test_proof_pipeline_writes_content(self):
        summary = run_stripe_connect_proof(stamp_date="2026-08-07")
        self.assertTrue(summary["ok"])
        self.assertIn("connect-quickstart.md", summary["content_pages"])
        quickstart = ROOT / "content" / "connect-quickstart.md"
        self.assertTrue(quickstart.exists())
        body = quickstart.read_text(encoding="utf-8")
        self.assertIn("POST /v1/accounts", body)
        self.assertIn("POST /v1/account_links", body)
        self.assertTrue((ROOT / "artifacts/content_engine/stripe/source-mix-report.md").exists())
        self.assertTrue((ROOT / "artifacts/content_engine/stripe/ingestion-report.md").exists())

    def test_mock_eval_passes_after_proof(self):
        run_stripe_connect_proof(stamp_date="2026-08-07")
        result = run_mock()
        self.assertEqual(result["gate"], "pass")
        write_outputs(result)
        self.assertTrue((ROOT / "evals" / "latest.md").exists())
        latest = (ROOT / "evals" / "latest.md").read_text(encoding="utf-8")
        self.assertIn("pass", latest)

    def test_live_refuses_non_test_key(self):
        from evals.run_connect_eval import run_live

        with self.assertRaises(ValueError):
            run_live("sk_live_fake")


if __name__ == "__main__":
    unittest.main()
