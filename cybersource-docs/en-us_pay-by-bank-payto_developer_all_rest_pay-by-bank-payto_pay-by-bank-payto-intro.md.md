Introduction to PayTo Pay by Bank {#pay-by-bank-payto-intro}
============================================================

`Cybersource` offers PayTo Pay by Bank, a payment method that enables your e-commerce customers to pay directly from their bank accounts. When using PayTo, your customers do not need to enter their card information. After you integrate PayTo into your checkout experience, your customers select the **Pay by Bank** option. This checkout option enables your customers to choose their bank from a list of trusted partner banks to authorize the payment. After payment approval, the funds transfer from your customer's account to your merchant account. This payment method is an account-to-account (A2A) transfer.

Benefits of Using PayTo Pay by Bank {#pay-by-bank-payto-intro_section_zpr_v3s_fgc}
----------------------------------------------------------------------------------

PayTo provides these benefits for e-commerce payments:

* Immediately transfers funds from the customer's account to your merchant bank account.
* Reduces the amount of customer data you store.
* Using a customer's bank authentication network to securely process payments.
* Avoids card processing fees.
  {#pay-by-bank-payto-intro_ul_aqr_v3s_fgc}

Supported Country and Currency {#pay-by-bank-payto-intro_section_bqr_v3s_fgc}
-----------------------------------------------------------------------------

PayTo is available in Australia and supports payments using the Australian dollar (AUD).

Supported Services
------------------

Sale, refund, and check status services are available with PayTo Pay by Bank. For more information, see these sections:

* [Process a Sale](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-sale-intro.md "")
* [Refund a Payment](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-refund-intro.md "")
* [Check a Status](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-checkstatus-intro.md "")

{#pay-by-bank-payto-intro_ul_iqs_jmz_4gc}  
You can also subscribe to webhook notifications. With webhook subscriptions, `Cybersource` will automatically notify you when a sale or a refund is completed. See [Introduction to Webhooks](/docs/cybs/en-us/pay-by-bank-payto/developer/all/rest/pay-by-bank-payto/pay-by-bank-payto-process-trxn/pay-by-bank-payto-webhooks-intro.md "").

Getting Started with REST {#pay-by-bank-payto-intro_section_cqr_v3s_fgc}
------------------------------------------------------------------------

To process payments through `Cybersource`, set up your payment processing system to be REST compliant. `Cybersource` uses the REST architecture for developing web services. REST enables communication between a client and server using HTTP protocols.  
If you have not set up secure communications between your client and server using either a JSON Web Token or HTTP signature, see the *[Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "")*.
