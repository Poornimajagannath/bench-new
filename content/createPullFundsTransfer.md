---
title: Process a Pull Funds Transfer
generated: true
source: doc-cybersource-payments-openapi
operation_id: createPullFundsTransfer
lineage_origin: generated_from_spec
---

# Process a Pull Funds Transfer

<!-- section:prose -->
## Overview

You use this endpoint to process a Pull Funds Transfer.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v1/pull-funds-transfer`  
**Operation ID:** `createPullFundsTransfer`

## Auth

This OpenAPI document does not declare `security` / `securityDefinitions` for the operation. Authenticate with HTTP Signature or JWT per CyberSource REST getting started (sandbox: `apitest.cybersource.com`).

## Safety

Use tokenized instruments or sandbox test values only. Do not send raw PAN in production.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code | string | no | Originator-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.
 |
| clientReferenceInformation.applicationName | string | no | The name of the Connection Method that the originator uses to send a transaction request to CyberSource.
 |
| clientReferenceInformation.applicationVersion | string | no | Version of the CyberSource application or integration used for a transaction.
 |
| clientReferenceInformation.applicationUser | string | no | The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.
 |
| orderInformation.amountDetails.totalAmount | string | yes | The total amount of the funds transfer including all fees.

This value cannot be negative.  
You can include a decimal point (.), but no other special characters.
 |
| orderInformation.amountDetails.currency | string | yes | Use a 3-character alpha currency code for currency of the sender.

ISO standard currencies: [http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  

Currency must be supported by the processor.
 |
| orderInformation.amountDetails.serviceFee | string | no | When present, this field contains the sender's surcharge as assessed by the originator. Values in this field must be in the same currency and format as defined in the amount field.
 |
| orderInformation.amountDetails.foreignExchangeFee | string | no | When present, this field contains the sender's foreign exchange markup fee (markup above the wholesale or VisaNet exchange rate as assessed by the originator). Values in this field must be in the same currency and format as defined in the amount field.
 |
| orderInformation.amountDetails.surcharge | object | no |  |
| orderInformation.isCryptoCurrencyPurchase | string | no | This indicates that the funds transfer is for a crypto currency transaction.
Optional
Y/y, true
N/n, false
 |
| processingInformation.commerceIndicator | string | no | Type of transaction. This field identifies the level of security used in an electronic commerce transaction over an open network (for example, the internet).

Values for a Payouts transaction:  
`INTERNET`, `RECURRING`, `RECURRING_INTERNET`, `VBV_FAILURE`, `VBV_ATTEMPTED`, `VBV`, `SPA_FAILURE`, `SPA_ATTEMPTED`, `SPA`  

If no value is entered this field will set a default value = `INTERNET`.
 |
| processingInformation.fundingOptions.initiator | object | no |  |
| processingInformation.recurringOptions.firstRecurringPayment | boolean | no | Indicates the transaction that is the first of a series of recurring payments.

- `True` = is first recurring payment
- `False` = is not first recurring payment

Conditional for MITCOF transactions
 |
| processingInformation.businessApplicationId | string | yes | Payouts transaction type.

Possible Values:
- `AA` = Account to account
- `PP` = Person to person
- `TU` = Top-up for enhanced prepaid loads
- `WT` = Wallet transfer
- `BI` = Bank-Initiated
- `FT` = Funds Transfer
- `FD` = Funds Disbursement
- `MP` = Merchant Payment
- `PD` = Payroll Disbursement
- `LA` = Liquid Assets
 |
| processingInformation.purposeOfPayment | string | no | Visa Direct  
Purpose of payment is required in certain markets to clearly identify the purpose of the payment based on the standard values defined for respective market.
 |
| processingInformation.payoutsOptions.retrievalReferenceNumber | string | no | This field contains a number that is used with other data elements as a key to identify and track all messages related to a given cardholder transaction; that is, to a given transaction set.

Recommended format: ydddhhnnnnnn 

Positions 1-4: The yddd equivalent of the date, where y = 0-9 and ddd = 001 – 366. 
Positions 5-12: A unique identification number generated by the merchant.
 |
| processingInformation.languageCode | string | no | Contains the ISO 639-2 defined language Code
 |
| processingInformation.accountVerificationCode | array | no | Account verification code will inform what Payment Account Verification should be performed. With this array of codes, a merchant can choose à la carte what verifications to run. This field is optional, and the default is 1 if it is not passed in. This means that a full validation of the fields will be performed.
Valid verification codes:
- `1` = Full Account Verification (Card Account, CVN, CAVV, TAVV, Address, Name, eMail, Phone, Identity)
- `2` = Card Account Verification
- `3` = Address Verification
- `4` = Card Authentication Method (CAM) (Cryptogram)
- `5` = Cardholder Authentication Verification (CAVV)
- `6` = Cardholder Identity Verification
- `7` = CVV2 Verification
- `8` = eMail Verification
- `9` = Name Verification
- `10` = Phone Verification
 |
| recipientInformation.administrativeArea | string | no | Recipient's state. Use the State, Province, and Territory Codes for the United States and Canada.
Value must be an ISO Standard State Code: 
https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf
 |
| recipientInformation.postalCode | string | no | Recipient's postal code.
 |
| recipientInformation.country | string | no | Recipient's country code. Check that this field contains 2-character alpha ISO 3166-1 standard values.
 |
| recipientInformation.personalIdentification.issuingCountry | string | no | Issuing country of the identification. The field format should be a 2 character ISO 3166-1 alpha-2 country code.
 |
| recipientInformation.personalIdentification.id | string | no | This tag will contain an acquirer-populated id value associated with the API.
 |
| recipientInformation.personalIdentification.type | string | no | This tag will contain the type of recipient identification. The valid values are:

- `BTHD`: (Date of birth)
- `CUID`: (Customer identification (unspecified))
- `NTID`: (National identification)
- `PASN`: (Passport number)
- `DRLN`: (Driver license)
- `TXIN`: (Tax identification)
- `CPNY`: (Company registration number)
- `PRXY`: (Proxy identification)
- `SSNB`: (Social security number)
- `ARNB`: (Alien registration number)
- `LAWE`: (Law enforcement identification)
- `MILI`: (Military identification)
- `TRVL`: (Travel identification (non-passport))
- `EMAL`: (Email)
- `PHON`: (Phone number)
 |
| recipientInformation.personalIdentification.personalIdType | string | no | This field denotes whether the Tax ID is a business or individual's Tax ID when idType contains the value of TXIN (Tax identification). 
The valid values are: B (Business) I (Individual)
 |
| recipientInformation.firstName | string | no | Recipient's first name.
 |
| recipientInformation.middleInitial | string | no | Middle Initial of recipient.
This field is supported by FDC Compass.
 |
| recipientInformation.middleName | string | no | Recipient’s middle name. This field is a pass through,
which means that CyberSource does not verify the value or modify it in any way before sending it to the processor.
If the field is not required for the transaction, CyberSource does not forward it to the processor.
 |
| recipientInformation.lastName | string | no | Recipient's last name. Conditional field. If `recipientInformation.sameAsSender` = `false`, this field is mandatory.
 |
| recipientInformation.address1 | string | no | Street address of recipient. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| recipientInformation.address2 | string | no | Second line of the recipient's address.
 |
| recipientInformation.buildingNumber | string | no | This field contains the house or the building number of the recipient address.
 |
| recipientInformation.locality | string | no | Recipient city.
 |
| recipientInformation.identificationNumber | string | no | Government-issued identification number.

Conditional: This field is mandatory if the `processingInformation.businessApplicationId` is any of the following:  
- `AA`
- `PP`
- `TU`
- `BI`
- `WT`
- `FT`
- and country code = `BR`, `AR`, `CO`, `PE`, in `recipientInformation.countryCode` (Argentina, Brazil, Colombia, and Peru)
 |
| recipientInformation.type | string | no | `B` for Business or `I` for individual.

Conditional:  If `recipientInformation.identificationNumber` is present, then this field is mandatory.
 |
| recipientInformation.descriptor | string | no | Recipient first name, this will be concatenated with the 4-digit originator abbreviation.
 |
| recipientInformation.accountId | string | no | Identifier for the recipient’s account.
 |
| recipientInformation.accountType | string | no | Identifies the recipient’s account type. This field is applicable for AFT transactions.

Valid values are:

- `00` Other
- `01` Routing transit number (RTN) and bank account
- `02` IBAN
- `03` Card account
- `04` Email
- `05` Phone number
- `06` Bank account number (BAN) and bank identification code (BIC)
- `07` Wallet ID
- `08` Social network ID
 |
| recipientInformation.aliasName | string | no | Account owner alias name.
 |
| recipientInformation.countryOfBirth | string | no | Account Owner Country of Birth
 |
| recipientInformation.dateOfBirth | string | no | Recipient’s date of birth. Format: YYYYMMDD.
 |
| recipientInformation.email | string | no | Account Owner email address
 |
| recipientInformation.nationality | string | no | Account Owner Nationality
 |
| recipientInformation.occupation | string | no | Account Owner Occupation
 |
| recipientInformation.streetName | string | no | This field contains the street name of the recipient's address.
 |
| senderInformation.postalCode | string | no | Sender’s postal code. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.firstName | string | no | First name of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.middleInitial | string | no | Middle Initial of sender
 |
| senderInformation.middleName | string | no | This field contains the middle name of the entity funding the transaction.
 |
| senderInformation.lastName | string | no | Last name of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.address1 | string | no | Street address of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.address2 | string | no | Second line of the sender's address.
 |
| senderInformation.locality | string | no | City of sender. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.administrativeArea | string | no | Sender’s state. Use the **State, Province, and Territory Codes for the United States and Canada**. This field is conditional: it is required if in the United States or Canada, and transaction is using neither a Customer nor Payment Instrument token. 

Value must be an ISO Standard State Code: [https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf)
 |
| senderInformation.country | string | no | Country of sender. Check that this field contains 2 character alpha ISO 3166-1 standard values. This field is conditional: it is required if using neither a Customer nor Payment Instrument token.
 |
| senderInformation.paymentInformation.card | object | no |  |
| senderInformation.paymentInformation.tokenizedCard | object | no |  |
| senderInformation.paymentInformation.customer | object | no |  |
| senderInformation.paymentInformation.paymentInstrument | object | no |  |
| senderInformation.paymentInformation.instrumentIdentifier | object | no |  |
| senderInformation.paymentInformation.accountType | string | no | If supported, the `accountType` can specify what type of account is used by the issuer. Must be a valid value:
- `00`-Not applicable
- `10`-Saving account
- `20`-Checking account
- `30`-Credit card account
- `40`-Universal account
 |
| senderInformation.consumerAuthentication.cavv | string | no | Cardholder authentication verification value (CAVV). 

Conditional: this field is mandatory if the transaction is using either a Visa or Visa Electron card, and if the commerce indicator is = `VBV`.

If in hexabinary format, length of field value must be =40.  
If in base64 format, length of field must be =28.
 |
| senderInformation.consumerAuthentication.strongAuthentication | object | no |  |
| senderInformation.personalIdentification.issuingCountry | string | no | Issuing country of the identification.  
The field format should be a 2 character ISO 3166-1 alpha-2 country code.
 |
| senderInformation.personalIdentification.id | string | no | The ID number/value.

Visa Direct(35 characters)  
This tag will contain an acquirer-populated id value associated with the API.  
If `senderInformation.personalIdentification.type`=`BTHD`, then the id format must be `YYYYMMDD`.
 |
| senderInformation.personalIdentification.type | string | no | Visa Direct  
This tag will contain the type of sender identification.  
The valid values are:  
• `BTHD` (Date of birth)  
• `CUID` (Customer identification (unspecified))  
• `NTID` (National identification)  
• `PASN` (Passport number)  
• `DRLN` (Driver license)  
• `TXIN` (Tax identification)  
• `CPNY` (Company registration number)  
• `PRXY` (Proxy identification)  
• `SSNB` (Social security number)  
• `ARNB` (Alien registration number)  
• `LAWE` (Law enforcement identification)  
• `MILI` (Military identification)  
• `TRVL` (Travel identification (non-passport))  
• `EMAL` (Email)  
• `PHON` (Phone number)
 |
| senderInformation.personalIdentification.personalIdType | string | no | It denotes whether the tax ID is a business or individual tax ID.  
The valid values are:  
• `B` (Business)  
• `I` (Individual)

Visa Direct  
This field is required when `senderInformation.personalIdentification.type` has the value of `TXIN` (Tax identification).  
A value for `senderInformation.personalInformation.id` is required when `senderInformation.personalIdentification.personalIdType` is present in a request.
 |
| senderInformation.referenceNumber | string | no | Visa Direct(16 characters)  
If the transaction is a money transfer, pre-paid load, or credit card bill pay, and if the sender intends to fund the transaction with a non-financial instrument (for example, cash), a reference number unique to the sender is required.  
If the transaction is a funds disbursement, the field is required.
 |
| senderInformation.account.fundsSource | string | no | Source of funds. Possible values:
- `01`: Credit card,
- `02`: Debit card,
- `03`: Prepaid card,
- `04`: Cash,
- `05`: Debit or deposit account that is not linked to a Visa card. Includes checking accounts, savings,
- `06`: Credit account that is not linked to a Visa card. Includes credit cards and proprietary lines,
- `07`: Mobile wallet account,
- `08`: Other source of funds.
 |
| senderInformation.account.number | string | no | - Cross-border: Account number of the recipient account being funded by the AFT, is mandatory in cross-border Money Transfer AFTs.
- Domestic: Optional in domestic AFTs.
- Europe Domestic and intra-EEA cross-border: Account number of the recipient account being funded is mandatory in domestic and intra-EEA Money Transfer AFTs.
In an AFT, this field contains the account number of the Recipient Account being funded by the AFT.
Note: Inclusion of this tag is conditional; Sender Information reference number or Sender account number are required. If this tag is not included, Sender Reference number must be present and contain a reference number for the recipient account.
 |
| senderInformation.aliasName | string | no | Sender's alias name.
 |
| senderInformation.countryOfBirth | string | no | Account Owner Country of Birth.
 |
| senderInformation.dateOfBirth | string | no | Sender’s date of birth. Format: YYYYMMDD.
 |
| senderInformation.email | string | no | Account Owner email address
 |
| senderInformation.name | string | no | Name of sender. Use this field if the sender is a business.
 |
| senderInformation.nationality | string | no | Account Owner Nationality
 |
| senderInformation.occupation | string | no | Account Owner Occupation.
 |
| senderInformation.phoneNumber | string | no | Sender’s phone number.
 |
| senderInformation.type | string | no | This field identifies if the sender is a business or an individual. 

The valid values are: 

• `B` (Business)  
• `I` (Individual)
 |
| buyerInformation.vatRegistrationNumber | string | no | Customer's VAT registration number for the individual sender tax identification. 
This field flows in ISO field 104, DSID 63 tag 06.

Visa is recommending the use of the following business application identifier (BAI) values 
and merchant category code (MCC) combinations to process domestic bill payments, toll payments, 
and business-to-business funding transactions as AFTs in Brazil:
- BB (Business-to-business)
- BP (Non-card bill payment)
- FT (Funds transfer)
- WT (Wallet transfer)

MCC: 4784

#### Mapping
- SCMP API Field: purchaser_vat_registration_number
- Simple Order API Field: invoiceHeader_purchaserVATRegistrationNumber
- CCS: customer.vatRegistrationNumber

Optional field.
 |
| aggregatorInformation.aggregatorId | string | no | Visa Direct(11 characters)  
Value that identifies you as a payment aggregator. Get this value from the processor.
 |
| aggregatorInformation.name | string | no | Visa Direct(25 characters)  
Your payment aggregator business name. This field is conditionally required when aggregator id is present.
 |
| aggregatorInformation.subMerchant.id | string | no | Visa Direct(15 characters)  
The ID you assigned to your sub-merchant.
 |
| aggregatorInformation.city | string | no | Aggregator city.
 |
| aggregatorInformation.country | string | no | Aggregator country.
 |
| aggregatorInformation.postalCode | string | no | Aggregator postal code.
 |
| aggregatorInformation.state | string | no | Aggregator state.
 |
| aggregatorInformation.streetAddress | string | no | Aggregator street name. 
 |
| merchantInformation.merchantDescriptor.address1 | string | no | First line of merchant's address.
 |
| merchantInformation.merchantDescriptor.administrativeArea | string | no | The state where the merchant is located.
 |
| merchantInformation.merchantDescriptor.contact | string | no | Contact information for the merchant. This field contains additional information for contacting the merchant, such as an additional phone number or a contact name.
 |
| merchantInformation.merchantDescriptor.country | string | no | Merchant's country.
 |
| merchantInformation.merchantDescriptor.county | string | no | Merchant's county. Used for US Merchants only.  Send a 3-digit numeric FIPS county code. https://www2.census.gov/programs-surveys/decennial/2010/partners/pdf/FIPS_StateCounty_Code.pdf
 |
| merchantInformation.merchantDescriptor.customerServicePhoneNumber | string | no | Indicates customer service phone number of Merchant.
 |
| merchantInformation.merchantDescriptor.locality | string | no | Merchant's City.
 |
| merchantInformation.merchantDescriptor.name | string | no | Merchant's name.
 |
| merchantInformation.merchantDescriptor.phone | string | no | Merchant's phone.
 |
| merchantInformation.merchantDescriptor.postalCode | string | no | Merchant's postal code.
 |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| id | string | no | A unique identification number to identify the submitted request. It is also appended to the endpoint of the resource.
 |
| submitTimeUtc | string | no | Time of request in UTC.
Format: `YYYY-MM-DDThh:mm:ssZ`

**Example**
`2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.).
The `T` separates the date and the time.
The `Z` indicates UTC.
 |
