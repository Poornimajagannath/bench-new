# Relay — Context-Swapping Success Criteria

## What Success Looks Like

The agent successfully generates correct code for a multi-payment method integration that adapts to different merchant contexts (card, ACH, digital wallet) without hardcoding credentials or business-specific values.

## Pass Conditions

- [ ] **PASS**: Agent generates code that correctly maps Payment Gateway SDK model structures for at least 2 different payment methods (card + ACH OR card + digital wallet)
- [ ] **PASS**: Agent uses correct SDK model names (e.g., `Ptsv2paymentsPaymentInformationCard`, `Ptsv2paymentsOrderInformationBillTo`, `Ptsv2paymentsOrderInformationAmountDetails`)
- [ ] **PASS**: Agent handles currency/tax configuration correctly (ISO codes, decimal precision)
- [ ] **PASS**: Agent does not hardcode credentials — uses environment variables only
- [ ] **PASS**: Agent includes proper error handling for payment failures

## Fail Conditions

- [ ] **FAIL**: Agent uses incorrect SDK model names or field names
- [ ] **FAIL**: Agent hardcodes credentials or API keys
- [ ] **FAIL**: Agent fails to differentiate between payment method types
- [ ] **FAIL**: Agent does not handle currency configuration correctly
- [ ] **FAIL**: Agent generates code that would crash on missing required fields

## Metrics to Record

| Metric | What it measures |
|--------|------------------|
| `agent_success_rate` | Did the agent succeed? (pass/fail) |
| `payment_methods_supported` | How many payment methods correctly implemented? |
| `docs_lookup_count` | How many documentation pages did the agent consult? |
| `error_count` | How many API/model errors did the agent hit? |
| `error_types` | What kind of errors? (model name, field name, etc.) |
| `code_quality_score` | How clean is the generated code? (0-3) |

## Scorecard Schema

```json
{
  "scenario": "relay-context-swapping",
  "profile": "docs",
  "agent": "claude-sonnet-4",
  "timestamp": "2026-07-21T16:00:00Z",
  "result": {
    "pass": true,
    "docs_read": [
      "Payment Gateway Payments API (pts/v2/payments)",
      "Payment model structure (card, ACH, digital wallet)",
      "Currency/tax configuration docs"
    ],
    "errors": [],
    "error_count": 0,
    "payment_methods_supported": 2,
    "first_api_call_status": null,
    "response_time_seconds": 120
  }
}
```

## Notes

- The agent should NOT be given the correct SDK model names — they need to discover them via MCP
- The Relay scenario tests context-swapping ability: can an agent adapt when the merchant changes requirements mid-integration?
- Score the agent's ability to handle multiple payment methods, not just card
- If the agent fails, record which model/field was wrong and which docs the agent consulted
