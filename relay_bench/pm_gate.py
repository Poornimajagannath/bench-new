"""PM approve/edit gate between DocETL-inspired suggestions and Relay Bench task packs.

V0 uses frozen PM decisions under data/pm_approvals.json (local proof, no UI).
Rejected suggestions never become task packs or verifiers.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

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


def apply_pm_decisions(
    rows: Iterable[Tuple[RawQuestion, Extraction, WorkflowSuggestion]],
    decisions: Dict[str, PmDecision],
) -> List[WorkflowCandidate]:
    """Apply PM approve/edit; only approved/edited rows become workflow candidates."""
    approved: List[WorkflowCandidate] = []
    for question, extraction, suggestion in rows:
        decision = decisions.get(question.seed_id)
        if decision is None:
            # No PM decision yet — hold for review; do not create task packs.
            continue
        if decision.decision == "reject":
            continue

        workflow_id = decision.approved_workflow_id or suggestion.suggested_workflow_id
        catalog = catalog_entry(workflow_id)
        stages = list(decision.edited_stages or suggestion.stages)
        goal = decision.edited_goal or extraction.goal

        confusion = list(extraction.symptoms)
        for entity in extraction.entities:
            marker = f"entity:{entity}"
            if marker not in confusion:
                confusion.append(marker)

        approved.append(
            WorkflowCandidate(
                workflow_id=workflow_id,
                title=str(catalog["title"]),
                goal=goal,
                stages=stages,
                api_sdk_facts=list(catalog["api_sdk_facts"]),  # type: ignore[arg-type]
                confusion_points=confusion,
                seed_ids=[question.seed_id],
                surface_hints=list(catalog.get("surface_hints", [])),  # type: ignore[arg-type]
                pm_decision=decision.decision,
                extraction=extraction.to_dict(),
                suggestion=suggestion.to_dict(),
            )
        )
    return approved


def require_pm_approved_candidate(
    workflow_id: str,
    rows: Optional[List[Tuple[RawQuestion, Extraction, WorkflowSuggestion]]] = None,
) -> WorkflowCandidate:
    """Fetch a single PM-approved candidate or raise."""
    from relay_bench.discovery import discover_suggestions

    suggestion_rows = rows if rows is not None else discover_suggestions()
    approved = apply_pm_decisions(suggestion_rows, load_pm_decisions())
    matches = [c for c in approved if c.workflow_id == workflow_id]
    if not matches:
        raise LookupError(
            f"No PM-approved candidate for workflow_id={workflow_id!r}. "
            "DocETL-inspired suggestions require PM approve/edit before task pack creation."
        )
    return matches[0]
