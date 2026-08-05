# Mission: Relay Bench mental model

## Why
You are steering a Cybersource / Visa Acceptance **compiled context** product (Relay). Agents are writing most of the code; you need a crisp model of what `bench-new` actually proves today — so you can decide what to fund next without confusing “DocETL-style” stubs with real integrations.

## Success looks like
- Point at any artifact under `artifacts/` and say which lane produced it (content compile vs bench/contract)
- Explain what “honest label” means for DocETL vs Tempo/Harbor in one sentence each
- Name the promotion firewall: what must pass before a context pack is trusted

## Constraints
- Often on phone — short lessons, large type, tap-sized quizzes
- Prefer this repo’s real files + primary upstream docs over abstract theory
- Sandbox only; no production credentials in examples

## Out of scope (for now)
- Full service decomposition / multi-brand portals
- Live Tempo/Harbor agent runners
- Deep OpenAPI Specs-to-Docs internals (later lesson)