| orderInformation.amountDetails.totalAmount | string | no | Amount you requested for the payment.
 |
| orderInformation.amountDetails.currency | string | no | Currency used for the order. Use the three-character ISO Standard Currency Codes
 |
| status | string | no | The status of the submitted transaction.

Possible values:
- AUTHORIZED
- DECLINED
- SERVER_ERROR
- INVALID_REQUEST
- PARTIAL_AUTHORIZED
 |
| errorInformation.reason | string | no | The reason of the status.

Possible values:
- CONTACT_PROCESSOR
- INVALID_MERCHANT_CONFIGURATION
- STOLEN_LOST_CARD
- PROCESSOR_DECLINED
- PARTIAL_APPROVAL
- PAYMENT_REFUSED
- INVALID_ACCOUNT
- ISSUER_UNAVAILABLE
- INSUFFICIENT_FUND
- EXPIRED_CARD
- INVALID_PIN
- UNAUTHORIZED_CARD
- EXCEEDS_CREDIT_LIMIT
- DEBIT_CARD_USAGE_LIMIT_EXCEEDED
- CVN_NOT_MATCH
- DUPLICATE_REQUEST
- GENERAL_DECLINE
- BLACKLISTED_CUSTOMER
- GATEWAY_TIMEOUT
- INVALID_DATA
- SYSTEM_ERROR
- SERVICE_UNAVAILABLE
- PROCESSOR_TIMEOUT
- PAYMENT_REJECTED
- PULL_PAYMENT_REFUSED
 |
