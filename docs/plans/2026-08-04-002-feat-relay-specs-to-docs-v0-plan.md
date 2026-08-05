# Plan: Relay Specs-to-Docs V0 (local prototype plan)

**ID:** 2026-08-04-002
**Status:** Planned (not implemented)
**Scope:** Local proof planning inside `bench-new` (not production Relay)

## Honest label

This plan extends the Relay System Design Document with a **specs-to-docs generation lane**.

It does **not** claim any of the following exist yet:

| Capability | In this plan's V0? |
|------------|--------------------|
| Real OpenAPI live fetch / GitHub webhooks | **No** — frozen local spec fixtures only |
| Real DocETL | **No** — DocETL-style extraction remains optional/later |
| Real Tempo / Harbor runner | **No** — Harbor/Tempo-style preview only |
| Overwriting canonical human docs | **No** — generated drafts + reconciliation only |
| `error-discovery` skill | **No** — needs agent/eval traces later |

## Why this lane exists

Phase 1a (`2026-08-04-001`) proved:

```text
local docs fixture
-> snapshot / normalize / segment
-> quickstart_unit extract
-> eval gate
-> promote + context pack
```

Specs-to-docs moves Relay **upstream**:

```text
spec/code contract change
-> parse contract entities
-> compose reference drafts + linked primitives
-> reconcile with human-authored overlays
-> eval (schema / content / contract-alignment / agent-use)
-> promote trusted derived artifacts
```

Principle to preserve:

> Specs are high-trust inputs, not sufficient outputs.

OpenAPI can anchor endpoint/auth/error freshness. It does **not** replace workflow narrative, onboarding sequence, migration nuance, or troubleshooting guidance.

## Relationship to existing bench

| Existing piece | Role |
|----------------|------|
| `relay_bench/content_engine/` | Docs ingest/compile lane (Phase 1a) |
| `relay_bench/contract_compiler.py` | Workflow contract promotion artifact |
| `artifacts/contracts/` | Trusted workflow bundles |
| **new (future)** `relay_bench/content_engine/specs_*` | Spec parse → compose → reconcile lane |

Both lanes must publish into the **same typed graph** with dual lineage:

- `lineage.origin = ingested_prose`
- `lineage.origin = generated_from_spec`
- `lineage.origin = hybrid_reconciled`

## Goals for Specs-to-Docs V0

1. Treat OpenAPI (and related contracts) as first-class registry sources.
2. Parse deterministic `contract_entity` objects from a local fixture.
3. Compose draft `api_reference_unit` objects and candidate quickstart hints.
4. Reconcile generated output against existing human/quickstart/workflow artifacts without overwriting source truth.
5. Gate promotion with schema + content + **contract-alignment** checks.
6. Emit synthetic eval seeds from auth/error/required-field cases.
7. Keep the system local, credential-free, and honest about preview integrations.

## Non-goals for V0

- GitHub Actions / webhook-triggered regeneration
- Network fetch of remote OpenAPI or repos
- Assuming OpenAPI alone produces full onboarding docs
- Mutating canonical source docs or upstream specs
- Full multi-format contract support beyond one OpenAPI fixture
- Production portal publish or MCP server implementation
- Importing `docetl`, `tempo-evals`, Harbor, or Docker

## Proposed local architecture (V0)

```text
source_registry (source_type=openapi)
-> local snapshot (content hash)
-> spec parser -> contract_entity[]
-> documentation composer
   -> api_reference_unit drafts
   -> auth/error sections
   -> quickstart hints (links, not full narrative replacement)
   -> synthetic eval seeds
-> reconciliation engine
   -> added / removed / changed / missing_quickstart_link / stale_claim
-> validation gates
   -> schema
   -> content
   -> contract_alignment
   -> agent_use (passed | deferred | failed)
-> promote derived artifacts only if gates pass
-> optional link to workflow contract bundle + context pack
```

## Schemas to add

### `contract_entity`

```yaml
contract_entity:
  entity_id: string
  product: list[string]
  service_name: string
  endpoint: string
  http_method: string
  operation_id: string
  auth_schemes: list[string]
  request_schema_refs: list[string]
  response_schema_refs: list[string]
  error_schema_refs: list[string]
  tags: list[string]
  examples: list[string]
```

### Reuse / extend existing

- `api_reference_unit` (from SDD; not implemented in Phase 1a)
- `quickstart_unit` hints only (do not auto-author full quickstarts from spec alone)
- `promotion_decision` gains `contract_alignment_passed`
- `context_pack.provenance` gains `lineage_origin`

### Reconciliation report

