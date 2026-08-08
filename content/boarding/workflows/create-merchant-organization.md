# Create a Merchant Organization

<!-- section:prose -->
Register a new merchant (organization + transacting org) via the Boarding Registration Service.
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- **Gap:** no prerequisite is specified in the source docs.

## Steps

### REST API path

1. **API:** `POST /boarding/v1/registrations` — Create a Merchant Organization
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set the value to `true`.
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md) — Set to the ID of the organization that you want to be above this one in the hierarchy, which in this case would be the portfolio.
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set the value to `MERCHANT`.
   - Example request:
     ```json
     {
         "registrationInformation": {
             "boardingFlow": "ENTERPRISE"
         },
         "organizationInformation": {
             "organizationId": "yourmerchantorgidhere",
             "status": "LIVE",
             "parentOrganizationId": "yourportfolioorgidhere",
             "type": "MERCHANT",
             "configurable": true,
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
                 "technicalContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "emergencyContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "name": "Test Merchant",
                 "websiteUrl": "https://www.MerchantUrlHere.com",
                 "phoneNumber": "5551234567",
                 "timeZone": "America/Los_Angeles",
                 "merchantCategoryCode": "5999"
             }
         }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - outcome_missing: false
   - Example response:
     ```json
     {
         "id": "1695804001",
         "submitTimeUtc": "2022-04-13T20:58:28Z",
         "status": "SUCCESS",
         "registrationInformation": {
             "mode": "COMPLETE",
             "boardingPackageId": "123456789012"
         },
         "organizationInformation": {
             "organizationId": "yourmercahntorgidhere",
             "parentOrganizationId": "yourportfolioorgidhere"
         },
         "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:1de1e10a`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-merch-api)</sub>

2. **API:** `POST /boarding/v1/registrations` — Add a Transacting Organization to a New Merchant Organization
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set the value to `false`.
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md) — Set to the ID of the merchant organization that you created during the previous section.
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set the value to `TRANSACTING`.
   - Example request:
     ```json
     {
         "registrationInformation": {
             "boardingFlow": "ENTERPRISE"
         },
         "organizationInformation": {
             "organizationId": "yourtransactingorgidhere",
             "status": "LIVE",
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
                 "technicalContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "emergencyContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "name": "Test Merchant",
                 "websiteUrl": "https://www.MerchantUrlHere.com",
                 "phoneNumber": "5551234567",
                 "timeZone": "America/Los_Angeles",
                 "merchantCategoryCode": "5999"
             },
             "parentOrganizationId": "yourmercahntorgidhere",
             "type": "TRANSACTING",
             "configurable": false
         },
         "productInformation": {
             "selectedProducts": {
                 "payments": {
                     "customerInvoicing": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "risk": {
                     "fraudManagementEssentials": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "commerceSolutions": {
                     "tokenManagement": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "valueAddedServices": {
                     "transactionSearch": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     },
                     "reporting": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 }
             }
         }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - outcome_missing: false
   - Example response:
     ```json
     {
         "id": "1696604001",
         "submitTimeUtc": "2022-04-13T21:03:02Z",
         "status": "SUCCESS",
         "registrationInformation": {
             "mode": "COMPLETE",
             "boardingPackageId": "123456789012"
         },
         "organizationInformation": {
             "organizationId": "yourtransactingorgidhere",
             "parentOrganizationId": "yourmercahntorgidhere"
         },
         "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:12aad1c5`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-new-transacting-api)</sub>

3. **API:** `POST /boarding/v1/registrations` — Add a Transacting Organization to an Existing Organization
   - Actor: Partner system (REST API)
   - test host: `https://apitest.cybersource.com`
   - Required fields:
     - [`organizationInformation.businessInformation.address.address1`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md)
     - [`organizationInformation.businessInformation.address.country`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md)
     - [`organizationInformation.businessInformation.address.locality`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md)
     - [`organizationInformation.businessInformation.businessContact.email`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md)
     - [`organizationInformation.businessInformation.businessContact.firstName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md)
     - [`organizationInformation.businessInformation.businessContact.lastName`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md)
     - [`organizationInformation.businessInformation.businessContact.phoneNumber`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md)
     - [`organizationInformation.businessInformation.name`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md)
     - [`organizationInformation.configurable`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md) — Set the value to `false`.
     - [`organizationInformation.parentOrganizationId`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md) — Set to the ID of the organization that you want to be above this one in the hierarchy.
     - [`organizationInformation.type`](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md) — Set the value to `TRANSACTING`.
   - Example request:
     ```json
     {
         "registrationInformation": {
             "boardingFlow": "ENTERPRISE"
         },
         "organizationInformation": {
             "organizationId": "yourtransactingorgidhere",
             "status": "LIVE",
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
                 "technicalContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "emergencyContact": {
                     "firstName": "Jane",
                     "lastName": "Smith",
                     "phoneNumber": "5551234567",
                     "email": "email@domain.com"
                 },
                 "name": "Test Merchant",
                 "websiteUrl": "https://www.MerchantUrlHere.com",
                 "phoneNumber": "5551234567",
                 "timeZone": "America/Los_Angeles",
                 "merchantCategoryCode": "5999"
             },
             "parentOrganizationId": "yourmercahntorgidhere",
             "type": "TRANSACTING",
             "configurable": false
         },
         "productInformation": {
             "selectedProducts": {
                 "payments": {
                     "customerInvoicing": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "risk": {
                     "fraudManagementEssentials": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "commerceSolutions": {
                     "tokenManagement": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 },
                 "valueAddedServices": {
                     "transactionSearch": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     },
                     "reporting": {
                         "subscriptionInformation": {
                             "enabled": true,
                             "selfServiceability": "NOT_SELF_SERVICEABLE"
                         }
                     }
                 }
             }
         }
     }
     ```
   - Expected outcome: Response status `SUCCESS` (see example response).
   - outcome_missing: false
   - Example response:
     ```json
     {
         "id": "1696604001",
         "submitTimeUtc": "2022-04-13T21:03:02Z",
         "status": "SUCCESS",
         "registrationInformation": {
             "mode": "COMPLETE",
             "boardingPackageId": "123456789012"
         },
         "organizationInformation": {
             "organizationId": "yourtransactingorgidhere",
             "parentOrganizationId": "yourmercahntorgidhere"
         },
         "message": "Request was processed successfully"
     }
     ```
   - <sub>[`en-us_boarding_developer_all_rest_boarding:endpoint:post:c8957234`](https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-transacting-api)</sub>

### Business Center UI path

4. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant:step:1:f88781f9`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant.html#merchants-v2-add-merchant_merchants-v2-add-merchant-step1)</sub>

5. **Action:** Select **Board a new merchant account** and click **Next**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant:step:2:40240e95`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant.html#merchants-v2-add-merchant_merchants-v2-add-merchant-step2)</sub>

6. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant:step:3:270a97fe`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant.html#merchants-v2-add-merchant_merchants-v2-add-merchant-step3)</sub>

7. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant:step:4:0ba9460d`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant.html#merchants-v2-add-merchant_merchants-v2-add-merchant-step4)</sub>

8. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant:step:5:8153fb6f`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant.html#merchants-v2-add-merchant_merchants-v2-add-merchant-step5)</sub>

9. **Action:** In Basic Information, enter the merchant account name and the organization ID in the provided text fields.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-acct-info:step:1:1eb3f5ac`</sub>

10. **Action:** Enter the merchant information in the provided text fields. Required fields are noted with an asterisk (\*).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-acct-info:step:2:507b2d05`</sub>

11. **Action:** Click **Save** . You are returned to the Add Merchant page. You can skip the optional hierarchy step by clicking **Skip**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-acct-info:step:3:aef77e67`</sub>

12. **Action:** Click **Start** in the Transacting Organization and Products section. The Transacting Organization and Products page is displayed.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page is displayed.
   - outcome_missing: false
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:1:7af7bbe8`</sub>

13. **Action:** Optional: modify the name and ID of the organization by using the text fields in the Transacting Organization Details section. The ID must be unique, not just in the portfolio or account, but across the system. By default, the name is the merchant name with 001 added to the end of the name. If you accept this default, additional transacting organizations will have default names that iterate the numbers at the end of their names, beginning with 002.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:2:eb75f3c3`</sub>

14. **Action:** Optional: By default, the organization information is inherited from the parent organization. To edit the organization information, click **Edit** in the Transacting Organization Information section. After editing, click **Apply**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:3:f3fbcc4c`</sub>

15. **Action:** To enable a product in the Product Enablement section, click the Enablement drop-down menu and select **Enabled**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:4:c1e2b558`</sub>

16. **Action:** To modify the configuration, click the **Edit** or **Configure** button (depending on the product). Some products are not configurable.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:5:8fef1460`</sub>

17. **Action:** To confirm the configuration, click **Apply**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:6:26cf4d96`</sub>

18. **Action:** To save all product configurations, click **Save**. You are returned to the Add Merchant page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:7:1ebbba21`</sub>

19. **Action:** To continue working with this organization, click **Continue working with this merchant** . To finish and return to Merchant Management or to add another merchant, click **Return to merchant management**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:step:8:c302b507`</sub>

20. **Action:** Under Merchants, click **Manage Merchants**. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - outcome_missing: false
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:1:cbff3268`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step2)</sub>

