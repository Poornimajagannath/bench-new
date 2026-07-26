# Plan: Relay Bench V0 Pipeline

**ID:** 2026-07-25-001  
**Status:** Ready for implementation  
**Scope:** Local proof inside this repo (not production Relay)

## Problem

Developers hit hard, multi-step CyberSource / Visa Acceptance workflows (Flex tokens, HTTP Signature, Microform + Payer Auth) and get stuck. We need a **local, credential-free** pipeline that:

1. Discovers typed workflow candidates from frozen hard-question seeds (DocETL-style).
2. Emits Relay workflow contracts / agent-visible benchmark task packs.
3. Verifies answers with a Tempo-style verifier against simulated fixtures.
4. Classifies failures and routes product-surface improvement actions (including VAP CLI descriptors).
5. Produces a PM-readable report of the proof.

DocETL-style extraction and Tempo-style benchmarking stay **separate stages** joined by typed artifacts. Do not fuse them into one opaque script.

## Pipeline

```text
hard question seeds
-> DocETL-style workflow discovery
-> typed workflow candidates
-> Relay workflow contract / benchmark task pack
-> Tempo-style verifier
-> failure classifier
-> product-surface improvement action
-> PM-readable report
```

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

## Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| `schemas.py` | Typed dataclasses for seeds, candidates, task packs, hidden truth, verifier results, actions, reports |
| `discovery.py` | DocETL-style map/reduce over frozen seeds → `WorkflowCandidate` |
| `task_pack.py` | Split candidate into agent-visible `TaskPack` + verifier-only `HiddenTruth` |
| `verifiers.py` | Tempo-style checks against simulated fixtures; return structured `VerifierResult` |
| `routing.py` | Classify failures → `ImprovementAction` (docs, SDK, VAP CLI workflow verifier, etc.) |
| `reporting.py` | PM-readable markdown/JSON answering the five proof questions |

## Workflows (V0 seeds)

1. `flex-token-lifecycle` — transient Flex token → permanent TMS instrument confusion
2. `http-signature-debug` — HTTP Signature header / SDK field-name friction
3. `microform-payer-auth-state-machine` — Microform capture vs Payer Auth enrollment/challenge states

## VAP CLI Product Bias

When routing to VAP CLI, treat the CLI as a **workflow verifier**, not a thin command wrapper. Descriptors should include: goal, command, API/SDK facts, readiness checks, recovery path, support-safe evidence, telemetry/eval hints, future MCP metadata. V0 actions are recommendations or deterministic fixture checks only.

## Non-Goals

- Live CyberSource sandbox calls
- Real credential materialization
- Production Relay deployment
- Opaque single-script fusion of discovery + verification

## Artifacts

```text
artifacts/task_packs/<workflow>.task_pack.json
artifacts/task_packs/<workflow>.hidden_truth.json   # verifier-only; never agent-facing
artifacts/verifier_results/<workflow>.result.json
artifacts/reports/<workflow>.report.md
artifacts/reports/<workflow>.report.json
```
