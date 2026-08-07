#!/usr/bin/env python3
"""A3: draft customer-facing Overview prose for content pages (facts untouched)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from content_bench.content_engine.humanizer import (  # noqa: E402
    FactHashGuardError,
    fact_hash,
    write_prose,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown pages under content/. Default: all content/*.md",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print summary without writing files",
    )
    args = parser.parse_args()
    paths = list(args.paths) or sorted((ROOT / "content").glob("*.md"))
    results = []
    for path in paths:
        if path.name == "README.md":
            continue
        original = path.read_text(encoding="utf-8")
        before = fact_hash(original)
        try:
            updated = write_prose(original)
        except FactHashGuardError as exc:
            print(f"FACT_HASH_GUARD: {path}: {exc}", file=sys.stderr)
            return 2
        after = fact_hash(updated)
        changed = updated != original
        try:
            rel = str(path.resolve().relative_to(ROOT))
        except ValueError:
            rel = str(path)
        results.append(
            {
                "path": rel,
                "changed": changed,
                "fact_hash": after.digest,
                "facts_preserved": before.digest == after.digest,
            }
        )
        if changed and not args.dry_run:
            path.write_text(updated, encoding="utf-8")
    print(json.dumps({"ok": True, "pages": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
