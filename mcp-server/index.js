#!/usr/bin/env node
// content-docs MCP server.
// Serves ONLY generated documentation: content/*.md pages and the
// spec-generated reference units in artifacts/content_engine/generated/.
// It never reads raw/ (the ingestion clean-room contract).
// Every hand test can be logged to evals/manual-runs.jsonl so manual
// testing feeds the same evidence stream as automated tempo evals.

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CONTENT_DIR = path.join(ROOT, "content");
const GENERATED_DIR = path.join(ROOT, "artifacts", "content_engine", "generated");
const EVAL_LOG = path.join(ROOT, "evals", "manual-runs.jsonl");

function listPages() {
  if (!fs.existsSync(CONTENT_DIR)) return [];
  return fs
    .readdirSync(CONTENT_DIR)
    .filter((f) => f.endsWith(".md") && f.toLowerCase() !== "readme.md")
    .map((f) => {
      const text = fs.readFileSync(path.join(CONTENT_DIR, f), "utf8");
      const title = (text.match(/^#\s+(.+)$/m) || [])[1] || f.replace(/\.md$/, "");
      return { slug: f.replace(/\.md$/, ""), title };
    });
}

function loadUnits() {
  if (!fs.existsSync(GENERATED_DIR)) return [];
  const units = [];
  for (const f of fs.readdirSync(GENERATED_DIR)) {
    if (!f.endsWith(".api_reference_units.json")) continue;
    try {
      const data = JSON.parse(fs.readFileSync(path.join(GENERATED_DIR, f), "utf8"));
      const list = Array.isArray(data) ? data : data.units || data.items || [];
      for (const u of list) units.push({ source_file: f, ...u });
    } catch {
      /* unreadable file: skip, never guess */
    }
  }
  return units;
}

function unitToText(u) {
  const lines = [
    `operation: ${u.operation_id || u.unit_id}`,
    `endpoint: ${u.http_method || ""} ${u.endpoint || ""}`.trim(),
    `summary: ${u.summary || ""}`,
    `auth: ${(u.auth_requirements || []).join(", ") || "not stated"}`,
  ];
  for (const e of u.error_cases || []) {
    lines.push(`error ${e.code}: ${e.meaning}. recovery: ${e.recovery}`);
  }
  for (const q of u.evidence_quotes || []) lines.push(`evidence: "${q}"`);
  lines.push(`provenance: ${u.lineage_origin || "unknown"} (${u.source_file})`);
  return lines.join("\n");
}

function score(text, terms) {
  const hay = text.toLowerCase();
  let s = 0;
  for (const t of terms) {
    if (!t) continue;
    let i = -1;
    while ((i = hay.indexOf(t, i + 1)) !== -1) s += 1;
  }
  return s;
}

const server = new McpServer({ name: "content-docs", version: "0.1.0" });

server.tool(
  "list_pages",
  "List every published docs page and every spec-generated reference unit.",
  {},
  async () => {
    const pages = listPages();
    const units = loadUnits().map((u) => ({
      operation: u.operation_id,
      endpoint: `${u.http_method || ""} ${u.endpoint || ""}`.trim(),
      summary: u.summary,
    }));
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({ published_pages: pages, reference_units: units }, null, 2),
        },
      ],
    };
  }
);

server.tool(
  "get_page",
  "Get the full markdown of one published page by slug, or one reference unit by operation id.",
  { id: z.string().describe("page slug from content/, or an operation id like createPayment") },
  async ({ id }) => {
    const file = path.join(CONTENT_DIR, `${id}.md`);
    if (fs.existsSync(file) && path.dirname(path.resolve(file)) === path.resolve(CONTENT_DIR)) {
      return { content: [{ type: "text", text: fs.readFileSync(file, "utf8") }] };
    }
    const unit = loadUnits().find(
      (u) => u.operation_id === id || u.unit_id === id
    );
    if (unit) return { content: [{ type: "text", text: unitToText(unit) }] };
    return {
      content: [
        {
          type: "text",
          text: `NOT FOUND: no published page or reference unit named "${id}". Do not answer from memory; tell the user this is a documentation gap.`,
        },
      ],
    };
  }
);

server.tool(
  "search_docs",
  "Search published pages and reference units. Returns ranked snippets with their source. Empty results mean the docs do not cover it.",
  { query: z.string() },
  async ({ query }) => {
    const terms = query.toLowerCase().split(/\s+/).filter((t) => t.length > 2);
    const results = [];
    for (const p of listPages()) {
      const text = fs.readFileSync(path.join(CONTENT_DIR, `${p.slug}.md`), "utf8");
      const s = score(p.title + " " + text, terms);
      if (s > 0) results.push({ source: `content/${p.slug}.md`, score: s, snippet: text.slice(0, 400) });
    }
    for (const u of loadUnits()) {
      const text = unitToText(u);
      const s = score(text, terms);
      if (s > 0) results.push({ source: `reference_unit:${u.operation_id}`, score: s, snippet: text });
    }
    results.sort((a, b) => b.score - a.score);
    const top = results.slice(0, 5);
    return {
      content: [
        {
          type: "text",
          text: top.length
            ? JSON.stringify(top, null, 2)
            : "NO RESULTS. The published docs do not cover this. Say so plainly and log it as a gap; do not answer from prior knowledge.",
        },
      ],
    };
  }
);

server.tool(
  "log_manual_test",
  "Record the outcome of a hand test so it feeds the improvement loop. Call this after answering.",
  {
    question: z.string(),
    verdict: z.enum(["answered_from_docs", "partial", "gap"]),
    sources_used: z.array(z.string()),
    notes: z.string().optional(),
  },
  async ({ question, verdict, sources_used, notes }) => {
    fs.mkdirSync(path.dirname(EVAL_LOG), { recursive: true });
    const entry = {
      ts: new Date().toISOString(),
      kind: "manual",
      question,
      verdict,
      sources_used,
      notes: notes || "",
    };
    fs.appendFileSync(EVAL_LOG, JSON.stringify(entry) + "\n");
    return { content: [{ type: "text", text: `logged to evals/manual-runs.jsonl` }] };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
