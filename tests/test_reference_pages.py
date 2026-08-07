"""A2 reference page generator tests."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT))

from content_bench.content_engine.reference_pages import (  # noqa: E402
    load_reference_units,
    render_reference_page,
    write_reference_pages,
)

# Engine unit tests pin the practice fixture — not the Wave 1 production denominator.
FIXTURE_UNITS = (
    ROOT
    / "artifacts"
    / "content_engine"
    / "generated"
    / "payments-core-openapi.api_reference_units.json"
)


class ReferencePagesTests(unittest.TestCase):
    def test_loads_eight_units(self):
        units = load_reference_units(FIXTURE_UNITS)
        self.assertEqual(len(units), 8)
        ops = {u["operation_id"] for u in units}
        self.assertIn("createPayment", ops)

    def test_create_payment_page_carries_spec_facts(self):
        units = load_reference_units(FIXTURE_UNITS)
        unit = next(u for u in units if u["operation_id"] == "createPayment")
        md = render_reference_page(unit)
        self.assertIn("lineage_origin: generated_from_spec", md)
        self.assertIn("`httpSignature`", md)
        self.assertIn("POST", md)
        self.assertIn("/pts/v2/payments", md)
        self.assertIn("Do not send raw PAN", md)
        self.assertIn("sandbox only", md.lower())

    def test_create_payment_request_table_lists_nested_fields(self):
        units = load_reference_units(FIXTURE_UNITS)
        unit = next(u for u in units if u["operation_id"] == "createPayment")
        md = render_reference_page(unit)
        # Request table only — real developer-typable dotted names + required flag.
        request_section = md.split("## Request", 1)[1].split("## Response", 1)[0]
        self.assertIn("orderInformation.amountDetails.totalAmount", request_section)
        self.assertRegex(
            request_section,
            r"\|\s*orderInformation\.amountDetails\.totalAmount\s*\|\s*string\s*\|\s*yes\s*\|",
        )

    def test_write_pages_uses_operation_id_filenames(self):
        units = load_reference_units(FIXTURE_UNITS)
        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            arts = Path(tmp) / "arts"
            summary = write_reference_pages(units, content_dir=content, artifact_dir=arts)
            self.assertEqual(summary["count"], 8)
            self.assertTrue((content / "createPayment.md").exists())
            body = (content / "createPayment.md").read_text(encoding="utf-8")
            self.assertIn("lineage_origin: generated_from_spec", body)
            summary_path = arts / "reference-pages-summary.json"
            self.assertTrue(summary_path.exists())
            loaded = json.loads(summary_path.read_text(encoding="utf-8"))
            self.assertTrue(loaded["ok"])

    def test_rejects_non_spec_lineage(self):
        bad = [
            {
                "operation_id": "x",
                "http_method": "GET",
                "endpoint": "/x",
                "summary": "x",
                "auth_requirements": [],
                "lineage_origin": "hand_pasted",
                "unit_id": "bad",
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                write_reference_pages(
                    bad,
                    content_dir=Path(tmp) / "c",
                    artifact_dir=Path(tmp) / "a",
                )


if __name__ == "__main__":
    unittest.main()
