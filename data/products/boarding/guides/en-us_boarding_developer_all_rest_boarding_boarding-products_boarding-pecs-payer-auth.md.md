`Payer Authentication` {#boarding-pecs-payer-auth}
==================================================

`Payer Authentication` uses the 3-D Secure protocol in online transactions to verify that payment is coming from the legitimate cardholder. Authenticating the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer.

Prerequisites
-------------

You must meet these requirements to enable and configure `Payer Authentication` for your merchants:

* You must include a merchant website URL. 3-D Secure protocol requires that the website URL must be in the format `https://www.example.com`.
* You must include a merchant category code for your merchant.
* At least one 3-D Secure template must be available. For information on creating product templates, see [Product Templates](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-intro-template.md "").

Status
------

When you add Payer Authentication to a merchant account, one of these statuses is assigned:

* Boarded: The Payer Authentication configuration was successfully saved and the merchant can proceed to transact the card network using the specified currency.
* Pending: The Payer Authentication configuration is partially saved or incomplete. Raise a ticket with customer support.
  {#boarding-pecs-payer-auth_d16e53}

