# CyberSource docs comparison eval

- When: `2026-08-07T06:25:44+00:00`
- Scope: generated `content/*.md` payments pages vs live developer.cybersource.com
- Fidelity score: **95.8%** (11 pass / 1 partial / 0 fail of 12 graded checks)

## Sources fetched

- `payments_intro` → https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md (HTTP 200)
- `payments_basic` → https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-processing-basic-intro.md (HTTP 200)
- `rest_getting_started` → https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started.md (HTTP 200)
- `llms_index` → https://developer.cybersource.com/llms.txt (HTTP 200)

## Checks

| ID | Area | Result | Notes |
| --- | --- | --- | --- |
| `create_path` | Payments API | **pass** | Generated createPayment path must match Payments REST surface. |
| `create_auth` | Auth | **pass** | Page must teach httpSignature from the OpenAPI security schemes. |
| `flattened_amount` | Request fields | **pass** | A2 flatten: nested amount fields must appear as dotted names. |
| `flattened_currency` | Request fields | **pass** | Currency must be present as a flattened body field. |
| `no_raw_pan` | Safety | **pass** | Sandbox payment pages must not encourage raw PAN in production. |
| `ops_coverage` | Coverage | **pass** | Every registered payments operation must have a generated page. |
| `upstream_payments_reachable` | Upstream | **pass** | Parity job must fetch live public CS docs. |
| `upstream_llms_reachable` | Upstream | **pass** | llms.txt index should remain fetchable for ingestion freshness. |
| `rest_getting_started_aligned` | Onboarding | **partial** | Aligned at a high level: auth + first payment concepts. |
| `payments_basic_concepts` | Onboarding | **pass** | Capture flow should appear in generated ops when present upstream. |
| `provenance` | Provenance | **pass** | Pages must label themselves as generated from the OpenAPI unit. |
| `no_raw_dir` | Serve contract | **pass** | Published pages must not point readers at raw/. |

## Verdict

Parity evidence **pass** at 95.8% on the graded checklist. Quote as “N of N parity checks,” not “identical to CyberSource.”

This parity eval is nightly evidence only — it must not gate PRs.
Private corpus, traces, and drop logs must never be copied to public content-bench.
