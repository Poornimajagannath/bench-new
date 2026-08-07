#!/usr/bin/env python3
"""Fail closed if rendered content HTML leaks raw markdown or broken local links."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PORTAL = ROOT / "portal" / "server.js"

# Raw markdown that must not appear in rendered HTML body text.
LEAK_PATTERNS = (
    re.compile(r"```"),
    re.compile(r"(?m)^#{1,6}\s+\S"),
)


def render_via_node(md: str) -> str:
    script = f"""
const {{ renderMarkdown }} = require({str(PORTAL)!r});
const md = {md!r};
process.stdout.write(renderMarkdown(md));
"""
    proc = subprocess.run(
        ["node", "-e", script],
        check=True,
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    return proc.stdout


def check_leaks(html: str) -> list[str]:
    issues = []
    for pat in LEAK_PATTERNS:
        if pat.search(html):
            issues.append(f"raw markdown leak matched {pat.pattern}")
    return issues


def check_local_links(md_files: list[Path]) -> list[str]:
    issues = []
    names = {p.stem for p in md_files}
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        for _, target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            slug = target.removesuffix(".md").lstrip("./")
            if slug not in names and not (CONTENT / f"{slug}.md").exists():
                issues.append(f"{path.name}: broken local link -> {target}")
    return issues


def main() -> int:
    md_files = sorted(CONTENT.glob("*.md"))
    # README is documentation for authors, not a portal page — skip link target requirement to itself.
    page_files = [p for p in md_files if p.name.lower() != "readme.md"]

    issues: list[str] = []
    sample = "# Title\n\nHello **world**\n\n```js\nconst x = 1;\n```\n"
    html = render_via_node(sample)
    if "<h1>Title</h1>" not in html:
        issues.append("renderer failed to emit h1")
    if "<code>" not in html and "<pre>" not in html:
        issues.append("renderer failed to emit code block")
    # Code content is escaped inside <pre><code>, so ``` fences must not remain.
    issues.extend(check_leaks(re.sub(r"<pre><code>.*?</code></pre>", "", html, flags=re.S)))

    for path in page_files:
        body = path.read_text(encoding="utf-8")
        rendered = render_via_node(body)
        issues.extend(f"{path.name}: {msg}" for msg in check_leaks(
            re.sub(r"<pre><code>.*?</code></pre>", "", rendered, flags=re.S)
        ))

    issues.extend(check_local_links(page_files))

    if issues:
        print("content render check FAILED:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(f"content render check OK ({len(page_files)} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
