Card Present Connect \| Electric Vehicle Charging Developer Guide {#ev-charging-about-guide}
============================================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to integrate payment processing for electric vehicle (EV) charging services. These API services are available using the REST API.

    Implementing these API services requires software development skills and knowledge of EV charging payment practices. You must write code that uses the REST API request and response fields to integrate the payment services into your existing EV charging payment system.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional processor-specific versions of this guide and additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.visaacceptance.com>

Recent Revisions to This Document {#ev-charging-doc-revisions}
==============================================================

26.05.01
--------

This revision contains only editorial changes and no technical updates.

26.02.01
--------

:
Updated payment services section titles and introductions for clarity in [Electric Vehicle Charging Payment Services](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro.md ""). This update did not include technical changes.
:
Added support for online PIN transactions in [Sale for Post-Pay Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-sale-postpay-intro.md ""). Updated required fields list and examples to include these REST API fields:

    * pointOfSaleInformation.encryptedKeySerialNumber
    * pointOfSaleInformation.encryptedPin
    * pointOfSaleInformation.pinBlockEncodingFormat
    {#ev-charging-doc-revisions_ul_a24_hm4_dhc}

:
Removed instruction to set the value to `0` from all instances of the pointOfSaleInformation.terminalPinCapability REST API field because online PIN transactions are now supported.
:
Updated instruction for pointOfSaleInformation.serviceCode REST API field. For more information, see field description in [Required Fields for a Sale in Post-Pay Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-sale-postpay-intro/ev-charging-sale-postpay-reqfields.md "").

25.09.01
--------

:
Renamed and updated Supported Card Types section to include supported entry modes. See [Supported Card Types and Entry Modes](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/home/ev-charging-card-types.md "").
:
Globally updated partial reversal description from "partial authorization reversal request" to "automatic, host-generated partial reversal request."
:
Reorganized [Electric Vehicle Charging Payment Services](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro.md "") to streamline the list of payment services. Updated all required fields lists and REST examples.
:
Replaced the Capture comments field value description in the Flexible Transaction table. See [Electric Vehicle Charging Transaction Descriptions](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-trxn-descrip.md "").

25.06.01
--------

:
Updated the transaction scenario workflow diagrams and descriptions in [Electric Vehicle Charging Transaction Scenarios](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types.md "").
:
Replaced examples in these sections:

    * [REST Example: Capture for Visa in Pre-Pay EMV Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-capture-prepay-intro/ev-charging-capture-prepay-ex-rest.md "")
    * [REST Example: Capture for Visa in Flexible EMV Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-capture-flexible-intro/ev-charging-capture-flexible-ex-rest.md "")

25.05.01
--------

Initial pilot release.

Introduction to Electric Vehicle Charging {#home}
=================================================

The `Cybersource` solution for processing electric vehicle (EV) charging transactions is Card Present Connect \| Electric Vehicle Charging. This solution is built on global standards established by card schemes to ensure reliable, scalable, and secure processing for card-not-present transactions and EMV contact/contactless card-present transactions. Magnetic stripe processing should be used only as a fallback payment method.

Supported Card Types and Entry Modes {#ev-charging-card-types}
==============================================================

These card types are supported for EV charging transactions:

* Mastercard

* Visa  
  These entry modes are supported for EV charging transactions:

* EMV contact and contactless

* Magnetic stripe swipe

Enabling Electric Vehicle Charging on the Card Present Connect Platform {#ev-charging-prereqs}
==============================================================================================

Before integrating `Cybersource` services for EV charging transactions, you must have these items in place:

* Merchant account with an acquirer that is enabled for processing EV charging transactions on `Visa Platform Connect`.
* `Cybersource` account for payment services.
* Payment technology provider (PTP) that is integrated with `Cybersource` and can perform message-level validation (MLV).
* EMV Level 1 certified terminals and EMV Level 2 certified software in preparation for EMV Level 3 Certification.

Validation and Certification {#ev-charging-val-cert}
====================================================

Work with your payment technology provider (PTP) to allocate time to complete the message-level validation (MLV) and EMV Level 3 certification with your EV charging processing system. You must pass MLV before beginning EMV Level 3 certification. You must complete validation and certification before your system can go live. For more information, see [Enabling Electric Vehicle Charging on the Card Present Connect Platform](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/home/ev-charging-prereqs.md "").

Message-Level Validation {#ev-charging-mlv}
===========================================

Message-level validation (MLV) is a script-based, field-level validation against `Cybersource` specifications.  
Your PTP uses amount-based test triggers to send transactions to a test environment and the Visa Certification Management System for decryption. The test results are XML or RESTful output, `Business Center` test transactions, and log prints.  
`Cybersource` uses these tests to validate the results:

* Cross-edit checks
* Data element validation
* Interchange compliance
* Data mapping validation

EMV Level 3 Certification {#ev-charging-emvl3-cert}
===================================================

This topic is an overview of the Level 3 certification with `Cybersource` and `Visa Platform Connect`. For details on how to design an EMV Level 3 certified payment application, see EMV Book 3 on the EMVCo website: <https://www.emvco.com>.  
*Certification* is a formal process that for validating the device and application compliance with card scheme acceptance requirements. The certification team uses a brand test tool and simulator. The process includes these elements:

* Using a card simulator such as ICC or Fime.
* Failed case analysis and resolution.
* For Mastercard certification, your PTP submits results to Mastercard and pays the costs for approved partners that Mastercard uses.
* For Visa certification, `Cybersource` submits results to Visa.
* Waivers from the card schemes for exceptions.
* Card scheme responses or Letter of Approval (LOA) to signify acceptance and Level 3 certification.  
  Although the processes and support for Global Card Present Connect projects and direct merchant and acquirer projects are different, the timelines are essentially the same.

Card-Present Transaction Risk Control Requirements {#cp-intro-transactions-risk-control}
========================================================================================

Card-present transactions carry lower risk than card-not-present transactions because the customer and payment card are physically present, which can result in lower transaction fees. However, acquirers must still apply standard risk-control measures. Acquirers must monitor transaction activity and manage fraud and disputes in accordance with payment network rules, including the Global Acquirer Risk Standards. They also must comply with these Visa risk compliance programs:

* Visa Fraud Monitoring Program

* Visa Dispute Monitoring Program
  {#cp-intro-transactions-risk-control_ul_gmj_31g_d3c} To meet risk control requirements, acquirers can use one of these options:

* Enable `Cybersource` transaction and fraud monitoring tools.

* Ensure that their payment technology partners (PTPs) implement transaction and fraud monitoring tools.

* Deploy their own transaction and fraud monitoring tools.

Each option provides necessary fraud and risk controls for direct merchant relationships and for PTPs that do not operate their own monitoring solutions. For more information, see [Fraud and Risk Management Solutions](https://www.cybersource.com/en-us/solutions/fraud-and-risk-management.md "").

Electric Vehicle Charging Transaction Scenarios {#ev-charging-trxn-types}
=========================================================================

This section describes the EV charging transaction scenarios supported by `Cybersource`.

Pre-Pay Transaction Scenario {#ev-charging-prepay-trxn-scenario}
================================================================

The Pre-Pay transaction scenario for EV charging enables a customer to pay in advance for the electricity they plan to use when charging their electric vehicle. The transaction amount is calculated based on the amount of time or number of kilowatts (kW) the customer chooses at the start of the charging session. When the final cost of the charging session is less than the estimated amount, an automatic, host-generated partial reversal request is sent at the time of capture.  
Pre-Pay Transaction Workflow ![Pre-Pay transaction workflow diagram showing the sequence of events in the
transaction process](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/ev-charging/images/evcharging-prepay-700x200.svg/jcr:content/renditions/original)  
The Pre-Pay transaction workflow for EV charging typically consists of this sequence of events:

1. The customer chooses the amount of time or number of kW to charge their electric vehicle and presents a payment method to pre-pay for the EV charging session.
2. The charging session transaction amount is calculated by the EV charging payment system using the amount of time spent charging or number of kW chosen.
3. The authorization request is sent to the issuing bank.
4. The issuing bank approves the transaction and sends an authorization response. A temporary hold for the authorized amount is placed on the customer's payment method.
5. The EV charging session starts. To add more time or kW, the customer must start a new charging session.
6. The EV charging session ends when the customer's chosen amount of time or number of kW is reached. If the charging session ends before the chosen amount of charging is achieved, an automatic, host-generated partial reversal request is sent for the unused transaction amount.
7. A capture request for the final transaction amount is sent to the issuing bank. When the final cost of the charging session is less than the estimated amount, an automatic, host-generated partial reversal request is sent at the time of capture.

Post-Pay Transaction Scenario {#ev-charging-postpay-trxn-scenario}
==================================================================

The Post-Pay transaction scenario for EV charging enables a customer to pay for the electricity they use to charge their electric vehicle when the charging session ends. The final transaction amount is calculated based on the amount of time or number of kilowatts (kW) used during the EV charging session.

#### Figure: {#ev-charging-postpay-trxn-scenario_fig_prs_1kv_pfc}

Post-Pay Transaction Workflow  
![Post-Pay transaction workflow diagram showing the sequence of events in the
transaction process](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/ev-charging/images/evcharging-postpay-700x150.svg/jcr:content/renditions/original)  
The Post-Pay transaction workflow for EV charging typically consists of this sequence of events:

1. The customer can choose a specific amount of time or the number of kilowatts (kW) to charge their electric vehicle or can start a charging session for an unspecified amount.
2. The customer presents a payment method to pay for the EV charging session.
3. The EV charging session starts.
4. The EV charging session ends when the customer's chosen amount of time or number of kW is reached, the battery is fully charged, or the customer manually stops the charging session.
5. The charging session transaction amount is calculated by the EV charging payment system using the amount of time spent charging or the number of kW consumed.
6. A sale request is sent to the issuing bank.

Flexible Transaction Scenario {#ev-charging-flexpay-trxn-scenario}
==================================================================

The Flexible transaction scenario for EV charging enables an efficient and customer- and merchant-friendly solution for EV charging transactions. The transaction amount is calculated based on the amount of time or number of kilowatts (kW) used during the EV charging session. This transaction scenario has implementation prerequisites. For more information, see [Prerequisites for the Flexible Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-flexpay-trxn-scenario/ev-charging-flexpay-trxn-scenario-prereqs.md "").  
The Flexible transaction scenario offers these features and benefits:

* Real time adjustments to the EV charging session cost. For more information about this key feature, see the description of *dynamic adjustment capability* below.
* Accommodation of variations in charging time and energy consumption.
* Customers benefit from more accurate billing based on actual usage.
* Merchants benefit from receiving accurate payments for the energy provided and reduce the risk of unpaid balances or excessive refunds.

{#ev-charging-flexpay-trxn-scenario_ul_p4q_frv_pfc}  
A key features of the Flexible transaction scenario is the *dynamic adjustment capability*. When the EV charging session costs more than the initially estimated amount, an incremental authorization request is sent to obtain the additional transaction amount. A merchant can send multiple incremental authorization requests during the charging sessions to increase the charging transaction amount. When the final cost of the charging session, including incremental authorizations, is less than the estimated amount, an automatic, host-generated partial reversal request is sent at the time of capture.

#### Figure:

Flexible Transaction Workflow  
![Flexible transaction workflow diagram showing the sequence of events in the
transaction process](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/ev-charging/images/evcharging-flex-700x350.svg/jcr:content/renditions/original)  
The Flexible transaction workflow for EV charging typically consists of this sequence of events:

1. The customer presents a payment method to start a charging session at an EV charging station.
2. The charging session transaction amount is calculated using the amount of time spent charging or number of kW chosen.
3. The authorization request is sent to the issuing bank.
4. The issuing bank approves the transaction and sends an authorization response. A temporary hold for the authorized amount is placed on the customer's payment method.
5. The EV charging session starts.
6. The final transaction amount is calculated by the EV charging payment system based on the charging time or kW consumed. When the transaction amount is more than the initially authorized amount, an incremental authorization is sent to the issuing bank for the difference between the two amounts.
7. The issuing bank approves incremental authorization request, when applies.
8. The EV charging session ends when the battery is fully charged or when the customer manually stops the charging session.
9. A capture request for the final transaction amount is sent to the issuing bank. When the final cost of the charging session, including any incremental authorizations, is less than the estimated amount, an automatic, host-generated partial reversal request is sent at the time of capture.

Prerequisites for the Flexible Transaction Scenario {#ev-charging-flexpay-trxn-scenario-prereqs}
================================================================================================

To implement the Flexible transaction scenario for EV charging, your payment system must have these prerequisite capabilities:

* Calculates initial estimated EV charging cost based on average charging duration and energy consumption.
* Monitors real time EV charging progress.
* Performs incremental authorizations.
* Communicates with payment systems to perform adjustments.

Electric Vehicle Charging Payment Services {#ev-charging-pymnt-svcs-intro}
==========================================================================

This section describes EV charging payment services.

Electric Vehicle Charging EMV and Card Data {#ev-charging-emv-card-data}
========================================================================

You can request these payment services for EV charging with EMV and card data:

* Authorization

* Incremental authorization

* Capture

* Reversal

* Sale

* Void  
  This table shows which EMV tags are:

* M: required

* P: prohibited

* O: optional

* C: conditional (Send the tag when it is present in the card and terminal.)

|                 Data Element                 | EMV Tag |          Mastercard          |      Visa      |
|----------------------------------------------|---------|------------------------------|----------------|
| Transaction Date                             | 9A      | M                            | M              |
| Transaction Type                             | 9C      | M                            | M              |
| Transaction Currency Code                    | 5F2A    | M                            | M              |
| Terminal Country Code                        | 9F1A    | M                            | M              |
| Amount Authorized                            | 9F02    | M                            | M              |
| Amount Other                                 | 9F03    | M                            | M              |
| Application PAN Sequence Number              | 5F34    | C                            | O              |
| Application Transaction Counter (ATC)        | 9F36    | M                            | M              |
| Application Interchange Profile (AIP)        | 82      | M                            | M              |
| Dedicated File (DF) Name                     | 84      | M                            | M              |
| Terminal Verification Results (TVR)          | 95      | M                            | M              |
| Issuer Application Data                      | 9F10    | M                            | M              |
| Application Cryptogram                       | 9F26    | M                            | M              |
| Cryptogram Information Data (CID)            | 9F27    | M                            | O              |
| Terminal Capabilities                        | 9F33    | M                            | M              |
| Cardholder Verification Method (CVM) Results | 9F34    | M                            | O              |
| Unpredictable Number (UN)                    | 9F37    | M                            | M              |
| Form Factor Indicator                        | 9F6E    | O (Authorization) P (Refund) | C              |
| Mastercard Authenticated Application Data    | 9F60    | O                            | Does not apply |
| Mastercard Kernel Identifier‐Terminal        | 96      | O                            | Does not apply |
[EMV Data Elements and Tags]

Electric Vehicle Charging Transaction Descriptions {#ev-charging-trxn-descrip}
==============================================================================

Use the EV charging transaction descriptions listed in the tables to help you identify types of request messages for production transactions in the `Cybersource` and in your transaction reports. Include the clientReferenceInformation.comments field with a transaction description value when you submit a request.

> IMPORTANT  
> After you add this enhancement to your transaction requests, test the field before deploying it to production. This change does not affect your Level 3 or MLV status if you make no other changes.  
> If you want `Cybersource` to review your test environment result after you add the comments field, contact customer support.

|    Service    | Card present (CP) or Card not present (CNP) |       Comments Field Value       |                                                                                                 Description                                                                                                  |
|---------------|---------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authorization | CP                                          | `Pre-Pay Auth`                   | Authorizes specific amount or duration to start the EV charging session.                                                                                                                                     |
| Capture       | CP                                          | `Pre-Pay Capture`                | Captures final amount for the charging session.                                                                                                                                                              |
| Capture       | CP                                          | `Pre-Pay Capture Less Than Auth` | Captures final amount for the EV charging session when less than the authorization amount. Sends automatic, host-generated partial reversal request for the unused amount when the charging session expires. |
[Pre-Pay Transactions]

| Service | Card present (CP) or Card not present (CNP) | Comments Field Value |                                                Description                                                 |
|---------|---------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------|
| Sale    | CP                                          | `Post-Pay Sale`      | Sale for the amount used during the EV charging session when the customer pays after the charging session. |
[Post-Pay Transactions]

|          Service          | Card present (CP) or Card not present (CNP) |       Comments Field Value        |                                                                                                 Description                                                                                                  |
|---------------------------|---------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authorization             | CP                                          | `Flexible Auth`                   | Authorizes specific amount or duration to start the EV charging session.                                                                                                                                     |
| Capture                   | CP                                          | `Flexible Capture`                | Captures final amount for the charging session.                                                                                                                                                              |
| Capture                   | CP                                          | `Flexible Capture Less Than Auth` | Captures final amount for the EV charging session when less than the authorization amount. Sends automatic, host-generated partial reversal request for the unused amount when the charging session expires. |
| Incremental authorization | CP                                          | `Flexible Incremental Auth`       | Requests incremental authorization when final amount is higher than estimated amount.                                                                                                                        |
[Flexible Transactions]

| Service  | Card present (CP) or Card not present (CNP) |   Comments Field Value   |                                                Description                                                 |
|----------|---------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------|
| Reversal | CP                                          | `Error REVERSAL Timeout` | Reverses previous authorization request for which a response was not received. Reversal not used for sale. |
| Reversal | CP                                          | `Error REVERSAL`         | Reverses previous authorization request. Reversal not used for sale.                                       |
| Void     | CP                                          | `Error VOID Timeout`     | Voids previous sale or capture request for which a response was not received.                              |
| Void     | CP                                          | `Error VOID Payment`     | Voids previous payment (sale) within the same day.                                                         |
| Void     | CP                                          | `Error VOID Capture`     | Voids previous capture within the same day.                                                                |
[Error Transactions]

Incremental Authentication Requirements in the European Union {#ev-charging-cvm-sca-eu-increm-auth-reqs}
========================================================================================================

To meet the customer authentication regulatory requirements for incremental authorizations in the European Union (EU), the recommendation is to set the floor limit on the terminal to a very low value. When you use a terminal with this setting to perform a card-present authorization, the Customer Verification Method (CVM) workflow is initiated. The Strong Customer Authentication (SCA) workflow is not initiated for incremental authorizations when you use the recommended floor limits on the terminal.  
For more information about processing incremental authorizations, see [Incremental Authorization for Flexible Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-increm-auth-flexible-intro.md "").

Authorization for Pre-Pay Scenario {#ev-charging-auth-prepay-intro}
===================================================================

Use this information to process an authorization for a Pre-Pay transaction. For more information about this payment service, see [Pre-Pay Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-prepay-trxn-scenario.md "").

Endpoint {#ev-charging-auth-prepay-intro_d7e16}
-----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#ev-charging-auth-prepay-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#ev-charging-auth-prepay-intro_d7e35}

Required Fields for an Authorization in Pre-Pay Scenario {#ev-charging-auth-prepay-reqfields}
=============================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Pre-Pay Auth`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this value to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:
This field is required when within project scope. Merchant configuration must support multiple terminal IDs. Otherwise, `Cybersource` uses the default terminal ID in the merchant configuration.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set the value to `0`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Authorization for Visa in Pre-Pay Scenario {#ev-charging-auth-prepay-ex-rest}
===========================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Pre-Pay Auth",
    "partner": {
      "developerId": "prodDeveloperId",
      "thirdPartyCertificationNumber": "prodTPCN",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID"
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "authIndicator": 0
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "20.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "catLevel": 2,
    "entryMode": "contact",
    "terminalCapability": 4,
    "terminalPinCapability": 0,
    "terminalId": "87654321",
    "emv": {
      "tags": "9F100706011103A000009F26089302EDF8DC3C6E519F02060000000011009F0306000000000000
9F1A020840950500000000005F2A0208409A031807039C01009F37043444BDD7820200009F360200019F330360B0E8
9F1E04123456789F2701809F6E0420700000
9F7C140000000000000000000000000000000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4761739xx1010135=28122011758928889?"
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20250516115959"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7474186405046592803814/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7474186405046592803814"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7474186405046592803814/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Pre-Pay Auth",
    "partner": {
      "developerId": "prodDeveloperId",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID"
  },
  "id": "7474186405046592803814",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "20.00",
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
      "category": "F",
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
      "tags": "9F36020001910A7D517A9478FA6AD53030"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "067278",
    "paymentAccountReferenceNumber": "V0010013018036783719331133719",
    "approvalCode": "057619",
    "networkTransactionId": "305136650405819",
    "settlementDate": "5141",
    "retrievalReferenceNumber": "513618067278",
    "transactionId": "305136650405819",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "7474186405046592803814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-05-16T18:04:01Z"
}
```

Capture for Pre-Pay EMV Scenario {#ev-charging-capture-prepay-intro}
====================================================================

Use this information to process a capture for a Pre-Pay EMV transaction. For more information about the Pre-Pay transaction scenario, see [Pre-Pay Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-prepay-trxn-scenario.md "").

Endpoint {#ev-charging-capture-prepay-intro_d7e127}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#ev-charging-capture-prepay-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#ev-charging-capture-prepay-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for a Capture in Pre-Pay EMV Scenario {#ev-charging-capture-prepay-reqfields}
=============================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Pre-Pay Capture`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:
This field is required only for contact entry mode.

REST Example: Capture for Visa in Pre-Pay EMV Scenario {#ev-charging-capture-prepay-ex-rest}
============================================================================================

Request

```
{
	"clientReferenceInformation": {
		"code": "test123",
		"comments": "Pre-Pay Capture",
		"partner": {
			"developerId": "prodDeveloperId",
			"thirdPartyCertificationNumber": "prodTPCN",
			"solutionId": "prodSolutionId"
		}
	},
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "20.00",
			"currency": "USD"
		}
	},
	"pointOfSaleInformation": {
		"emv": {
			"tags": "9F100706011103A000009F26089302EDF8DC3C6E519F02060000000011009F03060000000000009F1A020840950500000000005F2A0208409A031807039C01009F37043444BDD7820200009F360200019F330360B0E89F1E04123456789F2701809F6E04207000009F7C140000000000000000000000000000000000000000"
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
			"href": "/pts/v2/captures/7474188291686245403812/voids"
		},
		"self": {
			"method": "GET",
			"href": "/pts/v2/captures/7474188291686245403812"
		}
	},
	"clientReferenceInformation": {
		"comments": "Pre-Pay Capture",
		"code": "test123",
		"partner": {
			"developerId": "prodDeveloperId",
			"solutionId": "prodSolutionId"
		}
	},
	"id": "7474188291686245403812",
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "20.00",
			"currency": "USD"
		}
	},
	"reconciliationId": "7474186405046592803814",
	"status": "PENDING",
	"submitTimeUtc": "2025-05-16T18:07:09Z"
}
```

Sale for Post-Pay Scenario {#ev-charging-sale-postpay-intro}
============================================================

Use this information to process a sale for a Post-Pay transaction. A sale combines an authorization and a capture into a single transaction. For more information about this payment service, see [Post-Pay Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-postpay-trxn-scenario.md "").

Endpoint {#ev-charging-sale-postpay-intro_d7e16}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#ev-charging-sale-postpay-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#ev-charging-sale-postpay-intro_d7e35}

Required Fields for a Sale in Post-Pay Scenario {#ev-charging-sale-postpay-reqfields}
=====================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Post-Pay Sale`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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

[paymentInformation.initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")
:
A value is required for contactless Mastercard transactions.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this value to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
A value is required when EMV Tag 5F34 is configured on the ICC/chip.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")
:
A value is required for non-US Mastercard transactions that include track data.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:
This field is required when within project scope. Merchant configuration must support multiple terminal IDs. Otherwise, `Cybersource` uses the default terminal ID in the merchant configuration.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set the value to `1`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this value to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Sale for Mastercard in Post-Pay Scenario with Online PIN {#ev-charging-sale-postpay-ex-rest}
==========================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Post-Pay Sale",
    "partner": {
      "developerId": "prodDeveloperId",
      "thirdPartyCertificationNumber": "prodTPCN",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID36963"
  },
    "processingInformation": {
    "capture": true,
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "authIndicator": "1"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002"
    },
    "initiationChannel": "00"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "40.00",
      "currency": "EUR"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20250920145732"
  },
  "pointOfSaleInformation": {
    "entryMode": "contactless",
    "catLevel": 2,
    "terminalCapability": 4,
    "emv": {
      "tags": "820279008407A0000000041010950500000480009A032409219C01005F2A0208409F02060000000040009F03060000000000009F10120110A0000F040000000000000000000000FF9F1A0208409F260874ED95E3A297502C9F2701809F3303E0F8C89F34034203009F3501229F360200029F3704A8775702"
    },
    "trackData": ";541333xx89020508=25122010727005691234?",
    "serviceCode": "201",
    "terminalPinCapability": 8,
    "pinBlockEncodingFormat": 0,
    "encryptedPin": "0CF46107296E1A55",
    "encryptedKeySerialNumber": "23288800010000200004"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7585749109016590303814/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7585749109016590303814"
    }
  },
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Post-Pay Sale",
    "partner": {
      "developerId": "prodDeveloperId",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID36963"
  },
  "id": "7585749109016590303814",
  "issuerInformation": {
    "clearingData": "6700210103F0F7F1031AF1F0F0F0F0F0F0F0F0F1F3F0F0F8F4F0F7F3F9F4F94040404040",
    "transactionInformation": "2025092207979288844308"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "40.00",
      "authorizedAmount": "40.00",
      "currency": "EUR"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "002"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "M",
      "group": "0"
    },
    "tokenizedCard": {
      "type": "002"
    },
    "card": {
      "type": "002"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "9F2701809F34034203009F350122910ABD514999106C1F4F0012"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "079792",
    "merchantNumber": "12345678901",
    "approvalCode": "608844",
    "networkTransactionId": "0922MCC0000QX",
    "retrievalReferenceNumber": "526521079792",
    "transactionId": "0922MCC0000QX",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "7585749109016590303814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-09-22T21:01:51Z"
}
```

Authorization for Flexible Scenario {#ev-charging-auth-flexible-intro}
======================================================================

Use this information to process an authorization for a Flexible transaction. For more information about this payment service, see [Flexible Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-flexpay-trxn-scenario.md "").  
For information about processing an incremental authorization when using the Flexible transaction scenario, see [Incremental Authorization for Flexible Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-increm-auth-flexible-intro.md "").

Endpoint {#ev-charging-auth-flexible-intro_d7e16}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#ev-charging-auth-flexible-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#ev-charging-auth-flexible-intro_d7e35}

Required Fields for an Authorization in Flexible Scenario {#ev-charging-auth-flexible-reqfields}
================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Flexible Auth`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this value to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this value to `contact`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this value to `4`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:
This field is required when within project scope. Merchant configuration must support multiple terminal IDs. Otherwise, `Cybersource` uses the default terminal ID in the merchant configuration.

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set the value to `0`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

REST Example: Authorization for Visa in Flexible Scenario {#ev-charging-auth-flexible-ex-rest}
==============================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Flexible Auth",
    "partner": {
      "developerId": "prodDeveloperId",
      "thirdPartyCertificationNumber": "prodTPCN",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID"
  },
  "processingInformation": {
    "commerceIndicator": "retail",
    "authorizationOptions": {
      "authIndicator": 0
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "20.00",
      "currency": "USD"
    }
  },
  "pointOfSaleInformation": {
    "catLevel": 2,
    "entryMode": "contactless",
    "terminalCapability": 4,
    "terminalPinCapability": 0,
    "terminalId": "87654321",
    "emv": {
      "tags": "9F100706011103A000009F26089302EDF8DC3C6E519F02060000000011009F03060000000000009F1A020840950500000000005F2A0208409A031807039C01009F37043444BDD7820200009F360200019F330360B0E89F1E04123456789F2701809F6E04207000009F7C140000000000000000000000000000000000000000",
      "cardSequenceNumber": "01"
    },
    "trackData": ";4761739xx1010135=28122011758928889?"
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20250516115959"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7474221808366131703814/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7474221808366131703814"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7474221808366131703814/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Flexible Auth",
    "partner": {
      "developerId": "prodDeveloperId",
      "solutionId": "prodSolutionId"
    },
    "transactionId": "UniqueTranID"
  },
  "id": "7474221808366131703814",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "20.00",
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
      "category": "F",
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
      "tags": "9F36020001910A7D517A9478FA6AD53030"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "067388",
    "paymentAccountReferenceNumber": "V0010013018036783719331133719",
    "approvalCode": "033470",
    "networkTransactionId": "305136685813069",
    "settlementDate": "5141",
    "retrievalReferenceNumber": "513619067388",
    "transactionId": "305136685813069",
    "responseCode": "00",
    "avs": {
      "code": "2"
    }
  },
  "reconciliationId": "7474221808366131703814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-05-16T19:03:01Z"
}
```

Incremental Authorization for Flexible Scenario {#ev-charging-increm-auth-flexible-intro}
=========================================================================================

Use this information to process an incremental authorization for a Flexible transaction. You can process multiple incremental authorizations for a single EV charging session. Use this type of authorization when the final transaction amount of the charging session is more than the amount of the initial authorization. When the final transaction amount is less than the total authorized amount, an automatic, host-generated partial reversal request is sent.  
For more information about this payment service, see [Flexible Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-flexpay-trxn-scenario.md "").

> IMPORTANT
> You must meet authentication requirements when processing incremental authorizations in the EU. For more information, see [Incremental Authentication Requirements in the European Union](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-pymnt-svcs-intro/ev-charging-cvm-sca-eu-increm-auth-reqs.md "").

Endpoint {#ev-charging-increm-auth-flexible-intro_d7e45}
--------------------------------------------------------

**Production:** `PATCH ``https://api.cybersource.com``/pts/v2/payments/`*{id}*{#ev-charging-increm-auth-flexible-intro_d7e54}  
**Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*{#ev-charging-increm-auth-flexible-intro_d7e66}  
The *{id}* is the transaction ID returned in the original authorization response.

Required Fields for an Incremental Authorization in Flexible Scenario {#ev-charging-increm-auth-flexible-reqfields}
===================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Incremental Auth`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[merchantInformation.transactionLocalDateTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-transaction-local-date-time.md "")
:

orderInformation.amountDetails.additionalAmount
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[processingInformation.authorizationOptions.initiator.credentialStoredOnFile](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")
:

REST Example: Incremental Authorization for Visa in Flexible Scenario {#ev-charging-increm-auth-flexible-ex-rest}
=================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "test123",
    "comments": "Flexible Incremental Auth",
    "partner": {
      "developerId": "prodDeveloperId",
      "thirdPartyCertificationNumber": "prodTPCN",
      "solutionId": "prodSolutionId"
    }
   },
  "processingInformation": {
    "authorizationOptions": {
      "initiator": {
        "storedCredentialUsed": true
      }
    }
  },
  "orderInformation": {
    "amountDetails": {
      "additionalAmount": "10.00",
      "currency": "USD"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": 20191002080000
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7474221808366131703814/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7474222613396289103814"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7474221808366131703814/captures"
    }
  },
  "clientReferenceInformation": {
    "comments": "Flexible Incremental Auth",
    "code": "test123",
    "partner": {
      "developerId": "prodDeveloperId",
      "solutionId": "prodSolutionId"
    }
  },
  "id": "7474222613396289103814",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "30.00",
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "category": "F"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "067388",
    "approvalCode": "033470",
    "transactionId": "305136685813069",
    "responseCode": "00"
  },
  "reconciliationId": "7474221808366131703814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-05-16T19:04:21Z"
}
```

Capture for Flexible EMV Scenario {#ev-charging-capture-flexible-intro}
=======================================================================

Use this information to process a capture for a Flexible EMV transaction. For more information about this payment service, see [Flexible Transaction Scenario](/docs/cybs/en-us/ev-charging/developer/ctv/rest/ev-charging/ev-charging-trxn-types/ev-charging-flexpay-trxn-scenario.md "").

Endpoint {#ev-charging-capture-flexible-intro_d7e127}
-----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#ev-charging-capture-flexible-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#ev-charging-capture-flexible-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for a Capture in Flexible EMV Scenario {#ev-charging-capture-flexible-reqfields}
================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Flexible Capture`.

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:
This field is required only for the contact entry mode.

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.encryptedPin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:
A value is required for online PIN transactions.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
A value is required for online PIN transactions.

REST Example: Capture for Visa in Flexible EMV Scenario {#ev-charging-capture-flexible-ex-rest}
===============================================================================================

Request

```
{
	"clientReferenceInformation": {
		"code": "test123",
		"comments": "Flexible Capture",
		"partner": {
			"developerId": "prodDeveloperId",
			"thirdPartyCertificationNumber": "prodTPCN",
			"solutionId": "prodSolutionId"
		}
	},
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "30.00",
			"currency": "USD"
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
			"href": "/pts/v2/captures/7574535623316268303813/voids"
		},
		"self": {
			"method": "GET",
			"href": "/pts/v2/captures/7574535623316268303813"
		}
	},
	"clientReferenceInformation": {
		"comments": "Flexible Capture",
		"code": "test123",
		"partner": {
			"developerId": "prodDeveloperId",
			"solutionId": "prodSolutionId"
		}
	},
	"id": "7574535623316268303813",
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "30.00",
			"currency": "USD"
		}
	},
	"reconciliationId": "7474221808366131703814",
	"status": "PENDING",
	"submitTimeUtc": "2025-05-16T20:04:21Z"
}
```

