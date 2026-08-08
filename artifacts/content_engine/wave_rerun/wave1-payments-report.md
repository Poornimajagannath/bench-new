# Wave 1 payments — denominator correction

Generated: 2026-08-08T04:31:38+00:00

The wave-rerun 3/4 figure used the engine-test fixture (payments-core.openapi.json, 4 /pts/ ops) and generated pages from the payments product-root guide endpoint_facts — not the registered Wave 1 OpenAPI. Nothing was dropped from the real spec; the denominator source changed. This rerun restores the registered spec (cybersource-payments.openapi.json, 30 /pts/ ops) and regenerates reference pages from cybersource-payments-openapi units.

## Side by side

| Run | Ratio | Pages | Denominator | Source file |
|---|---|---:|---:|---|
| Wave 1 closeout | 30/30 | 30 | 30 | `data/content_engine/specs/cybersource-payments.openapi.json` |
| Mistaken wave rerun | 3/4 | 38 | 4 | `data/content_engine/specs/payments-core.openapi.json` |
| This correction | 30/30 | 30 | 30 | `data/content_engine/specs/cybersource-payments.openapi.json` |

Evidence for closeout 30/30: `evals/evidence/wave1-payments/denominator-and-gaps.md`.
Units used for correction: `artifacts/content_engine/generated/cybersource-payments-openapi.api_reference_units.json`.

## Secondary: registered ops covered by payments guide endpoint_facts

**12/30** (denominator: registered `/pts/` ops; source: `raw/product-roots/en-us_payments_developer_ctv_rest_payments.md.md`). Secondary metric only — Wave 1 gate remains pages vs registered OpenAPI ops, not guide coverage.

| Method | Path | operationId | Guide endpoint_fact |
|---|---|---|---|
| `POST` | `/pts/v2/payments` | `createPayment` | yes |
| `PATCH` | `/pts/v2/payments/{id}` | `incrementAuth` | yes |
| `POST` | `/pts/v2/payments/{id}/reversals` | `authReversal` | yes |
| `POST` | `/pts/v2/reversals` | `mitReversal` | yes |
| `POST` | `/pts/v2/payments/{id}/captures` | `capturePayment` | yes |
| `POST` | `/pts/v2/payments/{id}/refunds` | `refundPayment` | yes |
| `POST` | `/pts/v2/captures/{id}/refunds` | `refundCapture` | yes |
| `POST` | `/pts/v2/credits` | `createCredit` | yes |
| `POST` | `/pts/v2/payments/{id}/voids` | `voidPayment` | yes |
| `POST` | `/pts/v2/captures/{id}/voids` | `voidCapture` | yes |
| `POST` | `/pts/v2/refunds/{id}/voids` | `voidRefund` | no |
| `POST` | `/pts/v2/credits/{id}/voids` | `voidCredit` | yes |
| `POST` | `/pts/v2/voids` | `mitVoid` | yes |
| `POST` | `/pts/v2/refresh-payment-status/{id}` | `refreshPaymentStatus` | no |
| `POST` | `/pts/v2/billing-agreements` | `billingAgreementsRegistration` | no |
| `PATCH` | `/pts/v2/billing-agreements/{id}` | `billingAgreementsDeRegistration` | no |
| `POST` | `/pts/v2/billing-agreements/{id}/intimations` | `billingAgreementsIntimation` | no |
| `POST` | `/pts/v2/payment-references/{id}/intents` | `createOrderRequest` | no |
| `POST` | `/pts/v2/payment-references` | `createSessionRequest` | no |
| `PATCH` | `/pts/v2/payment-references/{id}` | `updateSessionRequest` | no |
| `POST` | `/pts/v2/intents` | `createOrder` | no |
| `PATCH` | `/pts/v2/intents/{id}` | `updateOrder` | no |
| `POST` | `/pts/v2/payment-tokens` | `retrieveOrDeletePaymentToken` | no |
| `GET` | `/pts/v1/transaction-batches` | `getTransactionBatches` | no |
| `GET` | `/pts/v1/transaction-batches/{id}` | `getTransactionBatchId` | no |
| `GET` | `/pts/v1/transaction-batch-details/{id}` | `getTransactionBatchDetails` | no |
| `POST` | `/pts/v2/payouts` | `octCreatePayment` | no |
| `POST` | `/pts/v1/pull-funds-transfer` | `createPullFundsTransfer` | no |
| `POST` | `/pts/v1/pull-funds-transfer/{id}/reversal` | `createPullFundsReversal` | no |
| `POST` | `/pts/v1/pull-funds-transfer/{id}/refund` | `createPullFundsRefund` | no |
