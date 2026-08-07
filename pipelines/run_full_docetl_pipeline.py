#!/usr/bin/env python3
"""Run the whole Content Bench + Content Engine pipeline with real DocETL.

Uses repo-tracked Payment Gateway lab docs from context/, scenarios/, templates/
plus the Microform quickstart fixture.

Stages:
  1) synthesize candidates (heuristic discovery artifact refresh)
  2) content engine extract/promote for every enabled source (--discovery docetl)
  3) bench_v0 for every PM-approved workflow (--discovery docetl)

Honesty: DocETL code_map only (no LLM). Labels must read imported-code_map.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.docetl_adapter import docetl_available
from content_bench.content_engine.pipeline import run_content_engine
from content_bench.content_engine.registry import list_enabled_sources
from content_bench.discovery import synthesize_candidates_payload
from content_bench.reporting import repo_relative


def _load_bench_module():
    path = ROOT / "pipelines" / "run_bench_v0.py"
    spec = importlib.util.spec_from_file_location("run_bench_v0", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _write_json(path: Path, payload: Dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Full DocETL-backed Content Bench pipeline")
    parser.add_argument(
        "--discovery",
        default="docetl",
        choices=["docetl", "docetl-llm", "heuristic"],
        help="Extract/discovery backend (default: docetl)",
    )
    parser.add_argument(
        "--fallback-on-error",
        action="store_true",
        help="Fall back to heuristic if DocETL cannot run",
    )
    parser.add_argument(
        "--skip-bench",
        action="store_true",
        help="Only run content engine + candidates synthesize",
    )
    args = parser.parse_args()

    if args.discovery.startswith("docetl") and not docetl_available():
        print(
            "[full_docetl] docetl package missing; pip install -r requirements-docetl.txt",
            file=sys.stderr,
        )
        return 2

    started = datetime.now(timezone.utc).isoformat()
    print(f"[full_docetl] start discovery={args.discovery} docetl_available={docetl_available()}")

    print("[full_docetl] stage=synthesize_candidates")
    candidates = synthesize_candidates_payload()
    candidates_path = ROOT / "artifacts" / "candidates.json"
    _write_json(candidates_path, candidates)
    print(
        f"[full_docetl] candidates suggestions={candidates['suggestion_count']} "
        f"approved={candidates['approved_candidate_count']} path={repo_relative(candidates_path)}"
    )

    sources = sorted(list_enabled_sources(), key=lambda r: r.source_id)
    content_results: List[Dict[str, Any]] = []
    print(f"[full_docetl] stage=content_engine sources={len(sources)}")
    for record in sources:
        print(f"[full_docetl] content_engine source={record.source_id} type={record.source_type}")
        try:
            result = run_content_engine(
                record.source_id,
                discovery=args.discovery,
                fallback_on_error=args.fallback_on_error,
            )
        except Exception as exc:  # noqa: BLE001 - record and continue
            result = {
                "ok": False,
                "source_id": record.source_id,
                "error": str(exc),
                "honest_label": {"docetl": "error"},
            }
            print(f"[full_docetl] ERROR source={record.source_id}: {exc}", file=sys.stderr)
        content_results.append(result)
        label = (result.get("honest_label") or {}).get("docetl")
        print(
            f"[full_docetl]   status={result.get('promotion_status', 'error')} "
            f"units={result.get('unit_count', 0)} docetl={label} ok={result.get('ok')}"
        )

    bench_results: List[Dict[str, Any]] = []
    if not args.skip_bench:
        bench = _load_bench_module()
        print("[full_docetl] stage=bench_v0")
        for workflow_id in sorted(bench.SUPPORTED):
            print(f"[full_docetl] bench workflow={workflow_id}")
            code = bench.run_pipeline(
                workflow_id,
                discovery=args.discovery,
                fallback_on_error=args.fallback_on_error,
            )
            bench_results.append({"workflow_id": workflow_id, "exit_code": code, "ok": code == 0})
            print(f"[full_docetl]   bench ok={code == 0} exit={code}")

    summary = {
        "started_at": started,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "discovery": args.discovery,
        "docetl_available": docetl_available(),
        "candidates_path": repo_relative(candidates_path),
        "content_engine": content_results,
        "bench": bench_results,
        "promoted_count": sum(1 for r in content_results if r.get("ok")),
        "blocked_count": sum(1 for r in content_results if not r.get("ok")),
        "bench_ok_count": sum(1 for r in bench_results if r.get("ok")),
        "honest_labels": sorted(
            {
                (r.get("honest_label") or {}).get("docetl", "unknown")
                for r in content_results
            }
        ),
    }
    out = ROOT / "artifacts" / "full_docetl_run.json"
    _write_json(out, summary)
    print(f"[full_docetl] summary={repo_relative(out)}")
    print(json.dumps({k: summary[k] for k in (
        "discovery", "promoted_count", "blocked_count", "bench_ok_count", "honest_labels"
    )}, indent=2))

    # Fail if DocETL was requested but nothing got an imported label.
    if args.discovery == "docetl":
        if "imported-code_map" not in summary["honest_labels"]:
            print("[full_docetl] DocETL did not execute for any source", file=sys.stderr)
            return 3
    if summary["blocked_count"] and summary["promoted_count"] == 0:
        return 1
    if bench_results and summary["bench_ok_count"] != len(bench_results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
