# Wave 2 boarding rerun — one-sequence workflows

Generated: 2026-08-08T04:22:03+00:00

Claims file: `normalized/2026-08-08-boarding.claims.json` (**2436** claims; source: renormalize + compose).
api_reference endpoint_facts in boarding raw: **70**

## Outcome gap (the number)

**215/277** sequence steps lack a stated outcome.
Denominator: **277** steps (20 API + 257 UI); source: `composed workflow sequence_stats (API ops + UI steps; expected outcome Gap markers)`.
Prior figure: 220/257 — Measured before endpoint extraction; UI-only step count.

## Per workflow

| Workflow | Steps | Outcome gaps | API | UI |
|---|---:|---:|---:|---:|
| create-merchant-organization | 34 | 27 | 3 | 31 |
| extend-hierarchy | 34 | 29 | 1 | 33 |
| enable-configure-products | 189 | 145 | 11 | 178 |
| search-organizations | 14 | 9 | 4 | 10 |
| change-organization-status | 4 | 3 | 1 | 3 |
| send-registration-email | 2 | 2 | 0 | 2 |

Gap addendum: `artifacts/content_engine/boarding/gap-report-wave-rerun.md`
