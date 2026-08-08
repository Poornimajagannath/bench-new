"""One corpus definition: census eligible set == ingestion input set.

Same spirit as the triage identity test — a disagreement between census and
ingest is a failing test, not a silent 3-of-182 ingest.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from content_bench.content_engine.corpus_census import run_corpus_census
from content_bench.content_engine.ingest import (
    CorpusMismatchError,
    select_ingest_sources_from_census,
)


def _make_corpus(root: Path) -> None:
    (root / "guide-create-org.md").write_text(
        "# Create an Organization\n\nFollow these steps to create one.\n"
        "Step 1 Send a POST /boarding/v1/registrations request.\n"
        + ("procedure detail\n" * 30),
        encoding="utf-8",
    )
    (root / "guide-token-ttl.md").write_text(
        "Transient tokens\n===============\n\n"
        "The token is valid for 15 minutes and may be reused in that window.\n",
        encoding="utf-8",
    )
    (root / "en-us_foo_intro.md.md").write_text(
        "Introduction to Foo\n\nSee these topics:\n\n* [A](/a.md)\n* [B](/b.md)\n",
        encoding="utf-8",
    )
    (root / "site-privacy.md").write_text(
        "# Privacy Policy\n\nLegal text.\n", encoding="utf-8"
    )


class CorpusParityTests(unittest.TestCase):
    def test_census_eligible_equals_ingest_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _make_corpus(root)
            result = run_corpus_census(root)
            census_path = root / "census-report.json"
            census_path.write_text(json.dumps(result), encoding="utf-8")

            srcs, drops = select_ingest_sources_from_census(
                census_path, docs_dir=root
            )
            self.assertEqual(len(srcs), result["eligible_count"])
            self.assertEqual(
                len(drops), result["quarantine_count"],
                "every quarantined doc must appear as a quarantine_policy drop",
            )
            self.assertTrue(all(d.reason == "quarantine_policy" for d in drops))
            # Roster is exactly the eligible classifications
            eligible_names = {
                row["path"]
                for row in result["classifications"]
                if not row["quarantined"]
            }
            self.assertEqual({p.name for p in srcs}, eligible_names)

    def test_navigation_lines_are_not_steps(self) -> None:
        from content_bench.content_engine.ingest import _extract_claims_from_text

        text = (
            "# Boarding Overview\n\n"
            "1. Create the organization. See [Create Organizations](/docs/a.md).\n"
            "2. [Manage Organizations](/docs/b.md)\n"
            "3. Enter a unique name for the template, and then click Next.\n"
        )
        claims, _ = _extract_claims_from_text(
            text, source_pointer="x.md", doc_stem="x"
        )
        steps = [c for c in claims if c.schema == "quickstart_step"]
        self.assertEqual(len(steps), 1, msg=[c.title for c in steps])
        self.assertIn("unique name", steps[0].title)

    def test_step_ids_unique_across_sections(self) -> None:
        from content_bench.content_engine.ingest import _extract_claims_from_text

        text = (
            "# Guide\n\n## Task A\n\n"
            "1. Click the Portfolio Management icon in the pane.\n"
            "## Task B\n\n"
            "1. Click the Token Management icon in the pane.\n"
        )
        claims, _ = _extract_claims_from_text(
            text, source_pointer="x.md", doc_stem="x"
        )
        steps = [c for c in claims if c.schema == "quickstart_step"]
        self.assertEqual(len(steps), 2)
        self.assertNotEqual(steps[0].claim_id, steps[1].claim_id)

    def test_claim_ids_unique_within_doc(self) -> None:
        from content_bench.content_engine.ingest import _extract_claims_from_text

        text = (
            "# Guide\n\nAn error message appears if the ID is DUPLICATED here.\n"
            "Later, an error message appears if the ID is DUPLICATED here.\n"
        )
        claims, _ = _extract_claims_from_text(
            text, source_pointer="x.md", doc_stem="x"
        )
        ids = [c.claim_id for c in claims]
        self.assertEqual(len(ids), len(set(ids)), msg=ids)

    def test_mismatch_fails_loudly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _make_corpus(root)
            result = run_corpus_census(root)
            census_path = root / "census-report.json"
            census_path.write_text(json.dumps(result), encoding="utf-8")
            # Corpus changes after the census: a file disappears.
            (root / "guide-token-ttl.md").unlink()
            with self.assertRaises(CorpusMismatchError):
                select_ingest_sources_from_census(census_path, docs_dir=root)


if __name__ == "__main__":
    unittest.main()
