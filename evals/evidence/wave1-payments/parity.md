# CyberSource docs comparison eval

- When: `2026-08-07T07:03:16+00:00`
- Scope: generated `content/*.md` payments pages vs live developer.cybersource.com
- Fidelity score: **100.0%** (12 pass / 0 partial / 0 fail of 12 graded checks)

## Sources fetched

- `payments_intro` → https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md (HTTP 200)
- `payments_basic` → https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-processing-basic-intro.md (HTTP 200)
- `rest_getting_started` → https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started.md (HTTP 200)
- `llms_index` → https://developer.cybersource.com/llms.txt (HTTP 200)

## Checks

| ID | Area | Result | Notes |
| --- | --- | --- | --- |
| `create_path` | Payments API | **pass** | Generated createPayment path must match the registered OpenAPI path. |
| `create_auth` | Auth | **pass** | When the registered spec omits security schemes, the page must say so and point at HTTP Signature / JWT getting-started guidance. |
| `flattened_amount` | Request fields | **pass** | A2 flatten: nested amount fields must appear as dotted names. |
| `flattened_currency` | Request fields | **pass** | Currency must be present as a flattened body field. |
| `no_raw_pan` | Safety | **pass** | Sandbox payment pages must not encourage raw PAN in production. |
| `ops_coverage` | Coverage | **pass** | Every in-scope operation from the registered payments OpenAPI must have a page. Denominator is computed at runtime — never a hard-coded list. |
| `upstream_payments_reachable` | Upstream | **pass** | Parity job must fetch live public CS docs. |
| `upstream_llms_reachable` | Upstream | **pass** | llms.txt index should remain fetchable for ingestion freshness. |
| `rest_getting_started_aligned` | Onboarding | **pass** | REST getting-started and generated pages both cover auth + first payment. |
| `payments_basic_concepts` | Onboarding | **pass** | Capture is in the registered spec; page + upstream basic intro should both exist. |
| `provenance` | Provenance | **pass** | Pages must label themselves as generated from the OpenAPI unit. |
| `no_raw_dir` | Serve contract | **pass** | Published pages must not point readers at raw/. |

## Verdict

Parity evidence **pass** at 100.0% on the graded checklist. Quote as “N of N parity checks,” not “identical to CyberSource.”

This parity eval is nightly evidence only — it must not gate PRs.
Private corpus, traces, and drop logs must never be copied to public content-bench.
