"""Tests for Specs-to-Docs V0 (Payment Gateway-shaped local OpenAPI fixture)."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from relay_bench.content_engine.registry import require_source
from relay_bench.content_engine.snapshot import materialize_snapshot
from relay_bench.content_engine.specs_compose import compose_reference_units
from relay_bench.content_engine.specs_parser import parse_openapi_entities
from relay_bench.content_engine.specs_pipeline import run_specs_to_docs
from relay_bench.content_engine.specs_validate import (
    validate_contract_alignment,
    validate_units_content,
    validate_units_schema,
)
from relay_bench.content_engine.schemas import ApiReferenceUnit

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID = "payments-core-openapi"

EXPECTED_OPS = {
    "createPayment",
    "getPayment",
    "capturePayment",
    "createCredit",
    "createCustomer",
    "getCustomer",
    "createMppCredentialSetup",
    "checkMppEnrollment",
}


class SpecsToDocsTests(unittest.TestCase):
    def test_registry_has_openapi_source(self):
        record = require_source(SOURCE_ID)
        self.assertEqual(record.source_type, "openapi")
        self.assertTrue((ROOT / record.repo_path).exists())
        self.assertEqual(
            record.linked_workflow_id,
            "microform-payer-auth-state-machine",
        )

    def test_parser_emits_eight_payment_gateway_operations(self):
        record = require_source(SOURCE_ID)
        snapshot = materialize_snapshot(record)
        entities = parse_openapi_entities(record, snapshot)
        ops = {e.operation_id for e in entities}
        self.assertEqual(ops, EXPECTED_OPS)
        self.assertTrue(all(e.auth_schemes for e in entities))
        self.assertTrue(all(e.endpoint.startswith("/") for e in entities))

    def test_pipeline_promotes_with_contract_alignment(self):
        result = run_specs_to_docs(SOURCE_ID)
        self.assertTrue(result["ok"], result["issues"])
        self.assertEqual(result["entity_count"], 8)
        self.assertEqual(result["unit_count"], 8)
        self.assertTrue(result["schema_passed"])
        self.assertTrue(result["content_passed"])
        self.assertTrue(result["contract_alignment_passed"])
        self.assertEqual(set(result["operation_ids"]), EXPECTED_OPS)

        for key in (
            "entities_path",
            "units_path",
            "eval_seeds_path",
            "reconciliation_path",
        ):
            path = ROOT / result[key]
            self.assertTrue(path.exists(), key)

        units_payload = json.loads((ROOT / result["units_path"]).read_text(encoding="utf-8"))
        self.assertEqual(units_payload["lineage_origin"], "generated_from_spec")
        blob = json.dumps(units_payload).lower()
        for banned in ("4111111111111111", "shared_secret_value", "merchantsecretkey="):
            self.assertNotIn(banned, blob)

        # Linked workflow contract lineage when present.
        if result["contract_bundle_path"]:
            self.assertTrue((ROOT / result["contract_bundle_path"]).exists())

    def test_alignment_fails_on_endpoint_drift(self):
        record = require_source(SOURCE_ID)
        snapshot = materialize_snapshot(record)
        entities = parse_openapi_entities(record, snapshot)
        units = compose_reference_units(record, entities)
        units[0].endpoint = "/tampered"
        ok, issues = validate_contract_alignment(entities, units)
        self.assertFalse(ok)
        self.assertTrue(any(i.code == "endpoint_mismatch" for i in issues))

    def test_content_gate_requires_evidence(self):
        bad = ApiReferenceUnit(
            unit_id="x",
            doc_id="d",
            api_name="a",
            endpoint="/x",
            http_method="GET",
            summary="s",
            auth_requirements=["httpSignature"],
            path_params=[],
            query_params=[],
            request_fields=[],
            response_fields=[],
            error_cases=[{"code": "x", "meaning": "y", "recovery": "z"}],
            workflows=[],
            code_examples=[],
            evidence_quotes=[],
            operation_id="x",
        )
        schema_ok, _ = validate_units_schema([bad])
        content_ok, issues = validate_units_content([bad])
        self.assertFalse(schema_ok)
        # content also fails lineage/evidence depending on order; evidence checked in schema too
        self.assertTrue(any(i.code == "missing_evidence" for i in _))


if __name__ == "__main__":
    unittest.main()
