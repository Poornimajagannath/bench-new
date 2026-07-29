# Relay Bench V0 (local prototype)

**Status:** Credential-free local proof
**Not:** production Relay, live CyberSource sandbox, real DocETL, or real Tempo/Harbor

## Product thesis

Developers stuck on Flex, Microform + Payer Auth, or HTTP Signature should not have to stitch together forum threads, docs pages, SDK quirks, and AI guesses.

Relay Bench turns that confusion into a **workflow contract**:

```text
public developer confusion
→ structured workflow candidate
→ agent-visible task pack (agent_task)
→ hidden verifier/oracle (verifier_private)
→ structured verifier result
→ product-surface improvement action
→ PM-readable report
```

That improves:

1. **Docs** — rewrite around misunderstood workflows, not isolated APIs
2. **VAP CLI** — eventually `vap workflow verify --id <workflow> --fixture local`
3. **Assistant / MCP answers** — ground replies in the contract
4. **Quality gate** — prove bad answers are caught so docs/CLI/assistant can be measured

## V0 boundary (honest label)

| Label | Upstream | Used in V0? |
|-------|----------|-------------|
| DocETL-inspired discovery | [`ucbepic/docetl`](https://github.com/ucbepic/docetl) | **No import** — local heuristic extract/suggest |
| Stable Bench-inspired verifier | [`tempoxyz/tempo-evals`](https://github.com/tempoxyz/tempo-evals) | **No Harbor/Docker** — deterministic fixture checks |

V0 is dependency-light Python stdlib only. No network. No sandbox credentials. No PAN/secret logging.

## Pipeline

```text
hard question seeds (20 frozen JSONL)
→ DocETL-inspired extract goal/symptoms/entities
→ suggest workflow_id + stages
→ PM approve/edit (reduce many seeds → one contract)
→ Relay Bench creates agent_task + verifier_private
→ failure classifier
→ product-surface improvement action
→ PM-readable report
```

## Run

```bash
python3 -m unittest discover -s tests
python3 pipelines/synthesize_candidates.py
python3 pipelines/run_demo.py --workflow flex-token-lifecycle
python3 pipelines/run_demo.py --workflow http-signature-debug
python3 pipelines/run_demo.py --workflow microform-payer-auth-state-machine
python3 pipelines/run_bench_v0.py --workflow microform-payer-auth-state-machine
```

## PM entrypoints

- `reports/what_we_built.md` — orientation: what Relay Bench V0 is
- `HANDOFF.md` — intent and acceptance criteria
- `reports/pm_workbook.md` — why Relay Bench exists
- `reports/demo_microform_payer_auth_state_machine.md` — advanced workflow proof
- `reports/generated_failure_taxonomy.md` — failure-class routing
- `artifacts/reports/microform-payer-auth-state-machine.report.md` — latest generated proof

## Plan

`docs/plans/2026-07-25-001-feat-relay-bench-v0-pipeline-plan.md` is authoritative for CE/DoD.
