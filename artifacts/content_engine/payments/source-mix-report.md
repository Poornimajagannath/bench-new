# Source mix report

Milestone 0 inventory: what fraction of each guide's facts could be regenerated from the local OpenAPI fixture versus facts that exist only in prose.

- OpenAPI: `data/content_engine/specs/cybersource-payments-core.openapi.json`
- Guides sampled: 38
- Overall spec-backed share: **85.6%**
- Overall prose-only share: **14.4%**
- Decision rule outcome: spec-primary: generate endpoint pages from OpenAPI; DocETL mines prose only for gaps

## Per-guide table

| Guide | Spec-backed | Prose-only | Spec hits | Prose hits | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| credentials | 78.3% | 21.7% | 18 | 5 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex | 81.1% | 18.9% | 30 | 7 | index-like; mostly navigation / revision surface |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro | 88.9% | 11.1% | 8 | 1 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments | 100.0% | 0.0% | 2 | 0 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_flex-api-2 | 66.7% | 33.3% | 2 | 1 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2 | 100.0% | 0.0% | 5 | 0 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_payments_intro_digt_accpt_sec_intg | 100.0% | 0.0% | 4 | 0 | — |
| en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_uc-intro | 87.5% | 12.5% | 7 | 1 | — |
| en-us_payer-authentication_developer_all_rest_payer-auth | 77.3% | 22.7% | 34 | 10 | index-like; mostly navigation / revision surface |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa-reports-intro | 50.0% | 50.0% | 1 | 1 | — |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa-testing-intro | 66.7% | 33.3% | 2 | 1 | — |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro | 40.0% | 60.0% | 2 | 3 | index-like; mostly navigation / revision surface |
| en-us_payer-authentication_developer_all_rest_payer-auth_pa2-intro-intro | 80.0% | 20.0% | 4 | 1 | — |
| en-us_payments_developer_ctv_rest_payments | 75.0% | 25.0% | 27 | 9 | index-like; mostly navigation / revision surface |
| en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_payments_developer_ctv_rest_payments_payments-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_tms_developer_all_rest_tms | 83.3% | 16.7% | 35 | 7 | index-like; mostly navigation / revision surface |
| en-us_tms_developer_all_rest_tms_tms-bin-lookup-service | 100.0% | 0.0% | 7 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-card-art | 100.0% | 0.0% | 3 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-create-request | 90.9% | 9.1% | 10 | 1 | — |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn | 100.0% | 0.0% | 2 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn | 100.0% | 0.0% | 1 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn | 50.0% | 50.0% | 1 | 1 | — |
| en-us_tms_developer_all_rest_tms_tms-ii-tkn | 100.0% | 0.0% | 3 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-net-tkn-intro | 76.9% | 23.1% | 10 | 3 | index-like; mostly navigation / revision surface |
| en-us_tms_developer_all_rest_tms_tms-net-tkn-onboard | 100.0% | 0.0% | 4 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-onboarding | 100.0% | 0.0% | 1 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-overview | 62.5% | 37.5% | 5 | 3 | index-like; mostly navigation / revision surface |
| en-us_tms_developer_all_rest_tms_tms-pi-tkn | 100.0% | 0.0% | 1 | 0 | — |
| en-us_tms_developer_all_rest_tms_tms-wallet-tkn | 100.0% | 0.0% | 2 | 0 | — |
| en-us_tms_developer_ctv_rest_tms | 81.0% | 19.0% | 34 | 8 | index-like; mostly navigation / revision surface |
| payer-auth | 77.3% | 22.7% | 34 | 10 | index-like; mostly navigation / revision surface |
| payments | 75.0% | 25.0% | 27 | 9 | index-like; mostly navigation / revision surface |
| rest-getting-started | 81.2% | 18.8% | 26 | 6 | index-like; mostly navigation / revision surface |
| sandbox | 100.0% | 0.0% | 1 | 0 | — |
| testing-guide | 100.0% | 0.0% | 9 | 0 | — |
| tms | 83.3% | 16.7% | 35 | 7 | index-like; mostly navigation / revision surface |

## Top 10 prose-only sections for a first integration

_No prose-dominant sections found in the sample._
