"""Tests for deep link verification against HTML fragment ids."""

from __future__ import annotations

import unittest

from content_bench.content_engine.deep_link_verify import (
    extract_html_fragment_ids,
    verify_deep_link,
)


class HtmlFragmentTests(unittest.TestCase):
    def test_extracts_id_and_name(self):
        html = '<h2 id="boarding-intro-overview">Intro</h2><a name="legacy"></a>'
        ids = extract_html_fragment_ids(html)
        self.assertIn("boarding-intro-overview", ids)
        self.assertIn("legacy", ids)


class VerifyDeepLinkTests(unittest.TestCase):
    def test_missing_anchor_on_empty_html(self):
        check = verify_deep_link(
            "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            "nonexistent-anchor-xyz",
            product_id="boarding",
            base_url="https://invalid.example.test",
        )
        self.assertFalse(check.anchor_found_in_html)


if __name__ == "__main__":
    unittest.main()
