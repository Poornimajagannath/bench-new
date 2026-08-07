#!/usr/bin/env python3
"""DocETL-inspired stage: raw questions → extract → suggest (+ show PM-approved set).

Does not import the real `docetl` package.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.discovery import synthesize_candidates_payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract/suggest workflow candidates from raw forum/docs/support questions"
    )
    parser.add_argument("--workflow", default=None, help="Optional suggested workflow_id filter")
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts" / "candidates.json"),
        help="Output path for candidates JSON",
    )
    args = parser.parse_args()

    payload = synthesize_candidates_payload(workflow_id=args.workflow)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"[synthesize_candidates] wrote {out_path}")
    print(f"[synthesize_candidates] suggestions={payload['suggestion_count']}")
    for row in payload["suggestions"]:
        s = row["suggestion"]
        e = row["extraction"]
        print(
            f"  - seed={s['seed_id']} suggest={s['suggested_workflow_id']} "
            f"entities={e['entities']}"
        )
    print(f"[synthesize_candidates] pm_approved={payload['approved_candidate_count']}")
    for c in payload["approved_candidates"]:
        print(f"  - approved {c['workflow_id']} ({c['pm_decision']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
