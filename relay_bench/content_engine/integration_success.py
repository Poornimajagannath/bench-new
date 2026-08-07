"""Integration Success OS V0 — assemble trusted Relay artifacts into a serve pack.

Honest label:
- Uses local promoted quickstart + specs-to-docs outputs.
- No live sandbox calls, no DocETL/Tempo imports, no credentials.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from relay_bench.content_engine.pipeline import run_content_engine
from relay_bench.content_engine.specs_pipeline import run_specs_to_docs
from relay_bench.reporting import repo_relative

ROOT = Path(__file__).resolve().parents[2]
ISO_DIR = ROOT / "artifacts" / "content_engine" / "integration_success"

DEFAULT_QUICKSTART_SOURCE = "microform-payer-auth-quickstart"
DEFAULT_OPENAPI_SOURCE = "payments-core-openapi"
DEFAULT_WORKFLOW_ID = "microform-payer-auth-state-machine"


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _go_live_checklist(operation_ids: List[str]) -> List[Dict[str, str]]:
    return [
        {
            "id": "auth-env",
            "title": "Load sandbox auth from environment variables",
            "detail": "Use PGW_MERCHANT_ID / PGW_KEY_ID / PGW_SHARED_SECRET; never hardcode.",
        },
        {
            "id": "first-api-call",
            "title": "Complete first successful sandbox API call",
            "detail": f"Primary ops available: {', '.join(operation_ids[:4])}",
        },
        {
            "id": "payer-auth-path",
            "title": "Do not treat Microform tokenize as completed 3DS",
            "detail": "Run enrollment and challenge/frictionless handling before authorization.",
        },
        {
            "id": "error-recovery",
            "title": "Handle auth and validation errors without leaking secrets",
            "detail": "Use generated error eval seeds; keep evidence support-safe.",
        },
        {
            "id": "go-live-switch",
            "title": "Switch to production only after sandbox checklist passes",
            "detail": "V0 does not call production. Keep PGW_ENVIRONMENT=sandbox until ready.",
        },
    ]


def assemble_integration_success_pack(
    *,
    quickstart_source: str = DEFAULT_QUICKSTART_SOURCE,
    openapi_source: str = DEFAULT_OPENAPI_SOURCE,
    workflow_id: str = DEFAULT_WORKFLOW_ID,
    ensure_compiled: bool = True,
) -> Dict[str, Any]:
    """Compile dependencies if needed, then assemble an Integration Success pack."""
    qs_result: Optional[Dict[str, Any]] = None
    spec_result: Optional[Dict[str, Any]] = None

    if ensure_compiled:
        qs_result = run_content_engine(quickstart_source)
        if not qs_result.get("ok"):
            raise RuntimeError(f"Quickstart compile failed: {qs_result.get('issues')}")
        spec_result = run_specs_to_docs(openapi_source)
        if not spec_result.get("ok"):
            raise RuntimeError(f"Specs-to-docs compile failed: {spec_result.get('issues')}")

    qs_units_path = (
        ROOT
        / "artifacts"
        / "content_engine"
        / "objects"
        / f"{quickstart_source}.quickstart_units.json"
    )
    qs_ctx_path = (
        ROOT
        / "artifacts"
        / "content_engine"
        / "context_packs"
        / f"{quickstart_source}.context_pack.json"
    )
    api_units_path = (
        ROOT
        / "artifacts"
        / "content_engine"
        / "generated"
        / f"{openapi_source}.api_reference_units.json"
    )
    eval_seeds_path = (
        ROOT
        / "artifacts"
        / "content_engine"
        / "generated"
        / f"{openapi_source}.eval_seeds.json"
    )
    contract_path = (
        ROOT / "artifacts" / "contracts" / f"{workflow_id}.contract_bundle.json"
    )

    for path in (qs_units_path, api_units_path, eval_seeds_path):
        if not path.exists():
            raise FileNotFoundError(
                f"Missing required artifact {repo_relative(path)}. "
                "Run content engine + specs-to-docs first."
            )

    qs_units = _load_json(qs_units_path).get("units") or []
    api_units = _load_json(api_units_path).get("units") or []
    eval_seeds = _load_json(eval_seeds_path).get("seeds") or []
    operation_ids = [u.get("operation_id", "") for u in api_units if u.get("operation_id")]

    steps = []
    for unit in qs_units:
        if unit.get("unit_type") != "step":
            continue
        steps.append(
            {
                "sequence_number": unit.get("sequence_number"),
                "title": unit.get("title"),
                "requires": unit.get("requires") or [],
                "outcomes": unit.get("outcomes") or [],
                "failure_modes": unit.get("failure_modes") or [],
            }
        )
    steps.sort(key=lambda s: s.get("sequence_number") or 0)

    pack = {
        "schema_version": "relay.integration_success_pack.v0",
        "product": "Integration Success OS",
        "audience": ["backend_developer"],
        "promise": (
            "A developer can integrate our API in a single session, with clear steps, "
            "working references, and a go-live checklist."
        ),
        "workflow_id": workflow_id,
        "quickstart_source": quickstart_source,
        "openapi_source": openapi_source,
        "guided_quickstart": {
            "title": "Payment Gateway / Acceptance Platform guided integration",
            "steps": steps,
            "step_count": len(steps),
        },
        "api_reference": {
            "operation_count": len(operation_ids),
            "operation_ids": operation_ids,
            "unit_ids": [u.get("unit_id") for u in api_units],
        },
        "test_scenarios": [
            {
                "seed_id": s.get("seed_id"),
                "kind": s.get("kind"),
                "operation_id": s.get("operation_id"),
                "user_query": s.get("user_query"),
            }
            for s in eval_seeds
            if s.get("kind") in {"happy_path", "missing_auth", "error_recovery"}
        ][:12],
        "go_live_checklist": _go_live_checklist(operation_ids),
        "lineage": {
            "quickstart_units_path": repo_relative(qs_units_path),
            "quickstart_context_pack_path": repo_relative(qs_ctx_path)
            if qs_ctx_path.exists()
            else None,
            "api_reference_units_path": repo_relative(api_units_path),
            "eval_seeds_path": repo_relative(eval_seeds_path),
            "workflow_contract_path": repo_relative(contract_path)
            if contract_path.exists()
            else None,
            "origins": [
                "ingested_prose",
                "generated_from_spec",
                "hybrid_reconciled",
            ],
        },
        "constraints": [
            "Local prototype only",
            "No network calls",
            "No live credentials, PAN, or secrets",
            "DocETL-style / Harbor-Tempo-style labels remain honest",
            "OpenAPI alone does not replace full onboarding narrative",
        ],
        "honest_label": {
            "docetl": "style-only-upstream",
            "tempo_harbor": "eval-seeds-only",
            "network": "denied",
            "humanify": "not-implemented",
        },
        "compile_results": {
            "quickstart": {
                "ok": bool(qs_result.get("ok")) if qs_result else None,
                "unit_count": qs_result.get("unit_count") if qs_result else None,
            },
            "specs_to_docs": {
                "ok": bool(spec_result.get("ok")) if spec_result else None,
                "entity_count": spec_result.get("entity_count") if spec_result else None,
                "unit_count": spec_result.get("unit_count") if spec_result else None,
            },
        },
    }

    ISO_DIR.mkdir(parents=True, exist_ok=True)
    json_path = ISO_DIR / "integration_success_pack.json"
    md_path = ISO_DIR / "integration_success_pack.md"
    json_path.write_text(json.dumps(pack, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_integration_success_markdown(pack), encoding="utf-8")

    return {
        "ok": True,
        "pack_json": repo_relative(json_path),
        "pack_md": repo_relative(md_path),
        "step_count": len(steps),
        "operation_count": len(operation_ids),
        "test_scenario_count": len(pack["test_scenarios"]),
        "checklist_count": len(pack["go_live_checklist"]),
        "workflow_id": workflow_id,
    }


def render_integration_success_markdown(pack: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Integration Success Pack (V0)",
        "",
        f"**Product:** {pack['product']}",
        "",
        pack["promise"],
        "",
        "Local proof only. No live sandbox calls.",
        "",
        "## Guided quickstart steps",
        "",
    ]
    for step in pack["guided_quickstart"]["steps"]:
        lines.append(
            f"{step['sequence_number']}. {step['title']}"
        )
    lines.extend(
        [
            "",
            "## API reference operations",
            "",
        ]
    )
    for op in pack["api_reference"]["operation_ids"]:
        lines.append(f"- `{op}`")
    lines.extend(["", "## Go-live checklist", ""])
    for item in pack["go_live_checklist"]:
        lines.append(f"- [ ] **{item['title']}** — {item['detail']}")
    lines.extend(
        [
            "",
            "## Lineage",
            "",
            f"- quickstart units: `{pack['lineage']['quickstart_units_path']}`",
            f"- api reference units: `{pack['lineage']['api_reference_units_path']}`",
            f"- eval seeds: `{pack['lineage']['eval_seeds_path']}`",
            f"- workflow contract: `{pack['lineage']['workflow_contract_path']}`",
            "",
            "## Honesty",
            "",
            f"- docetl: `{pack['honest_label']['docetl']}`",
            f"- tempo/harbor: `{pack['honest_label']['tempo_harbor']}`",
            f"- network: `{pack['honest_label']['network']}`",
            "",
        ]
    )
    return "\n".join(line.rstrip() for line in lines).rstrip() + "\n"
