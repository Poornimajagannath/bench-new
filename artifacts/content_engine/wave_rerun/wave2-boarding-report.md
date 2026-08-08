# Wave 2 boarding rerun — one-sequence workflows

Generated: 2026-08-08T04:31:39+00:00

Claims file: `normalized/2026-08-08-boarding.claims.json` (**2436** claims; source: renormalize + compose).
api_reference endpoint_facts in boarding corpus: **70**

## Composition eligibility (952 vs 20)

Composer already renders endpoint_fact as sequence API entries (method/path/required fields/example), not only quickstart_step. Underuse vs 952 was mostly cross-product scope + host/stub dedupe, not a step-only filter.

- Cross-product api_reference claims: **952** (source: `artifacts/content_engine/api_reference/api-reference-extraction-report.json`). 952 spans every product root (payments, tms, …). It is not the boarding workflow eligibility pool.
- Boarding api_reference claims: **70** (source: `normalized/2026-08-08-boarding.claims.json (after prefer-child; api_reference pattern only)`)
- Unique boarding ops (by anchor): **19**
- Eligible matched claim instances (doc_matchers): **70**
- Used in sequence after dedupe: **21**
- Unique ops used: **19** / 19
- Orphan ops (no matcher): **0**

### Why claims were excluded

- `not_boarding_product`: **882** — api_reference claims on non-boarding product roots
- `duplicate_host_or_stub_collapsed`: **49** — prod+test host pairs and child Endpoint-stub pages collapsed to one richest claim per operation anchor
- `no_workflow_doc_matcher`: **0** — boarding api_reference op whose anchor matched no workflow

### Per workflow

| Workflow | Matched api_reference claims | Used after dedupe |
|---|---:|---:|
| create-merchant-organization | 12 | 3 |
| extend-hierarchy | 4 | 1 |
| enable-configure-products | 36 | 11 |
| search-organizations | 14 | 5 |
| change-organization-status | 4 | 1 |
| send-registration-email | 0 | 0 |

## Outcome gap (the number)

**215/278** sequence steps lack a stated outcome.
Denominator: **278** steps (21 API + 257 UI); source: `composed workflow sequence_stats (API ops + UI steps; expected outcome Gap markers)`.
Prior figure: 220/257 — Measured before endpoint extraction; UI-only step count.

## Per workflow (sequence)

| Workflow | Steps | Outcome gaps | API | UI |
|---|---:|---:|---:|---:|
| create-merchant-organization | 34 | 27 | 3 | 31 |
| extend-hierarchy | 34 | 29 | 1 | 33 |
| enable-configure-products | 189 | 145 | 11 | 178 |
| search-organizations | 15 | 9 | 5 | 10 |
| change-organization-status | 4 | 3 | 1 | 3 |
| send-registration-email | 2 | 2 | 0 | 2 |

Gap addendum: `artifacts/content_engine/boarding/gap-report-wave-rerun.md`
