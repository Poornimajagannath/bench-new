# Wave 1 payments rerun — reference pages from endpoint_facts

Generated: 2026-08-08T04:22:03+00:00

Source root: `raw/product-roots/en-us_payments_developer_ctv_rest_payments.md.md`
endpoint_fact claims in root: **76**
of which path `/pts/…`: **76**
Pages written: **38** (lineage: ['generated_from_endpoint_fact'])

## /pts/ coverage

Denominator: **4** OpenAPI operations under `/pts/` (source: `data/content_engine/specs/payments-core.openapi.json`).
Covered by guide `endpoint_fact`: **3/4**.

| Method | Path | operationId | Covered |
|---|---|---|---|
| `POST` | `/pts/v2/payments` | `createPayment` | yes |
| `GET` | `/pts/v2/payments/{id}` | `getPayment` | no |
| `POST` | `/pts/v2/payments/{id}/captures` | `capturePayment` | yes |
| `POST` | `/pts/v2/credits` | `createCredit` | yes |

Guide unique `/pts/` method+path keys (source: payments product root extraction): **6**

- `PATCH /pts/v2/payments`
- `POST /pts/v2/captures`
- `POST /pts/v2/credits`
- `POST /pts/v2/payments`
- `POST /pts/v2/reversals`
- `POST /pts/v2/voids`
