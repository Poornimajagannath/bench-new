"""PM-readable report generation for Relay Bench V0 proofs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from relay_bench.schemas import (
    BenchReport,
    FailureClassification,
    VerifierResult,
    WorkflowCandidate,
)

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "artifacts" / "reports"


def repo_relative(path: Path | str) -> str:
    """Emit portable repo-relative paths (e.g. artifacts/task_packs/...)."""
    p = Path(path)
    resolved = p.resolve() if p.is_absolute() else (ROOT / p).resolve()
    try:
        return resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        # Outside the repo: fall back to the original path string.
        return Path(path).as_posix()


def build_report(
    candidate: WorkflowCandidate,
    classification: FailureClassification,
    bad_result: VerifierResult,
    task_pack_path: Path,
    verifier_result_path: Path,
    bad_answer_mistake: str | None = None,
) -> BenchReport:
    bad_errors = [c.detail for c in bad_result.checks if not c.passed]
    if bad_answer_mistake:
        bad_errors.insert(0, bad_answer_mistake)

    next_improvements = [a.summary for a in classification.actions]

    return BenchReport(
        workflow_id=candidate.workflow_id,
        developer_confusion=list(candidate.confusion_points),
        relay_discovered=[
            candidate.goal,
            f"stages:{','.join(candidate.stages)}",
            *[f"fact:{f}" for f in candidate.api_sdk_facts],
        ],
        bad_answer_errors=bad_errors or list(bad_result.caught_failures),
        verifier_caught=list(bad_result.caught_failures),
        next_product_improvements=next_improvements,
        classification=classification,
        task_pack_path=repo_relative(task_pack_path),
        verifier_result_path=repo_relative(verifier_result_path),
    )


def render_markdown(report: BenchReport) -> str:
    lines: List[str] = [
        f"# Relay Bench V0 Report — `{report.workflow_id}`",
        "",
        "Local proof only. No network. No live credentials.",
        "",
        "## 1. What developers were confused about",
        "",
    ]
    for item in report.developer_confusion:
        lines.append(f"- {item}")
    lines.extend(["", "## 2. What Relay discovered", ""])
    for item in report.relay_discovered:
        lines.append(f"- {item}")
    lines.extend(["", "## 3. What the bad answer got wrong", ""])
    for item in report.bad_answer_errors:
        lines.append(f"- {item}")
    lines.extend(["", "## 4. How the verifier caught it", ""])
    for item in report.verifier_caught:
        lines.append(f"- failed check `{item}`")
    lines.extend(["", "## 5. What product surface improves next", ""])
    for item in report.next_product_improvements:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Classification",
            "",
            f"- category: `{report.classification.category}`",
            f"- summary: {report.classification.summary}",
            "",
            "## Artifacts",
            "",
            f"- task pack: `{report.task_pack_path}`",
            f"- verifier results: `{report.verifier_result_path}`",
            "",
        ]
    )

    # Highlight Relay CLI descriptor when present
    for action in report.classification.actions:
        if action.product_surface == "vap_cli" and action.vap_cli is not None:
            cli = action.vap_cli
            lines.extend(
                [
                    "## Relay CLI workflow verifier (recommended)",
                    "",
                    f"- goal: {cli.goal}",
                    f"- command: `{cli.command}`",
                    "- readiness checks:",
                ]
            )
            for rc in cli.readiness_checks:
                lines.append(f"  - {rc}")
            lines.extend(["- recovery path:"])
            for rp in cli.recovery_path:
                lines.append(f"  - {rp}")
            break

    # Exactly one trailing newline; no blank line at EOF.
    body = "\n".join(line.rstrip() for line in lines).rstrip() + "\n"
    return body


def write_report(report: BenchReport) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    md_path = REPORT_DIR / f"{report.workflow_id}.report.md"
    json_path = REPORT_DIR / f"{report.workflow_id}.report.json"
    md_path.write_text(render_markdown(report), encoding="utf-8")
    json_path.write_text(json.dumps(report.to_dict(), indent=2) + "\n", encoding="utf-8")
    return md_path, json_path
