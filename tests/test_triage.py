"""Triage module: one definition shared by census and ingest."""

from __future__ import annotations

import unittest

from content_bench.content_engine import corpus_census, ingest, triage


class TriageSharedDefinitionTests(unittest.TestCase):
    """Census and ingest must call triage — not re-implement it."""

    def test_ingest_uses_triage_functions(self):
        self.assertIs(ingest._constraint_kind, triage.constraint_kind)
        self.assertIs(ingest._looks_like_shell, triage.looks_like_shell)
        self.assertIs(ingest._first_heading, triage.first_heading)
        self.assertIs(ingest._iter_sentences, triage.iter_sentences)

    def test_census_uses_triage_functions(self):
        self.assertIs(
            corpus_census._has_constraint_signals, triage.has_constraint_signals
        )
        self.assertIs(corpus_census._link_density, triage.link_density)


class ConstraintDetectorTests(unittest.TestCase):
    """Explicit constraint-page detector: the class that keeps getting lost."""

    def test_ttl_and_reuse(self):
        s = (
            "The transient token can be used multiple times within the "
            "15-minute period."
        )
        self.assertEqual(triage.constraint_kind(s), "ttl_and_reuse")

    def test_ttl_only(self):
        s = "You can use it in place of the PAN with payment services for 15 minutes."
        self.assertEqual(triage.constraint_kind(s), "ttl_or_validity")

    def test_pci(self):
        s = "This could qualify you for PCI DSS SAQ A."
        self.assertEqual(triage.constraint_kind(s), "pci_compliance")

    def test_mandatory_header(self):
        s = "Each request that you send to Cybersource requires header information."
        self.assertEqual(triage.constraint_kind(s), "mandatory_header")

    def test_device_encryption(self):
        s = "Sensitive data is encrypted on the customer's device before transmission."
        self.assertEqual(triage.constraint_kind(s), "device_encryption")

    def test_validate_does_not_trip_valid(self):
        s = "After you validate the request payload you can submit the form data."
        self.assertIsNone(triage.constraint_kind(s))

    def test_id_format_rule(self):
        s = "The acquirer merchant ID must be from 1 to 35 alphanumeric characters."
        self.assertEqual(triage.constraint_kind(s), "id_format_rule")
        s2 = "Organization IDs must be unique, not just within the portfolio, but across the system."
        self.assertEqual(triage.constraint_kind(s2), "id_format_rule")

    def test_hierarchy_limit(self):
        s = "There can only be one merchant in any branch of the hierarchy."
        self.assertEqual(triage.constraint_kind(s), "hierarchy_limit")

    def test_prerequisite(self):
        s = "Having a TRID is a prerequisite for enabling network tokenization."
        self.assertEqual(triage.constraint_kind(s), "prerequisite")
        s2 = "You must have a portfolio account on our platform."
        self.assertEqual(triage.constraint_kind(s2), "prerequisite")
        # L1-prereq-pattern-tune (C3 sibling triage / Spark Qwen proposal)
        self.assertEqual(
            triage.constraint_kind(
                "Before you can implement payer authentication services, "
                "your business team must contact your acquirer and Cybersource."
            ),
            "prerequisite",
        )
        self.assertEqual(
            triage.constraint_kind(
                "This implementation requires the use of JavaScript to "
                "leverage the authentication."
            ),
            "prerequisite",
        )
        self.assertEqual(
            triage.constraint_kind(
                "Notify your account representative that you want to "
                "implement payer authentication."
            ),
            "prerequisite",
        )

    def test_page_and_sentence_detectors_agree_on_boarding_classes(self):
        page = (
            "Requirements\n============\n\n"
            "You must have a portfolio account on our platform.\n"
        )
        self.assertTrue(triage.has_constraint_signals(page))
        page2 = "Hierarchy\n=========\n\nThere can only be one merchant in any branch of the hierarchy.\n"
        self.assertTrue(triage.has_constraint_signals(page2))

    def test_page_level_signals(self):
        self.assertTrue(
            triage.has_constraint_signals("Tokens expire after 15 minutes.")
        )
        self.assertFalse(
            triage.has_constraint_signals("See these topics for more information.")
        )


class ShellDetectorTests(unittest.TestCase):
    def test_constraint_page_is_never_shell(self):
        text = (
            "Transient tokens\n===============\n\n"
            "The token is valid for 15 minutes and may be reused in that window.\n"
        )
        self.assertFalse(triage.looks_like_shell(text, len(text.encode())))

    def test_nav_stub_is_shell(self):
        text = (
            "Introduction to Foo {#foo}\n====================\n\n"
            "See these topics:\n\n* [A](/a.md)\n* [B](/b.md)\n"
        )
        self.assertTrue(triage.looks_like_shell(text, len(text.encode())))


if __name__ == "__main__":
    unittest.main()