| errorInformation.message | string | no | The detail message related to the status and reason listed above.
 |
| errorInformation.details | array | no |  |
| processorInformation.systemTraceAuditNumber | string | no | This field is returned by authorization and incremental authorization services.
System trace number that must be printed on the customer’s receipt.
 |
| processorInformation.approvalCode | string | no | Issuer-generated approval code for the transaction.
 |
| processorInformation.responseCode | string | no | Transaction status from the processor.
 |
| processorInformation.transactionId | string | no | Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor.
 |
| processorInformation.consumerAuthenticationResponse.code | string | no | Mapped response code for Visa Secure. A code is only returned if a CAVV result code is returned by the processor.
 |
| processorInformation.retrievalReferenceNumber | string | no | This field contains a number that is used with other data elements as a key to identify and track all messages related to a given cardholder transaction; that is, to a given transaction set.

Recommended format: ydddhhnnnnnn 

Positions 1-4: The yddd equivalent of the date, where y = 0-9 and ddd = 001 – 366. 
Positions 5-12: A unique identification number generated by the merchant or assigned by Cybersource.
 |
| processorInformation.avs.code | string | no | AVS result code.

Code	Description
- 'Y' Full Match
- 'A' Partial Match (street address only)
- 'Z' Partial Match (postal/zip only)
- 'N' Non-Match
- 'U' Unable to Verify
- 'R' Indeterminate Outcome (Retry)
 |
