Configure the Token Vault Settings Using the `Business Center` {#tms-vault-settings}
====================================================================================

Follow these steps to configure your merchant token vault settings:

1. Log in to the `Business Center` test environment or production environment.

   * **Test:** `https://businesscentertest.cybersource.com`
   * **Production:** `https://businesscenter.cybersource.com`
2. In the left navigation panel, click the Token Management icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-tkn-mgmt.svg/jcr:content/renditions/original) ).

3. Click Vault Management New. The Vault Management page appears.

4. From the Vault Owner drop-down list, select the vault owner..

5. In the Details column, click Vault Settings. The Edit Vault page appears.

6. Click Edit.  
   A dialog box appears with a message to warn you that changing your vault settings could result in your merchants being unable to access tokens, which could result in failing transactions. Click Yes if you want to continue.

7. Enter the vault name, supported payment methods, supported token types and formats, card number masking format, payment instrument storing configuration, and the webhook URL.  
   For each token type, you can choose from these token formats:

   * 32 Character Hex
   * 22 Digits
   * 19 Digits Luhn Check Passing
   * 16 Digits Luhn Check Passing

   > IMPORTANT Account Updater is incompatible with instrument identifier tokens in the 22-digit format.

8. Click SAVE.

9. To return to the vault management page, click VAULT MANAGEMENT.

