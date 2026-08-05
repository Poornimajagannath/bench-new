"""Tests for Relay Content Engine V0 prototype."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from relay_bench.content_engine.extract import extract_quickstart_units
from relay_bench.content_engine.normalize import normalize_document
from relay_bench.content_engine.pipeline import run_content_engine
from relay_bench.content_engine.registry import require_source
from relay_bench.content_engine.segment import segment_document
from relay_bench.content_engine.snapshot import materialize_snapshot
from relay_bench.content_engine.validate import validate_content, validate_schema
from relay_bench.content_engine.schemas import QuickstartUnit

ROOT = Path(__file__).resolve().parents[1]


class ContentEngineTests(unittest.TestCase):
    def test_registry_loads_fixture_source(self):
        record = require_source("microform-payer-auth-quickstart")
        self.assertEqual(record.source_type, "quickstart")
        self.assertEqual(
            record.linked_workflow_id,
            "microform-payer-auth-state-machine",
        )
        self.assertTrue((ROOT / record.repo_path).exists())

    def test_pipeline_promotes_quickstart_and_writes_context_pack(self):
        result = run_content_engine("microform-payer-auth-quickstart")
        self.assertTrue(result["ok"], result["issues"])
        self.assertEqual(result["promotion_status"], "promoted")
        self.assertGreaterEqual(result["unit_count"], 6)
        self.assertTrue(result["schema_passed"])
        self.assertTrue(result["content_passed"])
        self.assertIn(result["agent_use_status"], {"passed", "deferred"})

        ctx = ROOT / result["context_pack_path"]
        self.assertTrue(ctx.exists())
        pack = json.loads(ctx.read_text(encoding="utf-8"))
        self.assertEqual(pack["source_id"], "microform-payer-auth-quickstart")
        self.assertTrue(pack["unit_ids"])
        self.assertIn("snapshot_id", pack["provenance"])
        self.assertEqual(
            pack["linked_workflow_id"],
            "microform-payer-auth-state-machine",
        )

        # No secret/PAN material in promoted pack.
        blob = json.dumps(pack).lower()
        for banned in ("shared_secret", "merchantsecretkey", "4111"):
            self.assertNotIn(banned, blob)

    def test_extract_emits_ordered_steps_with_evidence(self):
        record = require_source("microform-payer-auth-quickstart")
        snapshot = materialize_snapshot(record)
        doc = normalize_document(record, snapshot)
        segments = segment_document(doc)
        units = extract_quickstart_units(record, doc, segments)
        steps = [u for u in units if u.unit_type == "step"]
        self.assertGreaterEqual(len(steps), 6)
        self.assertEqual([s.sequence_number for s in steps], list(range(1, len(steps) + 1)))
        self.assertTrue(all(s.evidence_quotes for s in steps))

        schema_ok, schema_issues = validate_schema(units)
        content_ok, content_issues = validate_content(units)
        self.assertTrue(schema_ok, schema_issues)
        self.assertTrue(content_ok, content_issues)

    def test_validation_blocks_promotion_without_evidence(self):
        bad = QuickstartUnit(
            unit_id="bad:step:1",
            source_page_id="doc-x",
            unit_type="step",
            title="Broken step",
            goal="demo",
            product=["x"],
            audience=["developer"],
            task=["x"],
            sequence_number=1,
            body_markdown="no grounding",
            evidence_quotes=[],
            requires=["something"],
        )
        schema_ok, _ = validate_schema([bad])
        content_ok, issues = validate_content([bad])
        self.assertTrue(schema_ok)
        self.assertFalse(content_ok)
        self.assertTrue(any(i.code == "missing_evidence" for i in issues))

    def test_snapshot_is_content_addressed(self):
        record = require_source("microform-payer-auth-quickstart")
        first = materialize_snapshot(record)
        second = materialize_snapshot(record)
        self.assertEqual(first.content_hash, second.content_hash)
        self.assertEqual(first.snapshot_id, second.snapshot_id)
        self.assertTrue((ROOT / first.raw_bytes_location).exists())


if __name__ == "__main__":
    unittest.main()
