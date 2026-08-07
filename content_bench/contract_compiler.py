"""Workflow Contract Compiler — durable bundle from one PM-approved candidate.

The approved workflow contract is the product source of truth. Task packs,
Harbor/Tempo-style eval previews, verifier receipts, and improvement actions
derive from it.

V0 honesty:
- DocETL-style extraction already happened upstream (not imported here).
- Harbor/Tempo-style export is a *preview* only (`preview_only: true`).
- No network, no live credentials, no PAN/secret materialization.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from content_bench.reporting import repo_relative
from content_bench.schemas import ImprovementAction, WorkflowCandidate
from content_bench.task_pack import (
    assert_no_verifier_leak,
    build_hidden_truth,
    build_task_pack,
    materialize_contract,
    to_agent_task,
)

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIR = ROOT / "artifacts" / "contracts"
TASK_PACK_DIR = ROOT / "artifacts" / "task_packs"
VERIFIER_RESULT_DIR = ROOT / "artifacts" / "verifier_results"
REPORT_DIR = ROOT / "artifacts" / "reports"

SCHEMA_VERSION = "content.workflow_contract_bundle.v0"

# Receipt may prove hidden truth exists; it must never print verifier-only data.
_RECEIPT_ALLOWED_KEYS = frozenset(
    {
        "hidden_truth_path",
        "agent_visible_path",
        "oracle_present",
        "bad_answer_present",
        "private_checks_present",
        "agent_pack_omits_oracle",
        "agent_pack_omits_bad_answer",
        "agent_pack_omits_private_checks",
        "oracle_field_count",
        "bad_answer_field_count",
        "private_check_count",
        "hidden_truth_sha256",
        "agent_visible_sha256",
    }
)

_FORBIDDEN_RECEIPT_SUBSTRINGS = (
    "oracle_answer",
    "oracle_summary",
    "bad_answer",
    "bad_answer_fixture",
    "verifier_private_checks",
    "hidden_checks",
    "scoring_rubric",
    "expected_bad_failure_ids",
)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_hidden_truth_receipt(
    *,
    agent_visible_path: Path,
    hidden_truth_path: Path,
) -> Dict[str, Any]:
    """Build a firewall-safe receipt proving hidden truth exists without leaking it."""
    agent_payload = _load_json(agent_visible_path)
    assert_no_verifier_leak(agent_payload)

    private_payload = _load_json(hidden_truth_path)
    # Support both modern verifier_private wrapper and legacy HiddenTruth shape.
    private = private_payload.get("verifier_private", private_payload)

    oracle = private.get("oracle_summary") or private.get("oracle_answer") or {}
    bad = private.get("bad_answer_fixture") or private.get("bad_answer") or {}
    checks = (
        private.get("hidden_checks")
        or private.get("verifier_private_checks")
        or []
    )

    agent_blob = json.dumps(agent_payload)
    agent_task = agent_payload.get("agent_task", agent_payload)

    receipt: Dict[str, Any] = {
        "hidden_truth_path": repo_relative(hidden_truth_path),
        "agent_visible_path": repo_relative(agent_visible_path),
        "oracle_present": bool(oracle),
        "bad_answer_present": bool(bad),
        "private_checks_present": bool(checks),
        "agent_pack_omits_oracle": (
            "oracle_answer" not in agent_task
            and "oracle_summary" not in agent_task
            and '"oracle_summary"' not in agent_blob
            and '"oracle_answer"' not in agent_blob
        ),
        "agent_pack_omits_bad_answer": (
            "bad_answer" not in agent_task
            and "bad_answer_fixture" not in agent_task
            and '"bad_answer_fixture"' not in agent_blob
            and '"bad_answer"' not in agent_blob
        ),
        "agent_pack_omits_private_checks": (
            "verifier_private_checks" not in agent_task
            and "hidden_checks" not in agent_task
            and '"hidden_checks"' not in agent_blob
            and '"verifier_private_checks"' not in agent_blob
        ),
        "oracle_field_count": len(oracle) if isinstance(oracle, dict) else 0,
        "bad_answer_field_count": len(bad) if isinstance(bad, dict) else 0,
        "private_check_count": len(checks) if isinstance(checks, list) else 0,
        "hidden_truth_sha256": _sha256_file(hidden_truth_path),
        "agent_visible_sha256": _sha256_file(agent_visible_path),
    }

    assert_receipt_firewall(receipt, hidden_truth_path=hidden_truth_path)
    return receipt


def assert_receipt_firewall(
    receipt: Dict[str, Any],
    *,
    hidden_truth_path: Optional[Path] = None,
) -> None:
    """Fail loudly if the receipt leaks verifier-only content or unknown keys."""
    unknown = set(receipt) - _RECEIPT_ALLOWED_KEYS
    if unknown:
        raise ValueError(f"hidden_truth_receipt has disallowed keys: {sorted(unknown)}")

    blob = json.dumps(receipt)
    for banned in _FORBIDDEN_RECEIPT_SUBSTRINGS:
        # Path strings may contain "hidden_truth" as a filename fragment; that is OK.
        # Forbid content-bearing field names as JSON keys / values beyond path filenames.
        if banned in ("oracle_answer", "oracle_summary", "bad_answer", "bad_answer_fixture"):
            if f'"{banned}"' in blob:
                raise ValueError(f"hidden_truth_receipt leaked field name {banned!r}")
        elif banned in ("verifier_private_checks", "hidden_checks", "scoring_rubric", "expected_bad_failure_ids"):
            if f'"{banned}"' in blob or f": {banned}" in blob:
                raise ValueError(f"hidden_truth_receipt leaked field name {banned!r}")

    if hidden_truth_path is not None and hidden_truth_path.exists():
        private_payload = _load_json(hidden_truth_path)
        private = private_payload.get("verifier_private", private_payload)
        mistake = ""
        bad = private.get("bad_answer_fixture") or private.get("bad_answer") or {}
        if isinstance(bad, dict):
            mistake = str(bad.get("mistake", ""))
        if mistake and mistake in blob:
            raise ValueError("hidden_truth_receipt leaked bad_answer mistake content")

        # Distinctive private check ids must not appear as content lists in the receipt.
        # Counts/hashes only — never check bodies.
        for check in private.get("hidden_checks") or private.get("verifier_private_checks") or []:
            if isinstance(check, dict):
                for value in check.values():
                    if isinstance(value, (dict, list)):
                        snippet = json.dumps(value)
                        if snippet in blob and len(snippet) > 2:
                            raise ValueError(
                                "hidden_truth_receipt leaked private check body content"
                            )


def build_harbor_shape_preview(
    candidate: WorkflowCandidate,
    *,
    agent_visible_path: Path,
) -> Dict[str, Any]:
    """Harbor/Tempo-style eval shape preview — not a real Harbor/Tempo task."""
    pack = build_task_pack(candidate)
    return {
        "preview_only": True,
        "runner_integration": "not implemented",
        "inspired_by": "Harbor / Tempo Stable Bench task shape (not imported in V0)",
        "instruction": pack.prompt,
        "environment": {
            "mode": "local-simulated",
            "network": "denied",
            "credentials": "none",
            "note": "Harbor/Tempo-style isolation is preview-only; no Docker runner in V0",
        },
        "test_ref": {
            "workflow_id": candidate.workflow_id,
            "agent_task_path": repo_relative(agent_visible_path),
            "verifier_style": "stable-bench-inspired-local-fixture",
        },
        "expected_artifact": pack.expected_deliverable,
        "required_receipts": [
            "hidden_truth_receipt",
            "verifier_result",
        ],
        "isolation_note": (
            "V0 does not run Harbor, tempo-evals, or Docker isolation. "
            "This preview documents how a future eval export could package the "
            "agent-visible task against verifier-private fixtures."
        ),
    }


def _default_paths(workflow_id: str) -> Dict[str, Path]:
    return {
        "agent_visible": TASK_PACK_DIR / f"{workflow_id}.agent_task.json",
        "hidden_truth": TASK_PACK_DIR / f"{workflow_id}.verifier_private.json",
        "verifier_result": VERIFIER_RESULT_DIR / f"{workflow_id}.result.json",
        "report_json": REPORT_DIR / f"{workflow_id}.report.json",
    }


def _load_improvement_actions(
    report_json_path: Path,
    explicit: Optional[Sequence[ImprovementAction]] = None,
) -> Optional[List[Dict[str, Any]]]:
    if explicit is not None:
        return [a.to_dict() for a in explicit]
    if not report_json_path.exists():
        return None
    report = _load_json(report_json_path)
    classification = report.get("classification") or {}
    actions = classification.get("actions")
    if not actions:
        return None
    return list(actions)


def compile_contract_bundle(
    candidate: WorkflowCandidate,
    *,
    agent_visible_path: Optional[Path] = None,
    hidden_truth_path: Optional[Path] = None,
    verifier_result_path: Optional[Path] = None,
    improvement_actions: Optional[Sequence[ImprovementAction]] = None,
    ensure_materialized: bool = True,
) -> Dict[str, Any]:
    """Compile one durable contract bundle from a PM-approved WorkflowCandidate."""
    paths = _default_paths(candidate.workflow_id)
    agent_path = agent_visible_path or paths["agent_visible"]
    private_path = hidden_truth_path or paths["hidden_truth"]

    if ensure_materialized or not agent_path.exists() or not private_path.exists():
        _pack, _hidden, agent_path, private_path = materialize_contract(candidate)
    else:
        # Still assert the agent-visible pack is firewall-safe.
        assert_no_verifier_leak(_load_json(agent_path))
        build_task_pack(candidate).assert_agent_safe()

    receipt = build_hidden_truth_receipt(
        agent_visible_path=agent_path,
        hidden_truth_path=private_path,
    )
    harbor_preview = build_harbor_shape_preview(
        candidate,
        agent_visible_path=agent_path,
    )

    result_path = verifier_result_path or paths["verifier_result"]
    actions = _load_improvement_actions(paths["report_json"], improvement_actions)

    bundle: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "workflow_id": candidate.workflow_id,
        "title": candidate.title,
        "goal": candidate.goal,
        "stages": list(candidate.stages),
        "api_sdk_facts": list(candidate.api_sdk_facts),
        "confusion_points": list(candidate.confusion_points),
        "source_seed_ids": list(candidate.seed_ids),
        "pm_decision": candidate.pm_decision,
        "task_pack_path": repo_relative(agent_path),
        "hidden_truth_receipt": receipt,
        "harbor_shape_preview": harbor_preview,
    }

    if result_path.exists():
        bundle["verifier_result_path"] = repo_relative(result_path)
    if actions is not None:
        bundle["improvement_actions"] = actions

    # Bundle-level firewall: receipt must remain leak-free inside the full JSON.
    assert_receipt_firewall(
        bundle["hidden_truth_receipt"],
        hidden_truth_path=private_path,
    )
    _assert_bundle_omits_hidden_content(bundle, private_path)

    return bundle


def _assert_bundle_omits_hidden_content(
    bundle: Dict[str, Any],
    hidden_truth_path: Path,
) -> None:
    """Ensure the compiled bundle does not embed oracle/bad/private bodies."""
    blob = json.dumps(bundle)
    private_payload = _load_json(hidden_truth_path)
    private = private_payload.get("verifier_private", private_payload)
    bad = private.get("bad_answer_fixture") or private.get("bad_answer") or {}
    mistake = str(bad.get("mistake", "")) if isinstance(bad, dict) else ""
    if mistake and mistake in blob:
        raise ValueError("contract bundle leaked bad_answer mistake content")

    # Top-level bundle must not grow verifier-private content keys.
    for banned in (
        "oracle_answer",
        "oracle_summary",
        "bad_answer",
        "bad_answer_fixture",
        "verifier_private_checks",
        "hidden_checks",
    ):
        if banned in bundle:
            raise ValueError(f"contract bundle leaked top-level key {banned!r}")


def render_contract_markdown(bundle: Dict[str, Any]) -> str:
    """Human-readable contract bundle answering the six compiler questions."""
    receipt = bundle["hidden_truth_receipt"]
    harbor = bundle["harbor_shape_preview"]
    lines: List[str] = [
        f"# Workflow Contract Bundle — `{bundle['workflow_id']}`",
        "",
        f"schema_version: `{bundle['schema_version']}`",
        "",
        "Local proof only. DocETL-style extraction and Harbor/Tempo-style eval "
        "export are inspirations — not live upstream integrations.",
        "",
        "## 1. What source confusion became this contract?",
        "",
        f"**Goal:** {bundle['goal']}",
        "",
        "Confusion points:",
    ]
    for item in bundle["confusion_points"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            f"Source seed ids: `{', '.join(bundle['source_seed_ids'])}`",
            "",
            "## 2. What did PM approve or edit?",
            "",
            f"- pm_decision: `{bundle['pm_decision']}`",
            f"- title: {bundle['title']}",
            f"- stages: `{', '.join(bundle['stages'])}`",
            "",
            "API/SDK facts:",
        ]
    )
    for fact in bundle["api_sdk_facts"]:
        lines.append(f"- {fact}")

    lines.extend(
        [
            "",
            "## 3. What agent-visible task pack was created?",
            "",
            f"- task_pack_path: `{bundle['task_pack_path']}`",
            f"- agent_visible_path: `{receipt['agent_visible_path']}`",
            "- The agent pack is the public contract surface (instruction, stages, "
            "allowed context). It must not include oracle, bad answer, or private checks.",
            "",
            "## 4. What hidden truth exists, without showing it?",
            "",
            f"- hidden_truth_path: `{receipt['hidden_truth_path']}`",
            f"- oracle_present: `{json.dumps(receipt['oracle_present'])}`",
            f"- bad_answer_present: `{json.dumps(receipt['bad_answer_present'])}`",
            f"- private_checks_present: `{json.dumps(receipt['private_checks_present'])}`",
            f"- agent_pack_omits_oracle: `{json.dumps(receipt['agent_pack_omits_oracle'])}`",
            f"- agent_pack_omits_bad_answer: `{json.dumps(receipt['agent_pack_omits_bad_answer'])}`",
            f"- agent_pack_omits_private_checks: `{json.dumps(receipt['agent_pack_omits_private_checks'])}`",
            f"- oracle_field_count: `{receipt.get('oracle_field_count', 0)}`",
            f"- bad_answer_field_count: `{receipt.get('bad_answer_field_count', 0)}`",
            f"- private_check_count: `{receipt.get('private_check_count', 0)}`",
            f"- hidden_truth_sha256: `{receipt.get('hidden_truth_sha256', '')}`",
            "",
            "Hidden truth content is intentionally omitted from this bundle.",
            "",
            "## 5. How would this map to a future Harbor/Tempo-style eval task?",
            "",
            f"- preview_only: `{json.dumps(harbor['preview_only'])}`",
            f"- runner_integration: `{harbor['runner_integration']}`",
            f"- environment.mode: `{harbor['environment']['mode']}`",
            f"- test_ref.workflow_id: `{harbor['test_ref']['workflow_id']}`",
            f"- expected_artifact: {harbor['expected_artifact']}",
            f"- isolation_note: {harbor['isolation_note']}",
            "",
            "## 6. What verifier result or product action exists now?",
            "",
        ]
    )

    if "verifier_result_path" in bundle:
        lines.append(f"- verifier_result_path: `{bundle['verifier_result_path']}`")
    else:
        lines.append("- verifier_result_path: _(not present yet)_")

    actions = bundle.get("improvement_actions")
    if actions:
        lines.append("- improvement_actions:")
        for action in actions:
            surface = action.get("product_surface", "?")
            summary = action.get("summary", "")
            lines.append(f"  - [{surface}] {summary}")
    else:
        lines.append("- improvement_actions: _(not present yet)_")

    lines.append("")
    body = "\n".join(line.rstrip() for line in lines).rstrip() + "\n"
    return body


def write_contract_bundle(bundle: Dict[str, Any]) -> tuple[Path, Path]:
    """Write JSON + markdown contract bundles under artifacts/contracts/."""
    CONTRACT_DIR.mkdir(parents=True, exist_ok=True)
    workflow_id = bundle["workflow_id"]
    json_path = CONTRACT_DIR / f"{workflow_id}.contract_bundle.json"
    md_path = CONTRACT_DIR / f"{workflow_id}.contract_bundle.md"

    json_path.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_contract_markdown(bundle), encoding="utf-8")

    # Re-read and re-assert firewall on the durable artifact.
    written = _load_json(json_path)
    hidden_path = ROOT / written["hidden_truth_receipt"]["hidden_truth_path"]
    assert_receipt_firewall(
        written["hidden_truth_receipt"],
        hidden_truth_path=hidden_path,
    )
    _assert_bundle_omits_hidden_content(written, hidden_path)
    return json_path, md_path


def compile_and_write(
    candidate: WorkflowCandidate,
    *,
    agent_visible_path: Optional[Path] = None,
    hidden_truth_path: Optional[Path] = None,
    verifier_result_path: Optional[Path] = None,
    improvement_actions: Optional[Sequence[ImprovementAction]] = None,
    ensure_materialized: bool = True,
) -> tuple[Dict[str, Any], Path, Path]:
    """Compile and persist the contract bundle for one workflow."""
    # Touch build helpers so imports stay honest about agent-visible derivation.
    _ = to_agent_task(build_task_pack(candidate), candidate)
    _ = build_hidden_truth(candidate)

    bundle = compile_contract_bundle(
        candidate,
        agent_visible_path=agent_visible_path,
        hidden_truth_path=hidden_truth_path,
        verifier_result_path=verifier_result_path,
        improvement_actions=improvement_actions,
        ensure_materialized=ensure_materialized,
    )
    json_path, md_path = write_contract_bundle(bundle)
    return bundle, json_path, md_path
