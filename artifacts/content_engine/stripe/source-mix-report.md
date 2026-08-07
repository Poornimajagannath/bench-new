# Source mix report

Milestone 0 inventory: what fraction of each guide's facts could be regenerated from the local OpenAPI fixture versus facts that exist only in prose.

- OpenAPI: `data/stripe/openapi-connect.fixture.json`
- Guides sampled: 4
- Overall spec-backed share: **76.5%**
- Overall prose-only share: **23.5%**
- Decision rule outcome: spec-primary: generate endpoint pages from OpenAPI; DocETL mines prose only for gaps

## Per-guide table

| Guide | Spec-backed | Prose-only | Spec hits | Prose hits | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| account-links | 80.0% | 20.0% | 4 | 1 | — |
| connect-authentication | 70.0% | 30.0% | 7 | 3 | — |
| how-connect-works | 72.7% | 27.3% | 8 | 3 | — |
| onboarding-quickstart | 83.3% | 16.7% | 5 | 1 | — |

## Top 10 prose-only sections for a first integration

_No prose-dominant sections found in the sample._
