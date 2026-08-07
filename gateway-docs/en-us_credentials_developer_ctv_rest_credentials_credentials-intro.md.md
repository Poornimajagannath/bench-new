Introduction to Credentialed Transactions {#credentials-intro}
==============================================================

Credentialed transactions, also known as credentials‑on‑file (COF) or card‑on‑file transactions, are payments that either store a customer's payment credentials for future use or use previously stored credentials to complete a transaction. All COF transactions begin with a customer-initiated transaction, in which the customer actively participates, such as a card‑present purchase, online checkout, or use of a stored credential.

Benefits of Credentialed Transactions
-------------------------------------

Merchants following the stored credentials framework experience these benefits:

* Better visibility into transaction risk.
* Improved authorization success rates.
* A smoother customer experience.
* Fewer disputes and customer complaints.
* Use of Real Time Relay Account Updater for fresher card details.  
  For more information on the stored credentials framework, see [Improving Authorization Management for Transactions with Stored Credentials](https://usa.relay.com/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf "").

Types of Credentialed Transactions
----------------------------------

There are several types of credentialed transactions:

* **Customer-initiated transaction (CIT):** During a CIT, customers can elect to have their credentials stored for future CITs or for merchant‑initiated transactions (MITs).
* **Merchant-initiated transaction (MIT):** A MIT is processed without the customer's active involvement and include these transactions:
  * **Industry practice transaction:** This MIT is performed as a subsequent transaction to a CIT because the initial transaction could not be completed in one transaction. Not every industry practice transaction involves a stored credential. If a stored credential is used only for one transaction, that transaction is not considered a credentialed transaction.
* **Standing instruction transactions:** This MIT is performed to follow agreed-upon instructions from the customer for the provision of goods and services.

Industry Practice Transactions {#credentials-mit-industry}
==========================================================

Industry practice transactions are MITs performed as follow‑on actions to a previous CIT. Although not all of them require stored credentials, repeated use of credentials qualifies them as COF transactions.  
These industry practice transactions and industry examples are available with your processor:

* [Delayed charges](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-delay-intro/credentials-delay-mit-pan-intro.md ""): Used to add charges after the initial transaction is complete. Examples: hotels (minibar, damages), car rentals (tolls), travel (post-trip charges), and health and wellness add-ons.
* [Incremental charges](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-incremental-intro/credentials-mit-incremental-intro.md ""): Used when an amount exceeds the original authorization. Examples: extending hotel stays, adding rental car insurance, restaurant gratuities, and event upgrades.
* [Reauthorizations](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-reauth-intro/credentials-mit-reauth-intro.md ""): Used when an authorization expires before fulfillment. Examples: long hotel stays, extended rental agreements, multi-week equipment rentals, and delayed subscription boxes.
* [Resubmissions](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-resub-intro/credentials-mit-resub-intro.md ""): Used when a previous authorization attempt fails. Examples: utility auto-pay retries, telecom billing, insurance premiums, and online membership renewals.
* [No-shows](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-noshow-intro/credentials-mit-noshow-intro.md ""): Used when a customer fails to appear for a reserved service for these industries: hotels, rentals, healthcare missed appointments, and restaurant reservation deposits.

`Business Center` Transactions
------------------------------

You can create an industry practice transaction in the `Business Center` by requesting a new authorization. Go to the Transaction Management section and confirm that the new authorization is a MIT. Choose one of these reason types for the authorization:

* Account Top Up
* Delayed Charges
* No Show
* Reauthorization
* Resubmission

This process requires you to have already stored the customer's credentials from a previous customer-initiated transaction. For more information on storing a customer's credentials in the `Business Center`, see [Customer-Initiated Transactions with Credentials on File](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-cit-intro.md "").  
To create an incremental transaction in the `Business Center`, choose one of these options:

* Account Top Up
* No Show

Standing Instruction Transactions {#credentials-intro-stdinst}
==============================================================

Standing instruction transactions are MITs that rely on stored credentials and follow agreed‑upon customer instructions for scheduled or ongoing payments. These transactions must comply with the stored credentials framework, which ensures secure storage and use of customer payment data. All standing instruction transactions begin with a CIT, when customers elect to store their credentials.  
These standing instruction transactions and industry examples are available with your processor:

* [Unscheduled COF](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-ucof-intro.md ""): Occasional, non‑scheduled charges that are made under a customer authorization for these industries:
  * Rideshare and transportation: cleaning fees, damage fees
  * Home services: irregular invoice-based jobs, such as repairs
  * Professional services: unplanned billable hours or fees
  * E‑commerce: back-order fulfillment outside a schedule


* [Installments](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-install-intro.md ""): A fixed purchase that is split into multiple scheduled payments for these industries:
  * Retail and electronics: installment plans for device purchases
  * Furniture and home goods: multi‑month payment plans
  * Education: tuition installment schedules
  * Healthcare financing: payment plans for procedures


* [Recurring](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-recur-intro.md ""): Repeated charges for ongoing services for these industries:
  * Streaming services: video, music, gaming subscriptions
  * Fitness and wellness: gym memberships, coaching subscriptions
  * Insurance: monthly premiums
  * Software and SaaS: business application licenses


* [Subscription Transactions for Mastercard](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-mc-subscription-intro.md ""): Mastercard‑specific recurring billing for subscription‑based services for these industries:
  * Digital media: news, magazines, premium content
  * Subscription boxes: food kits, beauty boxes, hobby crates
  * Online services: cloud storage, identity monitoring
  * Educational platforms: e‑learning subscriptions


* [Standing Order Transactions for Mastercard](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-mit-stand-order-intro.md ""): Merchant‑initiated charges made at regular, agreed-upon intervals for these industries:
  * Utilities: monthly electricity, water, gas payments
  * Telecommunications: phone and internet service billing
  * Loan and mortgage payments: fixed monthly obligations
* Charitable donations: recurring monthly contributions

Requirements for Standing Instruction Transactions {#credentials-reqs}
======================================================================

Merchants who offer stored credentials must:

* Disclose to cardholders how their credentials will be used.
* Obtain the customer's consent to store their credentials.
* Notify customers when the terms of use change.
* Inform the card issuer during an authorization that the credentials are stored on file.
* Identify all transactions that use stored credentials.
  {#credentials-reqs_ul_j2t_dqy_3tb}

Recurring Billing for Recurring Payments {#credentials-mit-recur-rb}
====================================================================

If you are using the Recurring Billing service, do not use this document. `Payment Gateway` saves and stores payment credentials for recurring transactions, ensuring compliance with COF best practices.  
For more information on Recurring Billing, see *[Recurring Billing](https://developer.example.com/docs/gateway/en-us/recurring-billing/developer/all/rest/recurring-billing-developer/recur-bill-services-intro.md "")*.

Transaction-Specific Fields {#credentials-matrix}
=================================================

To make an authorization request into a credentialed transaction, you must include additional fields that inform `Payment Gateway` to either store the customer's payment information for future use, or to use an already stored card-on-file for the payment. This section describes the additional required fields that create an initial and subsequent credentialed transaction.

Initial Transactions
--------------------

For an initial transaction, include these fields with a standard authorization request:

[processingInformation.authorizationOptions. initiator. credentialStoredOnFile](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")
:
Set the value to `true`.

[processingInformation. authorizationOptions. initiator. merchantInitiatedTransaction.reason](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:
Some processors and card types require a reason code when storing payment credentials.

[processingInformation. authorizationOptions. initiator. type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set the value to `customer`.

[processingInformation. commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set to one of these possible values:

    * `internet`: Online transaction.
    * `MOTO`: Mail order/telephone order transaction.
    * A payer authentication value.  
      See [Payer Authentication Values](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-ref-info-intro/credentials-ref-info-payerauth.md "").
    {#credentials-matrix_ul_ejm_5rv_yhc}

{#credentials-matrix_dl_jjm_5rv_yhc}

```
{
  "processingInformation": {
    "commerceIndicator": "internet",
    "authorizationOptions": {
      "initiator": {
        "type": "customer",
        "credentialStoredOnFile": true,
        "merchantInitiatedTransaction": {
          "reason": "7"
        }
      }
    }
  }
}        
```

When you receive the initial transaction response, save the transaction identifier, which is located in the id field. You need the transaction identifier for subsequent transactions. If you are using the Token Management Service (TMS), `Payment Gateway` stores the transaction identifier for you.  
This table shows the fields required for each type of CIT and initial transaction.  
![](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/credentials/images/cred-matrix-cit-rest-600x340.svg/jcr:content/renditions/original)

Subsequent Transactions
-----------------------

For a subsequent transaction, include these fields with a standard authorization request:

processingInformation.authorizationOptions. initiator. merchantInitiatedTransaction. previousTransactionID
:
* American Express: Set the value to the transaction ID from the original transaction.
* Discover: Set the value to the transaction ID from the original transaction.
* Relay: set the value to the last successful transaction ID.

[processingInformation. authorizationOptions. initiator. merchantInitiatedTransaction.reason](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:
Some processors and card types require a reason code when you use stored payment credentials.

[processingInformation. authorizationOptions. initiator. storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:
Set the value to `true`.

[processingInformation. authorizationOptions. initiator. type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set the value to `merchant` for MIT transactions.

[processingInformation. commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set to one of these possible values:

    * `install`: Installment payment
    * `internet`: E-commerce order
    * `MOTO`: Mail order or telephone order
    * `recurring`: Recurring payment
    * A payer authentication value.  
      See [Payer Authentication Values](/docs/gateway/en-us/credentials/developer/ctv/rest/credentials/credentials-ref-info-intro/credentials-ref-info-payerauth.md "").
    {#credentials-matrix_ul_drx_ds1_zhc}

{#credentials-matrix_dl_crx_ds1_zhc}

```
{
  "processingInformation": {
    "commerceIndicator": "internet",
    "authorizationOptions": {
      "initiator": {
        "type": "merchant",
        "storedCredentialUsed": true,
        "merchantInitiatedTransaction": {
          "reason": "7",
          "previousTransactionId": "123456789123"
        }
      }
    }
  }
}        
```

{#credentials-matrix_codeblock_sx1_gyb_tvb}  
This table shows the values for subsequent authorization fields.  
![](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/credentials/images/cred-matrix-mit-rest-600x390.svg/jcr:content/renditions/original)
