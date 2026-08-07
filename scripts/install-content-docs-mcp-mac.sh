#!/usr/bin/env bash
# Run this ON YOUR MAC to attach content-docs MCP (served from Spark over SSH).
# Prereq: `ssh ourspark` works without a password prompt (or use ssh-agent).
set -euo pipefail

SPARK_HOST="${SPARK_HOST:-ourspark}"
NODE_ON_SPARK="${NODE_ON_SPARK:-/home/badari/.nvm/versions/node/v22.23.1/bin/node}"
SERVER_ON_SPARK="${SERVER_ON_SPARK:-/home/badari/workspace/poornima/content-bench/mcp-server/index.js}"

echo "Using Spark host: $SPARK_HOST"
ssh -o BatchMode=yes -o ConnectTimeout=10 "$SPARK_HOST" "test -f '$SERVER_ON_SPARK'" \
  || { echo "Cannot reach $SPARK_HOST or missing $SERVER_ON_SPARK"; exit 1; }

# --- Cursor (global) ---
CURSOR_MCP="${HOME}/.cursor/mcp.json"
mkdir -p "${HOME}/.cursor"
python3 - <<PY
import json
from pathlib import Path
p = Path("${CURSOR_MCP}")
data = {"mcpServers": {}}
if p.exists():
    data = json.loads(p.read_text())
    data.setdefault("mcpServers", {})
data["mcpServers"]["content-docs"] = {
    "command": "ssh",
    "args": ["${SPARK_HOST}", "${NODE_ON_SPARK}", "${SERVER_ON_SPARK}"],
}
p.write_text(json.dumps(data, indent=2) + "\n")
print(f"Updated {p}")
PY

# --- Claude Code (user scope) ---
if command -v claude >/dev/null 2>&1; then
  claude mcp remove content-docs -s user 2>/dev/null || true
  claude mcp add content-docs -s user -- ssh "$SPARK_HOST" "$NODE_ON_SPARK" "$SERVER_ON_SPARK"
  echo "Claude Code: content-docs added (user scope)"
else
  echo "Claude Code CLI not found; skip (install then re-run)"
fi

# --- Codex ---
if command -v codex >/dev/null 2>&1; then
  codex mcp remove content-docs 2>/dev/null || true
  codex mcp add content-docs -- ssh "$SPARK_HOST" "$NODE_ON_SPARK" "$SERVER_ON_SPARK"
  echo "Codex: content-docs added"
else
  echo "Codex CLI not found; skip (install then re-run)"
fi

# --- Hermes on Mac ---
HERMES_CFG="${HERMES_HOME:-$HOME/.hermes}/config.yaml"
mkdir -p "$(dirname "$HERMES_CFG")"
python3 - <<PY
from pathlib import Path
try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML required: pip install pyyaml")
p = Path("${HERMES_CFG}")
cfg = {}
if p.exists():
    cfg = yaml.safe_load(p.read_text()) or {}
servers = cfg.setdefault("mcp_servers", {})
servers["content-docs"] = {
    "command": "ssh",
    "args": ["${SPARK_HOST}", "${NODE_ON_SPARK}", "${SERVER_ON_SPARK}"],
    "enabled": True,
    "connect_timeout": 45,
}
p.write_text(yaml.safe_dump(cfg, sort_keys=False))
print(f"Updated {p}")
PY

echo
echo "Done. Reload MCP in Cursor / Claude / Codex / Hermes, then ask:"
echo '  how do I create a Connect account in sandbox?'
echo '  how do refunds work?   # expect honest gap'
