"""Product-root fetch: derivation, section split, TOC cross-check."""

from __future__ import annotations

import unittest
import unittest.mock

from content_bench.content_engine.product_roots import (
    derive_bare_family_root,
    derive_family_repeat_root,
    derive_guide_dir_root,
    derive_product_root,
    generate_root_candidates,
    parse_docs_md_products,
    pick_candidate_offline,
    probe_and_pick_root,
    split_root_sections,
    toc_page_covered_by_root,
)


DOCS_SNIPPET = """
[<br />
Accept Payments
Learn how
<br />
<br />](/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md)
[<br />
Token Management
TMS
<br />
<br />](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-overview.md)
[<br />
ACH
PDF
<br />
<br />](/content/dam/new-documentation/documentation/en/e-checks/developer/all/so/e-checks-so.pdf)
"""


class DerivationTests(unittest.TestCase):
    def test_family_repeat_boarding_payments_tms(self):
        cases = [
            (
                "/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro.md",
                "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            ),
            (
                "/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md",
                "/docs/cybs/en-us/payments/developer/ctv/rest/payments.md",
            ),
            (
                "/docs/cybs/en-us/tms/developer/all/rest/tms/tms-overview.md",
                "/docs/cybs/en-us/tms/developer/all/rest/tms.md",
            ),
        ]
        for intro, expected in cases:
            self.assertEqual(derive_family_repeat_root(intro), expected)
            chosen, how, _, _ = derive_product_root(intro)
            self.assertEqual(chosen, expected)
            self.assertEqual(how, "family_repeat")

    def test_guide_dir_when_family_does_not_repeat(self):
        intro = (
            "/docs/cybs/en-us/echeck/user/all/rest/"
            "echeck-user-guide/echeck-txnprocess-intro.md"
        )
        self.assertIsNone(derive_family_repeat_root(intro))
        self.assertEqual(
            derive_guide_dir_root(intro),
            "/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide.md",
        )
        chosen, how, _, _ = derive_product_root(intro)
        self.assertEqual(how, "guide_dir")
        self.assertTrue(chosen.endswith("/echeck-user-guide.md"))

    def test_listed_root_when_parent_is_generic_rest(self):
        """llms lists …/rest/applepay.md — must not promote to …/rest.md."""
        intro = "/docs/cybs/en-us/apple-pay/developer/all/rest/applepay.md"
        chosen, how, _, _ = derive_product_root(intro)
        self.assertEqual(chosen, intro)
        self.assertEqual(how, "listed_root")

    def test_listed_root_template_mgmt(self):
        intro = (
            "/docs/cybs/en-us/boarding-template-management/user/all/ada/"
            "boarding-template-mgmt.md"
        )
        chosen, how, _, _ = derive_product_root(intro)
        self.assertEqual(chosen, intro)
        self.assertEqual(how, "listed_root")

    def test_compendium_collapse_release_notes(self):
        intro = (
            "/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/"
            "doc-release-notes-intro/April-2025.md"
        )
        chosen, how, _, _ = derive_product_root(intro)
        self.assertEqual(
            chosen,
            "/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes.md",
        )
        self.assertEqual(how, "compendium")

    def test_bare_family_root(self):
        intro = (
            "/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro.md"
        )
        self.assertEqual(
            derive_bare_family_root(intro),
            "/docs/cybs/en-us/boarding/boarding.md",
        )

    def test_pick_candidate_offline_prefers_family_repeat(self):
        intro = (
            "/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md"
        )
        cands = generate_root_candidates(intro)
        chosen, shape = pick_candidate_offline(cands)
        self.assertEqual(shape, "family_repeat")
        self.assertTrue(chosen.endswith("/payments.md"))

    def test_probe_and_pick_prefers_most_anchors(self):
        intro = "/docs/cybs/en-us/foo/developer/all/rest/foo/sub.md"
        cands = generate_root_candidates(intro)
        bodies = {
            "/docs/cybs/en-us/foo/foo.md": "A {#a1}\n\n" + "x" * 100,
            "/docs/cybs/en-us/foo/developer/all/rest/foo.md": (
                "A {#a1}\n\nB {#a2}\n\nC {#a3}\n\n" + "y" * 50
            ),
        }

        def fake_probe(path, **kwargs):
            from content_bench.content_engine.product_roots import CandidateProbe

            text = bodies.get(path, "")
            if not text:
                return CandidateProbe(path=path, shape="", http_status=404, discard_reason="404")
            anchors = text.count("{#")
            return CandidateProbe(
                path=path,
                shape="",
                http_status=200,
                bytes=len(text.encode()),
                anchor_count=anchors,
                valid=True,
            )

        with unittest.mock.patch(
            "content_bench.content_engine.product_roots.probe_candidate_full",
            side_effect=fake_probe,
        ):
            chosen, shape, probes = probe_and_pick_root(cands, sleep_s=0)
        self.assertEqual(
            chosen,
            "/docs/cybs/en-us/foo/developer/all/rest/foo.md",
        )
        self.assertGreater(
            next(p for p in probes if p.path == chosen).anchor_count,
            1,
        )

    def test_pdf_not_md(self):
        chosen, how, _, _ = derive_product_root(
            "/content/dam/new-documentation/documentation/en/e-checks/developer/all/so/e-checks-so.pdf"
        )
        self.assertIsNone(chosen)
        self.assertEqual(how, "not_md")


class ParseDocsTests(unittest.TestCase):
    def test_parses_unique_cards(self):
        products = parse_docs_md_products(DOCS_SNIPPET)
        self.assertEqual(len(products), 3)
        self.assertEqual(products[0].title, "Accept Payments")
        self.assertTrue(products[0].intro_path.endswith("payments-intro.md"))


class SplitTests(unittest.TestCase):
    def test_splits_underline_and_atx_anchors(self):
        text = (
            "Merchant Boarding {#boarding-about-guide}\n"
            "=========================================\n"
            "\n"
            "Intro prose here.\n"
            "\n"
            "### Nested {#nested-anchor}\n"
            "\n"
            "Nested body.\n"
            "\n"
            "Next Topic {#next-topic}\n"
            "=======================\n"
            "\n"
            "Tail.\n"
        )
        sections = split_root_sections(
            text,
            root_path="/docs/cybs/en-us/boarding/developer/all/rest/boarding.md",
            base_url="https://developer.cybersource.com",
        )
        self.assertEqual(len(sections), 3)
        self.assertEqual(sections[0].anchor, "boarding-about-guide")
        self.assertEqual(sections[0].title, "Merchant Boarding")
        self.assertEqual(sections[0].byte_start, 0)
        self.assertEqual(
            sections[0].deep_link,
            "https://developer.cybersource.com/docs/cybs/en-us/boarding/"
            "developer/all/rest/boarding.html#boarding-about-guide",
        )
        self.assertEqual(sections[1].anchor, "nested-anchor")
        self.assertEqual(sections[1].heading_level, 3)
        self.assertEqual(sections[2].anchor, "next-topic")
        self.assertEqual(sections[-1].byte_end, len(text.encode("utf-8")))
        # byte ranges cover the file without gaps between sections
        for i in range(len(sections) - 1):
            self.assertEqual(sections[i].byte_end, sections[i + 1].byte_start)


class CrossCheckTests(unittest.TestCase):
    def test_anchor_overlap_counts_as_covered(self):
        root = "Title {#a1}\n====\n\nShared body about merchants.\n"
        page = "Title {#a1}\n====\n\nShared body about merchants.\n"
        self.assertTrue(toc_page_covered_by_root(page, root, {"a1"}))

    def test_missing_content_is_gap(self):
        root = "Title {#a1}\n====\n\nOnly root material here forever.\n"
        page = (
            "Orphan Page {#orphan}\n===========\n\n"
            "Completely different prose that never appears in the root document at all.\n"
        )
        self.assertFalse(toc_page_covered_by_root(page, root, {"a1"}))


if __name__ == "__main__":
    unittest.main()
