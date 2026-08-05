"""Tests for Integration Success OS V0 assembler."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from relay_bench.content_engine.integration_success import (
    assemble_integration_success_pack,
    render_integration_success_markdown,
)

ROOT = Path(__file__).resolve().parents[1]


class IntegrationSuccessTests(unittest.TestCase):
    def test_assemble_pack_from_compiled_lanes(self):
        result = assemble_integration_success_pack(ensure_compiled=True)
        self.assertTrue(result["ok"])
        self.assertGreaterEqual(result["step_count"], 6)
        self.assertEqual(result["operation_count"], 8)
        self.assertGreaterEqual(result["test_scenario_count"], 8)
        self.assertEqual(result["checklist_count"], 5)

        pack_path = ROOT / result["pack_json"]
        md_path = ROOT / result["pack_md"]
        self.assertTrue(pack_path.exists())
        self.assertTrue(md_path.exists())

        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        self.assertEqual(pack["schema_version"], "relay.integration_success_pack.v0")
        self.assertIn("createPayment", pack["api_reference"]["operation_ids"])
        self.assertIn("checkMppEnrollment", pack["api_reference"]["operation_ids"])
        self.assertTrue(pack["guided_quickstart"]["steps"])
        self.assertTrue(pack["go_live_checklist"])
        self.assertEqual(pack["honest_label"]["network"], "denied")

        # No secret/PAN material.
        blob = json.dumps(pack).lower()
        for banned in ("4111111111111111", "shared_secret_value", "merchantsecretkey="):
            self.assertNotIn(banned, blob)

        md = md_path.read_text(encoding="utf-8")
        self.assertIn("Go-live checklist", md)
        self.assertIn("createPayment", md)
        self.assertIn("Local proof only", md)

    def test_markdown_renderer_includes_lineage(self):
        # Read the checked-in pack; do not reassemble with ensure_compiled=False
        # (that rewrites compile_results to null and dirties the proof artifact).
        pack_path = (
            ROOT
            / "artifacts"
            / "content_engine"
            / "integration_success"
            / "integration_success_pack.json"
        )
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        md = render_integration_success_markdown(pack)
        self.assertIn("Lineage", md)
        self.assertIn("Honesty", md)


if __name__ == "__main__":
    unittest.main()
