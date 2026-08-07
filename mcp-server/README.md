# content-docs MCP server

A doc agent you can attach to Cursor, Codex, or Claude Code. It answers questions using only the generated docs (`content/` pages and spec-generated reference units), cites sources, refuses to guess, and logs every hand test to `evals/manual-runs.jsonl` so manual testing feeds the improvement loop.

## Setup

One time: `cd mcp-server && npm install`

### Cursor

Create `.cursor/mcp.json` in the repo root:

```json
{
  "mcpServers": {
    "content-docs": {
      "command": "node",
      "args": ["mcp-server/index.js"]
    }
  }
}
```

Then paste `agents/doc-agent.md` into a Cursor custom mode (or rules) so the agent follows the docs-only contract.

### Codex CLI

Add to `~/.codex/config.toml`:

```toml
[mcp_servers.content-docs]
command = "node"
args = ["/absolute/path/to/repo/mcp-server/index.js"]
```

### Claude Code

`claude mcp add content-docs -- node mcp-server/index.js`

## How to hand test

Ask the agent a real developer question, e.g. "how do I create a Connect account in sandbox?" A good agent answer cites a `content/connect-*.md` page (or a reference unit) and names the auth scheme from the docs. Then ask something the docs do not cover yet, e.g. "how do refunds work?" The right behavior is "the docs do not cover this," logged with verdict `gap`. Check `evals/manual-runs.jsonl` afterward; every question you ask becomes evidence for the nightly loop.


## Multi-client install (Spark + Mac)

On **DGX Spark** (already done for this machine): Hermes (`HERMES_HOME` config), Claude Code (`claude mcp add -s user`), Codex (`codex mcp add`), and Cursor (`~/.cursor/mcp.json`) all point at the local stdio server.

On **Mac**, run the SSH installer (docs stay on Spark):

```bash
scp ourspark:/home/badari/workspace/poornima/content-bench/scripts/install-content-docs-mcp-mac.sh /tmp/
bash /tmp/install-content-docs-mcp-mac.sh
```

Override the SSH host if needed: `SPARK_HOST=your-host bash /tmp/install-content-docs-mcp-mac.sh`.