21. **Action:** In the left navigation panel, click **Portfolio Management**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:2:34fbd153`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step1)</sub>

22. **Action:** age Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:3:cc40b3f4`</sub>

23. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:4:3543cb3b`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step3)</sub>

24. **Action:** Select **Add to an existing account** and then click **Next**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:5:3167d256`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step4)</sub>

25. **Action:** If you have more than one boarding package, the Boarding Presets section is displayed. Enter the name of the merchant organization to add the new transacting organization to. Then choose a boarding package from the drop-down menu, or enter text in the search field to find one. Then click **Next**. If you have only one boarding package, the Boarding Presets section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: If you have more than one boarding package, the Boarding Presets section is displayed.
   - outcome_missing: false
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:6:e66e74b6`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step5)</sub>

26. **Action:** Optional: add additional organizations by clicking **Start** in the Hierarchy Details section. Or skip this step by clicking **Skip**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>[`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing:step:7:38389ace`](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-to-existing.html#boarding-merchants-v2-add-to-existing_merchants-v2-add-existing-step6)</sub>

27. **Action:** Click **Start** in the Transacting Organization and Products section. The Transacting Organization and Products page is displayed.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page is displayed.
   - outcome_missing: false
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:1:cc10e60a`</sub>

28. **Action:** Optional: modify the name and ID of the organization by using the text fields in the Transacting Organization Details section. By default, the name is the merchant name with 001 added to the end of the name. If you accept this default, additional transacting organizations will have default names that iterate the numbers at the end of their names, beginning with 002.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:2:e2ea1308`</sub>

29. **Action:** Optional: to edit the organization information, Click **Edit** in the Transacting Organization Information section. After editing, click **Apply**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:3:9e61fb56`</sub>

