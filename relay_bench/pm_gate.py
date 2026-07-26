"""PM approve/edit gate between DocETL-inspired suggestions and Relay Bench task packs.

V0 uses frozen PM decisions under data/pm_approvals.json (local proof, no UI).
Rejected suggestions never become task packs or verifiers.

Approved seeds are reduced by workflow_id: many confused inputs → one richer
workflow contract (merged seed_ids, symptoms/entities/confusion, PM edits).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from relay_bench.discovery import catalog_entry
from relay_bench.schemas import (
    Extraction,
    PmDecision,
    RawQuestion,
    WorkflowCandidate,
    WorkflowSuggestion,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PM_PATH = ROOT / "data" / "pm_approvals.json"

ApprovedRow = Tuple[RawQuestion, Extraction, WorkflowSuggestion, PmDecision]


def load_pm_decisions(path: Optional[Path] = None) -> Dict[str, PmDecision]:
    pm_path = path or DEFAULT_PM_PATH
    raw = json.loads(pm_path.read_text(encoding="utf-8"))
    decisions: Dict[str, PmDecision] = {}
    for item in raw:
        decision = PmDecision(
            seed_id=item["seed_id"],
            decision=item["decision"],
            approved_workflow_id=item["approved_workflow_id"],
            edited_stages=item.get("edited_stages"),
            edited_goal=item.get("edited_goal"),
            pm_notes=item.get("pm_notes", ""),
        )
        if decision.decision not in {"approve", "edit", "reject"}:
            raise ValueError(f"Invalid PM decision for {decision.seed_id}: {decision.decision}")
        decisions[decision.seed_id] = decision
    return decisions


def _unique_extend(target: List[str], values: Sequence[str]) -> None:
    for value in values:
        if value not in target:
            target.append(value)


def _default_stages_for_approved_workflow(
    workflow_id: str,
    rows: Sequence[ApprovedRow],
) -> List[str]:
    """Stages when PM did not supply edited_stages.

    Always prefer the *approved* workflow catalog. Never keep suggestion stages
    after a PM remaps approved_workflow_id away from suggested_workflow_id.
    """
    catalog_stages = list(catalog_entry(workflow_id)["stages"])  # type: ignore[arg-type]
    remapped = any(
        bool(decision.approved_workflow_id)
        and decision.approved_workflow_id != suggestion.suggested_workflow_id
        for _q, _e, suggestion, decision in rows
    )
    if remapped:
        return catalog_stages

    # Same-workflow approve: suggestion stages should match catalog; catalog wins.
    return catalog_stages


def _resolve_workflow_edits(
    workflow_id: str,
    rows: Sequence[ApprovedRow],
) -> Tuple[List[str], str, str]:
    """Resolve stages/goal/pm_decision at workflow level from per-seed PM decisions."""
    edited_stages_options = [
        list(decision.edited_stages)
        for _q, _e, _s, decision in rows
        if decision.edited_stages
    ]
    if edited_stages_options:
        stages = edited_stages_options[0]
        for other in edited_stages_options[1:]:
            if other != stages:
                raise ValueError(
                    "Conflicting PM edited_stages for the same workflow_id: "
                    f"{stages!r} vs {other!r}"
                )
    else:
        stages = _default_stages_for_approved_workflow(workflow_id, rows)

    edited_goals = [
        decision.edited_goal
        for _q, _e, _s, decision in rows
        if decision.edited_goal
    ]
    if edited_goals:
        goal = edited_goals[0]
        for other in edited_goals[1:]:
            if other != goal:
                raise ValueError(
                    "Conflicting PM edited_goal for the same workflow_id: "
                    f"{goal!r} vs {other!r}"
                )
    else:
        # Prefer first extraction goal; keep additional goals in confusion merge.
        goal = rows[0][1].goal

    pm_decision = "edit" if any(d.decision == "edit" for *_rest, d in rows) else "approve"
    return stages, goal, pm_decision


def _reduce_workflow_group(
    workflow_id: str,
    rows: Sequence[ApprovedRow],
) -> WorkflowCandidate:
    catalog = catalog_entry(workflow_id)
    stages, goal, pm_decision = _resolve_workflow_edits(workflow_id, rows)

    seed_ids: List[str] = []
    confusion: List[str] = []
    symptoms: List[str] = []
    entities: List[str] = []
    goals: List[str] = []
    rationales: List[str] = []
    pm_notes: List[str] = []

    for question, extraction, suggestion, decision in rows:
        _unique_extend(seed_ids, [question.seed_id])
        _unique_extend(symptoms, extraction.symptoms)
        _unique_extend(entities, extraction.entities)
        _unique_extend(goals, [extraction.goal])
        _unique_extend(rationales, suggestion.rationale)
        if decision.pm_notes:
            _unique_extend(pm_notes, [decision.pm_notes])

        _unique_extend(confusion, extraction.symptoms)
        for entity in extraction.entities:
            _unique_extend(confusion, [f"entity:{entity}"])
        if extraction.goal != goal:
            _unique_extend(confusion, [f"alt_goal:{extraction.goal}"])

    return WorkflowCandidate(
        workflow_id=workflow_id,
        title=str(catalog["title"]),
        goal=goal,
        stages=stages,
        api_sdk_facts=list(catalog["api_sdk_facts"]),  # type: ignore[arg-type]
        confusion_points=confusion,
        seed_ids=seed_ids,
        surface_hints=list(catalog.get("surface_hints", [])),  # type: ignore[arg-type]
        pm_decision=pm_decision,
        extraction={
            "seed_ids": seed_ids,
            "goals": goals,
            "symptoms": symptoms,
            "entities": entities,
            "merged_from_seed_count": len(seed_ids),
        },
        suggestion={
            "approved_workflow_id": workflow_id,
            "original_suggested_workflow_ids": sorted(
                {
                    suggestion.suggested_workflow_id
                    for _q, _e, suggestion, _d in rows
                }
            ),
            "stages": stages,
            "rationale": rationales,
            "pm_notes": pm_notes,
            "merged_from_seed_count": len(seed_ids),
            "remapped_from_suggestion": any(
                bool(decision.approved_workflow_id)
                and decision.approved_workflow_id != suggestion.suggested_workflow_id
                for _q, _e, suggestion, decision in rows
            ),
        },
    )


def apply_pm_decisions(
    rows: Iterable[Tuple[RawQuestion, Extraction, WorkflowSuggestion]],
    decisions: Dict[str, PmDecision],
) -> List[WorkflowCandidate]:
    """Approve/edit per seed, then reduce by workflow_id into richer candidates."""
    grouped: Dict[str, List[ApprovedRow]] = {}
    for question, extraction, suggestion in rows:
        decision = decisions.get(question.seed_id)
        if decision is None:
            # No PM decision yet — hold for review; do not create task packs.
            continue
        if decision.decision == "reject":
            continue

        workflow_id = decision.approved_workflow_id or suggestion.suggested_workflow_id
        grouped.setdefault(workflow_id, []).append(
            (question, extraction, suggestion, decision)
        )

    return [
        _reduce_workflow_group(workflow_id, group_rows)
        for workflow_id, group_rows in sorted(grouped.items())
    ]


def require_pm_approved_candidate(
    workflow_id: str,
    rows: Optional[List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]]] = None,
) -> WorkflowCandidate:
    """Fetch the single reduced PM-approved candidate for a workflow, or raise."""
    from relay_bench.discovery import discover_suggestions

    suggestion_rows = rows if rows is not None else discover_suggestions()
    approved = apply_pm_decisions(suggestion_rows, load_pm_decisions())
    matches = [c for c in approved if c.workflow_id == workflow_id]
    if not matches:
        raise LookupError(
            f"No PM-approved candidate for workflow_id={workflow_id!r}. "
            "DocETL-inspired suggestions require PM approve/edit before task pack creation."
        )
    if len(matches) > 1:
        raise RuntimeError(
            f"Expected one reduced candidate for {workflow_id!r}, found {len(matches)}. "
            "apply_pm_decisions must group by workflow_id."
        )
    return matches[0]
