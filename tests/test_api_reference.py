"""API-reference pattern → rich endpoint_fact; anchors land in metadata."""

from __future__ import annotations

import unittest

from content_bench.content_engine.api_reference import extract_api_reference_claims
from content_bench.content_engine.ingest import _extract_claims_from_text
from content_bench.content_engine.source_noise import (
    clean_claim_text,
    deep_link_for,
    live_html_url_from_pointer,
)
from content_bench.content_engine.workflow_pages import (
    WorkflowSpec,
    compose_workflow_page,
)


BOARDING_API_REF = """\
Create a Merchant Organization {#boarding-reg-create-merch-api}
===============================================================

Use these instructions to create a merchant account using the API.

Endpoint {#boarding-reg-create-merch-api_d7e665}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-merch-api_d7e672}
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-reg-create-merch-api_d7e682}

Required Fields for Boarding a Merchant Organization {#boarding-reg-create-merch-api-req-fields}
================================================================================================

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set the value to `true`.

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set the value to `MERCHANT`.

REST Example: Creating a Merchant Organization {#boarding-reg-create-merch-api-example}
=======================================================================================

Request

```
{
    "organizationInformation": {
        "type": "MERCHANT",
        "configurable": true
    }
}
```

Response to a Successful Request

```
{
    "status": "SUCCESS"
}
```
"""

UI_AND_API = (
    BOARDING_API_REF
    + "\n\n"
    + "1. Click the Portfolio Management icon in the pane.{#merchants-v2-add-merchant_step1}\n"
    + "{#merchants-v2-add-merchant_step1}\n"
)


class ApiReferenceExtractionTests(unittest.TestCase):
    def test_emits_endpoint_fact_not_steps_for_pattern(self):
        claims, report, covered = extract_api_reference_claims(
            BOARDING_API_REF,
            source_pointer="en-us_boarding_developer_all_rest_boarding.md.md",
            doc_stem="boarding",
        )
        self.assertEqual(report.matched, 1)
        self.assertEqual(report.matched_with_required_fields, 1)
        self.assertEqual(report.matched_with_example, 1)
        self.assertEqual(len(claims), 2)  # prod + test
        self.assertTrue(all(c.schema == "endpoint_fact" for c in claims))
        test = next(c for c in claims if c.extras.get("environment") == "test")
        self.assertEqual(test.extras["method"], "POST")
        self.assertEqual(test.extras["path"], "/boarding/v1/registrations")
        self.assertEqual(test.extras["host"], "https://apitest.cybersource.com")
        fields = {f["name"]: f["instruction"] for f in test.extras["required_fields"]}
        self.assertIn("organizationInformation.type", fields)
        self.assertIn("MERCHANT", fields["organizationInformation.type"])
        self.assertIn("type", test.extras["example_request"])
        self.assertIn("SUCCESS", test.extras["example_response"])
        self.assertEqual(test.extras["anchor"], "boarding-reg-create-merch-api")
        self.assertIn("#boarding-reg-create-merch-api", test.extras["deep_link"])
        self.assertNotIn("{#", test.text)

    def test_page_can_yield_steps_and_endpoints(self):
        claims, drops = _extract_claims_from_text(
            UI_AND_API,
            source_pointer="en-us_boarding_developer_all_rest_boarding.md.md",
            doc_stem="boarding",
        )
        self.assertFalse(drops)
        steps = [c for c in claims if c.schema == "quickstart_step"]
        eps = [c for c in claims if c.schema == "endpoint_fact"]
        self.assertEqual(len(steps), 1)
        self.assertGreaterEqual(len(eps), 2)
        self.assertNotIn("{#", steps[0].text)
        self.assertEqual(
            steps[0].extras.get("anchor"), "merchants-v2-add-merchant_step1"
        )
        self.assertIn(
            "merchants-v2-add-merchant_step1",
            steps[0].extras.get("deep_link") or "",
        )


class SourceNoiseTests(unittest.TestCase):
    def test_clean_strips_anchors_and_empty_titles(self):
        raw = (
            'Click [here](https://example.com/x.md "") now.{#step1}\n'
            "{#step1}\n"
        )
        clean, meta = clean_claim_text(raw)
        self.assertNotIn("{#", clean)
        self.assertNotIn('""', clean)
        self.assertEqual(meta["anchor"], "step1")
        self.assertIn("https://example.com/x.md", clean)

    def test_deep_link_from_local_name(self):
        url = live_html_url_from_pointer(
            "product-roots/en-us_boarding_developer_all_rest_boarding.md.md"
        )
        self.assertEqual(
            url,
            "https://developer.cybersource.com/docs/cybs/en-us/boarding/"
            "developer/all/rest/boarding.html",
        )
        self.assertEqual(
            deep_link_for(
                "en-us_boarding_developer_all_rest_boarding.md.md",
                "boarding-reg-create-merch-api",
            ),
            url + "#boarding-reg-create-merch-api",
        )


class StepAnchorMetadataTests(unittest.TestCase):
    def test_anchor_in_metadata_not_text(self):
        text = (
            "# Guide\n\n"
            "1. Click the Portfolio Management icon in the pane.{#merchants-v2-step1}\n"
        )
        claims, _ = _extract_claims_from_text(
            text, source_pointer="en-us_boarding_user_all_ebc_x.md.md", doc_stem="x"
        )
        steps = [c for c in claims if c.schema == "quickstart_step"]
        self.assertEqual(len(steps), 1)
        self.assertNotIn("{#", steps[0].text)
        self.assertEqual(steps[0].extras.get("anchor"), "merchants-v2-step1")
        self.assertIn("line_start", steps[0].extras)


class RenderDeepLinkTests(unittest.TestCase):
    def test_composed_page_has_deep_link_no_brace_anchor(self):
        claims, _ = _extract_claims_from_text(
            UI_AND_API,
            source_pointer="en-us_boarding_developer_all_rest_boarding.md.md",
            doc_stem="boarding",
        )
        spec = WorkflowSpec(
            workflow_id="create-merchant-organization",
            title="Create a Merchant Organization",
            goal="Board a merchant.",
            doc_matchers=("boarding",),
        )
        page = compose_workflow_page(
            spec, [c.to_dict() for c in claims], stamp="test"
        )
        self.assertNotRegex(page, r"\{#[^}]+\}")
        self.assertIn("apitest.cybersource.com", page)
        self.assertIn("MERCHANT", page)
        self.assertIn("cybersource.com", page)
        self.assertIn("#boarding-reg-create-merch-api", page)
        self.assertIn("#merchants-v2-add-merchant_step1", page)
        # One continuous sequence: API then UI, numbering does not restart.
        self.assertIn("**API:**", page)
        self.assertIn("1. **API:**", page)
        self.assertRegex(page, r"2\. \*\*Action:\*\*")
        self.assertIn("sequence_stats:", page)


if __name__ == "__main__":
    unittest.main()
