"""Tests for llms-first corpus discovery and unfetchable classification."""

from __future__ import annotations

import unittest

from content_bench.content_engine.corpus_discovery import (
    REASON_DERIVATION_ERROR,
    REASON_EMPTY_200,
    REASON_HUB_PAGE,
    REASON_PDF,
    REASON_SITE_DEFECT,
    classify_unfetchable,
    discover_roots_from_llms,
    extract_llms_urls,
)


LLMS_SNIPPET = """
## Payments
- [Payments](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md)
- [Boarding sub](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-overview.md)
## ACH
- [ACH PDF](https://developer.cybersource.com/content/dam/new-documentation/documentation/en/e-checks/developer/all/so/e-checks-so.pdf)
## Hub
- [Accept](https://developer.cybersource.com/accept-payments.md)
"""


class ExtractUrlsTests(unittest.TestCase):
    def test_extracts_md_and_pdf(self):
        md, pdf = extract_llms_urls(LLMS_SNIPPET)
        self.assertEqual(len(md), 3)
        self.assertEqual(len(pdf), 1)
        self.assertTrue(any("payments-intro.md" in u for u in md))
        self.assertTrue(any("e-checks-so.pdf" in u for u in pdf))


class DeriveRootsTests(unittest.TestCase):
    def test_dedupes_subtopics_to_family_root(self):
        roots, md, pdf, docs_only = discover_roots_from_llms(LLMS_SNIPPET)
        self.assertEqual(len(pdf), 1)
        payment_root = "/docs/cybs/en-us/payments/developer/ctv/rest/payments.md"
        boarding_root = "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md"
        self.assertIn(payment_root, roots)
        self.assertIn(boarding_root, roots)
        self.assertGreaterEqual(roots[payment_root].sample_urls, 1)
        self.assertEqual(roots[payment_root].winning_shape, "family_repeat")

    def test_docs_md_supplements_missing_families(self):
        docs = """
[<br />
Boarding REST
Merchant onboarding
<br />
<br />](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro.md)
"""
        roots, _, _, docs_only = discover_roots_from_llms("", docs_text=docs)
        self.assertIn(
            "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md", roots
        )
        self.assertIn(
            "/docs/cybs/en-us/boarding/developer/all/rest/boarding.md", docs_only
        )

    def test_candidates_include_guide_dir_and_bare_family(self):
        intro = (
            "/docs/cybs/en-us/echeck/user/all/rest/"
            "echeck-user-guide/echeck-txnprocess-intro.md"
        )
        from content_bench.content_engine.product_roots import generate_root_candidates

        cands = generate_root_candidates(intro)
        shapes = {s for _, s in cands}
        self.assertIn("guide_dir", shapes)
        self.assertIn("bare_family", shapes)

    def test_candidates_family_repeat_for_boarding(self):
        intro = (
            "/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro.md"
        )
        from content_bench.content_engine.product_roots import generate_root_candidates

        cands = generate_root_candidates(intro)
        shapes = {s for _, s in cands}
        self.assertIn("family_repeat", shapes)
        self.assertIn("bare_family", shapes)


class ClassifyUnfetchableTests(unittest.TestCase):
    def test_pdf(self):
        reason, bucket = classify_unfetchable(
            "/foo/bar.pdf",
            md_status=404,
            md_bytes=0,
            html_status=None,
            listed_as_root_in_llms=True,
            derivation="not_md",
        )
        self.assertEqual(reason, REASON_PDF)

    def test_derivation_error_404_constructed(self):
        reason, bucket = classify_unfetchable(
            "/docs/cybs/en-us/apple-pay/developer/all/rest.md",
            md_status=404,
            md_bytes=36538,
            html_status=404,
            listed_as_root_in_llms=False,
            derivation="family_repeat",
        )
        self.assertEqual(reason, REASON_DERIVATION_ERROR)
        self.assertEqual(bucket, "ours")

    def test_site_defect_500(self):
        reason, bucket = classify_unfetchable(
            "/docs/cybs/en-us/merchant-boarding/developer/all/rest/merchant-boarding.md",
            md_status=500,
            md_bytes=5,
            html_status=200,
            listed_as_root_in_llms=True,
            derivation="family_repeat",
        )
        self.assertEqual(reason, REASON_SITE_DEFECT)
        self.assertEqual(bucket, "theirs")

    def test_empty_200_distinct_from_404(self):
        reason, bucket = classify_unfetchable(
            "/docs/cybs/en-us/country-codes/reference/all/na/country-codes.md",
            md_status=200,
            md_bytes=0,
            html_status=200,
            listed_as_root_in_llms=True,
            derivation="family_repeat",
        )
        self.assertEqual(reason, REASON_EMPTY_200)
        self.assertNotEqual(reason, REASON_DERIVATION_ERROR)

    def test_hub_page(self):
        reason, bucket = classify_unfetchable(
            "/accept-payments.md",
            md_status=404,
            md_bytes=0,
            html_status=404,
            listed_as_root_in_llms=False,
            derivation="unresolved",
        )
        self.assertEqual(reason, REASON_HUB_PAGE)
        self.assertEqual(bucket, "structural")


if __name__ == "__main__":
    unittest.main()
