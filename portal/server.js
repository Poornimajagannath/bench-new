#!/usr/bin/env node
/**
 * Thin portal: serves content/*.md only.
 * Never reads raw/ or hand-pasted JS data modules.
 */
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CONTENT_DIR = path.join(ROOT, "content");
const PORT = Number(process.env.PORT || 8787);

function listMarkdown() {
  if (!fs.existsSync(CONTENT_DIR)) return [];
  return fs
    .readdirSync(CONTENT_DIR)
    .filter(
      (name) =>
        name.endsWith(".md") && name.toLowerCase() !== "readme.md"
    )
    .sort();
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderMarkdown(md) {
  // Minimal, dependency-free renderer sufficient for CI leak checks.
  const lines = md.replace(/\r\n/g, "\n").split("\n");
  const html = [];
  let inCode = false;
  let inList = false;

  const closeList = () => {
    if (inList) {
      html.push("</ul>");
      inList = false;
    }
  };

  for (const line of lines) {
    if (line.startsWith("```")) {
      closeList();
      if (!inCode) {
        html.push("<pre><code>");
        inCode = true;
      } else {
        html.push("</code></pre>");
        inCode = false;
      }
      continue;
    }
    if (inCode) {
      html.push(`${escapeHtml(line)}\n`);
      continue;
    }
    if (/^#\s+/.test(line)) {
      closeList();
      html.push(`<h1>${escapeHtml(line.replace(/^#\s+/, ""))}</h1>`);
      continue;
    }
    if (/^##\s+/.test(line)) {
      closeList();
      html.push(`<h2>${escapeHtml(line.replace(/^##\s+/, ""))}</h2>`);
      continue;
    }
    if (/^###\s+/.test(line)) {
      closeList();
      html.push(`<h3>${escapeHtml(line.replace(/^###\s+/, ""))}</h3>`);
      continue;
    }
    if (/^[-*]\s+/.test(line)) {
      if (!inList) {
        html.push("<ul>");
        inList = true;
      }
      html.push(`<li>${escapeHtml(line.replace(/^[-*]\s+/, ""))}</li>`);
      continue;
    }
    if (!line.trim()) {
      closeList();
      continue;
    }
    closeList();
    const withLinks = escapeHtml(line).replace(
      /\[([^\]]+)\]\(([^)]+)\)/g,
      '<a href="$2">$1</a>'
    );
    html.push(`<p>${withLinks}</p>`);
  }
  closeList();
  if (inCode) html.push("</code></pre>");
  return html.join("\n");
}

function layout(title, body) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>${escapeHtml(title)}</title>
  <style>
    body { font-family: Georgia, "Times New Roman", serif; margin: 2rem auto; max-width: 42rem; line-height: 1.5; color: #1a1a1a; background: #f7f4ef; }
    a { color: #0b4f6c; }
    pre { background: #1a1a1a; color: #f7f4ef; padding: 1rem; overflow: auto; }
    .empty { border: 1px dashed #8a8178; padding: 1.5rem; background: #fffdf8; }
    nav a { margin-right: 1rem; }
  </style>
</head>
<body>
${body}
</body>
</html>`;
}

function emptyState() {
  return layout(
    "Content portal",
    `<h1>Content portal</h1>
<div class="empty">
  <p>No generated pages yet.</p>
  <p>This portal reads only <code>content/*.md</code>. It never serves hand-pasted JS data modules or <code>raw/</code>.</p>
  <p>Run the content pipeline, approve a PR, and pages will appear here.</p>
</div>`
  );
}

function indexPage(files) {
  if (!files.length) return emptyState();
  const links = files
    .map((f) => {
      const slug = f.replace(/\.md$/, "");
      return `<li><a href="/${encodeURIComponent(slug)}">${escapeHtml(slug)}</a></li>`;
    })
    .join("\n");
  return layout(
    "Content portal",
    `<h1>Content portal</h1><nav><ul>${links}</ul></nav>`
  );
}

function pageFor(slug) {
  const file = path.join(CONTENT_DIR, `${slug}.md`);
  if (!fs.existsSync(file)) return null;
  const md = fs.readFileSync(file, "utf8");
  const body = `<nav><a href="/">All pages</a></nav>\n${renderMarkdown(md)}`;
  return layout(slug, body);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url || "/", `http://${req.headers.host || "localhost"}`);
  const files = listMarkdown();

  if (url.pathname === "/" || url.pathname === "") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(indexPage(files));
    return;
  }

  if (url.pathname === "/healthz") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ ok: true, pages: files.length, reads: ["content/"] }));
    return;
  }

  const slug = decodeURIComponent(url.pathname.replace(/^\//, "")).replace(/\/$/, "");
  if (slug.includes("..") || slug.includes("/") || slug.includes("\\")) {
    res.writeHead(400, { "Content-Type": "text/plain" });
    res.end("Bad path");
    return;
  }
  const page = pageFor(slug);
  if (!page) {
    res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
    res.end(layout("Not found", `<h1>Not found</h1><p>No content page named ${escapeHtml(slug)}.</p>`));
    return;
  }
  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  res.end(page);
});

if (require.main === module) {
  server.listen(PORT, "127.0.0.1", () => {
    console.log(`Portal serving content/ on http://127.0.0.1:${PORT}`);
  });
}

module.exports = { renderMarkdown, listMarkdown, CONTENT_DIR, emptyState };
