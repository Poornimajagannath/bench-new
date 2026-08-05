Services Returned by the API {#txn-applications}
================================================

The Transaction Details API response contains an applications array that lists the services that processed the request. The table below lists all the services that can be returned by the Transaction Search and Details APIs.

| Application                     | Description                                      |
|:--------------------------------|:-------------------------------------------------|
| ics_score                       | Advanced Fraud Screen                            |
| ics_ap_auth                     | Alt Pay Authorization                            |
| ics_ap_auth_reversal            | Alt Pay Authorization Reversal                   |
| ics_ap_billing_agreement        | Alt Pay Billing Agreement                        |
| ics_ap_cancel                   | Alt Pay Cancel                                   |
| ics_ap_capture                  | Alt Pay Capture                                  |
| ics_ap_initiate                 | Alt Pay Initiate                                 |
| ics_ap_options                  | Alt Pay Options                                  |
| ics_ap_order                    | Alt Pay Order                                    |
| ics_ap_refund                   | Alt Pay Refund                                   |
| ics_ap_sale                     | Alt Pay Sale                                     |
| ics_ap_sessions                 | Alt Pay Session                                  |
| ics_ap_check_status             | Alt Pay Service Status                           |
| ics_auto_auth_reversal          | Automatic Authorization Reversal                 |
| ics_bank_transfer               | Bank Transfer                                    |
| ics_bank_transfer_real_time     | Bank Transfer Real Time                          |
| ics_bank_transfer_refund        | Bank Transfer Refund                             |
| ics_bin_lookup                  | BIN Lookup Service                               |
| ics_boleto_payment              | Boleto Payment                                   |
| ics_auth                        | Card Authorization                               |
| ics_auth_reversal               | Card Full Authorization Reversal                 |
| ics_bill                        | Card Settlement                                  |
| ics_credit                      | Card Credit                                      |
| ics_cm_action                   | Case Management Action                           |
| ics_china_payment               | China Payment                                    |
| ics_china_refund                | China Refund                                     |
| ics_auto_full_auth_reversal     | Credit Card Auto Full Authorization Reversal     |
| ics_auth_refresh                | Credit Card System Authorization                 |
| ics_credit_auth                 | Credit Card Credit Authorization                 |
| ics_risk_update                 | Customer List Modification                       |
| ics_dcc                         | DCC Lookup                                       |
| ics_dcc_update                  | DCC Update                                       |
| ics_decision                    | Decision Manager                                 |
| ics_dm_event                    | Decision Manager Events                          |
| ics_direct_debit                | Direct Debit                                     |
| ics_direct_debit_mandate        | Direct Debit Mandate                             |
| ics_direct_debit_refund         | Direct Debit Refund                              |
| ics_direct_debit_validate       | Direct Debit Validation                          |
| ics_ecp_authenticate            | Electronic Check Authenticate                    |
| ics_ecp_credit                  | Electronic Check Credit                          |
| ics_ecp_debit                   | Electronic Check Debit                           |
| ics_ecp_avs                     | Electronic Check Account Validation              |
| ics_get_masterpass_data         | Get MasterPass Data                              |
| ics_get_visa_checkout_data      | Get `Visa Click to Pay`                          |
| ics_create_isv                  | Gift Certificate Creation                        |
| ics_get_isv_history             | Gift Certificate History                         |
| ics_add_value_to_isv            | Gift Certificate Increase                        |
| ics_get_isv_info                | Gift Certificate Information                     |
| ics_modify_isv                  | Gift Certificate Modification                    |
| ics_get_isv_profiles            | Gift Certificate Profiles                        |
| ics_redeem_isv                  | Gift Certificate Redemption                      |
| ics_gift_card_activation        | Gift Card Activation Service                     |
| ics_gift_card_balance_inquiry   | Gift Card Balance Inquiry Service                |
| ics_gift_card_redemption        | Gift Card Redemption Service                     |
| ics_gift_card_refund            | Gift Card Refund Service                         |
| ics_gift_card_reload            | Gift Card Reload Service                         |
| ics_gift_card_reversal          | Gift Card Reversal Service                       |
| ics_gift_card_void              | Gift Card Void Service                           |
| ics_gift_card_timeout_reversal  | Gift Card Timeout Reversal Service               |
| ics_ifs_setup                   | IFS Setup                                        |
| ics_ifs_update                  | IFS Update                                       |
| ics_incremental_auth            | Incremental Authorization                        |
| ics_ipgeo                       | IP Geolocation                                   |
| ics_oct                         | Original Credit Transaction                      |
| ics_pa_setup                    | Payer Authentication Setup                       |
| ics_pa_enroll                   | Payer Authentication Enrollment                  |
| ics_pa_validate                 | Payer Authentication Validation                  |
| ics_authentication_exemptions   | Visa Exemption Service                           |
| paypal_mip_agreement_ipn        | PayPal Billing Agreement                         |
| ics_paypal_button_create        | PayPal Button Create                             |
| ics_paypal_credit               | PayPal Credit                                    |
| ics_paypal_authorization        | PayPal Express Checkout Authorization            |
| ics_paypal_create_agreement     | PayPal Express Checkout Billing Agreement Create |
| ics_paypal_update_agreement     | PayPal Express Checkout Billing Agreement Update |
| ics_paypal_ec_order_setup       | PayPal Express Checkout Order Setup              |
| ics_paypal_auth_reversal        | PayPal Express Checkout Auth Reversal            |
| ics_paypal_ec_do_payment        | PayPal Express Checkout Do Payment               |
| ics_paypal_do_ref_transaction   | PayPal Express Checkout Do Reference             |
| ics_paypal_refund               | PayPal Express Checkout Refund                   |
| ics_paypal_do_capture           | PayPal Express Checkout Settlement               |
| paypal_ipn                      | PayPal Payment                                   |
| ics_paypal_preapproved_payment  | PayPal Preapproved Payment                       |
| ics_pin_debit_credit            | PIN Debit Credit                                 |
| ics_pin_debit_purchase          | PIN Debit Purchase                               |
| ics_pin_debit_reversal          | PIN Debit Reversal                               |
| ics_timeout_pin_debit_reversal  | PIN Debit Timeout Reversal                       |
| ics_pinless_debit               | PINless Debit                                    |
| ics_pinless_debit_validate      | PINless Debit Validation                         |
| ics_pinless_debit_reversal      | PINless Debit Reversal                           |
| ics_export                      | Product Export Verification                      |
| ics_service_fee_auth            | Service Fee Authorization                        |
| ics_service_fee_auth_reversal   | Service Fee Authorization Reversal               |
| ics_service_fee_bill            | Service Fee Settlement                           |
| ics_service_fee_credit          | Service Fee Credit Card Credit                   |
| ics_service_fee_ecp_credit      | Service Fee eCheck Credit                        |
| ics_service_fee_ecp_debit       | Service Fee eCheck Debit                         |
| ics_pay_subscription_create     | Subscription Creation                            |
| ics_pay_subscription_create_dup | Subscription Creation Duplicates                 |
| ics_pay_subscription_delete     | Subscription Delete                              |
| ics_pay_subscription_update     | Subscription Modification                        |
| ics_dav                         | Shipping Address Verification                    |
| ics_download                    | Software Download URL                            |
| ics_tax                         | Tax Calculation                                  |
| ics_timeout_auth_reversal       | Timeout Auth Reversal                            |
| ics_timeout_oct_reversal        | Timeout OCT Reversal                             |
| ics_void                        | Voided Transactions                              |
| ics_auto_void_auth_reversal     | Authorization Reversal after Void                |
| ics_pay_subscription_retrieve   | Subscription Retrieval                           |
| ics_ap_create_mandate           | Alt Pay Direct Debit - Create Mandate            |
| ics_ap_update_mandate           | Alt Pay Direct Debit - Update Mandate            |
| ics_ap_import_mandate           | Alt Pay Direct Debit - Import Mandate            |
| ics_ap_revoke_mandate           | Alt Pay Direct Debit - Revoke Mandate            |
| ics_ap_mandate_status           | Alt Pay Direct Debit - Mandate status            |
[Applications Returned by the API]

