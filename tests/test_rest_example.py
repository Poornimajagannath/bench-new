"""rest_example schema: standalone REST Example JSON pages extract as claims."""

from __future__ import annotations

import unittest
from pathlib import Path

from content_bench.content_engine.ingest import _extract_claims_from_text

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = (
    ROOT
    / "data/products/boarding/guides/"
    / (
        "en-us_boarding_developer_all_rest_boarding_boarding-extend-hierarchy_"
        "boarding-reg-create-structural-api_"
        "boarding-reg-create-structural-api-example.md.md"
    )
)


class RestExampleTests(unittest.TestCase):
    def test_fixture_extracts_request_and_response(self):
        text = (
            "REST Example: Creating a Structural Organization "
            "{#boarding-reg-create-structural-api-example}\n"
            "==============================================================================================\n\n"
            "Request\n\n"
            "```\n"
            '{\n    "registrationInformation": {"boardingFlow": "ENTERPRISE"},\n'
            '    "organizationInformation": {"type": "STRUCTURAL"}\n}\n'
            "```\n\n"
            "Response to a Successful Request\n\n"
            "```\n"
            '{\n    "id": "1695804002",\n    "status": "SUCCESS"\n}\n'
            "```\n"
        )
        claims, drops = _extract_claims_from_text(
            text, source_pointer="fixture.md", doc_stem="fixture"
        )
        examples = [c for c in claims if c.schema == "rest_example"]
        self.assertEqual(len(drops), 0)
        self.assertEqual(len(examples), 2)
        roles = {c.extras["role"] for c in examples}
        self.assertEqual(roles, {"request", "response"})
        req = next(c for c in examples if c.extras["role"] == "request")
        self.assertIn("registrationInformation", req.extras["top_level_keys"])
        self.assertIn("registrationInformation", req.text)

    def test_real_boarding_rest_example_page(self):
        if not SAMPLE.is_file():
            self.skipTest("boarding REST example sample missing")
        text = SAMPLE.read_text(encoding="utf-8")
        claims, _ = _extract_claims_from_text(
            text, source_pointer=SAMPLE.name, doc_stem=SAMPLE.stem
        )
        examples = [c for c in claims if c.schema == "rest_example"]
        self.assertGreaterEqual(len(examples), 2)
        self.assertTrue(any(c.extras.get("role") == "request" for c in examples))
        self.assertTrue(any(c.extras.get("role") == "response" for c in examples))


if __name__ == "__main__":
    unittest.main()
