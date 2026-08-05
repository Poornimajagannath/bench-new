# Relay Bench V0 — Handoff

## PM intent

Prove that public developer confusion can be reduced into a **Relay-style workflow contract** with:

- an agent-visible task (`agent_task`)
- a hidden verifier/oracle (`verifier_private`)
- a deterministic catch of known-bad answers
- a product-surface recommendation (docs / VAP CLI / MCP)

This is a throwaway-but-reviewable local prototype. It is **not** production Relay.

## Existing packet

| Artifact | Role |
|----------|------|
| `data/hard_questions.seed.jsonl` | 20 frozen forum/docs/support questions (no pre-labeled `workflow_id`) |
| `data/pm_approvals.json` | PM approve/edit decisions; many seeds reduce to 3 workflows |
| `relay_bench/` | Schemas, DocETL-inspired discovery, PM gate, task pack, verifier, routing, reporting |
| `pipelines/synthesize_candidates.py` | Extract → suggest (+ show PM-approved set) |
| `pipelines/run_demo.py` | Per-workflow demo materialization |
| `pipelines/run_bench_v0.py` | Full staged proof for one workflow |
| `artifacts/` | Generated task packs, verifier results, reports |
| `reports/` | Stable PM-facing narrative copies |
| `docs/plans/2026-07-25-001-feat-relay-bench-v0-pipeline-plan.md` | Authoritative CE plan |

## Acceptance criteria

1. Commands in README all exit 0.
2. 20 seeds synthesize into suggestions; PM gate reduces to **3** workflow contracts.
3. `agent_task` artifacts contain no oracle, bad-answer, or verifier-private fields/values.
4. Bad-answer probe requires the **full** `expected_bad_failure_ids` set.
5. Reports answer the five PM questions.
6. Language says DocETL-inspired / Stable Bench-inspired — not real upstream integration.
7. No network, credentials, PAN, or secret logging.

## Workflows in scope

- `flex-token-lifecycle`
- `http-signature-debug`
- `microform-payer-auth-state-machine`

## Out of scope / stop conditions

Ask before: live network, sandbox credentials, raw PAN/secrets, production Relay/VAP CLI edits, or collapsing discovery + verification into one untyped script.
