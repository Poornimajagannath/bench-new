# Enable and Configure Products

<!-- section:prose -->
Enable products for a merchant during or after onboarding (BRS invokes PECS.

PECS updates after).
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth:prose:58bfc6580728`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth.md.md
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth:prose:a4431adf9e91`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth.md.md
- Must be in the format `http://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields:prose:452b05be0057`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields.md.md
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms:prose:00452a944a4e`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms.md.md
- Having a TRID is a prerequisite for enabling network tokenization.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:prose:bf5e52f8feb7`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids.md.md
- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth:prose:58bfc6580728`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth.md.md
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth:prose:a4431adf9e91`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth.md.md
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms:prose:00452a944a4e`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms.md.md
- IMPORTANT You must include this field for all card types configured for the processor.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor_pecs-add-delete-processor-req-fields:prose:477d5afd2eaa`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor_pecs-add-delete-processor-req-fields.md.md
- IMPORTANT You must include this field for all card types configured for the processor.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor_pecs-delete-processor-req-fields:prose:477d5afd2eaa`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor_pecs-delete-processor-req-fields.md.md
- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL is in the format `https://www.example.com`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth:prose:609b36db9ed6`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth.md.md
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth:prose:a4431adf9e91`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth.md.md
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms:prose:00452a944a4e`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms.md.md
- Having a TRID is a prerequisite for enabling network tokenization.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:prose:bf5e52f8feb7`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids.md.md

## Steps

### REST API path

1. **API:** `POST /boarding/v1/registrations` — Enable `Payer Authentication`
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.administrativeArea`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.address.postalCode`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.businessContact.websiteUrl`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-website-url.md) — Must be in the format `http://www.example.com`.
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set to `false`.
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md)
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set to `TRANSACTING`.
     - [`registrationInformation.boardingFlow`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md) — Set to `ADDPRODUCT`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-4.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-10.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.requestorId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-8.md) — Discover/Diners Club ProtectBuy-Specific Fields -----------------------------------------------
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-17.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-23.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-29.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.securePasswordForJCB`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-30.md) — Mastercard/Meeza Identity Check-Specific Fields -----------------------------------------------
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-36.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-42.md) — Set to `true`.
     - [`productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-48.md) — Set to `true`.
   - Example request:
     ```json
     {
       "registrationInformation": {
         "boardingFlow": "ADDPRODUCT"
       },
       "organizationInformation": {
         "organizationId": "apitester00",
         "parentOrganizationId": "nishtx",
         "type": "TRANSACTING",
         "configurable": false,
         "businessInformation": {
           "address": {
             "country": "US",
             "address1": "123 Main",
             "postalCode": "99999",
             "administrativeArea": "WA",
             "locality": "Seattle"
           },
           "businessContact": {
             "firstName": "Jane",
             "lastName": "Smith",
             "phoneNumber": "5551234567",
             "email": "email@domain.com"
           },
           "name": "Test Merchant",
           "websiteUrl": "https://www.example.com"
         }
       },
       "productInformation": {
         "selectedProducts": {
           "payments": {
             "payerAuthentication": {
               "configurationInformation": {
                 "configurations": {
                   "cardTypes": {
                     "amexSafeKey": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "12345678901-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "CB": {
                       "requestorId": "",
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "211111-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "dinersClubInternationalProtectBuy": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "311111-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "ELO": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "11111111-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "jCBJSecure": {
                       "securePasswordForJCB": "jcbpass",
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "123456-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "masterCardSecureCode": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "522222-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "UPI": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "611111-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     },
                     "verifiedByVisa": {
                       "enabled": true,
                       "currencies": [
                         {
                           "currencyCodes": ["ALL"],
                           "acquirerId": "411111-1000",
                           "processorMerchantId": "procmerch123"
                         }
                       ]
                     }
                   }
                 }
               }
             }
           }
         }
       }
     }
     ```
   - Expected outcome: Response status `PROCESSING` (see example response).
   - Example response:
     ```json
     {
       "id": "87304104004",
       "submitTimeUtc": "2024-05-14T15:53:19Z",
       "status": "PROCESSING",
       "registrationInformation": {
         "mode": "COMPLETE",
         "boardingPackageId": "190303004"
       },
       "organizationInformation": {
         "organizationId": "apitester00",
         "parentOrganizationId": "nishtx"
       },
       "message": "Request is being processed"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:0817e1d1`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-payer-auth-enable-intro)</sub>

