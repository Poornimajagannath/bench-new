# PM workbook — Why Relay Bench exists

## The pain

When a developer is stuck on Flex, Microform + Payer Auth, or HTTP Signature, today’s path is:

1. Search forums
2. Skim docs pages
3. Guess SDK field names
4. Ask an assistant that may skip stages
5. Fail again without a clear product fix

That is not a measurable developer-experience loop.

## The bet

Relay Bench converts confusion into a **workflow contract**:

```text
developer confusion
→ workflow candidate
→ agent_task
→ verifier_private
→ verifier result
→ docs / CLI / MCP improvement
```

For Microform + Payer Authentication, the system can say:

- Developers skip enrollment / challenge / validation
- Correct stages are the state machine below
- The bad answer fails these checks
- Next surface: docs + VAP CLI workflow verifier

## What “good” looks like for PM

| Surface | Improvement |
|---------|-------------|
| Docs | Rewrite around the misunderstood workflow order |
| VAP CLI | `vap workflow verify --id microform-payer-auth-state-machine --fixture local` |
| MCP / assistant | Answer from the contract, not generic retrieval |
| Quality | Measure whether bad answers are still caught after doc/CLI changes |

## Honest V0 caveat

This package proves the **shape**. It does not yet import real DocETL or Tempo evals/Harbor. V1 decides whether to integrate those systems or keep a lightweight local implementation.

## Where to look next

1. `reports/what_we_built.md`
2. `reports/demo_microform_payer_auth_state_machine.md`
3. `artifacts/reports/microform-payer-auth-state-machine.report.md`
4. `reports/generated_failure_taxonomy.md`
