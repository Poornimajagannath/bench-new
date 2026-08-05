Card Present Connect \| Mass Transit Developer Guide {#um-about-guide}
======================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to integrate payment processing for mass transit fare collection systems. These services are available using only the REST API.

    Implementing these services requires software development skills and knowledge and understanding of the card scheme mass transit rules. You must write code that uses the REST API request and response fields to integrate the payment services into your existing mass transit fare collection system.

Conventions
:
These special statements are used in this document:
> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

    > WARNING
    > A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional technical documentation.

    Contact the card schemes for these technical documents:

    * *Discover Global Network Contactless D-PAS: Open Loop Transit Implementation Guide*
    * *Mastercard Global Transit Implementation Guide*
    * *Mastercard Transit Solutions*
    * *Mastercard Transit Terminal Requirements*
    * *Visa Contactless Transit Implementation Guide*
    * *Visa Contactless Transit Terminal Implementation Guide*
    * *Visa Transforming Urban Mobility*

Customer Support
:
For support information about any service, visit the Support Center:  
<http://support.visaacceptance.com>

Recent Revisions to This Document {#um-doc-revisions}
=====================================================

26.06.01
--------

:
Revised and combined Mass Transit Transactions section and Mass Transit Transaction Workflows section into a new section: [Mass Transit Models and Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro.md "").
:
Revised and renamed Additional Workflows section to create a new section: [Common Mass Transit Transaction Workflows and Features](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro.md "").
:
Updated the response/request example in [Merchant-Initiated Sale for Visa Debt Recovery with Stored Card Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-mit-intro.md "").
:
Added support for [Merchant-Initiated Sale for Mastercard Debt Recovery with Card Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/mt-mc-mit-debtrecov-sale-intro.md "").

26.02.01
--------

:
Updated debt recovery workflow descriptions in [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
:
Added response field handling information for authorization requests that return a value in the errorInformation.reason field in these sections:

    * [Mastercard Authorization with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-mc-auth-intro.md "")
    * [Visa Deferred Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-deferred-intro.md "")
    {#um-doc-revisions_ul_j5c_wsj_zhc}

:
Added support for [Merchant-Initiated Sale for Discover Debt Recovery with Card Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/mt-discover-mit-debtrecov-sale-intro.md "").

25.12.01
--------

This revision contains only editorial changes and no technical updates.

25.02
-----

Transaction Types
:
Updated the first ride risk (FRR) transaction type descriptions for field values `TransitDA FRR MIT DR auth` and `TransitDA FRR tap DR auth`. See [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md "").

25.01
-----

Discover
:
Added support for Discover cards in the U.S. See these sections:

    * [Discover Pay As You Go Model](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-discover-payg-intro.md "")
    * [Discover Authorization with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-discover-auth-intro.md "")
    * [Discover Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-discover-intro.md "")

Introduction to Card Present Connect \| Mass Transit {#um-intro-overview}
=========================================================================

Card Present Connect \| Mass Transit is the `Cybersource` solution for processing transactions using card scheme mass transit models. This solution follows global card scheme standards for contactless EMV transit transactions.

Transit Rider Benefits {#um-intro-rider}
========================================

These are some transit rider benefits:

* Retail-like contactless payment experience.
* Fast, contactless tap to enter and exit.
* Payment card data protection.
* Single, combined payment for multiple trips during a set period.
* Ability to request journey history and corresponding receipt.
* Travel fare total on payment card statements.
* Consistent fare collection experience across transit systems in various cities and countries.

Transit System Benefits {#um-intro-merchant}
============================================

These are some mass transit systems benefits:

* Lower ticketing overhead that can reduce the need for ticket booths or paper tickets.
* Ability to track riders when they tap to enter and exit.
* Flexible fare management, including:
  * Riders pay as they go.
  * Fares are aggregated for one payment transaction each travel period.
* Merchant protection such as:
  * Encrypted payment data.
  * First Ride Risk support in some regions.
* Debt recovery support.

Supported Card Types {#um-intro-supported-card-types}
=====================================================

The Mass Transit solution supports these card types. For more information, see [Mass Transit Models and Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro.md "").
* American Express
* Discover (US only)
* Mastercard
* Visa

Mass Transit Terminology {#um-intro-terms}
==========================================

Account Verification Request (AVR)
:
Zero amount authorization request that you send to determine whether the payment card is valid.

Aggregated
:
Transaction in which you calculate the fare based on multiple contactless card taps for trips during a predetermined time period, usually 24 hours, processed as a single transaction.

Back office
:
A component within your transit systems that processes the taps received from transit readers, and that performs any or all journey construction, fare calculation, risk management, and payment processing.

Card hash
:
One-way hash token ID of the payment card data that is used to maintain the deny list.

Combined data authentication (CDA)
:
Authentication technique that uses a combination of card and transaction data.

Deferred authorization
:
Combined authorization and capture request, also known as a sale, for aggregated fare payments.

Deny list
:
List of cards that failed ODA because of an unsuccessful AVR or transit payment. It is used for blocking cards that have not been accepted for travel within your transit system when you are processing aggregated payments, such as the Mastercard PAYG and Visa MTT models.

Deny list manager
:
Manages the deny list and distributes it to the validators.

First Ride Risk debt recovery
:
Under specific and limited conditions established by the card schemes, you can recover the cost of the first ride by capturing a declined authorization. For details, refer to each of the card scheme's rules for mass transit chargeback thresholds and protection. See [First Ride Risk](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-intro-overview/um-workflow-first-ride-risk.md "").

Instrument identifier token
:
`Token Management Service` token that stores the payment card number.

Journey construction
:
The process of analyzing individual taps received from transit readers and forming logical journeys performed by cardholders.

Mobility and Transport Transaction (MTT)
:
Visa model for contactless mass transit payments for single or multiple modes of transportation, which includes fixed, distance-based, and time-based fares.

Offline data authentication (ODA)
:
EMV security feature in which payment cards are authenticated offline. ODA is necessary so that cardholders can quickly tap and enter the transit system. It is used for aggregated transactions, such as Mastercard PAYG and Visa MTT.

Pay As You Go (PAYG) for Mastercard
:
Mastercard model in which the fare is not known when the cardholder taps their card for travel. All cardholder taps are recorded to calculate the fare and process an aggregated payment.

Payment instrument token
:
`Token Management Service` token that stores the instrument identifier token, card expiration date, and billing address.

Retail
:
Transaction in which you process the payment as a standard contactless retail payment.

Tap
:
Refers to the act of presenting a contactless card at a validator.

Ticket inspection
:
Process in which ticket inspectors verify compliance with fare policies by checking paper tickets or using a portable terminal to read the payment card.

Ticket inspectors
:
Transit employees who travel on the transit system to verify passenger travel status.

Transient token
:
Unique, time-limited token ID that is associated with the tokens created by TMS. The validator forwards this ID to your back office to use for payment transactions and to manage tokens. `Cybersource` automatically deletes this token after seven days.

Travel period
:
Period of time during which a traveler can make multiple taps in and out of the transit system, before you submit the final payment transaction for the aggregated amount.

Validator
:
EMV contactless card-present terminal located at an automated turnstile device where cardholders tap their card to enter, and optionally exit from, the transit system. Before allowing the cardholder to enter the transit system, the validator checks the deny list to ensure that the card has not failed ODA.

Mass Transit Prerequisites {#um-intro-reqs}
===========================================

Before integrating `Cybersource` services for mass transit, you must have these systems in place:

* Merchant account with an acquirer that is enabled for mass transit transactions on `Visa Platform Connect`.
* `Cybersource` account for payment services.
* Payment technology provider (PTP) that is integrated with `Cybersource` and can perform message-level validation (MLV).
* EMV Level 1 certified transit terminals and EMV Level 2 certified software in preparation for EMV Level 3 Certification.

Mass Transit Validation and Certification {#um-intro-mlv-emvcert}
=================================================================

You must complete validation and certification activities before your system can go live. Work with your payment technology provider (PTP) to complete message-level validation (MLV) and EMV Level 3 certification of your transit fare processing system. You must pass MLV before beginning EMV Level 3 certification.

Message-Level Validation {#um-intro-mlv2}
=========================================

Message-level validation (MLV) is a script-based, field-level validation against `Cybersource` specifications.  
Your PTP uses amount-based test triggers to send transactions into a test environment and the Visa Certification Management System for decryption. The test results are XML or RESTful output, `Business Center` test transactions, and log prints.  
`Cybersource` uses these activities to validate the results:

* Cross edit checks
* Data element validation
* Interchange compliance
* Data mapping validation

EMV Level 3 Certification {#um-intro-emvl3-cert}
================================================

This section describes the Level 3 certification process used by `Cybersource` and `Visa Platform Connect`. The certification processes and support for Global Card Present Connect projects and for direct merchant and acquirer projects differ from what is described here, but the timelines are basically the same.  
*Certification* is a formal process used to validate that the device and application are compliance with card scheme acceptance regulations. The certification team uses a brand test tool and simulator during the certification process, which includes these elements:

* A payment card simulation tool such as UL, ICC, or Fime.
* Failed case analysis and resolution.
* For Mastercard certification, your PTP submits results to Mastercard and pays the costs for approved partners that Mastercard uses.
* For Visa certification, `Cybersource` submits results to Visa.
* Waivers from the card schemes for exceptions.
* Card schemes responses or Letter of Approval (LOA) to signify acceptance and Level 3 certification.
  {#um-intro-emvl3-cert_ul_vq2_3tg_xtb}  
  For information about how to design an EMV Level 3 certified payment application, see [*EMV Book 3 Application Specification*](https://www.emvco.com/specifications/ "").

First Ride Risk {#um-workflow-first-ride-risk}
==============================================

First Ride Risk (FRR) is a feature that addresses the liability for the first use of a payment credential that fails pre-authorization and might result in a refusal for travel. Use FRR to capture a transaction even when the pre-authorization fails. In this case, the merchant or acquirer assumes responsibility for the risk.

First Ride Risk Eligibility Reason Codes {#um-workflow-first-ride-risk-codes}
=============================================================================

When a failed pre-authorization returns one of these response codes in the processorInformation.responseCode field, the transaction is eligible for FRR and capture:

* `01`: Refer to card issuers.
* `04`: Pick-up.
* `05`: ID certification fails.
* `12`: Invalid related transaction.
* `13`: Invalid amount.
* `14`: Invalid card number (no such account).
* `21`: Card not initialized.
* `22`: Suspected malfunction, related transaction error.
* `34`: Fraud.
* `38`: PIN try limit exceeded.
* `40`: Function requested not supported.
* `41`: Lost card.
* `43`: Stolen card.
* `57`: Transaction not allowed to be processed by cardholder.
* `58`: Transaction not allowed to be processed by terminal.
* `59`: Suspected fraud.
* `62`: Restricted card.
* `68`: Issuer response timeout.
* `75`: Allowable number of PIN tries exceeded.
* `90`: Cutoff is in progress.
* `91`: Issuer cannot process.
* `97`: ATM/POS terminal number cannot be located.
* `98`: Issuer response not received.
* `99`: PIN block error.
* `1A`: The transaction needs additional customer authentication.
* `A0`: MAC failed.
* `N1`: Items not on Bankbook beyond limit, declined.
* `P1`: Contact phone number of cardholder cannot be found in the issuer's system.

Transit Test Cases {#um-test-cases}
===================================

| Case # |                         Transaction                         |    Card Type     | Amount  |                                                                                                                       Comments                                                                                                                        |
|--------|-------------------------------------------------------------|------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Visa AVR and Sale for Aggregated Transaction**                                                                                                                                                                                                                                                                                                      |||||
| 1      | Account verification request (AVR)                          | Visa             | 0.00    | For Visa, an AVR is performed when the card is first used in the transit system or on a more frequent basis depending on what the PTO/PTP requires.                                                                                                   |
| 2      | Deferred sale for aggregated transaction                    | Visa             | 9900.00 |                                                                                                                                                                                                                                                       |
| **Visa First Ride Protection**                                                                                                                                                                                                                                                                                                                        |||||
| 3.1    | Deferred sale for an aggregated transaction                 | Visa             | 9904.00 | Response is a decline that is eligible for capture.                                                                                                                                                                                                   |
| 3.2    | Follow-on capture                                           | Visa             | 9904.00 | Even though the amount exceeds what is allowed for captured under Visa's First Ride Protection rules, proceed with the capture in order to complete this test case.                                                                                   |
| **Mastercard Authorization and Capture**                                                                                                                                                                                                                                                                                                              |||||
| 4.1    | Authorization for an aggregated transaction                 | Mastercard       | 10.00   |                                                                                                                                                                                                                                                       |
| 4.2    | Follow-on capture of an aggregated transaction              | Mastercard       | 9900.00 |                                                                                                                                                                                                                                                       |
| **Debt Recovery**                                                                                                                                                                                                                                                                                                                                     |||||
| 5.1    | Deferred sale                                               | Mastercard, Visa | 9904.00 | Response is a decline that is not eligible for capture. Attempt to reclaim debt using MOTO, tap-initiated, merchant-initiated, card-not-present debt recovery.                                                                                        |
| 5.2    | MOTO debt recovery                                          | Mastercard, Visa | 9601.00 | Response is a decline, but it allows you to validate the Debt Recovery payload.                                                                                                                                                                       |
| 6.2    | Tap-initiated debt recovery                                 | Mastercard, Visa | 9904.00 | Response is a decline, but it allows you to validate the Debt Recovery payload.                                                                                                                                                                       |
| 7.2    | Merchant-initiated debt recovery                            | Mastercard, Visa | 9904.00 | Response is a decline, but it allows you to validate the Debt Recovery payload.                                                                                                                                                                       |
| 8.2    | Card-not-present debt recovery with payer authentication    | Mastercard, Visa | 9904.00 | Response is a decline, but it allows you to validate the Debt Recovery payload.                                                                                                                                                                       |
| 9.2    | Card-not-present debt recovery without payer authentication | Mastercard, Visa | 9904.00 | Response is a decline, but it allows you to validate the Debt Recovery payload.                                                                                                                                                                       |
| **Follow-On Transactions**                                                                                                                                                                                                                                                                                                                            |||||
| 12.2   | Stand-alone credit on test case 02                          | Visa             | 20.00   | Validates your ability to process a credit for an overcharged amount.                                                                                                                                                                                 |
| 13.2   | Void on stand-alone credit test case 12.2                   | Visa             | 9900.00 | Validates your ability to void a stand-alone credit that was processed incorrectly.                                                                                                                                                                   |
| 14     | Reversal of test case 02                                    | Visa             | 9900.00 | Validates your ability to reverse an authorized amount when the final fare is higher than what was originally authorized. After a reversal, resubmit the correct sale amount.                                                                         |
| **Transaction Search**                                                                                                                                                                                                                                                                                                                                |||||
| 15.1   | Deferred sale                                               | Visa             | 9900.00 | Ignore the response in order to simulate a timeout.                                                                                                                                                                                                   |
| 15.2   | Transaction Search                                          | ---              | ---     | The test case 15.1 should show as successful, and therefore no further action is required. If the transaction was declined, the transaction would be placed on the deny list, and first ride protection or debt recovery process should be initiated. |
[Message-Level Validation Test Cases]

Mass Transit Models and Workflows {#um-transit-models-flows-intro}
==================================================================

The Mass Transit solution supports a variety of payment models and workflows for transit fare collection and management.  
This section describes card-specific mass transit models and workflows. Each card type has a distinct mass transit model and transaction workflow that defines how fares are authorized, processed, and settled. Common workflows that are not card specific are also discussed.

American Express Mass Transit Model {#um-models-flows-amex-payg-intro}
======================================================================

The American Express mass transit model is American Express Pay As You Go (PAYG). It is a delayed authorization model that uses the Expresspay transit policy workflow.

American Express Pay As You Go Model Capabilities and Features {#um-models-flows-amex-payg-function-feature}
============================================================================================================

This section describes the capabilities and features of the American Express PAYG model.  
The table lists the mandatory (M) and optional (O) capabilities of this mass transit model.

|                      Capability                       | Requirement |
|-------------------------------------------------------|-------------|
| Dedicated transit merchant category code (MCC) values | M           |
| Population of transit access terminal indicator       | M           |
| Decline expired cards                                 | M           |
| Deny list capability                                  | M           |
| Transaction aggregation                               | O           |
| Account status check                                  | M           |
| Enhanced risk mitigation                              | O           |
| Application transaction counter (ATC) synchronization | O           |
| PAN translation                                       | O           |
[Capabilities of the American Express PAYG Model]

These are the key features of the American Express PAYG model:

* Journeys are multimodal.
* Fares are based on distance.
* Points of entry are contactless.
* Accounts are verified with an authorization for a nominal amount or the maximum fare amount.
* The deny list is checked so that cardholders with previously declined transactions can be blocked.
* Data can be authenticated offline to confirm that the card is valid.
* Multiple card taps and fares can be aggregated into a single payment.
* The deny list is automatically updated every 20 minutes.
* The back office records all trips and fares in order to reconstruct journeys and calculate the final fare.
* When the nominal amount authorization is declined, debt recovery can be performed.
* Standard follow-on payment services can be used to capture, reverse, or void transactions.
  {#um-models-flows-amex-payg-function-feature_ul_isp_3pg_lzb}

American Express Pay As You Go Workflow {#um-models-flows-amex-payg-flow}
=========================================================================

American Express PAYG is a delayed authorization model that uses the Expresspay transit policy workflow. It begins when the rider taps a payment card at the fare collection terminal.

#### Figure: {#um-models-flows-amex-payg-flow_fig_fqh_y5d_j3c}

Pay As You Go Delayed Authorization Model  
![Workflow diagram showing the American Express Pay As You Go Aggregated
transaction model.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/transit-amex-flow-800x600.svg/jcr:content/renditions/original)

1. The cardholder taps the card to enter the transit system.
2. The gate validates the card using offline data authentication (ODA), the card expiration date, and the deny list.
3. When the card is valid, the gate allows the passenger to enter the transit system.
4. When the ODA fails, the card is added to the deny list, and the debt recovery process begins. See [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
5. You send an authorization request for a nominal amount. For authorization and capture options, see [American Express Authorization and Capture Options](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-amex-payg-intro/um-models-flows-amex-payg-auth-capture.md ""). Also see [American Express Delayed Online Authorization with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-amex-auth-intro.md "").
6. When the authorization is successful, you calculate the fare for the travel period.
7. At the last tap of the day, submit a follow-on capture request for the day's aggregated fare amount.

American Express Authorization and Capture Options {#um-models-flows-amex-payg-auth-capture}
============================================================================================

There are two options for handling American Express PAYG authorizations and captures. Implement the option that suits your business model.

> IMPORTANT  
> American Express requires your payment technology partner (PTP) to support nominal and full value authorizations during the Level 3 certification.

1. Send an authorization request for a nominal amount.
2. During the travel period, collect the rider's tap data to calculate the aggregated fare.
3. Choose the request to send:
   * **Option 1:** When the floor limit is reached, send a capture request to collect the accumulated amount.
   * **Option 2:** When the number of trips exceeds the floor limit, send a delayed online authorization request.
4. After receiving a successful response, return to step 1 to handle subsequent trips and journeys.

Discover Pay As You Go Model {#um-models-flows-discover-payg-intro}
===================================================================

The Discover transaction model is Discover Pay As You Go (PAYG).

Discover Pay As You Go Model Features {#um-models-flows-discover-payg-feature}
==============================================================================

These are the key features of the Discover PAYG model:

* Journeys are multimodal.
* Fares are based on distance.
* Points of entry are contactless.
* Accounts are verified with an authorization for a nominal amount or the maximum fare amount.
* The deny list is checked so that cardholders with previously declined transactions can be blocked.
* Data can be authenticated offline to confirm that the card is valid.
* `Token Management Service` (`TMS`) option for managing sensitive authentication data (SAD).
* Multiple card taps and fares can be aggregated into a single payment.
* The deny list is automatically updated every 20 minutes.
* The back office records all trips and fares in order to reconstruct journeys and calculate the final fare.
* When the nominal amount authorization is declined, debt recovery can be performed.
* Standard follow-on payment services can be used to capture, reverse, or void transactions.

Discover Pay As You Go Model Workflow {#um-models-flows-discover-payg-flow}
===========================================================================

The Discover PAYG workflow begins when the rider taps a payment card at the fare collection terminal.

#### Figure:

Discover Pay As You Go Model  
![Diagram of the Discover Pay As You Go Aggregated transaction model.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/pay-as-you-go-model-discover-460x440.svg/jcr:content/renditions/original)

1. The cardholder taps the card to enter the transit system.
2. The gate validates the card using offline data authentication (ODA), the card expiration date, and the deny list.
3. When the card is valid, the gate allows the passenger to enter the transit system.
4. When the ODA fails, the card is added to the deny list, and the debt recovery process begins. See [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
5. You send an authorization request for a nominal amount. See [Discover Authorization with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-discover-auth-intro.md "").
6. When the authorization is successful, you calculate the fare for the travel period.
7. When the fare is more than 15.00 USD, an authorization or sale request for the higher amount is sent. See [Discover Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-discover-intro.md "").
8. At the last tap of the day, a follow-on capture request for the day's aggregated fare amount is sent.

Discover Pay As You Go Aggregated Transactions {#um-models-flows-discover-aggregate}
====================================================================================

When the cardholder taps their Discover card in a transit system, initiate an aggregated transaction by requesting an authorization for 1.00 USD that includes the processingInformation.authorizationOptions.aggregatedAuthIndicator field set to `true`.  
If the issuer approves the authorization, subsequent taps do not require an authorization. The capture amount must not exceed 15.00 USD in the US, and the capture date must not exceed the aggregation duration of up to 14 days from the first tap transaction.  
If the aggregate total nears the maximum aggregation amount, and the next tap will cause the aggregation amount to exceed 15.00 USD, capture the existing aggregate total. Then, authorize the current tap for 1.00 USD to begin a new aggregation cycle, and include the processingInformation.authorizationOptions.aggregatedAuthIndicator field set to `true`.  
For more information about Discover aggregated transactions, see the *Discover Global Network Contactless D-PAS: Open Loop Transit Implementation Guide*.

Mastercard Pay As You Go Model {#um-models-flows-mc-payg-intro}
===============================================================

The Mastercard transit transaction model is Mastercard Pay As You Go (PAYG).

Mastercard Pay As You Go Model Features {#um-models-flows-mc-payg-feature}
==========================================================================

These are the key features of the Mastercard PAYG model:

* Journeys are multimodal.
* Fares are based on distance.
* Points of entry are contactless.
* Accounts are verified with an authorization for a nominal amount or the maximum fare amount.
* The deny list is checked so that cardholders with previously declined transactions can be blocked.
* Data can be authenticated offline to confirm that the card is valid.
* `Token Management Service` (`TMS`) option for managing sensitive authentication data (SAD).
* Multiple card taps and fares can be aggregated into a single payment.
* The deny list is automatically updated every 20 minutes.
* The back office records all trips and fares in order to reconstruct journeys and calculate the final fare.
* When the nominal amount authorization is declined, debt recovery can be performed.
* Standard follow-on payment services can be used to capture, reverse, or void transactions.

Mastercard Pay As You Go Workflow {#um-models-flows-mc-payg-flow}
=================================================================

The Mastercard PAYG workflow begins when the rider taps a payment card at the fare collection terminal.

#### Figure:

Mastercard Pay As You Go Model  
![Diagram showing the Mastercard Pay As You Go model](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/pay-as-you-go-model-460x440.svg/jcr:content/renditions/original)

1. The cardholder taps the card to enter the transit system.
2. The gate validates the card using Mastercard combined data authentication (CDA), card expiration date, and the deny list.
3. When the card is valid, the gate allows the passenger to enter the transit system.
4. When the CDA fails, the card is added to the deny list, and the debt recovery process begins. See [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
5. You send an authorization request for a nominal amount. See [Mastercard Authorization with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-mc-auth-intro.md "").
6. When the authorization is successful, you calculate the fare for the travel period and submit a sale request at the end of the travel period.

Visa Mass Transit Model {#um-intro-models-visa}
===============================================

The Visa transit transaction model is Visa Mobility and Transport Transactions (MTT).

#### Figure: {#um-intro-models-visa_fig_rxt_312_j3c}

Visa Mobility and Transport Transaction Model  
![Diagram of the Visa Mobility and Transport Transaction Model](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/mobility-and-transport-transaction-model-450x450.svg/jcr:content/renditions/original)

Visa Mobility and Transport Transaction Model Capabilities and Features {#um-intro-models-visa-mtt}
===================================================================================================

This section describes the capabilities and features of the Visa MTT model.  
The table lists the capabilities of this mass transit model.

|                             Capability                              |   MTT    |
|---------------------------------------------------------------------|----------|
| Designed for very high customer throughput.                         | Yes      |
| Fare amount always known at the time the journey is started.        | No       |
| Transit reader accepts contactless payments only.                   | Yes      |
| Intended for complex fares, including "capping" or multimodal.      | Yes      |
| Allows accumulation of multiple journeys into a single transaction. | Yes      |
| Account verification request (AVR) performed on first use of card.  | Yes      |
| Special liability model included (chargeback threshold).            | Yes      |
| Requires declined cards to be blocked using deny lists.             | Yes      |
| Requires merchant back office for fare calculation.                 | Yes      |
| Intended authorization model.                                       | Deferred |
| Authorization resubmissions for debt recovery.                      | Yes      |
[Capabilities of the Visa MTT Model]

These are the key features of the Visa MTT model:

* Journeys are multimodal.
* Fares are based on distance.
* Points of entry are contactless.
* Accounts are verified with an account verification request (AVR) authorization for a nominal amount or the maximum fare amount.
* The deny list is checked so that cardholders with previously declined transactions can be blocked.
* Data can be authenticated offline to confirm the card is valid.
* `Token Management Service` (`TMS`) option for managing sensitive authentication data (SAD).
* Multiple card taps can be aggregated into a single payment.
* The back office manages the deny list and distributes them to terminals.
* The back office records all trips and fares to perform journey reconstruction to calculate the final fare.
* Standard follow-on payment services can be used to capture, reverse, or void transactions.
* First ride risk protection when the first authorization fails.
* When the AVR authorization is declined, debt recovery can be performed.

Visa Mobility and Transport Transaction Workflow {#um-workflow-visa-mtt}
========================================================================

The Visa MTT workflow begins when the rider taps a payment card at the fare collection terminal.

#### Figure: {#um-workflow-visa-mtt_fig_yvg_y43_k3c}

Visa Mobility and Transport Transaction Model  
![Diagram showing Visa Mobility and Transport Transaction Model](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/visa-mobility-and-transport-transaction-model-320x600.svg/jcr:content/renditions/original)
1. The cardholder taps the card to enter the transit system.
2. The validator checks the deny list to determine card validity, and allows the rider to enter the transit system.
3. The back office submits an account verification request (AVR) to `Cybersource`. See [Visa Account Verification Request with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-visa-avr-intro.md "").
4. When the authorization fails, the card is added to the deny list, and the debt recovery process begins. See [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
5. During the travel period, the back office collects the rider's tap data to calculate the fare.
6. At the end of the travel period, the back office submits a deferred authorization and capture request. See [Fare Calculation and Submission Workflow](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-fare-calc.md "").
   {#um-workflow-visa-mtt_ol_hgs_smg_qtb}

Common Mass Transit Transaction Workflows and Features {#um-models-flows-common-intro}
======================================================================================

This section describes mass transit transaction workflows and features that are common across supported card schemes.

Aggregated Fare Transaction Workflow {#um-transit-models-flows-aggregated}
==========================================================================

This section describes the Aggregated Fare transactions workflow. In this workflow, the final transit fare is not always known at the time of travel. It is calculated at the end of a travel period, typically 24 hours, based on the journeys made during that period and any applicable fare limits. An *aggregated transaction* is used on contactless terminals at transit system access points to support fare calculation after the travel period has ended.

#### Figure: {#um-transit-models-flows-aggregated_fig_q2r_wmd_j3c}

Aggregated Fare Transaction Workflow  
![Diagram showing aggregated fare transaction workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/aggregated-transaction-flow-480x520.svg/jcr:content/renditions/original)

Aggregated Model with the `Token Management Service` {#um-models-flows-aggregated-tms-ctv-intro}
================================================================================================

Using tokens can reduce the amount of cardholder information that your systems store, process, or transmit. This approach can simplify your Payment Card Industry Data Security Standard (PCI DSS) compliance efforts for maintaining a secure payment processing environment.  
When you integrate aggregated acceptance models with the `Token Management Service` (`TMS`), `TMS` tokenizes, stores, and manages customer and payment data. You store these tokens in your environment instead of customer payment details.  
Use `TMS` to store these types of data:

* EMV track 2 equivalent
* EMV tag-length-value (TLV) string of tags for use during payment authorization
* Card number (`TMS` instrument identifier)
* Card hash value (used within deny list management systems)  
  `TMS` uses a cryptographic base derivation key (BDK) to create tokens that represent the customer and payment data. You store these tokens in your environment and databases instead of customer payment details.

Aggregated Model with the `Token Management Service` Workflow {#um-models-flows-aggregated-tms-ctv-workflow}
============================================================================================================

The Aggregated Model with `TMS` workflow begins when the rider taps a payment card at a fare collection reader (terminal) in the transit system.

#### Figure:

Transit Transactions with `TMS` Workflow  
![Diagram of transit transactions with the Token Management Service](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/mtt-emv-data-tokenization-685x340.svg/jcr:content/renditions/original)

First Tap Process with `TMS`
----------------------------

This process begins when the rider taps their card at the validator.

1. Rider taps card at the validator.
2. The terminal uses the Level 3 payment application to generate a card hash and checks the deny list for the card hash.
3. When the card hash is on the deny list, the card is not approved for travel and the terminal does not open the gate.
4. When the card hash is not on the deny list, the card is approved for travel and the terminal opens the gate and begins the account verification request (AVR) process.
5. The rider performs additional taps as required by the transit system during the travel period.

AVR Process with `TMS`
----------------------

This process begins when the validator sends the transient token data to the back office.

1. The validator sends this tap data to `TMS` to tokenize the data:
   * Transient token, in the ID field
   * Card hash
   * Fluid data descriptor, encoding, and value
2. `TMS` creates tokens of the tap data and stores the card hash with the tokens.
3. The back office performs a verification request as required by the card scheme transit model.
4. The back office uses the transient token ID for these requests:
   * Retrieving the token IDs for debt recovery and BIN lookup requests
   * Performing an AVR, deferred authorization, and follow-on transactions

End of Travel Period Process with `TMS`
---------------------------------------

This process begins at the end of the travel period.

1. At the end of the travel period, the back office calculates the fare and sends a deferred authorization, which can be a combined authorization and capture, using the transient token ID in place of the card data.
2. If the authorization fails, the back office retrieves the card hash from `TMS`, adds the card hash to the deny list, and begins the debt recovery process.

Debt Recovery Process with `TMS`
--------------------------------

This process begins when your back office requests debt recovery.

1. In accordance with the relevant card scheme rule set, the back office requests a merchant-initiated debt recovery using the instrument identifier token ID in place of a card number.
2. When debt recovery is successful, the back office uses the card hash token to retrieve the full card hash value.
3. The back office removes the card hashes from the deny list.
4. When the debt recovery fails, the associated card hashes stay on the deny list.

Near Real-Time Workflow {#um-models-flows-common-denylist}
==========================================================

The near real-time workflow begins when the cardholder taps a payment card at the validator to enter the transit system.

#### Figure:

Near Real-Time Workflow  
![Diagram showing Near Real-Time workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/near-real-time-workflow-550x415.svg/jcr:content/renditions/original)

1. The validator checks the deny list for the payment card.
2. When the card is on the deny list due to a previous failed payment, the validator does not open the gate, and the payment is processed through a debt recovery workflow. See the [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
3. When the card is not on the deny list, the validator opens the transit gate for the cardholder to travel.
4. A new transient token is generated for processing the account verification request (AVR).
5. The back office sends an account verification request (AVR) to `Cybersource`.
6. When the AVR fails, the card is added to the deny list and might be eligible for the first ride risk debt recovery.
7. When the AVR is successful, the card data is used to track subsequent taps, calculate fares for the day, and capture the deferred authorization.

Fare Calculation and Submission Workflow {#um-models-flows-common-fare-calc}
============================================================================

The fare calculation workflow begins at the end of the travel period.

#### Figure:

Visa Fare Calculation and Submission Workflow  
![Diagram showing Visa Fare Calculation and Submission Workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/fare-calculation-submision-workflow-430x600.svg/jcr:content/renditions/original)

1. The back office calculates the fare of all rides taken during the travel period.
2. You request a sale transaction for the accumulated fare. See [Visa Deferred Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-deferred-intro.md "").
3. When the sale is successful, the process is complete.
4. When the sale is declined, the card hash is added to the deny list.
5. When the declined sale amount is above the chargeback threshold, the transaction is moved to debt recovery. See [Debt Recovery Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro/um-models-flows-common-intro/um-models-flows-common-debt-recovery.md "").
6. When the declined sale amount is for a first ride and below the chargeback threshold, you can request the payment using the first ride risk chargeback rules as defined by each card scheme.
   {#um-models-flows-common-fare-calc_ol_cvj_rjw_7tb}

Debt Recovery Workflows {#um-models-flows-common-debt-recovery}
===============================================================

Debt recovery workflows show how to use debt recovery transactions to collect outstanding debt when an aggregated end-of-day transaction is declined.  
Card schemes require merchants to support merchant-initiated debt recovery. This type of transaction can also be required to remove a card from a deny list. Each card scheme has its own transaction-processing rules for debt recovery retry attempts, transaction time limits, and related mass transit transactions. For more information, see each card scheme's rules for transit debt recovery retry attempts and transaction time limits.
IMPORTANT Use a debt recovery transaction to remove a card from a deny list. This action must be completed within one hour of receiving the authorization approval.  
These debt recovery transactions are supported:

* A merchant-initiated transaction that uses the card number.
* A tap-initiated transaction that uses the EMV track 2 equivalent and EMV tags created when the cardholder re-enters the transit system.
* A cardholder-initiated transaction that the customer requests by contacting you.

{#um-models-flows-common-debt-recovery_ul_kxv_bsd_xhc}  
When a debt recovery transaction is declined, you can request payment using the First Ride Risk liability model. For more information, see each card scheme's rules for mass transit transaction chargebacks.

Merchant-Initiated Debt Recovery
--------------------------------

A *merchant-initiated* (MIT) *debt recovery* transaction is a deferred authorization that originates from your back office. This type of transaction is also called *auto-debt recovery*. The authorization resubmission typically uses the card number and references the original, end-of-day transaction that was declined. Visa allows up to six authorization resubmissions within 14 days.

#### Figure: {#um-models-flows-common-debt-recovery_fig_glc_2d2_j3c}

Visa Merchant-Initiated Debt Recovery Workflow  
![Diagram showing Visa's Merchant-Initiated Debt Recovery workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/merchant-init-debt-recovery-flow-475x345.svg/jcr:content/renditions/original)

1. When the number of retry attempts for the MIT debt recovery transaction exceeds the card scheme's limit, stop further processing and keep the card on the deny list.
2. When the amount is below the debt recovery amount limit, send a sale request. See [Merchant-Initiated Sale for Visa Debt Recovery with Stored Card Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-mit-intro.md "").
3. When the transaction is declined, keep the card on the deny list.
4. When the transaction is successful, remove the card from the deny list.

Scheduled Debt Recovery Transaction Resubmission
------------------------------------------------

A *scheduled debt recovery* transaction is a system-generated transaction that originates from your back office. This transaction typically uses the card number and references the original, end-of-day transaction that was declined. Multiple authorization resubmissions might be triggered within 14 days.

#### Figure: {#um-models-flows-common-debt-recovery_fig_ibv_nh1_zhc}

Scheduled Debt Recovery Workflow ![Workflow diagram showing Scheduled Debt Recovery workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/system-gen-debt-recovery-flow-600x345.svg/jcr:content/renditions/original)

1. You configure your payment system to generate scheduled debt recovery authorization requests.
2. The scheduled authorizations attempt debt recovery submissions within 14 days of the initial transaction.
3. When the number of retry attempts for the scheduled debt transaction exceeds the card scheme's limit, stop further processing and keep the card on the deny list.
4. When the amount is below the debt recovery amount limit, send a sale request.
5. When the transaction is declined, keep the card on the deny list.
6. When the transaction is successful, remove the card from the deny list.

Tap-Initiated Debt Recovery
---------------------------

A *tap-initiated debt recovery* transaction occurs when the cardholder returns to the transit gate, and the validator recognizes a new contactless tap.  
You can deny the rider entrance unless the tap-initiated debt recovery transaction is attempted in real time while the cardholder is at the gate. The authorization request includes the EMV track 2 equivalent and EMV tags from the new tap, and a future capture date.

#### Figure: {#um-models-flows-common-debt-recovery_fig_xpp_lr3_k3c}

Tap-Initiated Debt Recovery Workflow  
![Diagram showing Tap-Initiated Debt Recovery Workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/tap-initiated-debt-recovery-flow-260x425.svg/jcr:content/renditions/original)

1. The cardholder taps their card to enter the transit system.
2. You submit a new authorization request using the EMV track 2 equivalent and EMV tags created by the validator and a capture date in the future.
3. When the transaction is declined, keep the card on the deny list.
4. When the transaction is successful, remove the card from the deny list.

Cardholder-Initiated Debt Recovery
----------------------------------

A *cardholder-initiated debt recovery* transaction occurs when the cardholder contacts you. The method of contact depends on where the transaction occurred such as on your e-commerce website or by phone or email for a mail order or telephone order (MOTO) transaction.  
For information about e-commerce or MOTO payment services, see the [*Payments Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").

#### Figure: {#um-models-flows-common-debt-recovery_fig_ltd_wr3_k3c}

Cardholder-Initiated Debt Recovery Flow  
![Diagram showing Cardholder-Initiated Debt Recovery Flow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/cardholder-init-debt-recov-flow-240x410.svg/jcr:content/renditions/original)

1. The cardholder contacts you through your website or by phone or email for a MOTO transaction.
2. You process a card-not-present (CNP) authorization.
3. When the request is successful, remove the card from the deny list.
4. When the request fails, leave the card on the deny list.

Using Multiple Accounts for Processing Functions {#um-models-flows-mult-accts}
==============================================================================

Mass transit systems can use multiple accounts to support a variety of processing functions. Processing functions include these types of tasks:

* Creating tap tokens
* Processing payment requests
* Retrieving card hash values
* Supporting customer journey history inquiries
  Each processing function is handled by a separate account to improve security, isolation, and operational clarity. These accounts are available in the Mass Transit solution:

Account 1
:
This account processes tap token create requests only. For this option, the validators communicate directly with `Cybersource`. Using a separate account enables you to deploy a separate security key to the validator system.

Account 2
:
This account processes payment requests using tokens. You can also choose to further separate debt recovery transactions from standard payment transactions. In that case, account 2a is dedicated to standard payment transactions, and account 2b is dedicated to debt recovery transactions.

Account 3
:
This account processes card hash retrieval requests only. The responses include the full, unmasked card hash value. Using a separate account enables you to deploy a separate security key to the validator system.

Account 4
:
This account operates a customer service web portal where riders can make journey history inquiries. The riders provide the card number to a hosted payment service (such as `Cybersource` Secure Acceptance) where they register as a user. Registration produces the `TMS` instrument identifier token and the card scheme PAR value. These values can be used by your back-office system to look up journey and billing information.

Journey History Service {#um-models-flows-journey-hist-intro}
=============================================================

Card schemes might require transit operators to provide cardholders with a journey history service that enables the cardholder to view their journey history and receipt information. Refer to card scheme documentation for more information about each card scheme's requirements for journey history.

Payment Account Reference
-------------------------

`Cybersource` supports the use of the payment account reference (PAR) by providing the PAR value in authorization responses when a PAR is available from the card issuer. The PAR response field is processorInformation.paymentAccountReferenceNumber. Using the PAR enables you to track card accounts when digital devices, such as smart phones and smart watches, have a network token or DPAN that the card issuer provided to the device. You can use the PAR to provide journey history to cardholders and to match the card account FPAN and DPAN values.

Merchant Descriptor
-------------------

You can use the merchant descriptor feature to produce a transaction-specific reference that cardholders can see on their card account statement. To use the merchant descriptor feature, include the merchantInformation.merchantDescriptor.name field in your authorization, credit, and capture requests. The value for the field must consist solely of English characters.

> IMPORTANT  
> Before implementing transit journey history functionality, confirm with your acquirer and card schemes that the PAR and merchant descriptor features are supported.

Additional Information
----------------------

For information about the `Cybersource` card-not-present services that support a transit system's journey history service, see the [*Payments Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").

Journey History Service Workflow {#um-models-flows-journey-hist-flow}
=====================================================================

The Journey History Service workflow begins when begins when the rider taps a payment card at a fare collection terminal. This service enables the cardholder to view their journey history and receipt information. See card scheme documentation for more information about each scheme's journey history requirements.

#### Figure:

Journey History Request with Token Creation Workflow  
![Workflow diagram showing journey history service using tokens
process.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/mtt-journey-history-390x375.svg/jcr:content/renditions/original)

Mass Transit Payment Services Using EMV and Card Data {#um-processing-emv-vpc}
==============================================================================

You can request these payment services for mass transit with EMV and card data:

* Authorization for account verification and debt recovery.
* Sale for aggregated fares and debt recovery.
* Stand-alone credit.  
  The EMV Data Elements and Tags table lists details about EMV tags that are mandatory (M), prohibited (P), optional (O), or conditional (C) for the processor. Send a conditional tag when it is present in the card and terminal.

|                 Data Element                 | EMV Tag | American Express | Discover PAYG  |       Mastercard PAYG        |    Visa MTT    |
|----------------------------------------------|---------|------------------|----------------|------------------------------|----------------|
| Transaction Date                             | 9A      | M                | M              | M                            | M              |
| Transaction Type                             | 9C      | M                | M              | M                            | M              |
| Transaction Currency Code                    | 5F2A    | M                | M              | M                            | M              |
| Terminal Country Code                        | 9F1A    | M                | M              | M                            | M              |
| Amount Authorized                            | 9F02    | M                | M              | M                            | M              |
| Amount Other                                 | 9F03    | M                | M              | M                            | M              |
| Application PAN Sequence Number              | 5F34    | M                | P              | C                            | O              |
| Application Transaction Counter (ATC)        | 9F36    | M                | M              | M                            | M              |
| Application Interchange Profile (AIP)        | 82      | M                | M              | M                            | M              |
| Dedicated File (DF) Name                     | 84      | M                | M              | M                            | M              |
| Terminal Verification Results (TVR)          | 95      | M                | M              | M                            | M              |
| Issuer Application Data                      | 9F10    | M                | M              | M                            | M              |
| Application Cryptogram                       | 9F26    | M                | M              | M                            | M              |
| Cryptogram Information Data (CID)            | 9F27    | M                | O              | M                            | O              |
| Terminal Capabilities                        | 9F33    | M                | M              | M                            | M              |
| Cardholder Verification Method (CVM) Results | 9F34    | O                | O              | M                            | O              |
| Unpredictable Number (UN)                    | 9F37    | M                | M              | M                            | M              |
| Form Factor Indicator                        | 9F6E    | C\*              | C              | O (Authorization) P (Refund) | C              |
| Mastercard Authenticated Application Data    | 9F60    | Does not apply   | Does not apply | O                            | Does not apply |
| Mastercard Kernel Identifier‐Terminal        | 96      | Does not apply   | Does not apply | O                            | Does not apply |
[EMV Data Elements and Tags]

\***Contactless American Express transactions**: If the Form Factor Indicator data is available on the card, then the merchant, acquirer, or processor must forward this information to the issuer.

Mass Transit Transaction Types {#um-processing-trxn-types}
==========================================================

This section describes mass transit transaction types and related field values. When you include the transaction type in your mass transit request, it appears in the `Business Center` and on transaction reports.  
To include the transaction type in your request, set the clientReferenceInformation.comments request field to the transaction value that corresponds to the service category.  
These are transactions type categories:

TransitDA
:
Use this category for transit deferred-aggregated (DA) transactions. These transactions are also called *Visa MTT* and *Mastercard PAYG* transactions.

BAU
:
Use this category for business-as-usual (BAU) transactions that represent no exceptions or errors for cardholders.

FRR
:
Use this category for first-ride-risk (FRR) transactions that occur where the First Ride Risk liability shift is used. These transactions are specific to a card scheme and region.

DR
:
Use this category for debt-recovery (DR) transactions initiated by the merchant or when the cardholder taps a contactless card at a validator to enter the transit system.

DR CIT
:
Use this category for debt-recovery (DR) customer-initiated transactions (CIT) that are initiated by the cardholder when they explicitly pay a debt, including e-commerce and telephone orders.

Service
:
Use this category for standard transactions when completing payment transactions.

Error
:
Use this category for standard transactions when handling transaction errors.
{#um-processing-trxn-types_ul_o4h_k34_syb}  
These tables list the field values for the payment services supported by each transaction type.

|    Service    |            Field Value             |                                                     Description                                                      |
|---------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Authorization | `TransitDA BAU zero value auth`    | Zero amount authorization to verify a card.                                                                          |
| Authorization | `TransitDA BAU nominal value auth` | Nominal value authorization to verify a card.                                                                        |
| Authorization | `TransitDA BAU full value auth`    | Deferred aggregated authorization for the aggregated value that is sent at the end of the travel period.             |
| Sale          | `TransitDA BAU full value sale`    | Deferred aggregated authorization and capture for the aggregated value that is sent at the end of the travel period. |
| Capture       | `TransitDA BAU capture`            | Capture of any business as usual authorization. Can be a nominal authorization or full value authorization.          |
| Capture       | `TransitDA BAU capture (split)`    | Capture without a previous authorization. Used by Mastercard PAYG in the UK.                                         |
| Authorization | `TransitDA BAU registration auth`  | Zero amount authorization as part of journey history service. Can include CVV2 and 3-D Secure 2.x.                   |
[Business as Usual (BAU) Transaction Field Values]

|    Service    |           Field Value           |                                                                        Description                                                                         |
|---------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authorization | `TransitDA FRR full auth`       | Full amount authorization for a previous verification authorization request that was declined. Decline response is common.                                 |
| Capture       | `TransitDA FRR capture`         | Forced capture of a declined authorization when FRR funding applies.                                                                                       |
| Authorization | `TransitDA FRR MIT DR auth`     | Merchant-initiated authorization to clear a debt status after the TransitDA FRR authorization is processed. If successful, the FRR capture is reversed.    |
| Reversal      | `TransitDA FRR MIT DR reversal` | Reversal sent if previous TransitDA FRR MIT DR authorization was successful.                                                                               |
| Authorization | `TransitDA FRR tap DR auth`     | Authorization sent following a card tap to clear a debt status after TransitDA FRR authorization is processed. If successful, the FRR capture is reversed. |
| Reversal      | `TransitDA FRR tap DR reversal` | Reversal when a TransitDA FRR tap DR authorization was successful.                                                                                         |
[First Ride Risk (FRR) Transaction Field Values]

|    Service    |                                   Field Value                                   |                                                  Description                                                  |
|---------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Sale          | `TransitDA Debt recovery MIT sale FPAN` `TransitDA Debt recovery MIT sale DPAN` | Merchant-initiated debt recovery authorization and capture using a FPAN or DPAN.                              |
| Authorization | `TransitDA Debt recovery MIT auth FPAN` `TransitDA Debt recovery MIT auth DPAN` | Merchant-initiated debt recovery authorization using a FPAN or DPAN.                                          |
| Capture       | `TransitDA Debt recovery MIT capture`                                           | Merchant-initiated debt recovery capture of a previous TransitDA Debt recovery MIT authorization transaction. |
| Sale          | `TransitDA Debt recovery tap sale`                                              | Tap-initiated EMV debt recovery authorization and capture.                                                    |
| Authorization | `TransitDA Debt recovery tap auth`                                              | Tap-initiated EMV debt recovery authorization.                                                                |
| Capture       | `TransitDA Debt recovery tap capture`                                           | Tap-initiated EMV debt recovery capture of a previous TransitDA Debt recovery tap authorization transaction.  |
[Debt Recovery (DR) Transaction Field Values]

|    Service    |                   Field Value                   |                                                        Description                                                        |
|---------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Sale          | `TransitDA Debt recovery CIT Ecom sale`         | Cardholder-initiated debt recovery authorization and capture.                                                             |
| Authorization | `TransitDA Debt recovery CIT Ecom auth`         | Cardholder-initiated debt recovery authorization.                                                                         |
| Capture       | `TransitDA Debt recovery CIT Ecom capture`      | Cardholder-initiated debt recovery capture of a previous TransitDA Debt recovery CIT Ecom authorization transaction.      |
| Sale          | `TransitDA Debt recovery CIT Ecom 3DS2 sale`    | Cardholder-initiated debt recovery authorization and capture.                                                             |
| Authorization | `TransitDA Debt recovery CIT Ecom 3DS2 auth`    | Cardholder-initiated debt recovery authorization.                                                                         |
| Capture       | `TransitDA Debt recovery CIT Ecom 3DS2 capture` | Cardholder-initiated debt recovery capture of a previous TransitDA Debt recovery CIT Ecom 3DS2 authorization transaction. |
| Sale          | `TransitDA Debt recovery CIT Moto sale`         | Cardholder-initiated debt recovery authorization and capture.                                                             |
| Authorization | `TransitDA Debt recovery CIT Moto auth`         | Cardholder-initiated debt recovery authorization.                                                                         |
| Capture       | `TransitDA Debt recovery CIT Moto capture`      | Cardholder-initiated debt recovery capture of previous TransitDA Debt recovery CIT MOTO authorization transaction.        |
[Cardholder-Initiated Debt Recovery (DR CIT) Transaction Field Values]

| Service |    Field Value     |                      Description                      |
|---------|--------------------|-------------------------------------------------------|
| Refund  | `REFUND Automatic` | Programmatic follow-on refund for a previous capture. |
| Credit  | `CREDIT Automatic` | Programmatic stand-alone credit.                      |
| Refund  | `REFUND Manual`    | Manual follow-on refund for a previous capture.       |
| Credit  | `CREDIT Manual`    | Manual stand-alone credit.                            |
[Services Transaction Field Values]

| Service  |    Field Value     |                                                               Description                                                                |
|----------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Reversal | `REVERSAL Timeout` | Reversal of a previous request for which a response was not received.                                                                    |
| Reversal | `REVERSAL other`   | Reversal for an authorization for a reason other than TransitDA FRR MIT DR reversal, TransitDA FRR tap DR reversal, or REVERSAL timeout. |
| Void     | `VOID Timeout`     | Void of a previous request for which a response was not received.                                                                        |
| Void     | `VOID Payment`     | Void of a payment within the same day.                                                                                                   |
| Void     | `VOID Capture`     | Void of a capture within the same day.                                                                                                   |
| Void     | `VOID Refund`      | Void of a refund within the same day.                                                                                                    |
| Void     | `VOID Credit`      | Void of a credit within the same day.                                                                                                    |
[Errors Transaction Field Values]

Required Fields for Authorizations with EMV Data {#mt-auth-fields-matrix}
=========================================================================

This table provides information about the fields required to process authorizations with EMV data.

| REST API Field                                                                                                                                                                                                                        |                                      American Express Account Status Check                                      |                                         American Express Delayed Online                                         |                                                  Discover PAYG                                                  |                                                 Mastercard PAYG                                                 |                                                    Visa AVR                                                     | Information/Value                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|-----------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")                                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. partner. solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "") | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For Visa AVR, set this field to `0.00`.                                                                                                                                                                       |
| [paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")                                             | ---                                                                                                             | ---                                                                                                             | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")                                                                   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `2`.                                                                                                                                                                                        |
| [pointOfSaleInformation.emv. cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For Visa, set this field to `1`.                                                                                                                                                                              |
| [pointOfSaleInformation.emv. tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")                                                                    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `contactless`.                                                                                                                                                                              |
| [pointOfSaleInformation. serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")                                                             | ---                                                                                                             | ---                                                                                                             | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")                                               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `5`.                                                                                                                                                                                        |
| [pointOfSaleInformation. terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")                                                               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `0`.                                                                                                                                                                                        |
| [pointOfSaleInformation. trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")                   | ---                                                                                                             | ---                                                                                                             | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | Set this field to `0`.                                                                                                                                                                                        |
| [processingInformation. authorizationOptions. deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")   | ---                                                                                                             | ---                                                                                                             | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ---                                                                                                                                                                                                           |
| [processingInformation. captureOptions. dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | ---                                                                                                                                                                                                           |
| [processingInformation. commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `retail`.                                                                                                                                                                                   |
| [processingInformation. industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")                                     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                             | Set this field to `transit`.                                                                                                                                                                                  |
[Required Fields for Mass Transit Authorizations with EMV Data]

American Express Account Status Check Authorization with EMV Data {#um-processing-amex-acct-status-auth-intro}
==============================================================================================================

Use this information to process an American Express account status check authorization with EMV data for a nominal amount of 1.00 USD or more. The required function code is 190.

Endpoint {#um-processing-amex-acct-status-auth-intro_d7e16}
-----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-amex-acct-status-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-amex-acct-status-auth-intro_d7e35}

Required Fields for a American Express Account Status Check AVR Authorization with EMV Data {#um-processing-amex-acct-status-reqd-fields}
=========================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU nominal value auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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
Set this field to `003`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this field to `00`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: American Express Account Status Check Authorization with EMV Data {#um-processing-amex-tsc-auth-ex-rest}
======================================================================================================================

Request

```
{ 
   "orderInformation": { 
      "amountDetails": { 
         "currency": "EUR", 
         "totalAmount": "3.00" 
      } 
   }, 
   "paymentInformation": { 
      "card": { 
         "type": "003" 
      } 
   }, 
   "processingInformation": { 
      "capture": false, 
      "captureOptions": { 
         "dateToCapture": "0901" 
      }, 
      "industryDataType": "transit", 
      "commerceIndicator": "retail", 
      "authorizationOptions": { 
         "partialAuthIndicator": false, 
         "deferredAuthIndicator": true, 
         "aggregatedAuthIndicator": true 
      } 
   }, 
   "pointOfSaleInformation": { 
      "emv": { 
         "tags": "9A032309019C01005F2A0209789F1A0203809F02060000000000009F03060000000000009F36020002820219C08408A000000025010901950500000080009F100706020103A400029F2608D89D7C3CA015E11C9F2701809F33030008889F34031F02029F3704A5CCF3EE9F6E04180000E05F340100", 
         "cardSequenceNumber": "00" 
      }, 
      "catLevel": "2", 
      "entryMode": "contactless", 
      "trackData": ";374245XXXXXXXXXX=241270115041234500000?", 
      "terminalId": "12345678", 
      "terminalCapability": "5", 
      "terminalPinCapability": "0" 
   }, 
   "clientReferenceInformation": { 
      "comments": "TransitDA BAU nominal value auth",
      "code": "v7qWAImW6e", 
      "partner": { 
         "solutionId": "BUALWMZK", 
         "thirdPartyCertificationNumber": "condue211609" 
      }, 
      "transactionId": "Fg1xkLJGMmmmvwbB9qWAImW6e" 
   } 
}
```

{#um-processing-amex-tsc-auth-ex-rest_codeblock_tms_qh4_jyb}  
Response to a Successful Request

```
{ 
   "_links": { 
      "authReversal": { 
         "method": "POST", 
         "href": "/pts/v2/payments/6984001952686181104951/reversals" 
      }, 
      "self": { 
         "method": "GET",
         "href": "/pts/v2/payments/6984001952686181104951" 
      },
      "capture": {
         "method": "POST",
         "href": "/pts/v2/payments/6984001952686181104951/captures"
      }
   },
   "clientReferenceInformation": { 
      "code": "v7qWAImW6e", 
      "partner": { 
         "solutionId": "BUALWMZK"
      }, 
      "transactionId": "Fg1xkLJGMmmmvwbB9qWAImW6e" 
   },
   "id": "6984001952686181104951", 
   "orderInformation": { 
      "amountDetails": {
         "authorizedAmount": "3.00", 
         "currency": "EUR"
      } 
   }, 
   "paymentAccountInformation": { 
      "card": {
         "type": "003" 
      } 
   }, 
   "paymentInformation": { 
      "accountFeatures": { 
         "category": "AX", 
         "group": "0" 
      }, 
      "tokenizedCard": { 
         "type": "003" 
      }, 
      "card": { 
         "type": "003" 
      } 
   }, 
   "pointOfSaleInformation": { 
      "emv": { 
         "tags": "9F2701809F34031F02025F340100" 
      } 
   },
   "processorInformation": {
      "systemTraceAuditNumber": "037806", 
       "approvalCode": "845614",
      "networktransactionId": "001032401292273",
      "retrievalReferenceNumber": "330009037806", 
      "transactionId": "001032401292273", 
      "responseCode": "00",
      "avs": { 
         "code": "2" 
      } 
   },
   "reconciliationId": "6984001952686181104951", 
   "status": "AUTHORIZED", 
   "submitTimeUtc": "2023-10-27T09:49:56Z" 
}
```

American Express Delayed Online Authorization with EMV Data {#um-processing-amex-auth-intro}
============================================================================================

Use this information to process an American Express delayed online authorization with EMV data for a nominal amount of 1.00 USD or more. The required function code is 100.

Endpoint {#um-processing-amex-auth-intro_d7e16}
-----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-amex-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-amex-auth-intro_d7e35}

Required Fields for a American Express Delayed Online Authorization with EMV Data {#um-processing-amex-do-auth-reqd-fields}
===========================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU nominal value auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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
Set this field to `003`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this field to `00`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: American Express Delayed Online Authorization with EMV Data {#um-processing-amex-do-auth-ex-rest}
===============================================================================================================

Request

```
{ 
   "orderInformation": { 
      "amountDetails": { 
         "currency": "EUR", 
         "totalAmount": "8.00" 
      } 
   }, 
   "paymentInformation": { 
      "card": { 
         "type": "003" 
      } 
   }, 
   "processingInformation": { 
      "captureOptions": { 
         "dateToCapture": "0901" 
      }, 
      "industryDataType": "transit", 
      "commerceIndicator": "retail"
      } 
   }, 
   "pointOfSaleInformation": { 
      "emv": { 
         "tags": "9A032309019C01005F2A0209789F1A0203809F02060000000000009F03060000000000009F36020002820219C08408A000000025010901950500000080009F100706020103A400029F2608D89D7C3CA015E11C9F2701809F33030008889F34031F02029F3704A5CCF3EE9F6E04180000E05F340100", 
         "cardSequenceNumber": "00" 
      }, 
      "catLevel": "2", 
      "entryMode": "contactless", 
      "trackData": ";341111XXXXXXXXXX=241270215041234500000?", 
      "terminalId": "12345678", 
      "terminalCapability": "5", 
      "terminalPinCapability": "0" 
   }, 
   "clientReferenceInformation": { 
      "comments": "TransitDA BAU full value auth",
      "code": "v7qWAImW6e", 
      "partner": { 
         "solutionId": "BUALWMZK", 
         "thirdPartyCertificationNumber": "condue211609" 
      }, 
      "transactionId": "Fg1xkLJGMmmmvwbB9qWAImW6e" 
   } 
}
```

{#um-processing-amex-do-auth-ex-rest_codeblock_tms_qh4_jyb}  
Response to a Successful Request

```
{
   "_links": { 
      "authReversal": {
         "method": "POST", 
                "href": "/pts/v2/payments/6984003567376178404953/reversals" 
           }, 
           "self": { 
                "method": "GET", 
                "href": "/pts/v2/payments/6984003567376178404953" 
           }, 
      "capture": { 
                "method": "POST", 
         "href": "/pts/v2/payments/6984003567376178404953/captures" 
      } 
   },
   "clientReferenceInformation": { 
      "code": "v7qWAImW6e", 
      "partner": { 
         "solutionId": "BUALWMZK" 
      }, 
           "transactionId": "Fs8xkLJGNslmvwbZ9qWAImW6e" 
   }, 
   "id": "6984003567376178404953", 
   "orderInformation": {
      "amountDetails": { 
         "authorizedAmount": "8.00",
         "currency": "EUR"
      } 
   },
   "paymentAccountInformation": { 
      "card": {
         "type": "003"
      } 
   }, 
   "paymentInformation": { 
      "accountFeatures": { 
         "category": "AX", 
         "group": "0"
      },
      "tokenizedCard": { 
         "type": "003" 
      }, 
      "card": {
         "type": "003" 
      }
   },
   "pointOfSaleInformation": { 
      "emv": { 
         "tags": "9F2701809F34033F00005F340100910AEE43F0FD6F46AABF3030" 
      } 
   },
   "processorInformation": { 
      "systemTraceAuditNumber": "037809", 
      "approvalCode": "437964",
      "networktransactionId": "000002605437964",
      "retrievalReferenceNumber": "330009037809",
      "transactionId": "000002605437964",
      "responseCode": "00",
      "avs": {
         "code": "2"
      } 
   },
   "reconciliationId": "6984003567376178404953", 
   "status": "AUTHORIZED",
   "submitTimeUtc": "2023-10-27T09:52:39Z" 
}   
```

Discover Authorization with EMV Data {#um-processing-discover-auth-intro}
=========================================================================

A Discover authorization with EMV data is an authorization request that can be for a nominal amount of 1.00 USD or a fare amount up to 15.00 USD. Mass transit Discover transactions are supported only in the U.S.

Endpoint {#um-processing-discover-auth-intro_d7e16}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-discover-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-discover-auth-intro_d7e35}

Required Fields for a Discover Authorization with EMV Data {#um-processing-discover-auth-reqd-fields}
=====================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU nominal value auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set this field to `1.00`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
Set this field to `004`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this field to `99`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Discover Authorization with EMV Data {#um-processing-discover-auth-ex-rest}
=========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA BAU nominal value auth",
        "code": "123456",
        "transactionId": "1346334405",
        "partner": {
            "solutionId": "123456",
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "capture": "false",
        "commerceIndicator": "retail",
        "authorizationOptions": {
            "deferredAuthIndicator": "true",
            "aggregatedAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "004"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0",
        "emv": {
            "tags": "9F2608101F3F75E8596414820211009F360200019F2701409F100A01151000000000000000950500000000009F370438A871109A032212129F1A0208409F33030008089F3501259F02060000000000005F2A0208409C01008407A0000001523010",
            "cardSequenceNumber": "99"
        },
        "trackData": ";651000XXXXXXXXXX=49122011804088500000?"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6920241974736435904951/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6920241974736435904951"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6920241974736435904951/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "comments": "TransitDA BAU nominal value auth",
        "partner": {
            "solutionId": "123456"
        },
        "transactionId": "1346334405"
    },
    "id": "6920241974736435904951",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "1.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "004"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "DI",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "004"
        },
        "card": {
            "type": "004"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F2701409F3501259F36020001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "033732",
        "approvalCode": "813783",
        "cardReferenceData": "05",
        "networktransactionId": "VISJ      303226529970011",
        "retrievalReferenceNumber": "322614033732",
        "consumerAuthenticationResponse": {
            "code": "0",
            "codeRaw": "0"
        },
        "transactionId": "VISJ      303226529970011",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "6920241974736435904951",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-08-14T14:43:19Z"
}
```

Mastercard Authorization with EMV Data {#um-processing-mc-auth-intro}
=====================================================================

Use this information to process a Mastercard authorization with EMV data for a nominal amount.

Response Field Handling
-----------------------

When you receive the `AUTH_DECLINE_CAPTURE_POSSIBLE` value in the errorInformation.reason field of an authorization response, it indicates that a capture attempt will not be rejected automatically. Before processing the capture, verify that it is permitted in this scenario by reviewing the card scheme's First Ride Risk and shared‑liability rules.  
For an example of the field data, see the response in [REST Example: Visa Deferred Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-deferred-intro/um-processing-sale-deferred-ex-rest.md ""). For more information about the field, see the [errorInformation.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/error-info-aa/error-info-reason.md "") field description.

Endpoint {#um-processing-mc-auth-intro_d7e16}
---------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-mc-auth-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-mc-auth-intro_d7e35}

Required Fields for a Mastercard Authorization with EMV Data {#um-processing-mc-auth-reqd-fields}
=================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU nominal value auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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
Set this field to `002`.

[paymentInformation.initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set this field to `0`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")
:

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.
{#um-processing-mc-auth-reqd-fields_dl_ihk_321_ndc}

REST Example: Mastercard Authorization with EMV Data {#um-processing-mc-auth-ex-rest}
=====================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA BAU nominal value auth",
        "code": "10000568",
        "transactionId": "20000568",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "commerceIndicator": "retail",
        "capture": "false",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "authorizationOptions": {
            "authIndicator": "0",
            "deferredAuthIndicator": "true",
            "aggregatedAuthIndicator": "true",
            "transportationMode": "00"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        },
        "initiationChannel": "00"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0", 
        "emv": {
            "tags": "5F2A0209768407A00000000410109F360200039F03060000000000009C01005F3401019F10120110A0000F040000000000000000000000FF9F33030008C89A032204259F2608093A260A58500E949F2701809F020600000000010082021B809F34033F00029F1A0209769F37046F4D8104950500200000019F6E06005601023030"
        },
        "trackData": ";5413XXXXXXXXXXXX=49122010123456789?",
        "serviceCode": "201"
    }
}
```

{#um-processing-mc-auth-ex-rest_codeblock_tms_qh4_jyb}  
Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508877845426512004004"
        }
    },
    "clientReferenceInformation": {
        "code": "10000574",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000574"
    },
    "errorInformation": {
        "reason": "AUTH_DECLINE_CAPTURE_POSSIBLE",
        "message": "Authorization Declined. Follow-on Capture can be processed."
    },
    "id": "6508877845426512004004",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "164207",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511164207",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "AUTHORIZED"
}
```

Visa Account Verification Request with EMV Data {#um-processing-visa-avr-intro}
===============================================================================

Use this information to process a Visa account verification request (AVR) with EMV data for a zero amount.

Endpoint {#um-processing-visa-avr-intro_d7e16}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-visa-avr-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-visa-avr-intro_d7e35}

Required Fields for a Visa AVR Authorization with EMV Data {#um-processing-visa-avr-reqd-fields}
================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU zero value auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set this field to `0.00`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
Set this field to `001`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

REST Example: Visa AVR Authorization with EMV Data {#um-processing-visa-avr-ex-rest}
====================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA BAU zero value auth",
        "code": "10000564",
        "transactionId": "20000564",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "capture": "false",
        "commerceIndicator": "retail"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0",
        "emv": {
            "tags": "5F2A0209768407A00000000310109F360200029F03060000000000009C01005F3401019F10201F220100A00000000000000000000000000000000000000000000000000000009F33030008089A032204259F260845E978CEEC63154F9F2701409F0206000000000200820220209F34031F00009F1A0209769F6E04207000009F3704B257DA1495050000000000",
            "cardSequenceNumber": "1"
        },
        "trackData": ";476173XXXXXXXXXX=241220119058254?"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6508875466126538104002/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508875466126538104002"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6508875466126538104002/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "10000564",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000564"
    },
    "id": "6508875466126538104002",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "0.00",
            "currency": "EUR"
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
        "systemTraceAuditNumber": "162930",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511162930",
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
    "reconciliationId": "6508875466126538104002",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-04-25T11:52:26Z"
}
```

Response to a Declined Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508876049646556304003"
        }
    },
    "clientReferenceInformation": {
        "code": "10000566",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000566"
    },
    "errorInformation": {
        "reason": "AUTH_DECLINE_CAPTURE_POSSIBLE",
        "message": "Authorization Declined. Follow-on Capture can be processed."
    },
    "id": "6508876049646556304003",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "162936",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511162936",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "AUTHORIZED"
}
```

Required Fields for a Sale with EMV Data {#mt-sale-fields-matrix}
=================================================================

This table provides information about the required fields for a sale with EMV data using various card types.

| REST API Field                                                                                                                                                                                                                       |                                                  Discover Sale                                                  |                                                  Visa Deferred                                                  | Information/Value                                                                                                                                                                                             |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")                                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation.partner. solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For Visa AVR, set this field to `0.00`.                                                                                                                                                                       |
| [paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")                                                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")                                                                  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `2`.                                                                                                                                                                                        |
| [pointOfSaleInformation.emv. cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation.emv. tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")                                                                   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")                                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `contactless`.                                                                                                                                                                              |
| [pointOfSaleInformation. terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")                                              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `5`.                                                                                                                                                                                        |
| [pointOfSaleInformation. terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")                                                              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `0`.                                                                                                                                                                                        |
| [pointOfSaleInformation. trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")                                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "") | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. captureOptions. dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `retail`.                                                                                                                                                                                   |
| [processingInformation. industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")                                    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `transit`.                                                                                                                                                                                  |
[Required Fields for Mass Transit Sales with EMV Data]

Discover Sale with EMV Data {#um-processing-sale-discover-intro}
================================================================

A sale transaction comprises an authorization and capture. When the fare is more than 15.00 USD, request a sale with EMV data.

Endpoint {#um-processing-sale-discover-intro_d7e16}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-sale-discover-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-sale-discover-intro_d7e35}

Required Fields for a Discover Sale with EMV Data {#um-processing-sale-discover-reqd-fields}
============================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA BAU nominal value sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set this field to `1.00`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
Set this field to `004`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this field to `99`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Discover Sale with EMV Data {#um-processing-sale-discover-ex-rest}
================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA BAU full value sale",
        "code": "123456",
        "transactionId": "1357334401",
        "partner": {
            "solutionId": "123456",
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "reconciliationId": "123456789",
        "captureOptions": {
            "dateToCapture": "0818"
        },
        "capture": "true",
        "commerceIndicator": "retail"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "25.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "004"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0",
        "emv": {
            "tags": "9F2608101F3F75E8596414820211009F360200019F2701409F100A01151000000000000000950500000000009F370438A871109A032212129F1A0208409F33030008089F3501259F02060000000000005F2A0208409C01008407A0000001523010",
            "cardSequenceNumber": "99"
        },
        "trackData": ";651000XXXXXXXXXX=49122011804088500000?"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6920243246666458104951/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6920243246666458104951"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "comments": "TransitDA BAU full value sale",
        "partner": {
            "solutionId": "123456"
        },
        "transactionId": "1357334401"
    },
    "id": "6920243246666458104951",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "15.00",
            "authorizedAmount": "15.00",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "004"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "DI",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "004"
        },
        "card": {
            "type": "004"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F2701409F3501259F36020001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "033735",
        "approvalCode": "378857",
        "cardReferenceData": "05",
        "networktransactionId": "VISJ      303226531251404",
        "retrievalReferenceNumber": "322614033735",
        "consumerAuthenticationResponse": {
            "code": "0",
            "codeRaw": "0"
        },
        "transactionId": "VISJ      303226531251404",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "6920243246666458104951",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-08-14T14:45:26Z"
} 
```

Visa Deferred Sale with EMV Data {#um-processing-sale-deferred-intro}
=====================================================================

Use this information to process a deferred sale transaction at the end of the travel period for an aggregated payment.

Response Field Handling
-----------------------

When you receive the `AUTH_DECLINE_CAPTURE_POSSIBLE` value in the errorInformation.reason field of an authorization response, it indicates that a capture attempt will not be rejected automatically. Before processing the capture, verify that it is permitted in this scenario by reviewing the card scheme's First Ride Risk and shared‑liability rules.  
For an example of the field data, see the response in [REST Example: Visa Deferred Sale with EMV Data](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-sale-deferred-intro/um-processing-sale-deferred-ex-rest.md ""). For more information about the field, see the [errorInformation.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/error-info-aa/error-info-reason.md "") field description.

Endpoint {#um-processing-sale-deferred-intro_d7e16}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-sale-deferred-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-sale-deferred-intro_d7e35}

Required Fields for a Visa Deferred Sale with EMV Data {#um-processing-sale-deferred-reqd-fields}
=================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `TransitDA BAU full value sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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
Set the value to `001`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set the value to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set the value to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set the value to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set the value to `true`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set the value to `transit`.

REST Example: Visa Deferred Sale with EMV Data {#um-processing-sale-deferred-ex-rest}
=====================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA BAU full value sale",
        "code": "10000565",
        "transactionId": "20000565",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "processingInformation.commerceIndicator": "retail",
        "capture": "true",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "authorizationOptions": {
            "deferredAuthIndicator": "true",
            "aggregatedAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0",
        "emv": {
            "tags": "5F2A0209768407A00000000310109F360200029F03060000000000009C01005F3401019F10201F220100A00000000000000000000000000000000000000000000000000000009F33030008089A032204259F260845E978CEEC63154F9F2701409F0206000000000200820220209F34031F00009F1A0209769F6E04207000009F3704B257DA1495050000000000",
            "cardSequenceNumber": "1"
        },
        "trackData": ";4761XXXXXXXXXXXX=241220119058254?"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6508875814676551204001/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508875814676551204001"
        }
    },
    "clientReferenceInformation": {
        "code": "10000565",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000565"
    },
    "id": "6508875814676551204001",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "authorizedAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
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
        "systemTraceAuditNumber": "164186",
        "approvalCode": "831000",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511164186",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "6508875814676551204001",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-04-25T11:53:01Z"
}
```

Response to a Declined Request with First Ride Protection

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508878333386555704002"
        }
    },
    "clientReferenceInformation": {
        "code": "10000576",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000576"
    },
    "errorInformation": {
        "reason": "AUTH_DECLINE_CAPTURE_POSSIBLE",
        "message": "Authorization Declined. Follow-on Capture can be processed."
    },
    "id": "6508878333386555704002",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "164212",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511164212",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "DECLINED"
}
```

Required Fields for Authorizations for Debt Recovery {#mt-auth-dr-fields-matrix}
================================================================================

This table provides information about the fields required for tap-initiated and merchant-initiated (MIT) authorizations for debt recovery.

| REST API Field                                                                                                                                                                                                                                                               |                                                  Tap-Initiated                                                  |                                                       MIT                                                       | Information/Value                                                                                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")                                                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. partner. solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")                                                                   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                                                              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")                                                                                        |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")                                                                                       |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")                                                                                                 |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")                                                                                                    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")                                                                                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `2`.                                                                                                                                                                                        |
| [pointOfSaleInformation.emv. cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")                                                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `1`.                                                                                                                                                                                        |
| [pointOfSaleInformation.emv. tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")                                                                                                           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")                                                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `contactless`.                                                                                                                                                                              |
| [pointOfSaleInformation. terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")                                                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `5`.                                                                                                                                                                                        |
| [pointOfSaleInformation. terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")                                                                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")                                                                               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `0`.                                                                                                                                                                                        |
| [pointOfSaleInformation. trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")                                                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")                                                |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")                                                  |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions.initiator. credentialStoredOnFile](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")                                  |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `false`.                                                                                                                                                                                    |
| [processingInformation. authorizationOptions. initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "") |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. initiator.merchantInitiatedTransaction. reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")             |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `1`.                                                                                                                                                                                        |
| [processingInformation. authorizationOptions. initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")                                |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")                                                   |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `merchant`.                                                                                                                                                                                 |
| [processingInformation. captureOptions. dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [processingInformation. commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")                                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `retail`.                                                                                                                                                                                   |
| [processingInformation. industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")                                                                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `transit`.                                                                                                                                                                                  |
[Required Fields for Mass Transit Authorizations for Debt Recovery]

Tap-Initiated Authorization for Debt Recovery with EMV Data {#um-processing-auth-debtrecov-intro}
=================================================================================================

Use this information to process a tap-initiated authorization for debt recovery. When a cardholder attempts to use a blocked card at the transit reader, create a new debt recovery authorization request using the chip data from the new tap, along with the fare amount of the previous declined authorization.

Endpoint {#um-processing-auth-debtrecov-intro_d7e16}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-auth-debtrecov-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-auth-debtrecov-intro_d7e35}

Required Fields for a Tap-Initiated Authorization for Debt Recovery with EMV Data {#um-processing-auth-debtrecov-reqd-fields}
=============================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery tap auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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
Set this field to `2`.

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this field to `1`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Tap-Initiated Authorization for Debt Recovery with EMV Data {#um-processing-auth-debtrecov-ex-rest}
=================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA Debt recovery tap auth",
        "code": "10000597",
        "transactionId": "20000597",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "commerceIndicator": "retail",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "deferredAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0",
        "emv": {
            "tags": "5F2A0209768407A00000000310109F360200029F03060000000000009C01005F3401019F10201F220100A00000000000000000000000000000000000000000000000000000009F33030008089A032204259F260845E978CEEC63154F9F2701409F0206000000000200820220209F34031F00009F1A0209769F6E04207000009F3704B257DA1495050000000000",
            "cardSequenceNumber": "1"
        },
        "trackData": ";476173XXXXXXXXXX=241220119058254?"
    }
}
```

Response to a Declined Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508883585936636904003"
        }
    },
    "clientReferenceInformation": {
        "code": "10000597",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000597"
    },
    "errorInformation": {
        "reason": "PROCESSOR_DECLINED",
        "message": "Decline - General decline of the card. No other information provided by the issuing bank."
    },
    "id": "6508883585936636904003",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "163648",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211512163648",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "DECLINED"
}
```

Merchant-Initiated Authorization for Debt Recovery with Stored Card Data {#um-processing-auth-mit-intro}
========================================================================================================

Use this information to process a merchant-initiated authorization for debt recovery with stored card data.

Endpoint {#um-processing-auth-mit-intro_d7e16}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-auth-mit-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-auth-mit-intro_d7e35}

Required Fields for a Merchant-Initiated Authorization for Debt Recovery with Stored Card Data {#um-processing-auth-mit-reqd-fields}
====================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery MIT auth`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.initiator.credentialStoredOnFile](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")
:
Set this field to `false`.

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:
Set this field to `1`.

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set this field to `merchant`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `moto`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.
{#um-processing-auth-mit-reqd-fields_dl_ls1_4wf_pdc}

REST Example: Merchant-Initiated Authorization for Debt Recovery with Stored Card Data {#um-processing-auth-mit-ex-rest}
========================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA Debt recovery MIT auth",
        "code": "10000596",
        "transactionId": "20000596",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "commerceIndicator": "moto",
        "industryDataType": "transit",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "ignoreAvsResult": "true",
            "ignoreCvResult": "true",
            "initiator": {
                "type": "merchant",
                "credentialStoredOnFile": "false",
                "storedCredentialUsed": "true",
                "merchantInitiatedTransaction": {
                    "reason": "1",
                    "previousTransactionId": "016153570198200"
                }
            }
        }
    },
    "paymentInformation": {
        "card": {
            "number": "476173XXXXXXXXXX",
            "expirationMonth": "12",
            "expirationYear": "2024",
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    }
}
```

Response to a Declined Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508883374816631904001"
        }
    },
    "clientReferenceInformation": {
        "code": "10000596",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000596"
    },
    "errorInformation": {
        "reason": "PROCESSOR_DECLINED",
        "message": "Decline - General decline of the card. No other information provided by the issuing bank."
    },
    "id": "6508883374816631904001",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "164869",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211512164869",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "1"
        }
    },
    "status": "DECLINED"
}
```

Required Fields for a Sale for Debt Recovery {#mt-sale-dr-fields-matrix}
========================================================================

This table provides information about the fields required for tap-initiated and merchant-initiated (MIT) sales for debt recovery.

| REST API Field                                                                                                                                                                                                                                                               |                                                       Tap                                                       |                                                       MIT                                                       | Information/Value                                                                                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")                                                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. partner. solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")                                                                   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                                                              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")                                                                                        |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")                                                                                       |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")                                                                                                 |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")                                                                                                    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [paymentInformation. initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")                                                                                    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `00`.                                                                                                                                                                                       |
| [pointOfSaleInformation. catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")                                                                                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `2`.                                                                                                                                                                                        |
| [pointOfSaleInformation.emv. tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")                                                                                                           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")                                                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `contactless`.                                                                                                                                                                              |
| [pointOfSaleInformation.serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")                                                                                                     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")                                                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `5`.                                                                                                                                                                                        |
| [pointOfSaleInformation. terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")                                                                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [pointOfSaleInformation. terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")                                                                               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `0`.                                                                                                                                                                                        |
| [pointOfSaleInformation. trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")                                                                                                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")                                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `1`.                                                                                                                                                                                        |
| [processingInformation. authorizationOptions. debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | Set this field to `true`. Do not include for Mastercard transactions.                                                                                                                                         |
| [processingInformation. authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")                                                |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")                                                  |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "") |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. authorizationOptions. initiator.merchantInitiatedTransaction. reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")             |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `1`.                                                                                                                                                                                        |
| [processingInformation. authorizationOptions. initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")                                |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. authorizationOptions. initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")                                                   |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `merchant`.                                                                                                                                                                                 |
| [processingInformation. authorizationOptions. transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")                                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [processingInformation. capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")                                                                                              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `true`.                                                                                                                                                                                     |
| [processingInformation. captureOptions. dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")                                                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [processingInformation. commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")                                                                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For tap-initiated, set this field to `retail`. For merchant-initiated, set this field to `moto`.                                                                                                              |
| [processingInformation. industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")                                                                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to `transit`.                                                                                                                                                                                  |
[Required Fields for Mass Transit Sales for Debt Recovery]

Tap-Initiated Sale for Mastercard Debt Recovery with EMV Data {#um-processing-sale-debtrecov-intro}
===================================================================================================

Use this information to process a tap-initiated sale for Mastercard debt recovery When a cardholder attempts to use a blocked card at the transit reader, create a new debt recovery sale request using the chip data from the new tap, along with the fare amount of the previous declined authorization.

Endpoint {#um-processing-sale-debtrecov-intro_d7e16}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-sale-debtrecov-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-sale-debtrecov-intro_d7e35}

Required Fields for a Tap-Initiated Sale for Mastercard Debt Recovery with EMV Data {#um-processing-sale-debtrecov-mc-eu-reqd-fields}
=====================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery tap sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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

[paymentInformation.initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")
:
Set this field to `00`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set this field to `1`.

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Tap-Initiated Sale for Mastercard Debt Recovery with EMV Data {#um-processing-sale-debtrecov-mc-ex-rest}
======================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA Debt recovery tap sale",
        "code": "10000575MC",
        "transactionId": "20000575MC",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "commerceIndicator": "retail",
        "capture": "true",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "authorizationOptions": {
            "authIndicator": "1",
            "debtRecoveryIndicator": "true",
            "transportationMode": "00"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "002"
        },
        "initiationChannel": "00"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0", 
        "emv": {
            "tags": "5F2A0209768407A00000000410109F360200039F03060000000000009C01005F3401019F10120110A0000F040000000000000000000000FF9F33030008C89A032204259F2608093A260A58500E949F2701809F020600000000010082021B809F34033F00029F1A0209769F37046F4D8104950500200000019F6E06005601023030"
        },
        "trackData": ";5413XXXXXXXXXXXX=49122010123456789?",
        "serviceCode": "201"
    }
}
```

Response to a Declined Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/650887802747651300400"
        }
    },
    "clientReferenceInformation": {
        "code": "10000575MC",
        "partner": {
           "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000575MC"
    },
    "errorInformation": {
        "reason": "PROCESSOR_DECLINED",
        "message": "Decline - General decline of the card. No other information provided by the issuing bank."
    },
    "id": "650887802747651300400",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "162956",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511162956",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "DECLINED"
}
```

Tap-Initiated Sale for Visa Debt Recovery with EMV Data {#um-processing-sale-debtrecov-intro-visa}
==================================================================================================

Use this information to process a tap-initiated sale for Visa debt recovery. When a cardholder attempts to use a blocked card at the transit reader, create a new debt recovery sale request using the chip data from the new tap, along with the fare amount of the previous declined authorization.

Endpoint {#um-processing-sale-debtrecov-intro-visa_d7e16}
---------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-sale-debtrecov-intro-visa_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-sale-debtrecov-intro-visa_d7e35}

Required Fields for a Tap-Initiated Sale for Visa Debt Recovery with EMV Data {#um-processing-sale-debtrecov-reqd-fields}
=========================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery tap sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

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

[paymentInformation.initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")
:
Set this field to `00`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.emv.tags](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.serviceCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-service-code.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[pointOfSaleInformation.trackData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set this field to `1`.

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Tap-Initiated Sale for Visa Debt Recovery with EMV Data {#um-processing-sale-debtrecov-ex-rest}
=============================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "TransitDA Debt recovery tap sale",
        "code": "10000575",
        "transactionId": "20000575",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "commerceIndicator": "retail",
        "capture": "true",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "authorizationOptions": {
            "authIndicator": "1",
            "debtRecoveryIndicator": "true",
            "deferredAuthIndicator": "true",
            "transportationMode": "00"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        },
        "initiationChannel": "00"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0", 
        "emv": {
            "tags": "5F2A0209768407A00000000410109F360200039F03060000000000009C01005F3401019F10120110A0000F040000000000000000000000FF9F33030008C89A032204259F2608093A260A58500E949F2701809F020600000000010082021B809F34033F00029F1A0209769F37046F4D8104950500200000019F6E06005601023030"
        },
        "trackData": ";4413XXXXXXXXXXXX=49122010123456789?",
        "serviceCode": "201"
    }
}
```

Response to a Declined Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6508878027476513004004"
        }
    },
    "clientReferenceInformation": {
        "code": "10000575",
        "partner": {
           "solutionId": "548UHQ8Z"
        },
        "transactionId": "20000575"
    },
    "errorInformation": {
        "reason": "PROCESSOR_DECLINED",
        "message": "Decline - General decline of the card. No other information provided by the issuing bank."
    },
    "id": "6508878027476513004004",
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020015910AB58D60185BEF0247303072179F180430303031860E04DA9F580903B1BAEDFD1438BA48"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "162956",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "211511162956",
        "transactionId": "016153570198200",
        "responseCode": "05",
        "avs": {
            "code": "2"
        }
    },
    "status": "DECLINED"
}
```

Merchant-Initiated Sale for Discover Debt Recovery with Card Data {#mt-discover-mit-debtrecov-sale-intro}
=========================================================================================================

Use this information to process a merchant-initiated sale for Discover debt recovery with card data.

Endpoint {#mt-discover-mit-debtrecov-sale-intro_d7e16}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#mt-discover-mit-debtrecov-sale-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#mt-discover-mit-debtrecov-sale-intro_d7e35}

Required Fields for a Merchant-Initiated Sale for Discover Debt Recovery with Card Data {#mt-discover-mit-debtrecov-sale-reqfields}
===================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `MIT Debt recovery for Discover`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.
{#mt-discover-mit-debtrecov-sale-reqfields_dl_hy5_wxf_pdc}

REST Example: Merchant-Initiated Sale for Discover Debt Recovery with Card Data {#mt-discover-mit-debtrecov-sale-api-ex-rest}
=============================================================================================================================

Request

```
{
	"clientReferenceInformation": {
		"code": "123456",
		"comments": "MIT Debt recovery for Discover",
		"transactionId": "1581515492",
		"partner": {
			"solutionId": "123456",
			"thirdPartyCertificationNumber": "123456789012"
		}
	},
	"processingInformation": {
		"reconciliationId": "6514890316826935604951",
		"commerceIndicator": "moto",
		"industryDataType": "transit",
		"capture": "true",
		"authorizationOptions": {
			"partialAuthIndicator": "false",
			"deferredAuthIndicator": "false",
			"aggregatedAuthIndicator": "false",
			"debtRecoveryIndicator": "true",
			"ignoreAvsResult": "true",
			"ignoreCvResult": "true"
		}
	},
	"initiator": {
		"merchantInitiatedTransaction": {
			"previousTransactionId": "305128510901924"
		}
	},
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "16.00",
			"currency": "USD"
		}
	},
	"paymentInformation": {
		"card": {
			"type": "004",
			"number": "6510000000000810",
			"expirationYear": "2023",
			"expirationMonth": "12"
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
			"href": "/pts/v2/payments/7467135408716514904807/voids"
		},
		"self": {
			"method": "GET",
			"href": "/pts/v2/payments/7467135408716514904807"
		}
	},
	"clientReferenceInformation": {
		"code": "123456",
		"comments": "MIT Debt recovery  for Discover",
		"partner": {
			"solutionId": "123456"
		},
		"transactionId": "1581515492"
	},
	"id": "7467135408716514904807",
	"orderInformation": {
		"amountDetails": {
			"totalAmount": "16.00",
			"authorizedAmount": "16.00",
			"currency": "USD"
		}
	},
	"paymentAccountInformation": {
		"card": {
			"type": "004"
		}
	},
	"paymentInformation": {
		"accountFeatures": {
			"category": "DI",
			"group": "0"
		},
		"tokenizedCard": {
			"type": "004"
		},
		"card": {
			"type": "004"
		}
	},
	"processorInformation": {
		"systemTraceAuditNumber": "039454",
		"approvalCode": "842703",
		"cardReferenceData": "00",
		"networkTransactionId": "VISJ      305128511412635",
		"settlementDate": "5138",
		"retrievalReferenceNumber": "512814039454",
		"consumerAuthenticationResponse": {
			"code": "0",
			"codeRaw": "0"
		},
		"transactionId": "VISJ      305128511412635",
		"responseCode": "00",
		"avs": {
			"code": "1"
		}
	},
	"reconciliationId": "7467135408716514904807",
	"status": "AUTHORIZED",
	"submitTimeUtc": "2025-05-08T14:12:21Z",
	"tokenInformation": {
		"additionalInformation": "0"
	}
}
```

Merchant-Initiated Sale for Mastercard Debt Recovery with Card Data {#mt-mc-mit-debtrecov-sale-intro}
=====================================================================================================

Use this information to process a merchant-initiated sale for debt recovery using card data.

Endpoint {#mt-mc-mit-debtrecov-sale-intro_d7e16}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#mt-mc-mit-debtrecov-sale-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#mt-mc-mit-debtrecov-sale-intro_d7e35}

Required Fields for a Merchant-Initiated Sale for Mastercard Debt Recovery with Card Data {#mt-mc-mit-debtrecov-sale-reqfields}
===============================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery MIT sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set this field to `1`.

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:
Set this field to `true`.

[processingInformation. authorizationOptions.partialAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-partial-auth-ind.md "")
:
Set this field to `false`.

[processingInformation.authorizationOptions.transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `moto`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.linkId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-link-id.md "")
:
{#mt-mc-mit-debtrecov-sale-reqfields_dl_hy5_wxf_pdc}

REST Example: Merchant-Initiated Sale for Mastercard Debt Recovery with Card Data {#mt-mc-mit-debtrecov-sale-ex-rest}
=====================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "comments": "TransitDA Debt recovery MIT sale",
    "code": "12345678",
    "transactionId": "11111111",
    "partner": {
      "thirdPartyCertificationNumber": "Test1234",
      "solutionId": "Test1234"
    }
  },
  "processingInformation": {
    "linkId": "7781511099196451104806",
    "capture": "true",
    "commerceIndicator": "moto",
    "industryDataType": "transit",
    "authorizationOptions": {
      "authIndicator": "1",
      "debtRecoveryIndicator": true,
      "partialAuthIndicator": false,
      "ignoreAvsResult": true,
      "ignoreCvResult": true,
      "transportationMode": "00"
    }
  },
  "paymentInformation": {
    "card": {
      "number": "5454545454545454",
      "expirationMonth": "12",
      "expirationYear": "2030",
      "type": "002"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "3.00",
      "currency": "EUR"
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
      "href": "/pts/v2/payments/7799475532416439004807/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7799475532416439004807"
    }
  },
  "clientReferenceInformation": {
    "code": "12345678",
    "comments": "TransitDA Debt recovery MIT sale",
    "partner": {
      "solutionId": "Test1234"
    },
    "transactionId": "2309146064"
  },
  "id": "7799475532416439004807",
  "issuerInformation": {
    "clearingData": "6700040102F0F1"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "3.00",
      "authorizedAmount": "3.00",
      "currency": "EUR"
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
  "processorInformation": {
    "systemTraceAuditNumber": "051520",
    "merchantNumber": "123456789012345",
    "approvalCode": "300664",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "0528MCC269181",
    "retrievalReferenceNumber": "614705051520",
    "consumerAuthenticationResponse": {
      "code": "2",
      "codeRaw": "2"
    },
    "transactionId": "0528MCC269181",
    "responseCode": "00",
    "avs": {
      "code": "1"
    }
  },
  "reconciliationId": "7799475532416439004807",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2026-05-28T05:52:33Z"
}
```

Merchant-Initiated Sale for Visa Debt Recovery with Stored Card Data {#um-processing-sale-mit-intro}
====================================================================================================

Use this information to process a merchant-initiated sale for debt recovery using stored card data.

Endpoint {#um-processing-sale-mit-intro_d7e16}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#um-processing-sale-mit-intro_d7e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#um-processing-sale-mit-intro_d7e35}

Required Fields for a Merchant-Initiated Sale for Visa Debt Recovery with Stored Card Data {#um-processing-sale-mit-reqd-fields}
================================================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `TransitDA Debt recovery MIT sale`.

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Cybersource` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.initiator.credentialStoredOnFile](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")
:
Set this field to `false`.

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:
Set this field to `1`.

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-cof.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set this field to `merchant`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `moto`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.
{#um-processing-sale-mit-reqd-fields_dl_hy5_wxf_pdc}

REST Example: Merchant-Initiated Sale for Visa Debt Recovery with Stored Card Data {#um-processing-sale-mit-ex-rest}
====================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "comments": "TransitDA Debt recovery MIT sale",
    "code": "11111111",
    "transactionId": "11111113",
    "partner": {
      "thirdPartyCertificationNumber": "ABC1234",
      "solutionId": "ABC1234"
    }
  },
  "merchantInformation": {
    "transactionLocalDateTime": "20260529101200"
  },
  "processingInformation": {
    "capture": "true",
    "commerceIndicator": "moto",
    "industryDataType": "transit",
    "authorizationOptions": {
      "debtRecoveryIndicator": "true",
      "ignoreAvsResult": "true",
      "ignoreCvResult": "true",
      "initiator": {
        "type": "merchant",
        "credentialStoredOnFile": "false",
        "storedCredentialUsed": "true",
        "merchantInitiatedTransaction": {
          "reason": "1",
          "previousTransactionId": "016153570198200"
        }
      }
    }
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2049",
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "3.00",
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
      "href": "/pts/v2/payments/7800495209556343503814/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7800495209556343503814"
    }
  },
  "clientReferenceInformation": {
    "code": "11111111",
    "comments": "TransitDA Debt recovery MIT sale",
    "partner": {
      "solutionId": "ABC1234"
    },
    "transactionId": "6194022212"
  },
  "id": "7800495209556343503814",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "3.00",
      "authorizedAmount": "3.00",
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
    "systemTraceAuditNumber": "148603",
    "merchantNumber": "123456789012345",
    "approvalCode": "291735",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "614910148603",
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "1"
    }
  },
  "reconciliationId": "7800495209556343503814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2026-05-29T10:12:01Z"
}
```

Mass Transit Payment Services Using TMS Tokens {#um-processing-tms}
===================================================================

Use TMS tokens to request these mass transit payment services:

* Authorization for account verification and debt recovery

* Sale for aggregated fares and debt recovery

* Stand-alone credit  
  In card-present EMV contactless requests, include the transient token ID in the tokenInformation.jti field in place of track 2 data.  
  When submitting a tap token creation request, you can include EMV tag-length-value (TLV) tags in the paymentInformation.fluidData.value field or as part of the payment transaction request within the pointOfSaleInformation.emv.tags field.  
  If you send EMV tags in the tap token create request, do not send EMV tags in the payment transaction request.  
  When EMV TLV tags are present in both the payment transaction and the token vault, `Cybersource` reads the value provided in the payment transaction rather than the values stored in the vault.  
  Mastercard EMV transactions include these three field values, which can be handled automatically:

* paymentInformation.card.initiationChannel

* pointOfSaleInformation.emv.cardSequenceNumber

* pointOfSaleInformation.serviceCode  
  Your account can be configured to read these values automatically from the EMV TLV tags and track 2 equivalent. When that option is enabled, do not include those three fields in EMV payment requests.  
  If any of these values are present in both the separate fields and the EMV TLV and track 2 equivalent, `Cybersource` reads the value provided in the separate fields rather than the values present in the EMV TLV and track 2 equivalent.

#### Figure:

Payment Processing with a Token Workflow  
![Diagram showing Payment Processing with a Token workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/mtt-backoffice-390x290.svg/jcr:content/renditions/original)

Mastercard Authorization with a Token {#um-processing-mc-auth-tkn-intro}
========================================================================

Use this information to process an authorization with a token.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Mastercard Authorization with a Token {#um-processing-mc-auth-tkn-reqd-fields}
====================================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
The value for this field is provided by `Cybersource`.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
The value for this field is provided by `Cybersource`.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.initiationChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-initiation-channel.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.authIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-auth-ind.md "")
:
Set this field to `0`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.transportationMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transportation-mode.md "")
:

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:
Generate this value using the UUID2/UUID4 data format.

REST Example: Mastercard Authorization with a Token {#um-processing-mc-auth-tkn-ex-rest}
========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "10000721",
        "transactionId": "987654321",
        "partner": {
            "thirdPartyCertificationNumber": "BPCDRC220403",
            "solutionId": "548UHQ8Z"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "processingInformation.commerceIndicator" : "retail",
        "captureOptions": {
            "dateToCapture": "0425"
        },
        "authorizationOptions": {
            "authIndicator": "0",
            "deferredAuthIndicator": "true",
            "aggregatedAuthIndicator": "true",
            "transportationMode": "00"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "initiationChannel": "00"
    },
    "tokenInformation": {
        "jti": "a76392f4-cde4-97aa-1112-0242ac14c005"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/64823013154065933040011/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6482301315406593304011"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6482301315406593304011/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "10000721",
        "partner": {
            "solutionId": "548UHQ8Z"
        },
        "transactionId": "987654321"
    },
    "id": "6482301315406593304011",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "type": "002"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "191316",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networktransactionId": "016153570198201",
        "retrievalReferenceNumber": "211511164721",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198201",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "6482301315406593304011",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-03-25T17:42:11Z"
}
```

Visa Account Verification Request with a Token {#um-processing-visa-avr-tkn-intro}
==================================================================================

Use this information to process a zero-amount authorization for a mass transit Visa account verification request (AVR).

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Visa AVR Authorization with a Transient Token {#um-processing-visa-avr-tkn-reqd-fields}
=============================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
Set this field to `0.00`.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
Set this field to `001`.

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

REST Example: Visa AVR Authorization with a Transient Token {#um-processing-visa-avr-tkn-ex-rest}
=================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "5987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "processingInformation.commerceIndicator" : "retail",
        "reconciliationId": "asfafafafaffa"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "0.00",
            "currency": "THB"
        }
    },
    "tokenInformation": {
        "jti": "a76392f4-cde4-97aa-1112-0242ac14c005"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6482301315406593304003/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6482301315406593304003"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6482301315406593304003/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "5987654321"
    },
    "id": "6482301315406593304003",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "0.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "191316",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networktransactionId": "016153570198200",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "asfafafafaffa",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-03-25T17:42:11Z"
}
```

Visa Deferred Sale with a Token {#um-processing-sale-deferred-tkn-intro}
========================================================================

Use this information to process a Visa deferred sale.  
A sale transaction combines an authorization and capture. At the end of the travel period, request a Visa deferred sale with a token for an aggregated payment.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Visa Deferred Sale with a Token {#um-processing-sale-deferred-tkn-reqd-fields}
====================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.catLevel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-cat-level.md "")
:
Set this field to `2`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[processingInformation.authorizationOptions.aggregatedAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-agg-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

REST Example: Visa Deferred Sale with a Token {#um-processing-sale-deferred-tkn-ex-rest}
========================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "21987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "reconciliationId": "fgssgsgsgsfg",
        "captureOptions": {
            "dateToCapture": "0325"
        },
        "capture": "true",
        "processingInformation.commerceIndicator" : "retail",
        "authorizationOptions": {
            "deferredAuthIndicator": "true",
            "aggregatedAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "300.00",
            "currency": "THB"
        }
    },
    "tokenInformation": {
        "jti": "a76392f4-cde4-97aa-1111-0242ac14c005"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6482303624466600104004/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6482303624466600104004"
        }
    },
    "clientReferenceInformation": {
        "code": "testcode1012",
        "transactionId": "21987654321"
    },
    "id": "6482303624466600104004",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "300.00",
            "authorizedAmount": "300.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "191328",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networktransactionId": "016153570198200",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "fgssgsgsgsfg",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-03-25T17:46:02Z"
}
```

Tap-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-debtrecov-tkn-intro}
====================================================================================================

Use this information to process a tap-initiated authorization for debt recovery with a token.  
When a cardholder attempts to use a blocked card at the transit reader, create a fresh debt recovery authorization request using the chip data from the new tap, along with the fare amount of the previous declined authorization.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Tap-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-debtrecov-tkn-reqd-fields}
================================================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

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
Set this field to `2`.

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contactless`.

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set this field to `5`.

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:
Set this field to `0`.

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

REST Example: Tap-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-debtrecov-tkn-ex-rest}
====================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "9987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "reconciliationId": "dsgfsgsgsfdsgf",
        "captureOptions": {
            "dateToCapture": "0114"
        },
        "processingInformation.commerceIndicator" : "retail",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "deferredAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "tokenInformation": {
        "jti": "a76392f4-cde4-97aa-1111-0242ac14c005"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6502823788756237404002/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6502823788756237404002"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6502823788756237404002/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "9987654321"
    },
    "id": "6502823788756237404002",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "5004564953419F26087C14E9BE1F1065094F07A0000000031010820220009F360203709F0702C0809F2701409F100706010A03902000950500000000009F3704DB6AD1679A032111145F3401019F1A0203809F33036008C89F34031F03029F3501259F02060000000000009F03060000000000005F2A0209789C01005F2D046974656E9F0607A00000000310108407A00000000310109F21031726589F6E04207000009F40052000000001DFFEC30A020100"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "115052",
        "approvalCode": "831000",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "210811115052",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "dsgfsgsgsfdsgf",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-04-18T11:46:19Z"
}
```

Merchant-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-mit-tkn-intro}
===================================================================================================

Use this information to process an authorization for a merchant-initiated debt recovery with a token.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Merchant-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-mit-tkn-reqd-fields}
===============================================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

REST Example: Merchant-Initiated Authorization for Debt Recovery with a Token {#um-processing-auth-mit-tkn-ex-rest}
===================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "29987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "processingInformation.commerceIndicator" : "moto",
        "industryDataType": "transit",
        "reconciliationId": "fgssgsgsgsfg",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "ignoreAvsResult": "true",
            "ignoreCvResult": "true",
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true",
                "merchantInitiatedTransaction": {
                    "reason": "1",
                    "previousTransactionId": "123456766012345"
                }
            }
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "type": "001"
        },
        "instrumentIdentifier": {
            "id": "CD616772D8355EA6E053AF598E0AE794"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "THB"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6482309374186627704003/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6482309374186627704003"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6482309374186627704003/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3",
        "transactionId": "29987654321"
    },
    "id": "6482309374186627704003",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "instrumentIdentifier": {
            "id": "CD616772D8355EA6E053AF598E0AE794",
            "state": "ACTIVE"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "5004564953419F26087C14E9BE1F1065094F07A0000000031010820220009F360203709F0702C0809F2701409F100706010A03902000950500000000009F3704DB6AD1679A032111145F3401019F1A0203809F33036008C89F34031F03029F3501259F02060000000000009F03060000000000005F2A0209789C01005F2D046974656E9F0607A00000000310108407A00000000310109F21031726589F6E04207000009F40052000000001DFFEC30A020100"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "191368",
        "approvalCode": "831000",
        "networktransactionId": "016153570198200",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "fgssgsgsgsfg",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-03-25T17:55:37Z"
}
```

Tap-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-debtrecov-tkn-intro}
===========================================================================================

Use this information to process a tap-initiated sale for debt recovery with a token.  
A sale transaction combines an authorization and capture. When a cardholder attempts to use a blocked card at the transit reader, create a fresh debt recovery sale request using the chip data from the new tap, along with the fare amount of the previous declined authorization.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Tap-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-debtrecov-tkn-reqd-fields}
=======================================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

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

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:

[pointOfSaleInformation.terminalCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.deferredAuthIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-deferred-auth-ind.md "")
:
Set this field to `true`.

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.captureOptions.dateToCapture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-date-to-capture.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `retail`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

[tokenInformation.jti](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

REST Example: Tap-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-debtrecov-tkn-ex-rest}
===========================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "12987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "industryDataType": "transit",
        "reconciliationId": "dsgfsgsgsfdsgf",
        "captureOptions": {
            "dateToCapture": "0114"
        },
        "capture": "true",
        "processingInformation.commerceIndicator" : "retail",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "deferredAuthIndicator": "true"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentInformation": {
        "card": {
            "type": "001"    
        }
    },
    "tokenInformation": {
        "jti": "a76392f4-cde4-97aa-1111-0242ac14c005"
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "catLevel": "2",
        "entryMode": "contactless",
        "terminalCapability": "5",
        "terminalPinCapability": "0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6502821914766725604006/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6502821914766725604006"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "12987654321"
    },
    "id": "6502821914766725604006",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "authorizedAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "5004564953419F26087C14E9BE1F1065094F07A0000000031010820220009F360203709F0702C0809F2701409F100706010A03902000950500000000009F3704DB6AD1679A032111145F3401019F1A0203809F33036008C89F34031F03029F3501259F02060000000000009F03060000000000005F2A0209789C01005F2D046974656E9F0607A00000000310108407A00000000310109F21031726589F6E04207000009F40052000000001DFFEC30A020100"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "114880",
        "approvalCode": "831000",
        "networktransactionId": "016153570198200",
        "retrievalReferenceNumber": "210811114880",
        "transactionId": "12987654321",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "dsgfsgsgsfdsgf",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-04-18T11:43:11Z"
}
```

Merchant-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-mit-tkn-intro}
==========================================================================================

Use this information to process a merchant-initiated sale for debt recovery with a token.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`

Required Fields for a Merchant-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-mit-tkn-reqd-fields}
======================================================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.cardType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[processingInformation.authorizationOptions.debtRecoveryIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-debt-recovery-ind.md "")
:
Set this field to `true`.

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction. previousTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:

[processingInformation.authorizationOptions.initiator.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set this field to `true`.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `moto`.

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

[processingInformation.reconciliationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:

REST Example: Merchant-Initiated Sale for Debt Recovery with a Token {#um-processing-sale-mit-tkn-ex-rest}
==========================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "26987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "processingInformation": {
        "commerceIndicator" : "moto",
        "industryDataType": "transit",
        "reconciliationId": "fgssgsgsgsfg",
        "capture": "true",
        "authorizationOptions": {
            "debtRecoveryIndicator": "true",
            "ignoreAvsResult": "true",
            "ignoreCvResult": "true",
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true",
                "merchantInitiatedTransaction": {
                    "reason": "1",
                    "previousTransactionId": "123456789012345"
                }
            }
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "cardType": "001"
        },
        "instrumentIdentifier": {
            "id": "CD616772D8355EA6E053AF598E0AE794"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "THB"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/6482305297396608504004/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6482305297396608504004"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3",
        "transactionId": "26987654321"
    },
    "id": "6482305297396608504004",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "authorizedAmount": "10.00",
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "instrumentIdentifier": {
            "id": "CD616772D8355EA6E053AF598E0AE794",
            "state": "ACTIVE"
        },
        "card": {
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "5004564953419F26087C14E9BE1F1065094F07A0000000031010820220009F360203709F0702C0809F2701409F100706010A03902000950500000000009F3704DB6AD1679A032111145F3401019F1A0203809F33036008C89F34031F03029F3501259F02060000000000009F03060000000000005F2A0209789C01005F2D046974656E9F0607A00000000310108407A00000000310109F21031726589F6E04207000009F40052000000001DFFEC30A020100"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "190723",
        "approvalCode": "831000",
        "networktransactionId": "016153570198200",
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "1"
        }
    },
    "reconciliationId": "fgssgsgsgsfg",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-03-25T17:48:50Z"
}
```

Mass Transit Follow-On Payment Services {#um-processing-followon}
=================================================================

The Mass Transit solution supports these follow-on transactions:

* Capture
* Authorization reversal
* Timeout reversal
* Timeout void

Required Fields for Mass Transit Captures {#mt-capture-fields-matrix}
=====================================================================

This table provides information about the fields required for mass transit captures.

| REST API Field                                                                                                                                                                                                                        |                                                     Capture                                                     | Information/Value                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "") | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
[Required Fields for Mass Transit Captures]

Capture {#um-processing-capture-intro}
======================================

Use this information to process a capture.  
When a transaction is below the threshold for First Ride Risk protection, use the capture service to capture funds from a declined authorization. For more information, see [First Ride Risk](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-intro-overview/um-workflow-first-ride-risk.md "").

Endpoint {#um-processing-capture-intro_d7e127}
----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#um-processing-capture-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#um-processing-capture-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for a Capture {#um-processing-capture-reqd-fields}
==================================================================

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
The value for this field is provided by `Cybersource`.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

REST Example: Capture {#um-processing-capture-ex-rest}
======================================================

Request

```
{
   "clientReferenceInformation": {
        "comments": "TransitDA BAU capture",
        "transactionId": "14987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
   "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "currency": "EUR"
    }
  }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/captures/6484688186356910704004/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/captures/6484688186356910704004"
        }
    },
    "clientReferenceInformation": {
        "comments": "capture",
        "code": "testcode1012",
        "transactionId": "14987654321"
    },
    "id": "6484688186356910704004",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "10.00",
            "currency": "EUR"
        }
    },
    "reconciliationId": "fgssgsgsgsfg",
    "status": "PENDING",
    "submitTimeUtc": "2022-03-28T12:00:18Z"
}
```

Required Fields for Mass Transit Reversals {#mt-reversal-fields-matrix}
=======================================================================

This table provides information about the fields required for mass transit reversals.

| REST API Field                                                                                                                                                                                                                        |                                             Authorization Reversal                                              |                                                Timeout Reversal                                                 | Information/Value                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")                                                  | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. partner. thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "") | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Cybersource` provides the value for this field.                                                                                                                                                              |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")                                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                       ---                                                       | ---                                                                                                                                                                                                           |
| [orderInformation. amountDetails. totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")                                 | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
| [reversalInformation. reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-reason.md "")                                                                 |                                                       ---                                                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ---                                                                                                                                                                                                           |
[Required Fields for Mass Transit Reversals]

Authorization Reversal {#um-processing-rev-intro}
=================================================

Use this information to reverse an unnecessary authorization.

Endpoint {#um-processing-rev-intro_d7e85}
-----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#um-processing-rev-intro_d7e94}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#um-processing-rev-intro_d7e107}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for an Authorization Reversal {#um-processing-rev-reqd-fields}
==============================================================================

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[reversalInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-currency.md "")
:

[reversalInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-total-amount.md "")
:

REST Example: Authorization Reversal {#um-processing-rev-ex-rest}
=================================================================

Request

```
{
    "clientReferenceInformation": {
        "comments": "REVERSAL Timeout",
        "transactionId": "11987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "reversalInformation": {
        "amountDetails": {
            "totalAmount": "300.00",
            "currency": "EUR"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/reversals/6484678664766823004004"
        }
    },
    "clientReferenceInformation": {
        "code": "123456",
        "transactionId": "11987654321"
    },
    "id": "6484678664766823004004",
    "orderInformation": {
        "amountDetails": {
            "currency": "EUR"
        }
    },
    "processorInformation": {
        "responseDetails": "ABC",
        "responseCode": "00"
    },
    "reconciliationId": "6484678664766823004004",
    "reversalAmountDetails": {
        "reversedAmount": "300.00",
        "currency": "EUR"
    },
    "status": "REVERSED",
    "submitTimeUtc": "2022-03-28T11:44:26Z"
}
```

Time-Out Authorization Reversal {#um-processing-timeout-rev-intro}
==================================================================

Use this information to reverse an authorization that is not completed within the time allowed and times out.
**Production:** `POST ``https://api.cybersource.com``/pts/v2/reversals`{#um-processing-timeout-rev-intro_d7e565}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/reversals`{#um-processing-timeout-rev-intro_d7e575}

Required Fields for a Time-Out Authorization Reversal {#um-processing-timeout-rev-reqd-fields}
==============================================================================================

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `REVERSAL Timeout`.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[reversalInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-total-amount.md "")
:

[reversalInformation.reason](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-total-amount.md "")
:

REST Example: Time-Out Authorization Reversal {#um-processing-timeout-rev-ex-rest}
==================================================================================

Request

```
{
  "clientReferenceInformation": {
    "comments": "REVERSAL Timeout",
    "transactionId": "78885555"
  },
  "reversalInformation": {
    "amountDetails": {
      "totalAmount": "10.00"
    },
    "reason": "testing"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "method": "GET",
      "href": "/pts/v2/reversals/6502854707106431104004"
    }
  },
  "clientReferenceInformation": {
    "code": "1650285470690",
    "transactionId": "78885555"
  },
  "id": "6502854707106431104004",
  "orderInformation": {
    "amountDetails": {
      "currency": "EUR"
    }
  },
  "pointOfSaleInformation": {
    "emv": {
      "tags": "5004564953419F26087C14E9BE1F1065094F07A0000000031010820220009F360203709F0702C0809F2701409F100706010A03902000950500000000009F3704DB6AD1679A032111145F3401019F1A0203809F33030008089F34031F03029F3501259F02060000000000009F03060000000000005F2A0209789C01005F2D046974656E9F0607A00000000310108407A00000000310109F21031726589F6E04207000009F40052000000001DFFEC30A020100"
    }
  },
  "processorInformation": {
    "responseCode": "00"
  },
  "reconciliationId": "6502854707106431104004",
  "reversalAmountDetails": {
    "reversedAmount": "10.00",
    "currency": "EUR"
  },
  "status": "REVERSED",
  "submitTimeUtc": "2022-04-18T12:37:50Z"
}
```

Response to a Decline Request

```
{
  "id": "6502857670496139204005",
  "submitTimeUtc": "2022-04-18T12:42:47Z",
  "status": "INVALID_REQUEST",
  "reason": "INVALID_DATA",
  "message": "Declined - One or more fields in the request contains invalid data"
}
```

Stand-Alone Credit with a Token {#um-processing-credit-intro}
=============================================================

Use this information to process a stand-alone credit with a token.  
A *stand-alone credit* is a credit that is not linked to a previous transaction. When you process a stand-alone credit, there is no set limit on the amount because there is no reference to the original transaction amount. There is no time limit for requesting a stand-alone credit.
IMPORTANT Restrict access to the stand-alone credit service and do not make it available directly on your customer-facing interface. Instead, include the feature in your internal customer-service process to prevent misuse and make sure all requests are reviewed.  
When a stand-alone credit request is successful, the issuing bank for the payment card takes money out of the merchant bank account and returns it to the customer. It typically takes two to four days for the acquiring bank to transfer funds from the merchant bank account.

Endpoint {#um-processing-credit-intro_d7e169}
---------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/credits/`{#um-processing-credit-intro_d7e178}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/credits/`{#um-processing-credit-intro_d7e188}

Required Fields for a Stand-Alone Credit with a Token {#um-processing-credit-tkn-reqd-fields}
=============================================================================================

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

REST Example: Stand-Alone Credit with a Token {#um-processing-credit-tkn-vpc-ex-rest}
=====================================================================================

Request

```
{
    "clientReferenceInformation": {
        "transactionId": "43987654321",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "03",
            "expirationYear": "2031",
            "type": "001"
        },
        "instrumentIdentifier": {
            "id": "DCED1B858116F177E053AF598E0AA10A"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount"
: "200.00",
            "currency": "THB"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/credits/6502828338426145304001/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/credits/6502828338426145304001"
        }
    },
    "clientReferenceInformation": {
        "code": "12345678",
        "transactionId": "43987654321"
    },
    "creditAmountDetails": {
        "currency": "THB",
        "creditAmount": "200.00"
    },
    "id": "6502828338426145304001",
    "orderInformation": {
        "amountDetails": {
            "currency": "THB"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "instrumentIdentifier": {
            "id": "DCED1B858116F177E053AF598E0AA10A",
            "state": "ACTIVE"
        },
        "card": {
            "type": "001"
        }
    },
    "reconciliationId": "6502828338426145304001",
    "status": "PENDING",
    "submitTimeUtc": "2022-04-18T11:53:54Z"
}
```

Required Field for Timeout Voids {#mt-void-fields-matrix}
=========================================================

This table provides information about the field required for timeout voids.

| REST API Field                                                                                                                                                                                  |                                                  Timeout Void                                                   | Information/Value                                                                                                                                                                                             |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientReferenceInformation. comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | For this value, see [Mass Transit Transaction Types](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-processing-emv-vpc/um-processing-trxn-types.md ""). |
| [clientReferenceInformation. transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "") | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Set this field to the unique clientReferenceInformation.transactionId value from the transaction that timed out.                                                                                              |
[Required Fields for Mass Transit Timeout Voids]

Time-Out Void {#um-processing-timeout-void-intro}
=================================================

Use this information to void an authorization, capture, refund, or credit when you do not receive a response within the time allowed and the transaction times out. Include a unique value in the clientReferenceInformation.transactionId field in your initial request and use the same unique value for the clientReferenceInformation.transactionId field in a request to reverse the transaction.

Endpoint {#um-processing-timeout-void-intro_d7e585}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/voids/`{#um-processing-timeout-void-intro_d7e594}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/voids/`{#um-processing-timeout-void-intro_d7e604}

Required Field for a Time-Out Void {#um-processing-timeout-void-reqd-fields}
============================================================================

[clientReferenceInformation.comments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set this field to `REVERSAL Timeout`.

[clientReferenceInformation.transactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

REST Example: Time-Out Void {#um-processing-timeout-void-ex-rest}
=================================================================

Request

```
{
  "clientReferenceInformation": {
    "comments": "VOID Timeout",
    "transactionId": "888858556"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "self": {
      "method": "GET",
      "href": "/pts/v2/voids/6502849034136438604002"
    }
  },
  "clientReferenceInformation": {
    "code": "1650284903396",
    "transactionId": "888858556"
  },
  "id": "6502849034136438604002",
  "orderInformation": {
    "amountDetails": {
      "currency": "EUR"
    }
  },
  "status": "VOIDED",
  "submitTimeUtc": "2022-04-18T12:28:23Z",
  "voidAmountDetails": {
    "currency": "EUR",
    "voidAmount": "10.00"
  }
}
```

Response to a Declined Request

```
{
  "id": "6502858209346457804004",
  "submitTimeUtc": "2022-04-18T12:43:41Z",
  "status": "INVALID_REQUEST",
  "reason": "INVALID_DATA",
  "message": "Declined - One or more fields in the request contains invalid data"
}
```

Mass Transit Token Management Services {#um-processing-token-intro}
===================================================================

Use the `Token Management Service` to create, retrieve, and delete tokens for mass transit.

Creating a Token {#um-processing-token-create-intro}
====================================================

Use this information to create tokens directly from the validator or through your back office system.  
When the customer taps their card, the validator generates a unique transaction identifier that is used to create these tokens:

* Transient token: tokenized EMV tag data and track2 data. Used as the transaction ID to create the instrument identifier and payment instrument tokens, and as the payment token for the final authorization and sale transactions. You can delete this token after a success transit payment for the travel period. `Cybersource` stores this token for 7 days.
* Instrument identifier: tokenized card number, used for follow-on payment transactions and BIN lookup.
* Payment instrument: stores the card hash that is used to identify the payment card in the deny list.
  {#um-processing-token-create-intro_ul_fsv_2db_j1c}

#### Figure: {#um-processing-token-create-intro_fig_uf5_w22_j3c}

Creating a Token Workflow  
![Diagram showing the Creating a Token workflow](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/mass-transit/images/mtt-create-token-390x430.svg/jcr:content/renditions/original)  
The token creation process begins when the when the cardholder taps a payment card at the fare collection terminal.

1. The cardholder taps their contactless card.
2. Regular local transit processing occurs. See [Mass Transit Models and Workflows](/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit/um-transit-models-flows-intro.md "").
3. The validator encrypts the card data and creates the card hash value.
4. Your system uses the card hash value to create the tokens.
5. You receive the tokens in the response message.

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/tms/v2/taps`{#um-processing-token-create-intro_restcust-test}  
**Production:** `POST ``https://api.cybersource.com``/tms/v2/taps`

Required Fields for Creating a Token {#um-processing-token-create-reqd-fields}
==============================================================================

[id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/id.md "")
:
Transient token identifier assigned by the contactless terminal.

[paymentInformation.card.hash](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-hashed-num.md "")
:

[paymentInformation.fluidData.descriptor](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-descriptor.md "")
:

[paymentInformation.fluidData.encoding](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-encoding.md "")
:

[paymentInformation.fluidData.value](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-value.md "")
:

[pointOfSaleInformation.deviceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-device-id.md "")
:

[processingInformation.industryDataType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set this field to `transit`.

REST Example: Create a Token {#um-processing-token-create-ex-rest}
==================================================================

Request

```
{
    "id": "a76392f4-cde4-97aa-1111-0252ac14c005",
    "paymentInformation": {
        "card": {
            "hash": "7400A4154369E584BA36CA19B50AAA3F9AE9764B3E87B2B93CF8FBC11112"
        },
        "fluidData": {
            "descriptor": "4649443D454D562E5041594D454E542E415049",
            "encoding": "Hex",
            "value": "DFEE120A8888885140001840000357189141DC75F996D2E930B9ADABE73 
5CBE80ECF17A263E94964F07A0000000031010500b4379626572736F7572
63655F2D02456E5F3401015F360102820220008407A00000000310109505
00000000009A032101199C01009F02060000000004009F03060000000000
009F030200019F1006A1B2C3D4E5F69F1A0208409F21031301255F2A0208
409F26080123456789ABCDEF9F2701409F33030000009F360200019F3501
259F3704123456789F390100"
        }
    },
    "pointOfSaleInformation": {
        "deviceId": "FF123457"
    },
    "processingInformation": {
        "industryDataType": "transit"
    }
}
```

Response 202

```
No body response 
```

Retrieving Transient Token Details {#um-processing-token-get-intro}
===================================================================

Use this information to retrieve transient token details, which include the instrument identifier token and payment instrument token.  
The payment instrument token is used for token management. The instrument identifier is used for these transactions:

* Merchant-initiated debt recovery
* Stand-alone credit
  {#um-processing-token-get-intro_ul_e35_pb3_rtb}

Endpoint
--------

**Test:** `POST ``https://apitest.cybersource.com``/tms/v2/taps/{id}`{#um-processing-token-get-intro_restcust-test}  
**Production:** `POST ``https://api.cybersource.com``/tms/v2/taps/{id}`

REST Example: Retrieve Transient Token Details {#um-processing-token-get-ex-rest}
=================================================================================

Request

```
{
}
```

{#um-processing-token-get-ex-rest_codeblock_hnh_lyg_lcc}  
Response 200

```
{
    "id": "a76392f4-cde4-97aa-1111-0252ac14c005",
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2030"
        }
    },
    "pointOfSaleInformation": {
        "deviceId": "FF123457",
        "emv": {
            "applicationIdentifier": "A0000000031010",
            "applicationLabel": "Company"
        }
    },
    "processingInformation": {
        "industryDataType": "transit"
    },
    "tokenInformation": {
        "instrumentIdentifier": {
            "id": "CD616772D8355EA6E53AF598E0AE794"
        },
        "paymentInstrument": {
            "id": "DB0875B76F95085CE053AF598E0A6354"
        }
    },
    "_links": {
        "self": {
            "href": "/tms/v2/taps/a76392f4-cde4-97aa-1111-0252ac14c005"
        },
        "paymentInstrument": {
            "href": "/tms/v1/paymentinstruments/DB0875B76F95085CE053AF598E0A6354"
        },
        "instrumentIdentifier": {
            "href": "/tms/v1/instrumentidentifiers/CD616772D835EA6E53AF598E0AE794"
        }
    }
}
```

Retrieving an Instrument Identifier Details {#um-processing-token-get-ii-intro}
===============================================================================

Use this information to retrieve instrument identifier details.

Endpoint
--------

**Test:** `GET ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers/{id}`  
**Production:** `GET ``https://api.cybersource.com``/tms/v1/instrumentidentifiers/{id}`  
The `id` is the instrument identifier ID that was returned in a token management service response.

```
    },
        "tokenInformation": {
            "instrumentIdentifier": {
                "id": "CD616772D8355EA6E053AF598E0AE794"
            },
```

REST Example: Retrieving Instrument Identifier Details {#um-processing-token-get-ii-ex-rest}
============================================================================================

Request

```
{
}
```

Response 200

```
{
    "_links": {
        "self": {
            "href": "https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794"
        },
        "paymentInstruments": {
            "href": "https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794/paymentinstruments"
        }
    },
    "id": "CD616772D8355EA6E053AF598E0AE794",
    "object": "instrumentIdentifier",
    "state": "ACTIVE",
    "card": {
        "number": "411111XXXXXXXXXX"
    },
    "processingInformation": {
        "authorizationOptions": {
            "initiator": {
                "merchantInitiatedTransaction": {
                    "previousTransactionId": "016153570198200"
                }
            }
        }
    }
}
```

Retrieving Card Hash Details {#um-processing-token-get-ii-pi-ch-intro}
======================================================================

Use this information to retrieve card hash details, which include the instrument identifier token and payment instrument token.

Endpoint
--------

**Test:** `GET ``https://apitest.cybersource.com``/tms/v1/paymentinstruments/{id}`  
**Production:** `GET ``https://api.cybersource.com``/tms/v1/paymentinstruments/{id}`  
The `id` is the transient token identifier assigned by the contactless terminal.

REST Example: Retrieving Card Hash Details {#um-processing-token-get-ii-pi-ch-ex-rest}
======================================================================================

Request

```
{
}
```

Response 200

```
{
    "_links": {
        "self": {
            "href": https://apitest.cybersource.com/tms/v1/paymentinstruments/CD98B27F62A8AECBE053AF598E0AF965
        }
    },
    "id": "CD98B27F62A8AECBE053AF598E0AF965",
    "object": "paymentInstrument",
    "state": "ACTIVE",
    "type": "cardHash",
    "card": {
        "expirationMonth": "12",
        "expirationYear": "2030",
        "type": "visa",
        "hash": "7400A4154369E584BA36CA19B50AAA3F9AE97FEAE64B3E87B2B93CF8FBC97777"
    },
    "metadata": {
        "creator": "tml_tap02"
    },
    "_embedded": {
        "instrumentIdentifier": {
            "_links": {
                "self": {
                    "href": https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794
                },
                "paymentInstruments": {
                    "href": https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794/paymentinstruments
                }
            },
            "id": "CD616772D8355EA6E053AF598E0AE794",
            "object": "instrumentIdentifier",
            "state": "ACTIVE",
            "card": {
                "number": "476173XXXXXXXXXX"
            },
            "processingInformation": {
                "authorizationOptions": {
                    "initiator": {
                        "merchantInitiatedTransaction": {
                            "previousTransactionId": "016153570198200"
                        }
                    }
                }
            },
            "metadata": {
                "creator": "tml_tap01"
            }
        }
    }
}
```

Retrieving Payment Instrument Details {#um-processing-token-get-pi-intro}
=========================================================================

Use this information to send a `GET` request to retrieve payment instrument details, which include the card details, card hash, and instrument identifier.

Endpoint
--------

**Test:** `GET ``https://apitest.cybersource.com``/tms/v1/paymentinstruments/{id}`  
**Production:** `GET ``https://api.cybersource.com``/tms/v1/paymentinstruments/{id}`  
The `id` is the transient token identifier assigned by the contactless terminal.

REST Example: Retrieving Payment Instrument Details {#um-processing-token-get-pi-ex-rest}
=========================================================================================

Request

```
{
}
```

Response 200

```
{
    "_links": {
        "self": {
            "href": https://apitest.cybersource.com/tms/v1/paymentinstruments/CD98B27F62A8AECBE053AF598E0AF965
        }
    },
    "id": "CD98B27F62A8AECBE053AF598E0AF965",
    "object": "paymentInstrument",
    "state": "ACTIVE",
    "type": "cardHash",
    "card": {
        "expirationMonth": "12",
        "expirationYear": "2030",
        "type": "visa",
        "hash": "7400A4154369E584BA36CA19B50AAA3F9AE97FEAE64B3E87B2B93CF8FBC97777"
    },
    "_embedded": {
        "instrumentIdentifier": {
            "_links": {
                "self": {
                    "href": https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794
                },
                "paymentInstruments": {
                    "href": https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD616772D8355EA6E053AF598E0AE794/paymentinstruments
                }
            },
            "id": "CD616772D8355EA6E053AF598E0AE794",
            "object": "instrumentIdentifier",
            "state": "ACTIVE",
            "card": {
                "number": "476173XXXXXXXXXX"
            },
            "processingInformation": {
                "authorizationOptions": {
                    "initiator": {
                        "merchantInitiatedTransaction": {
                            "previousTransactionId": "016153570198200"
                        }
                    }
                }
            }
        }
    }
}
```

Deleting an Instrument Identifier {#um-processing-token-delete-ii-intro}
========================================================================

Use this information to send a `DELETE` request to delete an instrument identifier.

Endpoint
--------

**Test:** `DELETE ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers/{id}`  
**Production:** `DELETE ``https://api.cybersource.com``/tms/v1/instrumentidentifiers/{id}`  
The `id` is the instrument identifier ID that was returned in a token management service response.

```
    },
        "tokenInformation": {
            "instrumentIdentifier": {
                "id": "CD616772D8355EA6E053AF598E0AE794"
            },
```

REST Example: Deleting an Instrument Identifier {#um-processing-token-delete-ii-ex-rest}
========================================================================================

Request

```
{
}
```

{#um-processing-token-delete-ii-ex-rest_codeblock_c5m_pyg_lcc}  
Response 204

```
No response body
```

Response 409

```
{
    "_links": {
        "paymentInstruments": {
            "href": "https://apitest.cybersource.com/tms/v1/instrumentidentifiers/CD776F4472D6AC69E053AF598E0A30F3/paymentinstruments"
        }
    },
    "errors": [
        {
            "type": "instrumentIdentifierDeletionError",
            "message": "Action cannot be performed as the InstrumentIdentifier is associated with one or more PaymentInstruments"
        }
    ]
}
```

Response 410: Deleting an Instrument Identifier

```
{
    "errors": [
        {
            "type": "notAvailable",
            "message": "Token not available"
        }
    ]
}
```

Deleting a Card Hash {#um-processing-token-delete-pi-ch-intro}
==============================================================

Use this information to send a `DELETE` request to delete a card hash.

Endpoint
--------

**Test:** `DELETE ``https://apitest.cybersource.com``/tms/v1/paymentinstruments/{id}`  
**Production:** `DELETE ``https://api.cybersource.com``/tms/v1/paymentinstruments/{id}`  
The `id` is the card.hash value that was returned in the retrieve a payment instrument response.

```
"card": {
    "expirationMonth": "12",
    "expirationYear": "2030",
    "type": "visa",
    "hash": "7400A4154369E584BA36CA19B50AAA3F9AE97FE93CF8FBC97777"
 }
```

{#um-processing-token-delete-pi-ch-intro_codeblock_nbz_cy5_31c}

REST Example: Deleting a Card Hash {#um-processing-token-delete-pi-ch-ex-rest}
==============================================================================

Request

```
{
}
```

{#um-processing-token-delete-pi-ch-ex-rest_codeblock_abg_nyg_lcc}  
Response 204: Deleting a Card Hash

```
No response body
```

Response 410: Deleting a Card Hash

```
{
    "errors": [
        {
            "type": "notAvailable",
            "message": "Token not available"
        }
    ]
}
```

