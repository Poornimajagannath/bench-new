eCheck Merchant Guide {#doctemp-about-guide}
============================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is for merchants who implement and use the eCheck service, either in the `Business Center` or by using the APIs.

Conventions
:
These statements appear in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the `Cybersource` documentation hub for additional technical documentation.

    [https://developer.cybersource.com/docs.html](https://developer.cybersource.com/docs.md "")

Customer Support
:
For support information about any service, visit the Support Center:

[http://support.visaacceptance.com](http://support.cybersource.com "")

Recent Revisions to This Document {#devtemp-doc-revisions}
==========================================================

25.08.01
--------

Process eCheck Transactions Using the REST API
:
Added links in the field lists to the field descriptions in the *REST API Field Reference Guide*.

25.06.01
--------

Payment Links Added
:
Added acceptance of eCheck payments through websites and invoices. See [Accepting eCheck Payments through Payment Links](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-pay-unified-checkout-invoice-paybylink-intr/echeck-bc-pay-by-linkdita.md "") and [Accepting eCheck Payments through Invoices](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-pay-unified-checkout-invoice-paybylink-intr/echeck-bc-invoicing.md "").

25.05.01
--------

Added Support for `Unified Checkout`
:
Added acceptance of eCheck payments through `Unified Checkout`. See [Accepting eCheck Payments through Unified Checkout](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-pay-unified-checkout-invoice-paybylink-intr/echeck-pay-unified-checkout.md "").

24.10.01
--------

Processing eCheck Transactions Using the REST API
:
Updated these procedures:

    * [Processing an eCheck Debit Transaction Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro/echeck-api-debit-intro.md "")
    * [Processing a Recurring eCheck Debit Transaction Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro/echeck-api-recurring-intro.md "")

    Added these procedures:

    * [Creating an eCheck Token Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro/echeck-api-cre-token-standalone.md "")
    * [Creating an eCheck Token and Processing an eCheck Transaction Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro/echeck-api-cre-token-with-txn.md "")
    * [Using an eCheck Token to Submit an eCheck Debit Transaction Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro/echeck-api-use-token-submit-debit-txn.md "")

24.09.01
--------

Initial release.

Introduction to the eCheck Service {#echeck-txnprocess-intro}
=============================================================

The eCheck payment service enables merchants to accept electronic check payments using a variety of methods, including mail, telephone, and online orders.  
There are two main types of eCheck transactions:

* A charge is initiated to take money from a customer's bank account and transfer it to the merchant's bank account. Most eCheck transactions are ACH charges.

* A credit or refund is initiated to transfer money back to the customer's bank account.  
  eCheck information can be used in a range of reports. For further information, see these topics:

* [Fields in the Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding/echeck-reports-recon-funding-fields.md "")

* [Fields in the Chargeback Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-chargeback/echeck-reports-recon-chargeback-fields.md "")

* [Fields in the Deposit Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-deposit/echeck-reports-recon-deposit-fields.md "")

* [eCheck Reconciliation Reporting Case Study](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-use-case.md "")

Requirements for Using the eCheck Service
-----------------------------------------

The eCheck service is available to eligible Visa Acceptance Solutions merchants that meet one of these two requirements:

* US citizens or residents who are at least 18 years of age and have been issued a Social Security number.
* United States or foreign-based corporations that use the eCheck services only for customers using US bank accounts and that hold and maintain a bank account in the United States with a US-based financial institution.

eCheck Transaction Types {#echeck-intro-txn-types}
==================================================

There are several ways that eCheck transactions may be originated or received. Each of these transactions is governed by requirements established by the National Automated Clearinghouse Association (Nacha).  
Your ability to process any or all of the supported eCheck transaction types depends on the underwriting and risk profile of your eCheck account.  
The type of eCheck transactions that you process also depends on your business model. For example, if you are a mail order/telephone order (MOTO) merchant, you might need to process only transactions initiated over the telephone. However, if you submit transactions exclusively through your e-commerce website, you may need the ability to process all transaction types except for telephone-initiated transactions.

Cash Concentration or Disbursement
----------------------------------

A Cash Concentration or Disbursement (SEC code CCD) is a charge or credit transaction against a customer's business checking account. One-time or recurring CCD transactions are typically fund transfers to or from corporate entities.

* CCD transactions may be submitted only against business or corporate checking accounts.
* An authorization agreement from the corporate customer is required for CCD transactions.

Prearranged Payment and Deposit
-------------------------------

A Prearranged Payment and Deposit (SEC code PPD) is a charge or credit transaction initiated by a merchant against a customer's personal checking or savings account. All credit transactions to personal banking accounts must be submitted as PPD, regardless of the original transaction type. These considerations apply:

* PPD transactions may be submitted only against personal checking and savings accounts. PPD transactions may be originated only when payment and deposit terms between the merchant and the customer are prearranged and in writing. The terms and transaction schedule are arranged between the customer and the merchant in advance of the actual date and time at which the transaction is submitted. PPD transactions cannot be used for telephone-initiated or internet-initiated transactions or for converting a paper check into an electronic payment.
* A written paper authorization from the customer is required for one-time transactions. A written paper authorization agreement indicating that the customer is authorizing a recurring charge to their bank account is required for recurring transactions. For PPD transactions, the customer's payment authorization may NOT be received by telephone or the internet.
* For recurring PPD transactions, the customer may revoke the standing payment authorizations (for example, calling a given telephone number or writing to a given address). Merchants are required to notify customers in writing at least 10 calendar days in advance of when the date or amount of an eCheck transaction is changed.

Telephone-Initiated Entry
-------------------------

A Telephone-Initiated Entry (SEC code TEL) is a one-time or recurring charge transaction against a customer's personal checking or savings account.

* TEL transactions may be originated only when a business relationship between the merchant and the customer already exists. If no relationship exists, TEL entries can be originated only when the customer initiates the telephone call to the merchant. An existing business relationship is defined as follows:

  * A written agreement is in place between the merchant and the customer.
  * The customer has purchased goods or services from the merchant within the past 2 years.
* Affiliates or partners of the merchant are not considered to have an existing relationship with a customer by association. A TEL transaction may not be used by a merchant when there is no existing relationship between the merchant and the customer and the merchant has initiated the telephone call.

* Payment authorization is obtained from the customer via the telephone for each TEL transaction. Prior to the eCheck transaction, authorizations must be either:

  * audio-recorded by the merchant or
* provided to the customer in writing.  
  For an oral authorization obtained over the telephone to be valid, the merchant must record a clear statement of the following:

* that the customer is authorizing a charge to their bank account

* that the customer understands the terms of the authorization, including:

  * customer's name
  * date of the authorization
  * date on or after which the customer's banking account will be charged
  * amount to be charged
* telephone number that is available to the customer during normal business hours  
  Either a copy or the original audio recording of the authorization or the written notice of authorization must be retained for two (2) years from the date of the authorization.

Internet-Initiated/Mobile Entry
-------------------------------

An Internet-Initiated / Mobile Entry (SEC code WEB) is a charge against a customer's personal checking or savings account. One-time or recurring WEB transactions may be initiated by using the internet or a mobile device on a wireless network.  
WEB transactions may only be submitted against personal checking and savings accounts. Merchants are responsible for preventing potentially fraudulent transactions by ensuring that WEB transactions are received from customers whose identities are authenticated, whether it is a PIN at the time of checkout or some other means required by the merchant.  
For a WEB entry, authorization is received from the customer from the internet or a mobile device on a wireless network during the payment or checkout process. Implementation of payment authorization language is up to the merchant, as long as it complies with the authorization requirements stated below. We recommend that payment authorization language appear on the same page that collects the customer's banking account information.  
The customer's payment authorization must meet these requirements:

* Be displayed on a computer screen or other visual display that permits the customer to read or print it.
* Be readily identifiable as an authorization.
* Clearly and conspicuously state its terms including the dollar amount, the effective date of the transfer, and whether the authorization is for a one-time purchase or for a recurring transaction.

For obtaining payment authorizations associated with WEB transactions, an authorization statement combined with a clickable button should be considered. It should clearly state that by clicking the button, the customer is providing authorization.  
For recurring WEB transactions, the merchant must also provide a notice that the customer may revoke the standing payment authorization by notifying the merchant as specified in the payment authorization (for example, calling a given telephone number or writing to a given address). Merchants are required to notify customers at least 10 calendar days in advance of when the date or amount of a recurring eCheck transaction is changed. This notification need only be given once, in advance of the next recurring transaction.

Getting Started with the eCheck Service {#echeck-gs}
====================================================

The eCheck payment service enables merchants to accept electronic check payments using a variety of methods, including mail, telephone, and online orders.  
The eCheck service is available to eligible Visa Acceptance Solutions merchants that meet one of these two requirements:

* U.S. citizens or residents who are at least 18 years of age and have been issued a Social Security number.
* United States or foreign-based corporations that use the eCheck services only for customers using US bank accounts and that hold and maintain a bank account in the United States with a US-based financial institution.

eCheck Application {#echeck-application-intro}
==============================================

To apply for the eCheck service, submit an application that contains information about your business. The Visa Acceptance Solutions Risk Team reviews your eCheck service application and accompanying documentation based on pre-determined underwriting criteria. Visa Acceptance Solutions may request additional information or documentation from you before making a decision about your application. In addition, a risk reserve (the withholding of a percentage of eCheck funds to cover potential costs incurred by high-risk transactions) may be required prior to activation of the service. After your application is reviewed, you will be notified via email of the underwriting decision. If your application is declined, the email will provide the reason(s) for the decline.

Submitting the eCheck Application {#echeck-application-procedure}
=================================================================

Follow these steps to submit the eCheck application:

1. Log in to the `Business Center`:
   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-application-procedure_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-application-procedure_d7e38}
2. In the left navigation panel, click Available Products. The Available Products page displays.
3. In the eCheck section, click Enable. The eCheck Application page displays.
4. Enter the information in the fields. All information is required. For an explanation of the application fields, see [Completing eCheck Application Fields](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-gs/echeck-application-intro/echeck-application-fields.md "").
5. Read the eCheck Services Agreement. Check the box to agree.
6. Click Submit to submit the application. You will receive an email confirming receipt. An underwriter will review the application and respond with any additional questions they have.

Completing eCheck Application Fields {#echeck-application-fields}
=================================================================

The merchant application contains these sections, which you must fill out completely.

Primary Owner Identifying Details
---------------------------------

Enter the identifying and contact information about the primary owner.  
To prevent fraud and ensure regulatory compliance, the federal government requires us to collect the Social Security number of the business owner. Non-US persons who do not have a Social Security number may provide their passport number, an alien identification card number, or number and country of issuance of any other government-issued document evidencing nationality or residence and bearing a photograph or similar safeguard.

Primary Owner Address Information
---------------------------------

Enter the address information about the primary owner. The owner must have an address in the same country as the business address.

Primary Owner Ownership Details
-------------------------------

Enter the job title and ownership percentage of the primary owner.

Additional Owners
-----------------

Per US Treasury customer due diligence requirements, all owners with 25 percent or greater ownership, or significant responsibility to control, manage, or direct the company must be declared.

Ownership Details
-----------------

Enter the details of the business.  
The Doing Business As name is the business's assumed, trade, or fictitious name. This name might be the same as the legal business name.  
The federal tax ID is the 9-digit tax identification issued to the business by the US government and used for tax reporting purposes. For sole proprietors, this number might be your Social Security number.

Business Address Information
----------------------------

Enter the address of the business. If it is the same as the primary owner's address, click Import from Owner Address. The owner must have an address in the same country as the business address.

Industry Information
--------------------

From the drop-down menu choose the merchant category code that fits your business.

Business Process Information
----------------------------

Enter information about your business's process.  
*Time frame to product delivery* is how long it takes for the customer to receive their product after paying for the order. If you are providing a product or service that is paid for at the time of or after delivery, enter 0.  
*Estimated Total Monthly Sales* is the total dollar amount of eCheck sales that you expect to process each month through this account. Do not include payment volume from other methods, such as credit cards or wire transfers.  
*Average Order Amount* is the average dollar amount of each individual order or sale. If you are a new business and are unsure of the amount, you may list the average price of your products and services for sale.  
*Largest Expected Order Amount* is the dollar amount of the largest order you expect to have. If you have a new business and are unsure, you may list the dollar amount of your most expensive product or service for sale.

Deposit Account Information
---------------------------

Enter information about the account to which you want funds deposited. This account might also be debited for any accrued fees, chargebacks, refunds, returns, or other amounts owed related to the eCheck account.  
*Routing Number* is the nine-digit routing number for your bank. It is printed on the bottom of your checks. If you do not have checks, contact your bank for the number.  
*Account Number* is the number of the bank account in which funds from your sales will be deposited.

eCheck Settings
---------------

Enter the eCheck descriptor.  
*eCheck descriptor* is the name that appears on the charge in your customer's bank statement. It should be the name they associate with your company. Most often it will be your business name or website URL and might need to be abbreviated to fit the 10-character limit.

Service Agreement
-----------------

Read the eCheck Service Agreement. Check the box to agree.  
Click Submit to submit the application. You will receive an email confirming that it has been received. An underwriter will review the application and respond with their decision or ask for additional details if needed.

Boarding Your Merchant Account for Sandbox Testing {#echeck-partner-onboard-sandbox-merchant}
=============================================================================================

This topic describes how to board the merchant account (MID) that you plan to use for testing eCheck transactions in the sandbox environment. IMPORTANT In order to perform this task, your MID must be enabled for eCheck with self-enablement allowed. If you need to verify the status of your MID, contact your partner user.  
At the final step of the task, upon submittal of the eCheck Application with test data, your MID is automatically enabled for eCheck.

1. Follow these steps to board your merchant account for sandbox testing:
2. Log in to the sandbox `Business Center` as the MID user:  
   ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-partner-onboard-sandbox-merchant_d7e29}
3. In the Available Products module, complete the eCheck Application with the test data you want to use in the sandbox testing environment.  
   For descriptions of fields in the eCheck Application, see [Completing eCheck Application Fields](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-gs/echeck-application-intro/echeck-application-fields.md "").
4. Click Submit.  
   Unlike an eCheck Application submitted for production processing, this eCheck Application does not go through underwriting because this MID is used only for test transactions.

#### RESULT

When the eCheck Application is submitted with test data, your MID is automatically enabled for eCheck.

Overview of eCheck Transaction Processing {#echeck-txnprocess-overview}
=======================================================================

This sequence describes eCheck transaction processing.

1. The merchant receives authorization from a customer to charge their bank account. The customer provides all of the required bank account information for the eCheck transaction type. After the transaction is submitted, purchase and payment information is securely transmitted to the Payment Gateway server. The transaction is accepted or rejected based on initial data validation and security criteria defined by `Cybersource`. Reasons for rejection include invalid routing number, inactive account number, and insufficient information.
2. If the transaction is accepted, `Cybersource` formats the transaction information and sends it as an ACH transaction to its bank, the Originating Depository Financial Institution (ODFI), with the rest of the transactions received that day.
3. The ODFI receives the transaction information and passes it to the ACH network for settlement. The ACH network uses the bank account information provided with the transaction to determine the bank that holds the customer's account, the Receiving Depository Financial Institution (RDFI).
4. The ACH network instructs the RDFI to charge the customer's account. The RDFI passes funds from the customer's account to the ACH network. The RDFI also notifies the ACH network of any administrative returns (funds could not be collected from the customer's bank account) or unauthorized returns (the customer disputes the purchase). An eCheck transaction might be returned for not sufficient funds (NSF), invalid account number, account closed, or account frozen. An eCheck transaction might be returned as unauthorized because the customer advised that it was not authorized, payment was stopped, or authorization was revoked. When a transaction is returned, `Cybersource` posts the return to the merchant.
5. The ACH network sends the funds to the ODFI (the bank associated with `Cybersource`).
6. The ODFI sends any returns to `Cybersource`.
7. After the funds holding period, `Cybersource` initiates a separate ACH transaction to deposit eCheck proceeds to the merchant's bank account.

eCheck Settlement {#echeck-txnprocess-settlement}
=================================================

Because eCheck payments are made from a customer's bank account, the settlement process is different from the credit card transaction settlement process. For eCheck transactions, settlement occurs when the payment gateway initiates an ACH transaction to collect funds from the customer's bank account. Funding occurs when funds collected are deposited to the merchant's bank account. The timing of eCheck deposits might vary by merchant. Settlement for eCheck transactions occurs each business day, excluding bank holidays. eCheck transactions submitted to `Cybersource` before your daily transaction cut-off time are sent to the bank the following business day. The settlement time for each batch of transactions marks the beginning of the `Cybersource` funds holding period. Transfer of eCheck proceeds to your bank account occurs on the business day after the transactions are considered collected by the system.
IMPORTANT The availability of funds is not verified in real time, so you should wait until the holding period is over before shipping or providing access to merchandise purchased using eCheck.  
The timeframe for settlement, returns, and funding can vary. These factors can influence timing: the day of the week the transaction is submitted, the number of holding days established for your eCheck account, whether the transaction is returned for any reason, or whether processing occurs over a weekend. eCheck transactions begin their funding when a transaction is captured and settled.  
This sequence describes a typical eCheck processing cycle with a 5-day holding period:

1. The merchant receives an eCheck transaction. At the transaction cut-off time, the transaction is picked up by the payment gateway.
2. The payment gateway submits the previous day's batch to the ACH network. This is the first day of the funds holding period. The number of holding days varies per merchant. For example, 5 days.
3. The ACH network collects funds for the transaction from the customer's bank and sends them to `Cybersource`. This is the second day of the funds holding period. The purpose of the holding period is to allow for returns for transactions included in the batch. Returns can come back on this day.
4. Third, fourth, and fifth day of the funds holding period. Returns can come back on this day.
5. The payment gateway sends available eCheck proceeds to the merchant's bank account. Returns can come back on this day.
6. The eCheck proceeds are available in the merchant's bank account. Returns can come back on this day.
   Processing only occurs on banking days, so the timeframe can be extended depending on what day of the week processing and holding days occur. For example, if day 1 in the example above is a Friday, day 2 does not occur until Monday, 2 days later, prolonging the timeframe by 2 days.

eCheck Returns {#echeck-txnprocess-returns}
===========================================

eCheck transactions consists of several validation phases. When first submitted to `Cybersource`, eCheck transactions are validated for the presence of required data, such as the bank account number and ABA routing number. After the transaction is submitted to the ACH network, it undergoes additional validations, for example, whether the customer's bank account exists and whether there are enough funds in the bank account. A transaction might be returned for various reasons. An eCheck transaction can pass the initial phases of validation and be returned or rejected later in the cycle.  
These are the three types of eCheck returns:

Insufficient funds (NSF) return
:
This type of return occurs when the customer's bank account does not have sufficient funds for the eCheck transaction.

Unauthorized return (chargeback)
:
These transactions are unauthorized returns:

    * The customer claims they did not authorize the eCheck transaction or had revoked their authorization.
    * The transaction was for a different dollar amount than was originally authorized.
    * The transaction was settled prior to the date of the customer's authorization.

:
Additional reasons for chargebacks are listed in [eCheck Chargebacks](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-txnprocess-overview/echeck-txnprocess-settlement/echeck-txnprocess-chargebacks.md "").

Administrative returns or returned items
:
This type of return includes all other reasons for a return, such as these:

    * Account is closed.
    * Account number is invalid.
    * Non-transaction account.
    * Account is frozen.

> IMPORTANT
> ` Cybersource ` does not automatically resubmit charges returned from a customer's bank due to NSF. You can resubmit transactions returned as NSF or uncollected funds up to two additional times for a total of three submissions. Continued attempts can result in a fine and possible sanctions from Nacha.  
> All unsuccessful eCheck transactions returned through the ACH network includes a return code to indicate the reason for the return. You are responsible for taking any appropriate action when eCheck transactions are returned. The amount of each return is posted to your eCheck settlement account and statement.

eCheck Chargebacks {#echeck-txnrprocess-chargebacks}
====================================================

For transactions made from personal checking and savings accounts, Nacha grants 60 calendar days during which a customer may return a charge item erroneously posted to the customer's bank account. The 60-day window begins the day the bank first made its statement with the transaction listed available to the customer.

> IMPORTANT
> If your eCheck return rates exceed Nacha thresholds, Nacha might require additional information. You will be notified by ` Cybersource ` and must immediately respond and become compliant. After becoming compliant you must maintain compliance for the next 180 days. If you cannot reach and maintain compliance, your account might be terminated.

| Return Type    | Nacha % Threshold | FNBO Volume Threshold | Days to Comply | Maintenance Period |
|:---------------|:------------------|:----------------------|:---------------|:-------------------|
| Unauthorized   | 0.50%             | 5 items               | 30 days        | 180 days           |
| Administrative | 3.0%              | 15 items              | 60 days        | 180 days           |
| Total          | 15.0%             | 25 items              | 60 days        | 180 days           |
[Nacha Thresholds for eCheck Returns]

Take precautions to minimize the risk of losses when using the eCheck service. To reduce the potential for chargebacks, you must ensure that you are receiving the proper payment authorization prior to processing an eCheck transaction. You may also want to consider waiting to ship goods until after eCheck transaction proceeds are deposited in your merchant bank account (following the required `Cybersource` holding period).

eCheck Credits and Refunds {#echeck-txnrprocess-creditsrefunds}
===============================================================

You may issue credits and refunds for eCheck transactions. The following requirements apply:

* The original eCheck transaction must have been processed through the Payment Gateway.
* eCheck refunds must be submitted with the transaction ID of the original eCheck transaction.
* The amount of the refund must be less than or equal to the amount of the original transaction.
* The sum of multiple refunds submitted against the original transaction must be less than or equal to the amount of the original transaction.
* Your eCheck settlement sub-account must contain available funds (funds that are no longer in the holding period) to cover the refund. If your account does not contain sufficient funds, the refund is rejected.

eCheck Transaction Statuses During Processing {#echeck-status}
==============================================================

A successful eCheck transaction goes through these status changes while it is being processed. All other statuses are standard payment statuses. For information about a specific response, see the [Transaction Response Codes Tool](https://developer.cybersource.com/api/reference/response-codes.md "").

* *Pending*: Transaction was submitted to the payment gateway.
* *Transmitted*: Transaction was sent to the bank or financial institution for settlement.
* *Completed*: No returns was received for this transaction 3 days after it was sent for settlement. The transaction is considered to be completed unless an atypical return is received later.

eCheck Integrations {#echeck-integrations}
==========================================

The eCheck service can be accessed in two ways:

* In the `Business Center`. See [Process eCheck Transactions Using the Business Center](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-bc-intro.md "")
* Using the REST API. See [Process eCheck Transactions Using the REST API](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-api-intro.md "")

eCheck Risk Reserve {#echeck-risk-reserve}
==========================================

A risk reserve account might be required as a condition for providing eCheck services. The risk reserve account holds a certain percentage or amount of your eCheck proceeds in reserve to cover potential costs incurred from high-risk or chargeback transactions. To see how risk reserve works in a use case, see [eCheck Reconciliation Reporting Case Study](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-use-case.md "").  
The risk reserve rate and target are determined during the underwriting process and communicated to the merchant when the application is accepted or might be requested at a later date based on financial condition, processing history, or increased limits.  
A reserve might also be implemented at any time after the account is opened based on an increase in returns, chargebacks, or other risk factors.  
Factors considered when determining whether a risk reserve account is required for your eCheck account might include:

* How long your company has been in business.
* How long your company has conducted business with `Cybersource`.
* Your company's transaction history with `Cybersource`.
* The credit-worthiness of the financial information you have provided.
* The credit-worthiness of the personal guarantee you have provided.
* Your company's industry type.

The risk reserve is specified by these values:

* The *Reserve Rate* is the percentage rate at which funds are withheld from each eCheck batch settlement for your account.
* The *Reserve Target* is the maximum dollar amount that can be held in your risk reserve account.

A merchant can either have a [fixed reserve](# "") or [no reserve (none)](# "").  
For a [fixed risk reserve](# ""), the reserve balance is established by one of these factors:

* The receipt of a lump sum deposit from you, the merchant.
* Withholding funds at the reserve rate established for the account from each batch settlement until the reserve balance is equal to the *Reserve Target*.
  Your fixed risk reserve can also be established by a combination of lump sum deposit and withholding of settlement funds.  
  As funds are transferred from your eCheck settlement sub-account to the reserve sub-account, the eCheck settlement balance is reduced and the reserve balance is increased by the same amount.  
  Fixed reserves are not automatically released to your merchant bank account; manual intervention is required. Risk reserve funds are withheld at the reserve rate until the reserve target is met. In the event that the reserve target setting for your account is reduced, the difference between the reserve balance and the new reserve target are transferred back to the eCheck settlement account, where available funds will be subsequently deposited to your bank account. When your reserve rate and reserve target are modified, changes become effective for the next batch settlement.

eCheck Processing Limits and Settings {#echeck-processing-limits}
=================================================================

When completing the eCheck application, you can request that a specific monthly and per-transaction limit be considered. However, the eCheck processing limits are determined during the underwriting process for your application. The requested amounts should be based on what you anticipate processing with eCheck. After sufficient processing history is established, you can request a limit increase at the Support Center at [support.visaacceptance.com](https://support.visaacceptance.com ""). At that time, the `Cybersource` Risk Team will review your account history and can approve, modify, or decline the request to increase your processing limits.
IMPORTANT If you exceed the monthly processing limit, a funding hold is applied to your account and you must contact the Support Center to remove the hold and increase your limit, if needed, based upon your account history.  
Processing settings include:

* *Per-Transaction Limit*: maximum amount allowed for a single eCheck transaction.
* *Monthly Processing Limit*: total amount of charges and refunds allowed per month for eCheck transactions.
* *Funds Holding Period*: number of days that funds from settled eCheck transactions are held before being deposited to your merchant bank account.

eCheck Notice of Change {#echeck-txnprocess-noc}
================================================

A Notification of Change (NOC) is an ACH notice from a customer's bank indicating that an eCheck transaction included incorrect customer or payment information. The bank will correct the information, post the transaction to the customer's bank account, and notify you that payment information needs to be updated. All NOCs will include a code that indicates the necessary change. You are responsible for taking any appropriate action when an NOC is received.  
You must make the necessary changes prior to originating the next eCheck transaction for the same customer. If you are using Recurring Billing be sure to update information in your subscription records. `Cybersource` maintains a database of all NOC entries. All submitted eCheck transactions are screened against this list. If the data is not corrected, you will receive an error when attempting to process a new transaction for the customer. Repeated attempts to submit an uncorrected transaction may result in a fine and sanctions from Nacha.  
You may view Notifications of Change received for your eCheck transactions in the `Business Center`:

1. Click Reports in the left navigation.
2. Under Transaction Reports, click Notification of Change.
3. Select the Date Range and click Search to run the report.

Payment Authorization and Authentication for eCheck Transactions {#echeck-txnprocess-pmtauth}
=============================================================================================

eCheck transactions must include both payment authorization and customer authentication in order to be successful.  
For eCheck transactions, an authorization is a paper or electronic document or record "signed" by the customer that authorizes a merchant to submit a charge transaction against their bank account. Merchants are required to obtain authorization from their customer before charging the customer's bank account. Payment authorization must include:

* Clear and conspicuous statement of the terms of the transaction, including amount.

* Written language displayed to the customer that is readily identifiable as an authorization by the customer for the transaction (for example, "I authorize \[Merchant\] to charge my bank account") and that can be reproduced.

* Evidence of the customer's identity.

* The date the authorization was granted and the effective date of the transaction (the transaction may not be processed before the effective date).

* The bank account number to be charged. Only US-based personal checking, savings, and business checking accounts may be used for processing eCheck transactions. Some banks may disallow certain types of these accounts from being used. Contact your bank to verify the types of checking accounts from which you may process eCheck transactions.

* The nine-digit ABA routing number of the customer's bank. The customer can locate their bank's ABA routing number, as well as their bank account number, at the bottom of one of their paper checks.  
  For recurring transactions, the following must also be provided:

* The frequency of the charge.

* The period for which the customer's payment authorization is granted.

* Written language indicating that the customer may revoke the authorization by notifying the merchant as specified in the authorization.
  For eCheck transactions, once a merchant has sufficiently authenticated a customer's identity through a credit check or review of identification, the merchant can issue identity credentials that will allow the customer to set up an account with username and password or personal identification number (PIN) for online transactions at the merchant's site. Identity authentication and payment authorization must occur simultaneously.
  IMPORTANT It is not acceptable to identify a customer when they log in to a website and then later consider that login an authentication when authorizing an ACH transaction.

eCheck Records Retention Requirements {#echeck-txnproces-recret}
================================================================

You must retain all authorizations for 2 years after a transaction completes, after a final recurring transaction, or after a payment authorization is revoked.

* For paper authorizations, you must retain the original authorization.
* For authorizations made over the telephone or over the internet, you must retain a copy of the authorization and a record of the authentication.
* For transactions that involve a paper check, you must retain a copy of the check for a minimum of 2 years because the signed check is considered the customer's authorization.  
  Nacha grants customers 60 days to identify an unauthorized charge. If a customer identifies an unauthorized charge after the 60-day period, the customer's bank can request a copy of the original authorization for the transaction from the merchant through the ODFI. If the appropriate authorization is not provided to the customer's bank within 10 banking days, the ODFI is permitted to allow the customer's bank to return the transaction.

> IMPORTANT
> Although Nacha and ` Cybersource ` require record retention for customer authorization records for a period of 2 years, the statute of limitations for state laws governing transaction disputes may dictate a period of between 2 to 7 years. ` Cybersource ` recommends that you be familiar with these laws.  
> You must be able to provide a copy of the authorization to the customer upon request. `Cybersource` might also request the original or a copy of a customer's payment authorization at any time. Merchants will have 3 business days to comply. If no response is received by the date requested, to avoid a Nacha rules violation, `Cybersource` will give permission for the return. If two future requests also go unanswered, `Cybersource` assumes that you are giving blanket permission to allow all returns and then accepts them on your behalf.

Manage eCheck Settings in the `Business Center` {#echeck-bc-settings-intro}
===========================================================================

This section describes how to use the eCheck module in the `Business Center` to view and manage your eCheck settings, business information, and owner information for your MID. You can also view your account balance and processing limits. IMPORTANT

> To view and edit eCheck-related information in these categories, you must perform step-up authentication:
>
> * Personally identifiable information about business owners on file for your account.
> * Payment account number (PAN) of the card used for funding all your ` Business Center ` transactions.
>   For more information, see [Accessing eCheck Settings in the Business Center](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-bc-settings-intro/echeck-bc-settings.md "").  
>   To grant individual team members access to the eCheck module for your MID, use the Account Management module in the `Business Center`, create user roles that specify user permissions to the eCheck module, create user accounts for your team members, and assign each user account to one of the roles you created. For more information, see [Creating Roles](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-bc-settings-intro/echeck-bc-permissions/echeck-bc-permissions-roles.md "").

Managing Merchant Permissions in the `Business Center` {#echeck-bc-permissions}
===============================================================================

The topics in this section describe how to grant access to the eCheck module for your MID.  
Before they can access the eCheck module, your team members must have user access permissions. To grant individual team members access to the eCheck settings for your MID, create user roles with user permissions to access the eCheck module, create user accounts for your team members, and assign each user account to one of the roles you created.

Creating Roles {#echeck-bc-permissions-roles.dita}
==================================================

Follow these steps to create a new user role:

1. Log in to the `Business Center`:

   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-bc-permissions-roles.dita_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-bc-permissions-roles.dita_d7e38}
2. Account Management \&gt; Roles. The Terminal Settings Page appears.

3. Click **Add a New User Role**.

4. Enter the role name and description.

5. Under eCheck Permissions, review and add any of these permissions:

   eCheck Status View
   :
   Gives view permission for eCheck status field.

   eCheck Settings View + Template View + Merchant Boarding View
   :
   Gives view permission for these fields:
   * eCheck Descriptor
   * Apply hold on all funding
   * Allow credits
   * Allowed eCheck transaction types
   * Number of days before funding
   * Settlement Account Balance
   * Estimated Total Monthly Sales
   * Average Order Amount
   * Actual Transaction Volume (current month, as of today)
   * Largest Expected Order Amount
   * Name on Bank Account
   * Account Type
   * Routing Number
   * Account Number (last four digits)
   * Reserve Account Balance (fixed $ amount)
   * Reserve Method
   * Reserve Rate (% of TPV)
   * Reserve Holding Days (number of days)
   * Reserve Target (fixed $ amount)

   eCheck Business Address Information View + Merchant Boarding View
   :
   Gives view permission for these fields:
   * Country
   * Street Address 1
   * Street Address 2 (Optional)
   * City
   * State
   * ZIP Code

   eCheck Business Address Information Management + Merchant Boarding Manage
   :
   :
   Gives view and edit permissions for these fields:
   * Country
   * Street Address 1
   * Street Address 2 (Optional)
   * City
   * State
   * ZIP Code

   eCheck Business Process Information View + SPS Application View
   :
   Gives view permission for these fields:
   * When is the Customer Charged?
   * Describe when the Customer is Charged (conditional display)
   * Do you Offer Subscriptions
   * Subscription monthly percentage
   * Subscription quarterly percentage
   * Subscription semiannual percentage
   * Subscription annual percentage
   * Timeframe to Product Delivery

   eCheck Business Identifying Details View + Merchant Boarding View
   :
   Gives view permission for these fields:
   * Legal Business Name
   * Doing Business As
   * Business Type
   * Business Start Date
   * Website URL
   * Merchant Category Code (MCC)
   * Business Description
   * Phone

   eCheck Business Identifying Details Management + Merchant Boarding Manage
   :
   Gives view and edit permissions for these fields:
   * Doing Business As
   * Business Description
   * Phone

   eCheck Owner Information View + SPS Application View
   :
   Gives View permission for these fields:
   * First Name
   * Last Name
   * Email Address
   * Mobile
   * Country
   * Street Address 1
   * Street Address 2 (Optional)
   * City
   * State
   * ZIP Code
   * Job Title

   eCheck Statements View
   :
   Gives view permission for the settlement and reserve account statements.

Creating a User Account and Adding Roles {#echeck-bc-permissions-useracct.dita}
===============================================================================

Follow these steps to create a new user account and add roles:

1. Log in to the `Business Center`:
   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-bc-permissions-useracct.dita_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-bc-permissions-useracct.dita_d7e38}
2. In the left navigation panel, under Account Management, choose **Users**.
3. Click **Add User**.
4. Add the user details.
5. Select a role from the ones listed in [Creating Roles](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-bc-settings-intro/echeck-bc-permissions/echeck-bc-permissions-roles.md "").

Accessing eCheck Settings in the `Business Center` {#echeck-bc-settings}
========================================================================

1. Follow these steps to view and manage the eCheck settings, business information, and owner information for your MID:

2. Log in to the `Business Center`:

   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-bc-settings_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-bc-settings_d7e38}
3. In the left navigation panel, under Payment Configuration, select the eCheck module.

4. Using the appropriate tabs, manage the eCheck settings, business information, and owner information for your MID based on the role assigned to your user account.

   #### Figure:

   Merchant eCheck Business Information  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-merchant-UI.png/jcr:content/renditions/original) To learn how to create a role and assign permissions, see [Managing Merchant Permissions in the Business Center](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-bc-settings-intro/echeck-bc-permissions.md "").

5. If you want to view and edit eCheck-related information in these categories, you must perform step-up authentication:

   * Personally identifiable information about business owners on file for your account.
   * Primary account number (PAN) used for funding all your eCheck transactions.

You can choose to receive the one-time password (OTP) in an SMS message or an email message.

eCheck Statements {#echeck-statements}
======================================

To access these statements for your merchant account, go to the `Business Center` eCheck module and click the **Statements** tab.

* eCheck settlement account statement
* eCheck reserve account statement

You can use the data in these statements to help reconcile funds movement for all your transactions. Each statement line item has a unique ID assigned, and you can use these IDs in communications with `Cybersource` teams.

eCheck Settlement Account Statements {#echeck-statements-settlement-acct}
=========================================================================

These statements provide a view of the amounts going in and out of your eCheck settlement account. An eCheck settlement account statement can include automated activities as well as manual funding activities, if any. You can filter and sort the lines displayed in the statement.  
A settlement account statement can include these types of activities:

* Automated funding to your bank account.
* Debit transactions getting funded into the settlement account.
* Returned transactions.
* Manual transfers into and out of the account, including manual funding and deficit recovery.

eCheck Reserve Account Statements {#echeck-statements-reserve-acct}
===================================================================

Like settlement account statements, reserve account statements appear in the Statements tab of the eCheck module, and you can filter and sort the lines displayed. The statements provide a view of the amounts going in and out of your reserve account, if you have one. It includes both automated activities and manual funding activities, if any. You can filter the statements using the data range and sort them as per your needs.  
A reserve account statement can include these types of activities:

* Automated deposit as a percentage of the transaction settlement.
* Manual transfers in and out of the reserve account.

Process eCheck Transactions Using the `Business Center` {#echeck-bc-intro}
==========================================================================

You can process eCheck transactions using the `Business Center`, including:

* Debits (using the Virtual Terminal).
* Recurring billing transactions (using an on-demand transaction).
* Recurring subscriptions.

Submitting Transactions Using the Virtual Terminal {#echeck-bc-submit-vt}
=========================================================================

You can process a debit in the `Business Center` by using the Virtual Terminal.

Configuring the Virtual Terminal to Process eCheck Transactions {#echeck-quick-start-vt-settings}
=================================================================================================

Follow these steps to enable the eCheck service on the Virtual Terminal.

1. Log in to the `Business Center`:
   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-quick-start-vt-settings_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-quick-start-vt-settings_d7e38}
2. Navigate to Virtual Terminal \&gt; Terminal Settings. The Terminal Settings Page appears.
3. Click the Global Payment Settings tab.
4. In the Card Status drop-down menu, select Not Present.
5. Choose Checks \&gt; Check Payment Options \&gt; Enable Check Payments, and check the Display box.
6. Optional: Check the Display box to display the Electronic Check Reference Number.
7. Optional: In the SEC Value drop-down menu, select an SEC code. If you do not select one, a default will be selected.  
   If the e-commerce indicator (ECI) for the Virtual Terminal is `MOTO`, the value of the SEC code defaults to `TEL`. If the ECI for the Virtual Terminal is not set to `MOTO`, the value of the SEC code defaults to `WEB`.
8. Click Submit, then click Confirm.

Processing eCheck Transactions Using the Virtual Terminal {#echeck-vt}
======================================================================

Follow these steps to process an eCheck debit transaction using the Virtual Terminal:

1. Log in to the `Business Center`:
   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-vt_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-vt_d7e38}
2. On the left navigation panel, click Virtual Terminal icon.
3. Click One-Time Payment. The One-Time Payment page appears.
4. Under Customer Presence, click Not Present.
5. In Transaction Type, under Order Details, select Echeck Debit, enter the amount, and enter any Level II values that you collect.
6. Under Merchant Defined Fields, enter merchant-defined values that you collect, if appropriate.
7. Under Level III Fields, enter Level III values that you collect, if appropriate.
8. Under Billing Information, enter information for billing the customer. Check the box if the shipping information is the same, or enter shipping information.
9. Under Payment Information, enter the eCheck account information.
10. If you want to create a token for this customer:
    1. In the Payment Information section of the page, select the Use payment details to create more transactions option.
    2. In the Subscription Information section of the page, choose the appropriate option in the Subscription Type drop-down menu.
11. Click the link to read the terms and conditions, and check the box to confirm that you have read and agree to the terms and conditions.
12. When you are finished, click Submit.

Submitting Transactions Using Recurring Billing and Token Management Service {#echeck-quick-start-rb-tms}
=========================================================================================================

To use eCheck with recurring billing or the `Token Management Service` (`TMS`), the SEC code must be set to `TEL` for personal accounts and `CCD` for corporate accounts.  
When you include a subscription ID in a payment request, any field associated with that subscription becomes optional. For example, address fields are optional if they are the same as the address fields in the subscription.  
When creating a profile or subscription for the eCheck service, include this information:

* Account number
* Account type
* Bank transit number
* Check number
* SEC code
  {#echeck-quick-start-rb-tms_ul_ebq_kqz_5wb}

Related Information
-------------------

* [Recurring Billing for the Business Center](https://docs.cybersource.com/content/dam/new-documentation/documentation/en/rb/user/all/ebc/recurring-billing-ebc.pdf "")
* [Token Management Using the REST API](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "")
* [Token Management Using the Business Center](https://ebc2.cybersource.com/content/ebc/help/cybs/en-us/tokens.md "")

Creating an eCheck Recurring Subscription {#echeck-recurring-subs}
==================================================================

1. Follow these steps to create an eCheck recurring subscription:

2. Log in to the `Business Center`:

   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-recurring-subs_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-recurring-subs_d7e38}
3. In the left navigation panel, choose Recurring Billing. The Recurring Billing page appears.

4. Click New Subscription. The Add Subscription panel appears.

5. Enter the eCheck recurring subscription required information:

   **Order Information**
   :
   Order/merchant reference number. You can include two types of data storage fields in a customer subscription.

   **Payment Information**
   :
   * Payment type: choose **Check**.
   * Alternate Merchant Descriptor. Alternate contact information for your business, such as email address or URL.
   * SEC Code: choose the authorization.
   * Account number
   * Check number
   * Account type
   * Check routing number, also known as the *transit number*.
   * Driver's license number
   * State/province
   * Date of birth
   {#echeck-recurring-subs_ul_jvb_vdj_vcc}

   **Customer Information**
   :
   * Customer ID
   * First and last name
   * Street address 1
   * City, state, ZIP/postal code
   * Country
   * Phone number
   * Email address
   {#echeck-recurring-subs_ul_wnr_12j_vcc}

   **Shipping Information**
   :
   * First and last name
   * Company
   * Street address 1
   * Street address 2
   * City, state, ZIP/postal code
   * Country
   {#echeck-recurring-subs_ul_eq5_d2j_vcc}

   **Subscription Information**
   :
   Subscription type: choose **Recurring**.

   **Recurring Transaction Information**
   :
   * Title
   * Recurring amount
   * Currency
   * Setup fee
   * Start date
   * Billing frequency
   * Number of payments
   {#echeck-recurring-subs_ul_mkm_32j_vcc}

6. Check Require approval before processing payments to have each payment approved before `Cybersource` processes it.  
   If you change the amount of the subscription, the status of all future payments is reset to unapproved even if the payments were already approved.

7. Click Submit. The success message appears along with the subscription ID for the customer subscription.

8. Click the subscription ID. The Subscription Details page appears.

Requesting an On-Demand Transaction {#echeck-req-od-txn}
========================================================

1. Follow these steps to request an on-demand transaction:
2. Log in to the `Business Center`:
   * **Test:**  
     ` `<https://businesscentertest.cybersource.com/ebc2>` `{#echeck-req-od-txn_d7e29}
   * **Production:**  
     ` `<https://businesscenter.cybersource.com>` `{#echeck-req-od-txn_d7e38}
3. In the left navigation panel, choose Recurring Billing. The Recurring Billing page appears.
4. Choose the scope for the search:
   * Organization

   * Type

     * Subscriptions
     * Subscription payments
   * Scope of subscriptions

     * All
     * Active
     * On-hold
     * Cancelled---choose a date range.
     * Creation date---choose a date range.
     * Expiration date---choose a date range.
     * Payment card expiration date---choose a date range.
     * Field and value---choose a specific field such as the subscription ID.

     The subscriptions list appears.

5. Click the title of the customer subscription that you want to modify. The Subscription Details page appears.
6. Click Make On-Demand Payment. The On-Demand Payment page appears. The on-demand transaction types:
   * Credit Card---authorization, sale.
   * Electronic checks---debit, credit.
7. Enter the amount for the transaction.
8. Choose the transaction type.
9. Click Submit. The Subscription Details page appears. You can request these transaction result message appears along with the request ID for the transaction.

eCheck Transaction Search and Details {#echeck-search-details}
==============================================================

You can search for transactions using search filters in the `Business Center` or by using the REST API.  
On the `Business Center`'s Transactions page, use the Application search filter to find one of these options from the Application drop-down menu:

* Electronic Check Credit
* Electronic Check Debit

{#echeck-search-details_ul_a2f_jqz_5wb}  
These eCheck API fields are supported for transaction search and details:

* paymentInformation.bank.account.suffix
* paymentInformation.bank.account.checkNumber

{#echeck-search-details_ul_b2f_jqz_5wb}

Related Information
-------------------

* [*Transaction Search Using the REST API*](https://developer.cybersource.com/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-search-intro.md "")
* [*Transaction Details Using the REST API*](https://developer.cybersource.com/docs/cybs/en-us/txn-search/developer/all/rest/txn-search/txn-details-intro.md "")

Process eCheck Transactions Using the REST API {#echeck-api-intro}
==================================================================

You can process a debit or recurring eCheck transaction using the API.

Processing an eCheck Debit Transaction Using the REST API {#echeck-api-debit-intro}
===================================================================================

This section shows you how to process an eCheck debit transaction using the REST API.

Processing an eCheck Debit Transaction
--------------------------------------

Follow these steps to process an eCheck debit transaction:

1. Create the message with the required API fields.
2. Send the message to one of these endpoints:
   * Production: `POST ``https://api.cybersource.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.cybersource.com``/pts/v2/payments`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields for an eCheck Debit Transaction {#echeck-api-req-fields}
========================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:
Value must be set to `USD`.

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required if you do not submit orderInformation.lineItems\[\].unitPrice and orderInformation.lineItems\[\].quantity.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
Set the value to a valid USPS two-letter state or possession abbreviation.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
Set the value to `US`.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.bank.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-num.md "")
:

[paymentInformation.bank.account.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-type.md "")
:

[paymentInformation.bank.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-routing-number.md "")
:

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `check`.

Optional Fields for an eCheck Debit Transaction {#echeck-api-optional-fields}
=============================================================================

[processingInformation. bankTransferOptions. secCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-bank-transfer-options-sec-code.md "")
:
Supported values:

    * `ccd`
    * `ppd`
    * `tel`
    * `web`

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Supported values:

    * `internet` (default)
    * `moto`
    * `recurring`

REST Example: eCheck Debit Transaction {#echeck-api-debit-example}
==================================================================

Request

```
{
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "Jane",
            "lastName": "Doe",
            "phoneNumber": "2053040804",
            "address1": "112 12 Ave",
            "postalCode": "98004",
            "locality": "Bellevue",
            "administrativeArea": "WA",
            "email": "test@example.com"
        },
       "amountDetails": {
            "currency": "USD",
            "totalAmount": 1200
        }
    },
    "clientReferenceInformation": {
        "code": "TC123"
    },
    "paymentInformation": {
        "bank": {
            "routingNumber": "071923284",
            "account": {
                "number": "12345678901234567",
                "type": "C"
            }
        },
        "paymentType": {
            "name": "check"
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "16681201582270123456789",
    "reconciliationId": "9PK9Y6A8A75018I",
    "submitTimeUtc": "2022-11-10T22:42:38Z",
    "status": "PENDING",
    "clientReferenceInformation": {
        "code": "TC123"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "1200"
        }
    }
}
```

Processing a Recurring eCheck Debit Transaction Using the REST API {#echeck-api-recurring-intro}
================================================================================================

This section shows how to process a recurring eCheck debit transaction using the REST API.

Processing a Recurring eCheck Debit Transaction
-----------------------------------------------

Follow these steps to process a recurring eCheck debit transaction:

1. Create the message with the required API fields.
2. Send the message to one of these endpoints:
   * Production: `POST ``https://api.cybersource.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.cybersource.com``/pts/v2/payments`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields for a Recurring eCheck Debit Transaction {#echeck-api-recurring-req-fields}
===========================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:
Value must be set to `USD`.

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required if you do not submit orderInformation.lineItems\[\].unitPrice and orderInformation.lineItems\[\].quantity.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
Set the value to a valid USPS two-letter state or possession abbreviation.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
Set the value to `US`.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.bank.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-num.md "")
:

[paymentInformation.bank.account.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-type.md "")
:

[paymentInformation.bank.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-routing-number.md "")
:

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `check`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `recurring`.

[processingInformation.recurringOptions.firstRecurringPayment](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-recurring-ops-first-recurring-payment.md "")
:
If this is the first payment in the recurring series of payments, set the value to `true`. For each subsequent payment in the series, set the value to `false`.

REST Example: Recurring eCheck Debit Transaction {#echeck-api-recurring-example}
================================================================================

Request

```
{
    "processingInformation": {
        "commerceIndicator": "recurring",
        "recurringOptions": {
            "firstRecurringPayment": true
        },
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "Jane",
            "lastName": "Doe",
            "phoneNumber": "2053040804",
            "address1": "112 12 Ave",
            "postalCode": "98004",
            "locality": "Bellevue",
            "administrativeArea": "WA",
            "email": "test@example.com"
        },
       "amountDetails": {
            "currency": "USD",
            "totalAmount": 1200
        }
    },
    "clientReferenceInformation": {
        "code": "TC123"
    },
    "paymentInformation": {
        "bank": {
            "routingNumber": "071923284",
            "account": {
                "number": "12345678901234567",
                "type": "C"
            }
        },
        "paymentType": {
            "name": "check"
        }
    }
}
```

Response to a Successful Request

```
{
    "id": "16681201582270123456789",
    "reconciliationId": "9PK9Y6A8A75018I",
    "submitTimeUtc": "2022-11-10T22:42:38Z",
    "status": "PENDING",
    "clientReferenceInformation": {
        "code": "TC123"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "1200"
        }
    }
}
```

Creating an eCheck Token Using the REST API {#echeck-api-cre-token-standalone}
==============================================================================

This section shows how to create an eCheck token for your customer using the REST API.

> IMPORTANT No transaction is run in this use case. The token is created for future use with this customer.

Creating a Customer Token With No Payment Details
-------------------------------------------------

Follow these steps to create an eCheck token for your customer using your customer's bank account details:

1. Create the message with the required API fields.
2. Send the message to one of these endpoints:
   * Production: `POST ``https://api.cybersource.com``/tms/v2/customers`
   * Test: `POST ``https://apitest.cybersource.com``/tms/v2/customers`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields for Creating an eCheck Token {#echeck-api-cre-token-standalone-req-fields}
==========================================================================================

[paymentInstrument.bankAccount.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/payment-instrmnt-bank-accnt-type.md "")
:

[paymentInstrument.instrumentIdentifier.bankAccount.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/payment-instrmnt-instrmnt-id-bank-accnt-num.md "")
:

[paymentInstrument.instrumentIdentifier.bankAccount.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/payment-instrmnt-instrmnt-id-bank-accnt-rout-num.md "")
:

REST Example: Creating an eCheck Token {#echeck-api-cre-token-standalone-example}
=================================================================================

Request

```
{
    "paymentInstrument": {
        "bankAccount": {
            "type": "savings"
        },
        "instrumentIdentifier": {
            "bankAccount": {
                "number": "12345678901234567",
                "routingNumber": "071923284"
            }
        }
    }
}
```

Response

```
{
     "_links": {
        "self": {
            "href": "/tms/v2/customers/2281788029E0D2B4E0633F36CF0AB40D"
        },
        "paymentInstruments": {
            "href": "/tms/v2/customers/2281788029E0D2B4E0633F36CF0AB40D/payment-instruments"
        },
        "shippingAddresses": {
            "href": "/tms/v2/customers/2281788029E0D2B4E0633F36CF0AB40D/shipping-addresses"
        }
    },
    "id": "2281788029E0D2B4E0633F36CF0AB40D",
    "objectInformation": {
        "title": "subscription_title",
        "comment": "comments"
    },
    "buyerInformation": {
        "merchantCustomerID": "customer_account_id"
    },
    "clientReferenceInformation": {
        "code": "merchant_ref_number"
    },
    "merchantDefinedInformation": [
        {
            "name": "data1",
            "value": "merchant_defined_data1"
        },
        {
            "name": "data2",
            "value": "merchant_defined_data2"
        },
        {
            "name": "data3",
            "value": "merchant_defined_data3"
        },
        {
            "name": "data4",
            "value": "merchant_defined_data4"
        },
        {
            "name": "sensitive1",
            "value": "merchant_secure_data1"
        },
        {
            "name": "sensitive2",
            "value": "merchant_secure_data2"
        },
        {
            "name": "sensitive3",
            "value": "merchant_secure_data3"
        },
        {
            "name": "sensitive4",
            "value": "merchant_secure_data4"
        }
    ],
    "metadata": {
        "creator": "npr_fnbo"
    }
}
```

Creating an eCheck Token and Processing an eCheck Transaction Using the REST API {#echeck-api-cre-token-with-txn}
=================================================================================================================

This section shows how to create an eCheck transaction along with an eCheck transaction using the REST API.

> IMPORTANT The token can also be used for future eCheck transactions for this customer.

Creating an eCheck Token and Processing an eCheck Transaction
-------------------------------------------------------------

Follow these steps to create an eCheck token for your customer and process an eCheck transaction at the same time:

1. Create the message with the required API fields.
2. Send the message to one of these endpoints:
   * Production: `POST ``https://api.cybersource.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.cybersource.com``/pts/v2/payments`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields for Creating an eCheck Token and Processing an eCheck Transaction {#echeck-api-cre-token-with-txn-req-fields}
=============================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Order reference or tracking number.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:
Set the value to `USD`.

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. `Cybersource` truncates the amount to the correct number of decimal places.
:
This field is required if line items *are not present* in the downstream service.
:
> IMPORTANT
> If line items *are present* in the downstream service, this value (if present) takes precedence over the sum of the line items.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
Set the value to a valid USPS two-letter state or possession abbreviation.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
Set the value to `US`.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.bank.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-num.md "")
:

[paymentInformation.bank.account.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-type.md "")
:

[paymentInformation.bank.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-routing-number.md "")
:

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `check`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set the value to `TOKEN_CREATE`.

[processingInformation.actionTokenTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-token-types.md "")
:
Indicates the type of `Token Management Service` (`TMS`) token to be created in the request. Possible values for this use case:

    * `customer`
    * `instrumentIdentifier`
    * `paymentInstrument`

Optional Fields for Creating an eCheck Token and Processing an eCheck Transaction {#echeck-api-cre-token-with-txn-opt-fields}
=============================================================================================================================

[clientReferenceInformation.applicationName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-name.md "")
:

[clientReferenceInformation.applicationUser](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-user.md "")
:

[clientReferenceInformation.applicationVersion](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-version.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.company.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-name.md "")
:

[processingInformation.bankTransferOptions.secCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-bank-transfer-options-sec-code.md "")
:
Specifies the authorization method for the transaction. Possible values for this use case:

    * `CCD`: Corporate cash disbursement.
    * `PPD`: Prearranged payment and deposit entry.
    * `TEL`: Telephone-initiated entry.
    * `WEB`: Internet-initiated entry.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Type of transaction. Possible values for this use case:

    * `internet` (default): Order placed from a website.
    * `moto`: Mail order or telephone order.
    * `recurring`: Recurring payment that is a US transaction or non-US mail order or telephone order (MOTO) transaction. For merchant-initiated transactions on `Visa Platform Connect` with Mastercard in India or with an India-issued card, the recurring value is used for the recurring payment scenario.

REST Example: Creating an eCheck Token and Processing an eCheck Transaction {#echeck-api-cre-token-with-txn-example}
====================================================================================================================

Request

```
{
    "paymentInformation": {
        "paymentType": {
            "name": "check"
        },
        "bank": {
            "routingNumber": "071923284",
            "account": {
                "number": "12345678901234567",
                "type": "C"
            }
        }
    },
    "clientReferenceInformation": {
        "code": "TC1-060"
    },
    "processingInformation": {
        "actionList": [
            "TOKEN_CREATE"
        ],
        "actionTokenTypes": [
            "customer"
        ]
    },
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "2053040804",
            "address1": "12th Ave",
            "postalCode": "98105",
            "locality": "Seattle",
            "administrativeArea": "WA",
            "email": "test@example.com"
        },
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.20"
        }
    }
}
```

Response

```
{
    "id": "7271075033691234567890",
    "reconciliationId": "0TT46FR91BDT7Y6",
    "submitTimeUtc": "2024-09-23T16:05:04Z",
    "status": "PENDING",
    "clientReferenceInformation": {
        "code": "TC1-060"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": “10.20"
        }
    },
    "paymentInformation": {},
    "tokenInformation": {
        "instrumentIdentifierNew": “false”,
        "customer": {
            "id": "22CC4C8BCC82EE54E0634136CF0A86E8"
        },
        "instrumentIdentifier": {
            "id": "E8C05D69D9C53AB1E0534136CF0AF328",
            "state": "ACTIVE"
        },
        "paymentInstrument": {
            "id": "22CC4C8BCC8AEE54E0634136CF0A86E8"
        }
    }
}
```

Using an eCheck Token to Submit an eCheck Debit Transaction Using the REST API {#echeck-api-use-token-submit-debit-txn}
=======================================================================================================================

This section shows how to use an eCheck token to submit an eCheck debit transaction using the REST API.

Using an eCheck Token to Submit an eCheck Transaction
-----------------------------------------------------

Follow these steps to use an eCheck token to submit an eCheck debit transaction:

1. Create the message with the required API fields.
2. Send the message to one of these endpoints:
   * Production: `POST ``https://api.cybersource.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.cybersource.com``/pts/v2/payments`
3. Verify the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success. See [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

Required Fields for Using an eCheck Token to Submit an eCheck Debit Transaction {#echeck-api-use-token-submit-debit-txn-req-fields}
===================================================================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:
Set the value to `USD`.

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
Set the value to a valid USPS two-letter state or possession abbreviation.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
Set the value to `US`.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.customer.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `check`.

Optional Fields for Using an eCheck Token to Submit an eCheck Debit Transaction {#echeck-api-use-token-submit-debit-txn-opt-fields}
===================================================================================================================================

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.company.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-name.md "")
:

[paymentInformation.bank.account.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-num.md "")
:

[paymentInformation.bank.account.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-account-type.md "")
:

[paymentInformation.bank.routingNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-bank-routing-number.md "")
:

[processingInformation.bankTransferOptions.secCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-bank-transfer-options-sec-code.md "")
:
Set the value to `WEB`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `internet`.

REST Example: Using an eCheck Token to Submit an eCheck Debit Transaction {#echeck-api-use-token-submit-debit-txn-example}
==========================================================================================================================

Request

```
{
    "paymentInformation": {
        "paymentType": {
            "name": "check"
        },
        "customer": {
            "id": "22CC4C8BCC82EE54E0634136CF0A86E8"
        }
    },
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "2053040804",
            "address1": "12th Ave",
            "postalCode": "98105",
            "locality": "Seattle",
            "administrativeArea": "WA",
            "email": "test@example.com"
        },
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.20"
        }
    }
}
```

Response

```
{
    "id": "7271080098361234567890",
    "reconciliationId": "0TT46FR91BDT7Y9",
    "submitTimeUtc": "2024-09-23T16:13:30Z",
    "status": "PENDING",
    "clientReferenceInformation": {
        "code": "TC1-060"
    },
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.20"
        }
    }
}
```

Accepting eCheck Payments through Unified Checkout, Pay by Link, and Invoicing {#echeck-pay-unified-checkout-invoice-paybylink-intro}
=====================================================================================================================================

There are several ways to accept digital payments with eCheck. Each payment option provides a way to integrate the eCheck payment option into your checkout through a Pay with bank account link, that enables the customer to provide bank account and contact information.

Accepting eCheck Payments through `Unified Checkout` {#echeck_pay_unified_checkout}
===================================================================================

`Unified Checkout` provides a single interface to securely accept digital payments on your website. The supported digital payment methods include eCheck.  
After you integrate `Unified Checkout` with your website, the eCheck payment option appears for your customers on the checkout page as Pay with bank account. After they click Pay with bank account, your customer is then prompted to provide their bank account details, billing address, and contact information before they submit the payment.  
For information on integrating with `Unified Checkout`, see the [*`Unified Checkout` Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").  
These screen captures show the sequence of events that your customer can expect when completing a payment with a bank account.
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-echeck-1.png/jcr:content/renditions/original) ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-echeck-2.png/jcr:content/renditions/original)  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-echeck-7.png/jcr:content/renditions/original)

Accepting eCheck Payments through Invoices {#echeck-bc-invoicing}
=================================================================

Businesses can bill any customer with an email address and accept digital payments securely from any connected device. If the eCheck payment is enabled for your account, it appears as *Pay with Bank Account* on the checkout page after the merchant clicks the invoice link.  
You can create and manage payment links in your invoices through the `Business Center` or directly integrate Invoice APIs into your own system to automate the creation and management of invoices. For more information on integrating invoicing into your workflow, see the [*Invoicing Developer Guide*](https://developer.cybersource.com/api-reference-assets/index.md#invoicing "").  
Your customers will follow this workflow to use the payment link on the invoice.

1. eCheck appears as a Pay with Bank Account option on the checkout page.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-invoicing-link.png/jcr:content/renditions/original)
2. When the customer clicks the link, a sidebar appears. In the sidebar, the customer enters information about their bank account and billing address and clicks Continue.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-invoicing-bank.png/jcr:content/renditions/original)
3. In the Contact section, the customer enters their email address and phone number and clicks Continue.
4. In the Confirm section, the customer reviews the information they provided. If necesssary, the customer can click Edit to make changes to any of the information. If the information is correct, the customer clicks Pay to make the payment.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-invoicing-contact.png/jcr:content/renditions/original)

Accepting eCheck Payments through Payment Links {#echeck-bc-pay-by-link}
========================================================================

Pay by Link provides payment links for selling products or receiving donations online. The links can be set at a fixed price or be configured so that the customer specifies the payment value. These links can be distributed to multiple customers.  
If the eCheck payment method is enabled for your account, it appears as *Pay with Bank Account*on the checkout page after the merchant clicks the payment link.  
You can create and manage payment links through the `Business Center` or directly integrate Pay by Link APIs into your own system to automate the creation and management of payment links. For more information on integrating with Pay by Link, see the [*Pay by Link Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/paybylink/developer/all/rest/paybylink/paybylink-about-guide.md "").  
Your customers will follow this workflow to use the payment link.

1. eCheck appears as a Pay with Bank Account option on the checkout page.

   #### Figure:

   Payment Link on the Webpage ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-pay-by-link-link.png/jcr:content/renditions/original)

2. When the customer clicks Pay with Bank Account, a sidebar appears. In the sidebar, the customer enters information about their bank account and billing address and clicks Continue.

   #### Figure:

   Bank Account Information and Billing Information ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-pay-by-link-contact.png/jcr:content/renditions/original)

3. In the Contact section, the customer enters their email address and phone number and clicks Continue.

4. In the Confirm section, the customer reviews the information they provided. If necesssary, the customer can click Edit to make changes to any of the information. If the information is correct, the customer clicks Pay to make the payment.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/echeck-pay-by-link-confirm.png/jcr:content/renditions/original)

eCheck Reconciliation Reports {#echeck-reports-recon}
=====================================================

Reconciliation reports provide additional information about your transactions. See these sections for further information:

* [Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding.md "")
* [Chargeback Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-chargeback.md "")
* [Deposit Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-deposit.md "")  
  For a case study in using reconciliation reports with eCheck, see [eCheck Reconciliation Reporting Case Study](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-use-case.md "").

Related Information
-------------------

* [Reporting User Guide](https://developer.cybersource.com/library/documentation/dev_guides/reporting_and_reconciliation/Reporting_User.pdf "")
* [Generating Reports Using the `Business Center`](https://ebc2.cybersource.com/content/ebc/help/cybs/en-us/reports_intro.md "")
* [Generating Reports Using the REST API](https://developer.cybersource.com/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_api.md "")

Funding Details Report {#echeck-reports-recon-funding}
======================================================

The eCheck Funding Details Report is a transaction-level report that shows the date on which a particular transaction was included in the funding calculation.

Related Information
-------------------

* [Chargeback Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-chargeback.md "")
* [Fields in the Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding/echeck-reports-recon-funding-fields.md "")

Fields in the Funding Details Report {#echeck-reports-recon-funding-fields}
===========================================================================

This topic lists the fields that appear in the eCheck Funding Details Report. The fields are organized into these groups: Application, BillTo, Check, Funding, PaymentData, PaymentMethod, and Request.

Application Field
-----------------

Name
:
Name of an application applied to this request.
:
Field name in the report: ApplicationName

BillTo Fields
-------------

Address1
:
First line of billing street address as it appears on credit card issuer's records.
:
Field name in the report: BillTo_Address1

Address2
:
Additional address information.
:
Field name in the report: BillTo_Address2

City
:
Billing address city.
:
Field name in the report: BillTo_City

CompanyName
:
Name of customer's company.
:
Field name in the report: BillTo_CompanyName

Country
:
Billing address country.
:
Field name in the report: BillTo_Country

Email
:
Customer's complete email address.
:
Field name in the report: BillTo_Emai

FirstName
:
Billing customer's first name.
:
Field name in the report: BillTo_FirstName

LastName
:
Billing customer's last name.
:
Field name in the report: BillTo_LastName

Phone
:
Billing customer phone number.
:
Field name in the report: BillTo_Phone

State
:
Billing address state
:
Field name in the report: BillTo_State

Zip
:
Billing address ZIP/postal code.
:
Field name in the report: Bill_To_Zip

Check Field
-----------

BankTransitNumber
:
Bank transit number.
:
Field name in the report: BankTransitNumber

Funding Fields
--------------

AdjustmentAmount
:
Amount of the adjustment made to the transaction amount.
:
Field name in the report: AdjustmentAmount

AdjustmentCurrency
:
Currency of the adjusted transaction.
:
Field name in the report: AdjustmentCurrency

AdjustmentDescription
:
Description of the adjustment.
:
Field name in the report: AdjustmentDescription

FundingAmount
:
Funding amount.
:
Field name in the report: FundingAmount

FundingCurrency
:
Funding currency.
:
Field name in the report: FundingCurrency

FundingDate
:
Funding date.
:
Field name in the report: FundingDate

Status
:
Status.
:
Field name in the report: Funding_Status

PaymentData Fields
------------------

Amount
:
Order grand total.
:
Field name in the report: Amount

CurrencyCode
:
Payment currency code.
:
Field name in the report: CurrencyCode

PaymentProcessor
:
Payment processor name.
:
Field name in the report: PaymentProcessor

TransactionRefNumber
:
Transaction reference number.
:
Field name in the report: TransactionReferenceNumber

PaymentMethod Fields
--------------------

AccountSuffix
:
Last four digits of customer's payment account number.
:
Field name in the report: AccountSuffix

AccountType
:
Account type. Possible values:

    * `C`: Checking
    * `S`: Savings
    * `X`: Corporate Checking
    * `Y`: Corporate Savings

:
Field name in the report: AccountType

Request Fields
--------------

MerchantID
:
Merchant ID used for transaction.
:
Field name in the report: MerchantID

MerchantReferenceNmber
:
Merchant's order reference or tracking number.
:
Field name in the report: MerchantReferenceNumber

RequestID
:
Transaction request identifier.
:
Field name in the report: RequestID

TransactionDate
:
Date of transaction.
:
Field name in the report: RequestDate

Chargeback Details Report {#echeck-reports-recon-chargeback}
============================================================

The eCheck Chargeback Details Report is a transaction-level report that shows the date on which a particular return or chargeback transaction from the processor was included in the funding calculation.

Related Information
-------------------

* [Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding.md "")
* [Fields in the Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding/echeck-reports-recon-funding-fields.md "")

Fields in the Chargeback Details Report {#echeck-reports-recon-chargeback-fields}
=================================================================================

This topic lists the fields that appear in the eCheck Chargeback Details Report. The fields are organized into these groups: Application, BillTo, ChargebackAndRetrieval, Check, PaymentData, PaymentMethod, and Request.

Application Fields
------------------

Name
:
Name of an application applied to this request.
:
Field name in the report: ApplicationName

BillTo Fields
-------------

Address1
:
First line of billing street address as it appears on credit card issuer's records.
:
Field name in the report: BillTo_Address1

Address2
:
Additional address information.
:
Field name in the report: BillTo_Address2

City
:
Billing address city.
:
Field name in the report: BillTo_City

CompanyName
:
Name of customer's company.
:
Field name in the report: BillTo_CompanyName

Country
:
Billing address country.
:
Field name in the report: BillTo_Country

Email
:
Customer's complete email address.
:
Field name in the report: BillTo_Email

FirstName
:
Billing customer's first name.
:
Field name in the report: BillTo_FirstName

LastName
:
Billing customer's last name.
:
Field name in the report: BillTo_LastName

Phone
:
Billing customer phone number.
:
Field name in the report: BillTo_Phone

State
:
Billing address state.
:
Field name in the report: BillTo_State

Zip
:
Billing address ZIP/postal code.
:
Field name in the report: BillTo_Zip

ChargebackAndRetrieval Fields
-----------------------------

CaseNumber
:
Processor-assigned case number.
:
Field name in the report: CaseNumber

CaseTime
:
The date that the case was opened.
:
Field name in the report: CaseTime

CaseType
:
Description of the case type.
:
Field name in the report: CaseType

ChargebackAmount
:
Amount of the chargeback.
:
Field name in the report: ChargebackAmount

ChargebackCurrency
:
Chargeback currency code.
:
Field name in the report: ChargebackCurrency

ChargebackReasonCode
:
Association chargeback reason code.
:
Field name in the report: ChargebackReasonCode

ChargebackReasonCodeDescription
:
Text description of the reason code.
:
Field name in the report: ChargebackReasonCodeDescription

ChargebackTime
:
The date that the chargeback was originated by the issuing bank.
:
Field name in the report: ChargebackTime

FinancialImpact
:
Financial impact indicator. Possible values:

    * `Y`: Financial impact
    * `N`: No financial impact

:
Field name in the report: FinancialImpact

TransactionType
:
Capture type of the original transaction.
:
Field name in the report: TransactionType

Check Field
-----------

BankTransitNumber
:
Bank transit number.
:
Field name in the report: BankTransitNumber

PaymentData Field
-----------------

PaymentProcessor
:
Payment processor name.
:
Field name in the report: PaymentProcessor

PaymentMethod Field
-------------------

AccountSuffix
:
Last four digits of customer's payment account number.
:
Field name in the report: AccountSuffix

Request Fields
--------------

MerchantID
:
Merchant ID used for transaction.
:
Field name in the report: MerchantID

MerchantReferenceNumber
:
Merchant's order reference or tracking number.
:
Field name in the report: MerchantReferenceNumber

RequestID
:
Transaction request identifier.
:
Field name in the report: RequestID

TransactionDate
:
Date of transaction.
:
Field name in the report: RequestDate

Deposit Details Report {#echeck-reports-recon-deposit}
======================================================

The eCheck Deposit Details Report is a summary-level report of the funds deposited to your bank account during a particular day. The deposit amount is calculated using this method:

* Total credits and debits (from the Funding Details Report).
* Total credits and debits, minus total returns and chargebacks (from the Chargeback Details Report).
* Total credits and debits, minus risk reserve, withholding, and other one-time adjustments.

Related Information
-------------------

* [Funding Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-funding.md "")
* [Chargeback Details Report](/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-reports-recon/echeck-reports-recon-chargeback.md "")

Deposit Details Report Line Items {#echeck-reports-recon-deposit-line-items}
============================================================================

The Deposit Details Report contains these line items:

Category = Settlement
:
This line item depicts the funds transferred from your eCheck settlement account to your merchant bank account as part of the daily automated funding job.

Category = Manual funding
:
This line item depicts the funds transferred from your eCheck settlement account to your merchant bank account as needed outside of the daily automated funding.

Category = Deficit recovery
:
This line item depicts the funds transferred from your merchant bank account to your eCheck settlement account in order to recover any deficit in the balance caused by returns or chargebacks.

Category = Manual transfer from settlement account to reserve account
:
This line item depicts the funds transferred from your eCheck settlement account to your eCheck reserve account.

Category = Manual transfer from reserve account to settlement account
:
This line item depicts the Funds transferred from your eCheck reserve account to your eCheck settlement account.  
The Deposit Details Report also includes line items for unscheduled activities such as these:

* Funding
* Deficit recovery
* Fund transfers between your eCheck settlement and reserve accounts

Fields in the Deposit Details Report {#echeck-reports-recon-deposit-fields}
===========================================================================

This topic lists fields that appear in the eCheck Deposit Details Report. The fields are organized into these groups: Application, BillTo, Check, Funding, PaymentData, PaymentMethod, and Request.

Application Fields
------------------

Name
:
Name of an application applied to this request.
:
Field name in the report: ApplicationName

BillTo Fields
-------------

Address1
:
First line of billing street address as it appears on credit card issuer's records.
:
Field name in the report: BillTo_Address1

Address2
:
Additional address information.
:
Field name in the report: BillTo_Address2

City
:
Billing address city.
:
Field name in the report: BillTo_City

CompanyName
:
Name of customer's company.
:
Field name in the report: BillTo_CompanyName

Country
:
Billing address country.
:
Field name in the report: BillTo_Country

Email
:
Customer's complete email address.
:
Field name in the report: BillTo_Email

FirstName
:
Billing customer's first name.
:
Field name in the report: BillTo_FirstName

LastName
:
Billing customer's last name.
:
Field name in the report: BillTo_LastName

Phone
:
Billing customer phone number.
:
Field name in the report: BillTo_Phone

State
:
Billing address state.
:
Field name in the report: BillTo_State

Zip
:
Billing address ZIP/postal code.
:
Field name in the report: Bill_To_Zip

Check Field
-----------

BankTransitNumber
:
Bank transit number.
:
Field name in the report: BankTransitNumber

Funding Fields
--------------

AdjustmentAmount
:
Amount of the adjustment made to the transaction amount.
:
Field name in the report:

AdjustmentCurrency
:
Currency of the adjusted transaction
:
Field name in the report: AdjustmentCurrency

AdjustmentDescription
:
Description of the adjustment.
:
Field name in the report: AdjustmentDescription

FundingAmount
:
Funding amount.
:
Field name in the report: FundingAmount

FundingCurrency
:
Funding currency.
:
Field name in the report: FundingCurrency

FundingDate
:
Funding date.
:
Field name in the report: FundingDate

Status
:
Status.
:
Field name in the report: Funding_Status

PaymentData Fields
------------------

Amount
:
Order grand total.
:
Field name in the report: Amount

CurrencyCode
:
Payment currency code.
:
Field name in the report: CurrencyCode

PaymentProcessor
:
Payment processor name.
:
Field name in the report: PaymentProcessor

TransactionRefNumber
:
Transaction reference number.
:
Field name in the report: TransactionReferenceNumber

PaymentMethod Fields
--------------------

AccountSuffix
:
Last four digits of customer's payment account number.
:
Field name in the report: AccountSuffix

AccountType
:
Account type. Possible values:

    * `C`: Checking
    * `S`: Savings
    * `X`: Corporate Checking
    * `Y`: Corporate Savings

:
Field name in the report: AccountType

Request Fields
--------------

MerchantID
:
Merchant ID used for transaction.
:
Field name in the report: MerchantID

MerchantReferenceNmber
:
Merchant's order reference or tracking number.
:
Field name in the report: MerchantReferenceNumber

RequestID
:
Transaction request identifier.
:
Field name in the report: RequestID

TransactionDate
:
Date of transaction.
:
Field name in the report: RequestDate

eCheck Reconciliation Reporting Case Study {#echeck-reports-use-case}
=====================================================================

This case study shows an example of eight business days' worth of eCheck activity and how that activity appears on reconciliation reports.  
These reports are reconciliation reports:

* Funding Details Report

* Deposit Details Report

* Chargeback Details Report  
  The case study is written assuming that these things are true about the merchant account:

* Risk Reserve Target: $1,000.00

* Risk Reserve Rate: 10%

* Funding Hold Period: 3 days

* Monthly Transaction Volume Limit: $40,000.00

Day 1 {#echeck-reports-use-case-day1}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-01.svg/jcr:content/renditions/original)  
On day 1, the merchant processes four debit transactions totaling $9,900. The merchant does not process any credit transactions. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 1 is moved to the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 2 {#echeck-reports-use-case-day2}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-02.svg/jcr:content/renditions/original)  
On day 2, the merchant processes three debit transactions totaling $4,000 and no credit transactions. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 2 is moved to the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 3 {#echeck-reports-use-case-day3}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-03.svg/jcr:content/renditions/original)  
On day 3, the merchant processes one debit transaction totaling $2,000 and one credit transaction totaling $3,000. Because of the 3-day funding hold, no money is moved to the reserve account. All money for day 3 is moved to the settlement account. In this case, because there is $1,000 more credit than debit, $1,000 is removed from the settlement account. No reconciliation reports are generated because nothing is funded yet.

Day 4 {#echeck-reports-use-case-day4}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-04.svg/jcr:content/renditions/original)  
On day 4, the merchant processes three debit transactions totaling $7,000. The merchant does not process any credit transactions. Day 1 is now funded due to the lapse of the 3-day holding period. $990 is moved to the risk reserve account because the risk reserve rate is 10%, and the day 1 total was $9,900. The day 4 total is moved to the settlement account. $5,910 is funded. That amount reflects the settlement account balance, minus the debit totals for days 2, 3, and 4, minus the reserve amount ($990). Because funding occurred, reconciliation reports are generated for day 1 transactions and day 3 credit (there are no holds on credits).

Day 5 {#echeck-reports-use-case-day5}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-05.svg/jcr:content/renditions/original)  
On day 5, the merchant processes two debit transactions totaling $500, and one credit transaction totaling $5,000. $10 is moved to the risk reserve account, bringing the risk reserve account up to its full $1,000. The target funding amount is a negative amount (-$1,010), so nothing is funded on day 5. The settlement amount is -$4,500, so $4,500 is removed from the settlement account. No reconciliation reports are generated because nothing was funded.

Day 6 {#echeck-reports-use-case-day6}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-06.svg/jcr:content/renditions/original)  
On day 6, the merchant processes three debit transactions totaling $8,250 and credit transactions totaling $500. The sum of credit and debit transactions ($7,750) is moved to the settlement account. $490 is funded from days 2 and 3, based on the settlement account balance, minus the debit amounts for days 4, 5, and 6. Reconciliation reports are generated for day 2 and 3 transactions and day 5 and 6 credits.  
On day 6, the $40,000 monthly transaction limit is reached. Consequently, all funding and all credit transactions are put on hold until the following month or until the limit is raised.  
To request that the monthly transaction processing limit is raised, visit the Support Center:  
<http://support.visaacceptance.com>

Day 7 {#echeck-reports-use-case-day7}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-07.svg/jcr:content/renditions/original)  
On day 7, the merchant processes three debit transactions totaling $2,000 and no credit transactions. $2,000 is moved to the settlement account. $5,750 is funded from day 4, based on the settlement account balances, minus days 5 and 6, and day 7 debit amounts. Reconciliation reports are generated for day 4 transactions and day 7 credits.  
On day 7, a Chargeback Details Report is generated because two returns were sent back by payment processors. A debit for $1,500 was returned because of an incorrect account number, and a credit for $250 was returned because the account was closed. The reason codes listed in the chargeback details report are ACH return codes.

Day 8 {#echeck-reports-use-case-day8}
=====================================

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/echeck/user-guide/images/funding-scenario-day-08.svg/jcr:content/renditions/original)  
On day 8, the merchant processes three debit transactions totaling $5,000 and no credit transactions. $5,000 is moved to the settlement account. $500 is funded from day 5 and $5,750 is re-deposited (because there was no account to which to move it), for a total deposit amount of $6,250.
