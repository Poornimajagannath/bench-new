#!/usr/bin/env python3
"""A2: turn api_reference_unit drafts into published content/*.md pages."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from content_bench.content_engine.reference_pages import write_reference_pages  # noqa: E402


def main() -> int:
    summary = write_reference_pages()
    print(json.dumps(summary, indent=2))
    print("Wrote pages:", ", ".join(summary["pages_written"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