| processorInformation.responseDetails | string | no | This field might contain information about a decline.
 |
| processorInformation.customer.personalIdResult | string | no | Personal identifier validation result.

Valid values:
- '1': Verified
- '2': Failed
- '3': Not performed
- '4': Issuer does not support id verification
 |
| processorInformation.electronicVerificationResults.emailRaw | string | no | Raw Electronic Verification response code from the processor for the customer's email address.

Valid values:
- '1': Verified
- '2': Failed
- '3': Not performed
 |
| processorInformation.electronicVerificationResults.firstNameRaw | string | no | Raw electronic verification response code from the processor for the customer's first name.

Valid values:
- '01': Match
- '50': Partial Match
- '99': No Match
 |
| processorInformation.electronicVerificationResults.lastNameRaw | string | no | Raw electronic verification response code from the processor for the customer's last name.

Valid values:
- '01': Match
- '50': Partial Match
- '99': No Match
 |
| processorInformation.electronicVerificationResults.middleNameRaw | string | no | Raw electronic verification response code from the processor for the customer's middle name.

Valid values:
- '01': Match
- '50': Partial Match
- '99': No Match
 |
| processorInformation.electronicVerificationResults.nameRaw | string | no | Raw Electronic Verification response code from the processor for the customer's name.

Valid values:
- '01': Match
- '50': Partial Match
- '99': No Match
 |
| processorInformation.electronicVerificationResults.phoneNumberRaw | string | no | Raw Electronic Verification response code from the processor for the customer's phone number.

Valid values:
- '1': Verified
- '2': Failed
- '3': Not performed
 |
| processorInformation.cardVerification.resultCode | string | no | CVN result code.
 |
| processorInformation.cardVerification.resultCodeRaw | string | no | CVN result code sent directly from the processor. Returned only when the processor returns this value.

**Important** Do not use this field to evaluate the result of card verification. Use for debugging purposes only.
 |
| _links.self.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.self.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| _links.reversal.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.reversal.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| _links.refund.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.refund.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| _links.customer.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.customer.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| _links.paymentInstrument.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.paymentInstrument.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| _links.instrumentIdentifier.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.instrumentIdentifier.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Process a Pull Funds Transfer"

> "Receive funds using an Account Funding Transaction (AFT).
"

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:createPullFundsTransfer`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
