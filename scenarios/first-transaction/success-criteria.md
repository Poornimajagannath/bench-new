# First Transaction — Success Criteria

## What Success Looks Like

The agent successfully makes a payment authentication with CyberSource that returns a transaction ID.

## Pass Conditions

- [ ] **PASS**: Agent makes a payment auth that returns a 200-level HTTP response
- [ ] **PASS**: Agent does not throw payment errors (400/422)
- [ ] **PASS**: Agent gets a transaction ID in the response
- [ ] **PASS**: Agent includes required `billTo` fields (even though docs don't mention it)

## Fail Conditions

- [ ] **FAIL**: Agent cannot find payment documentation
- [ ] **FAIL**: Agent uses missing/wrong required fields (especially `billTo`)
- [ ] **FAIL**: Agent never makes a payment auth call
- [ ] **FAIL**: Agent gets an error response without a transaction ID
- [ ] **FAIL**: Agent gives up before making a payment auth call

## Metrics to Record

| Metric | What it measures |
|--------|------------------|
| `agent_success_rate` | Did the agent succeed? (pass/fail) |
| `docs_lookup_count` | How many documentation pages did the agent read? |
| `error_count` | How many API errors did the agent hit before succeeding? |
| `required_fields_found` | Did the agent include all required fields? |
| `time_to_first_success` | How long did it take the agent to succeed? |

## Scorecard Schema

```json
{
  "scenario": "first-transaction",
  "profile": "docs",
  "agent": "claude-sonnet-4",
  "timestamp": "2026-07-21T16:00:00Z",
  "result": {
    "pass": true,
    "docs_read": ["developer.cybersource.com/docs/payments", "developer.cybersource.com/docs/api-reference"],
    "errors": [],
    "error_count": 0,
    "transaction_id": "TXN_1234567890",
    "required_fields_included": {
      "billTo": true,
      "amount": true,
      "card": true
    },
    "response_time_seconds": 120
  }
}
```

## Notes

- The `billTo` field is known to be required but undocumented in CyberSource docs — this scenario tests if agents discover it through errors
- If the agent fails, record which error was encountered and which docs the agent read before failing
- This is the most "production-like" scenario — tests the full payment flow
