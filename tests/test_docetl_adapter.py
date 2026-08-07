"""Tests for optional real DocETL adapter (code_map path; no LLM key required)."""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from unittest import mock

from content_bench.content_engine.docetl_adapter import (
    DocETLUnavailableError,
    docetl_available,
    extract_quickstart_units_with_backend,
    llm_api_key_present,
    normalize_extract_mode,
)
from content_bench.content_engine.normalize import normalize_document
from content_bench.content_engine.pipeline import run_content_engine
from content_bench.content_engine.registry import require_source
from content_bench.content_engine.segment import segment_document
from content_bench.content_engine.snapshot import materialize_snapshot
from content_bench.docetl_discovery import discover_suggestions_with_backend
from content_bench.discovery import load_raw_questions

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(docetl_available(), "docetl package not installed")
class DocETLAdapterTests(unittest.TestCase):
    def test_normalize_modes(self):
        self.assertEqual(normalize_extract_mode("heuristic"), "heuristic")
        self.assertEqual(normalize_extract_mode("docetl"), "docetl")
        self.assertEqual(normalize_extract_mode("code_map"), "docetl")
        self.assertEqual(normalize_extract_mode("docetl-llm"), "docetl-llm")
        with self.assertRaises(ValueError):
            normalize_extract_mode("harbor")

    def test_docetl_code_map_promotes_same_fixture(self):
        result = run_content_engine(
            "microform-payer-auth-quickstart",
            discovery="docetl",
        )
        self.assertTrue(result["ok"], result["issues"])
        self.assertEqual(result["honest_label"]["docetl"], "imported-code_map")
        self.assertGreaterEqual(result["unit_count"], 6)

        objects = ROOT / "artifacts/content_engine/objects/microform-payer-auth-quickstart.quickstart_units.json"
        payload = json.loads(objects.read_text(encoding="utf-8"))
        self.assertEqual(payload["extractor_label"], "imported-code_map")
        self.assertIn("imported", payload["inspired_by"])

    def test_docetl_code_map_matches_heuristic_step_count(self):
        record = require_source("microform-payer-auth-quickstart")
        snapshot = materialize_snapshot(record)
        doc = normalize_document(record, snapshot)
        segments = segment_document(doc)

        heuristic_units, h_label = extract_quickstart_units_with_backend(
            record, doc, segments, mode="heuristic"
        )
        docetl_units, d_label = extract_quickstart_units_with_backend(
            record, doc, segments, mode="docetl"
        )
        self.assertEqual(h_label["docetl"], "style-only")
        self.assertEqual(d_label["docetl"], "imported-code_map")
        self.assertEqual(
            [u.unit_type for u in heuristic_units],
            [u.unit_type for u in docetl_units],
        )
        self.assertEqual(
            [u.sequence_number for u in heuristic_units if u.unit_type == "step"],
            [u.sequence_number for u in docetl_units if u.unit_type == "step"],
        )

    def test_docetl_llm_without_key_fails_honestly(self):
        if llm_api_key_present():
            self.skipTest("LLM API key present; cannot assert missing-key failure")
        record = require_source("microform-payer-auth-quickstart")
        snapshot = materialize_snapshot(record)
        doc = normalize_document(record, snapshot)
        segments = segment_document(doc)
        with self.assertRaises(DocETLUnavailableError):
            extract_quickstart_units_with_backend(
                record, doc, segments, mode="docetl-llm"
            )

    def test_docetl_llm_fallback_labels_honesty(self):
        if llm_api_key_present():
            self.skipTest("LLM API key present; skip fallback path")
        record = require_source("microform-payer-auth-quickstart")
        snapshot = materialize_snapshot(record)
        doc = normalize_document(record, snapshot)
        segments = segment_document(doc)
        units, label = extract_quickstart_units_with_backend(
            record,
            doc,
            segments,
            mode="docetl-llm",
            fallback_on_error=True,
        )
        self.assertTrue(units)
        self.assertEqual(label["docetl"], "style-only")
        self.assertIn("fallback-to-heuristic", label.get("detail", ""))

    def test_discovery_docetl_code_map(self):
        questions = load_raw_questions()[:3]
        rows, label = discover_suggestions_with_backend(
            questions=questions, mode="docetl"
        )
        self.assertEqual(label["docetl"], "imported-code_map")
        self.assertEqual(len(rows), len(questions))
        for question, extraction, suggestion in rows:
            self.assertEqual(extraction.seed_id, question.seed_id)
            self.assertTrue(extraction.goal)
            self.assertTrue(suggestion.suggested_workflow_id)

    def test_missing_package_raises_or_falls_back(self):
        record = require_source("microform-payer-auth-quickstart")
        snapshot = materialize_snapshot(record)
        doc = normalize_document(record, snapshot)
        segments = segment_document(doc)
        with mock.patch.dict("sys.modules", {"docetl": None}):
            # Force import failure inside adapter by patching import path.
            with mock.patch(
                "content_bench.content_engine.docetl_adapter._extract_via_code_map",
                side_effect=DocETLUnavailableError("docetl package is not installed"),
            ):
                with self.assertRaises(DocETLUnavailableError):
                    extract_quickstart_units_with_backend(
                        record, doc, segments, mode="docetl"
                    )
                units, label = extract_quickstart_units_with_backend(
                    record,
                    doc,
                    segments,
                    mode="docetl",
                    fallback_on_error=True,
                )
                self.assertTrue(units)
                self.assertEqual(label["docetl"], "style-only")


class HeuristicDefaultStillHonest(unittest.TestCase):
    def test_default_pipeline_stays_style_only(self):
        result = run_content_engine("microform-payer-auth-quickstart")
        self.assertTrue(result["ok"], result["issues"])
        self.assertEqual(result["honest_label"]["docetl"], "style-only")


if __name__ == "__main__":
    unittest.main()
