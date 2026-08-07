# Enable and Configure Products

<!-- section:prose -->
Enable products for a merchant during or after onboarding (BRS invokes PECS.

PECS updates after).
<!-- /section:prose -->

_Generated from `normalized/2026-08-08-boarding.claims.json`; do not hand-edit. Fix the source and regenerate._

<!-- section:facts -->

## Preconditions

- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth:prose:58bfc6580728` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth.md.md</sub>
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth:prose:a4431adf9e91` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth.md.md</sub>
- Must be in the format `http://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields:prose:452b05be0057` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields.md.md</sub>
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms:prose:00452a944a4e` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms.md.md</sub>
- Having a TRID is a prerequisite for enabling network tokenization.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:prose:bf5e52f8feb7` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids.md.md</sub>
- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth:prose:58bfc6580728` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth.md.md</sub>
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth:prose:a4431adf9e91` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth.md.md</sub>
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms:prose:00452a944a4e` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-tms.md.md</sub>
- IMPORTANT You must include this field for all card types configured for the processor.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor_pecs-add-delete-processor-req-fields:prose:477d5afd2eaa` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-add-delete-processor_pecs-add-delete-processor-req-fields.md.md</sub>
- IMPORTANT You must include this field for all card types configured for the processor.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor_pecs-delete-processor-req-fields:prose:477d5afd2eaa` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_pecs-delete-processor_pecs-delete-processor-req-fields.md.md</sub>
- * You must include a merchant website URL. 3-D Secure protocol requires that the website URL is in the format `https://www.example.com`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth:prose:609b36db9ed6` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth.md.md</sub>
- * You must include a merchant category code for your merchant.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth:prose:a4431adf9e91` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth.md.md</sub>
- You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms:prose:00452a944a4e` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms.md.md</sub>
- Having a TRID is a prerequisite for enabling network tokenization.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:prose:bf5e52f8feb7` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids.md.md</sub>

## Steps

### Via Partner system (REST API) — `en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids.md.md`

1. **Action:** Navigate to Token Management.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:1:bf5226ae`</sub>
2. **Action:** Click Vault Management.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:2:8989bba2`</sub>
3. **Action:** Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:3:7be4cbc4`</sub>
4. **Action:** Choose the merchant account to view the `TMS` vaults that are configured for the merchant.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:4:febc62c5`</sub>
5. **Action:** Click Network Tokenization.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:5:681c8223`</sub>
6. **Action:** Click Enroll to VISA/Mastercard token services.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:6:af861b97`</sub>
7. **Action:** Enter the required information for each card type:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:7:bcfd9129`</sub>
8. **Action:** Click Onboard with Acquirer ID.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:8:07eadfa0`</sub>
9. **Action:** Enter the required information:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:9:d937e717`</sub>
10. **Action:** Click Enroll to Network Token Services to complete enrollment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:step:10:e629cfe3`</sub>
### Via Partner system (REST API) — `en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access.md.md`

1. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:1:82047b1f`</sub>
2. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:2:844c6600`</sub>
3. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:3:c84c8ce9`</sub>
4. **Action:** Select the vault owner that you want to configure from the Vault Owner drop-down list.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:4:983ce7a5`</sub>
5. **Action:** In the Details column, click Access Settings. The MID Access page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The MID Access page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:5:e0377d5e`</sub>
6. **Action:** Check the box for the vault settings you want to enable for each merchant you want to configure:
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:6:be525cc3`</sub>
7. **Action:** Click Submit to save your settings.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:7:d1339209`</sub>
### Via Partner system (REST API) — `en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings.md.md`

1. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:1:9af7cbce`</sub>
2. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:2:23a5cb4a`</sub>
3. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:3:15d16a36`</sub>
4. **Action:** From the Vault Owner drop-down list, select the vault owner..
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:4:206c6907`</sub>
5. **Action:** In the Details column, click Vault Settings. The Edit Vault page appears.
   - Actor: Partner system (REST API)
   - Expected outcome: The Edit Vault page appears.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:5:021ba039`</sub>
6. **Action:** Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:7:4ee26959`</sub>
7. **Action:** To return to the vault management page, click VAULT MANAGEMENT.
   - Actor: Partner system (REST API)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:9:ffdbb17a`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:1:801c6574`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:2:46c4bc64`</sub>
3. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:3:a08cfe83`</sub>
4. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:4:ae51b6ec`</sub>
5. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:5:d2542426`</sub>
6. **Action:** Under Payments, select Alternative Payments and click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:6:3bdd2506`</sub>
7. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:7:1afa1e26`</sub>
8. **Action:** Click Continue. The Product Configuration page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:8:9535a452`</sub>
9. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:9:abe72a95`</sub>
10. **Action:** Click Continue to return to the Merchant Details page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-add:step:10:400bae13`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:1:3be597a6`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:2:81e9a752`</sub>
3. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:3:d47b0824`</sub>
4. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:4:2bc24e44`</sub>
5. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:5:1c503020`</sub>
6. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:6:ec52c350`</sub>
7. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:7:ed19a55b`</sub>
8. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:8:321fccca`</sub>
9. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:9:c8966550`</sub>
10. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:10:92c9fcb4`</sub>
11. **Action:** Under Product Enablement, find Alternative Payments and select Allow Self Enablement under the Enablement drop-down menu.{#boarding-config-altpay-boarding-self_boarding-config-altpay-boarding-self-step8}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:11:3e8de3f9`</sub>
12. **Action:** Click Save. Alternative Payments is now available for self-enablement for the merchant.{#boarding-config-altpay-boarding-self_boarding-config-altpay-boarding-self-step9}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding-self:step:12:8c900dce`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding.md.md`

1. **Action:** In the left navigation panel, click **Portfolio Management**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:1:84efa501`</sub>
2. **Action:** Under Merchants, click **Manage Merchants**. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:2:44b8c90a`</sub>
3. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:3:d8f30e44`</sub>
4. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:4:55661281`</sub>
5. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:5:70dcb843`</sub>
6. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:6:74e4ca33`</sub>
7. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:7:71913371`</sub>
8. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:8:c87239f4`</sub>
9. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step6}
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:9:529cbd84`</sub>
10. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step7}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:10:27b675c4`</sub>
11. **Action:** Under Product Enablement, find Alternative Payments and select Enabled under the Enablement drop-down menu.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step8}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:11:5590cfca`</sub>
12. **Action:** Click Configure. The Configure Alternative Payment Methods page appears.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step9}
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:12:fefbafd1`</sub>
13. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:13:6c53b944`</sub>
14. **Action:** Click Continue. The Product Configuration page appears.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step11}
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:14:66d3600b`</sub>
15. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:15:e3a6f564`</sub>
16. **Action:** Click Continue to return to the Merchant Details page.{#boarding-config-altpay-boarding_boarding-config-altpay-boarding-step13}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-boarding:step:16:1b3e9011`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:1:e9ace8fd`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:2:6fb27c98`</sub>
3. **Action:** Search for the organization in the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:3:ccf10971`</sub>
4. **Action:** Find the organization in the Search Results table and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:4:605c9886`</sub>
5. **Action:** Under Products, click Edit next to Alternative Payments. The Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:5:f27e4448`</sub>
6. **Action:** If you want to add an available alternative payment method, click Add Services. The Configure Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:6:412b436b`</sub>
7. **Action:** If you want to configure an enabled alternative payment method, click Edit. The Configure Alternative Payment Methods page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Configure Alternative Payment Methods page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:7:d6587764`</sub>
8. **Action:** Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:8:52d5d495`</sub>
9. **Action:** Click Continue. The Product Configuration page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Product Configuration page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:9:f17a52e6`</sub>
10. **Action:** Enter the required details for each alternative payment method you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:10:c999b66a`</sub>
11. **Action:** Click Continue to return to the Merchant Details page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-altpay_boarding-config-altpay-existing:step:11:86fe1995`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task.md.md`

1. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:1:a9418ad9`</sub>
2. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:2:09859f03`</sub>
3. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:3:c953ad31`</sub>
4. **Action:** Select the product you want to enable. Click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-enablement-products-intro_boarding-enable-products-task:step:4:0c01db28`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:1:315e4918`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:2:5854d539`</sub>
3. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:3:4faacb75`</sub>
4. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:4:a134be58`</sub>
5. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:5:23765ebd`</sub>
6. **Action:** Select Payer Authentication and click Add.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:6:4a7a2bea`</sub>
7. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.{#config-payer-auth-add_config-payer-auth-add-step1}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:7:63737da1`</sub>
8. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:8:de695665`</sub>
9. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:9:e6f976aa`</sub>
10. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:10:42400b21`</sub>
11. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:11:ae6ad600`</sub>
12. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:12:440e2e63`</sub>
13. **Action:** Click the trash can icon to delete a configuration.{#config-payer-auth-add_config-payer-auth-add-step7}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:13:67bf86a1`</sub>
14. **Action:** Click View all currencies to collapse or expand all currencies that are configured.{#config-payer-auth-add_config-payer-auth-add-step8}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:14:79ccfa0b`</sub>
15. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.{#config-payer-auth-add_config-payer-auth-add-step9}
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:15:de251be1`</sub>
16. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:step:16:94e1f492`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:1:4c3bdc86`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:2:c0b28e96`</sub>
3. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:3:90633964`</sub>
4. **Action:** Choose a location to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:4:2d4175cd`</sub>
5. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:5:bcbd02a6`</sub>
6. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:6:99c6b97f`</sub>
7. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:7:6389a740`</sub>
8. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:8:51ff745b`</sub>
9. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:9:8529de0b`</sub>
10. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:10:ee903114`</sub>
11. **Action:** Under Product Enablement, find `Payer Authentication` and select Enabled from the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:11:076dbff0`</sub>
12. **Action:** Click Configure to configure `Payer Authentication`.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:12:b3c2d975`</sub>
13. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:13:30bb71b4`</sub>
14. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:14:d1ede173`</sub>
15. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:15:cce02f71`</sub>
16. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:16:b99ed1bf`</sub>
17. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:17:710e913b`</sub>
18. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:18:05b9d6de`</sub>
19. **Action:** Click the trash can icon to delete a configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:19:9161d2bc`</sub>
20. **Action:** Click View all currencies to collapse or expand all currencies that are configured.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:20:66247b5f`</sub>
21. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:21:cf9a7d1a`</sub>
22. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:22:f348961c`</sub>
23. **Action:** A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:step:23:8445837f`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:1:192fb731`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:2:d186554c`</sub>
3. **Action:** Search for the organization in the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:3:649f9651`</sub>
4. **Action:** Find the organization in the Search Results table and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:4:dae744c9`</sub>
5. **Action:** Under Products, click Modify next to Payer Authentication.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:5:134a2503`</sub>
6. **Action:** In the Payer Authentication Set Up drop-down menu, choose a template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:6:5f53c678`</sub>
7. **Action:** Click Configure for each `Payer Authentication` card service that you want to configure.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:7:0ace24f8`</sub>
8. **Action:** Click Enable on the Enable/Disable slider to configure acquirer currencies.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:8:d50caa67`</sub>
9. **Action:** Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:9:b3b1648c`</sub>
10. **Action:** From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:10:d8b2030d`</sub>
11. **Action:** Click Add more currency to configure another currency for an acquirer.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:11:0c78012d`</sub>
12. **Action:** Click the trash can icon to delete a configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:12:21bb36be`</sub>
13. **Action:** Click View all currencies to collapse or expand all currencies that are configured.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:13:2d518b66`</sub>
14. **Action:** Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:14:a0e45866`</sub>
15. **Action:** If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:15:ab96d42b`</sub>
16. **Action:** A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:step:16:8b0e1484`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:1:93fbf65f`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:2:d7adbcce`</sub>
3. **Action:** Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:3:7734cc17`</sub>
4. **Action:** Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Merchant Details page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:4:40c0e850`</sub>
5. **Action:** In the Products section, click + Add Products. The Add a Product page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Add a Product page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:5:cc47dd2d`</sub>
6. **Action:** Under Commerce Solutions, select Token Management Service. Click Add. The Token Management Service page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Token Management Service page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:6:00674bc6`</sub>
7. **Action:** In the Product Configuration Template drop-down menu, select your template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:7:4bfcef6a`</sub>
8. **Action:** Click Apply to save your configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-add:step:8:7332fbb3`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new.md.md`

1. **Action:** In the left navigation pane, click the Portfolio Management icon.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:1:2be96c36`</sub>
2. **Action:** Under Merchants, click Manage Merchants. The Manage Merchants page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Manage Merchants page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:2:ebe3c0dd`</sub>
3. **Action:** Click **+ Add Merchant**.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:3:0b852b6b`</sub>
4. **Action:** Select where you want to board your merchant:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:4:f1d22a26`</sub>
5. **Action:** If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:5:30dd86b8`</sub>
6. **Action:** If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:6:aedf22e4`</sub>
7. **Action:** Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:7:d444321f`</sub>
8. **Action:** Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:8:84e2da26`</sub>
9. **Action:** Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Transacting Organization and Products page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:9:647e1fb9`</sub>
10. **Action:** Under Transacting Organization Details, enter the transacting organization name and the organization ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:10:7781b8b3`</sub>
11. **Action:** Under Product Enablement, find `Token Management Service` and select Enabled under the Enablement drop-down menu.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:11:0c5e392c`</sub>
12. **Action:** Click Configure to configure `Token Management Service`.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:12:94d80f51`</sub>
13. **Action:** In the Product Configuration Template drop-down menu, select your template.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:13:f3e09147`</sub>
14. **Action:** Click Apply to save your configuration.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_boarding-config-tms-new:step:14:1f2938c2`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids.md.md`

1. **Action:** Navigate to Token Management.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:1:bf5226ae`</sub>
2. **Action:** Click Vault Management.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:2:8989bba2`</sub>
3. **Action:** Use the Vault Owner filter to search for the merchant account that has `TMS` enabled.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:3:7be4cbc4`</sub>
4. **Action:** Choose the merchant account to view the `TMS` vaults that are configured for the merchant.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:4:febc62c5`</sub>
5. **Action:** Click Network Tokenization.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:5:681c8223`</sub>
6. **Action:** Click Enroll to VISA/Mastercard token services.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:6:af861b97`</sub>
7. **Action:** Enter the required information for each card type:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:7:bcfd9129`</sub>
8. **Action:** Click Onboard with Acquirer ID.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:8:07eadfa0`</sub>
9. **Action:** Enter the required information:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:9:d937e717`</sub>
10. **Action:** Click Enroll to Network Token Services to complete enrollment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:step:10:e629cfe3`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access.md.md`

1. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:1:82047b1f`</sub>
2. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:2:844c6600`</sub>
3. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:3:c84c8ce9`</sub>
4. **Action:** Select the vault owner that you want to configure from the Vault Owner drop-down list.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:4:983ce7a5`</sub>
5. **Action:** In the Details column, click Access Settings. The MID Access page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The MID Access page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:5:e0377d5e`</sub>
6. **Action:** Check the box for the vault settings you want to enable for each merchant you want to configure:
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:6:be525cc3`</sub>
7. **Action:** Click Submit to save your settings.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-mid-access:step:7:d1339209`</sub>
### Via Partner admin (Business Center) — `en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings.md.md`

1. **Action:** Log in to the `Business Center` test environment or production environment.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:1:9af7cbce`</sub>
2. **Action:** In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:2:23a5cb4a`</sub>
3. **Action:** Click Vault Management New. The Vault Management page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Vault Management page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:3:15d16a36`</sub>
4. **Action:** From the Vault Owner drop-down list, select the vault owner..
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:4:206c6907`</sub>
5. **Action:** In the Details column, click Vault Settings. The Edit Vault page appears.
   - Actor: Partner admin (Business Center)
   - Expected outcome: The Edit Vault page appears.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:5:021ba039`</sub>
6. **Action:** Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:7:4ee26959`</sub>
7. **Action:** To return to the vault management page, click VAULT MANAGEMENT.
   - Actor: Partner admin (Business Center)
   - Expected outcome: **Gap:** not stated in source.
   - <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-vault-settings:step:9:ffdbb17a`</sub>

## Constraints

- [id_format_rule] The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields:prose:fb96fec35a26` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-payer-auth_boarding-payer-auth-enable-intro_boarding-payer-auth-enable-reqfields.md.md</sub>
- [ttl_or_validity] Allow 2 to 3 days for the completion of your request.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids:prose:a99f103acaf8` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products-intro_boarding-tms_tms-vault-hierarchy_tms-trids.md.md</sub>
- [id_format_rule] The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-req-fields:prose:fb96fec35a26` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-req-fields.md.md</sub>
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:prose:1ac5173eb260` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md</sub>
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:prose:f213e5b78ab0` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md</sub>
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:prose:1ac5173eb260` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding.md.md</sub>
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding:prose:f213e5b78ab0` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-boarding.md.md</sub>
- [id_format_rule] The acquirer merchant ID must be from 1 to 35 alphanumeric characters.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:prose:1ac5173eb260` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing.md.md</sub>
- [id_format_rule] The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing:prose:f213e5b78ab0` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-existing.md.md</sub>
- [ttl_or_validity] Allow 2 to 3 days for the completion of your request.  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids:prose:a99f103acaf8` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-tms_tms-vault-hierarchy_tms-trids.md.md</sub>

## Failure modes

- error-codes  
  <sub>`en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-ex:error:c8c941da` · 2026-08-08-boarding/en-us_boarding_developer_all_rest_boarding_boarding-products_boarding-pecs-payer-auth_pecs-config-payerauth_pecs-config-payerauth-ex.md.md</sub>
- error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications  
  <sub>`en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add:error:95df168d` · 2026-08-08-boarding/en-us_boarding_user_all_ebc_boarding-user_boarding-products_boarding-payer-auth_boarding-config-payer-auth-add.md.md</sub>

<!-- /section:facts -->
