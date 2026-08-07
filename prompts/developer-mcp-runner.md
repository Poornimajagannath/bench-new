You are running an Autonomous Integration Lab scenario for Payment Gateway using the **Developer MCP-Assisted Agent Runner**.

You have access to the Payment Gateway Developer MCP (`payment-gateway-developer-mcp`). Before writing any integration code, you MUST query the MCP for:
- SDK documentation for the relevant API class and methods
- Method signatures and required/optional parameters
- Request/response model definitions
- Setup guides for authentication and the relevant feature area
- MLE (Message Level Encryption) guidance if the scenario involves sensitive card data
- Code templates or samples for the target flow

Read these files first, in order:
- context/auth.md
- context/source-index.md
- context/sandbox-rules.md
- context/sdk-map.md
- context/llms-notes.md
- context/developer-mcp-guide.md
- scenarios/${PGW_SCENARIO}/task.md
- scenarios/${PGW_SCENARIO}/success-criteria.md
- scenarios/${PGW_SCENARIO}/inputs.md
- evaluators/scorecard-rubric.md

Your job is to build the scenario inside `runs/${PGW_RUN_ID}/`.

Requirements:
- Use Node.js or TypeScript as specified in the scenario.
- Use the official Payment Gateway SDK or Acceptance Agent Toolkit as specified.
- Use sandbox only (`apitest.example.com`).
- Load credentials from environment variables only:
  - PGW_MERCHANT_ID
  - PGW_KEY_ID
  - PGW_SHARED_SECRET
  - PGW_ENVIRONMENT
- Never hardcode secrets.
- Never use production endpoints or credentials.
- Do not fake or mock success — only record a successful outcome after a real Payment Gateway sandbox response.
- If the MCP is unavailable or returns an error, fall back to official docs and note the gap in findings.md.
- If you are blocked, state exactly why in findings.md and stop.

MCP usage discipline:
- Query the MCP before writing code for each API class you use.
- Record every MCP tool call in the manifest under `mcp_queries`.
- Note whether each MCP response was helpful (filled a gap), redundant (already in docs), confusing (contradicted docs or was unclear), or missing (MCP had no result).
- Score `mcpUsefulness` per the rubric in `evaluators/scorecard-rubric.md` after the run.

Deliverables (all inside `runs/${PGW_RUN_ID}/`):
- `app/` — runnable integration code
- `logs/run.log` — timestamped log of all steps, API calls, HTTP statuses, Payment Gateway reason codes, and MCP queries
- `findings.md` — analysis using `evaluators/findings-template.md`
- `manifest.json` — reproducibility data (see CLAUDE.md output contract), extended with `mcp_queries` array
- `scorecard.json` — rubric scores matching `evaluators/scorecard.schema.json`, including `mcpUsefulness`

For findings.md, document:
- What worked (step by step)
- What failed (exact error, HTTP status, reason code)
- Auth friction (category from context/auth.md)
- SDK friction (specific method or parameter issues)
- Documentation friction (URL, what was missing)
- Sandbox or test-data friction
- Agent guesses (each undocumented decision)
- MCP contribution: where it helped, where it confused, where it had gaps
- Recommended DevEx fixes (backlog-ready, with bucket and severity from dx-issue-taxonomy.md)

For scorecard.json, include `mcpUsefulness` (0–3) alongside the standard six dimensions:
- 3 = MCP was essential — provided information not available in static docs, directly unblocked progress
- 2 = MCP was helpful — supplemented docs, saved time, reduced guessing
- 1 = MCP was marginal — available but didn't add value beyond what docs already covered
- 0 = MCP not used, unavailable, or actively confused the agent
