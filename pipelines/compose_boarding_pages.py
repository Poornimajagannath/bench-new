#!/usr/bin/env python3
"""Step 4: compose boarding workflow pages from normalized claims.

Reads normalized/ only (never raw/). Runs the humanizer with the fact-hash
guard on every page. Writes a composition report with the prefer-child
dedupe residuals.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from content_bench.content_engine.humanizer import (  # noqa: E402
    assert_facts_unchanged,
    humanize,
)
from content_bench.content_engine.workflow_pages import compose_all  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--claims",
        default=str(ROOT / "normalized/2026-08-08-boarding.claims.json"),
    )
    parser.add_argument(
        "--out-dir", default=str(ROOT / "content/boarding/workflows")
    )
    parser.add_argument(
        "--report",
        default=str(ROOT / "artifacts/content_engine/boarding/composition-report.json"),
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    result = compose_all(Path(args.claims), out_dir=out_dir)

    # Humanize prose sections; fact-hash guard must hold on every page.
    for page in result["pages"]:
        path = ROOT / page["path"] if not Path(page["path"]).is_absolute() else Path(page["path"])
        original = path.read_text(encoding="utf-8")
        updated = humanize(original)
        assert_facts_unchanged(original, updated)
        path.write_text(updated, encoding="utf-8")
        page["fact_hash_guard"] = "pass"

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(f"pages={len(result['pages'])} out_dir={out_dir}")
    print(
        f"claims={result['claims_total']} after_prefer_child={result['claims_after_prefer_child']} "
        f"mega_residuals={result['mega_residuals']}"
    )
    for p in result["pages"]:
        print(f"  {p['workflow_id']}: steps={p['steps']} gaps={p['gaps']} guard={p['fact_hash_guard']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