```yaml
reconciliation_report:
  source_id: string
  spec_snapshot_id: string
  compared_against: list[string]
  added_entities: list[string]
  removed_entities: list[string]
  changed_entities: list[string]
  missing_quickstart_links: list[string]
  stale_human_claims: list[string]
  decisions: list[{entity_id: string, action: enum[generate, flag, keep_human, merge]}]
```

## Subcomponents (implementation shape later)

Prefer this package layout unless a smaller path is obvious at build time:

```text
relay_bench/content_engine/
  specs_parser.py
  specs_compose.py
  specs_reconcile.py
  specs_validate.py
pipelines/
  run_specs_to_docs_v0.py
data/content_engine/
  specs/<fixture>.openapi.json
tests/
  test_specs_to_docs.py
artifacts/content_engine/
  contracts/
  generated/
  reconciliation/
```

### 1. Spec parser

- Input: frozen OpenAPI fixture
- Output: `contract_entity[]` + contract store artifact
- Deterministic IDs from `operation_id` or method+path

### 2. Documentation composer

From each entity, emit:

- draft reference markdown (Relay-derived, not canonical source)
- `api_reference_unit`
- quickstart hint (`endpoint` ↔ candidate workflow/quickstart link)
- eval seeds (missing auth, happy path, representative error)

### 3. Reconciliation engine

Compare generated entities/units against:

- existing Phase 1a quickstart objects
- linked workflow contract bundle when present
- optional human overlay fixture

Never overwrite upstream specs or human source docs. Write Relay-layer drafts + flags only.

### 4. Validation / promotion

| Gate | V0 rule |
|------|---------|
| Schema | required fields / types / refs present |
| Content | grounded summaries, auth/error completeness for references |
| Contract alignment | generated units match parsed entities; no silent drift |
| Agent-use | `deferred` unless linked workflow contract/verifier evidence exists |

Promote only when schema + content + contract-alignment pass.

## Fixture recommendation

Start with one tiny local OpenAPI fixture adjacent to the existing Microform + Payer Auth lane, for example:

- setup / enrollment-like operations (names only; no live endpoints required)
- auth schemes as env-var references (no secret values)
- 2–3 error cases usable as eval seeds

No PAN, no credentials, no network hosts that imply live calls.

## Suggested command (future implementation)

```bash
python3 pipelines/run_specs_to_docs_v0.py --source <openapi-source-id>
```

Expected artifacts:

- `artifacts/content_engine/contracts/<source>.entities.json`
- `artifacts/content_engine/generated/<source>.api_reference_units.json`
- `artifacts/content_engine/reconciliation/<source>.report.json`
- `artifacts/content_engine/generated/<source>.eval_seeds.json`
- promotion decision + optional context-pack update

## Definition of Done (when implemented later)

- [ ] Local OpenAPI source registered and snapshotted
- [ ] Parser emits deterministic `contract_entity` objects
- [ ] Composer emits `api_reference_unit` drafts + eval seeds
- [ ] Reconciliation report created without mutating source fixtures
- [ ] Promotion blocked on contract-alignment failure
- [ ] Linked workflow/quickstart lineage recorded when available
- [ ] Unit tests cover parse/compose/reconcile/promote
- [ ] Language remains honest: no real GitHub automation, DocETL, or Harbor claims
- [ ] Existing content-engine and contract-compiler tests still pass

## Rollout alignment with SDD

| SDD phase | This plan |
|-----------|-----------|
| Phase 1 Core compilation | Done locally via `2026-08-04-001` |
| Phase 2 Structured expansion | Partial later (`api_reference_unit` begins here) |
| Phase 3 Spec-to-docs automation | **This plan (local V0 only)** |
| Phase 4 Eval-gated promotion | Extend existing gates with contract alignment |
| Phase 5 Proactive onboarding | Later; can consume spec-derived eval seeds |

## Open questions to resolve before build

1. First contract format: OpenAPI 3 only, or also JSON Schema fragments?
2. How are intentional spec-vs-guide exceptions represented?
3. Are generated reference drafts auto-promoted after gates, or always `draft` until human signoff?
4. Should eval seeds enter the existing verifier lane immediately, or stay advisory in V0?
5. Multi-brand inheritance (shared / Visa / CyberSource): defer or minimal tag only?

## Recommended decision

Implement Specs-to-Docs as a **separate local lane** that feeds the same Relay object graph and promotion gates, rather than bolting generation into the quickstart extractor. Keep human docs and upstream specs immutable; generate Relay-layer drafts; reconcile; eval; then promote.

## Explicit non-action in this PR

This document is plan-only. No parser/composer/reconcile code, fixtures, or pipeline command are included here.
