---
slug: ledgers/kelly-decisions
title: Kelly Decisions Ledger
type: ledger
---

# Kelly Decisions Ledger

## Format
```
## [YYYY-MM-DD]
- **Decision:** [What was decided]
- **Reasoning:** [Why]
- **Alternatives considered:** [What else was evaluated]
- **Status:** [Implemented / Draft / Deferred]
```

## 2026-07-25
- **Decision:** Use GBrain as canonical ledger, not flat files. INDEX.md is a map only.
- **Reasoning:** Gumclaw lesson — system learns through files, not models. GBrain provides queryable, durable memory.
- **Alternatives considered:** SQLite, plain markdown files, separate agent state
- **Status:** Implemented

- **Decision:** Kelly/Polly/Sherlock are personality skills, not separate agent runtimes.
- **Reasoning:** Multi-agent fleet was operationally messy (Gumclaw lesson). One runtime, three modes, shared substrate.
- **Alternatives considered:** Three separate Hermes instances, multi-agent orchestration
- **Status:** Implemented
