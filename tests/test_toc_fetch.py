"""TOC fetch module: denominator from the family TOC; llms.txt is a hint."""

from __future__ import annotations

import unittest

from content_bench.content_engine.toc_fetch import (
    extract_toc_topics,
    looks_like_markdown,
    topic_id,
    url_to_local_name,
)

BASE = "https://docs.example.com"


class TocDenominatorTests(unittest.TestCase):
    def test_extracts_family_topics_only(self):
        html = (
            '<a href="/docs/x/en-us/boarding/rest/boarding/a.html">A</a>'
            '<a href="/docs/x/en-us/boarding/rest/boarding/b.md">B</a>'
            '<a href="/docs/x/en-us/payments/rest/p.html">other family</a>'
            '<a href="mailto:x@y.z">mail</a>'
            '<a href="//cdn.example.com/app.js">asset</a>'
        )
        topics = extract_toc_topics(html, BASE, "/en-us/boarding/rest/boarding")
        self.assertEqual(
            topics,
            [
                "/docs/x/en-us/boarding/rest/boarding/a",
                "/docs/x/en-us/boarding/rest/boarding/b",
            ],
        )

    def test_md_and_html_collapse_to_one_topic(self):
        html = (
            '<a href="/docs/x/boarding/a.html">A</a>'
            '<a href="/docs/x/boarding/a.md">A md</a>'
        )
        topics = extract_toc_topics(html, BASE, "/boarding/")
        self.assertEqual(topics, ["/docs/x/boarding/a"])

    def test_topic_id_strips_extensions(self):
        self.assertEqual(topic_id("/d/a.md"), "/d/a")
        self.assertEqual(topic_id("/d/a.html"), "/d/a")
        self.assertEqual(topic_id("/d/a"), "/d/a")


class LocalNameTests(unittest.TestCase):
    def test_strip_prefix_and_flatten(self):
        self.assertEqual(
            url_to_local_name("/docs/cybs/en-us/boarding/a", strip_prefix="/docs/cybs/"),
            "en-us_boarding_a.md.md",
        )


class MarkdownSniffTests(unittest.TestCase):
    def test_rejects_html_document(self):
        self.assertFalse(looks_like_markdown("<!DOCTYPE html><html><body>x</body>"))

    def test_rejects_site_chrome(self):
        self.assertFalse(
            looks_like_markdown(
                "[Skip to login](#login)\n[Skip to content](#main)\nnav nav nav"
            )
        )

    def test_accepts_dita_markdown(self):
        text = "Title {#anchor}\n" + "=" * 20 + "\n\nBody sentence about tokens.\n"
        self.assertTrue(looks_like_markdown(text))


if __name__ == "__main__":
    unittest.main()
