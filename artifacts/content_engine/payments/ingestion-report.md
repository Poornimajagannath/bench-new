# Ingestion report

Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.

- Stamp date: `2026-08-07`
- Docs fetched into raw: 29
- Claims extracted: 6813
- Raw dir: `raw/2026-08-07`
- Normalized file: `normalized/2026-08-07.claims.json`
- Read contract: normalized/, content/
- Forbidden: raw/

## Claims by schema

| Schema | Count |
| --- | ---: |
| quickstart_step | 1321 |
| endpoint_fact | 1696 |
| error_case | 112 |
| prose_claim | 1074 |
| field_table | 2610 |

## Extraction recall

- Prior `no_schema_match` drops in comparison set: 20
- Of those, now yielding claims: **8**
- Still dropped: 12

## Drop log

| Path | Reason | Bytes | First heading | Detail |
| --- | --- | ---: | --- | --- |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa-testing-intro.md.md | quarantine_policy | 400 | Testing Payer Authentication | excluded by corpus census quarantine list |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md | quarantine_policy | 2452 | Implementing Direct API for Payer Authentication | excluded by corpus census quarantine list |
| en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md | quarantine_policy | 688 | Debit and Prepaid Card Processing | excluded by corpus census quarantine list |
| en-us_payments_developer_ctv_rest_payments_payments-intro.md.md | quarantine_policy | 914 | Introduction to Payments | excluded by corpus census quarantine list |
| en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md | quarantine_policy | 229 | Standard Payment Processing | excluded by corpus census quarantine list |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md | quarantine_policy | 230 | Customer Tokens | excluded by corpus census quarantine list |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md | quarantine_policy | 316 | Customer Payment Instruments | excluded by corpus census quarantine list |
| en-us_tms_developer_all_rest_tms_tms-onboarding.md.md | quarantine_policy | 783 | `Token Management Service` Onboarding | excluded by corpus census quarantine list |
| en-us_tms_developer_all_rest_tms_tms-pi-tkn.md.md | quarantine_policy | 318 | Payment Instrument Tokens | excluded by corpus census quarantine list |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md | no_schema_match | 2452 | Implementing Direct API for Payer Authentication | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md | no_schema_match | 688 | Debit and Prepaid Card Processing | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-intro.md.md | no_schema_match | 914 | Introduction to Payments | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md | no_schema_match | 229 | Standard Payment Processing | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md | no_schema_match | 230 | Customer Tokens | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md | no_schema_match | 316 | Customer Payment Instruments | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn.md.md | no_schema_match | 448 | Shipping Address Tokens | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-ii-tkn.md.md | no_schema_match | 1693 | Instrument Identifier Tokens | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-onboarding.md.md | no_schema_match | 783 | `Token Management Service` Onboarding | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-pi-tkn.md.md | no_schema_match | 318 | Payment Instrument Tokens | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-wallet-tkn.md.md | no_schema_match | 210 | Using `Token Management Service` with Wallet Apps | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/sandbox.md | no_schema_match | 622 | Source: https://developer.cybersource.com/hello-world/sandbox.md | no quickstart/endpoint/error/prose claim extracted |

## Sampled human check (10 drops)

Do not triage by filename alone. For each row confirm shell vs missed claim.

| # | Path | Reason | Bytes | First heading |
| ---: | --- | --- | ---: | --- |
| 1 | `2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md` | no_schema_match | 2452 | Implementing Direct API for Payer Authentication |
| 2 | `2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md` | no_schema_match | 688 | Debit and Prepaid Card Processing |
| 3 | `2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-intro.md.md` | no_schema_match | 914 | Introduction to Payments |
| 4 | `2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md` | no_schema_match | 229 | Standard Payment Processing |
| 5 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md` | no_schema_match | 230 | Customer Tokens |
| 6 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md` | no_schema_match | 316 | Customer Payment Instruments |
| 7 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn.md.md` | no_schema_match | 448 | Shipping Address Tokens |
| 8 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-ii-tkn.md.md` | no_schema_match | 1693 | Instrument Identifier Tokens |
| 9 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-onboarding.md.md` | no_schema_match | 783 | `Token Management Service` Onboarding |
| 10 | `2026-08-07/en-us_tms_developer_all_rest_tms_tms-pi-tkn.md.md` | no_schema_match | 318 | Payment Instrument Tokens |
