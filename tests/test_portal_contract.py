"""Portal contract: content-only serve path, honest empty state."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / "portal" / "server.js"


class PortalContractTests(unittest.TestCase):
    def test_empty_state_mentions_content_only(self):
        script = """
const { emptyState } = require('./portal/server.js');
process.stdout.write(emptyState());
"""
        proc = subprocess.run(
            ["node", "-e", script],
            cwd=str(ROOT),
            check=True,
            capture_output=True,
            text=True,
        )
        html = proc.stdout
        self.assertIn("No generated pages yet", html)
        self.assertIn("content/*.md", html)
        self.assertNotIn("Auth Setup", html)
        self.assertNotIn("quickstart-data", html)

    def test_render_markdown_no_fence_leak_outside_code(self):
        script = r"""
const { renderMarkdown } = require('./portal/server.js');
const html = renderMarkdown('# Hi\n\n```js\nconst a = 1;\n```\n\nDone.\n');
if (html.includes('<h1>Hi</h1>') && html.includes('<pre><code>') && !html.includes('```')) {
  process.stdout.write('ok');
} else {
  process.stdout.write(html);
  process.exit(1);
}
"""
        proc = subprocess.run(
            ["node", "-e", script],
            cwd=str(ROOT),
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.stdout.strip(), "ok")

    def test_no_hand_pasted_quickstart_module(self):
        banned = ROOT / "lib" / "quickstart-data.js"
        self.assertFalse(banned.exists(), "hand-pasted quickstart-data.js must not return")


if __name__ == "__main__":
    unittest.main()
