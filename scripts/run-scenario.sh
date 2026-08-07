#!/usr/bin/env bash
# run-scenario.sh — run one Content Bench benchmark scenario.
#
# Usage:
#     scripts/run-scenario.sh SCENARIO [RUN_MODE]
#
# Arguments:
#     SCENARIO   scenario directory name (authentication, setup-checkout, first-transaction)
#     RUN_MODE   "dry" or "live" (default: "dry")
#
# Environment:
#     PGW_MERCHANT_ID, PGW_KEY_ID, PGW_SHARED_SECRET — required for live runs
#     LAB_DRY_RUN=1 — simulate run without calling Hermes Agent
#
# Outputs:
#     Logs to stderr; echoes the run_id as the last line of stdout.

set -euo pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_env

SCENARIO="${1:-authentication}"
RUN_MODE="${2:-dry}"

# Validate scenario directory exists
[ -d "${LAB_ROOT}/scenarios/${SCENARIO}" ] || die "Unknown scenario: ${SCENARIO}"

# Generate run ID
export PGW_RUN_ID
PGW_RUN_ID="$(next_run_id "$SCENARIO")"
export PGW_SCENARIO="$SCENARIO"

RUN_DIR="${LAB_ROOT}/runs/${PGW_RUN_ID}"

log "Starting run: run_id=${PGW_RUN_ID} scenario=${SCENARIO} mode=${RUN_MODE}"

# Create run directory structure
mkdir -p "${RUN_DIR}/app" "${RUN_DIR}/logs"

# Write initial log banner
cat >> "${RUN_DIR}/logs/run.log" <<LOG
[$(ts)] run_id=${PGW_RUN_ID}
[$(ts)] scenario=${SCENARIO} mode=${RUN_MODE} agent=hermes-spark
[$(ts)] env_check=checking vars=[PGW_MERCHANT_ID,PGW_KEY_ID,PGW_SHARED_SECRET,PGW_ENVIRONMENT]
LOG

if [ "$RUN_MODE" = "dry" ] || [ "${LAB_DRY_RUN:-0}" = "1" ]; then
  log "DRY RUN: simulating Hermes Agent execution"
  sleep 1

  # Write placeholder artifacts
  cat > "${RUN_DIR}/findings.md" <<MD
# Content Benchmark — Findings

## Run metadata
- run_id: ${PGW_RUN_ID}
- scenario: ${SCENARIO}
- mode: dry-run
- date_utc: $(ts)
- final_outcome: dry-run

## What worked
Dry run — no real execution.

## What failed
N/A (dry run)

## Auth friction
N/A

## SDK friction
N/A

## Documentation friction
N/A

## Sandbox or test-data friction
N/A

## Agent guesses
N/A

## Recommended fixes
N/A

## Evidence
- key log lines: dry-run mode
- commands run: none
- files created: findings.md, scorecard.json, manifest.json
MD

  cat > "${RUN_DIR}/scorecard.json" <<JSON
{
  "run_id": "${PGW_RUN_ID}",
  "scenario": "${SCENARIO}",
  "agent": "hermes-spark",
  "sdk_language": "node",
  "status": "failed",
  "confidence": "high",
  "scores": {
    "integration_success": 0,
    "auth_clarity": 0,
    "sdk_usability": 0,
    "docs_sufficiency": 0,
    "agent_guessing": 3,
    "human_intervention": 3
  },
  "timings": {
    "time_to_first_api_response_ms": 0,
    "time_to_first_success_ms": null,
    "total_run_time_ms": 1000
  },
  "friction": {
    "human_interventions": 0,
    "docs_pages_consulted": 0,
    "agent_guess_count": 0,
    "auth_failure_count": 0,
    "sdk_failure_count": 0
  },
  "reproducibility": {
    "replayable": true,
    "pinned_versions": false,
    "manifest_complete": true
  },
  "issues": [],
  "notes": "Dry run — no real execution."
}
JSON

  cat > "${RUN_DIR}/manifest.json" <<JSON
{
  "run_id": "${PGW_RUN_ID}",
  "scenario": "${SCENARIO}",
  "started_at_utc": "$(ts)",
  "finished_at_utc": "$(ts)",
  "repo_commit_sha": "$(cd "${LAB_ROOT}" && git rev-parse HEAD 2>/dev/null || echo 'unknown')",
  "worktree_path": "${RUN_DIR}",
  "agent_invocation": "dry-run",
  "sdk_language": "node",
  "sdk_version": "unknown",
  "lockfile_present": false,
  "env_var_names_used": ["PGW_MERCHANT_ID","PGW_KEY_ID","PGW_SHARED_SECRET","PGW_ENVIRONMENT"],
  "files_read": [],
  "commands_run": [],
  "exit_codes": [],
  "sources_consulted": []
}
JSON

  echo "[$(ts)] dry_run=complete" >> "${RUN_DIR}/logs/run.log"
  log "Dry run complete: run_id=${PGW_RUN_ID}"

