#!/usr/bin/env bash
# lib.sh — shared helpers for the Autonomous Integration Lab scripts.
# Source this file at the top of each script: . "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

LAB_ROOT="${LAB_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

load_env() {
  local envfile="${LAB_ROOT}/.env"
  if [ -f "$envfile" ]; then
    # shellcheck disable=SC1090
    set -a; source "$envfile"; set +a
  fi
  # Validate required vars
  local missing=()
  for var in PGW_MERCHANT_ID PGW_KEY_ID PGW_SHARED_SECRET; do
    [ -z "${!var:-}" ] && missing+=("$var")
  done
  if [ "${#missing[@]}" -gt 0 ] && ! is_dry_run; then
    die "Missing required environment variables: ${missing[*]}"
  fi
  export PGW_ENVIRONMENT="${PGW_ENVIRONMENT:-sandbox}"
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

ts() {
  date -u +%Y-%m-%dT%H:%M:%SZ
}

log() {
  echo "[$(ts)] $*" >&2
}

die() {
  echo "[$(ts)] FATAL: $*" >&2
  exit 1
}

# ---------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------

is_dry_run() {
  [ "${LAB_DRY_RUN:-0}" = "1" ]
}

# ---------------------------------------------------------------------------
# JSON helpers
# ---------------------------------------------------------------------------

# json_get FILE KEY — extract a scalar value from a JSON file using python3 or jq.
# KEY supports dot-notation: scores.integration_success
json_get() {
  local file="$1" key="$2"
  if command -v jq >/dev/null 2>&1; then
    jq -r ".${key} // empty" "$file" 2>/dev/null
  else
    python3 -c "
import json, sys
data = json.load(open('$file'))
keys = '$key'.split('.')
val = data
for k in keys:
    val = val.get(k, '') if isinstance(val, dict) else ''
print(val if val is not None else '')
" 2>/dev/null
  fi
}

# ---------------------------------------------------------------------------
# Run ID generation
# ---------------------------------------------------------------------------

# next_run_id SCENARIO — generate the next available run ID for a scenario.
next_run_id() {
  local scenario="$1"
  local date_str
  date_str="$(date -u +%Y-%m-%d)"
  local prefix="${date_str}-${scenario}"
  local existing
  existing="$(ls -d "${LAB_ROOT}/runs/${prefix}"-* 2>/dev/null | wc -l | tr -d ' ')"
  local idx
  idx="$(printf '%03d' "$((existing + 1))")"
  echo "${prefix}-${idx}"
}
