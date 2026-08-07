Add `Payer Authentication` to an Existing Organization {#config-payer-auth-add}
===============================================================================

Follow these steps to add `Payer Authentication` to an organization:

1. In the left navigation pane, click the Portfolio Management icon.

2. Under Merchants, click Manage Merchants. The Manage Merchants page appears.

3. Search for the organization on the Manage Merchant page. For more information on searching for an organization, see [Searching for Organizations (Version 2)](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/merchants-v2-searc-0.md "").

4. Find the organization in the Search Results table, and click the eyeball icon. The Merchant Details page appears.

5. In the Products section, click + Add Products. The Add a Product page appears.

6. Select Payer Authentication and click Add.

7. In the Payer Authentication Set Up drop-down menu, choose a template.{#config-payer-auth-add_config-payer-auth-add-step1}
   {#config-payer-auth-add_config-payer-auth-add-step1}

8. Click Configure for each `Payer Authentication` card service that you want to configure.  
   Your card processing settings and the accepted card types determine which of these services are available to you:

   * Visa Secure
   * Mastercard/Meeza Identity Check
   * American Express SafeKey
   * JCB J/Secure
   * Discover/Diners Club ProtectBuy
   * ELO
   * UnionPay 3-D Secure
   * Cartes Bancaires
     {#config-payer-auth-add_config-payer-auth-add-step2}
     {#config-payer-auth-add_config-payer-auth-add-step2}
9. Click Enable on the Enable/Disable slider to configure acquirer currencies.

   1. Optional: Click Disable to disable acquirer currency configurations. Your existing configurations remain but are unavailable.
      {#config-payer-auth-add_config-payer-auth-add-step3}
      {#config-payer-auth-add_config-payer-auth-add-step3}
10. Enter the acquirer merchant ID and acquirer ID. The acquirer merchant ID must be from 1 to 35 alphanumeric characters. The acquirer ID must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `acquirerID-1000`. An error message appears if the acquirer merchant ID or acquirer ID do not meet these specifications.

    #### ADDITIONAL INFORMATION {#config-payer-auth-add_config-payer-auth-add-step4}

    For testing purposes, use Merchant ID: `123456789` and Acquirer ID: `cybersource`.  
    For Cartes Bancaires, you must also enter the SIRET number.
    {#config-payer-auth-add_config-payer-auth-add-step4}

11. From the Currency drop-down menu, select the currency to enable for each acquirer. A *Duplicate Currency* warning appears when you have already configured a currency for an acquirer.

    > IMPORTANT The default currency configuration includes all currencies. If you do not configure a currency for an acquirer, the default is used.
    > {#config-payer-auth-add_config-payer-auth-add-step5}
    > {#config-payer-auth-add_config-payer-auth-add-step5}

12. Click Add more currency to configure another currency for an acquirer.

    1. Check the box next to **Copy last Acquirer Merchant ID and Acquirer ID for new item** to populate the acquirer merchant ID and acquirer ID fields.
       {#config-payer-auth-add_config-payer-auth-add-step6}
       {#config-payer-auth-add_config-payer-auth-add-step6}
13. Click the trash can icon to delete a configuration.{#config-payer-auth-add_config-payer-auth-add-step7}
    {#config-payer-auth-add_config-payer-auth-add-step7}

14. Click View all currencies to collapse or expand all currencies that are configured.{#config-payer-auth-add_config-payer-auth-add-step8}
    {#config-payer-auth-add_config-payer-auth-add-step8}

15. Click Save to save your configuration and return to the Payer Authentication Set Up and Enablement page.{#config-payer-auth-add_config-payer-auth-add-step9}
    {#config-payer-auth-add_config-payer-auth-add-step9}

16. If you do not want to save your changes, click Cancel to return to the Payer Authentication Set Up and Enablement page.

    1. A warning box appears and states that you have unsaved changes. Click Yes, cancel to return to the Payer Authentication Set Up and Enablement page without saving your configuration changes. Click Wait to stay on the card service configuration page.
       {#config-payer-auth-add_config-payer-auth-add-step10}
       {#config-payer-auth-add_config-payer-auth-add-step10}