else
  # Live execution using Hermes Agent
  if ! command -v hermes >/dev/null 2>&1; then
    die "hermes CLI not found. Install it with: pip install --upgrade hermes-agent"
  fi

  # Read scenario files
  TASK_FILE="${LAB_ROOT}/scenarios/${SCENARIO}/task.md"
  INPUTS_FILE="${LAB_ROOT}/scenarios/${SCENARIO}/inputs.md"
  SUCCESS_FILE="${LAB_ROOT}/scenarios/${SCENARIO}/success-criteria.md"
  CONTEXT_DIR="${LAB_ROOT}/context"

  for context_file in auth.md sandbox-rules.md source-index.md; do
    if [ ! -f "${CONTEXT_DIR}/${context_file}" ]; then
      die "Context file not found: ${CONTEXT_DIR}/${context_file}"
    fi
  done

  if [ ! -f "$TASK_FILE" ]; then
    die "Task file not found: ${TASK_FILE}"
  fi

  log "Running Hermes Agent for scenario ${SCENARIO}"

  # Build the agent prompt with scenario context
  cat > "${RUN_DIR}/agent-prompt.md" <<PROMPT
You are running inside the Content Benchmark lab for Payment Gateway.

## Your Task
Run scenario '${SCENARIO}' in runs/${PGW_RUN_ID}.

## Read These Files in Order
1. ${TASK_FILE} — what to build
2. ${INPUTS_FILE} — required inputs
3. ${SUCCESS_FILE} — what constitutes a pass
4. ${CONTEXT_DIR}/auth.md — credential loading and auth error taxonomy
5. ${CONTEXT_DIR}/source-index.md — authoritative doc and SDK links
6. ${CONTEXT_DIR}/sandbox-rules.md — test cards, constraints, sandbox behavior

## Output Contract
Create these files inside runs/${PGW_RUN_ID}/:
- app/ — Generated integration code (if successful)
- findings.md — Human-readable analysis
- logs/run.log — Timestamped structured log (continue appending)

Follow the task exactly. If you succeed, create runs/${PGW_RUN_ID}/app/README.md describing what you built. If you fail, explain why in findings.md.

## Sandbox Rules
- Use test card: 4111111111111111, expiry 12/2031, CVV 123
- Sandbox endpoint: https://apitest.example.com
- Load credentials from env vars only: PGW_MERCHANT_ID, PGW_KEY_ID, PGW_SHARED_SECRET
- Never print or hardcode secrets

## SDK Field Names (Known Gap)
Use merchantKeyId and merchantsecretKey (NOT keyId and secretKey)

Agent Prompt:
PROMPT

  log "Agent prompt written to ${RUN_DIR}/agent-prompt.md"

  # Run Hermes Agent in non-interactive mode
  cd "${LAB_ROOT}"
  HERMES_PROMPT=$(cat "${RUN_DIR}/agent-prompt.md")
  hermes chat -q "${HERMES_PROMPT}" -Q 2>>"${RUN_DIR}/logs/run.log" > "${RUN_DIR}/hermes-output.txt" || HERMES_EXIT=$? || HERMES_EXIT=$?
  HERMES_EXIT=${HERMES_EXIT:-0}
  log "Hermes Agent exit code: ${HERMES_EXIT}"

  # Validate output
  if [ ${HERMES_EXIT} -ne 0 ]; then
    log "WARNING: Hermes Agent exited with code ${HERMES_EXIT}"
  fi

  if [ -f "${RUN_DIR}/findings.md" ] && [ -f "${RUN_DIR}/logs/run.log" ]; then
    log "Run artifacts validated: findings.md and run.log exist"
  else
    log "WARNING: Missing expected artifacts"
  fi

  echo "[$(ts)] live_run=complete" >> "${RUN_DIR}/logs/run.log"
  log "Live run complete: run_id=${PGW_RUN_ID}"
fi

# Echo run ID as last line (consumed by lab-loop.sh)
echo "${PGW_RUN_ID}"