2. **API:** `POST /boarding/v1/registrations` — Enable `Token Management Service` Using a Template
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.administrativeArea`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.address.postalCode`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set to `false`.
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md)
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set to `TRANSACTING`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation.templateId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-tem.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.subscriptionInformation.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-sub-enab.md) — Set to `true` to enable `Token Management Service`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.subscriptionInformation.selfServiceability`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-sub-self.md)
     - [`registrationInformation.boardingFlow`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md) — Set to `ADDPRODUCT`.
   - Example request:
     ```json
     {
       "registrationInformation": {
         "boardingFlow": "ADDPRODUCT"
       },
       "organizationInformation": {
         "parentOrganizationId": "3b2bwnhbm7cdzath0qcn0luhkpvb",
         "type": "TRANSACTING",
         "configurable": false,
         "businessInformation": {
           "name": "Test Merchant",
           "address": {
             "country": "US",
             "address1": "123 Main",
             "locality": "Seattle",
             "administrativeArea": "WA",
             "postalCode": "99999"
           },
           "businessContact": {
             "firstName": "Jane",
             "lastName": "Smith",
             "phoneNumber": "5551234567",
             "email": "email@domain.com"
           }
         }
       },
       "productInformation": {
         "selectedProducts": {
           "commerceSolutions": {
             "tokenManagement": {
               "subscriptionInformation": {
                 "enabled": true,
                 "selfServiceability": "NOT_SELF_SERVICEABLE"
               },
               "configurationInformation": {
                 "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
               }
             }
           }
         }
       }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - Example response:
     ```json
     {
       "id": "94498504004",
       "submitTimeUtc": "2024-07-01T16:25:20Z",
       "status": "SUCCESS",
       "registrationInformation": {
         "mode": "COMPLETE",
         "boardingPackageId": "1168704004"
       },
       "organizationInformation": {
         "organizationId": "{MerchantAccountOrgId}",
         "parentOrganizationId": "{PortfolioOrgId}"
       },
       "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:f562c266`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-tms-enable-intro)</sub>

