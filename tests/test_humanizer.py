"""A3 humanizer: style pass + fact_hash guard."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from content_bench.content_engine.humanizer import (  # noqa: E402
    FactHashGuardError,
    apply_style_rules,
    assert_facts_unchanged,
    fact_hash,
    guarded_transform,
    humanize,
    write_prose,
)
from content_bench.content_engine.reference_pages import (  # noqa: E402
    render_reference_page,
)
from content_bench.content_engine.stripe_connect import (  # noqa: E402
    render_endpoint_page,
    render_quickstart,
)


SAMPLE_UNIT = {
    "operation_id": "createPayment",
    "http_method": "POST",
    "endpoint": "/pts/v2/payments",
    "summary": "Create a payment authorization",
    "auth_requirements": ["httpSignature"],
    "lineage_origin": "generated_from_spec",
    "doc_id": "doc-payments-core-openapi",
    "request_fields": [
        {
            "name": "orderInformation.amountDetails.totalAmount",
            "type": "string",
            "required": True,
            "description": "Order total amount",
        }
    ],
    "response_fields": [{"name": "id", "type": "string", "required": False}],
    "error_cases": [
        {
            "code": "error_schema",
            "meaning": "Error payload",
            "recovery": "Inspect reason/details",
        }
    ],
    "evidence_quotes": ["Create a payment authorization"],
    "workflows": ["microform-payer-auth-state-machine"],
    "unit_id": "payments-core-openapi:ref:createPayment",
    "api_name": "Payment Gateway Payments Core (local Content Bench fixture)",
}


class HumanizerTests(unittest.TestCase):
    def test_fact_hash_stable_under_prose_rewrite(self):
        page = render_reference_page(SAMPLE_UNIT)
        before = fact_hash(page)
        updated = humanize(page)
        after = fact_hash(updated)
        self.assertEqual(before.digest, after.digest)
        assert_facts_unchanged(page, updated)

    def test_humanizer_cannot_change_templated_fact(self):
        """Architect review gate: prove enjoyable cannot edit a fact."""
        page = render_reference_page(SAMPLE_UNIT)
        original_hash = fact_hash(page)
        self.assertIn("`/pts/v2/payments`", original_hash.facts_body)

        def evil_rewrite(markdown: str) -> str:
            # Mutate a templated path inside the facts block.
            return markdown.replace("`/pts/v2/payments`", "`/pts/v2/evil`")

        with self.assertRaises(FactHashGuardError):
            guarded_transform(page, evil_rewrite)

        # Simulate a buggy humanize implementation that rewrites the whole page.
        def buggy_humanize(markdown: str) -> str:
            return evil_rewrite(markdown)

        with self.assertRaises(FactHashGuardError):
            guarded_transform(page, buggy_humanize)

        # Happy path still preserves the path fact.
        polished = humanize(page)
        self.assertEqual(fact_hash(polished).digest, original_hash.digest)
        self.assertIn("`/pts/v2/payments`", polished)
        self.assertNotIn("`/pts/v2/evil`", polished)

    def test_humanize_strips_ai_vocab_from_prose(self):
        page = render_reference_page(SAMPLE_UNIT)
        # Inject AI-isms into the prose section only.
        polluted = page.replace(
            "You use this endpoint to create a payment authorization.",
            "This endpoint serves as a pivotal gateway, showcasing a seamless "
            "and robust experience as described in the OpenAPI fixture.",
        )
        before = fact_hash(polluted)
        cleaned = humanize(polluted)
        after = fact_hash(cleaned)
        self.assertEqual(before.digest, after.digest)
        self.assertNotIn("pivotal", cleaned.lower())
        self.assertNotIn("showcasing", cleaned.lower())
        self.assertNotIn("as described in the OpenAPI", cleaned)
        self.assertIn("`/pts/v2/payments`", cleaned)
        self.assertIn("orderInformation.amountDetails.totalAmount", cleaned)

    def test_write_prose_marks_uncertainty_with_todo(self):
        bare = (
            "---\ntitle: Demo\ngenerated: true\n---\n\n"
            "# Demo\n\n"
            "<!-- section:facts -->\n"
            "**Method:** `GET`  \n"
            "**Path:** `/v1/demo`  \n"
            "<!-- /section:facts -->\n"
        )
        drafted = write_prose(bare)
        self.assertIn("<!-- section:prose -->", drafted)
        self.assertIn("<!-- TODO:", drafted)
        assert_facts_unchanged(bare, drafted)

    def test_style_rules_second_person(self):
        prose = "## Overview\n\nThe client should send a POST. Developers must store the id.\n"
        out = apply_style_rules(prose, "")
        self.assertIn("you ", out.lower())
        self.assertNotIn("The client should", out)

    def test_connect_endpoint_and_quickstart_round_trip(self):
        claim = {
            "title": "POST /v1/accounts",
            "text": "Create a connected account",
            "extras": {
                "method": "POST",
                "path": "/v1/accounts",
                "operation_id": "PostAccounts",
                "parameters": [
                    {
                        "name": "controller[fees][payer]",
                        "in": "body",
                        "required": True,
                        "type": "string",
                        "description": "Who pays Stripe fees",
                    }
                ],
                "status_codes": ["200", "400"],
                "security": [{"bearerAuth": []}],
            },
        }
        endpoint = render_endpoint_page(claim)
        quickstart = render_quickstart(
            [
                {
                    "sequence": 1,
                    "title": "Prepare platform test credentials",
                    "goal": "Authenticate as the Connect platform in test mode.",
                    "prerequisites": ["Stripe account"],
                    "actions": ["Confirm the key prefix is sk_test_."],
                    "expected_outcome": "API requests authenticate without 401.",
                    "common_errors": ["401 when using a publishable key"],
                }
            ]
        )
        for page in (endpoint, quickstart):
            before = fact_hash(page)
            after = fact_hash(humanize(page))
            self.assertEqual(before.digest, after.digest)

    def test_pipeline_scripts_dry_run(self):
        import subprocess

        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            content.mkdir()
            page = content / "createPayment.md"
            page.write_text(render_reference_page(SAMPLE_UNIT), encoding="utf-8")
            for script in ("write_prose.py", "humanize.py"):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "pipelines" / script), "--dry-run", str(page)],
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("facts_preserved", result.stdout)


if __name__ == "__main__":
    unittest.main()
