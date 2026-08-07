# Authentication — Success Criteria

## What Success Looks Like

The agent successfully authenticates with Payment Gateway and makes at least one valid API call.

## Pass Conditions

- [ ] **PASS**: Agent makes an API call that returns a 200-level HTTP response
- [ ] **PASS**: Agent does not throw authentication errors (401/403)
- [ ] **PASS**: Agent does not throw credential format errors (400 with "missing" or "invalid" in message)

## Fail Conditions

- [ ] **FAIL**: Agent cannot find authentication documentation
- [ ] **FAIL**: Agent uses wrong credential field names (`keyId`/`secretKey` instead of `merchantKeyId`/`merchantsecretKey`)
- [ ] **FAIL**: Agent uses an expired card expiry year
- [ ] **FAIL**: Agent points to the wrong API endpoint (live instead of sandbox)
- [ ] **FAIL**: Agent never makes an API call (gives up)

## Metrics to Record

| Metric | What it measures |
|--------|------------------|
| `agent_success_rate` | Did the agent succeed? (pass/fail) |
| `docs_lookup_count` | How many documentation pages did the agent read? |
| `error_count` | How many API errors did the agent hit before succeeding? |
| `error_types` | What kind of errors? (auth, network, format, etc.) |
| `time_to_first_success` | How long did it take the agent to succeed? |

## Scorecard Schema

```json
{
  "scenario": "authentication",
  "profile": "docs",
  "agent": "claude-sonnet-4",
  "timestamp": "2026-07-21T16:00:00Z",
  "result": {
    "pass": true,
    "docs_read": ["developer.example.com/docs/auth", "developer.example.com/docs/credentials"],
    "errors": [],
    "error_count": 0,
    "first_api_call_status": 200,
    "response_time_seconds": 45
  }
}
```

## Notes

- The agent should NOT be given the correct field names — they need to find them in the docs or discover them through trial/error
- The Payment Gateway lab already has a known bug: docs claim `keyId`/`secretKey` but SDK expects `merchantKeyId`/`merchantsecretKey`. This scenario tests whether agents can discover the right field names.
- If the agent fails, record which error was encountered and which docs the agent read before failing
