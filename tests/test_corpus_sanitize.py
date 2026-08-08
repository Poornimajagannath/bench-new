"""Tests for corpus sanitize: anchor lift, quarantine, code block fidelity."""

from __future__ import annotations

import re
import unittest

from content_bench.content_engine.corpus_sanitize import (
    classify_section_quarantine,
    extract_code_blocks,
    sanitize_root,
    validate_all_sections,
    validate_clean_body,
)
from content_bench.content_engine.source_noise import _ANCHOR_RE, _EMPTY_LINK_TITLE_RE


SAMPLE_ROOT = """
Merchant Boarding {#boarding-about-guide}
=====================================

For support information about any service, visit the Support Center:
[Support Center](https://example.com/support)

Recent Revisions to This Document {#boarding-revisions}
======================================================

| Date | Change |
|------|--------|
| 2026 | Editorial |

Introduction {#boarding-intro-overview}
======================================

Create a merchant using the API.

### Step 1 {#boarding-step1}

Run this request:

```json
{"merchant": {"name": "Test"}}
```

See also [docs](https://example.com/page "").
"""


class SanitizeBodyTests(unittest.TestCase):
    def test_no_raw_anchors_in_clean_body(self):
        sections, blocks, report = sanitize_root(
            SAMPLE_ROOT,
            root_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            product_id="boarding",
        )
        failures = validate_all_sections(sections)
        self.assertEqual(failures, {}, msg=str(failures))
        intro = next(s for s in sections if s.anchor == "boarding-intro-overview")
        self.assertNotRegex(intro.body, r"\{#")
        self.assertIn("boarding-intro-overview", intro.anchors_lifted)
        self.assertIn("#boarding-intro-overview", intro.deep_link)

    def test_no_empty_link_titles(self):
        sections, _, _ = sanitize_root(
            SAMPLE_ROOT,
            root_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            product_id="boarding",
        )
        intro = next(s for s in sections if s.anchor == "boarding-intro-overview")
        self.assertNotRegex(intro.body, r'\]\([^)]+\s+""\)')

    def test_validate_clean_body_catches_violations(self):
        bad = "Text with {#bad-anchor} still here"
        self.assertTrue(validate_clean_body(bad))
        bad2 = '[link](https://x.com "")'
        self.assertTrue(validate_clean_body(bad2))


class QuarantineTests(unittest.TestCase):
    def test_revision_history_quarantined(self):
        kind, reason = classify_section_quarantine(
            "Recent Revisions to This Document", "boarding-revisions", "| Date |"
        )
        self.assertEqual(kind, "revision_history")

    def test_about_guide_quarantined(self):
        kind, _ = classify_section_quarantine(
            "About This Guide", "about-guide", "Audience: developers"
        )
        self.assertEqual(kind, "about_guide_boilerplate")

    def test_support_center_quarantined(self):
        kind, _ = classify_section_quarantine(
            "Intro", "intro", "visit the Support Center for help"
        )
        self.assertEqual(kind, "support_center")

    def test_procedural_section_not_quarantined(self):
        sections, _, report = sanitize_root(
            SAMPLE_ROOT,
            root_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            product_id="boarding",
        )
        intro = next(s for s in sections if s.anchor == "boarding-intro-overview")
        self.assertFalse(intro.quarantined)
        self.assertGreater(report.sections_clean, 0)
        self.assertGreater(report.sections_quarantined, 0)


class CodeBlockTests(unittest.TestCase):
    def test_code_block_byte_exact_from_raw(self):
        sections, blocks, _ = sanitize_root(
            SAMPLE_ROOT,
            root_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            product_id="boarding",
        )
        self.assertGreaterEqual(len(blocks), 1)
        blk = blocks[0]
        self.assertEqual(blk.language, "json")
        self.assertIn('"merchant"', blk.raw_bytes)
        self.assertEqual(blk.nearest_anchor, "boarding-step1")

    def test_extract_preserves_inner_bytes(self):
        raw = '```python\nx = 1\n```'
        blocks = extract_code_blocks(raw, section_anchor="test")
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0].raw_bytes, "x = 1\n")


if __name__ == "__main__":
    unittest.main()