3. **API:** `POST /boarding/v1/registrations` — Enable `TMS` and Enroll in Network Tokenization for a New Merchant
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.defaultTokenType`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-vau.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.location`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-21.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.sensitivePrivileges.cardNumberMaskingFormat`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-22.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.customer`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-23.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierBankAccount`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-24.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierCard`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-25.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.paymentInstrument`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-26.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-net.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerMerchantId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--0.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--1.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--2.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.doingBusinessAs`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--4.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--5.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices. mastercardDigitalEnablementService.enrollment`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-13.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices.visaTokenService.enrollment`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-18.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.websiteUrl`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--3.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableService`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-12.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableTransactionalTokens`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-11.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.notifications.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-15.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.paymentCredentials.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-10.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableService`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-17.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableTransactionalTokens`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-16.md) — Set to `true`.
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.administrativeArea`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.address.postalCode`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set to `true`.
     - [`organizationInformation.organizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-organization-id.md)
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md)
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set to `MERCHANT`.
     - [`registrationInformation.boardingFlow`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md) — Set to `ADDPRODUCT`.
   - Example request:
     ```json
     {
       "registrationInformation": {
         "boardingFlow": "ENTERPRISE"
       },
       "organizationInformation": {
         "organizationId": "yourmerchantorgidhere",
         "parentOrganizationId": "yourportfolioorgidhere",
         "type": "MERCHANT",
         "configurable": true,
         "businessInformation": {
           "name": "NetworkTokenMerchant",
           "address": {
             "country": "US",
             "address1": "123456 SandMarket",
             "locality": "ORMOND BEACH",
             "administrativeArea": "FL",
             "postalCode": "32176"
           },
           "websiteUrl": "https://www.NetworkTokenMerchant.com",
           "businessContact": {
             "firstName": "Token",
             "lastName": "Man",
             "phoneNumber": "6574567813",
             "email": "networktokenman@visa.com"
           }
         }
       },
       "productInformation": {
         "selectedProducts": {
           "commerceSolutions": {
             "tokenManagement": {
               "subscriptionInformation": {
                 "enabled": true
               },
               "configurationInformation": {
                 "configurations": {
                   "vault": {
                     "location": "GDC",
                     "defaultTokenType": "CUSTOMER",
                     "tokenFormats": {
                       "customer": "32_HEX",
                       "paymentInstrument": "32_HEX",
                       "instrumentIdentifierCard": "19_DIGIT_LAST_4",
                       "instrumentIdentifierBankAccount": "32_HEX"
                     },
                     "sensitivePrivileges": {
                       "cardNumberMaskingFormat": "FIRST_6_LAST_4"
                     },
                     "networkTokenServices": {
                       "notifications": {
                         "enabled": true
                       },
                       "paymentCredentials": {
                         "enabled": true
                       },
                       "synchronousProvisioning": {
                         "enabled": false
                       },
                       "visaTokenService": {
                         "enableService": true,
                         "enableTransactionalTokens": true
                       },
                       "mastercardDigitalEnablementService": {
                         "enableService": true,
                         "enableTransactionalTokens": true
                       }
                     }
                   },
                   "networkTokenEnrollment": {
                     "businessInformation": {
                       "name": "NetworkTokenMerchant",
                       "doingBusinessAs": "NetworkTokenCo1",
                       "address": {
                         "country": "US",
                         "locality": "ORMOND BEACH"
                       },
                       "websiteUrl": "https://www.NetworkTokenMerchant.com",
                       "acquirer": {
                         "acquirerId": "40010052242",
                         "acquirerMerchantId": "MerchantOrgID"
                       }
                     },
                     "networkTokenServices": {
                       "visaTokenService": {
                         "enrollment": true
                       },
                       "mastercardDigitalEnablementService": {
                         "enrollment": true
                       }
                     }
                   }
                 }
               }
             }
           }
         }
       }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - Example response:
     ```json
     {
       "id": "94498504004",
       "submitTimeUtc": "2024-07-01T16:25:20Z",
       "status": "SUCCESS",
       "registrationInformation": {
         "mode": "COMPLETE",
         "boardingPackageId": "1168704004"
       },
       "organizationInformation": {
         "organizationId": "{MerchantAccountOrgId}",
         "parentOrganizationId": "{PortfolioOrgId}"
       },
       "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:b8f6e30d`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-tms-enable-net-tkn-intro)</sub>

4. **API:** `POST /boarding/v1/registrations` — Enable `TMS` and Enroll in Network Tokenization for an Existing Merchant
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md)
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set to `MERCHANT`.
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set to `true`.
     - [`registrationInformation.boardingFlow`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md) — Set to `ADDPRODUCT`.
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.postalCode`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md)
     - [`organizationInformation.businessInformation.address.administrativeArea`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.organizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-organization-id.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.location`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-21.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.defaultTokenType`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-vau.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.customer`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-23.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.paymentInstrument`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-26.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierCard`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-25.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.tokenFormats.instrumentIdentifierBankAccount`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-24.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.vault.sensitivePrivileges.cardNumberMaskingFormat`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-22.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--5.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.doingBusinessAs`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--4.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--1.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--2.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.websiteUrl`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--3.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-net.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement.configurationInformation. configurations.networkTokenEnrollment.businessInformation.acquirer.acquirerMerchantId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf--0.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices.visaTokenService.enrollment`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-18.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenEnrollment.networkTokenServices. mastercardDigitalEnablementService.enrollment`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-13.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.notifications.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-15.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.paymentCredentials.enabled`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-10.md)
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableService`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-17.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.visaTokenService.enableTransactionalTokens`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-16.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableService`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-12.md) — Set to `true`.
     - [`productInformation.selectedProducts.commerceSolutions.tokenManagement. configurationInformation.configurations.networkTokenServices.mastercardDigitalEnablementService.enableTransactionalTokens`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-commerce-sol-tkn-mgmnt-conf-11.md) — Set to `true`.
   - Example request:
     ```json
     {
        "registrationInformation":{
           "boardingFlow":"ADDPRODUCT"
        },
        "organizationInformation":{
           "organizationId":"yourmerchantorgidhere",
           "parentOrganizationId":"yourportfolioorgidhere",
           "type":"MERCHANT",
           "configurable":true,
           "businessInformation":{
              "name":"TokenMerchant",
              "address":{
                 "country":"US",
                 "address1":"123456 SandMarket",
                 "locality":"ORMOND BEACH",
                 "administrativeArea":"FL",
                 "postalCode":"32176"
              },
              "websiteUrl":"https://www.MerchantUrlHere.com",
              "businessContact":{
                 "firstName":"Token",
                 "lastName":"Man",
                 "phoneNumber":"6574567813",
                 "email":"tokenman@visa.com"
              }
           }
        },
        "productInformation":{
           "selectedProducts":{
              "commerceSolutions":{
                 "tokenManagement":{
                    "subscriptionInformation":{
                       "enabled":true
                    },
                    "configurationInformation":{
                       "configurations":{
                             "vault":{
                             "location": "GDC",
                             "defaultTokenType":"CUSTOMER",
                             "tokenFormats":{
                                "customer":"32_HEX",
                                "paymentInstrument":"32_HEX",
                                "instrumentIdentifierCard":"19_DIGIT_LAST_4",
                                "instrumentIdentifierBankAccount":"32_HEX"
                             },
                             "sensitivePrivileges":{
                                "cardNumberMaskingFormat":"FIRST_6_LAST_4"
                             }                     },
                          "networkTokenEnrollment":{
                             "businessInformation":{
                                "name":"TokenMerchant",
                                "doingBusinessAs":"NetworkTokenCo1",
                                "address":{
                                   "country":"US",
                                   "locality":"ORMOND BEACH"
                                },
                                "websiteUrl":"https://www.MerchantUrlHere.com",
                                "acquirer":{
                                   "acquirerId":"40010052242",
                                   "acquirerMerchantId":"yourmerchantorgidhere"
                                }
                             },
                             "networkTokenServices":{
                                "visaTokenService":{
                                   "enrollment":true
                                },
                                "mastercardDigitalEnablementService":{
                                   "enrollment":true
                                }
                             }
                          },
                             "networkTokenServices":{
                                "notifications":{
                                   "enabled":true
                                },
                                "paymentCredentials":{
                                   "enabled":true
                                },
                                "visaTokenService":{
                                   "enableService":true,
                                   "enableTransactionalTokens":true
                                },
                                "mastercardDigitalEnablementService":{
                                   "enableService":true,
                                   "enableTransactionalTokens":true
                                }
                             }
                       }
                    }
                 }
              }
           }
        }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - Example response:
     ```json
     {
       "id": "94498504004",
       "submitTimeUtc": "2024-07-01T16:25:20Z",
       "status": "SUCCESS",
       "registrationInformation": {
         "mode": "COMPLETE",
         "boardingPackageId": "1168704004"
       },
       "organizationInformation": {
         "organizationId": "{MerchantAccountOrgId}",
         "parentOrganizationId": "{PortfolioOrgId}"
       },
       "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:c7cc2d57`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-tms-enable-net-tkn-existing-intro)</sub>

5. **API:** `POST /products/v1/product-setups` — Add a New Product to an Existing Organization
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:4908017a`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api)</sub>

6. **API:** `POST /products/v1/product-setups` — Update Batch Group Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:97973906`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch)</sub>

