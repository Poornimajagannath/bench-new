#!/usr/bin/env bash
# ============================================================================
# lab-loop.sh — the Autonomous Integration Lab operating loop.
#
# For each scenario, for each iteration: run -> evaluate -> score -> collect,
# retrying on failure up to a limit, and gate on a scorecard threshold. Writes
# a loop summary (CSV + JSON) and exits non-zero if any iteration failed the
# gate (so it can drive CI / nightly runs).
#
# Usage:
#     scripts/lab-loop.sh [options]
#
# Options:
#     -s SCENARIO    scenario to run (repeatable). Default: first-payment-node
#     -n N           iterations per scenario             (default: 1)
#     -r N           max retries per iteration on fail   (default: 3)
#     -t SCORE       min integration_success to pass     (default: 3, range 0-3)
#     -a AGENT       agent label                         (default: claude-code-cli)
#     -h             show this help
#
# Examples:
#     scripts/lab-loop.sh                                    # 1x golden path, 3 retries
#     scripts/lab-loop.sh -s first-payment-node -n 5 -r 5   # 5 attempts, 5 retries
#     scripts/lab-loop.sh -s tokenization-node -s webhooks-node -t 2
#     LAB_DRY_RUN=1 scripts/lab-loop.sh -n 3                # exercise plumbing only
# ============================================================================
set -euo pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_env

ITERATIONS=1
RETRIES=3
THRESHOLD=3
AGENT="claude-code-cli"
SCENARIOS=()

usage() {
  sed -n '2,/^# ===/p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

while getopts ":s:n:r:t:a:h" opt; do
  case "$opt" in
    s) SCENARIOS+=("$OPTARG") ;;
    n) ITERATIONS="$OPTARG" ;;
    r) RETRIES="$OPTARG" ;;
    t) THRESHOLD="$OPTARG" ;;
    a) AGENT="$OPTARG" ;;
    h) usage 0 ;;
    \?) die "unknown option -$OPTARG (try -h)" ;;
    :) die "option -$OPTARG needs a value" ;;
  esac
done

[ "${#SCENARIOS[@]}" -eq 0 ] && SCENARIOS=("first-payment-node")

if is_dry_run; then
  log "MODE: dry-run (simulated agent; set ANTHROPIC_API_KEY + install claude for live runs)"
else
  log "MODE: live (Claude Code)"
fi

log "scenarios=[${SCENARIOS[*]}] iterations=${ITERATIONS} retries=${RETRIES} threshold=${THRESHOLD}"

SUMMARY_TS="$(date -u +%Y%m%d-%H%M%S)"
CSV="${LAB_ROOT}/runs/loop-summary-${SUMMARY_TS}.csv"
JSON="${LAB_ROOT}/runs/loop-summary-${SUMMARY_TS}.json"
echo "scenario,iteration,attempt,run_id,status,integration_success,gate" > "$CSV"

ROWS_JSON="["
total=0; passed=0; first_row=1

run_once() {
  # scenario -> echoes run_id (last line of run-scenario.sh stdout)
  bash "${LAB_ROOT}/scripts/run-scenario.sh" "$1" "$AGENT" | tail -n 1
}

for scenario in "${SCENARIOS[@]}"; do
  [ -d "${LAB_ROOT}/scenarios/$scenario" ] || die "unknown scenario: $scenario"

  for i in $(seq 1 "$ITERATIONS"); do
    attempt=0; gate="fail"; run_id=""; status=""; isc=""

    while :; do
      log "=== scenario=${scenario} iteration=${i} attempt=${attempt} ==="
      run_id="$(run_once "$scenario")"

      bash "${LAB_ROOT}/scripts/evaluate-run.sh" "$run_id" >/dev/null 2>&1 \
        || log "WARN: evaluate-run.sh returned non-zero (continuing)"
      bash "${LAB_ROOT}/scripts/collect-artifacts.sh" "$run_id" >/dev/null 2>&1 || true

      status="$(json_get "${LAB_ROOT}/runs/${run_id}/scorecard.json" status)"
      isc="$(json_get "${LAB_ROOT}/runs/${run_id}/scorecard.json" scores.integration_success)"
      isc="${isc:-0}"

      if [ "$isc" -ge "$THRESHOLD" ] 2>/dev/null; then
        gate="pass"
      else
        gate="fail"
      fi

      log "result: run=${run_id} status=${status} integration_success=${isc} gate=${gate}"

      [ "$gate" = "pass" ] && break
      [ "$attempt" -ge "$RETRIES" ] && break
      attempt=$((attempt + 1))
      log "retrying (${attempt}/${RETRIES})..."
    done

    total=$((total + 1))
    [ "$gate" = "pass" ] && passed=$((passed + 1))

    echo "${scenario},${i},${attempt},${run_id},${status},${isc},${gate}" >> "$CSV"

    [ $first_row -eq 0 ] && ROWS_JSON+=","
    first_row=0
    ROWS_JSON+="{\"scenario\":\"${scenario}\",\"iteration\":${i},\"attempts\":${attempt},\"run_id\":\"${run_id}\",\"status\":\"${status}\",\"integration_success\":${isc},\"gate\":\"${gate}\"}"
  done
done
ROWS_JSON+="]"

rate=$(python3 -c "print(f'{($passed/$total*100) if $total else 0:.1f}')" 2>/dev/null || echo "0.0")

cat > "$JSON" <<JSON
{
  "generated_at_utc": "$(ts)",
  "mode": "$(is_dry_run && echo dry-run || echo live)",
  "threshold_integration_success": ${THRESHOLD},
  "total": ${total},
  "passed": ${passed},
  "pass_rate_pct": ${rate},
  "results": ${ROWS_JSON}
}
JSON

echo
echo "================ LAB LOOP SUMMARY ================"
column -t -s, "$CSV" 2>/dev/null || cat "$CSV"
echo "-------------------------------------------------"
printf 'passed %d/%d (%.1f%%)   threshold=integration_success>=%s\n' \
  "$passed" "$total" "$rate" "$THRESHOLD"
echo "summary CSV:  $CSV"
echo "summary JSON: $JSON"
echo "================================================="

# CI gate: non-zero unless everything passed.
[ "$passed" -eq "$total" ] && exit 0 || exit 1
