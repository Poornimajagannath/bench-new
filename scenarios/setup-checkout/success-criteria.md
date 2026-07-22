# Setup Checkout — Success Criteria

## What Success Looks Like

The agent successfully configures a checkout and makes a test transaction that returns a transaction ID.

## Pass Conditions

- [ ] **PASS**: Agent configures a checkout (Unified Checkout or Flex Microcheckout)
- [ ] **PASS**: Agent makes a test transaction that returns a transaction ID
- [ ] **PASS**: Transaction ID is a valid CyberSource format (not an error)
- [ ] **PASS**: Agent does not throw checkout configuration errors (400/422)

## Fail Conditions

- [ ] **FAIL**: Agent cannot find checkout documentation
- [ ] **FAIL**: Agent uses wrong checkout parameters
- [ ] **FAIL**: Agent never makes a test transaction
- [ ] **FAIL**: Agent gets an error response without a transaction ID
- [ ] **FAIL**: Agent gives up before configuring checkout

## Metrics to Record

| Metric | What it measures |
|--------|------------------|
| `agent_success_rate` | Did the agent succeed? (pass/fail) |
| `docs_lookup_count` | How many documentation pages did the agent read? |
| `error_count` | How many API errors did the agent hit before succeeding? |
| `checkout_type` | Which checkout method was chosen? (Unified or Flex) |
| `time_to_first_success` | How long did it take the agent to succeed? |

## Scorecard Schema

```json
{
  "scenario": "setup-checkout",
  "profile": "docs",
  "agent": "claude-sonnet-4",
  "timestamp": "2026-07-21T16:00:00Z",
  "result": {
    "pass": true,
    "checkout_type": "Unified Checkout",
    "docs_read": ["developer.cybersource.com/docs/checkout", "developer.cybersource.com/docs/unified-checkout"],
    "errors": [],
    "error_count": 0,
    "transaction_id": "TXN_1234567890",
    "response_time_seconds": 90
  }
}
```

## Notes

- The agent should be able to configure checkout from docs alone (no MCP or code generation required)
- Both Unified Checkout and Flex Microcheckout are valid — agent can choose either
- If the agent fails, record which error was encountered and which docs the agent read before failing
