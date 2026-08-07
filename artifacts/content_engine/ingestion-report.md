# Ingestion report

Milestone 0.5: corpus cleaned at the door. `raw/` is immutable evidence; serve layers read only `normalized/` and `content/`.

- Stamp date: `2026-08-07`
- Docs fetched into raw: 60
- Claims extracted: 1067
- Raw dir: `raw/2026-08-07`
- Normalized file: `normalized/2026-08-07.claims.json`
- Read contract: normalized/, content/
- Forbidden: raw/

## Claims by schema

| Schema | Count |
| --- | ---: |
| quickstart_step | 486 |
| endpoint_fact | 8 |
| error_case | 135 |
| prose_claim | 438 |

## Drop log

| Path | Reason | Detail |
| --- | --- | --- |
| 2026-08-07/en-us_apple-pay_developer_all_rest_applepay_applepay-getting-started.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_click-to-pay_developer_all_rest_click-to-pay_ctp-tokens-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_click-to-pay_developer_all_rest_click-to-pay_uc-token-get-pymnt-details.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_cp-retail_integration_ctv_rest_cp-retail_cp-intro-cpc.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_cp-retail_integration_ctv_rest_cp-retail_cp-payment-services-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_credentials_developer_ctv_rest_credentials_credentials-reauth-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_dcc_developer_all_rest_dcc-merchant_dcc-merchant-use-cases_dcc-merchant-refund.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_payments_intro_digt_accpt_sec_intg.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_ev-charging_developer_ctv_rest_ev-charging_home.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_google-pay_developer_ctv_rest_googlepay_googpay-pay-auth-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_invoicing_developer_all_rest_invoicing_invoicing-ebc.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_lodging_developer_ctv_rest_lodging_lodging-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_lodging_developer_ctv_rest_lodging_lodging-payment-services.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_paybylink_developer_all_rest_paybylink_paybylink-services.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa-testing-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payer-authentication_developer_all_rest_payer-auth_pa2-intro-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_paze_integration_all_rest_paze_paze-gs.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_paze_integration_all_rest_paze_paze-txns-auth-cybs.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_paze_integration_all_rest_paze_paze-txns-auth-merch.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_platform_relnote_all_na_rn-2025-07-18_rn-general.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_platform_relnote_all_na_rn-2025-09-26_rn-general.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_platform_relnote_all_na_rn-2025-12-12_rn-general.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_platform_relnote_all_na_rn-2026-03-06_rn-general.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_reporting_user_all_ebc_reporting-ug_c_Viewing_On-Demand_Reports.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_tms_developer_all_rest_tms_tms-bin-lookup-service.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_txn-search_developer_all_rest_txn-search_time-zones.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
| 2026-08-07/en-us_unified-checkout_developer_all_rest_unified-checkout_uc-reference-test-cards.md.md | no_schema_match | no quickstart/endpoint/error/prose claim extracted |
