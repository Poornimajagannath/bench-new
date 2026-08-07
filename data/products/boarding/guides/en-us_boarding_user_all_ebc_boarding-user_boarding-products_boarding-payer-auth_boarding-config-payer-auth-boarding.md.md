Add `Payer Authentication` to a Merchant Account {#boarding-config-payer-auth-existing}
=======================================================================================

Follow these steps to add `Payer Authentication` to a merchant account:

1. In the left navigation pane, click the Portfolio Management icon.

2. Under Merchants, click Manage Merchants. The Manage Merchants page appears.

3. Click **+ Add Merchant**.

4. Choose a location to board your merchant:

   * Board a new merchant account to create a new merchant account.
   * Add to an existing account to add a transacting merchant to an existing merchant organization.

   Click Next.

5. If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.

6. If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.

7. Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").

8. Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.

9. Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.

10. Under Transacting Organization Details, enter the transacting organization name and the organization ID.

11. Under Product Enablement, find `Payer Authentication` and select Enabled from the Enablement drop-down menu.

12. Click Configure to configure `Payer Authentication`.

13. In the Payer Authentication Set Up drop-down menu, choose a template.

14. Click Configure for each `Payer Authentication` card service that you want to configure.  
    Your card processing settings and the accepted card types determine which of these services are available to you:

    * Visa Secure
    * Mastercard/Meeza Identity Check
    * American Express SafeKey
    * JCB J/Secure
    * Discover/Diners Club ProtectBuy
    * ELO
    * UnionPay 3-D Secure
    * Cartes Bancaires
15. Click Enable on the Enable/Disable slider to configure acquirer currencies.

    1. Optional: Click Disable to disable acquirer currency configurations. Your existing configurations remain but are unavailable.
16. Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.

    #### ADDITIONAL INFORMATION

    For testing purposes, use Merchant ID: `123456789` and Acquirer ID: `cybersource`.  
    For Cartes Bancaires, you must also enter the SIRET number.

17. From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.

    > IMPORTANT The default currency configuration includes all currencies. If you do not configure a currency for an acquirer, the default is used.

18. Click Add more currency to configure another currency for an acquirer.

    1. Check the box next to **Copy last Acquirer Merchant ID and Acquirer ID for new item** to populate the acquirer merchant ID and acquirer ID fields.
19. Click the trash can icon to delete a configuration.

20. Click View all currencies to collapse or expand all currencies that are configured.

21. Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.

22. If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.

23. A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.

