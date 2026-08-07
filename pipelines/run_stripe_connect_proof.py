#!/usr/bin/env python3
"""Stripe Connect proof: source mix → ingest → content facts + quickstart."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from relay_bench.content_engine.stripe_connect import run_stripe_connect_proof  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Stripe Connect content-engine proof")
    parser.add_argument("--stamp-date", default=None, help="YYYY-MM-DD for raw/ stamp")
    args = parser.parse_args()
    summary = run_stripe_connect_proof(stamp_date=args.stamp_date)
    print(json.dumps(summary, indent=2))
    print(f"Wrote content pages: {', '.join(summary['content_pages'])}")
    return 0 if summary.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
