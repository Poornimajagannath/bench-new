"""Tests for Milestone 0.5 ingestion snapshot."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from relay_bench.content_engine.ingest import (
    render_ingestion_report,
    run_ingestion_snapshot,
    stamp_copy_to_raw,
)

ROOT = Path(__file__).resolve().parents[1]


class IngestTests(unittest.TestCase):
    def test_offline_ingest_raw_normalized_and_drops(self):
        openapi = {
            "openapi": "3.0.0",
            "paths": {
                "/pts/v2/payments": {
                    "post": {
                        "operationId": "createPayment",
                        "parameters": [{"name": "id", "in": "query", "required": False, "schema": {"type": "string"}}],
                        "responses": {"201": {"description": "ok"}, "400": {"description": "bad"}},
                    }
                }
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            docs = tmp_path / "docs"
            docs.mkdir()
            (docs / "quickstart.md").write_text(
                "# Quickstart\n\n1. Install the SDK\n2. Create a payment\n\n"
                "POST /pts/v2/payments\n\nError 401 when JWT is missing.\n"
                "- You must verify the response code before capturing.\n",
                encoding="utf-8",
            )
            (docs / "home-merch.md").write_text(
                "# Home\n\nTable of contents\n\nRevision history\n",
                encoding="utf-8",
            )
            spec = tmp_path / "openapi.json"
            spec.write_text(json.dumps(openapi), encoding="utf-8")
            raw_root = tmp_path / "raw"
            normalized = tmp_path / "normalized"
            report = run_ingestion_snapshot(
                docs_dir=docs,
                raw_root=raw_root,
                normalized_root=normalized,
                openapi_path=spec,
                stamp_date="2026-08-07",
                sample_limit=10,
            )
            self.assertEqual(report["docs_fetched"], 2)
            self.assertGreaterEqual(report["claims_extracted"], 1)
            self.assertTrue((raw_root / "2026-08-07" / "quickstart.md").exists())
            meta = json.loads(
                (raw_root / "2026-08-07" / "quickstart.md.meta.json").read_text(encoding="utf-8")
            )
            self.assertIn("source_url", meta)
            self.assertIn("fetched_at", meta)
            claims_path = normalized / "2026-08-07.claims.json"
            self.assertTrue(claims_path.exists())
            payload = json.loads(claims_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["read_contract"]["forbidden"], ["raw/"])
            self.assertTrue(any(c["schema"] == "endpoint_fact" for c in payload["claims"]))
            self.assertGreaterEqual(report["drop_count"], 1)
            md = render_ingestion_report(report)
            self.assertIn("Drop log", md)

    def test_raw_is_immutable(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            src = tmp_path / "a.md"
            src.write_text("hello", encoding="utf-8")
            raw_root = tmp_path / "raw"
            stamp_copy_to_raw([src], raw_root=raw_root, stamp_date="2026-08-07")
            src.write_text("changed", encoding="utf-8")
            _, _, drops = stamp_copy_to_raw([src], raw_root=raw_root, stamp_date="2026-08-07")
            self.assertEqual((raw_root / "2026-08-07" / "a.md").read_text(encoding="utf-8"), "hello")
            self.assertTrue(any(d.reason == "raw_immutable_conflict" for d in drops))

    def test_read_contract_forbids_raw_for_serve_layers(self):
        report = {
            "stamp_date": "x",
            "docs_fetched": 0,
            "claims_extracted": 0,
            "claims_by_schema": {},
            "drop_count": 0,
            "drops": [],
            "raw_dir": "raw/x",
            "normalized_file": "normalized/x.claims.json",
            "read_contract": ["normalized/", "content/"],
            "forbidden_reads": ["raw/"],
        }
        md = render_ingestion_report(report)
        self.assertIn("Forbidden", md)


if __name__ == "__main__":
    unittest.main()
