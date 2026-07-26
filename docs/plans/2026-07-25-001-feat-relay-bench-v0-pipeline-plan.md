# Plan: Relay Bench V0 Pipeline

**ID:** 2026-07-25-001
**Status:** Implemented (local prototype)
**Scope:** Local proof inside this repo (not production Relay)

## Honest V0 label

This V0 proves a concept **inspired by** DocETL and Tempo Stable Bench.
It does **not** integrate the real systems yet:

| Inspired by | Actual upstream | Used in V0? |
|-------------|-----------------|-------------|
| DocETL-inspired workflow discovery | [`ucbepic/docetl`](https://github.com/ucbepic/docetl) (`docetl` on PyPI) | **No** — local heuristic extract/suggest only |
| Stable Bench-inspired verifier | [`tempoxyz/tempo-evals`](https://github.com/tempoxyz/tempo-evals) (Harbor, Stable Bench task format, Docker isolation) | **No** — local deterministic fixture checks only |

There is no dependency on `docetl`, `harbor`, or `tempo-evals` in V0.

**PM read:** This PR proves the staging/contract concept. Real DocETL map/reduce/extract pipelines and Tempo/Harbor isolated agent runs are a V1 decision.

## Problem

Developers hit hard, multi-step CyberSource / Visa Acceptance workflows (Flex tokens, HTTP Signature, Microform + Payer Auth) and get stuck. We need a **local, credential-free** pipeline that:

1. Discovers typed workflow candidates from raw forum/docs/support questions (DocETL-inspired).
2. Emits Relay workflow contracts / agent-visible benchmark task packs.
3. Verifies answers with a Stable Bench-inspired verifier against simulated fixtures.
4. Classifies failures and routes product-surface improvement actions (including VAP CLI descriptors).
5. Produces a PM-readable report of the proof.

DocETL-inspired extraction and Stable Bench-inspired verification stay **separate stages** joined by typed artifacts. Do not fuse them into one opaque script.

## Pipeline

```text
raw forum/docs/support questions
-> DocETL-inspired extract of goal/symptoms/entities
-> suggest workflow_id + stages
-> PM approves/edits
-> Relay Bench creates task pack + Stable Bench-inspired verifier
-> failure classifier
-> product-surface improvement action
-> PM-readable report
```

Raw questions must not carry a pre-assigned `workflow_id`. Suggestion is produced from extraction; task packs are created only after PM approve/edit (`data/pm_approvals.json` for the local V0 proof).

## Definition of Done

- [x] `relay_bench/` package with schemas, discovery, task_pack, verifiers, routing, reporting
- [x] `pipelines/synthesize_candidates.py` produces typed candidates from frozen seeds
- [x] `pipelines/run_demo.py` demos the three seeded workflows
- [x] `pipelines/run_bench_v0.py --workflow microform-payer-auth-state-machine` runs the full staged pipeline
- [x] Agent-visible task packs omit oracle, bad answer, and verifier-private checks
- [x] Hidden truth lives in a separate artifact / in-memory structure used only by the verifier
- [x] No network, no live credentials, no PAN/secret logging
- [x] Unit tests cover discovery, task pack separation, verifiers, reporting
- [x] All verification commands listed in the Cursor build prompt pass
- [x] Language clearly labels DocETL-inspired / Stable Bench-inspired (not real upstream integration)

## Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| `schemas.py` | Typed dataclasses for seeds, candidates, task packs, hidden truth, verifier results, actions, reports |
| `discovery.py` | DocETL-inspired: raw questions → extract goal/symptoms/entities → suggest workflow_id + stages |
| `pm_gate.py` | PM approve/edit/reject gate; reduce approved seeds by `workflow_id` into one richer `WorkflowCandidate` |
| `task_pack.py` | Split approved candidate into agent-visible `TaskPack` + verifier-only `HiddenTruth` |
| `verifiers.py` | Stable Bench-inspired checks against simulated fixtures; return structured `VerifierResult` |
| `routing.py` | Classify failures → `ImprovementAction` (docs, SDK, VAP CLI workflow verifier, etc.) |
| `reporting.py` | PM-readable markdown/JSON answering the five proof questions |

## Workflows (V0 seeds)

1. `flex-token-lifecycle` — transient Flex token → permanent TMS instrument confusion
2. `http-signature-debug` — HTTP Signature header / SDK field-name friction
3. `microform-payer-auth-state-machine` — Microform capture vs Payer Auth enrollment/challenge states

## VAP CLI Product Bias

When routing to VAP CLI, treat the CLI as a **workflow verifier**, not a thin command wrapper. Descriptors should include: goal, command, API/SDK facts, readiness checks, recovery path, support-safe evidence, telemetry/eval hints, future MCP metadata. V0 actions are recommendations or deterministic fixture checks only.

## Non-Goals (V0)

- Importing or depending on `docetl`, `tempo-evals`, Harbor, or Docker isolation
- Live CyberSource sandbox calls
- Real credential materialization
- Production Relay deployment
- Opaque single-script fusion of discovery + verification

## V1 options (not in this PR)

- Bring in `docetl` for real map/reduce/extract pipelines over raw forum/docs/support inputs
- Bring in `tempo-evals` / Harbor-style task packaging for isolated agent runs, oracle separation, verifier images, and reproducible docs/MCP profiles

## Artifacts

```text
artifacts/task_packs/<workflow>.task_pack.json
artifacts/task_packs/<workflow>.hidden_truth.json   # verifier-only; never agent-facing
artifacts/verifier_results/<workflow>.result.json
artifacts/reports/<workflow>.report.md
artifacts/reports/<workflow>.report.json
```
