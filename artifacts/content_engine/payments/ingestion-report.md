# Ingestion report

Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.

- Stamp date: `2026-08-07`
- Docs fetched into raw: 38
- Claims extracted: 2551
- Raw dir: `raw/2026-08-07`
- Normalized file: `normalized/2026-08-07.claims.json`
- Read contract: normalized/, content/
- Forbidden: raw/

## Claims by schema

| Schema | Count |
| --- | ---: |
| quickstart_step | 1428 |
| endpoint_fact | 87 |
| error_case | 161 |
| prose_claim | 875 |

## Drop log

| Path | Reason | Detail |
| --- | --- | --- |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_payments_intro_digt_accpt_sec_intg.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_uc-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa-testing-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-intro-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-bin-lookup-service.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-ii-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-onboarding.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-pi-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-wallet-tkn.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/sandbox.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
