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


class EndpointUrlStyleTests(unittest.TestCase):
    """Loop C1: backticked full-URL endpoint lines must yield endpoint_fact."""

    def test_backticked_full_url_endpoint(self):
        text = (
            "Create a Merchant Organization {#x}\n=====================\n\n"
            "**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`\n"
            "**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`\n"
        )
        claims, drops = _extract_claims_from_text(
            text, source_pointer="x.md", doc_stem="x"
        )
        eps = [c for c in claims if c.schema == "endpoint_fact"]
        self.assertEqual(len(eps), 2, msg=[c.text for c in claims])
        envs = {c.extras.get("environment") for c in eps}
        self.assertEqual(envs, {"production", "test"})
        self.assertFalse(drops)

    def test_bare_verb_path_still_works(self):
        text = "# T\n\nSend a POST /pts/v2/payments request with the body below.\n"
        claims, _ = _extract_claims_from_text(
            text, source_pointer="x.md", doc_stem="x"
        )
        eps = [c for c in claims if c.schema == "endpoint_fact"]
        self.assertEqual(len(eps), 1)
        self.assertEqual(eps[0].extras["path"], "/pts/v2/payments")


class StepAnchorTests(unittest.TestCase):
    """Anchors are deep-link data: out of claim text, into extras."""

    def test_anchor_lifted_to_metadata(self):
        text = (
            "# Guide\n\n"
            "1. Click the Portfolio Management icon in the pane.{#merchants-v2-step1}\n"
        )
        claims, _ = _extract_claims_from_text(
            text,
            source_pointer="en-us_boarding_user_all_ebc_x.md.md",
            doc_stem="x",
        )
        steps = [c for c in claims if c.schema == "quickstart_step"]
        self.assertEqual(len(steps), 1)
        self.assertNotIn("{#", steps[0].text)
        self.assertEqual(steps[0].extras.get("anchor"), "merchants-v2-step1")
        self.assertIn("merchants-v2-step1", steps[0].extras.get("deep_link") or "")


if __name__ == "__main__":
    unittest.main()
