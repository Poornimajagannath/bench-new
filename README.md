# Visa Relay Benchmark Lab

**Status:** Docs-only (live auth blocked — see BLOCKERS.md)

## Structure

```
visa-relay-bench/
├── README.md                # This file
├── BLOCKERS.md              # Live auth blockers (HTTP Signature v1.0 bug)
├── FINDINGS-TEMPLATE.md     # Benchmark result format
├── CLAUDE.md                # Agent instructions
├── scenarios/               # Test scenarios
│   ├── agent-readiness-testing/
│   ├── authentication/      # Auth scenario (no live execution)
│   ├── first-transaction/
│   ├── setup-checkout/
│   └── visa-relay-context-swapping/
├── templates/               # Code templates from MCP SDK docs
│   ├── card-payment/
│   ├── ach-payment/
│   ├── digital-wallet/
│   ├── multi-currency/
│   └── config/
├── evaluators/              # Scoring rubrics
├── scripts/                 # Run scripts
├── context/                 # Reference docs
└── prompts/                 # Agent prompts
```

## Scenarios

| Scenario | Description | Status |
|----------|-------------|--------|
| agent-readiness-testing | Test if agents can handle CyberSource workflows | Ready |
| authentication | Auth credential management (docs only) | Blocked |
| first-transaction | First payment transaction scenario | Ready |
| setup-checkout | Checkout integration scenario | Ready |
| visa-relay-context-swapping | Context switching between scenarios | Ready |

## Running

```bash
# Run a single scenario
bash scripts/run-scenario.sh <scenario-name>

# Evaluate results
bash scripts/evaluate-run.sh <run-id>

# Full lab loop
bash scripts/lab-loop.sh
```

## Notes

- All scenarios use docs-only evaluation unless live auth is resolved
- See BLOCKERS.md for the auth issue status
- Templates are generated from MCP SDK model documentation
