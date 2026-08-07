"""Corpus census classification + quarantine policy."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from content_bench.content_engine.corpus_census import (
    DEFAULT_QUARANTINE_KINDS,
    classify_document,
    load_quarantine_policy,
    render_census_markdown,
    render_quarantine_markdown,
    run_corpus_census,
)


class CorpusCensusTests(unittest.TestCase):
    def test_release_note_from_filename(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "en-us_platform_relnote_all_na_rn-2026-05-01_rn-general.md.md"
            p.write_text("# Release Notes\n\nGeneral updates.\n", encoding="utf-8")
            c = classify_document(p)
            self.assertEqual(c.kind, "release_note")

    def test_legal_from_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "site-policy.md"
            p.write_text("# Privacy Policy\n\nWe collect account data.\n", encoding="utf-8")
            c = classify_document(p)
            self.assertEqual(c.kind, "legal")

    def test_index_intro_stub(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "en-us_boarding_developer_all_rest_boarding_boarding-intro-overview.md.md"
            p.write_text(
                "Introduction to the Boarding Registration Service {#boarding-intro-overview}\n"
                "Icon\n\n"
                "To understand accounts, see these topics:\n\n"
                "* [Understanding Accounts](/docs/cybs/en-us/boarding/a.md)\n"
                "* [Extending the Hierarchy](/docs/cybs/en-us/boarding/b.md)\n",
                encoding="utf-8",
            )
            c = classify_document(p)
            self.assertEqual(c.kind, "index_navigation")

    def test_api_reference_from_filename(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "en-us_api-fields_reference_all_rest_api-fields.md.md"
            p.write_text(
                "# REST API Field Reference\n\n"
                "This section provides information about request and reply fields.\n"
                + ("field details\n" * 40),
                encoding="utf-8",
            )
            c = classify_document(p)
            self.assertEqual(c.kind, "api_reference")

    def test_how_to_from_procedure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "create-registration.md"
            p.write_text(
                "# Create a Boarding Registration\n\n"
                "Follow these steps to create a registration.\n\n"
                "Step 1 Send a POST /boarding/v1/registrations request.\n"
                + ("more procedure text\n" * 30),
                encoding="utf-8",
            )
            c = classify_document(p)
            self.assertEqual(c.kind, "how_to_guide")

    def test_developer_in_path_alone_is_not_how_to(self) -> None:
        """CS paths almost always contain `developer`; that must not force how-to."""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "en-us_apple-pay_developer_all_rest_applepay_applepay-intro.md.md"
            p.write_text(
                "Introduction to Apple Pay {#applepay-intro}\n\n"
                "See these topics:\n\n"
                "* [Getting Started](/docs/a.md)\n"
                "* [Configuration](/docs/b.md)\n",
                encoding="utf-8",
            )
            c = classify_document(p)
            self.assertEqual(c.kind, "index_navigation")

    def test_default_policy_excludes_release_legal_index(self) -> None:
        self.assertEqual(
            set(DEFAULT_QUARANTINE_KINDS),
            {"release_note", "legal", "index_navigation"},
        )
        pol = load_quarantine_policy(None)
        self.assertIn("release_note", pol["exclude_kinds"])

    def test_census_publishes_counts_and_quarantine(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "en-us_doc-rel_relnote_all_na_doc-release-notes.md.md").write_text(
                "# Document Release Notes\n\nNotes.\n", encoding="utf-8"
            )
            (root / "privacy-policy.md").write_text(
                "# Privacy Policy\n\nLegal text.\n", encoding="utf-8"
            )
            (root / "guide-getting-started.md").write_text(
                "# Getting Started\n\nFollow these steps to integrate.\n"
                "Step 1 call POST /pts/v2/payments\n" + ("x\n" * 40),
                encoding="utf-8",
            )
            (root / "en-us_foo_intro.md.md").write_text(
                "Introduction to Foo\n\nSee these topics:\n\n"
                "* [A](/a.md)\n* [B](/b.md)\n",
                encoding="utf-8",
            )
            result = run_corpus_census(root)
            self.assertEqual(result["doc_count"], 4)
            self.assertGreaterEqual(result["counts_by_kind"]["release_note"], 1)
            self.assertGreaterEqual(result["counts_by_kind"]["legal"], 1)
            self.assertGreaterEqual(result["counts_by_kind"]["index_navigation"], 1)
            self.assertGreaterEqual(result["quarantine_count"], 3)
            self.assertGreaterEqual(result["eligible_count"], 1)
            md = render_census_markdown(result)
            self.assertIn("Counts by kind", md)
            qmd = render_quarantine_markdown(result)
            self.assertIn("excluded from ingestion by policy", qmd)
            # Eligible guide must not appear on quarantine list
            qpaths = {r["path"] for r in result["quarantine_list"]}
            self.assertNotIn("guide-getting-started.md", qpaths)


if __name__ == "__main__":
    unittest.main()
