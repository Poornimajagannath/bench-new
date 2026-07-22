 Benchmark Lab

**Status:** Docs-only )

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
│   └──-context-swapping/
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
|context-swapping | Context switching between scenarios | Ready |

## Running

```bash
# Run a single scenario
bash scripts/run-scenario.sh <scenario-name>

# Evaluate results
bash scripts/evaluate-run.sh <run-id>

# Full lab loop
bash scripts/lab-loop.sh
```


