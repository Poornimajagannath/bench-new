`Payer Authentication` {#boarding-payer-auth}
=============================================

`Payer Authentication` uses the 3-D Secure protocol in online transactions to verify that payment is coming from the legitimate cardholder. Authenticating the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer.

Prerequisites
-------------

You must meet these requirements to enable and configure `Payer Authentication` for your merchants:

* You must include a merchant website URL. 3-D Secure protocol requires that the website URL is in the format `https://www.example.com`. For information on adding a merchant website to your merchant account information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
* You must include a merchant category code for your merchant. For information on adding a merchant category code to your merchant account information, see [Add Merchant Account Information](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-reg-intro/merchants-v2-add-merchant/merchants-v2-add-merch-acct-info.md "").
* At least one 3-D Secure template must be available. For information on creating product templates, see [Product Templates](/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-intro-template.md "").

Status
------

When you add Payer Authentication to a merchant account, one of these statuses is assigned:

* Boarded: The Payer Authentication configuration was successfully saved and the merchant can proceed to transact the card network using the specified currency.
* Pending: The Payer Authentication configuration is partially saved or incomplete. Raise a ticket with customer support.
  {#boarding-payer-auth_ul_gn4_xfb_q2c}

