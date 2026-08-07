Modify a `Payer Authentication` Configuration for an Organization {#config-payer-auth-existing}
===============================================================================================

Follow these steps to modify `Payer Authentication` for an organization:

1. In the left navigation pane, click the Portfolio Management icon.

2. Under Merchants, click Manage Merchants. The Manage Merchants page appears.

3. Search for the organization in the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").

4. Find the organization in the Search Results table and click the eyeball icon. The Merchant Details page appears.

5. Under Products, click Modify next to Payer Authentication.

6. In the Payer Authentication Set Up drop-down menu, choose a template.

7. Click Configure for each `Payer Authentication` card service that you want to configure.  
   Your card processing settings and the accepted card types determine which of these services are available to you:

   * Visa Secure
   * Mastercard/Meeza Identity Check
   * American Express SafeKey
   * JCB J/Secure
   * Discover/Diners Club ProtectBuy
   * ELO
   * UnionPay 3-D Secure
   * Cartes Bancaires
8. Click Enable on the Enable/Disable slider to configure acquirer currencies.

   1. Optional: Click Disable to disable acquirer currency configurations. Your existing configurations remain but are unavailable.
9. Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.

   #### ADDITIONAL INFORMATION

   For testing purposes, use Merchant ID: `123456789` and Acquirer ID: `cybersource`.  
   For Cartes Bancaires, you must also enter the SIRET number.

10. From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.

    > IMPORTANT The default currency configuration includes all currencies. If you do not configure a currency for an acquirer, the default is used.

11. Click Add more currency to configure another currency for an acquirer.

    1. Check the box next to **Copy last Acquirer Merchant ID and Acquirer ID for new item** to populate the acquirer merchant ID and acquirer ID fields.
12. Click the trash can icon to delete a configuration.

13. Click View all currencies to collapse or expand all currencies that are configured.

14. Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.

15. If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.

16. A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.