30. **Action:** To enable a product in the Product Enablement section, click the Enablement drop-down menu and select **Enabled**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:4:5267d9de`</sub>

31. **Action:** To modify the configuration, click the **Edit** or **configure** button (depending on the product). Some products are not configurable.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:5:7e6463dc`</sub>

32. **Action:** To confirm the configuration, click **Apply**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:6:d60a0eed`</sub>

33. **Action:** To save all product configurations, click **Save**. You are returned to the Add Merchant page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:7:b7cdaebe`</sub>

34. **Action:** To continue working with this organization, click **Continue working with this merchant** . To finish and return to Merchant Management, click **Return to merchant management**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - outcome_missing: true
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-to-existing_merchants-v2-existing-trans-org-prod:step:8:4c04d091`</sub>

<!-- sequence_stats: steps=34 outcome_gaps=27 outcome_missing=27 api_ops=3 ui_steps=31 -->

## Constraints

- [id_format_rule] It must be unique, not just in the portfolio or account, but in the system.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-acct-info:prose:e1afb7ab5681`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-acct-info.md.md
- [id_format_rule] The ID must be unique, not just in the portfolio or account, but across the system.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod:prose:bebdf35a5910`</sub> · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-reg-intro_merchants-v2-add-merchant_merchants-v2-add-merch-trans-org-prod.md.md

## Failure modes

- **Gap:** no error cases documented for this workflow in the source docs.

<!-- /section:facts -->
