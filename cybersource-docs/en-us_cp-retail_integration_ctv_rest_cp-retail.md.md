Card Present Connect \| Retail Integration Guide {#cp-retail-about-guide}
=========================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This guide is written for merchants who want to process card-present retail payments through `Cybersource` and provides information about the `REST API` guide for `Platform Connect`. For information about additional requirements and options for card-present transactions, see the [*Payments Developer Guide*](https://developer.cybersource.com/docs.md#PaymentServices "") in the Technical Documentation Portal.

Conventions
-----------

The following special statement is used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#cp-retail-doc-revisions}
============================================================

26.01.01
--------

:
Added new features:

    * [Strong Customer Authentication Support in the EU Region](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-intro-cpc/cp-auth-sca-intro.md "")
    * [Deferred Authorization](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro/cp-services-deferred-auth-intro.md "")
    {#cp-retail-doc-revisions_ul_wmk_ll3_b3c}

:
Renamed PIN Debit EBT Purchase with SNAP Account Swiped Track Data and Balance Inquiry to [PIN Debit EBT Purchase with SNAP Account Swiped Track Data and Balance Response Data](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-ebt-purch-swipe-snap-bal-inq-task.md ""). Also replaced REST API request and response examples.
:
Updated REST API required fields list and request and response examples in [Reverse a PIN Debit EBT Purchase](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-ebt-void-task.md "").

25.09.01
--------

This update contains only editorial changes and no technical updates.

25.06.01
--------

:
Added support for Discover cash advance in [Authorization for Cash Advance with Credit Card](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro/cp-services-auth-cash-adv-intro.md "").

25.02
-----

:
Renamed "Card Present Payment Processing" to [Retail Payment Services Using EMV and Card Data](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro.md "").
:
Added new EMV and card data information for payment services in [Retail EMV and Card Data](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro/cp-emv-card-data.md "").
:
Renamed "Card-Present Mobile Point-of-Sale Payment Processing" to [Mobile Point-of-Sale Payment Services](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-services-mpos-intro.md "").
:
Updated fields and examples in [Authorization for Cash Advance with Credit Card](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro/cp-services-auth-cash-adv-intro.md "").
:
Added new international transaction feature. See [Dynamic Currency Conversion Payment Services](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/dcc-intro.md#dcc-intro "").

25.01
-----

:
Reorganized these sections, making only editorial changes and no technical updates:

    * [Retail Payment Services Using EMV and Card Data](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro.md "").
    * [Introduction to PIN Debit Processing](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-pd-pin-debit-intro.md "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Card Present Connect \| Retail {#cp-intro-cpc}
==============================================================

Card Present Connect \| Retail is part of a unified commerce solution for payment technology providers. This solution supports card-present transactions at the point of sale (POS) and on mobile POS devices. It also enables you to integrate with multiple processors and acquirers.  
The platform uses end-to-end encryption to enable secure and innovative payment solutions. Retail integration and value-added services are available through a single integration on the Card Present Connect payment management platform.  
An added benefit of Card Present Connect \| Retail is that you can streamline Platform Connect certification, which helps you verify secure and compliant payments.

Enabling the Card Present Connect Platform {#cp-enabling-task}
==============================================================

Before you can use the Card Present Connect platform, you must enable it.  
Follow these steps to enable the Card Present Connect platform:

1. Set up a `Cybersource` merchant account. To get started, contact your sales engineer, alliance partner, or technical account manager.
2. Integrate the `Cybersource` APIs for use on the Card Present Connect platform.
3. Integrate your terminal's key management encryption and decryption with the Card Present Connect platform.
4. Complete message-level validation (MLV) and Level 3 (L3) device certification. To get started, contact your sales engineer, alliance partner, or technical account manager.

Supported Card Entry Modes {#cp-intro-transactions}
===================================================

Card entry modes describe the ways a payment terminal captures card data during an in-person transaction. These modes depend on how the customer's card interacts with the device and determine how the terminal reads and processes the card information. Understanding these entry modes helps ensure the correct method is used when completing a card-present transaction at a physical retail location.  
Card-present transactions support these entry modes:

EMV (chip-based)
:
The customer inserts the card for a contact payment or taps the card or device for a contactless payment.

Magnetic stripe
:
The customer swipes the card through the magnetic-stripe reader on the device.

Hand-keyed
:
You manually enter the card details when EMV or magnetic-stripe data is unavailable due to card damage, read failure, or other limitations.  
Card-present transactions are typically more secure than card-not-present transactions because both the cardholder and the card are physically present. However, standard risk-control measures still apply. For more information, see [Card-Present Transaction Risk Control Requirements](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-intro-cpc/cp-intro-transactions-risk-control.md "").

EMV Card Entry Modes {#cp-intro-about-transactions-emv}
=======================================================

EMV card entry modes describe the ways a payment terminal reads card data from an EMV‑enabled payment card. An EMV card contains an embedded chip that stores cardholder data securely and supports methods that help reduce fraud and improve transaction security.  
The payment terminal uses these card entry modes to obtains EMV card data:

Contact
:
The customer inserts a chip‑enabled card into the payment terminal. You can verify the customer's identity by requiring PIN entry. When signature use cases are added, signature verification might also apply.

Contactless
:
The customer taps a contactless‑enabled card or a payment‑enabled mobile or wearable device on or near the terminal. Supported devices, including cards, phones, watches, and wearables, use the same underlying contactless technology. This type of payment is also called *Tap to Pay*.

Magnetic Stripe Entry Mode {#cp-intro-about-transactions-swipe}
===============================================================

Payment cards typically store customer data on a magnetic stripe embedded in the back of the card. For this entry mode, a customer swipes their card on a payment terminal to pass this data to the merchant's point-of-sale system. Swiping the payment card is typically used for non-EMV cards, such as pre-paid cards, or as an alternative payment method when a contact or contactless EMV payment fails.  
The magnetic stripe entry mode describes how a payment terminal reads card data from the magnetic stripe on the back of a payment card. The terminal captures this data when the customer swipes the card, enabling the point-of-sale system to process the transaction.  
This entry mode is often used for non‑EMV cards, such as prepaid cards, or when EMV contact or contactless interaction cannot be completed due to card or terminal issues.  
Although magnetic‑stripe entry provides a fallback when EMV methods are unavailable, it offers less security because magnetic‑stripe data is easier to copy or compromise. Standard risk‑control measures still apply when using this entry mode. For more information, see [Card-Present Transaction Risk Control Requirements](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-intro-cpc/cp-intro-transactions-risk-control.md "").

Hand-Keyed Entry Mode {#cp-intro-about-transactions-keyed}
==========================================================

Hand-keyed entry mode describes how a point-of-sale (POS) system captures card data when the terminal cannot read the card electronically through EMV or magnetic-stripe methods. In this fallback card-data entry mode, you manually type the card details into the POS when the terminal cannot read the card reliably, the card is damaged, or standard entry modes are unavailable.

Card-Present Transaction Risk Control Requirements {#cp-intro-transactions-risk-control}
========================================================================================

Card-present transactions carry lower risk than card-not-present transactions because the customer and payment card are physically present, which can result in lower transaction fees. However, acquirers must still apply standard risk-control measures. Acquirers must monitor transaction activity and manage fraud and disputes in accordance with payment network rules, including the Global Acquirer Risk Standards. They also must comply with these Relay risk compliance programs:

* Relay Fraud Monitoring Program

* Relay Dispute Monitoring Program
  {#cp-intro-transactions-risk-control_ul_gmj_31g_d3c} To meet risk control requirements, acquirers can use one of these options:

* Enable `Cybersource` transaction and fraud monitoring tools.

* Ensure that their payment technology partners (PTPs) implement transaction and fraud monitoring tools.

* Deploy their own transaction and fraud monitoring tools.

Each option provides necessary fraud and risk controls for direct merchant relationships and for PTPs that do not operate their own monitoring solutions. For more information, see [Fraud and Risk Management Solutions](https://www.cybersource.com/en-us/solutions/fraud-and-risk-management.md "").

Strong Customer Authentication Support in the EU Region {#cp-auth-sca-intro}
============================================================================

Card Present Connect enables merchants to process card-present transactions in compliance with global payment regulations and mandates. In response to European Union (EU) updates to industry standards, specifically Payment Services Directive version 2 (PSD2) and Strong Customer Authentication (SCA) requirements, `Cybersource` now supports SCA transaction processing.  
To comply with PSD2, American Express, Mastercard, and Relay use specific authorization response codes to indicate when SCA is required but was not provided in the initial transaction. This temporary transaction decline is known as a *soft decline*. Card Present Connect supports soft decline response codes for card-present EMV contact and contactless transactions.  
An authorization response that includes a soft decline response code indicates that the transaction cannot be approved until SCA is performed. The payment technology provider's (PTP) point-of-sale (POS) solution must restart the transaction and request information from the customer to complete SCA. The customer typically completes authentication by providing their PIN. How the customer provides SCA information depends on the card type, payment entry mode, and the soft-decline response code received.

Requirements for Strong Customer Authentication Support in the EU Region {#cp-auth-sca-requirements}
====================================================================================================

Your POS system must meet these requirements to ensure PSD2 compliance and support card-present transactions with SCA.

* Supports these POS system capabilities:
  * Contact or contactless EMV transactions
  * Online PIN transactions (where applicable)
  * Repeated transactions with encrypted PIN
* Supports these rest API fields and values to trigger repeated transactions with PIN:
  * pointOfSaleInformation.emv.isRepeat = `true`
  * pointOfSaleInformation.encryptedKeySerialNumber = `&lt;encrypted KSN value&gt;`
  * pointOfSaleInformation.encryptedPin = `&lt;encrypted PIN block&gt;`
  * pointOfSaleInformation.pinBlockEncodingFormat = `encrypted PIN block format`
* Supports these soft-decline authorization response codes:
  * `1A`
  * `65`
  * `70`
    {#cp-auth-sca-requirements_ul_xvh_vc3_b3c}

Supported Soft Decline Authorization Response Codes in the EU Region {#cp-auth-sca-soft-decline-response-codes}
===============================================================================================================

The table outlines the soft-decline authorization response codes (ARC) supported by various card types in the EU region.

| Card Type        |              Soft Decline Authorization Response Code              |                                                                                               Action Based on Response Code                                                                                               | CAS Test Trigger Amount |
|:-----------------|:------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------|
| American Express |                                `1A`                                |                 Device switches to contact payment interface (for ARC `12`), when supported, Cardholder is prompted to insert payment card into terminal. If not supported, the transaction is declined.                  | `4128.00`               |
| American Express | Parsing information: ARC = `12` (EMV Reply Tag 91, last two bytes) |                 Device switches to contact payment interface (for ARC `12`), when supported, Cardholder is prompted to insert payment card into terminal. If not supported, the transaction is declined.                  | `4128.00`               |
| American Express |                                `1A`                                | Device prompts cardholder for online PIN (for ARC `13`). Original authorization request is resubmitted with online PIN. Include this REST API field and value in the request: pointOfSaleInformation.emv.isRepeat=`true`. | `4128.00`               |
| American Express | Parsing information: ARC = `13` (EMV Reply Tag 91, last two bytes) | Device prompts cardholder for online PIN (for ARC `13`). Original authorization request is resubmitted with online PIN. Include this REST API field and value in the request: pointOfSaleInformation.emv.isRepeat=`true`. | `4128.00`               |
| Mastercard       |                                `65`                                |                         Device switches to contact payment interface, when supported. Cardholder is prompted to insert payment card into terminal. If not supported, the transaction is declined.                         | `4065.00`               |
| Mastercard, Relay |                                `70`                                |        Device prompts cardholder for online PIN. Original authorization request is resubmitted with online PIN. Include this REST API field and value in the request: pointOfSaleInformation.emv.isRepeat=`true`.         | `6825.22`               |
| Relay             |                                `1A`                                |                         Device switches to contact payment interface, when supported. Cardholder is prompted to insert payment card into terminal. If not supported, the transaction is declined.                         | `4128.00`               |
[Soft Decline Authorization Response Codes for EU Region]

Retail Payment Services Using EMV and Card Data {#cp-payment-services-intro}
============================================================================

This section describes how to process card-present retail payments using EMV and card data. The payment card must be present for these retail transactions.  
These card-present retail payment services are supported:

* Authorizations:

  * Contact EMV and online PIN. An EMV authorization is based on the EMV chip embedded in the cardholder's payment card.
  * Contact EMV and offline PIN
  * Contactless EMV and online PIN
  * Magnetic stripe swipe. This type of authorization is based on the magnetic stripe on the back of the cardholder's payment card.
  * Hand-keyed data. This type of authorization is based on you manually entering the card information into the payment terminal.
  * Cash advance with credit card
  * Deferred
    {#cp-payment-services-intro_ul_et1_qfl_myb}
* Capture

* Capture for contact EMV authorization

* Credit

* Authorization reversal

* Void

* Timeout void

* Mobile point-of-sale (mPOS) authorizations and sales

* PIN debit services
  {#cp-payment-services-intro_ul_o1b_lfl_myb}  
  For more information about payment services and processing, see these resources:

* [API field reference guide for the REST API](https://developer.example.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

* Github repositories: [Cybersource](https://github.com/Cybersource "")

Retail EMV and Card Data {#cp-emv-card-data}
============================================

You can request these payment services for retail with EMV and card data:

* Authorization: standard and incremental

* Capture

* Credit  
  This table shows which EMV tags are:

* M: mandatory

* P: prohibited

* O: optional

* C: conditional (Send the tag when it is present in card and terminal.)

|                 Data Element                 | EMV Tag |          Mastercard          | Relay |
|----------------------------------------------|---------|------------------------------|------|
| Transaction Date                             | 9A      | M                            | M    |
| Transaction Type                             | 9C      | M                            | M    |
| Transaction Currency Code                    | 5F2A    | M                            | M    |
| Terminal Country Code                        | 9F1A    | M                            | M    |
| Amount Authorized                            | 9F02    | M                            | M    |
| Amount Other                                 | 9F03    | M                            | M    |
| Application PAN Sequence Number              | 5F34    | C                            | O    |
| Application Transaction Counter (ATC)        | 9F36    | M                            | M    |
| Application Interchange Profile (AIP)        | 82      | M                            | M    |
| Dedicated File (DF) Name                     | 84      | M                            | M    |
| Terminal Verification Results (TVR)          | 95      | M                            | M    |
| Issuer Application Data                      | 9F10    | M                            | M    |
| Application Cryptogram                       | 9F26    | M                            | M    |
| Cryptogram Information Data (CID)            | 9F27    | M                            | O    |
| Terminal Capabilities                        | 9F33    | M                            | M    |
| Cardholder Verification Method (CVM) Results | 9F34    | M                            | O    |
| Unpredictable Number (UN)                    | 9F37    | M                            | M    |
| Form Factor Indicator                        | 9F6E    | O (Authorization) P (Refund) | C    |
[EMV Data Elements and Tags]

Authorization with Contact EMV and Online PIN {#cp-emv-contact-onlinepin-auth-intro}
====================================================================================

For an EMV chip contact authorization, the customer inserts the card directly into a point-of-sale (POS) terminal. For an online PIN authorization, the customer enters a PIN to verify their identity, and the issuer verifies the PIN.  
Online PIN transactions are supported by these card types:

* Relay
* Mastercard
* American Express
* Discover

Endpoint {#cp-emv-contact-onlinepin-auth-intro_d7e16}
-----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-emv-contact-onlinepin-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-emv-contact-onlinepin-auth-intro_d7e35}

Required Fields for Processing an Authorization with Contact EMV and Online PIN {#cp-emv-contact-onlinepin-auth-reqfields}
==========================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact` for an EMV payment.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Country-Specific Required Fields for Processing an Authorization with Contact EMV or Contactless PIN {#cp-emv-fields-required-country}
======================================================================================================================================

Argentina
---------

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:
Required when the time zone is not set in your account.

[invoiceDetails.salesSlipNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/invoice-details-aa/invoice-details-sales-slip-num.md "")
:

India
-----

[pointOfSaleInformation.terminalCompliance](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-compliance.md "")
:

Japan
-----

[invoiceDetails.salesSlipNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/invoice-details-aa/invoice-details-sales-slip-num.md "")
:

REST Example: Processing an Authorization with Contact EMV and Online PIN {#cp-emv-contact-onlinepin-auth-ex-rest}
==================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "transactionId": "uniqueValue1",
    "partner": {
      "thirdPartyCertificationNumber": "testTPCN"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    }
  },
  "paymentInformation": {
     "card": {
                "type": "001"
       }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "9900.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contact",
    "terminalCapability": 4,
     "terminalPinCapability": 6,
    "emv": {
      "tags": "5F3401019F3303E0F8C8950580800480009F370465B81A3A9F100706011203A0A0009F2608E9D097D1901E8AB99F36020002820218009C01009F1A0208409A032307259F02060000000007005F2A0208409F0306000000000000DF78083831393931303236DF791B322D30323436362D312D31432D5246492D303331332D342E332E62",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4761xxxxxxxxxxxx=251220111478549?",
    "pinBlockEncodingFormat":0,
    "encryptedPin": "F509429A3C3FD201",
    "encryptedKeySerialNumber": "FFFF1B1D140000200001"
  },
        "merchantInformation": {
             "transactionLocalDateTime": "20230724085022"
       }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/6938891699856080004953/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6938891699856080004953"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6938891699856080004953/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "test123",
    "transactionId": "uniqueValue1"
  },
  "id": "6938891699856080004953",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "9900.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "A",
      "group": "0"
    },
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "188535",
    "approvalCode": "831000",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "324704188535",
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "6938891699856080004953",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-09-05T04:46:10Z"
}
```

Authorization with Contact EMV and Offline PIN {#cp-emv-contact-offlinepin-auth-intro}
======================================================================================

During a contact EMV authorization, the customer inserts the card into the terminal, which causes the EMV chip to be in contact with the terminal. When processing an offline PIN transaction, the EMV chip verifies the customer PIN.

Endpoint {#cp-emv-contact-offlinepin-auth-intro_d7e16}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-emv-contact-offlinepin-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-emv-contact-offlinepin-auth-intro_d7e35}

Required Fields for Processing an Authorization with Contact EMV and Offline PIN {#cp-emv-contact-offlinepin-auth-reqfields}
============================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`. Set the value to `0` if the terminal does not support PINs.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Processing an Authorization with Contact EMV and Offline PIN {#cp-emv-contact-offlinepin-auth-ex-rest}
====================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "transactionId": "uniqueValue2",
    "partner": {
      "thirdPartyCertificationNumber": "testTPCN"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "partialAuthIndicator": "true"
    }
  },
  "paymentInformation": {
     "card": {
                "type": "001"
       }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "9900.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contact",
    "terminalCapability": 4,
     "terminalPinCapability": 6,
    "emv": {
      "tags": "5F3401019F3303E0F8C8950580800480009F370465B81A3A9F100706011203A0A0009F2608E9D097D1901E8AB99F36020002820218009C01009F1A0208409A032307259F02060000000007005F2A0208409F0306000000000000DF78083831393931303236DF791B322D30323436362D312D31432D5246492D303331332D342E332E62",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4761xxxxxxxxxxxx=251220111478549?"
  },
       "merchantInformation": {
             "transactionLocalDateTime": "20230724085022"
    }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/6938894575296498704951/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6938894575296498704951"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6938894575296498704951/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "test123",
    "transactionId": "uniqueValue2"
  },
  "id": "6938894575296498704951",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "9900.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "A",
      "group": "0"
    },
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "188589",
    "approvalCode": "831000",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "324704188589",
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "6938894575296498704951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-09-05T04:50:58Z"
}
```

Authorization with Contactless EMV and Online PIN {#cp-emv-contactless-onlinepin-auth-intro}
============================================================================================

For an EMV contactless payment, the customer taps the card on the terminal. The terminal and chip use near-field communication (NFC) to communicate with each other. For an online PIN transaction, the customer uses a PIN to verify their identity and the issuer verifies the PIN.  
Online PIN transactions are supported by these card types:

* Relay
* Mastercard
* American Express
* Discover

Endpoint {#cp-emv-contactless-onlinepin-auth-intro_d7e16}
---------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-emv-contactless-onlinepin-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-emv-contactless-onlinepin-auth-intro_d7e35}

Required Fields for Processing an Authorization with Contactless EMV and Online PIN {#cp-emv-contactless-onlinepin-auth-reqfields}
==================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless` for an EMV payment.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `5`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Processing an Authorization with Contactless EMV and Online PIN {#cp-emv-contactless-onlinepin-auth-ex-rest}
==========================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "uniqueValue3",
        "partner": {
            "thirdPartyCertificationNumber": "testTPCN"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "authorizationOptions": {
            "partialAuthIndicator": "true"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "entryMode": "contactless",
        "terminalCapability": 4,
        "terminalPinCapability": 6,
        "emv": {
            "tags": "5F3401019F3303E0F8C8950580800480009F370465B81A3A9F100706011203A0A0009F2608E9D097D1901E8AB99F36020002820218009C01009F1A0208409A032307259F02060000000007005F2A0208409F0306000000000000DF78083831393931303236DF791B322D30323436362D312D31432D5246492D303331332D342E332E62",
            "cardSequenceNumber": "01"
        },
        "trackData": ";4761xxxxxxxxxxxx=251220111478549?",
        "pinBlockEncodingFormat":0,
        "encryptedPin": "F509429A3C3FD201",
        "encryptedKeySerialNumber": "FFFF1B1D140000200001"
    },
    "merchantInformation": {
        "transactionLocalDateTime": "20230724085022"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6938904668436727104951/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6938904668436727104951"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6938904668436727104951/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "uniqueValue3"
    },
    "id": "6938904668436727104951",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "188851",
        "approvalCode": "831000",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "324705188851",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "6938904668436727104951",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-09-05T05:07:47Z"
}
```

Authorization with Magnetic Stripe Swipe {#cp-services-auth-mag-intro}
======================================================================

Although EMV chips on payment cards have become common, sometimes the EMV chip cannot be used to validate the cardholder. In these instances, you can choose to validate the cardholder by using the magnetic stripe on back of the payment card.

Endpoint {#cp-services-auth-mag-intro_d7e16}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mag-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mag-intro_d7e35}

Required Fields for Processing an Authorization with Swiped Track Data {#cp-services-auth-mag-reqfields}
========================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Processing an Authorization with Swiped Track Data {#cp-services-auth-mag-ex-json-rest}
=====================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "ABC123",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
        }
    },
    "pointOfSaleInformation": {
        "trackData": ";4111xxxxxxxxxxxx=231220112345678?",
        "entryMode": "swiped",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9601.00",
            "currency": "USD"
        }
    },
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6869553167546562203955/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6869553167546562203955"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6869553167546562203955/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "ABC123"
    },
    "id": "6869553167546562203955",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9601.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111"
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "63427009RIT9HBR9",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-16T22:41:57Z"
}
```

Authorizations with Hand-Keyed Data {#cp-services-auth-key-intro}
=================================================================

To obtain an authorization when the payment terminal cannot capture the card data electronically through other entry modes, hand key or manually enter the customer's card data in your POS system.

Endpoint {#cp-services-auth-key-intro_d7e16}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-key-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-key-intro_d7e35}

Required Fields for Processing an Authorization with Hand-Keyed Data {#cp-services-auth-key-reqfields}
======================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:
> IMPORTANT  
> This field is optional if your account is configured for relaxed requirements for expiration date. For details about relaxed requirements, see the support article [Relaxed Requirements for Address Data and Expiration Date in Credit Card Transactions](ç "") .

[paymentInformation.card.expirationyear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[pointOfSaleInformation.cardPresent](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-card-present.md "")
:
Set the value to `true`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `keyed`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `1`, `2`, `3`, `4`, or `5`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Authorization with Hand Keyed Data {#cp-services-auth-key-ex-rest}
================================================================================

Request

```
{    
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445679",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "authorizationOptions": {
            "ignoreAvsResult": "true",
            "ignoreCvResult": "true"
        }
    },
    "pointOfSaleInformation": {
        "entryMode": "keyed",
        "terminalCapability": "4",
        "terminalPinCapability": "6"
    },
    "paymentInformation": {
        "card": {
            "number": "4111111111111111",
            "securityCode": "123",
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9604.00",
            "currency": "USD"
        },
        "billTo": {
            "postalCode": "94538"
        }
    }
    "merchantInformation": { 
        "transactionLocalDateTime": "20230724085022" 
    }
}
```

Response to a Successful Request  
A successful response returns `status=AUTHORIZED`.

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6080032225246314603005/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6080032225246314603005"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6080032225246314603005",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9604.00",
            "authorizedAmount": "9604.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "173156",
        "approvalCode": "831000",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "networkTransactionId": "016153570198200",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
             "code": "Z",
             "codeRaw": "Z"
        }
    },
    "reconciliationId": "6080032225246314603005",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2020-12-15T03:33:42Z"
    }
```

Authorization for Cash Advance with Credit Card {#cp-services-auth-cash-adv-intro}
==================================================================================

Using the cash advance feature, a cardholder can withdraw cash against their credit card account limit at their bank. The cardholder presents their credit card and identification to bank staff or uses the bank's card terminal to complete this transaction. IMPORTANT The cash advance with credit card at ATM option is not supported currently.  
These card types support cash advance with credit card transactions in the U.S:

* Discover. The minimum transaction amount is 10.00 USD.
* Mastercard
* Relay
  {#cp-services-auth-cash-adv-intro_ul_kmt_yqq_42c}

Fields Specific to This Use Case
--------------------------------

[processingInformation.authorizationOptions.cashAdvanceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-cash-advance-ind.md "")
:
Set the value to `true`.

[merchantInformation.categoryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-category-code-a.md "")
:
Set the value to `6010`. This field is not required if merchant category code `6010` is configured in the merchant account. If sent, this field overrides the value in the merchant account.

Endpoint {#cp-services-auth-cash-adv-intro_d7e16}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-cash-adv-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-cash-adv-intro_d7e35}

Required Fields for Authorization for Cash Advance with Credit Card {#cp-services-auth-cash-adv-req-fields}
===========================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.categoryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-category-code-a.md "")
:
Set the value to `6010`. This field is not required when merchant category code `6010` is configured in the merchant account. If sent, this field overrides the value in the merchant account.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.cashAdvanceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-cash-advance-ind.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Authorization for Cash Advance with Credit Card {#cp-services-auth-cash-adv-ex-rest}
==================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "Cash Advance",
        "transactionId": "uniqueValue1",
        "partner": {
            "thirdPartyCertificationNumber": "testTPCN"
        }
    },
    "processingInformation": {
        "authorizationOptions": {
            "cashAdvanceIndicator": "true"
        },
        "commerceIndicator": "retail"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "entryMode": "contact",
        "terminalCapability": 4,
        "terminalPinCapability": 6,
        "emv": {
            "tags": "5F3401019F3303E0F8C8950580800480009F370465B81A3A9F100706011203A0A0009F2608E9D097D1901E8AB99F36020002820218009C01009F1A0208409A032307259F02060000000007005F2A0208409F0306000000000000DF78083831393931303236DF791B322D30323436362D312D31432D5246492D303331332D342E332E62",
            "cardSequenceNumber": "01"
        },
        "trackData": ";4761xxxxxxxxxxxx=251220111478549?",
        "pinBlockEncodingFormat":0,
        "encryptedPin": "F509429A3C3FD201",
        "encryptedKeySerialNumber": "FFFF1B1D140000200001"
    },
    "merchantInformation": {
        "transactionLocalDateTime": "20230724085022"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6938891699856080004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6938891699856080004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6938891699856080004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "uniqueValue1"
    },
    "id": "6938891699856080004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "188535",
        "approvalCode": "831000",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "324704188535",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "6938891699856080004953",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-09-05T04:46:10Z"
}
```

Deferred Authorization {#cp-services-deferred-auth-intro}
=========================================================

Use this information to process a deferred authorization. This payment service enables you to process a delayed authorization request when real-time submission of the request is not possible due to connectivity issues, system outages, or other limitations.  
Review these requirements for a deferred authorization transaction:

* Include this field in the authorization or sale request: processingInformation.authorizationOptions.deferredAuthIndicator.
* Submit the authorization request within 24 hours of the original transaction date. This requirement applies to non-transit industries.
  {#cp-services-deferred-auth-intro_ul_qxd_y2n_whc}

Supported Card Types
--------------------

These card types support deferred authorizations:

* Mastercard
* Relay
  {#cp-services-deferred-auth-intro_ul_rzx_5v4_whc}

Fields Specific to This Use Case
--------------------------------

This field is required for this use case:

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/vas/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set the value to `true`.

Endpoint {#cp-services-deferred-auth-intro_d7e16}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-deferred-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-deferred-auth-intro_d7e35}

Required Fields for Deferred Authorization {#cp-services-deferred-auth-api-reqfields}
=====================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
A value is required for contact or contactless entry modes.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:
A value is required for contact or contactless entry modes.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/vas/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set the value to `true`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true` when sale transactions are supported.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Deferred Authorization {#cp-services-deferred-auth-api-ex-rest}
=============================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "uniqueValue123",
        "partner": {
            "thirdPartyCertificationNumber": "testTPCN"
        }
    },
    "processingInformation": {
        "capture": true,
        "commerceIndicator": "retail",
        "authorizationOptions": {
            "deferredAuthIndicator": true
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "entryMode": "contact",
        "terminalCapability": "4",
        "terminalPinCapability": "6",
        "emv": {
            "tags": "9F100706011103A000009F26089302EDF8DC3C6E519F02060000000011009F03060000000000009F1A020840950500000000005F2A0208409A031807039C01009F37043444BDD7820200009F360200019F330360B0E89F1E04123456789F2701809F6E04207000009F7C140000000000000000000000000000000000000000",
            "cardSequenceNumber": "01"
        },
        "trackData": ";4761739001010135=28122011758928889?"
    },
    "merchantInformation": {
        "transactionLocalDateTime": "20251110115959"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7686002727826702603813/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7686002727826702603813"
        }
    },
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "uniqueValue123"
    },
    "id": "7686002727826702603813",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "401178",
        "merchantNumber": "123456789012",
        "approvalCode": "831000",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "601621401178",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "7686002727826702603813",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2026-01-16T21:51:13Z"
}
```

Authorization Reversal {#payments-processing-basic-auth-reversal-intro}
=======================================================================

This section provides the information about how to process an authorization reversal.  
Reversing an authorization releases the hold on the customer's payment card funds that the issuing bank placed when processing the authorization.  
For a debit card or prepaid card in which only a partial amount was approved, the amount of the reversal must be the amount that was authorized, not the amount that was requested.
All supported card types can process authorization reversals.

Endpoint {#payments-processing-basic-auth-reversal-intro_d19e85}
----------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#payments-processing-basic-auth-reversal-intro_d19e94}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#payments-processing-basic-auth-reversal-intro_d19e107}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for Processing an Authorization Reversal {#payments-processing-basic-auth-reversal-required-fields}
===================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[reversalInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-currency.md "")
:

[reversalInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-total-amount.md "")
:
The amount of the reversal must be the same as the authorization amount that was included in the authorization response message. Do not use the amount that was requested in the authorization request message.

REST Example: Processing an Authorization Reversal {#payments-processing-basic-auth-reversal-ex-rest}
=====================================================================================================

Request

```
{ 
    "clientReferenceInformation": { 
      "code": "test123"
    } 
    "reversalInformation" : { 
        "amountDetails" : { 
            "totalAmount" : "100.00",
            "currency" : "USD"
        } 
    } 
}
```

Response to a Successful Request

```
{
    "_links" : {
      "self" : {
          "method" : "GET",
          "href" : "/pts/v2/reversals/6869460219566537303955"
      }
    },
    "clientReferenceInformation" : {
        "code" : "RTS-Auth-Reversal"
    },
    "id" : "6869460219566537303955",
    "orderInformation" : {
        "amountDetails" : {
            "currency" : "USD"
        }
    },
    "processorInformation" : {
        "responseCode" : "200"
    },
    "reconciliationId" : "82kBK3qDNtls",
    "reversalAmountDetails" : {
        "reversedAmount" : "100.00",
        "currency" : "USD"
    },
    "status" : "REVERSED",
    "submitTimeUtc" : "2023-06-16T20:07:02Z"
}
```

Capture {#payments-processing-basic-capture-intro}
==================================================

This section describes how to capture an authorized transaction.
All supported card types can process captures.

Endpoint {#payments-processing-basic-capture-intro_d19e127}
-----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#payments-processing-basic-capture-intro_d19e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#payments-processing-basic-capture-intro_d19e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for Capturing an Authorization {#payments-processing-basic-capture-required-fields}
===================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
This field value maps from the original authorization, sale, or credit transaction.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

REST Example: Capturing an Authorization {#payments-processing-basic-capture-ex-rest}
=====================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "ABC123"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "EUR"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/captures/6662994431376681303954/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/captures/6662994431376681303954"
        }
    },
    "clientReferenceInformation": {
        "code": "1666299443215"
    },
    "id": "6662994431376681303954",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "EUR"
        }
    },
    "reconciliationId": "66535942B9CGT52U",
    "status": "PENDING",
    "submitTimeUtc": "2022-10-20T20:57:23Z"
}
```

Capture for Contact EMV Authorization {#cp-services-capture-contact-emv-auth-intro}
===================================================================================

To capture a contact EMV authorization, you must include additional information in your capture request. Include these EMV tags from the data on the EMV chip:

* `95`: Terminal verification results
* `9F10`: Issuer application data
* `9F26`: Application cryptogram  
  For information about capturing a contactless EMV authorization, see [Capture](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/cp-payment-services-intro/payments-processing-basic-capture-intro.md "").

Endpoint {#cp-services-capture-contact-emv-auth-intro_d7e127}
-------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#cp-services-capture-contact-emv-auth-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#cp-services-capture-contact-emv-auth-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for Capturing a Contact EMV Authorization {#cp-services-capture-contact-emv-auth-required-fields}
=================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Field value maps from the original authorization, sale, or credit transaction.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info_/order-info-amount-details-currency.md "")

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info_/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:
Include this data:

    * 95: Terminal verification results
    * 9F10: Issuer application data
    * 9F26: Application cryptogram

REST Example: Capturing a Contact EMV Authorization {#cp-services-capture-contact-emv-auth-ex-rest}
===================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
F2A0208409F0306000000000000"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links" : {
        "void" : {
            "method" : "POST",
             "href" : "/pts/v2/captures/6512628085536163703211/voids"
        },
        "self" : {
            "method" : "GET",
            "href" : "/pts/v2/captures/6512628085536163703211"
        }
    },
    "clientReferenceInformation" : {
        "code" : "1651262808531"
    },
    "id" : "6512628085536163703211",
    "orderInformation" : {
        "amountDetails" : {
            "totalAmount" : "100.00",
            "currency" : "USD"
        }
    },
    "reconciliationId" : "6512627267816161803211",
    "status" : "PENDING",
    "submitTimeUtc" : "2022-04-29T20:06:49Z"
}
```

Stand-Alone Credit {#cp-services-standalone-credit-intro}
=========================================================

This section describes how to process a stand-alone credit. A stand-alone credit is used to process a credit with no reference to a previous transaction. The amount for a stand-alone credit is not limited because there is no reference to an original transaction amount. The customer is required to present their payment card for this type of credit.

Endpoint {#cp-services-standalone-credit-intro_d7e169}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#cp-services-standalone-credit-intro_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#cp-services-standalone-credit-intro_d7e188}

Required Fields for Processing a Stand-Alone Credit {#cp-services-standalone-credit-required-fields}
====================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
{#cp-services-standalone-credit-required-fields_dl_vbd_yfw_1yb}

REST Example: Stand-Alone Credit {#cp-services-standalone-credit-ex-rest}
=========================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test123",
        "transactionId": "11223344",
        "partner": {
            "thirdPartyCertificationNumber": "testTPCN"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "87654321",
        "entryMode": "contactless",
        "terminalCapability": "4",
        "terminalPinCapability": "0",
        "emv": {
            "tags": 
"5F2A02084082025800950542800480009A032907259C01209F02060000009900009F10070601120
3A000009F1A0208409F1E08364B3335303633379F26084F674AF82F5566BD9F330360F0E89F36022
3019F370479E0A7B59F2701809F34030203005F340101",
            "cardSequenceNumber": "01"
        },
        "trackData": ";4761739001010119=29122011758928889?"
    },
    "merchantInformation": {
      "transactionLocalDateTime": "20230724085022"
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/credits/6663069906146706403954/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/credits/6663069906146706403954"
        }
    },
    "clientReferenceInformation": {
        "code": "1666306990717"
    },
    "creditAmountDetails": {
        "currency": "eur",
        "creditAmount": "100.00"
    },
    "id": "6663069906146706403954",
    "orderInformation": {
        "amountDetails": {
            "currency": "eur"
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
        "approvalCode": "888888",
        "responseCode": "100"
    },
    "reconciliationId": "66490108K9CLFJPN",
    "status": "PENDING",
    "submitTimeUtc": "2022-10-20T23:03:10Z"
}
```

Void for a Capture or Credit {#payments-processing-basic-void-intro}
====================================================================

This section describes how to void a capture or credit that was submitted but not yet processed by the processor.

Endpoints {#payments-processing-basic-void-intro_d19e268}
---------------------------------------------------------

**Void a Capture**  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/captures/`*{id}*`/voids`{#payments-processing-basic-void-intro_d19e281}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/captures/`*{id}*`/voids`{#payments-processing-basic-void-intro_d19e294}  
**Void a Credit**  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`*{id}*`/voids`{#payments-processing-basic-void-intro_d19e311}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`*{id}*`/voids`{#payments-processing-basic-void-intro_d19e325}  
The *{id}* is the transaction ID returned during the capture or credit response.

Required Fields for Voiding a Capture or Credit {#payments-processing-basic-void-required-fields}
=================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Including this field is recommended, but not required.

REST Example: Voiding a Capture or Credit {#payments-processing-basic-void-ex-rest}
===================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test123"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/voids/6541933390746728203005"
        }
    },
    "clientReferenceInformation": {
        "code": "1654193339056"
    },
    "id": "6541933390746728203005",
    "orderInformation": {
        "amountDetails": {
        "currency": "USD"
        }
    },
    "status": "VOIDED",
    "submitTimeUtc": "2022-06-02T18:08:59Z",
    "voidAmountDetails": {
        "currency": "usd",
        "voidAmount": "100.00"
    }
}
```

Timeout Void for a Capture, Sale, Refund, or Credit {#cp-timeout-void-intro}
============================================================================

When you do not receive a response message after sending a capture, sale, refund, or credit request, this feature enables you to void the transaction that you requested.  
Include the clientReferenceInformation.transactionId field in the original request for a capture, sale, refund, or credit. The value of the merchant transaction ID must be unique for 60 days.  
When the original transaction fails, the response message for the void request includes these fields:

* voidAmountDetails.originalTransactionAmount
* processorInformation.responseCode

Endpoint {#cp-timeout-void-intro_d7e585}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/voids/`{#cp-timeout-void-intro_d7e594}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/voids/`{#cp-timeout-void-intro_d7e604}

Required Fields for Processing a Timeout Void for a Capture, Sale, Refund, or Credit {#cp-timeout-void-required-fields}
=======================================================================================================================

Use the value from this field to request a timeout void :

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:
Identifier that links the void request to the original request.

REST Example: Processing a Timeout Void for a Capture, Sale, Refund, or Credit {#cp-timeout-void-ex-rest-ctv}
=============================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "transactionId": "987654321"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "method": "GET",
        "href": "/pts/v2/voids/6541933390746728203005"
    }
  },
  "clientReferenceInformation": {
    "code": "1654193339056"
  },
  "id": "6541933390746728203005",
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    }
  },
  "status": "VOIDED",
  "submitTimeUtc": "2023-06-02T18:08:59Z",
  "voidAmountDetails": {
    "currency": "usd",
    "voidAmount": "100.00"
  }
}
```

Introduction to PIN Debit Processing {#cp-pd-pin-debit-intro}
=============================================================

Customers commonly use debit cards, also called *ATM cards* or *check cards*, in card-present situations. Your agreement with the debit networks determines whether the customer must provide a personal identification number (PIN).  
`Cybersource` supports PIN debit transactions on `Platform Connect`. PIN debit transactions are supported only in the U.S.  
Debit cards are branded with debit network logos, such as STAR, NYCE, Accel, and Pulse, and often with Relay or Mastercard logos. The logos indicate that the cards are accepted wherever Relay or Mastercard are accepted and are processed through a debit or credit card network.
IMPORTANT Issuer regulations require that you present the customer with the choice to use their debit card as a debit or credit card.  
The customer chooses whether to process the card as a debit card or a credit card. In either case, the money is taken out of the customer's bank account, and the transaction is included on the customer's bank account statement. The customer does not receive a credit card bill as they would with a regular credit card.

PIN Debit Integration {#cp-pd-integrating}
==========================================

Follow these steps to integrate PIN debit processing:

1. Contact `Cybersource` or your acquirer to determine whether you are eligible to process PIN debit transactions. As part of this process, the debit networks might require you to complete applications.
2. Determine whether `Cybersource` or your acquirer requires any additional banking information from you.
3. Determine whether you must comply with any special debit network requirements when processing PIN debit transactions. For example, some networks require that you verify the customer's identity before processing the payment.
4. Contact customer support so that your `Cybersource` account can be configured for PIN debit transactions.

PIN Debit Transactions {#pd-processing-flow}
============================================

PIN debit transactions begin when the customer presents a PIN debit card at the payment terminal.

#### Figure:

PIN Debit Transaction Flow  
![Diagram of the PIN Debit transaction flow.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/card-present/images/pin-debit-infographic.svg/jcr:content/renditions/original)

1. The customer swipes the card through a magnetic card reader, inserts the card into the EMV terminal (contact), or taps the card against an EMV scanner (contactless) on the terminal.
2. The customer chooses to process the card as a debit card or a credit card. IMPORTANT Issuer regulations require that you present the customer with the choice to use their debit card as a debit or credit card.
3. If the customer chooses the debit card option, you request the PIN debit purchase service. The transaction is routed through the debit card networks.  
   PIN debit transactions are *full-financial transactions*; they are single message transactions that include an authorization and capture. As such, you do not need to request a separate capture as you would with a credit card transaction.  
   If the PIN debit purchase service fails, you can attempt to process the card as a credit card.
4. If the customer chooses the credit card option, or if the card cannot be used for a PIN debit purchase, process the transaction as a credit card sale, requesting the authorization and capture services together. The transaction is routed through the credit card networks.  
   Refer to the *Payments Developer Guide for the REST API \| Platform Connect* for information about using credit card services to process debit card transactions.
5. If you need to refund a PIN debit purchase, use the PIN debit credit service.
6. To reverse a PIN debit purchase or PIN debit credit, use the PIN debit reversal service. IMPORTANT To request a PIN debit reversal, you must submit the request within one hour of the request that you are reversing.

PIN Debit Network Routing {#pd-network-routing-intro}
=====================================================

Listing your preferred network routing codes in your `Business Center` merchant account is an optional setting. To ensure that transactions are routed to networks in your priority order, `Cybersource` recommends including the processingInformation.networkRoutingOrder field in PIN debit requests. Set the value to the priority order of the routing networks for the transaction. When you include this field it overrides your merchant account setting. When you do not include this field in your request, `Cybersource` uses the list of network codes in your merchant account.  
For Electronic Benefit Transfer (EBT) transactions, set the processingInformation.networkRoutingOrder field to `K`. If you do not include this field in EBT requests, your merchant account must be configured with `K` in the first priority order for network routing.

PIN Debit Processing Versus Credit Card Processing {#pd-vs-cc-processing}
=========================================================================

You can process Relay or Mastercard branded debit cards through the credit card network by using the credit card authorization and capture services, which is the same way that you process credit card transactions.  
PIN debit transactions and credit card transactions are processed differently from each other:

* For a PIN debit transaction, request only the authorization service. You are not required to request a capture because the authorization service authorizes the transaction and moves the money.
* For a credit card transaction, you receive an authorization code indicating an approval. For a PIN debit transaction, you do not necessarily receive an authorization code. Some processors provide an authorization code, but the code is not required in order for you to receive your money. For a PIN debit transaction, you cannot verbally obtain an authorization code from the processor or bank.

PIN Debit Reconciliation {#pd-recon}
====================================

PIN debit purchase and credit data is added to the TC33A capture file for reconciliation purposes only. Use it to verify this information:

* Merchant ID (MID)
* Total amount
* Approved: yes or no
* Action code

Track Data {#pd-feature-track-data-intro}
=========================================

PIN debit processing uses track 2 data in purchase and credit requests. When you include track data in a request using the pointOfSaleInformation.trackData field, the sentinels are required.  
In this example, the track 2 data follows the semicolon (;). The most important parts of the track data are the card number, card expiration year, and card expiration month. In this example, the card number is 4111111111111111, the expiration year is 26, and the expiration month is 12. The end sentinel (?) follows the final character of data recorded on the track.
Track Data Example

```
;4111111111111111=26121019761186800000?
```

Terminal IDs {#pd-terminal-id}
==============================

By default, your merchant account is configured to validate a default terminal ID (TID). If you want to override the default TID and send TIDs in the pointOfSaleInformation.terminalId request field in PIN Debit requests, contact customer support to configure your account to disable TID validation.

Electronic Benefit Transfer {#pd-feature-ebt-intro}
===================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible people. EBT cards function like prepaid debit cards that can be used at authorized retailers. Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps people with low incomes purchase eligible food items.  
This feature enables you to submit purchase, credit, and reversal requests on EBT cards and vouchers. For EBT transactions, only swiped and manually keyed entry are supported. Contactless EMV transactions are not supported.
IMPORTANT Federal law mandates that you cannot deny an EBT transaction because of technical problems such as a non-working terminal or a non-working PIN pad.  
When a technical problem prevents you from initiating an EBT transaction, follow these steps:

1. Complete an EBT voucher transaction, which is similar to a verbal authorization.
2. Telephone the issuer to receive the approval information verbally.
3. Capture all of the approval information on one of the paper vouchers that you received with the EBT network device.
4. When the EBT system is back online, enter the voucher information into the EBT device to complete the transaction.

PIN Debit Optional Features {#pd-feature-intro}
===============================================

This section describes the optional features that are available for PIN Debit processing.

Cash Back {#pd-feature-cash-back-intro}
=======================================

This feature enables a customer in a card-present situation to add a cash-back amount to the total transaction amount when using a debit card. The customer receives that amount in cash along with the purchase. For example, a customer purchasing products totaling 18.99 might ask for 20.00 cash back. They would pay a total of 38.99 (18.99 + 20.00) with their debit card and receive 20.00 in cash along with their products.
IMPORTANT Cash back is not supported on partial authorizations.  
To use this feature, include the orderInformation.amountDetails.cashbackAmount field in a PIN debit purchase request.  
When the cash-back amount is 0.00, do not include the orderInformation.amountDetails.cashbackAmount field.  
For more information, see [PIN Debit Purchase with Contactless EMV and Cash Back](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-cash-back-cntctlss-task.md "").

Merchant Descriptors {#pd-feature-merchdescr-intro}
===================================================

This feature enables you to submit merchant descriptor values that are displayed on a cardholder's statement.
IMPORTANT Before using merchant descriptors in your requests, check with your bank to learn whether you must pre-register your merchant descriptor information with them.  
`Cybersource` always provides merchant descriptor information to the acquirer for all of your PIN debit purchase and PIN debit credit transactions. When you do not include a particular merchant descriptor in your PIN debit purchase or PIN debit credit request, `Cybersource` uses the corresponding value from your merchant account.  
For more information, see [PIN Debit Purchase with Swiped Track Data and Merchant Descriptors](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-purch-swipe-merchdescr-task.md "").

Merchant Descriptor Fields
--------------------------

You can include these merchant descriptor fields in a PIN debit purchase or PIN debit credit:

merchantInformation.merchantDescriptor.administrativeArea
:
If you include this field in a request, you must also include merchantInformation.merchantDescriptor.country.

merchantInformation.merchantDescriptor.alternateName
:

merchantInformation.merchantDescriptor.country
:
If you include this field in a request, you must also include merchantInformation.merchantDescriptor.administrativeArea.

merchantInformation.merchantDescriptor.locality
:

merchantInformation.merchantDescriptor.name
:

merchantInformation.merchantDescriptor.postalCode
:

Merchant-Inititated Reversals {#pd-feature-mit-reversal-intro}
==============================================================

When you do not receive a response message after sending a PIN debit purchase or credit request, your request might have timed out. This feature enables you to reverse a timed-out transaction within 2 hours of the original request.  
When using the merchant-initiated reversals feature, include the clientReferenceInformation.transactionId field in your original request for a PIN debit purchase. The value of the transaction ID must be unique for 60 days. It links your reversal request to your original request.

Partial Authorizations {#pd-feature-partial-auth-intro}
=======================================================

For PIN debit cards, the issuing bank can approve a partial amount if the balance on the card is less than the requested authorization amount.  
Support for your processor and card type does not guarantee a partial authorization. The issuing bank decides whether or not to approve a partial amount. When the balance on a debit card or prepaid card is less than the requested authorization amount, the issuing bank can approve a partial amount. When this happens, you can accept multiple forms of payment for the order starting with some or all of the approved amount, followed by one or more different payment methods.  
You must opt in to be able to receive and capture partial authorizations. Choose one of these options:

* Call `Cybersource` customer support to have your merchant account enabled for partial authorizations. When you do this, all of your authorization requests are enabled for partial authorizations.


* Set the processingInformation.authorizationOptions.partialAuthIndicator field to `true` in a PIN debit purchase request. When you do this, only that specific transaction is enabled for partial authorization.

When your account is enabled for partial authorizations, you can disable partial authorization for a specific transaction by setting the processingInformation.authorizationOptions.partialAuthIndicator field to `false` in the PIN debit purchase request.  
For more information, see [PIN Debit Partial Authorization with Swiped Track Data](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-purch-swipe-partial-task.md "").

Payment Network Tokens {#pd-feature-pnt-intro}
==============================================

Payment network tokens are supported as card-present contactless transactions.

Surcharge Fees {#pd-feature-surcharge-intro}
============================================

This feature enables you to charge the customer a surcharge fee for a PIN debit purchase or credit transaction.
IMPORTANT Surcharge fees are not allowed on debit or prepaid cards in the U.S.  
Include the surcharge amount in the total transaction amount, and set the orderInformation.amountDetails.surcharge.amount field to the surcharge amount. This information is passed to the issuer and acquirer for tracking. The issuer can provide information about the surcharge amount to the customer.  
When there is no surcharge fee, do not include the orderInformation.amountDetails.surcharge.amount field in the request.  
For more information, see [PIN Debit Purchase with Contactless EMV and a Surcharge Fee](/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail/pd-processing/pd-cntctlss-purch-srchrg-task.md "").

PIN Debit Services {#pd-processing}
===================================

This section describes how to process PIN debit transactions that use these services:

* Contactless EMV purchases
* Swiped purchases
* Cash back
* Credits
* Electronic Benefits Transfer (EBT) transactions:
  * EBT cash benefit account purchases
  * EBT Supplemental Nutrition Assistance Program (SNAP) account purchases
  * EBT voucher purchases
  * EBT purchases with cash back
  * EBT credits
  * EBT reversals
* Merchant-initiated reversals
* Partial authorizations

PIN Debit Purchase with Contactless EMV {#pd-cntctlss-purch-task}
=================================================================

This section describes how to process a PIN debit purchase with contactless EMV when the customer taps the card on the terminal.

Endpoint {#pd-cntctlss-purch-task_d7e16}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-cntctlss-purch-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-cntctlss-purch-task_d7e35}

Required Fields for a PIN Debit Purchase with Contactless EMV {#pd-cntctlss-purch-req-fields}
=============================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Purchase with Contactless EMV {#pd-cntctlss-purch-ex-rest}
==================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "24.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883842752296552503964/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883842752296552503964"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883842752296552503964",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "24.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883842752296552503964"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "109328",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456109328",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883842752296552503964",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T11:37:55Z"
}
```

PIN Debit Purchase with Contact EMV {#pd-contact-purch-task}
============================================================

This section describes how to process a PIN debit purchase with contact EMV when the customer inserts the card into the terminal.

Endpoint {#pd-contact-purch-task_d7e16}
---------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-contact-purch-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-contact-purch-task_d7e35}

Required Fields for a PIN Debit Purchase with Contact EMV {#pd-contact-purch-req-fields}
========================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Purchase with Contact EMV {#pd-contact-purch-ex-rest}
=============================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "VMHF"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "202.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "12345678",
    "entryMode": "contact",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": "0",,
    "encryptedPin": "5D5FA5E5B448F33B",
    "encryptedKeySerialNumber": "FFFF1B1D140000200001"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7012752230096541604951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7012752230096541604951"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "7012752230096541604951",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "202.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "7012752230096541604951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "141924",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456141924",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "7012752230096541604951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-11-29T16:27:03Z"
}
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883842752296552503964/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883842752296552503964"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883842752296552503964",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "24.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883842752296552503964"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "109328",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456109328",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883842752296552503964",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T11:37:55Z"
}
```

PIN Debit Purchase with Contactless EMV and Cash Back {#pd-cash-back-cntctlss-task}
===================================================================================

This section describes how to process a PIN debit purchase with contactless EMV and cash back.

Field Specific to This Use Case
-------------------------------

This API field is specific to this use case:

[orderInformation.amountDetails.cashbackAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-cashback-amount.md "")
:

Endpoint {#pd-cash-back-cntctlss-task_d7e16}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-cash-back-cntctlss-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-cash-back-cntctlss-task_d7e35}

Required Fields for a PIN Debit Purchase with Contactless EMV and Cash Back {#pd-cash-back-cntctlss-req-fields}
===============================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.cashbackAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-cashback-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Purchase with Contactless EMV and Cash Back {#pd-cash-back-cntctlss-ex-rest}
====================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "204.00",
      "currency": "USD",
      "cashbackAmount": "45.00"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883842752296552503955/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883842752296552503955"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883842752296552503955",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "204.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883842752296552503955"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "109328",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456109328",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883842752296552503955",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T11:37:55Z"
}
```

PIN Debit Purchase with Swiped Track Data and Merchant Descriptors {#pd-purch-swipe-merchdescr-task}
====================================================================================================

This section describes how to process a PIN debit purchase with swiped track data and merchant descriptors.

Fields Specific to This Use Case
--------------------------------

These optional API request fields are specific to this use case:

[merchantInformation.merchantDescriptor.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-admin-area.md "")
:

[merchantInformation.merchantDescriptor.alternateName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-alt.md "")
:

[merchantInformation.merchantDescriptor.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:

[merchantInformation.merchantDescriptor.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-locality.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:

Endpoint {#pd-purch-swipe-merchdescr-task_d7e16}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-purch-swipe-merchdescr-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-purch-swipe-merchdescr-task_d7e35}

Required Fields for a PIN Debit Purchase with Swiped Track Data and Merchant Descriptors {#pd-purch-swipe-merchdescr-req-fields}
================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Purchase with Swiped Track Data and Merchant Descriptors {#pd-purch-swipe-merchdescr-ex-rest}
=====================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234", 
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "202.00",
      "currency": "USD"
    }
  },
  "merchantInformation": {
    "merchantDescriptor": {
      "name": "John Smith",
      "alternateName": "ABC Limited",
      "locality": "Austin",
      "country": "United States",
      "administrativeArea": "AL"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "trackData": "%B4111111111111111^JONES/JONES ^3312101976110000868000000?;4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883842752296552503995/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883842752296552503995"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883842752296552503995",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "24.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883842752296552503995"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "109328",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456109328",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883842752296552503995",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T11:37:55Z"
}
```

PIN Debit Partial Authorization with Swiped Track Data {#pd-purch-swipe-partial-task}
=====================================================================================

This section describes how to process a PIN debit partial authorization with swiped track data.

Fields Specific to This Use Case
--------------------------------

This API request field is specific to this use case:

[processingInformation.authorizationOptions.partialAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-partial-auth-ind.md "")
:
Set the value to `true`.

Endpoint {#pd-purch-swipe-partial-task_d7e16}
---------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-purch-swipe-partial-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-purch-swipe-partial-task_d7e35}

Required Fields for a Swiped PIN Debit Partial Authorization {#pd-purch-swipe-partial-req-fields}
=================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.partialAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-partial-auth-ind.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Partial Authorization with Swiped Track Data {#pd-purch-swipe-partial-ex-rest}
======================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234", 
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV",
    "authorizationOptions": {
      "partialAuthIndicator": "true"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "202.00",
      "currency": "USD"
    }
  },
  "merchantInformation": {
    "merchantDescriptor": {
      "name": "John Smith",
      "alternateName": "ABC Limited",
      "locality": "Austin",
      "country": "United States",
      "administrativeArea": "AL"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": "4",
    "trackData": "%B4111111111111111^JONES/JONES ^3312101976110000868000000?;4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6886788570426450204953/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6886788570426450204953"
    }
  },
  "clientReferenceInformation": {
    "code": "Pin Debit Purchase Using Swiped Track Data"
  },
  "id": "6886788570426450204953",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "150.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6886788570426450204953"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "111888",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456111888",
    "transactionId": "000000000000000",
    "responseCode": "10"
  },
  "reconciliationId": "6886788570426450204953",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-06T21:27:37Z"
}
```

PIN Debit Purchase with Contactless EMV and a Surcharge Fee {#pd-cntctlss-purch-srchrg-task}
============================================================================================

This section describes how to process a EMV PIN debit purchase with contactless EMV and a surcharge fee.

Field Specific to This Use Case
-------------------------------

This API request field is specific to this use case:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

Endpoint {#pd-cntctlss-purch-srchrg-task_d7e16}
-----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-cntctlss-purch-srchrg-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-cntctlss-purch-srchrg-task_d7e35}

Required Fields for a PIN Debit Purchase with Contactless EMV and a Surcharge Fee {#pd-cntctlss-purch-srchrg-req-fields}
========================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.surcharge.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-surcharge-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Purchase with Contactless EMV and a Surcharge Fee {#pd-cntctlss-purch-srchrg-ex-rest}
=============================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
    },
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "24.00",
      "currency": "USD",
      "surcharge": {
        "amount": "-20.00" 
      }
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883842752296552503964/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883842752296552503964"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883842752296552503964",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "24.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883842752296552503964"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "109328",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456109328",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883842752296552503964",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T11:37:55Z"
}
```

PIN Debit Balance Inquiry with Contactless EMV {#pd-bal-inq-cntctlss-task}
==========================================================================

This section describes how to process a PIN debit balance inquiry with contactless EMV.

Fields Specific to This Use Case
--------------------------------

This API request field and value is specific to this use case:

processingInformation.authorizationOptions.balanceInquiry
:
Set the value to `true`.  
These API response fields are returned in this use case:

paymentInformation.accountFeatures.accountType
:

paymentInformation.accountFeatures.balanceAmount
:

paymentInformation.accountFeatures.balanceAmountType
:

paymentInformation.accountFeatures.balanceSign
:

paymentInformation.accountFeatures.currency
:

Endpoint {#pd-bal-inq-cntctlss-task_d7e16}
------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-bal-inq-cntctlss-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-bal-inq-cntctlss-task_d7e35}

Required Fields for a PIN Debit Balance Inquiry with Contactless EMV {#pd-bal-inq-cntctlss-req-fields}
======================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set the value to `0.00`.

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.balanceInquiry](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-balance-inquiry.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Balance Inquiry with Contactless EMV {#pd-bal-inq-cntctlss-ex-rest}
===========================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "balanceInquiry": "true"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20200323103021"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "0.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6898513109826580904004/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6898513109826580904004"
    }
  },
  "clientReferenceInformation": {
  "code": "ABC123" 
  },
  "id": "6898513109826580904004",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "0.00",
      "currency": "usd"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "balances": [
        {
          "amountType": "02",
          "amount": "+20.00",
          "accountType": "00",
          "currency": "usd"
        }
      ]
    }
  }
},
  "processingInformation": {
    "reconciliationId": "6898513109826580904004"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "191877",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456191877",
    "transactionId": "016153570198200",
    "responseCode": "00"
  },
  "reconciliationId": "6898513109826580904004",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-20T11:08:31Z"
}
```

PIN Debit Balance Inquiry with Swiped Track Data {#pd-bal-inq-swipe-task}
=========================================================================

This section describes how to process a PIN debit balance inquiry with swiped track data.

Fields Specific to This Use Case
--------------------------------

This API request field and value is specific to this use case:

processingInformation.authorizationOptions.balanceInquiry
:
Set the value to `true`.  
These API response fields are returned in this use case:

paymentInformation.accountFeatures.accountType
:

paymentInformation.accountFeatures.balanceAmount
:

paymentInformation.accountFeatures.balanceAmountType
:

paymentInformation.accountFeatures.balanceSign
:

paymentInformation.accountFeatures.currency
:

Endpoint {#pd-bal-inq-swipe-task_d7e16}
---------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-bal-inq-swipe-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-bal-inq-swipe-task_d7e35}

Required Fields for a PIN Debit Balance Inquiry with Swiped Track Data {#pd-bal-inq-swipe-req-fields}
=====================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.merchantDescriptor.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-postalcode.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set the value to `0.00`.

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.balanceInquiry](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-balance-inquiry.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Balance Inquiry with Swiped Track Data {#pd-bal-inq-swipe-ex-rest}
==========================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "balanceInquiry": "true"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20200323103021"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "0.00",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005",
    "trackData": "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6879489725216492803092/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6879489725216492803092"
    }
  },
  "clientReferenceInformation": {
    "code": "987654321" 
  },
  "id": "6879489725216492803092",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "0.00",
      "currency": "usd"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "balances": [
        {
          "amountType": "02",
          "amount": "+20.00",
          "accountType": "00",
          "currency": "usd"
        }
      ]
    }
  }
},
  "processingInformation": {
    "reconciliationId": "6879489725216492803092"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "837760",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456837760",
    "transactionId": "016153570198200",
    "responseCode": "00"
  },
  "reconciliationId": "6879489725216492803092",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-06-28T10:42:52Z"
}
```

PIN Debit Credit with Swiped Track Data {#pd-credit-swipe-task}
===============================================================

This section describes how to process a PIN debit credit with swiped track data.

Endpoint {#pd-credit-swipe-task_d7e169}
---------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#pd-credit-swipe-task_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#pd-credit-swipe-task_d7e188}

Required Fields for a PIN Debit Credit with Swiped Track Data {#pd-credit-swipe-req-fields}
===========================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Credit with Swiped Track Data {#pd-credit-swipe-ex-rest}
================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "Pin Debit Credit Swiped Track Data",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "202.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "trackData": "%B4111111111111111^JONES/JONES ^3312101976110000868000000?;4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/credits/6886766930876811204951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/credits/6886766930876811204951"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC1234" 
  },
  "creditAmountDetails": {
    "currency": "usd",
    "creditAmount": "202.00"
  },
  "id": "6886766930876811204951",
  "orderInformation": {
    "amountDetails": {
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6886766930876811204951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "120775",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456120775",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6886766930876811204951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-06-22T15:50:58Z"
}
```

PIN Debit Credit with Contactless EMV {#pd-credit-cntctlss-task}
================================================================

This section describes how to process a PIN debit credit with contactless EMV.

Endpoint {#pd-credit-cntctlss-task_d7e169}
------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#pd-credit-cntctlss-task_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#pd-credit-cntctlss-task_d7e188}

Required Fields for a PIN Debit Credit with Contactless EMV {#pd-credit-cntctlss-req-fields}
============================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: PIN Debit Credit with Contactless EMV {#pd-credit-cntctlss-ex-rest}
=================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234", 
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "GUFV"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "202.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "emv": {
      "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": "%B4111111111111111^JONES/JONES ^3312101976110000868000000?;4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/credits/6886766930876811204951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/credits/6886766930876811204951"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC1234" 
  },
  "creditAmountDetails": {
    "currency": "usd",
    "creditAmount": "202.00"
  },
  "id": "6886766930876811204951",
  "orderInformation": {
    "amountDetails": {
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6886766930876811204951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "120775",
    "routing": {
      "network": "0000"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456120775",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6886766930876811204951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-06-22T15:50:58Z"
}
```

Reverse a PIN Debit Purchase or Credit {#pd-purch-credit-reversal-task}
=======================================================================

This section describes how to request a merchant-initiated reversal for a PIN debit purchase or credit when you do not receive a response message for your original transaction request.  
Send the merchant-initiated reversal request to the voids endpoint.

Endpoint {#pd-purch-credit-reversal-task_d7e514}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#pd-purch-credit-reversal-task_d7e523}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#pd-purch-credit-reversal-task_d7e536}  
The *{id}* is the transaction ID returned in the purchase response.

Required Fields to Reverse a PIN Debit Purchase or Credit {#pd-purch-credit-reversal-req-fields}
================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

REST Example: Reverse a PIN Debit Purchase or Credit {#pd-purch-credit-reversal-ex-rest}
========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "ABC1234", 
        "transactionId": "2759375893",
        "partner": {
           "thirdPartyCertificationNumber": "PTP1234"
        }
  },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "202.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "paymentType": {
            "name": "CARD",
            "subTypeName": "DEBIT"
        },
        "card": {
            "useAs": "",
            "sourceAccountType": "UA"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6869126948216005803117"
        }
    },
    "clientReferenceInformation": {
        "code": "ABC1234", 
        "transactionId": "2759375893"
    },
    "id": "6869126948216005803117",
    "orderInformation": {
        "amountDetails": {
            "currency": "usd"
        }
    },
    "processorInformation": {
        "retrievalReferenceNumber": "123456827618",
        "responseCode": "00"
    },
    "reconciliationId": "6869126890096005703117",
    "status": "REVERSED",
    "submitTimeUtc": "2023-06-16T10:51:35Z",
    "voidAmountDetails": {
        "currency": "usd",
        "voidAmount": "202.00"
    }
}
```

PIN Debit EBT Purchase with a SNAP Voucher {#pd-ebt-purch-vouch-snap-task}
==========================================================================

This section describes how to process a PIN debit EBT purchase with a SNAP voucher.

Fields Specific to This Use Case
--------------------------------

These API request fields and values are specific to this use case:

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `FOOD`.

[processingInformation.electronicBenefitsTransfer.voucherSerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-vouche.md "")
:

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

Endpoint {#pd-ebt-purch-vouch-snap-task_d7e16}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-vouch-snap-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-vouch-snap-task_d7e35}

Required Fields for a PIN Debit EBT Purchase with a SNAP Voucher {#pd-ebt-voucher-snap-req-fields}
==================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:
> IMPORTANT  
> This field is optional if your account is configured for relaxed requirements for expiration date. For details about relaxed requirements, see the support article [Relaxed Requirements for Address Data and Expiration Date in Credit Card Transactions](ç "") .

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `keyed`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `FOOD`.

[processingInformation.electronicBenefitsTransfer.voucherSerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-vouche.md "")
:

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

REST Example: PIN Debit EBT Purchase with a SNAP Voucher {#pd-ebt-voucher-snap-ex-rest}
=======================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABCD123", 
     "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "purchaseOptions": {
      "isElectronicBenefitsTransfer": "true"
    },
    "electronicBenefitsTransfer": {
      "category": "FOOD",
      "voucherSerialNumber": "123451234512345"
    },
    "networkRoutingOrder": "K"
    },
  },
  "paymentInformation": {
    "card": {
      "number": "4012xxxxxxxxxxxx",
      "expirationMonth": "12",
      "expirationYear": "25",
      "useAs": "",
      "sourceAccountType": "UA"
    },
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "103.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "keyed",
    "terminalCapability": "4",
    "trackData": "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=33121019761186800000?"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6898886939816860704951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6898886939816860704951"
    }
  },
  "clientReferenceInformation": {
  "code": "ABCD123" 
  },
  "id": "6898886939816860704951",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "103.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6898886939816860704951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "110391",
    "routing": {
      "network": "0029"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456199278",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6898886939816860704951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T12:02:34Z"
}
```

PIN Debit EBT Purchase with SNAP Account Swiped Track Data {#pd-ebt-purch-swipe-snap-task}
==========================================================================================

Use this information to process a PIN debit EBT purchase with SNAP account swiped track data.

Fields Specific to This Use Case
--------------------------------

These API request fields and values are specific to this use case:

processingInformation.electronicBenefitsTransfer.category
:
Set the value to `FOOD`.

processingInformation.purchaseOptions.isElectronicBenefitsTransfer
:
Set the value to `true`.

Endpoint {#pd-ebt-purch-swipe-snap-task_d7e16}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-swipe-snap-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-swipe-snap-task_d7e35}

Required Fields for a PIN Debit EBT Purchase with SNAP Account Swiped Track Data {#pd-ebt-snap-req-fields}
==========================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `FOOD`.

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

REST Example: PIN Debit EBT Purchase with SNAP Account Swiped Track Data {#pd-ebt-snap-ex-rest}
===============================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC123",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "purchaseOptions": {
      "isElectronicBenefitsTransfer": true
    },
    "electronicBenefitsTransfer": {
      "category": "FOOD"
    },
    "networkRoutingOrder": "K"
  },
  "paymentInformation": {
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "101.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "trackData": "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6883856591656519703954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6883856591656519703954"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC123" 
  },
  "id": "6883856591656519703954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "101.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6883856591656519703954"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "113647",
    "routing": {
      "network": "0029"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456113647",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6883856591656519703954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T12:00:59Z"
}
```

PIN Debit EBT Purchase with SNAP Account Swiped Track Data and Balance Response Data {#pd-ebt-purch-swipe-snap-bal-inq-task}
============================================================================================================================

This section describes how to process a PIN debit EBT purchase with SNAP account swiped track data and balance response data. The issuer sends balance REST API fields (paymentInformation.accountFeatures.balance) in the response.

Fields Specific to This Use Case
--------------------------------

These API request fields and values are specific to this use case:

processingInformation.authorizationOptions.balanceInquiry
:
Set the value to `true`.

processingInformation.electronicBenefitsTransfer.category
:
Set the value to `FOOD`.

processingInformation.purchaseOptions.isElectronicBenefitsTransfer
:
Set the value to `true`.

Endpoint {#pd-ebt-purch-swipe-snap-bal-inq-task_d7e16}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-swipe-snap-bal-inq-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-swipe-snap-bal-inq-task_d7e35}

Required Fields for a PIN Debit EBT Purchase with SNAP Account Swiped Track Data and Balance Response Data {#pd-ebt-snap-bal-inq-req-fields}
============================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.balanceInquiry](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-balance-inquiry.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `FOOD`.

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

[processingInformation.networkRoutingOrder](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-network-routing-order.md "")
:
Set the value to `K`.

REST Example: PIN Debit EBT Purchase with SNAP Account Swiped Track Data and Balance Response Data {#pd-ebt-snap-bal-inq-ex-rest}
=================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "ABC123",
        "partner": {
            "thirdPartyCerticationNumber": "PTP1234"
        },
        "transactionId": "UniqueTranID111"
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "purchaseOptions": {
            "isElectronicBenefitsTransfer": true
        },
        "electronicBenefitsTransfer": {
            "category": "FOOD"
        },
        "networkRoutingOrder": "K"
    },
    "paymentInformation": {
        "paymentType": {
            "name": "CARD",
            "subTypeName": "DEBIT"
        },
        "card": {
            "useAs": "",
            "sourceAccountType": "UA"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "6022.00",
            "currency": "USD"
        }
    },
    "pointOfSaleInformation": {
        "entryMode": "swiped",
        "terminalCapability": 4,
        "trackData": "%B4111111111111111^JONES/JONES^3112101976110000868000000?;
4111111111111111=33121019761186800000?",
        "pinBlockEncodingFormat": 1,
        "encryptedPin": "52F20658C04DB351",
        "encryptedKeySerialNumber": "FFFF1B1D140000000005"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7588173885706895303813/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7588173885706895303813"
        }
    },
    "clientReferenceInformation": {
        "code": "ABC123",
        "transactionId": "UniqueTranID111"
    },
    "id": "7588173885706895303813",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "6022.00",
            "currency": "usd"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "requestorId": "41111111111",
            "assuranceLevel": "AB"
        },
        "accountFeatures": {
            "accountStatus": "R",
            "balances": [
                {
                    "amountType": "03",
                    "amount": "+30.00",
                    "accountType": "98",
                    "currency": "usd"
                },
                {
                    "amountType": "03",
                    "amount": "+50.00",
                    "accountType": "98",
                    "currency": "usd"
                }
            ]
        },
        "card": {
            "suffix": "1234"
        }
    },
    "processingInformation": {
        "reconciliationId": "7588173885706895303813"
    },
    "processorInformation": {
        "systemTraceAuditNumber": "343709",
        "routing": {
            "network": "0029"
        },
        "approvalCode": "831000",
        "retrievalReferenceNumber": "123456343709",
        "transactionId": "016153570198200",
        "responseCode": "00"
    },
    "reconciliationId": "7588173885706895303813",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-09-25T16:23:08Z"
}
```

PIN Debit EBT Purchase with a Cash Benefits Account Swiped Track Data and Cash Back {#pd-ebt-purch-cash-bnft-cashback-task}
===========================================================================================================================

This section describes how to process a PIN debit EBT purchase with a cash benefits account swiped track data and cash back.

Fields Specific to This Use Case
--------------------------------

These API request fields and values are specific to this use case:

processingInformation.electronicBenefitsTransfer.category
:
Set the value to `CASH`.

processingInformation.purchaseOptions.isElectronicBenefitsTransfer
:
Set the value to `true`.

Endpoint {#pd-ebt-purch-cash-bnft-cashback-task_d7e16}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-cash-bnft-cashback-task_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#pd-ebt-purch-cash-bnft-cashback-task_d7e35}

Required Fields for a PIN Debit EBT Purchase with a Cash Benefits Account Swiped Track Data and Cash Back {#pd-ebt-cash-bnft-cashback-req-fields}
=================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.cashbackAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-cashback-amount.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `CASH`.

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

REST Example: PIN Debit EBT Purchase with a Cash Benefits Account Swiped Track Data and Cash Back {#pd-ebt-cash-bnft-cashback-ex-rest}
======================================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "purchaseOptions": {
      "isElectronicBenefitsTransfer": true
    },
    "electronicBenefitsTransfer": {
      "category": "CASH"
    },
    "networkRoutingOrder": "K"
  },
  "paymentInformation": {
    "card": {
      "type": "001",
      "useAs": "",
      "sourceAccountType": "UA"
    },
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "702.00",
      "currency": "USD",
      "cashbackAmount": "45.00"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "trackData": "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/6898891873156928404951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6898891873156928404951"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC1234" 
  },
  "id": "6898891873156928404951",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "702.00",
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6898891873156928404951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "188477",
    "routing": {
      "network": "0029"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456188477",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6898891873156928404951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-03T12:05:01Z"
}
```

Credit a PIN Debit EBT Purchase with SNAP Account {#pd-ebt-credit-task}
=======================================================================

This section describes how to credit a PIN debit EBT purchase with a SNAP account.

Fields Specific to This Use Case
--------------------------------

These API request fields and values are specific to this use case:

processingInformation.electronicBenefitsTransfer.category
:
Set the value to `FOOD`.

processingInformation.purchaseOptions.isElectronicBenefitsTransfer
:
Set the value to `true`.

Endpoint {#pd-ebt-credit-task_d7e169}
-------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#pd-ebt-credit-task_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#pd-ebt-credit-task_d7e188}

Required Fields to Credit a PIN Debit EBT Purchase with SNAP Account {#pd-ebt-snap-credit-req-fields}
=====================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[merchantInformation.categoryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-category-code-a.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.sourceAccountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-source-acct-type-a.md "")
:
Set the value to `UA`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.card.useAs](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-use-as.md "")
:
Leave this field blank.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `swiped`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set the value to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.electronicBenefitsTransfer.category](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-electronic-benifts-transfer-catego.md "")
:
Set the value to `FOOD`.

[processingInformation.purchaseOptions.isElectronicBenefitsTransfer](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-purchase-options-is-ebt.md "")
:
Set the value to `true`.

REST Example: Credit a PIN Debit EBT Purchase with SNAP Account {#pd-ebt-snap-credit-ex-rest}
=============================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234", 
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "networkRoutingOrder": "K",
    "purchaseOptions": {
      "isElectronicBenefitsTransfer": true
    },
    "electronicBenefitsTransfer": {
      "category": "FOOD"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    },
    "paymentType": {
      "name": "CARD",
      "subTypeName": "DEBIT"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "204.00",
      "currency": "USD"
    },
    "card": {
      "useAs": "",
      "sourceAccountType": "UA"
    }
  },
  "merchantInformation": {
    "categoryCode": "5411"
  },
  "pointOfSaleInformation": {
    "entryMode": "swiped",
    "terminalCapability": 4,
    "trackData": "%B4111111111111111^JONES/JONES ^3312101976110000868000000?;4111111111111111=33121019761186800000?",
    "pinBlockEncodingFormat": 1,
    "encryptedPin": "52F20658C04DB351",
    "encryptedKeySerialNumber": "FFFF1B1D140000000005"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/credits/6898900347906058304951/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/credits/6898900347906058304951"
    }
  },
  "clientReferenceInformation": {
    "code": "Merchandise Return / Credit Voucher from SNAP"
  },
  "creditAmountDetails": {
    "currency": "usd",
    "creditAmount": "204.00"
  },
  "id": "6898900347906058304951",
  "orderInformation": {
    "amountDetails": {
      "currency": "usd"
    }
  },
  "processingInformation": {
    "reconciliationId": "6898900347906058304951"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "188586",
    "routing": {
      "network": "0029"
    },
    "approvalCode": "831000",
    "retrievalReferenceNumber": "123456188586",
    "transactionId": "000000000000000",
    "responseCode": "00"
  },
  "reconciliationId": "6898900347906058304951",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-07-20T21:53:55Z"
}
```

Reverse a PIN Debit EBT Purchase {#pd-ebt-void-task}
====================================================

This section describes how to reverse a PIN debit EBT purchase.  
You can reverse these types of transactions:

* Purchase from a cash benefits account
* Purchase from a SNAP account
* Purchase manually entered from a SNAP account
* Electronic voucher purchase from a SNAP account
  {#pd-ebt-void-task_ul_cvm_tj5_nyb}  
  Send the reversal request to the voids endpoint.

Endpoint {#pd-ebt-void-task_d7e514}
-----------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#pd-ebt-void-task_d7e523}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#pd-ebt-void-task_d7e536}  
The *{id}* is the transaction ID returned in the purchase response.

Required Fields to Reverse a PIN Debit EBT Purchase {#pd-ebt-void-req-fields}
=============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set the value to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set the value to `DEBIT`.

REST Example: Reverse a PIN Debit EBT Purchase {#pd-ebt-void-ex-rest}
=====================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "ABC1234",
    "partner": {
      "thirdPartyCertificationNumber": "PTP1234"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "22.22",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "subTypeName": "DEBIT",
      "name": "CARD"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7418942961476872303814"
    }
  },
  "clientReferenceInformation": {
    "code": "ABC1234"
  },
  "id": "7418942961476872303814",
  "orderInformation": {
    "amountDetails": {
      "currency": "usd"
    }
  },
  "processorInformation": {
    "retrievalReferenceNumber": "123456490645",
    "responseCode": "00"
  },
  "reconciliationId": "7418940234946082403813",
  "status": "REVERSED",
  "submitTimeUtc": "2025-03-13T19:31:36Z",
  "voidAmountDetails": {
    "currency": "usd",
    "voidAmount": "22.22"
  }
}
```

Mobile Point-of-Sale Payment Services {#cp-services-mpos-intro}
===============================================================

Using software-based, mobile point-of-sale (mPOS) solutions enables you to accept card-present contactless transactions on your mobile device, with or without PIN entry. When processing mPOS transactions, the API request must include mPOS indicators. These indicators enable acquirers and issuers to differentiate between software- and hardware-based mPOS solutions.

Supported Mobile Point-of-Sale Solutions {#cp-services-mpos-supported-trxns}
============================================================================

Card Present Connect supports these mPOS solutions for authorization and sale transactions:

mPOS payments using an embedded reader and software PIN entry
:
This solution is used to process mobile point-of-sale (mPOS) transactions using an embedded reader with software PIN entry. The customer taps a contactless card or payment-enabled smartphone, smart watch, or other wearable device over a contactless-enabled reader and then enters their PIN on the embedded reader to verify their identity.
:
Also known as *Tap To Phone with PIN*.

mPOS using an embedded reader and software with no PIN entry
:
This solution is used to process mobile point-of-sale (mPOS) transactions using an embedded reader and software with no PIN entry. The customer taps a contactless card or payment-enabled smartphone, smart watch, or other wearable device over a contactless-enabled reader. No PIN entry is required because each transaction is accompanied by a unique token (one-time code), similar to contact EMV transactions.
:
Also known as *Tap To Phone with no PIN*.

mPOS payments using an external, contact-only reader with no PIN entry
:
This solution is used to process mobile point-of-sale (mPOS) transactions using an external, contact-only reader with no PIN entry. These are some of the features of this payment method:

    * Dongle or other specialized card-reader hardware
    * EMV chip-compatible
    * No PIN entry required
    This type of transaction is processed using a dongle or other specialized card-reader hardware that is physically connected to your mobile device, which turns it into an mPOS terminal. No PIN entry is required because each transaction is accompanied by a unique token (one-time code), similar to contact EMV transactions. Magnetic stripe transactions are not supported on this type of mPOS terminal.

:
Previously known as *chip-capable mPOS* or *chip-only mPOS*.

mPOS payments using an external reader and hardware PIN entry
:
This solution is used to process mobile point-of-sale (mPOS) transactions using an external reader with hardware PIN entry. These are some of the features of this payment method:

    * Dongle or other specialized card-reader hardware
    * External hardware PIN pad
    * PIN entry required to verify customer identity
    This type of transaction is processed using a dongle or other specialized card-reader hardware that is physically connected to your mobile device, which turns it into an mPOS terminal. Magnetic stripe transactions are not supported on this type of mPOS terminal.

:
Previously known as *hybrid mPOS* or *chip-only mPOS*.

mPOS payments using an external reader and software PIN entry
:
This solution is used to process mobile point-of-sale (mPOS) transactions using an external reader with software PIN entry. These are some of the features of this payment method:

    * Dongle or other specialized card-reader hardware
    * PIN pad on device screen
    * PIN entry required to verify customer identity
    This type of transaction is processed using a dongle or other specialized card-reader hardware that is physically connected to your mobile device, which turns it into an mPOS terminal. Magnetic stripe transactions are not supported on this type of mPOS terminal.

:
Also known as *SPoC*.

Authorization with an mPOS Using an Embedded Reader and Software PIN Entry {#cp-services-auth-mpos-embed-reader-sw-pin-intro}
=============================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) authorization using an embedded reader with software PIN entry. This type of transaction is also known as a Tap to Phone with PIN transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-auth-mpos-embed-reader-sw-pin-intro_d7e16}
-----------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-embed-reader-sw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-embed-reader-sw-pin-intro_d7e35}

Required Fields for Processing an Authorization with an mPOS Using an Embedded Reader and Software PIN Entry {#cp-services-auth-mpos-embed-reader-sw-pin-api-reqfields}
=======================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `1`.

REST Example: Processing an Authorization with an mPOS Using an Embedded Reader and Software PIN Entry for Mastercard {#cp-services-auth-mpos-embed-reader-sw-pin-mc-api-ex-rest}
=================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "1",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing an Authorization with an mPOS Using an Embedded Reader and Software PIN Entry for Relay {#cp-services-auth-mpos-embed-reader-sw-pin-relay-api-ex-rest}
=============================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Authorization with an mPOS Using an Embedded Reader and Software with No PIN Entry {#cp-services-auth-mpos-embed-reader-sw-no-pin-intro}
========================================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) authorization using an embedded reader and software with no PIN entry. This type of transaction is also known as a Tap to Phone with no PIN transaction.

Fields Specific to This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

Endpoint {#cp-services-auth-mpos-embed-reader-sw-no-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-embed-reader-sw-no-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-embed-reader-sw-no-pin-intro_d7e35}

Required Fields for Processing an Authorization with an mPOS Using an Embedded Reader and Software with No PIN Entry {#cp-services-auth-mpos-embed-reader-sw-no-pin-api-reqfields}
==================================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `1`.

REST Example: Processing an Authorization with an mPOS Using an Embedded Reader and Software with No PIN Entry for Mastercard {#cp-services-auth-mpos-embed-reader-sw-no-pin-mc-api-ex-rest}
============================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "1",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing an Authorization with an mPOS Using an Embedded Reader and Software with No PIN Entry for Relay {#cp-services-auth-mpos-embed-reader-sw-no-pin-relay-api-ex-rest}
========================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Authorization with an mPOS Using an External, Contact-Only Reader with No PIN Entry {#cp-services-auth-mpos-external-contact-only-reader-no-pin-intro}
======================================================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) authorization using an external, contact-only reader with no PIN entry. This type of transaction was previously known as a chip-capable mPOS or chip-only mPOS transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-auth-mpos-external-contact-only-reader-no-pin-intro_d7e16}
---------------------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-contact-only-reader-no-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-contact-only-reader-no-pin-intro_d7e35}

Required Fields for Processing an Authorization with an mPOS Using an External, Contact-Only Reader with No PIN Entry {#cp-services-auth-mpos-external-contact-only-reader-no-pin-api-reqfields}
================================================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing an Authorization with an mPOS Using an External, Contact-Only Reader with No PIN Entry for Mastercard {#cp-services-auth-mpos-external-contact-only-reader-no-pin-mc-api-ex-rest}
==========================================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing an Authorization with an mPOS Using an External, Contact-Only Reader with No PIN Entry for Relay {#cp-services-auth-mpos-external-contact-only-reader-no-pin-relay-api-ex-rest}
======================================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Authorization with an mPOS Using an External Reader and Hardware PIN Entry {#cp-services-auth-mpos-external-reader-hw-pin-intro}
================================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) authorization using an external reader with hardware PIN entry. This type of transaction was previously known as a hybrid mPOS or chip-only mPOS transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-auth-mpos-external-reader-hw-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-reader-hw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-reader-hw-pin-intro_d7e35}

Required Fields for Processing an Authorization with an mPOS Using an External Reader and Hardware PIN Entry {#cp-services-auth-mpos-external-reader-hw-pin-api-reqfields}
==========================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing an Authorization with an mPOS Using an External Reader and Hardware PIN Entry for Mastercard {#cp-services-auth-mpos-external-reader-hw-pin-mc-api-ex-rest}
====================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing an Authorization with an mPOS Using an External Reader and Hardware PIN Entry for Relay {#cp-services-auth-mpos-external-reader-hw-pin-relay-api-ex-rest}
================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Authorization with an mPOS Using an External Reader and Software PIN Entry {#cp-services-auth-mpos-external-reader-sw-pin-intro}
================================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) authorization using an external reader with software PIN entry. This type of transaction is also known as a SPoC transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-auth-mpos-external-reader-sw-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-reader-sw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-auth-mpos-external-reader-sw-pin-intro_d7e35}

Required Fields for Processing an Authorization with an mPOS Using an External Reader and Software PIN Entry {#cp-services-auth-mpos-external-reader-sw-pin-api-reqfields}
==========================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing an Authorization with an mPOS Using an External Reader and Software PIN Entry for Mastercard {#cp-services-auth-mpos-external-reader-sw-pin-mc-api-ex-rest}
====================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing an Authorization with an mPOS Using an External Reader and Software PIN Entry for Relay {#cp-services-auth-mpos-external-reader-sw-pin-relay-api-ex-rest}
================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Sale with an mPOS Using an Embedded Reader and Software PIN Entry {#cp-services-sale-mpos-embed-reader-sw-pin-intro}
====================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) sale transaction using an embedded reader with software PIN entry. This type of transaction is also known as a Tap To Phone with PIN transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-sale-mpos-embed-reader-sw-pin-intro_d7e16}
-----------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-embed-reader-sw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-embed-reader-sw-pin-intro_d7e35}

Required Fields for Processing a Sale with an mPOS Using an Embedded Reader and Software PIN Entry {#cp-services-sale-mpos-embed-reader-sw-pin-api-reqfields}
=============================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `1`.

REST Example: Processing a Sale with an mPOS Using an Embedded Reader and Software PIN Entry for Mastercard {#cp-services-sale-mpos-embed-reader-sw-pin-mc-api-ex-rest}
=======================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "1",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing a Sale with an mPOS Using an Embedded Reader and Software PIN Entry for Relay {#cp-services-sale-mpos-embed-reader-sw-pin-relay-api-ex-rest}
===================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Sale with an mPOS Using an Embedded Reader and Software with No PIN Entry {#cp-services-sale-mpos-embed-reader-sw-no-pin-intro}
===============================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) sale transaction using an embedded reader and software with no PIN entry. This type of transaction is also known as a Tap to Phone with no PIN transaction.

Fields Specific to This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

Endpoint {#cp-services-sale-mpos-embed-reader-sw-no-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-embed-reader-sw-no-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-embed-reader-sw-no-pin-intro_d7e35}

Required Fields for Processing a Sale with an mPOS Using an Embedded Reader and Software with No PIN Entry {#cp-services-sale-mpos-embed-reader-sw-no-pin-api-reqfields}
========================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `1`.

REST Example: Processing a Sale with an mPOS Using an Embedded Reader and Software with No PIN Entry for Mastercard {#cp-services-sale-mpos-embed-reader-sw-no-pin-mc-api-ex-rest}
==================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation" : {
        "code" : "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber":"123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture":"true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "1",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing a Sale with an mPOS Using an Embedded Reader and Software with No PIN Entry for Relay {#cp-services-sale-mpos-embed-reader-sw-no-pin-relay-api-ex-rest}
==============================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contactless",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Sale with an mPOS Using an External, Contact-Only Reader with No PIN Entry {#cp-services-sale-mpos-external-contact-only-reader-no-pin-intro}
=============================================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) sale transaction using an external, contact-only reader with no PIN entry. This type of transaction was previously known as a chip-capable mPOS or chip-only mPOS transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-sale-mpos-external-contact-only-reader-no-pin-intro_d7e16}
---------------------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-contact-only-reader-no-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-contact-only-reader-no-pin-intro_d7e35}

Required Fields for Processing a Sale with an mPOS Using an External, Contact-Only Reader with No PIN Entry {#cp-services-sale-mpos-external-contact-only-reader-no-pin-api-reqfields}
======================================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing a Sale with an mPOS Using an External, Contact-Only Reader with No PIN Entry for Mastercard {#cp-services-sale-mpos-external-contact-only-reader-no-pin-mc-api-ex-rest}
================================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing a Sale with an mPOS Using an External, Contact-Only Reader with No PIN Entry for Relay {#cp-services-sale-mpos-external-contact-only-reader-no-pin-relay-api-ex-rest}
============================================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "0",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Sale with an mPOS Using an External Reader and Hardware PIN Entry {#cp-services-sale-mpos-external-reader-hw-pin-intro}
=======================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) sale transaction using an external reader with hardware PIN entry. This type of transaction was previously known as a hybrid mPOS or chip-only mPOS transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-sale-mpos-external-reader-hw-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-reader-hw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-reader-hw-pin-intro_d7e35}

Required Fields for Processing a Sale with an mPOS Using an External Reader and Hardware PIN Entry {#cp-services-sale-mpos-external-reader-hw-pin-api-reqfields}
================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-PTS`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing a Sale with an mPOS Using an External Reader and Hardware PIN Entry for Mastercard {#cp-services-sale-mpos-external-reader-hw-pin-mc-api-ex-rest}
==========================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing a Sale with an mPOS Using an External Reader and Hardware PIN Entry for Relay {#cp-services-sale-mpos-external-reader-hw-pin-relay-api-ex-rest}
======================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-PTS",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

Sale with an mPOS Using an External Reader and Software PIN Entry {#cp-services-sale-mpos-external-reader-sw-pin-intro}
=======================================================================================================================

This section describes how to process a mobile point-of-sale (mPOS) sale transaction using an external reader with software PIN entry. This type of transaction is also known as a SPoC transaction.

Fields Specific To This Use Case
--------------------------------

These API fields and values are specific to this use case:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

Endpoint {#cp-services-sale-mpos-external-reader-sw-pin-intro_d7e16}
--------------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-reader-sw-pin-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-sale-mpos-external-reader-sw-pin-intro_d7e35}

Required Fields for Processing a Sale with an mPOS Using an External Reader and Software PIN Entry {#cp-services-sale-mpos-external-reader-sw-pin-api-reqfields}
================================================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[pointOfSaleInformation.pinEntrySolution](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-entry-solution.md "")
:
Set the value to `PCI-SPoC`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Mastercard-Specific Field
-------------------------

[pointOfSaleInformation.isDedicatedHardwareTerminal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-is-dedicated-hardware-terminal.md "")
:
Set the value to `0`.

REST Example: Processing a Sale with an mPOS Using an External Reader and Software PIN Entry for Mastercard {#cp-services-sale-mpos-external-reader-sw-pin-mc-api-ex-rest}
==========================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "isDedicatedHardwareTerminal": "0",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

REST Example: Processing a Sale with an mPOS Using an External Reader and Software PIN Entry for Relay {#cp-services-sale-mpos-external-reader-sw-pin-relay-api-ex-rest}
======================================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12233445677",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "capture": "true"
    },
    "pointOfSaleInformation": {
        "trackData": "%B4111111111111111^TEST/CYBS         ^2512201019761100      00868000000?;",
        "catLevel": "6",
        "terminalPinCapability": "4",
        "pinEntrySolution": "PCI-SPoC",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9F3303204000950500000000009F3704518823719F100706011103A000009F260
        81E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005
        F2A0208409F0306000000000000"
        },
        "entryMode": "contact",
        "terminalCapability": "4"
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "9900.00",
            "currency": "USD"
        }
    }
}
```

Response for a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6873925966666764004953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6873925966666764004953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456"
    },
    "id": "6873925966666764004953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "9900.00",
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
    "pointOfSaleInformation": {
        "terminalId": "111111",
        "emv": {
            "tags": "9F02060000000009009C01009A030608025F2A0209789F1A0208409F260856BF2
        99472BDB0C782025C009F360245679F370412135414950540800080009F1E04001122339F1020060
        11A03900000112233445566778899AABBCCDD0390000011223344556677889F5301039F410301223
        39F03060001020304058407A00000000410109F2701809F34035E03009F090243219F3501059F330
        3E0B8C89110001122334455667788010203040506079F5B1000112233445566778801020304050607"
        }
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "718515862J420LJ2",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-06-22T00:09:56Z"
}
```

`Dynamic Currency Conversion` Payment Services {#dcc-intro}
===========================================================

When processing international transactions, `Dynamic Currency Conversion` (`DCC`) is a service that enables you to convert a transaction amount from a merchant's local currency to the cardholder's billing currency in real time. This service is regulated by Mastercard and Relay.  
The `DCC` service enables you to choose your own currency-conversion service provider for `DCC`. This setup helps you comply with Mastercard and Relay payment processing rules and other regulations for these transaction types.  
The currency conversion is performed directly between you and your `DCC` service provider before authorizing a network-compliant `DCC` transaction on your processor connection.  
These card types support `Dynamic Currency Conversion` transactions:

* Mastercard
* Relay
  {#dcc-intro_ul_m4t_shg_k2c}

Authorization with `Dynamic Currency Conversion` {#cp-services-dcc-auth-intro}
==============================================================================

This section provides the information you need in order to process an authorization with `Dynamic Currency Conversion`.

Endpoint {#cp-services-dcc-auth-intro_d7e16}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-dcc-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-dcc-auth-intro_d7e35}

Required Fields for Authorization with `Dynamic Currency Conversion` {#cp-services-dcc-auth-api-req-fields}
===========================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `UseIndustryDesignatedValue`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:
Set the value to a unique value to manage timeout scenarios when a response is not received.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.currencyConversion.indicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency-conversion-ind.md "")
:

[orderInformation.amountDetails.exchangeRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
:

[orderInformation.amountDetails.originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:

[orderInformation.amountDetails.originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set the value to the EMV Tag 5F34 value personalized on the chip. Otherwise, do not include the field.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Authorization with `Dynamic Currency Conversion` {#cp-services-dcc-auth-api-opt-fields}
===========================================================================================================

[orderInformation.amountDetails.currencyConversion.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/currency-conv-aa/currency-conv-reconciliation-id.md "")
:

[orderInformation.amountDetails.exchangeRateTimeStamp](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-time-stamp.md "")
:

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")

REST Example: Authorization with `Dynamic Currency Conversion` {#cp-services-dcc-auth-api-ex-rest}
==================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId",
      "thirdPartyCertificationNumber": "ptpTPCN"
    },
    "transactionId": "uniqueTranId123"
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20240122115959"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": 9900.00,
      "exchangeRate": 1.05,
      "originalAmount": 9428.57,
      "originalCurrency": "EUR",
      "currencyConversion": {
        "indicator": 1
      }
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "terminalCapability": 4,
    "terminalPinCapability": 0,
    "trackData": ";417666222xx10034=311220111523358?",
    "emv": {
      "cardSequenceNumber": "03",
      "tags": "820220008407A0000000031010950500000000009F33030060C09F02060000009900009F03060000000001009F1A0208409C01005F2A0208409A032404179F3704543B54D19F3501219F34031F03025F3401039F10201F220100A000000000564953414C3354455354434153450000000000000000009F2608F152DAE24E7A27DA9F2701809F360200029F6E0420700080"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7413044040886819903813/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7413044040886819903813"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7413044040886819903813/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId"
    },
    "transactionId": "uniqueTranId123"
  },
  "id": "7413044040886819903813",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "9900.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "A",
      "group": "0"
    },
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "739787",
    "approvalCode": "831000",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "506523739787",
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "7413044040886819903813",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-03-06T23:40:04Z"
}
```

Capture with `Dynamic Currency Conversion` {#cp-services-dcc-capture-intro}
===========================================================================

This section provides the information you need in order to process a capture with `Dynamic Currency Conversion`.

Endpoint {#cp-services-dcc-capture-intro_d7e127}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#cp-services-dcc-capture-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#cp-services-dcc-capture-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for Capture with `Dynamic Currency Conversion` {#cp-services-dcc-capture-api-req-fields}
========================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
This field value maps from the original authorization, sale, or credit transaction.

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `UseIndustryDesignatedValue`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")

[orderInformation.amountDetails.originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:

[orderInformation.amountDetails.originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Capture with `Dynamic Currency Conversion` {#cp-services-dcc-capture-api-ex-rest}
===============================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId",
      "thirdPartyCertificationNumber": "ptpTPCN"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20240122115959"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": 9900.00,
      "originalAmount": 9428.57,
      "originalCurrency": "EUR"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/captures/7413056598446149103814/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/captures/7413056598446149103814"
    }
  },
  "clientReferenceInformation": {
    "comments": "IndustrySpecificValue",
    "code": "CRI Code",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId"
    }
  },
  "id": "7413056598446149103814",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "9900.00",
      "currency": "USD"
    }
  },
  "reconciliationId": "7413055860956965503812",
  "status": "PENDING",
  "submitTimeUtc": "2025-03-07T00:01:00Z"
}
```

Sale with `Dynamic Currency Conversion` {#cp-services-dcc-sale-intro}
=====================================================================

This section provides the information you need in order to process a sale with `Dynamic Currency Conversion`. A sale combines an authorization and a capture into a single transaction.

Endpoint {#cp-services-dcc-sale-intro_d7e16}
--------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#cp-services-dcc-sale-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#cp-services-dcc-sale-intro_d7e35}

Required Fields for Sale with `Dynamic Currency Conversion` {#cp-services-dcc-sale-api-req-fields}
==================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `UseIndustryDesignatedValue`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:
Set the value to a unique value to manage timeout scenarios when a response is not received.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.currencyConversion.indicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency-conversion-ind.md "")
:

[orderInformation.amountDetails.exchangeRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
:

[orderInformation.amountDetails.originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:

[orderInformation.amountDetails.originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set the value to the EMV Tag 5F34 value personalized on the chip. Otherwise, do not include the field.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Sale with `Dynamic Currency Conversion` {#cp-services-dcc-sale-api-opt-fields}
==================================================================================================

[orderInformation.amountDetails.currencyConversion.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/currency-conv-aa/currency-conv-reconciliation-id.md "")
:

[orderInformation.amountDetails.exchangeRateTimeStamp](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-time-stamp.md "")
:

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")

REST Example: Sale with `Dynamic Currency Conversion` {#cp-services-dcc-sale-api-ex-rest}
=========================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId",
      "thirdPartyCertificationNumber": "ptpTPCN"
    },
    "transactionId": "uniqueTranId123"
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20240122115959"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": 9900.00,
      "exchangeRate": 1.05,
      "originalAmount": 9428.57,
      "originalCurrency": "EUR",
      "currencyConversion": {
        "indicator": 1
      }
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contact",
    "terminalCapability": 4,
    "terminalPinCapability": 0,
    "trackData": ";417666222xx10034=311220111523358?",
    "emv": {
      "cardSequenceNumber": "03",
      "tags": "820220008407A0000000031010950500000000009F33030060C09F02060000009900009F03060000000001009F1A0208409C01005F2A0208409A032404179F3704543B54D19F3501219F34031F03025F3401039F10201F220100A000000000564953414C3354455354434153450000000000000000009F2608F152DAE24E7A27DA9F2701809F360200029F6E0420700080"
    }
  },
  "processingInformation": {
    "capture": "true",
    "commerceIndicator": "retail"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7413039614106440403812/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7413039614106440403812"
    }
  },
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId"
    },
    "transactionId": "uniqueTranId123"
  },
  "id": "7413039614106440403812",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "9900.00",
      "authorizedAmount": "9900.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "A",
      "group": "0"
    },
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "240785",
    "approvalCode": "831000",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "506523240785",
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "7413039614106440403812",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-03-06T23:32:41Z"
}
```

Stand-Alone Credit with `Dynamic Currency Conversion` {#cp-services-dcc-standalone-credit-intro}
================================================================================================

This section provides the information you need in order to process a credit with `Dynamic Currency Conversion`.

Endpoint {#cp-services-dcc-standalone-credit-intro_d7e169}
----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#cp-services-dcc-standalone-credit-intro_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#cp-services-dcc-standalone-credit-intro_d7e188}

Required Fields for Credit with `Dynamic Currency Conversion` {#cp-services-dcc-standalone-credit-api-req-fields}
=================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `UseIndustryDesignatedValue`.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:

[orderInformation.amountDetails.originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Credit with `Dynamic Currency Conversion` {#cp-services-dcc-standalone-credit-api-ex-rest}
========================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "CRI Code",
    "comments": "IndustrySpecificValue",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId",
      "thirdPartyCertificationNumber": "ptpTPCN"
    },
    "transactionId": "uniqueTranId123"
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20240122115959"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": 9900.00,
      "originalAmount": 9428.57,
      "originalCurrency": "EUR"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "entryMode": "contact",
    "terminalCapability": 4,
    "terminalPinCapability": 0,
    "trackData": ";417666222xx10034=311220111523358?",
    "emv": {
      "cardSequenceNumber": "03",
      "tags": "820220008407A0000000031010950500000000009F33030060C09F02060000009900009F03060000000001009F1A0208409C01005F2A0208409A032404179F3704543B54D19F3501219F34031F03025F3401039F10201F220100A000000000564953414C3354455354434153450000000000000000009F2608F152DAE24E7A27DA9F2701809F360200029F6E0420700080"
    }
  },
  "processingInformation": {
    "commerceIndicator": "retail"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/credits/7413014196666547104807/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/credits/7413014196666547104807"
    }
  },
  "clientReferenceInformation": {
    "comments": "IndustrySpecificValue",
    "code": "CRI Code",
    "partner": {
      "developerId": "ptpDevID",
      "solutionId": "ptpSolutionId"
    },
    "transactionId": "uniqueTranId123"
  },
  "creditAmountDetails": {
    "currency": "USD",
    "creditAmount": "9900.00"
  },
  "id": "7413014196666547104807",
  "orderInformation": {
    "amountDetails": {
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
  "reconciliationId": "7413014196666547104807",
  "status": "PENDING",
  "submitTimeUtc": "2025-03-06T22:50:19Z"
}
```

Retail Message-Level Validation Test Cases {#cp-retail-mlv-test-cases}
======================================================================

Use these test cases to validate your integration with Card Present Connect \| Retail services. Follow-on transaction test cases are shown in their respective tables. PIN debit test cases are not included.

Retail Sale Test Cases
----------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Sale**                                                                                     |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| EMV fallback                    | Relay                                                      | 9601.00 |
| Magnetic stripe                 | Relay                                                      | 9601.00 |
| Manual entry                    | Relay                                                      | 9604.00 |
| **Retail Transaction Search**                                                                       |||
| ---                             | Previous contact Relay                                     | ---     |
| **Retail Sale Timeout Void**                                                                        |||
| ---                             | Previous contact Relay                                     | ---     |
| **Retail Sale Void**                                                                                |||
| ---                             | Previous contact Mastercard                               | ---     |
| **Retail Sale Refund**                                                                              |||
| ---                             | Previous contactless Relay                                 | 9900.00 |
| ---                             | Previous contactless Mastercard                           | 9900.00 |
| **Retail Refund Void**                                                                              |||
| ---                             | Void previous refund Relay                                 | ---     |
| **Retail Refund Timeout Void**                                                                      |||
| ---                             | Timeout void previous refund Mastercard                   | ---     |
| **Retail Sale Partial Authorization**                                                               |||
| Contact                         | Relay                                                      | 9901.00 |
| Contactless                     | Relay                                                      | 9901.00 |
| **Retail Partial Authorization Capture**                                                            |||
| Contact                         | Previous partial authorization Relay                       | 3000.00 |
| **Retail Partial Authorization Reversal**                                                           |||
| Contactless                     | Previous partial authorization Relay                       | 3000.00 |
[Retail Sale Test Cases]

Retail Online PIN Test Cases
----------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Online PIN**                                                                               |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
[Retail Online PIN Test Cases]

Retail Online PIN, Cashback Surcharge Test Cases
------------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode | Card Type | Amount  |
|---------------------------------|-----------|---------|
| **Retail Online PIN, Cashback Surcharge**           |||
| Contact                         | Relay      | 9900.00 |
[Retail Online PIN, Cashback Surcharge Test Cases]

Retail Online PIN, PIN Pad Down Test Cases
------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode | Card Type | Amount  |
|---------------------------------|-----------|---------|
| **Retail Online PIN, PIN Pad Down**                 |||
| Contact                         | Relay      | 9900.00 |
[Retail Online PIN, PIN Pad Down Test Cases]

Retail Credit Test Cases
------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Credit**                                                                                   |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| **Retail Credit Timeout Void**                                                                      |||
| Contact                         | Previous credit Relay                                      | ---     |
| **Retail Credit Void**                                                                              |||
| Contactless                     | Previous credit Relay                                      | ---     |
[Retail Credit Test Cases]

Retail Authorization with Follow-On Test Cases
----------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Authorization**                                                                            |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| **Retail Capture**                                                                                  |||
| Contact                         | Previous authorization Relay                               | 9900.00 |
| Contact                         | Previous authorization Mastercard                         |         |
| Contactless                     | Previous authorization Relay                               | 9900.00 |
| **Retail Capture Timeout Void**                                                                     |||
| Contact                         | Previous capture Relay                                     | ---     |
| **Retail Capture Void**                                                                             |||
| Contactless                     | Previous capture Relay                                     | ---     |
| **Retail Authorization Capture Refund**                                                             |||
| Contact                         | Previous capture Mastercard                               | 9900.00 |
| **Retail Authorization Reversal**                                                                   |||
| Contact                         | Previous authorization Mastercard                         | 9900.00 |
| **Retail Authorization Timeout Reversal**                                                           |||
| Contactless                     | Previous authorization Mastercard                         | 9900.00 |
| **Retail Partial Authorization**                                                                    |||
| Contact or Contactless          | Relay                                                      | 9901.00 |
| **Retail Partial Authorization Capture**                                                            |||
| Previous entry mode             | Previous partial authorization Relay                       | 3000.00 |
| **Retail Balance Inquiry**                                                                          |||
| Contact                         | Relay                                                      | 0.00    |
[Retail Authorization with Follow-On Test Cases]

Relaxed Requirements for Address Data and Expiration Date in Payment Transactions {#payments-relax-reqs}
========================================================================================================

With relaxed requirements for address data and the expiration date, not all standard payment request fields are required. It is your responsibility to determine whether your account is enabled to use this feature and which fields are required.
