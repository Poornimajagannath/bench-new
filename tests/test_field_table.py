"""field_table schema: template-matrix reference rows extract as claims."""

from __future__ import annotations

import unittest

from content_bench.content_engine.ingest import _extract_claims_from_text


TABLE_PAGE = (
    "ACH Templates {#templates-matrix-echeck}\n"
    "========================================\n\n"
    "Select configuration options for these fields:\n\n"
    "| Field                       | Value or Option |\n"
    "|:----------------------------|:----------------|\n"
    "| echeck Processor            | Bofa ACH        |\n"
    "| Company ID                  | Merchant's ID assigned by the acquiring bank. |\n"
    "[ACH Template Configuration Options]\n"
)


class FieldTableTests(unittest.TestCase):
    def test_rows_become_field_table_claims(self):
        claims, drops = _extract_claims_from_text(
            TABLE_PAGE, source_pointer="ach.md", doc_stem="ach"
        )
        self.assertFalse(drops)
        rows = [c for c in claims if c.schema == "field_table"]
        self.assertEqual(len(rows), 2)
        blob = " ".join(c.text for c in rows)
        self.assertIn("echeck Processor: Bofa ACH", blob)
        self.assertIn("Company ID", blob)
        self.assertTrue(all(c.extras.get("field") for c in rows))
        ids = [c.claim_id for c in claims]
        self.assertEqual(len(ids), len(set(ids)))

    def test_separator_and_caption_are_not_rows(self):
        claims, _ = _extract_claims_from_text(
            TABLE_PAGE, source_pointer="ach.md", doc_stem="ach"
        )
        rows = [c for c in claims if c.schema == "field_table"]
        for c in rows:
            self.assertNotIn("---", c.text)
            self.assertNotIn("Configuration Options]", c.text)

    def test_table_context_carried(self):
        claims, _ = _extract_claims_from_text(
            TABLE_PAGE, source_pointer="ach.md", doc_stem="ach"
        )
        rows = [c for c in claims if c.schema == "field_table"]
        self.assertTrue(all("ACH Templates" in (c.extras.get("table") or "") for c in rows))


if __name__ == "__main__":
    unittest.main()
