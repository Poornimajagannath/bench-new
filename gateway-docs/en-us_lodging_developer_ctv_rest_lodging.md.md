Card Present Connect \| Lodging Developer Guide {#lodging-about-guide}
======================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to integrate payment processing for lodging services. These services are available using the REST API.

    Implementing these services requires software development skills and knowledge of lodging payment practices. You must write code that uses the REST API request and response fields to integrate the payment services into your existing lodging payment system.

Related Documentation
:
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional processor-specific versions of this guide and additional technical documentation.
:
For `Token Management Service` documentation, see the [*Token Management Service Developer Guide*](https://developer.example.com/docs/gateway/en-us/tms/developer/ctv/rest/tms/tms-about-guide.md "").

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#lodging-doc-revisions}
==========================================================

26.05.01
--------

This revision contains only editorial changes and no technical updates.

25.06.01
--------

:
Removed processingInformation.industryDataType field from list of required fields and updated example REST request in [Incremental Authorization](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-payment-services/lodging-incremental-auth-task.md "").

25.02
-----

:
Added new section, [Lodging EMV and Card Data](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-payment-services/lodging-emv-card-data.md "").
:
Updated the list of limitation in [Incremental Authorization](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-payment-services/lodging-incremental-auth-task.md "").

25.01
-----

Initial pilot release.

Introduction to Card Present Connect \| Lodging {#lodging-intro}
================================================================

Card Present Connect \| Lodging is the `Payment Gateway` solution for processing lodging transactions. `Payment Gateway` lodging processing is based on the global standards established by the card schemes for reliable, scalable, and secure card-not-present transactions and contact and contactless EMV card-present transactions.

Supported Card Types {#lodging-card-types}
==========================================

These card types can be used to process lodging transactions:

* Mastercard
* Relay  
  PIN debit cards are supported in North America only and can be used to process sales transactions only. Other transaction types, such as refunds or pre-authorizations, are not supported on PIN debit cards.

Prerequisites {#lodging-prereqs}
================================

Before integrating `Payment Gateway` services for lodging transactions, you must have these items in place:

* Merchant account with an acquirer that is enabled for processing lodging transactions on `Platform Connect`.
* `Payment Gateway` account for payment services.
* Payment technology provider (PTP) that is integrated with `Payment Gateway` and can perform message-level validation (MLV).
* EMV Level 1 certified terminals and EMV Level 2 certified software in preparation for EMV Level 3 Certification.

Validation and Certification {#lodging-val-cert}
================================================

Work with your payment technology provider (PTP) to allocate time to complete the message-level validation (MLV) and EMV Level 3 certification with your lodging processing system. You must pass MLV before beginning EMV Level 3 certification. You must complete validation and certification before your system can go live. For more information, see [Prerequisites](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-intro/lodging-prereqs.md "").

Message-Level Validation {#lodging-mlv}
=======================================

Message-level validation (MLV) is a script-based field-level validation against `Payment Gateway` specifications.  
Your PTP uses amount-based test triggers to send transactions to a test environment and the Relay Certification Management System for decryption. The test results are XML or RESTful output, `Business Center` test transactions, and log prints.  
`Payment Gateway` uses these tests to validates the results:

* Cross edit checks
* Data element validation
* Interchange compliance
* Data mapping validation

EMV Level 3 Certification {#lodging-emvl3-cert}
===============================================

This topic is an overview of the Level 3 certification with `Payment Gateway` and `Platform Connect`. For details on how to design an EMV Level 3 certified payment application, see EMV Book 3 on the EMVCo website: <https://www.emvco.com>  
Certification is a formal process that is used to validate the device and application compliance with card scheme acceptance requirements. The certification team uses a brand test tool and simulator. The process involves these elements:

* Using a card simulator such as ICC or Fime.
* Failed case analysis and resolution.
* For Mastercard certification, your PTP submits results to Mastercard and pays the costs for approved partners that Mastercard uses.
* For Relay certification, `Payment Gateway` submits results to Relay.
* Waivers from the card schemes for exceptions.
* Card scheme responses or Letter of Approval (LOA) to signify acceptance and Level 3 certification.  
  The processes and support for Global Card Present Connect projects and direct merchant and acquirer projects are different, but the timelines are essentially the same.

Card-Present Transaction Risk Control Requirements {#cp-intro-transactions-risk-control}
========================================================================================

Card-present transactions carry lower risk than card-not-present transactions because the customer and payment card are physically present, which can result in lower transaction fees. However, acquirers must still apply standard risk-control measures. Acquirers must monitor transaction activity and manage fraud and disputes in accordance with payment network rules, including the Global Acquirer Risk Standards. They also must comply with these Relay risk compliance programs:

* Relay Fraud Monitoring Program

* Relay Dispute Monitoring Program
  {#cp-intro-transactions-risk-control_ul_gmj_31g_d3c} To meet risk control requirements, acquirers can use one of these options:

* Enable `Payment Gateway` transaction and fraud monitoring tools.

* Ensure that their payment technology partners (PTPs) implement transaction and fraud monitoring tools.

* Deploy their own transaction and fraud monitoring tools.

Each option provides necessary fraud and risk controls for direct merchant relationships and for PTPs that do not operate their own monitoring solutions. For more information, see [Fraud and Risk Management Solutions](https://www.example.com/en-us/solutions/fraud-and-risk-management.md "").

Lodging Transaction Scenarios {#lodging-trxn-types}
===================================================

This section describes the lodging transaction scenarios supported by `Payment Gateway`.

Check-In Transaction Scenario {#lodging-trxntype-checkin}
=========================================================

Check-in is a crucial step in the guest's journey, and it sets the tone for their entire stay. A smooth and efficient check-in process can make a positive impression on guests and encourage them to return to your property.

#### Figure: {#lodging-trxntype-checkin_fig-check-in}

Check-In Transaction Workflow ![Lodging check-in transaction workflow diagram showing the sequence of events
that occur during check-in.](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/lodging/images/1-cpc-ldg-checkin-600x265.svg/jcr:content/renditions/original)  
The lodging check-in transaction workflow typically includes this sequence of events:

1. The guest arrives and presents their identification and reservation information.
2. The front desk staff verifies the guest's reservation.
3. The front desk staff collects the guest's payment card.
4. The front desk staff inserts, swipes, or taps the guest's payment card or enters the payment information manually into their payment system. The authorization request sent to the processor includes the lodging fields.
5. The processor sends an authorization request to the issuing bank.
6. The issuing bank approves the transaction and sends an authorization response to the processor.
7. The payment technology provider (PTP) sends the authorization response to the lodging's property management system (PMS).
8. The PMS updates the guest's reservation with the payment information and generates a receipt.
9. The front desk staff gives the guest a room key and receipt.

Incremental Authorization Scenario {#lodging-trxntype-incr-auth}
================================================================

An incremental transaction is an additional authorization that increases the original amount of a transaction. The final authorized total combines the amounts from the initial and the incremental authorizations.  
This type of authorization is used to increase the total payment amount when the initial authorization is insufficient to cover the total cost of lodging and associated services.  
Lodging transactions comprise these types of incremental authorizations:

* Initial authorization: Upon reservation or check-in, the guest's payment card is pre-authorized for an estimated amount based on the initial reservation details and potential additional charges. The lodging staff obtains explicit consent from the guest to process the incremental authorizations when charges exceed the initial authorization.
* Additional charges: As the guest's stay progresses and additional charges are incurred, such as dining, spa treatments, or minibar consumption, the initial pre-authorization might become insufficient to cover the total amount due for payment. To ensure adequate coverage for the guest's expenses, the lodging staff initiates an incremental authorization request for an additional amount.  
  For examples of scenarios in which an incremental authorization could be used, see [Check-In Transaction Scenario](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-trxn-types/lodging-trxntype-checkin.md "") and [Check-Out Transaction Scenario](/docs/gateway/en-us/lodging/developer/ctv/rest/lodging/lodging-trxn-types/lodging-trxntype-checkout.md "").

Check-Out Transaction Scenario {#lodging-trxntype-checkout}
===========================================================

The check-out process begins when the guest indicates that they are checking out of the lodging.

#### Figure: {#lodging-trxntype-checkout_fig-check-out}

Check-Out Transaction Workflow ![Lodging check-out transaction workflow diagram showing the sequence of events
that occur during check-out.](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/lodging/images/2-cpc-ldg-checkout-600x160.svg/jcr:content/renditions/original)  
The lodging check-out transaction workflow typically includes this sequence of events:

1. The guest confirms they want to pay their bill using the stored payment method.
2. The lodging's system calculates the total amount due, including any remaining balance on the incremental authorization.
3. The lodging's payment system processes the transaction, communicating with the payment processor and the card issuer.
4. The lodging's payment system verifies the payment information, authorizes the transaction, and captures the funds.
5. The front desk staff gives the guest a paper receipt, which includes charges and payment information.
6. The lodging sends an electronic receipt or sends an email copy of the receipt to the guest (optional).

No-Show Transaction Scenario {#lodging-trxntype-noshow}
=======================================================

A no-show occurs when a guest makes a reservation but does not check in or cancel the reservation. No-show transactions are determined by the lodging's disclosed and agreed-upon cancellation policy.  
A lodging business can handle no-shows in several ways, including these options:

* Charging a no-show fee: This fee is charged to the guest's credit card if they do not cancel their reservation within a certain amount of time. The amount of the fee is typically based on the room rate and the length of the stay.
* Requiring a deposit: This is a payment that the guest is required to make upfront in order to secure their reservation. The deposit is typically refunded if the guest cancels their reservation by a certain date.

#### Figure: {#lodging-trxntype-noshow_fig-no-show}

No-Show Transaction Workflow ![Lodging no-show transaction workflow diagram showing the sequence of events
that take place when a no-show occurs.](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/lodging/images/3-cpc-ldg-no-show-600x160.svg/jcr:content/renditions/original)  
The no-show transaction workflow typically includes this sequence of events:

1. The guest makes a reservation online, by phone, or in person. At the time of booking, the guest provides their credit card information.
2. The lodging staff sends the guest a confirmation email or text message with the details of the reservation. The guest confirms their reservation by replying to the email or text message.
3. The guest does not check in or cancel their reservation by the time their reservation is scheduled to start, which is considered a no-show.
4. The lodging charges the guest a no-show fee using the same payment method the guest used to make the reservation. The amount of the fee is based on the lodging's no-show policy.

Lodging Payment Services {#lodging-payment-services}
====================================================

Use this information to process lodging transactions.

Lodging EMV and Card Data {#lodging-emv-card-data}
==================================================

You can request these payment services for lodging with EMV and card data:

* Authorization: standard and incremental

* Capture

* Stand-alone credit  
  This table shows the requirement for EMV tags using these categories:

* M: mandatory

* P: prohibited

* O: optional

* C: conditional (send tag when it is present in card and terminal)

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

Lodging Transaction Descriptions {#lodging-trxn-descr}
======================================================

Use the lodging transaction descriptions listed in the tables to help you identify types of request messages for production transactions in the `Business Center` and in your transaction reports. Include the clientReferenceInformation.comments field with a transaction description value when you submit a request.

> IMPORTANT  
> After you add this enhancement to your transaction requests, test the field before deploying it to production. This change does not affect your Level 3 or MLV status if you make no other changes.  
> If you want `Payment Gateway` to review your test environment result after you add the comments field, contact customer support.

|    Service    | Card Present (CP) or Card Not Present (CNP) | Comments Field Value |                                          Description                                           |
|---------------|---------------------------------------------|----------------------|------------------------------------------------------------------------------------------------|
| Authorization | CNP                                         | `Checkin Auth CNP`   | Authorization when the guest makes the reservation online or by phone.                         |
| Sale          | CNP                                         | `Checkin Sale CNP`   | Sale when the guest pays for the whole stay when they make the reservation online or by phone. |
| Authorization | CP                                          | `Checkin Auth CP`    | Authorization when the guest reserves their stay at check in.                                  |
| Sale          | CP                                          | `Checkin Sale CP`    | Sale when the guest pays for their stay and services at check in.                              |
[Check-In Transactions]

|          Service          | Card Present (CP) or Card Not Present (CNP) |  Comments Field Value  |               Description                |
|---------------------------|---------------------------------------------|------------------------|------------------------------------------|
| Incremental Authorization | CP                                          | `Incremental Auth CP`  | Incremental authorization in person.     |
| Incremental Authorization | CNP                                         | `Incremental Auth CNP` | Incremental authorization using a token. |
[Incremental Authorizations]

| Service | Card Present (CP) or Card Not Present (CNP) | Comments Field Value  |                                                                                         Description                                                                                         |
|---------|---------------------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Capture | CP                                          | `Checkout Capture CP` | Capture when the guest is checking out.                                                                                                                                                     |
| Sale    | CP                                          | `Checkout Sale CP`    | Sale when the guest already paid for their stay and needs to pay for additional services.                                                                                                   |
| Void    | CP                                          | `Checkout Void CP`    | Void the capture when the guest uses a different form of payment, such as cash. A transaction can be voided only when the capture request has not already been submitted to your processor. |
| \* There are no card-not-present transactions during the check-out procedure.                                                                                                                                                                                            ||||
[Check-Out Transactions]

| Service | Card Present (CP) or Card Not Present (CNP) | Comments Field Value |                                                    Description                                                    |
|---------|---------------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------|
| Sale    | CNP                                         | `Noshow Sale CNP`    | Sale when the guest is a no-show.                                                                                 |
| Refund  | CNP                                         | `Noshow Refund CNP`  | Refund when the customer already paid for the whole stay. Refund the amount that is not included the no-show fee. |
[No-Show Transactions]

| Service | Card Present (CP) or Card Not Present (CNP) | Comments Field Value |                   Description                    |
|---------|---------------------------------------------|----------------------|--------------------------------------------------|
| Refund  | CNP                                         | `Service REFUND CNP` | Follow-on refund for a previous capture or sale. |
| Credit  | CNP                                         | `Service CREDIT CNP` | Stand-alone credit.                              |
| Refund  | CP                                          | `Service REFUND CP`  | Follow-on refund for a previous capture or sale. |
| Credit  | CP                                          | `Service CREDIT CP`  | Stand-alone credit.                              |
[Refund and Credit Transactions]

| Service  | Card Present (CP) or Card Not Present (CNP) |     Comments Field Value     |                                     Description                                      |
|----------|---------------------------------------------|------------------------------|--------------------------------------------------------------------------------------|
| Reversal | CNP                                         | `Error REVERSAL Timeout CNP` | Reversal for a previous authorization that timed out.                                |
| Void     | CNP                                         | `Error VOID Timeout CNP`     | Void for a previous capture or credit that timed out.                                |
| Void     | CNP                                         | `Error VOID Payment CNP`     | Void for a previous payment that completed and had to be voided within the same day. |
| Void     | CNP                                         | `Error VOID Capture CNP`     | Void for a previous capture that completed and had to be voided within the same day. |
| Reversal | CP                                          | `Error REVERSAL Timeout CP`  | Reversal for a previous authorization that timed out.                                |
| Void     | CP                                          | `Error VOID Timeout CP`      | Void for a previous capture or credit that timed out.                                |
| Void     | CP                                          | `Error VOID Payment CP`      | Void for a previous payment that completed and had to be voided within the same day. |
| Void     | CP                                          | `Error VOID Capture CP`      | Void for a previous capture that completed and had to be voided within the same day. |
| Void     | CNP                                         | `Error VOID Refund`          | Void for a previous refund that completed and had to be voided within the same day.  |
| Void     | CNP                                         | `Error VOID Credit`          | Void for a previous credit that completed and had to be voided within the same day.  |
[Error Transactions]

Lodging Data Fields {#lodging-data-fields}
==========================================

This is a list of the required data fields for lodging transactions. To view required fields by transaction type, see the *Required Fields* section for the specific payment service in this section.

processingInformation.industryDataType
:
Set the value to `lodging`.

travelInformation.agency.code
:

travelInformation.agency.name
:

travelInformation.duration
:

travelInformation.lodging.additionalDiscountAmount
:

travelInformation.lodging.adjustmentAmount
:

travelInformation.lodging.audioVisualCost
:

travelInformation.lodging.banquetCost
:

travelInformation.lodging.businessCenterCost
:

travelInformation.lodging.cashDisbursementCost
:

travelInformation.lodging.checkInDate
:

travelInformation.lodging.checkOutDate
:

travelInformation.lodging.conferenceRoomCost
:

travelInformation.lodging.corporateClientCode
:

travelInformation.lodging.customerServicePhoneNumber
:

travelInformation.lodging.earlyCheckOutCost
:

travelInformation.lodging.foodAndBeverageCost
:

travelInformation.lodging.giftShopCost
:

travelInformation.lodging.gratuityAmount
:

travelInformation.lodging.guestName
:

travelInformation.lodging.healthClubCost
:

travelInformation.lodging.internetAccessCost
:

travelInformation.lodging.laundryCost
:

travelInformation.lodging.loungeBarCost
:

travelInformation.lodging.miniBarCost
:

travelInformation.lodging.miscellaneousCost
:

travelInformation.lodging.movieCost
:

travelInformation.lodging.nonRoomCost
:

travelInformation.lodging.nonRoomTaxAmount
:

travelInformation.lodging.numberOfGuests
:

travelInformation.lodging.numberOfRooms
:

travelInformation.lodging.phoneCost
:

travelInformation.lodging.prepaidCost
:

travelInformation.lodging.restaurantCost
:

travelInformation.lodging.room.dailyRate
:

travelInformation.lodging.room.numberOfNights
:

travelInformation.lodging.roomBedType
:

travelInformation.lodging.roomLocation
:

travelInformation.lodging.roomRateType
:

travelInformation.lodging.roomServiceCost
:

travelInformation.lodging.roomTaxAmount
:

travelInformation.lodging.roomTaxType
:

travelInformation.lodging.smokingPreference
:

travelInformation.lodging.specialProgramCode
:

travelInformation.lodging.totalTaxAmount
:

travelInformation.lodging.transportationCost
:

travelInformation.lodging.valetParkingCost
:

Check-In Authorization with Contact EMV and `TMS` Token Creation {#lodging-checkin-auth-contact-emv-token-task}
===============================================================================================================

Use this information to process an authorization with contact EMV and to create a `Token Management Service` token.

Endpoint {#lodging-checkin-auth-contact-emv-token-task_d7e16}
-------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#lodging-checkin-auth-contact-emv-token-task_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#lodging-checkin-auth-contact-emv-token-task_d7e35}

Required Fields for a Check-In Authorization with Contact EMV and `TMS` Token Creation {#lodging-checkin-auth-contact-emv-token-req-fields}
===========================================================================================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Checkin Auth CP`.

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:

[clientReferenceInformation.transactionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:
Set this field to a unique value to manage timeout scenarios when a response message is not received.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set the value to `01`.

[pointOfSaleInformation.emv.tags](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.entryMode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set the value to `contact`.

[pointOfSaleInformation.terminalCapability](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:
Set the value to `4`.

[pointOfSaleInformation.terminalId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:
This field is required if it is within project scope. Merchant configuration is required in order to support multiple terminal IDs. Otherwise, `Payment Gateway` uses the default terminal ID in the merchant configuration.

[pointOfSaleInformation.trackData](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.actionList](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set the value to `TOKEN_CREATE`.

[processingInformation.actionTokenTypes](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-token-types.md "")
:
Set the field to one of these values:

    * `customer`
    * `instrumentIdentifier`
    * `paymentInstrument`

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.industryDataType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set the value to `lodging`.

[processingInformation.reconciliationId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-reconciliation-id.md "")
:
Set the value to the room or folio number.

[travelInformation.duration](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-duration.md "")
:

REST Example: Check-In Authorization with Contact EMV and `TMS` Token Creation {#lodging-checkin-auth-contact-emv-token-ex-rest}
================================================================================================================================

This example shows you how to authorize a payment at check in with contact EMV while creating customer, payment instrument, and instrument identifier tokens.  
Request

```
{
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Checkin Auth CP",
        "_comment": "Include the transactionId - A unique value used to manage timeout scenarios when response message is not received.",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012",
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "processingInformation": {
        "actionList": [
            "TOKEN_CREATE"
        ],
        "actionTokenTypes": [
            "instrumentIdentifier",
            "paymentInstrument",
            "customer"
        ],
        "commerceIndicator": "retail",
        "capture": false,
        "industryDataType": "lodging",
        "_comment": "reconciliationId field - Please pass ROOM/folio Number for Lodging",
        "reconciliationId": "214"
    },
    "travelInformation": {
        "duration": "2"
    },
    "pointOfSaleInformation": {
        "_comment": "terminalId field required if in project scope.  Merchant configuration required to support multiple TID.  Otherwise, default TID in merchant configuration used",
        "terminalId": "12345678",
        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9A032203289C01005F2A0206049F1A0206049F02060000000202009F03060000000000005F3401019F36020002820200208407A0000000031010950500000000009F10201F220100A00000000000000000000000000000000000000000000000000000009F2608CE9652E31FCB34C79F2701809F33036068C89F34030200009F3704548FF8CF9F6E0420700000"
        },
        "trackData": ";4761731xxxx00027=241220119058254?",
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
            "totalAmount": "500.00",
            "currency": "USD"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7334466205036952804953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7334466205036952804953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7334466205036952804953/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Checkin Auth CP",
        "partner": {
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "id": "7334466205036952804953",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "500.00",
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
            "tags": "9F360200029108970A2A7200860000"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "023821",
        "paymentAccountReferenceNumber": "V0010013019319455709071563112",
        "approvalCode": "034508",
        "networkTransactionId": "304341034201726",
        "settlementDate": "4346",
        "retrievalReferenceNumber": "434000023821",
        "transactionId": "304341034201726",
        "responseCode": "00",
        "avs": {
            "code": "2"
        }
    },
    "reconciliationId": "214",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-12-06T00:57:00Z",
    "tokenInformation": {
        "instrumentidentifierNew": false,
        "instrumentIdentifier": {
            "state": "ACTIVE",
            "id": "7034970000031910027"
        },
        "paymentInstrument": {
            "id": "28906F4B4175D130E063AF598E0A1E0C"
        },
        "customer": {
            "id": "28907456CBDCCBBFE063AF598E0A8A5F"
        }
    }
}
```

{#lodging-checkin-auth-contact-emv-token-ex-rest_codeblock_qkq_f1t_lwb}

Check-In Authorization with Contact EMV PIN Debit {#lodging-checkin-contact-emv-pd-task}
========================================================================================

Use this information to process a check-in authorization when a guest checks in with a contact EMV PIN debit payment card. Request a PIN debit purchase with contact EMV.

Endpoint {#lodging-checkin-contact-emv-pd-task_d7e16}
-----------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#lodging-checkin-contact-emv-pd-task_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#lodging-checkin-contact-emv-pd-task_d7e35}

Required Fields for a Check-In Authorization with Contact EMV PIN Debit {#lodging-checkin-contact-emv-pd-req-fields}
====================================================================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set this field to `CARD`.

[paymentInformation.paymentType.subTypeName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-sub-type-name.md "")
:
Set this field to `DEBIT`.

[pointOfSaleInformation.deviceId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-device-id.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Required only when the card has a sequence number configured on the EMV chip.

[pointOfSaleInformation.emv.tags](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[pointOfSaleInformation.encryptedKeySerialNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-key-serial-num.md "")
:

[pointOfSaleInformation.encryptedPin](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-encrypted-pin.md "")
:

[pointOfSaleInformation.entryMode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Set this field to `contact`.

[pointOfSaleInformation.pinBlockEncodingFormat](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-pin-block-encoding-format.md "")
:
Set this field to `1`.

[pointOfSaleInformation.terminalCapability](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-capability.md "")
:

[pointOfSaleInformation.terminalID](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

[pointOfSaleInformation.terminalPinCapability](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-pin-capability.md "")
:

[pointOfSaleInformation.trackData](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-track-data.md "")
:

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `retail`.

[processingInformation.networkRoutingOrder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-network-routing-order.md "")
:

[travelInformation.duration](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-duration.md "")
:

REST Example: Check-In Authorization with Contact EMV PIN Debit {#lodging-checkin-contact-emv-pd-ex-rest}
=========================================================================================================

This example shows you how to authorize a payment at check in with contact EMV while creating customer, payment instrument, and shipping address tokens. The example includes optional lodging fields.  
Request

```
{
    "clientReferenceInformation": {
        "comments": "Checkin Auth CP",
        "code": "9876543219",
        "transactionId": "tid9876",
        "partner": {
            "developerId": "developer9876",
            "solutionId": "solution9876"
        }
    },
    "processingInformation": {
        "commerceIndicator": "retail",
        "industryDataType": "lodging",
        "networkRoutingOrder": "7MF8VGEH"
    },
    "paymentInformation": {
        "paymentType": {
            "name": "CARD",
            "subTypeName": "DEBIT"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "150",
            "currency": "USD"
        }
    },
    "travelInformation": {
        "duration": "11",
        "lodging": {
            "room": [
                {
                    "dailyRate": "120.00",
                    "numberOfNights": 1
                }
            ],
            "roomTaxType": "3.00",
            "totalTaxAmount": "5.00",
            "prepaidCost": "5.00",
            "foodAndBeverageCost": "15.00",
            "cashDisbursementCost": "2.00"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678",
        "entryMode": "contact",
        "terminalCapability": 4,
        "terminalPinCapability": 12,
        "emv": {
            "tags": "5F3401019F3303E0F8C8950580800480009F370465B81A3A9F100706011203A0A0009F2608E9D097D1901E8AB99F36020002820218009C01009F1A0208409A031808169F02060000000007005F2A0208409F0306000000000000DF78083831393931303236DF791B322D30323436362D312D31432D5246492D303331332D342E332E62",
            "cardSequenceNumber": "01"
        },
        "trackData": ";476173XXXXXXXXXX=251220111478549?",
        "deviceId": "",
        "pinBlockEncodingFormat": 0,
        "encryptedPin": "F509429A3C3FD201",
        "encryptedKeySerialNumber": "FFFF1B1D140000200001"
    },
    "merchantInformation": {
        "categoryCode": 7011
    }
}        
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7231221422946408604951/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7231221422946408604951"
        }
    },
    "clientReferenceInformation": {
        "code": "Lodging_Ben_ct_AddFields"
    },
    "id": "7231221422946408604951",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "150.00",
            "currency": "usd"
        }
    },
    "pointOfSaleInformation": {
        "emv": {
            "tags": "9F36020002910816D717A200860000"
        }
    },
    "processingInformation": {
        "reconciliationId": "7231221422946408604951"
    },
    "processorInformation": {
        "systemTraceAuditNumber": "017809",
        "routing": {
            "network": "0002"
        },
        "approvalCode": "059782",
        "retrievalReferenceNumber": "123456017809",
        "transactionId": "304221469420503",
        "responseCode": "00"
    },
    "reconciliationId": "7231221422946408604951",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-08-08T13:02:22Z"
}        
```

Incremental Authorization {#lodging-incremental-auth-task}
==========================================================

Use this information to process a lodging incremental authorization. You can add products and services to an existing authorization by using an incremental authorization. The incremental authorization service has these limitations:

* Maximum of 100 incremental authorizations per transaction, in addition to the initial authorization.
* Interchange optimization is not supported.

Endpoint {#lodging-incremental-auth-task_d7e45}
-----------------------------------------------

**Production:** `PATCH ``https://api.example.com``/pts/v2/payments/`*{id}*{#lodging-incremental-auth-task_d7e54}  
**Test:** `PATCH ``https://apitest.example.com``/pts/v2/payments/`*{id}*{#lodging-incremental-auth-task_d7e66}  
The *{id}* is the transaction ID returned in the original authorization response.

Incremental Authorization Service Scenario
------------------------------------------

This sequence is an example of how an incremental authorization can be used:

1. The customer reserves a room for two nights at a cost of 200.00 per night. You request an authorization for 400.00. This initial authorization request is approved.
2. The customer orders dinner through room service the first night. You request an incremental authorization of 50.00 for the dinner.
3. The customer decides to stay an extra night. You request an incremental authorization of 200.00 for the additional night.
4. The customer uses items from the mini-bar. The cost of these mini-bar items is 50.00. You request an incremental authorization of 50.00.
5. When the customer ends their stay and checks out, they sign a receipt for 700.00, which is the total of all costs incurred.
6. You request a capture for 700.00.

Required Fields for an Incremental Authorization {#lodging-incremental-auth-req-fields}
=======================================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Incremental Auth CP`.

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Payment Gateway` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:
Set the value to `true`.

[processingInformation.authorizationOptions.initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set the value to `merchant`.

REST Example: Incremental Authorization {#lodging-incremental-auth-ex-rest}
===========================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Incremental Auth CP",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012",
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "processingInformation": {
        "authorizationOptions": {
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true"
            }
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "USD"
        }
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7334466205036952804953/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7334466205036952804953"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7334466205036952804953/captures"
        }
    },
    "clientReferenceInformation": {
        "comments": "Incremental Auth CP",
        "code": "TestCode123",
        "partner": {
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "id": "7334466205036952804953",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "600.00",
            "authorizedAmount": "100.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "accountFeatures": {
            "category": "A"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "023821",
        "approvalCode": "012921",
        "transactionId": "304341034201726",
        "responseCode": "00"
    },
    "reconciliationId": "214",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-12-06T00:58:10Z"
}
```

Check-Out Capture {#lodging-capture-intro}
==========================================

Use this information to process a check-out capture.

Endpoint {#lodging-capture-intro_d7e127}
----------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments/`*{id}*`/captures`{#lodging-capture-intro_d7e136}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments/`*{id}*`/captures`{#lodging-capture-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for a Check-Out Capture {#lodging-checkout-capture-req-fields}
==============================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Checkout Capture CP`.

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Payment Gateway` provides the value for this field.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[pointOfSaleInformation.emv.cardSequenceNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-card-sequence-num.md "")
:
Set this value to `01`.

[pointOfSaleInformation.emv.tags](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-emv-tags.md "")
:

[processingInformation.industryDataType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set the value to `lodging`.

[travel-info-lodg-check-in-date.html](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-lodg-check-in-date.md "")
:

[travelInformation.lodging.checkOutDate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-lodg-check-out-date.md "")
:

[travelInformation.lodging.specialProgramCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-lodg-spec-prog-code.md "")
:
Set this value to `1`.

REST Example: Check-Out Capture {#lodging-checkout-capture-ex-rest}
===================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Checkout Capture CP",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012",
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "600.00",
            "currency": "USD"
        }
    },
    "processingInformation": {
        "industryDataType": "lodging"
    },
    "travelInformation": {
        "lodging": {
            "checkInDate": "052124",
            "checkOutDate": "052224",
            "specialProgramCode": "1" 
        }
    },
    "pointOfSaleInformation": {

        "emv": {
            "cardSequenceNumber": "01",
            "tags": "9A032203289C01005F2A0206049F1A0206049F02060000000202009F03060000000000005F3401019F36020002820200208407A0000000031010950500000000009F10201F220100A00000000000000000000000000000000000000000000000000000009F2608CE9652E31FCB34C79F2701809F33036068C89F34030200009F3704548FF8CF9F6E0420700000"
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
            "href": "/pts/v2/captures/7334467613636968504953/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/captures/7334467613636968504953"
        }
    },
    "clientReferenceInformation": {
        "comments": "Checkout Capture CP",
        "code": "TestCode123",
        "partner": {
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "id": "7334467613636968504953",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "600.00",
            "currency": "USD"
        }
    },
    "reconciliationId": "214",
    "status": "PENDING",
    "submitTimeUtc": "2025-12-06T00:59:21Z"
}
```

{#lodging-checkout-capture-ex-rest_codeblock_qkq_f1t_lwb}

No-Show Sale Using a Stored Credential {#lodging-noshow-sale-task}
==================================================================

Use this information to request a no-show sale when the customer does not use or cancel the reservation. In this scenario, use the stored credential (token) to charge the customer an agreed-upon fee, as stated in your lodging's disclosed no-show and cancellation policies.

Endpoint {#lodging-noshow-sale-task_d7e16}
------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#lodging-noshow-sale-task_d7e25}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#lodging-noshow-sale-task_d7e35}

Required Fields for a No-Show Sale Using a Stored Credential {#lodging-noshow-sale-req-fields}
==============================================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.comments](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-comments.md "")
:
Set the value to `Noshow Sale CP`.

[clientReferenceInformation.partner.developerId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.solutionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.partner.thirdPartyCertificationNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-third-party-certnum.md "")
:
`Payment Gateway` provides the value for this field.

[clientReferenceInformation.transactionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-transaction-id.md "")
:
Set this field to a unique value to manage timeout scenarios when a response message is not received.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.authorizationOptions.ignoreAvsResult](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-avs-result.md "")
:
Set the value to `true`.

[processingInformation.authorizationOptions.ignoreCvResult](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-ignore-cv-result.md "")
:
Set the value to `true`.

[processingInformation.authorizationOptions.initiator. merchantInitiatedTransaction.originalAuthorizedAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-orig-auth-a.md "")
:

[processingInformation.authorizationOptions.initiator. merchantInitiatedTransaction. previousTransactionId](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-txn.md "")
:

[processingInformation. authorizationOptions. initiator. merchantInitiatedTransaction. reason](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-mit-reason.md "")
:
Set the value to `4`.

[processingInformation.authorizationOptions.initiator.storedCredentialUsed](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-sc-used.md "")
:
Set the value to `true`.

[processingInformation.authorizationOptions. initiator.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-initiator-type.md "")
:
Set the value to `merchant`.

[processingInformation.capture](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set the value to `internet`.

[processingInformation.industryDataType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-industry-data-type.md "")
:
Set the value to `lodging`.

[travelInformation.lodging.specialProgramCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-lodg-spec-prog-code.md "")
:
Set this value to `2`.

REST Example: No-Show Sale Using a Stored Credential {#lodging-noshow-sale-ex-rest}
===================================================================================

This example shows you how to request a sale payment for a no-show transaction. The example includes optional lodging fields.  
Request

```
{
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Noshow Sale CP",
        "_comment": "Include the transactionId - A unique value used to manage timeout scenarios when response message is not received.",
        "partner": {
            "thirdPartyCertificationNumber": "123456789012",
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "processingInformation": {
        "capture": "true",
        "commerceIndicator": "internet",
        "authorizationOptions": {
            "ignoreAvsResult": "true",
            "ignoreCvResult": "true",
            "initiator": {
                "type": "merchant",
                "storedCredentialUsed": "true",
                "merchantInitiatedTransaction": {
                    "reason": "4",
                    "_comment": "previousTransactionId field - value from original authorization response message",
                    "previousTransactionId": "304332675422846",
                    "originalAuthorizedAmount": "488.00"
                }
            }
        },
        "industryDataType": "lodging"
    },
    "travelInformation": {
        "lodging": {
            "specialProgramCode": "2"
        }
    },
    "orderInformation": {
        "billTo": {
            "country": "US",
            "lastName": "Smith",
            "address1": "1295 Main Rd",
            "postalCode": "94043",
            "locality": "Mountain View",
            "administrativeArea": "CA",
            "firstName": "Jane",
            "email": "null@example.com"
        },
        "amountDetails": {
            "totalAmount": "500.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "400552XXXXXXXXXX",
            "securityCode": "424",
            "expirationMonth": "12",
            "type": "001"
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
            "href": "/pts/v2/payments/7334468105946974604953/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7334468105946974604953"
        }
    },
    "clientReferenceInformation": {
        "code": "TestCode123",
        "comments": "Noshow Sale CP",
        "partner": {
            "developerId": "AssignedDevID",
            "solutionId": "AssignedSolutionID"
        }
    },
    "id": "7334468105946974604953",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "500.00",
            "authorizedAmount": "500.00",
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
            "category": "B",
            "group": "0"
        },
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "023826",
        "paymentAccountReferenceNumber": "V0010013019053587486979965591",
        "approvalCode": "054511",
        "cardVerification": {
            "resultCodeRaw": "M",
            "resultCode": "M"
        },
        "networkTransactionId": "304341036102578",
        "settlementDate": "4346",
        "retrievalReferenceNumber": "434001023826",
        "transactionId": "304341036102578",
        "responseCode": "00",
        "avs": {
            "code": "U",
            "codeRaw": "U"
        }
    },
    "reconciliationId": "7334468105946974604953",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-12-06T01:00:10Z"
}
```

