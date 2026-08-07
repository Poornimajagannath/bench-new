You are running an Autonomous Integration Lab scenario for Payment Gateway.

Read these files first, in order:
- context/auth.md
- context/source-index.md
- context/sandbox-rules.md
- context/sdk-map.md
- context/llms-notes.md
- scenarios/${PGW_SCENARIO}/task.md
- scenarios/${PGW_SCENARIO}/success-criteria.md
- scenarios/${PGW_SCENARIO}/inputs.md
- evaluators/scorecard-rubric.md

Your job is to build the scenario inside `runs/${PGW_RUN_ID}/`.

Requirements:
- Use Node.js (or TypeScript if the scenario specifies it).
- Use the official Payment Gateway SDK or Acceptance Agent Toolkit as specified in the scenario.
- Use sandbox only (`apitest.example.com`).
- Load credentials from environment variables only:
  - PGW_MERCHANT_ID
  - PGW_KEY_ID
  - PGW_SHARED_SECRET
  - PGW_ENVIRONMENT
- Never hardcode secrets.
- Never use production endpoints or credentials.
- Do not fake or mock success — only record a successful outcome after a real Payment Gateway sandbox response.
- If you are blocked, state exactly why in findings.md and stop.

Deliverables (all inside `runs/${PGW_RUN_ID}/`):
- `app/` — runnable integration code
- `logs/run.log` — timestamped log of all steps, API calls, HTTP statuses, and Payment Gateway reason codes
- `findings.md` — analysis using `evaluators/findings-template.md`
- `manifest.json` — reproducibility data (see CLAUDE.md output contract)
- `scorecard.json` — rubric scores matching `evaluators/scorecard.schema.json`

For findings.md, document:
- What worked (step by step)
- What failed (exact error, HTTP status, reason code)
- Auth friction (category from context/auth.md)
- SDK friction (specific method or parameter issues)
- Documentation friction (URL, what was missing)
- Sandbox or test-data friction
- Agent guesses (each undocumented decision)
- Recommended DevEx fixes (backlog-ready, with bucket and severity from dx-issue-taxonomy.md)

For manifest.json, include:
- run_id, scenario, started_at_utc, finished_at_utc
- repo_commit_sha (run `git rev-parse HEAD`)
- worktree_path (current directory)
- claude_invocation (the command that started this session)
- sdk_language, sdk_version
- lockfile_present (boolean)
- env_var_names_used (list of names, never values)
- files_read (all context and scenario files consulted)
- commands_run (all shell commands executed)
- exit_codes (exit code of each command)
- sources_consulted (URLs of official docs consulted)

For scorecard.json, follow evaluators/scorecard.schema.json exactly. Do not soften findings. Do not infer success without evidence.
