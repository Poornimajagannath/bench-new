"""Tests for Milestone 0 source-mix inventory."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from relay_bench.content_engine.source_mix import (
    analyze_source_mix,
    render_source_mix_markdown,
)

ROOT = Path(__file__).resolve().parents[1]


class SourceMixTests(unittest.TestCase):
    def test_fixture_corpus_scores_and_top_prose(self):
        openapi = {
            "openapi": "3.0.0",
            "paths": {
                "/pts/v2/payments": {
                    "post": {
                        "operationId": "createPayment",
                        "parameters": [{"name": "Authorization", "in": "header", "required": True}],
                        "responses": {"201": {"description": "Created"}, "401": {"description": "Auth"}},
                    }
                }
            },
            "components": {"securitySchemes": {"httpSignature": {"type": "apiKey"}}},
        }
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            spec = tmp_path / "openapi.json"
            spec.write_text(json.dumps(openapi), encoding="utf-8")
            docs = tmp_path / "docs"
            docs.mkdir()
            (docs / "auth-guide.md").write_text(
                "# Auth\n\n## Before you begin\nYou must load JWT credentials.\n"
                "## Create a payment\nPOST /pts/v2/payments with Authorization header.\n"
                "## Gotcha\nSandbox does not simulate production retries.\n",
                encoding="utf-8",
            )
            (docs / "index-home.md").write_text(
                "# Index\n\nTable of contents\n\nRevision history\n",
                encoding="utf-8",
            )
            result = analyze_source_mix(
                openapi_path=spec,
                docs_dir=docs,
                sample_limit=10,
            )
            self.assertEqual(result["docs_sampled"], 2)
            self.assertIn("decision_rule", result)
            self.assertGreaterEqual(len(result["top_prose_sections"]), 1)
            md = render_source_mix_markdown(result)
            self.assertIn("Source mix report", md)
            self.assertIn("Per-guide table", md)
            self.assertIn("Top 10 prose-only sections", md)

    def test_real_openapi_loads(self):
        spec = ROOT / "data/content_engine/specs/payments-core.openapi.json"
        self.assertTrue(spec.exists())
        result = analyze_source_mix(
            openapi_path=spec,
            docs_dir=ROOT / "gateway-docs",
            sample_limit=5,
        )
        self.assertGreaterEqual(result["docs_sampled"], 1)


if __name__ == "__main__":
    unittest.main()
