# Autonomous Integration Lab — Claude Code Operating Manual

You are running inside the Autonomous Integration Lab for Cybersource. Read this file first on every session.

## Purpose

This lab measures whether an AI coding agent can complete a Cybersource sandbox integration from near-zero context, using the same artifacts a real developer would use: public docs, official SDKs, sandbox credentials, and local context files. Every run produces a replayable artifact set: generated app, logs, findings report, scorecard JSON, and manifest.

## Lab rules (non-negotiable)

1. **Sandbox only.** Never use production Cybersource endpoints or credentials.
2. **No hardcoded secrets.** Load all credentials from environment variables only.
3. **Never print secrets.** Redact any credential values from logs and output.
4. **Do not fake success.** If a sandbox call fails, record the failure accurately.
5. **If blocked, say so precisely.** State the exact blocker in findings.md rather than guessing past it silently.
6. **Record everything.** Every API call, its HTTP status, and its Cybersource reason code must appear in logs/run.log.

## Required env vars

```
CYBS_MERCHANT_ID      — your sandbox merchant ID from developer.cybersource.com
CYBS_KEY_ID           — HTTP Signature key ID (from Business Center > Payment Configuration > Key Management)
CYBS_SHARED_SECRET    — shared secret paired with CYBS_KEY_ID
CYBS_ENVIRONMENT      — must be "sandbox"
CYBS_RUN_ID           — set by run-scenario.sh; identifies the run folder
CYBS_SCENARIO         — set by run-scenario.sh; identifies the scenario
CYBS_LANGUAGE         — set by run-scenario.sh; default "node"
ANTHROPIC_API_KEY     — for Claude Code execution
```

## Reading order for every run

1. `context/auth.md` — credential loading and auth error taxonomy
2. `context/source-index.md` — authoritative doc and SDK links
3. `context/sandbox-rules.md` — test cards, constraints, and what sandbox simulates
4. `scenarios/<SCENARIO>/task.md` — what to build
5. `scenarios/<SCENARIO>/success-criteria.md` — what constitutes a pass
6. `evaluators/scorecard-rubric.md` — how your run will be scored

## Output contract

Every run must emit these files inside `runs/$CYBS_RUN_ID/`:

| File | Required | Description |
|---|---|---|
| `app/` | Yes | Generated integration code |
| `logs/run.log` | Yes | Timestamped structured log |
| `findings.md` | Yes | Human-readable analysis using findings-template.md |
| `scorecard.json` | Yes | Machine-readable scores matching scorecard.schema.json |
| `manifest.json` | Yes | Reproducibility data |
| `transcript.ndjson` | Recommended | Raw Claude Code stream-json output |
| `source-manifest.md` | Recommended | Exact docs and SDK versions consulted |

## Hook policies

The `.claude/settings.json` file enforces these at runtime:

- **SessionStart**: validate required env vars; write run metadata banner to logs/run.log
- **PreToolUse**: deny any command targeting production endpoints, deny writes outside `runs/$CYBS_RUN_ID/` and `app/`
- **PostToolUse**: append tool call metadata to transcript
- **SessionEnd**: verify `findings.md`, `manifest.json`, and `scorecard.json` exist; warn if missing

## Skill

Use `/run-lab` (defined in `.claude/skills/run-lab/SKILL.md`) to execute a full scenario run interactively.

## CLI invocations

```bash
# Interactive supervised run
claude --permission-mode plan

# Non-interactive scenario run (CI/nightly)
claude -p \
  --append-system-prompt-file prompts/v0-runner.md \
  --output-format stream-json \
  --verbose \
  --include-hook-events \
  "Run scenario $CYBS_SCENARIO in runs/${CYBS_RUN_ID}"

# Evaluator run
claude -p \
  --append-system-prompt-file prompts/evaluator.md \
  --output-format json \
  --json-schema "$(cat evaluators/scorecard.schema.json)" \
  "Evaluate run ${CYBS_RUN_ID}"

# Full loop (multiple iterations, retry, CI gate)
scripts/lab-loop.sh -s first-payment-node -n 3 -r 1 -t 3
```
