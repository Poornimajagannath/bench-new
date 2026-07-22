# Agent Readiness Testing — Success Criteria

## What Success Looks Like

The agent systematically tests multiple integration scenarios, identifies DX issues accurately, and produces a structured report with actionable recommendations.

## Pass Conditions

- [ ] **PASS**: Agent tests at least 2 different payment methods (card + ACH OR card + digital wallet)
- [ ] **PASS**: Agent correctly identifies SDK field name mismatches between docs and implementation
- [ ] **PASS**: Agent documents auth failures with root cause analysis
- [ ] **PASS**: Agent tests at least 3 different currencies and reports handling issues
- [ ] **PASS**: Agent categorizes issues by bucket (auth, model, currency, error handling, etc.)
- [ ] **PASS**: Agent assigns severity ratings (low/medium/high) to each issue

## Fail Conditions

- [ ] **FAIL**: Agent doesn't test multiple payment methods
- [ ] **FAIL**: Agent fails to identify SDK/documented field name differences
- [ ] **FAIL**: Agent reports issues without severity or bucket categorization
- [ ] **FAIL**: Agent misses currency/internationalization issues
- [ ] **FAIL**: Agent produces incomplete findings report

## Metrics to Record

| Metric | What it measures |
|--------|------------------|
| `agent_success_rate` | Did the agent succeed? (pass/fail) |
| `test_scenarios_covered` | How many scenarios tested? |
| `issues_identified` | How many DX issues found? |
| `issues_by_bucket` | Distribution of issues across categories |
| `docs_consulted` | How many docs/pages consulted? |
| `findings_quality` | Are recommendations actionable? (0-3) |

## Scorecard Schema

```json
{
  "scenario": "agent-readiness-testing",
  "profile": "docs",
  "agent": "claude-sonnet-4",
  "timestamp": "2026-07-21T16:00:00Z",
  "result": {
    "pass": true,
    "test_scenarios_covered": 3,
    "issues_identified": 5,
    "issues_by_bucket": {
      "auth-mechanism": 2,
      "sdk-usage": 2,
      "currency-config": 1
    },
    "docs_read": [
      "CyberSource Auth Documentation",
      "Payment Model Structures",
      "Currency/Tax Configuration"
    ],
    "findings_quality": 3
  }
}
```

## Notes

- Score the agent's systematic approach, not just whether it finds every issue
- The agent must categorize issues by bucket (see dx-issue-taxonomy.md)
- Severity ratings must be justified with evidence
- If the agent fails, record which test scenarios it skipped and why
