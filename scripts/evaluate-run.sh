#!/usr/bin/env bash
# evaluate-run.sh — run the evaluator against a completed run folder.
#
# Usage:
#     scripts/evaluate-run.sh RUN_ID
#
# The evaluator reads the run's manifest, findings, and logs, then writes
# or overwrites scorecard.json in the run folder.
set -euo pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

RUN_ID="${1:-}"
[ -z "$RUN_ID" ] && die "Usage: evaluate-run.sh RUN_ID"

RUN_DIR="${LAB_ROOT}/runs/${RUN_ID}"
[ -d "$RUN_DIR" ] || die "Run directory not found: ${RUN_DIR}"

log "Evaluating run: ${RUN_ID}"

if is_dry_run; then
  log "DRY RUN: skipping evaluator Claude Code call"
  exit 0
fi

if ! command -v claude >/dev/null 2>&1; then
  die "claude CLI not found. Install it with: npm install -g @anthropic-ai/claude-code"
fi

# Build the evaluator prompt with the actual RUN_ID substituted
EVALUATOR_PROMPT="$(sed "s/{{RUN_ID}}/${RUN_ID}/g" "${LAB_ROOT}/prompts/evaluator.md")"

# Run the evaluator in JSON output mode, writing to scorecard.json
claude -p \
  --output-format json \
  --json-schema "$(cat "${LAB_ROOT}/evaluators/scorecard.schema.json")" \
  "$EVALUATOR_PROMPT" \
  > "${RUN_DIR}/scorecard.json.tmp" 2>/dev/null \
  && mv "${RUN_DIR}/scorecard.json.tmp" "${RUN_DIR}/scorecard.json" \
  || { log "Evaluator failed or schema validation error — check scorecard.json.tmp"; exit 1; }

log "Evaluation complete: scorecard written to ${RUN_DIR}/scorecard.json"
