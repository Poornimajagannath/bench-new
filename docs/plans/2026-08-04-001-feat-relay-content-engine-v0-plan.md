# Plan: Relay Content Engine V0 (local prototype)

**ID:** 2026-08-04-001
**Status:** Prototyping
**Scope:** Local proof inside `bench-new` (not production Relay)

## Honest V0 label

This plan maps the Relay System Design Document onto a **local content-engine slice**.

It does **not** claim:

| Inspired by / planned | Used in this V0? |
|-----------------------|------------------|
| Real DocETL extraction | **No** — DocETL-style heuristic extract only; optional real DocETL is a later flag |
| Real Tempo / Harbor runner | **No** — Harbor/Tempo-style preview via existing contract compiler |
| Live llms.txt / portal fetch | **No** — frozen local snapshots only |
| `error-discovery` skill | **No** — needs agent/eval traces first |
| Production Relay / VAP CLI edits | **No** |

## Product center

Relay is a **compiled content and context engine**:

```text
raw sources
-> snapshot
-> normalize / segment
-> extract typed knowledge objects
-> eval gate
-> promote trusted outputs
-> serve many surfaces
```

The Workflow Contract Compiler already proves one promoted object type. Content Engine V0 adds the missing front half for **one fixture quickstart** and a tiny serving stub.

## Relationship to existing bench

| Existing module | Role in content engine |
|-----------------|------------------------|
| `discovery.py` / `pm_gate.py` | Confusion → workflow candidate (adjacent lane) |
| `task_pack.py` / `verifiers.py` | Agent-visible pack + hidden-truth eval |
| `contract_compiler.py` | Promote workflow contracts |
| **new** `content_engine/` | Source registry → snapshot → normalize → extract quickstart units → promote → context pack |

## Phase 1a prototype (this PR)

```text
local source registry
-> local markdown snapshot (immutable hash)
-> normalize + segment
-> DocETL-style extract of quickstart_unit objects
-> schema + content validation
-> promote only if pass
-> publish:
   - typed object artifacts
   - context-pack stub
   - link to existing workflow contract when present
```

### In scope

- `data/content_engine/` fixtures and registry
- `relay_bench/content_engine/` package
- `pipelines/run_content_engine_v0.py`
- unit tests for validate/promote firewalls
- artifacts under `artifacts/content_engine/`

### Out of scope / stop conditions

- network fetch of docs / OpenAPI / repos
- importing `docetl`, `tempo-evals`, Harbor, Docker
- live credentials, PAN, secrets
- rewriting canonical source docs
- cloning `error-discovery-skill`
- multi-brand inheritance model
- full knowledge graph / vector store

## Schemas (V0 subset)

Implement only what the prototype needs:

- `source_record`
- `source_snapshot`
- `normalized_document`
- `document_segment`
- `quickstart_unit`
- `promotion_decision`
- `context_pack` (serving stub)

Defer `api_reference_unit` / `api_sample` to Phase 2.

## Eval gates (V0)

1. **Schema validation** — required fields, types, sequence uniqueness
2. **Content validation** — evidence quotes present, sequence integrity, no credential/PAN material
3. **Agent-use validation** — reuse existing workflow verifier / contract receipt when `workflow_id` is linked; otherwise mark `agent_use: deferred`

Promotion requires schema + content pass. Agent-use may be `passed | deferred | failed`.

## Commands

```bash
python3 -m unittest discover -s tests
python3 pipelines/run_content_engine_v0.py --source microform-payer-auth-quickstart
```

## Definition of Done

- [x] Plan committed
- [x] Local registry + markdown snapshot fixture exist
- [x] Pipeline writes normalized, object, promotion, and context-pack artifacts
- [x] Failing validation blocks promotion
- [x] No network / no secrets / no DocETL import
- [x] Language stays DocETL-style / Harbor-Tempo-style honest
- [x] Existing workflow contract compiler tests still pass

## Later phases

1. Optional `--discovery docetl` adapter — **done in follow-on** (`docetl` = real package `code_map` without LLM; `docetl-llm` when an API key exists)
2. API reference + sample extraction
3. Real Tempo/Harbor agent-use runner
4. Proactive starter-pack onboarding + synthetic tasks
5. `error-discovery` over eval/agent traces
6. llms.txt / MCP publish adapters
