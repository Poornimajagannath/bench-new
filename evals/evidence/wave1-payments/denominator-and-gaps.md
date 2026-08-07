# Wave 1 completion — real payments OpenAPI denominator

- When: `2026-08-07T07:03:27+00:00`
- Registered source: `cybersource-payments-openapi`
- Spec file: `data/content_engine/specs/cybersource-payments.openapi.json`
- Upstream: `https://developer.cybersource.com/api-reference-assets/specs/cybs_merged.json` (scope `/pts/`)
- Fixture retained: `payments-core-openapi` → `data/content_engine/specs/payments-core.openapi.json` (engine tests only)

## Specs-to-docs

| Metric | Value |
| --- | ---: |
| Operations found | **30** |
| Pages generated | **30** |
| Deliberate exclusions | **0** |

Exclusion list (`data/content_engine/payments_op_exclusions.json`): `[]`  
_Deliberate skip list for Wave 1 real-spec run. Empty = generate a page for every /pts/ operation in cybersource-payments.openapi.json. Add operationIds here only with a one-line reason in reasons._

### Operations (denominator)

| Method | Path | operationId |
| --- | --- | --- |
| POST | `/pts/v1/pull-funds-transfer` | `createPullFundsTransfer` |
| POST | `/pts/v1/pull-funds-transfer/{id}/refund` | `createPullFundsRefund` |
| POST | `/pts/v1/pull-funds-transfer/{id}/reversal` | `createPullFundsReversal` |
| GET | `/pts/v1/transaction-batch-details/{id}` | `getTransactionBatchDetails` |
| GET | `/pts/v1/transaction-batches` | `getTransactionBatches` |
| GET | `/pts/v1/transaction-batches/{id}` | `getTransactionBatchId` |
| POST | `/pts/v2/billing-agreements` | `billingAgreementsRegistration` |
| PATCH | `/pts/v2/billing-agreements/{id}` | `billingAgreementsDeRegistration` |
| POST | `/pts/v2/billing-agreements/{id}/intimations` | `billingAgreementsIntimation` |
| POST | `/pts/v2/captures/{id}/refunds` | `refundCapture` |
| POST | `/pts/v2/captures/{id}/voids` | `voidCapture` |
| POST | `/pts/v2/credits` | `createCredit` |
| POST | `/pts/v2/credits/{id}/voids` | `voidCredit` |
| POST | `/pts/v2/intents` | `createOrder` |
| PATCH | `/pts/v2/intents/{id}` | `updateOrder` |
| POST | `/pts/v2/payment-references` | `createSessionRequest` |
| PATCH | `/pts/v2/payment-references/{id}` | `updateSessionRequest` |
| POST | `/pts/v2/payment-references/{id}/intents` | `createOrderRequest` |
| POST | `/pts/v2/payment-tokens` | `retrieveOrDeletePaymentToken` |
| POST | `/pts/v2/payments` | `createPayment` |
| PATCH | `/pts/v2/payments/{id}` | `incrementAuth` |
| POST | `/pts/v2/payments/{id}/captures` | `capturePayment` |
| POST | `/pts/v2/payments/{id}/refunds` | `refundPayment` |
| POST | `/pts/v2/payments/{id}/reversals` | `authReversal` |
| POST | `/pts/v2/payments/{id}/voids` | `voidPayment` |
| POST | `/pts/v2/payouts` | `octCreatePayment` |
| POST | `/pts/v2/refresh-payment-status/{id}` | `refreshPaymentStatus` |
| POST | `/pts/v2/refunds/{id}/voids` | `voidRefund` |
| POST | `/pts/v2/reversals` | `mitReversal` |
| POST | `/pts/v2/voids` | `mitVoid` |

## Gate table (real denominators)

| Gate | Result |
| --- | --- |
| Unit tests | **74 ran, 7 skipped, 0 failed** |
| Ops with pages | **30/30** |
| Task eval mock | **pass** (denominator 30) |
| Parity score | **100.0%** (12 pass / 0 partial / 0 fail) |
| Zero `raw/` reads | **pass** |
| Fact-hash / humanizer | pages regenerated + humanize pipeline run |

## Prior 95.8% run — what did not pass

From the fixture-era evidence (`evals/evidence/wave1-payments/parity.md`):

| Check | Result then | Classification |
| --- | --- | --- |
| `rest_getting_started_aligned` | **partial** | **Eval calibration.** Checker was hard-coded to return at best `partial`. Fixed: now measurable pass/partial/fail against runtime signals. Current run: **pass**. |

## Top three drop-log entries (Wave 1 payments ingestion)

1. `2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro.md.md` — no_schema_match — no quickstart/endpoint/error/prose claim extracted
2. `2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments.md.md` — no_schema_match — no quickstart/endpoint/error/prose claim extracted
3. `2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2.md.md` — no_schema_match — no quickstart/endpoint/error/prose claim extracted

## Eval honesty

- `evals/spec_ops.py` loads operation lists from the registered OpenAPI at runtime.
- No hard-coded expected operation lists in `evals/run_payments_eval.py` or `evals/run_cybersource_docs_compare.py`.
