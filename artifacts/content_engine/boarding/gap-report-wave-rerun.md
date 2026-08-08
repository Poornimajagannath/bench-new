# Wave 2 boarding — gap report (post endpoint extraction)

Generated: 2026-08-08T04:22:03+00:00

## The headline finding that changed shape

**1. Stated outcomes are still mostly missing after API extraction.** Of **277** sequence steps across the six composed workflows (API operations + UI steps), **215** have no stated outcome (denominator: 277 steps; source: `composed workflow sequence_stats (API ops + UI steps; expected outcome Gap markers)`). Prior Wave 2 figure was 220/257 (Measured before endpoint extraction; UI-only step count.). Sequence mix: 20 API ops + 257 UI steps.

- API ops in sequence: **20** (source: composition sequence_stats)
- UI steps in sequence: **257**
- Outcome gaps: **215/277**

## Per workflow

| Workflow | Steps | Outcome gaps | API ops | UI steps |
|---|---:|---:|---:|---:|
| create-merchant-organization | 34 | 27 | 3 | 31 |
| extend-hierarchy | 34 | 29 | 1 | 33 |
| enable-configure-products | 189 | 145 | 11 | 178 |
| search-organizations | 14 | 9 | 4 | 10 |
| change-organization-status | 4 | 3 | 1 | 3 |
| send-registration-email | 2 | 2 | 0 | 2 |

---

# Developers can see the endpoint and still cannot call it

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: `api_reference.extract_api_reference_claims over raw/product-roots`).

- Missing Required Fields: **57** / 176
- Missing REST Example: **17** / 176
- Missing both: **16** / 176

## Endpoints with no Required Fields list

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-structural-api |
| boarding | `GET` | `/oms/v1/organizations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-information-api |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-auth-enable-intro |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#ctp-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-enable-intro |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-auth-enable-intro |
| digital-accept-flex | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#ctp-token-get-pymnt-credentials |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-auth-tokens |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#da-processing-auth-token-task |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-auth-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-amex-intro_section_kl3_tbh_xwb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-device-tkn-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tap-create-ii-intro |
| tms | `DELETE` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-delete-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-intro |
| tms | `PATCH` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-update-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-pi-intro |
| tms | `DELETE` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-delete-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-all-intro |
| tms | `PATCH` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-update-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-create-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-add-nondefault-addr-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-cust-pi-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-create-trans-token-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| tms | `DELETE` | `/tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ctf-delete-binding-intro |
| unified-checkout | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-token-get-pymnt-details |
| unified-checkout | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-auth-tokens |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints with no REST Example

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| invoicing | `POST` | `/invoicing/v2/invoices` | https://developer.cybersource.com/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.html#invoicing-services-create-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints missing both

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |
