Introduction to Pay by Bank {#paybybank-intro}
==============================================

Pay by Bank is a solution that enables you to offer your e-commerce customers the ability to pay directly from their bank account in real time without providing payment card information. When a payment is processed, your customer's bank transfers the funds directly to your merchant bank account.  
In the UK, Pay by Bank follows the open banking regulations for bank-to-bank transfers.

Benefits of Using Pay by Bank
-----------------------------

Pay by Bank makes processing e-commerce transactions simpler, faster, and more secure by:

* Reducing customer data storage because card data is no longer needed.
* Streamlining reconciliation data into an easy-to-read report.
* Using a customer's bank authentication network to securely process payments.
* Avoiding card processing fees.
* Providing an easy connection to Pay by Bank through an API integration.

Supported Services
------------------

Sale, refund, and check status services are available with Pay by Bank. For more information, see these sections:

* [Sale](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-sale-intro.md "")
* [Refund](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-refund-intro.md "")
* [Check Status](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-status-intro.md "")

You can also subscribe to webhook notifications. With webhook subscriptions, `Cybersource` automatically notifies you when a sale or a refund is complete. See [Webhook Subscriptions](/docs/cybs/en-us/pay-by-bank/developer/all/rest/pay-by-bank/paybybank-intro-services/paybybank-webhook-intro.md "").

Requirements
------------

You must have a merchant ID for each country in which you process transactions. Contact your `Cybersource` account manager for more information.

Supported Currencies
--------------------

This table lists the currencies supported by the Pay by Bank services.

|        Currency        | Currency Code |
|------------------------|---------------|
| British pound sterling | `GBP`         |
| Euro                   | `EUR`\*       |
[Supported Currencies]

\*Refunds are not currently supported for EUR.