7. **API:** `POST /products/v1/product-setups` — Add a Processor Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:a3c2ae2f`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor)</sub>

8. **API:** `POST /products/v1/product-setups` — Delete a Processor Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:decc31ed`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor)</sub>

9. **API:** `POST /products/v1/product-setups` — Add and Delete a Processor Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:10df3c29`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor)</sub>

10. **API:** `POST /products/v1/product-setups` — Configure `Payer Authentication` Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request: **Gap:** no REST Example request in the source.
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:199873b9`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth)</sub>

11. **API:** `POST /products/v1/product-setups` — Enable `TMS` with a Template Using the PECS API
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields: **Gap:** not listed for this endpoint in the source.
   - Example request:
     ```json
     {
       "organizationId": "ergaergaerg001",
       "commerceSolutions": {
         "tokenManagement": {
           "subscriptionInformation": {
             "enabled": true,
             "selfServiceability": "NOT_SELF_SERVICEABLE"
           },
           "configurationInformation": {
             "templateId": "43107BC1-E3DA-4019-9306-4510AD4DE05F"
           }
         }
       }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - Example response:
     ```json
     {
       "setups": {
         "commerceSolutions": {
           "tokenManagement": {
             "configurationStatus": {
               "status": "SUCCESS",
               "message": "Profile Assigned Successfully"
             },
             "subscriptionStatus": {
               "status": "SUCCESS",
               "message": "success"
             }
           }
         }
       },
       "status": "PROCESSED",
       "submitTimeUtc": "2022-06-03T08:46:13+0000"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:ea27ebb1`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro)</sub>

### Business Center UI path

12. **Action:** Navigate to Token Management.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:1:bf5226ae`</sub>

13. **Action:** Click Vault Management.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:2:8989bba2`</sub>

14. **Action:** Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:3:7be4cbc4`</sub>

15. **Action:** Choose the merchant account to view the `TMS` vaults that are configured for the merchant.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:4:febc62c5`</sub>

16. **Action:** Click Network Tokenization.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:5:681c8223`</sub>

17. **Action:** Click Enroll to VISA/Mastercard token services.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:6:af861b97`</sub>

18. **Action:** Enter the required information for each card type:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:7:bcfd9129`</sub>

19. **Action:** Click Onboard with Acquirer ID.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:8:07eadfa0`</sub>

20. **Action:** Enter the required information:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:9:d937e717`</sub>

21. **Action:** Click Enroll to Network Token Services to complete enrollment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:10:e629cfe3`</sub>

22. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:1:82047b1f`</sub>

23. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:2:844c6600`</sub>

24. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:3:c84c8ce9`</sub>

25. **Action:** Select the vault owner that you want to configure from the Vault Owner drop-down list.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:4:983ce7a5`</sub>

26. **Action:** In the Details column, click Access Settings. The MID Access page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The MID Access page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:5:e0377d5e`</sub>

27. **Action:** Check the box for the vault settings you want to enable for each merchant you want to configure:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:6:be525cc3`</sub>

28. **Action:** Click Submit to save your settings.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:7:d1339209`</sub>

29. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:1:9af7cbce`</sub>

30. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:2:23a5cb4a`</sub>

31. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:3:15d16a36`</sub>

32. **Action:** From the Vault Owner drop-down list, select the vault owner..
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:4:206c6907`</sub>

33. **Action:** In the Details column, click Vault Settings. The Edit Vault page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Edit Vault page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:5:021ba039`</sub>

34. **Action:** Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:7:4ee26959`</sub>

35. **Action:** To return to the vault management page, click VAULT MANAGEMENT.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:9:ffdbb17a`</sub>

36. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:1:801c6574`</sub>

37. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:2:46c4bc64`</sub>

38. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:3:6d4e39f8`</sub>

39. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:4:ae51b6ec`</sub>

40. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:5:d2542426`</sub>

41. **Action:** Under Payments, select Alternative Payments and click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:6:3bdd2506`</sub>

42. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:7:1afa1e26`</sub>

43. **Action:** Click Continue. The Product Configuration page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:8:9535a452`</sub>

44. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:9:abe72a95`</sub>

45. **Action:** Click Continue to return to the Merchant Details page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:10:400bae13`</sub>

46. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:1:3be597a6`</sub>

47. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:2:81e9a752`</sub>

48. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:3:d47b0824`</sub>

49. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:4:2bc24e44`</sub>

50. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:5:1c503020`</sub>

51. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:6:ec52c350`</sub>

52. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:7:f283b6ad`</sub>

53. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:8:321fccca`</sub>

54. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:9:c8966550`</sub>

55. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:10:92c9fcb4`</sub>

56. **Action:** Under Product Enablement, find Alternative Payments and select Allow Self Enablement under the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:11:eb957f7b`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding-self.html#boarding-config-altpay-boarding-self_boarding-config-altpay-boarding-self-step8)</sub>

57. **Action:** Click Save. Alternative Payments is now available for self-enablement for the merchant.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:12:7d3fb96a`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding-self.html#boarding-config-altpay-boarding-self_boarding-config-altpay-boarding-self-step9)</sub>

58. **Action:** In the left navigation panel, click **Portfolio Management**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:1:84efa501`</sub>

59. **Action:** Under Merchants, click **Manage Merchants**. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:2:44b8c90a`</sub>

60. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:3:d8f30e44`</sub>

61. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:4:55661281`</sub>

62. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:5:70dcb843`</sub>

63. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:6:74e4ca33`</sub>

64. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:7:3a5e1999`</sub>

65. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:8:c87239f4`</sub>

66. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:9:4ff18883`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step6)</sub>

67. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:10:19ff732e`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step7)</sub>

68. **Action:** Under Product Enablement, find Alternative Payments and select Enabled under the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:11:5617dc0d`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step8)</sub>

69. **Action:** Click Configure. The Configure Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:12:d6164c48`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step9)</sub>

70. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:13:6c53b944`</sub>

71. **Action:** Click Continue. The Product Configuration page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:14:a142b937`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step11)</sub>

72. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:15:e3a6f564`</sub>

73. **Action:** Click Continue to return to the Merchant Details page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:16:661e57a2`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-altpay/boarding-config-altpay-boarding.html#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step13)</sub>

74. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:1:e9ace8fd`</sub>

75. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:2:6fb27c98`</sub>

76. **Action:** Search for the organization in the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:3:33fe6b52`</sub>

77. **Action:** Find the organization in the Search Results table and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:4:605c9886`</sub>

78. **Action:** Under Products, click Edit next to Alternative Payments. The Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:5:f27e4448`</sub>

79. **Action:** If you want to add an available alternative payment method, click Add Services. The Configure Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:6:412b436b`</sub>

80. **Action:** If you want to configure an enabled alternative payment method, click Edit. The Configure Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:7:d6587764`</sub>

81. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:8:52d5d495`</sub>

82. **Action:** Click Continue. The Product Configuration page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:9:f17a52e6`</sub>

83. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:10:c999b66a`</sub>

84. **Action:** Click Continue to return to the Merchant Details page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:11:86fe1995`</sub>

85. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:1:26970f70`</sub>

86. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:2:09859f03`</sub>

87. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:3:c953ad31`</sub>

88. **Action:** Select the product you want to enable. Click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:4:0c01db28`</sub>

89. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:1:315e4918`</sub>

90. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:2:5854d539`</sub>

91. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:3:3982b537`</sub>

92. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:4:a134be58`</sub>

93. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:5:23765ebd`</sub>

94. **Action:** Select Payer Authentication and click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:6:4a7a2bea`</sub>

95. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:7:a2e6d18f`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-payer-auth/boarding-config-payer-auth-add.html#config-payer-auth-add_config-payer-auth-add-step1)</sub>

96. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:8:de695665`</sub>

97. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:9:e6f976aa`</sub>

98. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:10:42400b21`</sub>

99. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:11:ae6ad600`</sub>

100. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:12:440e2e63`</sub>

101. **Action:** Click the trash can icon to delete a configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:13:4d90f8de`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-payer-auth/boarding-config-payer-auth-add.html#config-payer-auth-add_config-payer-auth-add-step7)</sub>

102. **Action:** Click View all currencies to collapse or expand all currencies that are configured.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:14:40ef0a0a`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-payer-auth/boarding-config-payer-auth-add.html#config-payer-auth-add_config-payer-auth-add-step8)</sub>

103. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:15:0c1a13af`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-payer-auth/boarding-config-payer-auth-add.html#config-payer-auth-add_config-payer-auth-add-step9)</sub>

104. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:16:94e1f492`</sub>

105. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:1:4c3bdc86`</sub>

106. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:2:c0b28e96`</sub>

107. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:3:90633964`</sub>

108. **Action:** Choose a location to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:4:2d4175cd`</sub>

109. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:5:bcbd02a6`</sub>

110. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:6:99c6b97f`</sub>

111. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:7:b3bd5964`</sub>

112. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:8:51ff745b`</sub>

113. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:9:8529de0b`</sub>

114. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:10:ee903114`</sub>

115. **Action:** Under Product Enablement, find `Payer Authentication` and select Enabled from the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:11:076dbff0`</sub>

116. **Action:** Click Configure to configure `Payer Authentication`.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:12:b3c2d975`</sub>

117. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:13:30bb71b4`</sub>

118. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:14:d1ede173`</sub>

119. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:15:cce02f71`</sub>

120. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:16:b99ed1bf`</sub>

121. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:17:710e913b`</sub>

122. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:18:05b9d6de`</sub>

123. **Action:** Click the trash can icon to delete a configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:19:9161d2bc`</sub>

124. **Action:** Click View all currencies to collapse or expand all currencies that are configured.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:20:66247b5f`</sub>

125. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:21:cf9a7d1a`</sub>

126. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:22:f348961c`</sub>

127. **Action:** A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:23:8445837f`</sub>

128. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:1:192fb731`</sub>

129. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:2:d186554c`</sub>

130. **Action:** Search for the organization in the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:3:9b9c1b59`</sub>

131. **Action:** Find the organization in the Search Results table and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:4:dae744c9`</sub>

132. **Action:** Under Products, click Modify next to Payer Authentication.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:5:134a2503`</sub>

133. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:6:5f53c678`</sub>

134. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:7:0ace24f8`</sub>

135. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:8:d50caa67`</sub>

136. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:9:b3b1648c`</sub>

137. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:10:d8b2030d`</sub>

138. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:11:0c78012d`</sub>

139. **Action:** Click the trash can icon to delete a configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:12:21bb36be`</sub>

140. **Action:** Click View all currencies to collapse or expand all currencies that are configured.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:13:2d518b66`</sub>

141. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:14:a0e45866`</sub>

142. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:15:ab96d42b`</sub>

143. **Action:** A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:16:8b0e1484`</sub>

144. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:1:93fbf65f`</sub>

145. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:2:d7adbcce`</sub>

146. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:3:6ab42d12`</sub>

147. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:4:40c0e850`</sub>

148. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:5:cc47dd2d`</sub>

149. **Action:** Under Commerce Solutions, select Token Management Service. Click Add. The Token Management Service page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Token Management Service page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:6:00674bc6`</sub>

150. **Action:** In the Product Configuration Template drop-down menu, select your template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:7:4bfcef6a`</sub>

151. **Action:** Click Apply to save your configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:8:7332fbb3`</sub>

152. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:1:2be96c36`</sub>

153. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:2:ebe3c0dd`</sub>

154. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:3:0b852b6b`</sub>

155. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:4:f1d22a26`</sub>

156. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:5:30dd86b8`</sub>

157. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:6:aedf22e4`</sub>

158. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:7:4a46e957`</sub>

159. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:8:84e2da26`</sub>

160. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:9:647e1fb9`</sub>

161. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:10:7781b8b3`</sub>

162. **Action:** Under Product Enablement, find `Token Management Service` and select Enabled under the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:11:0c5e392c`</sub>

163. **Action:** Click Configure to configure `Token Management Service`.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:12:94d80f51`</sub>

164. **Action:** In the Product Configuration Template drop-down menu, select your template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:13:f3e09147`</sub>

165. **Action:** Click Apply to save your configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:14:1f2938c2`</sub>

166. **Action:** Navigate to Token Management.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:1:bf5226ae`</sub>

167. **Action:** Click Vault Management.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:2:8989bba2`</sub>

168. **Action:** Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:3:7be4cbc4`</sub>

169. **Action:** Choose the merchant account to view the `TMS` vaults that are configured for the merchant.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:4:febc62c5`</sub>

170. **Action:** Click Network Tokenization.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:5:681c8223`</sub>

171. **Action:** Click Enroll to VISA/Mastercard token services.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:6:af861b97`</sub>

172. **Action:** Enter the required information for each card type:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:7:bcfd9129`</sub>

173. **Action:** Click Onboard with Acquirer ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:8:07eadfa0`</sub>

174. **Action:** Enter the required information:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:9:d937e717`</sub>

175. **Action:** Click Enroll to Network Token Services to complete enrollment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:10:e629cfe3`</sub>

176. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:1:82047b1f`</sub>

177. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:2:844c6600`</sub>

178. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:3:c84c8ce9`</sub>

179. **Action:** Select the vault owner that you want to configure from the Vault Owner drop-down list.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:4:983ce7a5`</sub>

180. **Action:** In the Details column, click Access Settings. The MID Access page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The MID Access page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:5:e0377d5e`</sub>

181. **Action:** Check the box for the vault settings you want to enable for each merchant you want to configure:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:6:be525cc3`</sub>

182. **Action:** Click Submit to save your settings.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:7:d1339209`</sub>

183. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:1:9af7cbce`</sub>

184. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:2:23a5cb4a`</sub>

185. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:3:15d16a36`</sub>

186. **Action:** From the Vault Owner drop-down list, select the vault owner..
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:4:206c6907`</sub>

187. **Action:** In the Details column, click Vault Settings. The Edit Vault page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Edit Vault page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:5:021ba039`</sub>

188. **Action:** Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:7:4ee26959`</sub>

189. **Action:** To return to the vault management page, click VAULT MANAGEMENT.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:9:ffdbb17a`</sub>

<!-- sequence_stats: steps=189 outcome_gaps=145 api_ops=11 ui_steps=178 -->

## Constraints

- [id_format_rule] The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields:prose:fb96fec35a26`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields.md.md
- [ttl_or_validity] Allow 2 to 3 days for the completion of your request.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:prose:a99f103acaf8`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids.md.md
- [id_format_rule] The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-req-fields:prose:fb96fec35a26`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-req-fields.md.md
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:prose:1ac5173eb260`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:prose:f213e5b78ab0`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:prose:1ac5173eb260`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding.md.md
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:prose:f213e5b78ab0`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding.md.md
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:prose:1ac5173eb260`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing.md.md
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:prose:f213e5b78ab0`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing.md.md
- [ttl_or_validity] Allow 2 to 3 days for the completion of your request.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:prose:a99f103acaf8`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids.md.md

## Failure modes

- error-codes  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-ex:error:c8c941da`</sub> · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-ex.md.md
- error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:error:95df168d`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md

<!-- /section:facts -->
