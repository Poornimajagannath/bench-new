# Source mix report

Milestone 0 inventory: what fraction of each guide's facts could be regenerated from the local OpenAPI fixture versus facts that exist only in prose.

- OpenAPI: `data/content_engine/specs/payments-core.openapi.json`
- Guides sampled: 40
- Overall spec-backed share: **74.1%**
- Overall prose-only share: **25.9%**
- Decision rule outcome: spec-primary: generate endpoint pages from OpenAPI; DocETL mines prose only for gaps

## Per-guide table

| Guide | Spec-backed | Prose-only | Spec hits | Prose hits | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| credentials | 78.3% | 21.7% | 18 | 5 | — |
| en-us_apple-pay_developer_all_rest_applepay_applepay-getting-started | 100.0% | 0.0% | 1 | 0 | — |
| en-us_click-to-pay_developer_all_rest_click-to-pay_ctp-getting-started-cs-setup-intro | 100.0% | 0.0% | 7 | 0 | — |
| en-us_click-to-pay_developer_all_rest_click-to-pay_ctp-getting-started-ss-setup | 70.0% | 30.0% | 7 | 3 | index-like; mostly navigation / revision surface |
| en-us_click-to-pay_developer_all_rest_click-to-pay_ctp-tokens-intro | 80.0% | 20.0% | 12 | 3 | — |
| en-us_click-to-pay_developer_all_rest_click-to-pay_uc-token-get-pymnt-credentials | 90.0% | 10.0% | 9 | 1 | — |
| en-us_click-to-pay_developer_all_rest_click-to-pay_uc-token-get-pymnt-details | 88.9% | 11.1% | 8 | 1 | — |
| en-us_cp-retail_integration_ctv_rest_cp-retail_cp-payment-services-intro | 100.0% | 0.0% | 4 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials | 78.3% | 21.7% | 18 | 5 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-cit-intro | 80.0% | 20.0% | 4 | 1 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-delay-intro | 100.0% | 0.0% | 1 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-incremental-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-install-intro | 50.0% | 50.0% | 1 | 1 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-intro | 83.3% | 16.7% | 10 | 2 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-mc-subscription-intro | 100.0% | 0.0% | 1 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-mit-stand-order-intro | 100.0% | 0.0% | 1 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-noshow-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-reauth-intro | 100.0% | 0.0% | 2 | 0 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-recur-intro | 66.7% | 33.3% | 2 | 1 | — |
| en-us_credentials_developer_ctv_rest_credentials_credentials-resub-intro | 100.0% | 0.0% | 3 | 0 | — |
| en-us_additional-amount-types_reference_all_na_additional-amount-types | 100.0% | 0.0% | 3 | 0 | — |
| en-us_batch_user_all_so_batch-upload_batch-results-txns-rpt-request | 100.0% | 0.0% | 2 | 0 | — |
| en-us_boarding_developer_all_rest_boarding_boarding-manage-org-intro | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_cp-retail_integration_ctv_rest_cp-retail_dcc-intro | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_doc-rel_relnote_all_na_doc-release-notes_doc-release-notes-intro_December-2025_sis-pax-25-12 | 83.3% | 16.7% | 5 | 1 | — |
| en-us_echeck_user_all_rest_echeck-user-guide_echeck-reports-use-case | 100.0% | 0.0% | 6 | 0 | — |
| en-us_installment-plans_developer_all_rest_installment-plans | 76.0% | 24.0% | 19 | 6 | — |
| en-us_lodging_developer_ctv_rest_lodging_lodging-trxn-types | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_pax-all-in-one_integration_all_na_pax-all-in-one_pax-aio-release-notes-intro | 81.8% | 18.2% | 9 | 2 | — |
| en-us_paybylink_developer_all_rest_paybylink_paybylink-intro | 87.5% | 12.5% | 7 | 1 | — |
| en-us_pin-debit_developer_ctv_rest_pin-debit_pd-processing | 100.0% | 0.0% | 2 | 0 | — |
| en-us_platform_relnote_all_na_rn-2025-09-05_rn-general | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_platform_relnote_all_na_rn-2026-01-02_rn-general | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_platform_relnote_all_na_rn-2026-04-10_rn-general | 0.0% | 100.0% | 0 | 0 | no classifiable signals |
| en-us_recurring-billing_user_all_rest_recurring-billing-user_recur-bill-services-intro | 75.0% | 25.0% | 3 | 1 | — |
| en-us_sa_developer_all_sa-checkout_secure-acceptance | 77.4% | 22.6% | 24 | 7 | index-like; mostly navigation / revision surface |
| en-us_state-codes_reference_all_na_state-codes | 100.0% | 0.0% | 4 | 0 | — |
| en-us_tap-to-phone_integration_all_rest_tap-to-phone_ttp-release-notes-intro | 81.8% | 18.2% | 9 | 2 | — |
| en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn | 50.0% | 50.0% | 1 | 1 | — |
| en-us_txn-search_developer_all_rest_txn-search | 85.0% | 15.0% | 17 | 3 | index-like; mostly navigation / revision surface |

## Top 10 prose-only sections for a first integration

_No prose-dominant sections found in the sample._
