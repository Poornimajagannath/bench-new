"""Generated content/ pages must never contain raw brace anchors."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
BRACE_ANCHOR = re.compile(r"\{#[^}]+\}")


class ContentNoBraceAnchorTests(unittest.TestCase):
    def test_no_generated_page_has_raw_brace_anchor(self):
        if not CONTENT.is_dir():
            self.skipTest("content/ not present")
        pages = sorted(CONTENT.rglob("*.md"))
        self.assertTrue(pages, "expected generated pages under content/")
        offenders = []
        for path in pages:
            text = path.read_text(encoding="utf-8", errors="replace")
            if BRACE_ANCHOR.search(text):
                offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual(
            offenders,
            [],
            msg="raw {#anchor} leaked into content/:\n  " + "\n  ".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
