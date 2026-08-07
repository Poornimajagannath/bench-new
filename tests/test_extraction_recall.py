"""Extraction recall: constraint prose on short pages; shell triage fields."""

from __future__ import annotations

import unittest
from pathlib import Path

from content_bench.content_engine.ingest import (
    _extract_claims_from_text,
    _first_heading,
    render_ingestion_report,
)

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "data" / "products" / "payments" / "guides"


class ExtractionRecallTests(unittest.TestCase):
    def _claims_for(self, name_substr: str):
        matches = list(GUIDES.glob(f"*{name_substr}*"))
        self.assertTrue(matches, f"missing guide matching {name_substr}")
        path = matches[0]
        text = path.read_text(encoding="utf-8")
        claims, drops = _extract_claims_from_text(
            text, source_pointer=path.name, doc_stem=path.stem
        )
        return path, text, claims, drops

    def test_da_payments_yields_ttl_and_reuse(self):
        _path, _text, claims, drops = self._claims_for("da-payments")
        self.assertFalse(drops, msg=f"unexpected drops: {drops}")
        blob = " ".join(c.text for c in claims).lower()
        self.assertTrue(any(c.schema == "prose_claim" for c in claims))
        self.assertIn("15 minute", blob)
        self.assertTrue("multiple times" in blob or "reuse" in blob)

    def test_microform_integ_yields_pci_encrypt_header(self):
        _path, _text, claims, drops = self._claims_for("microform-integ-v2")
        self.assertFalse(drops)
        blob = " ".join(c.text for c in claims).lower()
        self.assertIn("pci", blob)
        self.assertTrue("saq" in blob or "encrypt" in blob)
        self.assertIn("header", blob)

    def test_ctp_intro_yields_header_or_encrypt_constraint(self):
        _path, _text, claims, drops = self._claims_for("ctp-intro.md.md")
        # Prefer digital-accept-flex ctp-intro specifically
        path = GUIDES / (
            "en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro.md.md"
        )
        text = path.read_text(encoding="utf-8")
        claims, drops = _extract_claims_from_text(
            text, source_pointer=path.name, doc_stem=path.stem
        )
        self.assertFalse(drops, msg=f"unexpected drops: {drops}")
        blob = " ".join(c.text for c in claims).lower()
        self.assertTrue(
            "header" in blob or "encrypt" in blob or "limited-use" in blob or "limited use" in blob,
            msg=blob[:400],
        )

    def test_shell_drop_includes_bytes_and_heading(self):
        text = "Introduction to Foo {#foo-intro}\n====================\n\nSee these topics:\n\n* [A](/a.md)\n* [B](/b.md)\n"
        claims, drops = _extract_claims_from_text(
            text, source_pointer="foo-intro.md", doc_stem="foo-intro"
        )
        self.assertEqual(claims, [])
        self.assertEqual(len(drops), 1)
        self.assertEqual(drops[0].reason, "shell")
        self.assertIsNotNone(drops[0].bytes)
        self.assertTrue(drops[0].first_heading)
        self.assertIn("Introduction to Foo", drops[0].first_heading)

    def test_short_constraint_page_is_not_empty_by_length(self):
        text = (
            "Transient tokens {#tt}\n=================\n\n"
            "The transient token is valid for 15 minutes and may be reused within that window.\n"
        )
        claims, drops = _extract_claims_from_text(
            text, source_pointer="tt.md", doc_stem="tt"
        )
        self.assertFalse(drops)
        self.assertGreaterEqual(len(claims), 1)
        self.assertEqual(_first_heading(text), "Transient tokens")

    def test_report_lists_shell_triage_columns_and_sample(self):
        report = {
            "stamp_date": "x",
            "docs_fetched": 1,
            "claims_extracted": 0,
            "claims_by_schema": {},
            "drop_count": 1,
            "drops": [
                {
                    "path": "a.md",
                    "reason": "shell",
                    "detail": "triage",
                    "bytes": 120,
                    "first_heading": "Intro",
                }
            ],
            "raw_dir": "raw/x",
            "normalized_file": "normalized/x.claims.json",
            "read_contract": ["normalized/", "content/"],
            "forbidden_reads": ["raw/"],
            "human_check_sample": [
                {
                    "path": "a.md",
                    "reason": "shell",
                    "bytes": 120,
                    "first_heading": "Intro",
                }
            ],
        }
        md = render_ingestion_report(report)
        self.assertIn("First heading", md)
        self.assertIn("Sampled human check", md)
        self.assertIn("120", md)


if __name__ == "__main__":
    unittest.main()
