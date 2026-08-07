Payouts Developer Guide {#payouts-about-guide}
==============================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This document is written for developers who want to use the `Payment Gateway` APIs to integrate `Payment Gateway` `Payouts` services into their transaction management system.

Conventions
-----------

This statement is used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
---------------------

Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") on the Payment Gateway Developer Center for links to further documentation resources.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#payouts-doc-revs}
=====================================================

25.05.01
--------

Updated OCT descriptions and added examples. See:

* [Introduction to OCT](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-intro-oct.md "")
* [Original Credit Transactions (OCTs)](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-standard-intro.md "")
* [Original Credit Transactions (OCTs) with Aggregators](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-agg-intro.md "")
* [Original Credit Transactions (OCTs) with Tokens](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-token-intro.md "").

24.11.01
--------

Added new fields to list of required fields.

24.09.01
--------

Added new fields to the list of required fields.

24.06.01
--------

Reorganized the document.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to `Payouts` {#payouts-intro-intro}
================================================

This introduction contains an overview of the `Payouts` service and describes the supported sender card types, payment networks, requirements, and limitations.

Overview of Payouts {#payouts-intro-overview}
=============================================

The `Payouts` service transfers funds from one account to another using a two-step transaction process:

* An *account funding transaction* (AFT) withdraws funds from a sender's account using standard credit card processing.
* An *original credit transaction* (OCT) deposits funds into a recipient's account.

An AFT and OCT are independent transactions, however, an AFT often precedes a corresponding OCT.  
In typical payment transactions, you initiate debits and credits to receive payments from cardholders for your goods and services. With `Payouts`, you provide a money transfer service by initiating AFT and OCT transactions that move funds between accounts. These are the money transfer types:

* An *account-to-account* payment transfers funds between accounts owned by the same person.
* A *business-to-person* payment transfers funds between a merchant and a cardholder.
* A *person-to-person* payment transfers funds between two cardholders.  
  For a person-to-person funds transfer, Pull and Push services are executed. When an AFT is authorized for a person-to-person transaction, the funds are available and can be withdrawn from the sender's account. This service is known as a *Pull* service. A subsequent OCT is authorized, and the funds are deposited into the recipient's account. This service is known as a *Push* service.  
  The `Payouts` system ensures that both Pull and Push services are executed efficiently, providing a seamless experience for users. By leveraging `Payouts`, businesses and individuals can streamline their financial operations, making transactions more efficient and reliable.  
  No merchant goods are involved in `Payouts` transactions.  
  This guide explains only how to process AFTs.

> IMPORTANT
> You must receive approval from ` Platform Connect ` before using the AFT service. Contact ` Platform Connect ` to register for the AFT program.

AFT Types {#payouts-services-aft-transactions}
==============================================

The Account Funding Transaction (AFT) is a specific type of transaction that moves funds from a Relay account to another Relay or non-Relay account. It is primarily used for loading or topping up prepaid card accounts, transferring funds into another financial account, such as a savings account, acting as a funding source for person-to-person (P2P) money transfers, or loading third-party digital wallets. AFTs cannot be used for purchasing goods or services or transferring funds to a merchant account.  
AFTs are the required transactions to load or top-up prepaid cards in all regions. An AFT is the required pull transaction to be used for disbursing payroll funds, P2P or me-to-me transactions, and pre-funding a customer's digital wallet in a card-not-present environment. When used independently to fund another Relay or non-Relay account, AFTs must be used only to fund an account belonging to the same individual or entity holding the Relay account.

Reversal and Adjustment Transactions
------------------------------------

You can reverse an AFT within the first 24 hours of the original transaction before the transaction settles.  
You can refund an AFT back to the sender's card within 30 days of the original AFT back to the sender's card. You cannot originate a refund if the original transaction is over 30 days old. The system accepts a refund after the original AFT settles. IMPORTANT Issuers can manage AFT refunds as credit adjustments instead of posting the transaction directly into the cardholder's account. Therefore, the time-frame for when the cardholder should expect the refund will vary by issuer.

Aggregator Support for `Payouts` {#agg-intro-overview}
======================================================

A third-party agents can act as an *aggregator* , or *payment facilitator* , for supported types of `Payouts` transactions. An aggregator is an organization that aggregates `Payouts` transactions for a group of sub-merchants under a single account, processing card transactions and settling funds directly to sub-merchants' bank accounts. An aggregator can be a merchant, an independent sales organization (ISO), or a member service provider (MSP). When aggregation is enabled, `Payment Gateway` can send payment facilitator information about a transaction that involves the facilitator.  
To have your account configured for this feature, contact customer support.

Supported Card Types {#payouts-intro-processor-cards}
=====================================================

Recipient card type for AFTs:

* Mastercard

* Relay
  {#payouts-intro-processor-cards_ul_f5p_x3r_jdc} These card types are supported :

* Mastercard

* Relay

Payment Networks {#payouts-intro-networks}
==========================================

Relay Direct
:
The Relay Direct payment network provides these functions for `Payouts`:

    * Enhanced message types for OCTs.
    * Processes, policies, and underlying operating regulations and mandates for issuers and acquirers.

Mastercard Send
:
The Mastercard Send payment network transfers funds to Mastercard products. Mastercard Send enables customers to move funds quickly and safely and receive disbursements from businesses and governments.

Requirements {#payouts-intro-requirements}
==========================================

To process Payouts services, you must meet these requirements:
* Obtain approval from your acquirer for requesting this type of transaction.
* Use your merchant category code.
* The amount must be less than or equal to 50,000 USD, unless otherwise noted. Amount limits might differ as required by local laws, local regulations, and limitations imposed by your acquirer. Contact your acquirer for more information.

Introduction to OCT {#payouts-intro-oct}
========================================

The Original Credit Transaction (OCT) is a CardNet transaction that delivers funds directly to a recipient's eligible Relay card. You cannot use OCTs alone to buy goods or services, except in Request to Pay Consumer-to-Small-Business (C2B) cases. OCTs do not allow merchandise return credits or refunds, except by exception or according to Relay rule #0008771.
IMPORTANT You must differentiate between OCT processing and merchandise credit refund processing. If you do not, it could lead to issues such as the reversal of reward points.  
These are Relay Direct services that use OCT:

* Money Transfer
* Funds Disbursement
* Merchant Settlement
* Digital Wallets
* Real-Time Deposit/Check Deposit
* Loyalty and Offers
* Prepaid Load
* Credit Card Bill Payment

{#payouts-intro-oct_ul_hxq_452_1fc}

Money Transfer {#payouts-intro-oct_section_ixq_452_1fc}
-------------------------------------------------------

This service enables customers to send funds to their Relay account or another customer's Relay account.

Funds Disbursement
------------------

This service allows you, government entities, or corporations to send funds to a Relay account. Examples include insurance claims, corporate and manufacturing rebates, affiliate and contractor payouts, expense reimbursements, government disbursements (such as value-added tax refunds), and online gambling and lottery payouts.

> IMPORTANT This service is available based on laws, current Relay policy, and the Relay rules.

Merchant Settlement {#payouts-intro-oct_section_jxq_452_1fc}
------------------------------------------------------------

This services allows acquirers or third-party service providers to speed up settlement payments between acquirers or payment facilitators and you.

Digital Wallets {#payouts-intro-oct_section_kxq_452_1fc}
--------------------------------------------------------

This service enables faster payments through digital or electronic wallet services. You can move funds out of a digital wallet and deliver them to a cardholder's Relay account. This is considered a Money Transfer transaction for risk-control purposes in the Relay processing network. A Staged Digital Wallet (SDW) functions as a brand acceptance mark.

> IMPORTANT Contact your Relay representative for more information and requirements on digital wallets. For more details on digital wallet transactions, visit the Staged Digital Wallet Operators (SDWO) section at Relay Access (Relay Online).

Real-Time Deposit/Check Deposit {#payouts-intro-oct_section_lxq_452_1fc}
------------------------------------------------------------------------

This service converts a check into a digital payment delivered to a cardholder's Relay account.

Loyalty and Offers {#payouts-intro-oct_section_mxq_452_1fc}
-----------------------------------------------------------

This service pays a loyalty reward or merchant offer onto a card using OCT as part of a loyalty program.

Prepaid Load {#payouts-intro-oct_section_nxq_452_1fc}
-----------------------------------------------------

This service enables customers to add value to an eligible Relay reloadable prepaid card.

> IMPORTANT The US market currently supports a separate prepaid load service called Relay ReadyLink. For more information on Relay ReadyLink, contact your Relay representative.

Credit Card Bill Payment {#payouts-intro-oct_section_oxq_452_1fc}
-----------------------------------------------------------------

This service enables consumers to pay a credit card bill.
IMPORTANT When using OCT supported by Relay Direct, you can only use Relay data, like transaction data, reports, and the Relay Direct Account Lookup (ACNL), to operate the Relay program. You cannot use this data for any other purpose.

Relay Card Types and Services for OCT {#payouts-intro-oct-card-types-services-networks}
======================================================================================

Relay card types include reloadable prepaid, deferred debit, debit, credit, and combo cards, each with specific OCT functionalities. OCTs can increase balances or serve as payments, depending on the card type and account setup. These services apply to both domestic and cross-border transactions, supporting money transfers, funds disbursement, prepaid loads, and credit card bill payments.

Relay Card Types
---------------

These are the different Relay card types, descriptions, and examples:

Relay Reloadable Prepaid
:
An OCT to an eligible Relay prepaid card increases the prepaid card balance.
:
If the prepaid card balance is 25 USD and the OCT received is for 100 USD, the new prepaid balance is 125 USD.

Relay Deferred Debit
:
Deferred Debit cards have a line of credit and an underlying bank account. An OCT to a Relay Deferred Debit card deposits funds into the underlying account when both the line of credit and underlying account are with the same bank. If the Deferred Debit card underlying account is with a different bank than the line of credit, post the funds to the card account.
:
If the underlying account has a balance of 800 USD and an OCT for 100 USD is received to the card, the new account balance is 900 USD. The credit balance owed on the card is not impacted by the receipt of the OCT. If the card has a balance owed of 200 USD and an OCT for 100 USD is received, the payment of USD 100 will be posted to the credit account. The new outstanding balance would be USD 100.

Relay Debit
:
An OCT to a Relay debit card increases the balance of the underlying bank account associated with the Relay debit card.
:
If the card balance is 800 USD and the OCT received is for 100 USD, the new account balance is 900 USD.

Relay Credit
:
An OCT to a Relay credit card serves as a payment to the account.
:
If the amount owed on the card is 800 USD and an OCT for 100 USD is received to the card, a payment of USD 100 will be posted to the account. The new outstanding balance is 700 USD.

Relay Combo Card (Brazil)
:
Combo cards allow cardholders to use credit or debit functionality during a transaction. An OCT to a Relay Combo card processed as debit increases the balance of the underlying deposit account linked to the card.
:
The credit balance owed on the card is not impacted by the receipt of the OCT. Funds are applied only to the debit balance in the deposit account. Do not present the OCT for combo cards as credit using the proper values.
:
If the deposit account linked to the card has a balance of 800 USD, and an OCT for 100 USD is received to the account, the new account balance is USD 900.

OCT Services
------------

See the table for an overview of Relay's Original Credit Transaction (OCT) services, key features and benefits:

| OCT Services                                                             | Destination Relay Account Types Relay Credit | Destination Relay Account Types Relay Debit | Destination Relay Account Types Relay Prepaid | Geographic Scope Domestic | Geographic Scope Cross-Border |
|:-------------------------------------------------------------------------|:-------------------------------------------|:------------------------------------------|:--------------------------------------------|:--------------------------|:------------------------------|
| Money Transfer (includes digital wallet and instant deposits)            | X                                          | X                                         | X                                           | X                         | X                             |
| Funds Disbursement (includes merchant settlement and Loyalty and Offers) | X                                          | X                                         | X                                           | X                         | X                             |
| Prepaid Load                                                             |                                            |                                           | X                                           | X                         |                               |
| Credit Card Bill Payment                                                 | X                                          |                                           |                                             | X                         |                               |

AFT Transactions {#payouts-services-intro}
==========================================

The Account Funding Transaction (AFT) allows the transfer of funds between a payment card and another account, including other payment cards. When used independently, an AFT can only transfer funds between accounts owned by the same person or business entity. An AFT is not intended to pay for goods and services, fund a merchant account, or repay debts.

> IMPORTANT
> You must receive approval from ` Platform Connect ` before using the AFT services. Contact ` Platform Connect ` to register in the AFT program.

Dual Message Account Funding Transactions (AFTs) {#payouts-services-auth-dual-message-aft-intro}
================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

Endpoint {#payouts-services-auth-dual-message-aft-intro_d7e16}
--------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-intro_d7e35}

Required Fields for a Dual-Message AFT Request {#payouts-services-auth-dual-message-aft-reqfields}
==================================================================================================

These fields are required to process a dual-message AFT request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-num.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:
{#payouts-services-auth-dual-message-aft-reqfields_dl_wyl_mhh_2cc}

REST Example: Dual-Message AFT {#payouts-services-auth-dual-message-aft-ex-rest}
================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "internet",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@pgw.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "locality": "recipient_city",
        "country": "GBR",
        "nationality": "US",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "senderInformation": {
            "account": {
                "number": "154264765376576126571652675176",
                "fundsSource": "02"
            },
            "firstName": "senderfirstname",
            "lastName": "senderLastname",
            "postalCode": "654321",
            "phoneNumber": "01234567892",
            "address1": "Colorful street 123",
            "locality": "Rotterdam",
            "countryCode": "GBR",
            "identificationNumber": "12345678910111213223",
            "personalIdType": "TXIN",
            "administrativeArea": "KA",
            "type": "B",
            "name": "Thomas Smith",
            "referenceNumber": "15426476537657"
        },
        "merchantInformation": {
            "vatRegistrationNumber": "15426476537657",
            "merchantDescriptor": {
                "name": "utf8_merchant_descriptor",
                "locality": "Mountain View",
                "postalCode": "94044",
                "administrativeArea": "CA"
            }
        },
        "captureOptions": {
            "dateToCapture": "1231"
        }
    }
}
```

Response

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7322307726266013203955/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7322307726266013203955"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7322307726266013203955/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7322307726266013203955",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "100.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "992005",
    "approvalCode": "831000",
    "cardVerification": {
      "resultCodeRaw": "M",
      "resultCode": "M"
    },
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "432623992005",
    "consumerAuthenticationResponse": {
      "code": "2",
      "codeRaw": "2"
    },
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "7322307726266013203955",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2024-11-21T23:12:52Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Relay Secure {#payouts-services-auth-dual-message-aft-vs-intro}
====================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Enables users to safely validate their identity and safely store their personal identity.

Endpoint {#payouts-services-auth-dual-message-aft-vs-intro_d7e16}
-----------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-intro_d7e35}

Required Fields for a Dual-Message AFT with Relay Secure Request {#payouts-services-auth-dual-message-aft-vs-reqfields}
======================================================================================================================

These fields are required to process a dual-message AFT with Relay Secure request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[recipientInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Relay Secure {#payouts-services-auth-dual-message-aft-vs-ex-rest}
====================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "processingInformation": {
    "businessApplicationId": "WT",
    "commerceIndicator": "vbv",
    "authorizationOptions": {
      "initiator": {
        "type": "customer",
        "storedCredentialUsed": "false"
      },
      "aftIndicator": "true",
      "fundingOptions":{
        "initiator": {
          "type":"S"
        }
      }
    }
  },
        "purposeOfPayment": "16"
    },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "type": "001",
      "securityCode": "123"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100",
      "currency": "USD",
      "anticipatedAmount": "123.45",
      "surcharge": {
        "amount": "5"
      }
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@pgw.com",
      "phoneNumber": "4158880000"
    }
  },
  "acquirerInformation": {
    "merchantId": "pa_ctv_sg101"
  },
    "aggregatorInformation.name": "test",
  "recipientInformation": {
    "accountId": "987654321",
    "accountType": "99",
    "address1": "Alpine Eco Road",
    "address2": "Address2 value",
    "firstName": "recFirstname",
    "lastName": "resLastname",
    "middleName": "recMiddletname",
    "locality": "recipient_city",
    "country": "GBR",
    "nationality": "US",
    "postalCode": "571216",
    "streetName": "Alpine eco road",
    "dateOfBirth": "",
    "beneficiaryId": "",
    "beneficiaryName": "",
    "buildingNumber":"Tulip Appartment",
    "beneficiaryAddress": ""
  },
  "senderInformation": {
    "account": {
      "number": "154264765376576126571652675176",
      "fundsSource": "02"
    },
    "firstName": "senderfirstname",
    "middleName": "sendermiddlename",
    "lastName": "senderLastname",
    "postalCode": "654321",
    "phoneNumber": "01234567892",
    "address1": "Colorful street 123",
    "locality": "Rotterdam",
    "countryCode": "GBR",
    "identificationNumber": "12345678910111213223",
    "personalIdType": "TXIN",
    "administrativeArea": "KA",
    "type": "B",
    "name": "Thomas Smith",
    "referenceNumber": "15426476537657"
  },
  "merchantInformation": {
    "vatRegistrationNumber": "15426476537657",
    "merchantDescriptor": {
      "name": "utf8_merchant_descriptor",
      "alternateName": "",
      "contact": "",
      "address1": "",
      "locality": "Mountain View",
      "country": "",
      "postalCode": "94044",
      "administrativeArea": "CA",
      "phone": "",
      "url": "",
      "countryOfOrigin": "",
      "storeId": "",
      "storeName": "",
      "customerServicePhoneNumber": ""
    }
  },
  "captureOptions": {
    "dateToCapture": "1231"
  },
  "consumerAuthenticationInformation": {
    "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
    "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
  }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193080414227102940072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193080414227102940072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193080414227102940072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193080414227102940072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816645",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417709816645",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193080414227102940072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T09:34:02Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Relay Secure for Merchant Aggregators {#payouts-services-auth-dual-message-aft-vs-agg-intro}
=================================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Enables users to safely validate their identity and safely store their personal identity.

Endpoint {#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e16}
---------------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-vs-agg-intro_d7e35}

Required Fields for a Dual-Message AFT with Relay Secure for Merchant Aggregators Request {#payouts-services-auth-dual-message-aft-vs-agg-reqfields}
===================================================================================================================================================

These fields are required to process a dual-message AFT with Relay Secure for merchant aggregators request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.aggregatorId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-agg-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

[aggregatorInformation.subMerchant.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-add1.md "")
:

[aggregatorInformation.subMerchant.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-admin-area.md "")
:

[aggregatorInformation.subMerchant.cardAcceptorId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-card-accept-id.md "")
:

[aggregatorInformation.subMerchant.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-country.md "")
:

[aggregatorInformation.subMerchant.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-email.md "")
:

[aggregatorInformation.subMerchant.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-id.md "")
:

[aggregatorInformation.subMerchant.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-locality.md "")
:

[aggregatorInformation.subMerchant.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-name.md "")
:

[aggregatorInformation.subMerchant.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-phone-number.md "")
:

[aggregatorInformation.subMerchant.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-postal-code.md "")
:

[aggregatorInformation.subMerchant.region](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-submerch-region.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[recipientInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Relay Secure for Merchant Aggregators {#payouts-services-auth-dual-message-aft-vs-agg-ex-rest}
=================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@pgw.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "nationality": "US",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "01234567892",
        "address1": "Colorful street 123",
        "locality": "Rotterdam",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "",
            "contact": "",
            "address1": "",
            "locality": "Mountain View",
            "country": "",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "",
            "url": "",
            "countryOfOrigin": "",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    },
    "aggregatorInformation": {
        "aggregatorId": "987654321",
        "name": "Aggregator name",
        "subMerchant": {
            "cardAcceptorId": "4321923",
            "id": "572126",
            "name": "sub merchant name",
            "address1": "Tower Plaza 123",
            "locality": "NewJersey",
            "administrativeArea": "NJ",
            "region": "",
            "postalCode": "22102",
            "country": "US",
            "email": "test@test.com",
            "phoneNumber": "987344334112"
        }
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193091579347103140072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193091579347103140072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193091579347103140072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193091579347103140072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816668",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417709816668",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193091579347103140072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T09:52:39Z"
}
```

Dual Message Account Funding Transactions (AFTs) with Network Tokens {#payouts-services-auth-dual-message-aft-token-intro}
==========================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) with Network Tokens provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.
* Increases the security with payout transactions.
* Decreases the chances of fraudulent transactions

Endpoint {#payouts-services-auth-dual-message-aft-token-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-token-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-token-intro_d7e35}

Required Fields for a Dual-Message AFT with Network Tokens Request {#payouts-services-auth-dual-message-aft-token-reqfields}
============================================================================================================================

These fields are required to process a dual-message AFT with network tokens request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.tokenizedCard.card.cryptogram](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-security-code.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:
{#payouts-services-auth-dual-message-aft-token-reqfields_dl_ntn_5xh_2cc}

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[recipientInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:
{#payouts-services-auth-dual-message-aft-token-reqfields_dl_otn_5xh_2cc}

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with Network Tokens {#payouts-services-auth-dual-message-aft-token-ex-rest}
==========================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "WT",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer",
                "storedCredentialUsed": "false"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "tokenizedCard": {
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "number": "4111111111111111",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123",
            "transactionType": "1"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@pgw.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "nationality": "US",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "01234567892",
        "address1": "Colorful street 123",
        "locality": "Rotterdam",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "",
            "contact": "",
            "address1": "",
            "locality": "Mountain View",
            "country": "",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "",
            "url": "",
            "countryOfOrigin": "",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193101615227103440072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193101615227103440072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193101615227103440072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193101615227103440072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816692",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816692",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193101615227103440072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:09:22Z"
}
```

Dual Message Account Funding Transactions (AFTs) to Establish a Recurring Payout Transaction (CIT) {#payouts-services-auth-dual-message-aft-cit-intro}
======================================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

Using the credential-on-file transactions, customers can set up recurring transfers, for example transferring USD 50 to the customer's wallet each month. To set up such a transaction, the customer needs to create a Customer Inititated Transaction (CIT) that establishes the frequency, amount and duration of the recurring transfer. This information is then saved so that follow on Merchant Initiated Transactions (MITs) can occur on the customer's behalf.

Endpoint {#payouts-services-auth-dual-message-aft-cit-intro_d7e16}
------------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-cit-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-cit-intro_d7e35}

Required Fields for a Dual-Message AFT with a CIT Request {#payouts-services-auth-dual-message-aft-cit-reqfields}
=================================================================================================================

These fields are required to process a dual-message AFT with a CIT request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:

[consumerAuthenticationInformation.xid](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:
This field is only required when you have received an XID value in a previous transaction.

[merchantInformation.merchantDescriptor.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-address1.md "")
:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.alternateName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-alt-name.md "")
:

[merchantInformation.merchantDescriptor.contact](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-contact.md "")
:

[merchantInformation.merchantDescriptor.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-county.md "")
:

[merchantInformation.merchantDescriptor.countryOfOrigin](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-of-origin.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.phone](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-phone.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.tokenizedCard.card.cryptogram](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[recipientInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

senderInformation.fundSource
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with a CIT {#payouts-services-auth-dual-message-aft-cit-ex-rest}
===============================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "WT",
        "commerceIndicator": "vbv",
        "authorizationOptions": {
            "initiator": {
                "type": "customer"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        },
        "tokenizedCard": {
            "number": "4111111111111111",
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "transactionType": "1"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@pgw.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "locality": "recipient_city",
        "country": "GBR",
        "nationality": "US",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "9876543210",
        "address1": "senderAddress",
        "locality": "Rotterdam",
        "fundsSource": "card",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "US",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "consumerAuthenticationInformation": {
        "cavv": "ABCDEabcde12345678900987654321abcdeABCDE",
        "xid": "12345678909876543210ABCDEabcdeABCDEF1234"
    },
    "merchantDescriptor": {
        "name": "utf8_merchant_descriptor",
        "alternateName": "merchant alternatename",
        "contact": "9995555444",
        "address1": "merchant address",
        "locality": "Mountain View",
        "country": "US",
        "postalCode": "94044",
        "administrativeArea": "CA",
        "phone": "99955554441",
        "url": "",
        "countryOfOrigin": "US",
        "storeId": "",
        "storeName": "",
        "customerServicePhoneNumber": ""
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193118915937104040072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193118915937104040072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193118915937104040072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193118915937104040072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816726",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816726",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193118915937104040072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:38:12Z"
} 
```

Dual Message Account Funding Transactions (AFTs) for a Recurring Payout Transaction (MIT) {#payouts-services-auth-dual-message-aft-mit-intro}
=============================================================================================================================================

Account Funding Transactions allow a payment service provider to debit funds from a cardholder's Mastercard or Relay account to fund a non-merchant account. This is typically used to load funds onto prepaid cards and electronic wallets.  
Dual Message Account Funding Transactions (AFTs) provide the following benefits:

* Enables customers to identify Mastercard and Relay transactions during the authorization and settlement.
* Allows acquiring partners to use Dual Message BINs when performing a payout transaction.

Using the credential-on-file transactions, customers can set up recurring transfers, for example transferring USD 50 to the customer's wallet each month. To set up such a transaction, the customer needs to create a Customer Inititated Transaction (CIT) that establishes the frequency, amount and duration of the recurring transfer. This information is then saved so that follow on Merchant Initiated Transactions (MITs) can occur on the customer's behalf.

Endpoint {#payouts-services-auth-dual-message-aft-mit-intro_d7e16}
------------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-mit-intro_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#payouts-services-auth-dual-message-aft-mit-intro_d7e35}

Required Fields for a Dual-Message AFT with an MIT Request {#payouts-services-auth-dual-message-aft-mit-reqfields}
==================================================================================================================

These fields are required to process a dual-message AFT with an MIT request:

[acquirerInformation.merchantId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[aggregatorInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-name.md "")
:

captureOptions.dateToCapture
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.alternateName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-alt-name.md "")
:

[merchantInformation.merchantDescriptor.contact](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-contact.md "")
:

[merchantInformation.merchantDescriptor.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-county.md "")
:

[merchantInformation.merchantDescriptor.countryOfOrigin](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-of-origin.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[merchantInformation.merchantDescriptor.phone](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-phone.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.vatRegistrationNumber](https://developer.example.com/docs/ctv/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-vat-registration-num.md "")
:

[orderInformation.amountDetails.anticipatedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-anticipated-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.securityCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.tokenizedCard.cryptogram](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[processingInformation.authorizationOptions.aftIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-aft-ind.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.previousTransactionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:
Set this value to `true`

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.fundingOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-funding-ops-initiator-type.md "")
:

[processingInformation.purposeOfPayment](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purpose-of-payment.md "")
:

[recipientInformation.accountId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-id.md "")
:

[recipientInformation.accountType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-account-type.md "")
:

[recipientInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address1.md "")
:

[recipientInformation.address2](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-address2.md "")
:

[recipientInformation.buildingNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-building-num.md "")
:

[recipientInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")
:

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")
:

[recipientInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-locality.md "")
:

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:
The value must be the standard three character ISO 3166 alpha country code. For more information, see [ISO 3166 Country Codes](https://www.iso.org/iso-3166-country-codes.md "").

[recipientInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-postal-code.md "")
:

[recipientInformation.streetName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-street-name.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")
:

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-number.md "")
:

[senderInformation.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-address1.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")
:

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:

senderInformation.fundSource
:

[senderInformation.identificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-identification-num.md "")
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:

[senderInformation.personalIdType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-personal-id-type.md "")
:

[senderInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-phone-number.md "")
:

[senderInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-postal-code.md "")
:

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

[senderInformation.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-type.md "")
:

Related Information
-------------------

* [REST API Field Reference Guide](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Dual-Message AFT with an MIT {#payouts-services-auth-dual-message-aft-mit-ex-rest}
================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "processingInformation": {
        "businessApplicationId": "AA",
        "commerceIndicator": "recurring",
        "authorizationOptions": {
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true"
            },
            "merchantInitiatedTransaction": {
                "previousTransactionID": "1234567890"
            },
            "aftIndicator": "true",
            "fundingOptions": {
                "initiator": {
                    "type": "S"
                }
            }
        }
    },
        "purposeOfPayment": "16"
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001",
            "securityCode": "123"
        },
        "tokenizedCard": {
            "number": "4111111111111111",
            "cryptogram": "ABCDE12345ABCED12345ABCDE123",
            "transactionType": "3"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100",
            "currency": "USD",
            "anticipatedAmount": "123.45",
            "surcharge": {
                "amount": "5"
            }
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Doe",
            "address1": "1 Market St",
            "locality": "san francisco",
            "administrativeArea": "CA",
            "postalCode": "94105",
            "country": "US",
            "email": "test@test.com",
            "phoneNumber": "4158880000"
        }
    },
    "acquirerInformation": {
        "merchantId": "pa_ctv_sg101"
    },
    "aggregatorInformation.name": "test",
    "recipientInformation": {
        "accountId": "987654321",
        "accountType": "99",
        "address1": "Alpine Eco Road",
        "address2": "Address2 value",
        "firstName": "recFirstname",
        "lastName": "resLastname",
        "middleName": "recMiddletname",
        "nationality": "US",
        "locality": "recipient_city",
        "country": "GBR",
        "postalCode": "571216",
        "streetName": "Alpine eco road",
        "dateOfBirth": "",
        "beneficiaryId": "",
        "beneficiaryName": "",
        "buildingNumber": "Tulip Appartment",
        "beneficiaryAddress": ""
    },
    "senderInformation": {
        "account": {
            "number": "154264765376576126571652675176",
            "fundsSource": "02"
        },
        "firstName": "senderfirstname",
        "middleName": "sendermiddlename",
        "lastName": "senderLastname",
        "postalCode": "654321",
        "phoneNumber": "9876543210",
        "address1": "senderAddress",
        "locality": "Rotterdam",
        "fundsSource": "card",
        "countryCode": "GBR",
        "identificationNumber": "12345678910111213223",
        "personalIdType": "TXIN",
        "administrativeArea": "KA",
        "type": "B",
        "name": "Thomas Smith",
        "referenceNumber": "15426476537657"
    },
    "captureOptions": {
        "dateToCapture": "1231"
    },
    "merchantInformation": {
        "vatRegistrationNumber": "15426476537657",
        "merchantDescriptor": {
            "name": "utf8_merchant_descriptor",
            "alternateName": "merchant alternatename",
            "contact": "9995555444",
            "address1": "merchant address",
            "locality": "Mountain View",
            "country": "US",
            "postalCode": "94044",
            "administrativeArea": "CA",
            "phone": "99955554441",
            "url": "",
            "countryOfOrigin": "US",
            "storeId": "",
            "storeName": "",
            "customerServicePhoneNumber": ""
        }
    }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7193111028367103640072/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7193111028367103640072"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7193111028367103640072/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "7193111028367103640072",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "816710",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "417710816710",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7193111028367103640072",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-06-25T10:25:03Z"
}
```

Original Credit Transactions (OCTs) {#payouts-services-oct-intro}
=================================================================

Original Credit Transactions deliver funds to a recipient's eligible accounts in real-time. OCTs are the second step in transferring funds from an sender to a receiver.

Original Credit Transactions (OCTs) {#payouts-services-oct-standard-intro}
==========================================================================

An OCT deposits funds into a recipient's account.

Endpoint
--------

**Production:** `POST ``https://api.example.com``/pts/v2/payouts`{#payouts-services-oct-standard-intro_restauth}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payouts`{#payouts-services-oct-standard-intro_payouts-barclays-test}

Required Fields for an OCT {#payouts-services-oct-standard-reqfields}
=====================================================================

These fields are required in a request for an OCT:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

clientReferenceInformation.requestId
:

merchantInformation.merchantDescriptor.street
:

merchantInformation.merchantId
:

merchantInformation.verificationValue
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Cannot exceed 50,000 USD.
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:

processingInformation.octAftReferenceRequestId
:

[recipientInformation.countryOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country-of-birth.md "")
:

[recipientInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-date-of-birth.md "")
:

[recipientInformation.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-email.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

recipientInformation.name
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:

[recipientInformation.occupation](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-occupation.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-num.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-date-of-birth.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:
First name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:
Required with Relay for South Africa.

senderInformation.id
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:
Last name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:
If the sender is an individual, use the senderInformation.firstName and senderInformation.lastName fields instead.

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

REST Example: OCT Request {#payouts-services-oct-ex-rest}
=========================================================

Request: Authorization Service for an OCT

```
{
    "clientReferenceInformation": {
        "code": "TC-23456$",
        "requestId": "6642672790803228323604"
    },
    "merchantInformation": {
        "merchantId": "pa_oct_sg101_ccs",
        "merchantDescriptor": {
            "street": "test",
            "state": "CA"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "card": {
            "number": "411111111111XXXX",
            "expirationMonth": "12",
            "expirationYear": "2026",
            "type": "001"
        }
    },
    "processingInformation": {
        "businessApplicationId": "aa",
        "icsApplications": "ics_oct"
    },
    "recipientInformation": {
        "name": "RecepientNameRecepientNameName",
        "firstName": "rfirstName",
        "middleName": "rmiddlename",
        "lastName": "rlastname",
        "address": {
            "address1": "test",
            "address2": "test",
            "buildingNumber": "test",
            "city": "test",
            "country": "US",
            "postalCode": "9440",
            "streetName": "test",
            "state": "1"
        }
    },
    "senderInformation": {
        "account": {
            "number": "1234",
            "fundsSource": "03"
        },
        "address": "abc",
        "city": "SenderCitySenderCitySende",
        "country": "Zim",
        "id": "ms_user",
        "referenceNumber": "1",
        "state": "AZ"
    }
}
```

Response: Authorization Service for an OCT

```
{
    "clientReferenceInformation": {
        "code": "TC-23456$"
    },
    "id": "7465072232626783103812",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "responseCode": "100"
    },
    "reconciliationId": "610954017ABE1KUI",
    "status": "ACCEPTED",
    "submitTimeUtc": "2025-05-06T045343Z"
}
```

Original Credit Transactions (OCTs) with Aggregators {#payouts-services-oct-agg-intro}
======================================================================================

Required Fields for an OCT with Aggregators {#payouts-servies-oct-agg-req-fields}
=================================================================================

These fields are required in a request for an OCT with aggregators:

[aggregatorInformation.city](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-city.md "")
:

[aggregatorInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-country.md "")
:

[aggregatorInformation.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-postal-code.md "")
:

[aggregatorInformation.state](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-state.md "")
:

[aggregatorInformation.streetAddress](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/agg-info-aa/agg-info-street-address.md "")
:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

clientReferenceInformation.requestId
:

merchantInformation.merchantDescriptor.street
:

merchantInformation.merchantId
:

merchantInformation.verificationValue
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Cannot exceed 50,000 USD.
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")
:
Not required when your account includes this value.

processingInformation.octAftReferenceRequestId
:

[recipientInformation.countryOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country-of-birth.md "")
:

[recipientInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-date-of-birth.md "")
:

[recipientInformation.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-email.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

recipientInformation.name
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:

[recipientInformation.occupation](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-occupation.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-num.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-date-of-birth.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:
First name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:
Required with Relay for South Africa.

senderInformation.id
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:
Last name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:
If the sender is an individual, use the senderInformation.firstName and senderInformation.lastName fields instead.

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: OCT Request with Aggregators {#payouts-services-oct-agg-ex-rest}
==============================================================================

Request: Authorization Service for an OCT with Aggregators

```
{
    "aggregatorInformation": {
        "city": "Bally",
        "country": "US",
        "postalCode": "560037",
        "serviceProvidername": "YourServiceProvider",
        "state": "CD",
        "streetAddress": "11 Elvine Street"
    },
    "clientReferenceInformation": {
        "code": "TC-23456$",
        "requestId": "6642672790803228323604"
    },
    "merchantInformation": {
        "merchantId": "pa_oct_sg101_ccs",
        "merchantDescriptor": {
            "street": "test",
            "state": "CA"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "card": {
            "number": "411111111111XXXX",
            "expirationMonth": "12",
            "expirationYear": "2026",
            "type": "001"
        }
    },
    "processingInformation": {
        "businessApplicationId": "aa",
        "icsApplications": "ics_oct"
    },
    "recipientInformation": {
        "name": "RecepientNameRecepientNameName",
        "firstName": "rfirstName",
        "middleName": "rmiddlename",
        "lastName": "rlastname",
        "address": {
            "address1": "test",
            "address2": "test",
            "buildingNumber": "test",
            "city": "test",
            "country": "US",
            "postalCode": "9440",
            "streetName": "test",
            "state": "1"
        }
    },
    "senderInformation": {
        "account": {
            "number": "1234",
            "fundsSource": "03"
        },
        "address": "abc",
        "city": "SenderCitySenderCitySende",
        "country": "Zim",
        "id": "ms_user",
        "referenceNumber": "1",
        "state": "AZ"
    }
}
```

Response: Authorization Service for an OCT with Aggregators

```
{
    "clientReferenceInformation": {
        "code": "TC-23456$"
    },
    "id": "7465085270996951503814",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "responseCode": "100"
    },
    "reconciliationId": "61095801LABCSIJL",
    "status": "ACCEPTED",
    "submitTimeUtc": "2025-05-06T051527Z"
}
```

Original Credit Transactions (OCTs) with Tokens {#payouts-services-oct-token-intro}
===================================================================================

An OCT with a token deposits funds into a recipient's account.

Endpoint
--------

**Production:** `POST ``https://api.example.com``/pts/v2/payouts`{#payouts-services-oct-token-intro_restauth}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payouts`{#payouts-services-oct-token-intro_payouts-ctv-test}

Required Fields for an OCT with Tokens {#payouts-services-oct-token-reqfields}
==============================================================================

These fields are required in a request for an OCT with tokens:

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

clientReferenceInformation.requestId
:

merchantInformation.merchantDescriptor.street
:

merchantInformation.merchantId
:

merchantInformation.verificationValue
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Cannot exceed 50,000 USD.

[paymentInformation.customer.customerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[processingInformation.businessApplicationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-business-appl-id.md "")

processingInformation.octAftReferenceRequestId
:

[recipientInformation.countryOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-country-of-birth.md "")
:

[recipientInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-date-of-birth.md "")
:

[recipientInformation.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-email.md "")
:

[recipientInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-first-name.md "")

[recipientInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-last-name.md "")

[recipientInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-middle-name.md "")
:

recipientInformation.name
:

[recipientInformation.nationality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-nationality.md "")
:

[recipientInformation.occupation](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/recipient-info-aa/recipient-info-occupation.md "")
:

[senderInformation.account.fundsSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-funds-source.md "")

[senderInformation.account.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-account-num.md "")
:

[senderInformation.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-administrative-area.md "")

[senderInformation.countryCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-country-code.md "")
:

[senderInformation.dateOfBirth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-date-of-birth.md "")
:

[senderInformation.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-first-name.md "")
:
First name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:
Required with Relay for South Africa.

senderInformation.id
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:
Last name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:

senderInformation.id
:

[senderInformation.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-last-name.md "")
:
Last name of sender when the sender is an individual. Required for original credit transactions (OCTs) that use the Payouts services and supported only for Mastercard card transactions. If the sender is a business or government entity, use the senderInformation.name field instead.
:

[senderInformation.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-locality.md "")
:

[senderInformation.middleName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-middle-name.md "")
:

[senderInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-name.md "")
:
If the sender is an individual, use the senderInformation.firstName and senderInformation.lastName fields instead.

[senderInformation.referenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/sender-info-aa/sender-info-reference-number.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: OCT with Tokens Request {#payouts-services-oct-token-ex-rest}
===========================================================================

Request: OCT Service with Tokens

```
{
    "clientReferenceInformation": {
        "code": "TC-23456$",
        "requestId": "6642672790803228323604"
    },
    "merchantInformation": {
        "merchantId": "pa_oct_sg101_ccs",
        "merchantDescriptor": {
            "street": "test",
            "state": "CA"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "customer": {
            "customerId": "F39732BE4BDA9A1EE053AF598E0A4081"
        }
    },
    "processingInformation": {
        "businessApplicationId": "aa",
        "icsApplications": "ics_oct"
    },
    "recipientInformation": {
        "name": "RecepientNameRecepientNameName",
        "firstName": "rfirstName",
        "middleName": "rmiddlename",
        "lastName": "rlastname",
        "address": {
            "address1": "test",
            "address2": "test",
            "buildingNumber": "test",
            "city": "test",
            "country": "US",
            "postalCode": "9440",
            "streetName": "test",
            "state": "1"
        }
    },
    "senderInformation": {
        "account": {
            "number": "1234",
            "fundsSource": "03"
        },
        "address": "abc",
        "city": "SenderCitySenderCitySende",
        "country": "Zim",
        "id": "ms_user",
        "referenceNumber": "1",
        "state": "AZ"
    }
}
```

Response: OCT Service with Tokens

```
{
    "clientReferenceInformation": {
        "code": "TC-23456$"
    },
    "id": "7465080235346809903814",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.01",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "responseCode": "100"
    },
    "reconciliationId": "61085203OABFKN5Q",
    "status": "ACCEPTED",
    "submitTimeUtc": "2025-05-06T050703Z"
}
```

Reference {#payouts-ref-intro}
==============================

This section provides helpful reference information for using Payouts services.

Business Application Identifier {#payouts-appendix-bai}
=======================================================

The Business Application Identifier (BAI) identifies the category of the Account Funding Transaction (AFT).  
All acquirers, service providers, and merchants must submit a valid BAI value when submitting an AFT.  
Provide one of the values when you send field `processingInformation.businessApplicationId`.

> IMPORTANT Ensure that your acquirer has a Merchant Category Code (MCC) that corresponds with the BAI value you are using. For more information, contact your acquirer.

| BAI Value | Category                                                                                                                                   | Requirements                                                                                                                                                                                                                                                                                                                                                                    |
|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AA`      | Account-to-Account money transfer. This value is for funding the cardholder's own account at the same or a different financial institution | Both accounts must be owned by the same person or entity. > IMPORTANT > If you are funding a prepaid account, use the ` TU ` value. Do not use the ` AA ` value.                                                                                                                                                                                                                |
| `BI`      | Financial institution offered Bank-initiated P2P money transfer                                                                            | P2P (person-to-person) money transfer is initiated from an online banking system, making it a bank-initiated transaction. This category is only used for specific scenarios and only available in limited markets. For more information, contact your Relay representative.                                                                                                      |
| `FD`      | Funds Disbursement                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                 |
| `FT`      | Funds Transfer                                                                                                                             | If the funds will be used for a high-brand risk transaction, the applicable high-brand risk MCC must be used. If a wallet is used to purchase liquid and cryptocurrency assets, the applicable special condition indicator must be used.                                                                                                                                        |
| `PD`      | Payroll Disbursement                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                 |
| `PP`      | Person-to-Person (P2P) money transfer                                                                                                      | P2P Money Transfer is initiated from an online banking system, making it a bank-initiated transaction. This category is used only when both AFTs and OCTs are supported. When an AFT is only supported, use the `FT` category.                                                                                                                                                  |
| `TU`      | Prepaid Card Load or Top-up                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                 |
| `WT`      | Staged Digital Wallet (SDW) Transfer                                                                                                       | If the funds will be used for a high-brand risk transaction, the applicable high-brand risk MCC must be used. If the funds are used for a gambling transaction, the applicable gambling MCC must be used. If a wallet is used to purchase liquid and cryptocurrency assets, the applicable special condition indicator must be used. An AFT is not intended for debt repayment. |
[Business Application Identifier Values]

**Business Application Identifier and Merchant Category Code Use Cases** {#payouts-ref-bai-mcc}
===============================================================================================

Acquirers, service providers, and you must use the correct Business Application Identifier (BAI) and Merchant Category Code (MCC) in the OCT authorization request message. These codes also be used in the clearing and settlement messages. This helps identify the type of OCT and the merchant or business that started the transaction.  
Both the BAI and the MCC help the issuer identify the business purpose of the OCT. The MCC should represent you, the acquirer, or the service provider/payment facilitator involved in the OCT transaction. Acquirers receive instructions during program approval on which BAI to use for their OCTs. The BAI and MCC Usage -- Money Transfer table lists the available BAIs and provides examples of relevant use cases.  
Certain industries, such as healthcare, insurance, payroll, and gambling, are regulated by federal, provincial, and local laws. You, acquirers, and service providers are responsible for ensuring that your Relay Direct program complies with all applicable laws. This includes making required disclosures, obtaining necessary consents, and ensuring that OCTs are not sent to or from countries where gambling is illegal.  
The table shows MCCs based on specific use cases. This is not a full list of all MCCs used with OCT.

> IMPORTANT  
> Starting April 16, 2023, ` Payment Gateway ` requires the merchant name field in a stand-alone tipping transaction to include the word "tip" for tipping use-cases.

|              BAI               |                                                                                                                                                                                          Use Case                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                            MCC                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                      Examples of Use                                                                                                                                                                                                                                                                                                       |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AA`                           | Account-to-Account Remote Deposit Check (RDC) capture Consumer funding of their own account                                                                                                                                                                                                                                                                                                 | `4829` Non-financial Institution Wire Transfer Money Orders (WTMOs) (Not applicable to the US with BAI `AA`) `6012` Financial Institutions: Merchandise and services `6211` Security Brokers/Dealers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | For OCT, this is a sender moving money from their own account to their card account. Me-to-Me money transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `BI`                           | Bank-Initiated Money Transfer **Important:** BAI `BI` is used for very specific scenarios and is enabled only in limited markets. Contact your Relay representative for information on: * The availability of BAI `BI` in your market, and * Applicability of BAI `BI` to your program. {#payouts-ref-bai-mcc_ul_k3p_3by_z2c}                                                                | `6012` Financial Institutions: Merchandise and services BAI `BI` should only be used in combination with MCC `6012`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Money transfer is initiated from an online banking system, making it a bank-initiated transaction. Usage of this BAI applies to money transfer offered in a closed-loop solution.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `CD`                           | Cash Deposit                                                                                                                                                                                                                                                                                                                                                                                | `6012` or Retail Merchant MCC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Deposit of cash using an OCT to add funds to a debit account at a bank branch or retail location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `FT`                           | Funds Transfer                                                                                                                                                                                                                                                                                                                                                                              | `6540` Non-financial Institutions: Stored value card purchase/load `4829` Non-financial Institution Wire Transfer Money Orders (WTMOs) `6012` Financial Institutions: Merchandise and services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Cashing out a Stored Value Digital Wallet (SVDW) account. Liquid and cryptocurrency asset as a general purpose wallet, proceeds from a sale or cash out, are paid out with an OCT with BAI `FT`. Cryptocurrency transactions must include the Special Condition Indicator (Field 60.4) = `7`. Wallet providers must use BAI `LA` instead of `FT`/`WT` for cashing out funds if it is a general-purpose wallet, and 50 percent or more of their annual sales volume comes from liquid or cryptocurrency assets.                                                                                                             |
| `LA` Effective 19 October 2024 | Liquid Assets A new BAI for Relay Direct transactions involving wallet pre-funding or the direct purchase of liquid and cryptocurrency assets. In Canada and the US the new BAI value will not be applicable for origination of domestic OCTs. Issuers and issuer processors must be ready to receive new BAI value of `LA` for cross-border OCTs originating outside of Canada and the U.S. | Any originating entity identified as a foreign currency exchange or cryptocurrency merchant, broker, or platform. `6012` -- Financial Institutions: Merchandise, services, and debt repayment `6051` -- Non-Financial Institutions: Foreign currency, liquid and cryptocurrency assets (cryptocurrency), money orders (not money transfer), account funding (not stored value load), travelers cheques, and debt repayment; must identify Relay Direct transactions under the BAI value of `LA`. `6211` -- Security Brokers/Dealers Brokerage. If greater than 50 percent of client annual sales volume, measured in the client's local fiat currency comes from noncryptocurrency (for example, stocks, bonds, and so on). | Liquid and cryptocurrency asset, proceeds from a sale or cash out, are paid out with an OCT with BAI `LA`. Cryptocurrency transactions must include the Special Condition Indicator (Field 60.4) = 7. Wallet providers must use BAI LA instead of `FT`/`WT` for cashing out funds if it is a general-purpose wallet, and 50 percent or more of their annual sales volume comes from liquid or cryptocurrency assets.                                                                                                                                                                                                       |
| `PP`                           | P2P Money Transfer                                                                                                                                                                                                                                                                                                                                                                          | `4829` Non-Financial Institution Wire Transfer Money Orders (WTMOs) `6012` Financial Institutions: Merchandise and services Based on the type of services, combine MCC `6012` with a valid BAI. Bank-initiated P2P programs must use a BAI of `BI` and MCC `6012` or a BAI of `PP` and MCC `6012`. Non bank-offered services must use a combination of PP and `4829`.                                                                                                                                                                                                                                                                                                                                                      | For OCT, this is a sender sending money to someone else's account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `WT`                           | Wallet Transfer-Staged Digital Wallet (SDW) Transfer                                                                                                                                                                                                                                                                                                                                        | `6051` Non-financial Institutions: Foreign currency, liquid and cryptocurrency assets (for example: cryptocurrency), money orders (not money transfer), account funding (not stored value load), travelers checks, and debt repayment `4829` Non-Financial Institution Wire Transfer Money Orders (WTMOs) `6012` Financial Institutions: Merchandise and services                                                                                                                                                                                                                                                                                                                                                          | For OCT this is the withdrawal or cash out of funds from a staged digital wallet to a card account. Wallet providers must use BAI `LA` instead of `FT`/`WT` for cashing out funds if it is a general-purpose wallet, and 50 percent or more of their annual sales volume comes from Liquid or Cryptocurrency assets. If the wallet supports cryptocurrency, this must be communicated by setting the Special Condition indicator (Field 60.4) = **7**. Acquirers and originators in Europe, India, and Brazil are not required to submit a business application identifier of `WT` for staged digital wallet transactions. |
[BAI and MCC Usage -- Money Transfer]

|                                                               BAI                                                                |                                                                                                                                                                                                                                                                                                                                                                                                         Use Case                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                        MCC                                                                                                                                                                                                                                        |                                                                                                                                                    Example of Use                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BB` (Not applicable to the US)                                                                                                  | Business-to-business Supplier Payments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Any MCC associated to the merchant, acquirer, or service provider business (example: `5812` = restaurant, `5311` = department store)                                                                                                                                                                                                                                                                                                                                              | Business-to-business payments for business-related supplies.                                                                                                                                                                                                                                                         |
| `BP`                                                                                                                             | Non-card Bill Pay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | MCC associated to the recipient business                                                                                                                                                                                                                                                                                                                                                                                                                                          | For non-card bill payment.                                                                                                                                                                                                                                                                                           |
| `CP`                                                                                                                             | Credit Card Bill Pay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `4829` Non-financial Institution Wire Transfer Money Orders (WTMOs) `6012` Financial Institutions: Merchandise and services                                                                                                                                                                                                                                                                                                                                                       | Pushing funds to a credit card account as a payment.                                                                                                                                                                                                                                                                 |
| `FD` > IMPORTANT > If requesting to use FD for a subuse case not listed, it must be described in detail in the PIF for approval. | General Funds Disbursement: All other funds disbursements not listed. Examples: * Commission payments * Digital goods -- games * Insurance payments * Loan disbursements * Alternative/online lending or peer-to-peer lending * Shared economy * Tax refund services: non-government initiated (for example, tax preparation businesses) * VAT tax reclamation * Earned wage access * Gig worker payouts * Marketplace payouts * Contractor payouts * Tip payouts * Corporate expense reimbursement * "Bad customer experience" payouts (for example, airline payment to disgruntled passenger) * Rebates * Education disbursements * Security deposit refunds * Reimbursement of over payments to billers (for example, Business owes me USD 50 after I cancel service mid-month) {#payouts-ref-bai-mcc_ul_m3p_3by_z2c} | Any MCC associated to the merchant, acquirer, or service provider business (example: `5812` = restaurant, `5311` = department store)                                                                                                                                                                                                                                                                                                                                              | Funds disbursements not covered by other BAI use cases listed above. If the program supports cryptocurrency, this must be communicated by setting the Special Condition indicator (Field 60.4) = **7**.                                                                                                              |
| `GD`                                                                                                                             | Government Disbursements and Government Initiated Tax Refunds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `9399` Government services (not elsewhere classified) `9402` Postal services -- government only `9405` U.S. Federal government agencies or departments 9222 fines; government administered `9211` Court costs, including alimony and child support 9311 tax payments                                                                                                                                                                                                              | Government payments, including social security payments, unemployment, disability, jury duty, and disaster relief/emergency.                                                                                                                                                                                         |
| `GP`                                                                                                                             | Gambling/Gaming Payouts (other than online gambling)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `7800` Government owned lottery (US only) `7801` Government-licensed casinos (US only) `7802` Government-licensed horse/dog racing (U.S. only). `7800`, `7801`, and `7802` are US only MCCs that also require the use of a valid Merchant Verification Value (MVV). Merchants must register with Relay to obtain an MVV. `7995` Betting, including lottery tickets, casino gaming chips, off-track betting, and wagers at racetracks `9406` Government-owned lottery (non-US only) | Casino payouts at gaming floor counter and sports books. Advanced deposit wagering. Gambling that is not considered online gambling.                                                                                                                                                                                 |
| `LO`                                                                                                                             | Loyalty Payments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Any MCC associated to the merchant, acquirer, or service provider business Examples: * `5812` = restaurant * `5311` = department store {#payouts-ref-bai-mcc_ul_n3p_3by_z2c}                                                                                                                                                                                                                                                                                                      | Payment for a canceled loyalty program/service, deposit refunds, employee rewards, and purchase rebate payments.                                                                                                                                                                                                     |
| `MD`                                                                                                                             | Merchant Settlement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `6012` Acquirers sending settlement payments to merchants `4829` Payment facilitator (includes sponsored processors, and ISOs) sending settlement payments to merchants                                                                                                                                                                                                                                                                                                           | Merchant payments for purchase transaction processing where the processor sends settlement payments to a Relay card account using OCT.                                                                                                                                                                                |
| `MI` **Effective January 2024**                                                                                                  | Faster Refunds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Any MCC associated with the merchant, acquirer, or service provider business.                                                                                                                                                                                                                                                                                                                                                                                                     | Refund purchases of goods and services made on a Relay Card using OCT.                                                                                                                                                                                                                                                |
| `OG`                                                                                                                             | Online Gambling Payouts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `7800` Government-owned lottery (US only) `7801` Government-licensed Casinos (US only) `7802` Government-licensed horse/dog racing (US only) `7995` Betting, including lottery tickets, casino gaming chips, off-track betting, and wagers at racetracks `9406` Government-owned lottery (non-US only)                                                                                                                                                                            | Payout of winnings from online gambling merchants, including casinos, horse/dog racing wagers, lottery, digital, and social gaming payouts.                                                                                                                                                                          |
| `PD`                                                                                                                             | Payroll and Pensions Disbursements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `8931` Accounting, auditing, and bookkeeping services                                                                                                                                                                                                                                                                                                                                                                                                                             | Independent contractor works for temporary staffing agency or directly with an employer, submits time sheet or completes project, and is paid to bank account by using a debit card.                                                                                                                                 |
| `RP`                                                                                                                             | Request-to-Pay Service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Refer to *Relay Direct Request to Pay Implementation Guide* for information on eligible MCC.                                                                                                                                                                                                                                                                                                                                                                                       | Relay's Request-to-Pay (R2P) service is a secure messaging framework built on APIs that enable client to request payment and communicate about a payment obligation, enabling bill splitting, and funds collection functionality for mobile banking applications. Limited geographic scope to Ukraine and Kazakhstan. |
| `TU`                                                                                                                             | Prepaid Card Load                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `6012` Financial Institutions -- merchandise and services `6540` Non-financial Institutions: Stored-value card purchase/load                                                                                                                                                                                                                                                                                                                                                      | Loads, reloads, and top-ups to prepaid card accounts. Restricts use to Prepaid card only. CardNet edit declines the transaction if the card product is not prepaid and BAI is `TU`. Money transfer velocity limits apply.                                                                                            |
[BAI and MCC Usage -- Funds Disbursement/Non-Money Transfer]

Relay issuers/issuer processors are required to receive and process all types of OCTs.

Sender Source {#payouts-appendix-sender-source}
===============================================

The Sender Source field identifies the source of funds. Provide one of the values when you send field `senderInformation.account.fundsSource`.  
All acquirers, service providers, and merchants are required to submit a valid sender source value when submitting an AFT.

| Value | Definition                                                                                                                                                                                                                    |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `01`  | Credit card                                                                                                                                                                                                                   |
| `02`  | Debit card                                                                                                                                                                                                                    |
| `03`  | Prepaid card                                                                                                                                                                                                                  |
| `04`  | Cash                                                                                                                                                                                                                          |
| `05`  | Debit or deposit accounts that are not linked to a Relay card such checking accounts, savings accounts, proprietary Payment Gateway `senderInformation.account.fundsSource` debit or ATM card account, and digital wallet account. |
| `06`  | Credit accounts that is not linked to a Relay card such as credit cards and proprietary lines of credit.                                                                                                                       |
[Sender Source Values]

Test Card Numbers {#payouts_oct_test_cards}
===========================================

Use the `Payment Gateway` test card numbers for OCTs validate your transactions. These numbers help you mimic real-life situations, find problems, and improve transaction safety and efficiency.

| Request                                                                                                                                                                                                           | Test Card Number |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| [Original Credit Transactions (OCTs)](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-standard-intro.md "")             | 4111111111111111 |
| [Original Credit Transactions (OCTs) with Aggregators](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-agg-intro.md "") | 4111111111111111 |
| [Original Credit Transactions (OCTs) with Tokens](/docs/gateway/en-us/payouts/developer/ctv/rest/payouts-dev/payouts-services-oct-intro/payouts-services-oct-token-intro.md "")    | 4111111111111111 |
[Test Card Numbers for OCTs]

