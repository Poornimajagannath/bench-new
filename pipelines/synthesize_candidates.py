#!/usr/bin/env python3
"""DocETL-style stage: frozen seeds → typed workflow candidates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.discovery import synthesize_candidates_payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Synthesize typed workflow candidates from frozen seeds")
    parser.add_argument("--workflow", default=None, help="Optional workflow_id filter")
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
    print(f"[synthesize_candidates] candidates={payload['candidate_count']}")
    for c in payload["candidates"]:
        print(f"  - {c['workflow_id']}: {c['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
