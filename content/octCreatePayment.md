---
title: Process a Payout
generated: true
source: doc-cybersource-payments-openapi
operation_id: octCreatePayment
lineage_origin: generated_from_spec
---

# Process a Payout

<!-- section:prose -->
## Overview

You use this endpoint to process a Payout.

<!-- TODO: Add a short customer-facing example once sandbox samples are approved. -->
<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payouts`  
**Operation ID:** `octCreatePayment`

## Auth

This OpenAPI document does not declare `security` / `securityDefinitions` for the operation. Authenticate with HTTP Signature or JWT per CyberSource REST getting started (sandbox: `apitest.cybersource.com`).

## Safety

Use tokenized instruments or sandbox test values only. Do not send raw PAN in production.

## Request

### Body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code | string | no | Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each
transaction so that you can perform meaningful searches for the transaction.

#### Used by
**Authorization**
Required field.

#### PIN Debit
Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being
reversed.

Required field for all PIN Debit requests (purchase, credit, and reversal).

#### FDC Nashville Global
Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports.
 |
| clientReferenceInformation.applicationName | string | no | The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource.
 |
| clientReferenceInformation.applicationVersion | string | no | Version of the CyberSource application or integration used for a transaction.
 |
| clientReferenceInformation.applicationUser | string | no | The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method.
 |
| orderInformation.amountDetails.totalAmount | string | no | Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters.
CyberSource truncates the amount to the correct number of decimal places.

**Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.

**Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths.

If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. 

#### Card Present
Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.

#### Invoicing / Pay By Link
Required for creating a new invoice or payment link.

#### PIN Debit
Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.

Required field for PIN Debit purchase and PIN Debit credit requests.
Optional field for PIN Debit reversal requests.

#### GPX
This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.

#### DCC with a Third-Party Provider
Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. 

#### DCC for First Data
Not used.
 |
| orderInformation.amountDetails.currency | string | no | Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)

#### Used by
**Authorization**
Required field.

**Authorization Reversal**
For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.

#### PIN Debit
Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).
Returned by PIN debit purchase.

For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing.
For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).

Required field for PIN Debit purchase and PIN Debit credit requests.
Optional field for PIN Debit reversal requests.

#### GPX
This field is optional for reversing an authorization or credit.

#### DCC for First Data
Your local currency.

#### Tax Calculation
Required for international tax and value added tax only.
Optional for U.S. and Canadian taxes.
Your local currency.
 |
| orderInformation.amountDetails.surcharge | object | no |  |
| orderInformation.billTo.firstName | string | no | Customer’s first name. This name must be the same as the name on the card.

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### SEPA
Required for Create Mandate and Import Mandate
#### BACS
Required for Import Mandate

#### CyberSource Latin American Processing
**Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\
**Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called _CyberSource Latin American Processing_. It is not for any other Latin American processors that CyberSource supports.

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.

#### For Payouts:
This field may be sent only for FDC Compass.

#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### OmniPay Direct
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.lastName | string | no | Customer’s last name. This name must be the same as the name on the card.

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### SEPA
Required for Create Mandate and Import Mandate
#### BACS
Required for Import Mandate
#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### CyberSource Latin American Processing
**Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\
**Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.

#### For Payouts:
This field may be sent only for FDC Compass.

#### OmniPay Direct
Optional field.

#### RBS WorldPay Atlanta
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.address1 | string | no | Payment card billing street address as it appears on the credit card issuer’s records.

#### SEPA
Required for Create Mandate and Import Mandate

#### Atos
This field must not contain colons (:).

#### CyberSource through VisaNet
**Important** When you populate orderInformation.billTo.address1 and orderInformation.billTo.address2,
CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters,
CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank.
Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks.
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet
accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations
of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the
credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless
ASCII characters for transmission to the credit card networks.

#### FDMS Nashville
When the street name is numeric, it must be sent in numeric format. For example, if the address is _One First Street_,
it must be sent as _1 1st Street_.

Required if keyed; not used if swiped.

String (20)

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### All other processors:
Optional.
String (60)

#### For Payouts
This field may be sent only for FDC Compass.

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.
 |
| orderInformation.billTo.address2 | string | no | Used for additional address information. For example: _Attention: Accounts Payable_
Optional field.

For Payouts: This field may be sent only for FDC Compass.

#### Atos
This field must not contain colons (:).

#### CyberSource through VisaNet
**Important** When you populate `orderInformation.billTo.address1` and `orderInformation.billTo.address2`,
CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters,
CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank.
Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks.
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet
accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations
of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the
credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless
ASCII characters for transmission to the credit card networks.

#### Chase Paymentech Solutions, FDC Compass, and TSYS Acquiring Solutions
This value is used for AVS.

#### FDMS Nashville
`orderInformation.billTo.address1` and `orderInformation.billTo.address2` together cannot exceed 20 characters.
String (20)

#### All Other Processors
String (60)
 |
| orderInformation.billTo.country | string | no | Payment card billing country. Use the two-character [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).

#### SEPA/BACS
Required for Create Mandate and Import Mandate

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet
accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations
of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the
credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII
characters for transmission to the credit card networks.

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### OmniPay Direct
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.locality | string | no | Payment card billing city.

#### SEPA
Required for Create Mandate and Import Mandate

#### Atos
This field must not contain colons (:).

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.

#### For Payouts:
This field may be sent only for FDC Compass.

#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### OmniPay Direct
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.administrativeArea | string | no | State or province of the billing address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).

For Payouts: This field may be sent only for FDC Compass.

##### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet
accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations
of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the
credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless
ASCII characters for transmission to the credit card networks.

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### OmniPay Direct
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.postalCode | string | no | Postal code for the billing address. The postal code must consist of 5 to 9 digits.

When the billing country is the U.S., the 9-digit postal code must follow this format:
[5 digits][dash][4 digits]

**Example** `12345-6789`

When the billing country is Canada, the 6-digit postal code must follow this format:
[alpha][numeric][alpha][space][numeric][alpha][numeric]

**Example** `A1B 2C3`

**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### SEPA
Required for Create Mandate and Import Mandate

#### For Payouts:
 This field may be sent only for FDC Compass.

#### American Express Direct
Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side.

#### Atos
This field must not contain colons (:).

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet
accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations
of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the
credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII
characters for transmission to the credit card networks.

#### FDMS Nashville
Required if `pointOfSaleInformation.entryMode=keyed` and the address is in the U.S. or Canada.
Optional if `pointOfSaleInformation.entryMode=keyed` and the address is **not** in the U.S. or Canada.
Not used if swiped.

#### RBS WorldPay Atlanta:
For best card-present keyed rates, send the postal code if `pointOfSaleInformation.entryMode=keyed`.

#### TSYS Acquiring Solutions
Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.

#### All other processors:
Optional field.
 |
| orderInformation.billTo.phoneNumber | string | no | Customer’s phone number.

It is recommended that you include the country code when the order is from outside the U.S.

#### Chase Paymentech Solutions
Optional field.

####  Credit Mutuel-CIC
Optional field.

#### CyberSource through VisaNet
Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.

#### For Payouts:
This field may be sent only for FDC Compass.

#### OmniPay Direct
Optional field.

#### SIX
Optional field.

#### TSYS Acquiring Solutions
Optional field.

#### Worldpay VAP
Optional field.

#### All other processors
Not used.
 |
| orderInformation.billTo.phoneType | string | no | Customer's phone number type.

#### For Payouts:
This field may be sent only for FDC Compass.

Possible Values:
* day
* home
* night
* work
 |
| orderInformation.isCryptocurrencyPurchase | string | no | #### Visa Platform Connect :
This API will contain the Flag that specifies whether the payment is for the purchase of cryptocurrency.
Additional values to add :
This API will contain the Flag that specifies whether the payment is for the purchase of cryptocurrency.
valid values are
- Y/y, true
- N/n, false
 |
| merchantInformation.categoryCode | integer | no | The value for this field is a four-digit number that the payment card industry uses to classify
merchants into market segments. A payment card company assigned one or more of these values to your business when you started
accepting the payment card company’s cards. When you do not include this field in your request, CyberSource uses the value in your
CyberSource account.

#### CyberSource through VisaNet
The value for this field corresponds to the following data in the TC 33 capture file5:
- Record: CP01 TCR4
- Position: 150-153
- Field: Merchant Category Code
 |
| merchantInformation.submitLocalDateTime | string | no | Time that the transaction was submitted in local time. The time is in hhmmss format.
 |
| merchantInformation.vatRegistrationNumber | string | no | Your government-assigned tax identification number.

#### Tax Calculation
Required field for value added tax only. Not applicable to U.S. and Canadian taxes.

#### CyberSource through VisaNet
For CtV processors, the maximum length is 20.
 |
| merchantInformation.merchantDescriptor.name | string | no | Your merchant name.

**Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22.

#### PIN debit
Your business name. This name is displayed on the cardholder’s statement. When you
include more than one consecutive space, extra spaces are removed.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

Optional field for PIN debit credit or PIN debit purchase requests.

#### Airline processing
Your merchant name. This name is displayed on the cardholder’s statement. When you include more than one consecutive space, extra spaces are removed.

**Note** Some airline fee programs may require the original ticket number (ticket identifier) or the ancillary service description in positions 13 through 23 of this field.

**Important** This value must consist of English characters.

Required for captures and credits.
 |
| merchantInformation.merchantDescriptor.locality | string | no | Merchant's City.

#### PIN debit
City for your business location. This value might be displayed on the cardholder’s statement.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

Optional field for PIN debit credit or PIN debit purchase requests.
 |
| merchantInformation.merchantDescriptor.country | string | no | Merchant's country.

#### PIN debit
Country code for your business location. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)
This value might be displayed on the cardholder’s statement.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.
**Note** If your business is located in the U.S. or Canada and you include this field in a
request, you must also include `merchantInformation.merchantDescriptor.administrativeArea`.

Optional field for PIN debit credit or PIN debit purchase.
 |
| merchantInformation.merchantDescriptor.administrativeArea | string | no | The state where the merchant is located.

#### PIN debit
State code or region code for your business. Use the Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) This value might be displayed on the cardholder’s statement.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

**Note** This field is supported only for businesses located in the U.S. or Canada.

Optional field for PIN debit credit or PIN debit purchase.
 |
| merchantInformation.merchantDescriptor.postalCode | string | no | Merchant's postal code.

#### PIN debit
Postal code for your business location. This value might be displayed on the cardholder’s statement.

If your business is domiciled in the U.S., you can use a 5-digit or 9-digit postal code. A 9-digit postal code must follow this format:
[5 digits][dash][4 digits]
Example: `12345-6789`

If your business is domiciled in Canada, you can use a 6-digit or 9-digit postal code. A 6-digit postal code must follow this format:
[alpha][numeric][alpha][space]
[numeric][alpha][numeric]
Example: `A1B 2C3`

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

**Note** This field is supported only for businesses located in the U.S. or Canada.
**Important** Mastercard requires a postal code for any country that uses postal codes.
You can provide the postal code in your account or you can include this field in your request.

Optional field for PIN debit credit or PIN debit purchase.
 |
| merchantInformation.merchantDescriptor.contact | string | no | Contact information for the merchant.

**Note** These are the maximum data lengths for the following payment processors:
- FDCCompass (13)
- Paymentech (13)
 |
| merchantInformation.merchantDescriptor.address1 | string | no | First line of merchant's address.
 |
| recipientInformation.firstName | string | no | First name of the recipient.   
This field is applicable for AFT & OCT transactions.

Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.
 |
| recipientInformation.middleName | string | no | Middle name of the recipient.   
This field is applicable for AFT & OCT transactions.

Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.
 |
| recipientInformation.lastName | string | no | Last name of the recipient. 
This field is applicable for AFT & OCT transactions.

Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.
 |
| recipientInformation.address1 | string | no | The street address of the recipient
This field is applicable for AFT and OCT transactions.

Only alpha numeric values are supported. Special characters not in the standard ASCII character set are not supported and will be stripped before being sent to sent to the processor.
 |
| recipientInformation.locality | string | no | The city of the recipient.
This field is applicable for AFT and OCT transactions.

Only alpha numeric values are supported.
Special characters not in the standard ASCII character set are not supported and will be stripped before being sent to sent to the processor.
 |
| recipientInformation.administrativeArea | string | no | The state or province of the recipient.
This field is applicable for AFT and OCT transactions when the recipient country is US or CA. Else it is optional.

Must be a two character value
 |
| recipientInformation.country | string | no | The country associated with the address of the recipient.
This field is applicable for AFT and OCT transactions.

Must be a two character ISO country code. 
For example, see [ISO Country Code](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.html)
 |
| recipientInformation.postalCode | string | no | Recipient postal code. Required only for FDCCompass. |
| recipientInformation.phoneNumber | string | no | Recipient phone number. Required only for FDCCompass. |
| recipientInformation.aliasName | string | no | Account owner alias name.
 |
| recipientInformation.nationality | string | no | Account Owner Nationality |
| recipientInformation.countryOfBirth | string | no | Account Owner Country of Birth |
| recipientInformation.occupation | string | no | Account Owner Occupation |
| recipientInformation.email | string | no | Account Owner email address |
| senderInformation.referenceNumber | string | no | Reference number generated by you that uniquely identifies the sender. |
| senderInformation.account.fundsSource | string | no | Source of funds. Possible values:

  Paymentech, CTV, FDC Compass:
 - 01: Credit card
 - 02: Debit card
 - 03: Prepaid card

  Paymentech, CTV -
 - 04: Cash
 - 05: Debit or deposit account that is not linked to a Visa card. Includes checking accounts, savings
       accounts, and proprietary debit or ATM cards.
 - 06: Credit account that is not linked to a Visa card. Includes credit cards and proprietary lines
       of credit.

  FDCCompass -
  - 04: Deposit Account

**Funds Disbursement**

This value is most likely 05 to identify that the originator used a deposit account to fund the
disbursement.

**Credit Card Bill Payment**

This value must be 02, 03, 04, or 05.
 |
| senderInformation.account.number | string | no | The account number of the entity funding the transaction. It is the sender’s account number. It can
be a debit/credit card account number or bank account number.

**Funds disbursements and OCT transactions**

This field is optional.

**All other transactions**

This field is required when the sender funds the transaction with a financial instrument, for example
debit card.
Length:
* FDCCompass (<= 19)
* Paymentech (<= 16)
 |
| senderInformation.firstName | string | no | First name of the sender.
This field is applicable for AFT and OCT transactions. 

Only alpha numeric values are supported.Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to the processor.
 |
| senderInformation.middleInitial | string | no | Recipient middle initial (Optional).
 |
| senderInformation.middleName | string | no | Middle name of the sender.
This field is applicable for AFT and OCT transactions. 

Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.
 |
| senderInformation.lastName | string | no | Last name of the sender.
This field is applicable for AFT and OCT transactions.

Only alpha numeric values are supported. Special characters not in the standard ASCII character set, are not supported and will be stripped before being sent to sent to the processor.
 |
| senderInformation.name | string | no | Name of sender.

**Funds Disbursement**

This value is the name of the originator sending the funds disbursement.
* CTV, Paymentech (30)
 |
| senderInformation.address1 | string | no | Street address of sender.

**Funds Disbursement**

This value is the address of the originator sending the funds disbursement.
 |
| senderInformation.locality | string | no | City of sender.

**Funds Disbursement**

This value is the city of the originator sending the funds disbursement.
 |
| senderInformation.administrativeArea | string | no | Sender’s state. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).
 |
| senderInformation.countryCode | string | no | Country of sender. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).
* CTV (3)
 |
| senderInformation.postalCode | string | no | Sender’s postal code. Required only for FDCCompass. |
| senderInformation.phoneNumber | string | no | Sender’s phone number. Required only for FDCCompass. |
| senderInformation.dateOfBirth | string | no | Sender’s date of birth in YYYYMMDD format. Required only for FDCCompass. |
| senderInformation.vatRegistrationNumber | string | no | Customer's government-assigned tax identification number.
 |
| senderInformation.personalIdType | string | no | #### Visa Platform Connect
This tag will contain the type of sender identification.
The valid values are:
• BTHD (Date of birth)
• CUID (Customer identification (unspecified))
• NTID (National identification)
• PASN (Passport number)
• DRLN (Driver license)
• TXIN (Tax identification)
• CPNY (Company registration number)
• PRXY (Proxy identification)
• SSNB (Social security number)
• ARNB (Alien registration number)
• LAWE (Law enforcement identification)
• MILI (Military identification)
• TRVL (Travel identification (non-passport))
• EMAL (Email)
• PHON (Phone number)
 |
| senderInformation.type | string | no | #### Visa Platform Connect
This tag will denote whether the tax ID is a business or individual tax ID when personal ID Type contains the value of TXIN (Tax identification).

The valid values are:
• B (Business)
• I (Individual)
 |
| senderInformation.identificationNumber | string | no | #### Visa Platform Connect
This tag will contain an acquirer-populated value associated with the API : senderInformation.personalIdType which will identify the personal ID type of the sender.
 |
| senderInformation.aliasName | string | no | Sender's alias name. |
| processingInformation.businessApplicationId | string | no | Payouts transaction type.

Applicable Processors: FDC Compass, Paymentech, CtV

Possible values:

**Credit Card Bill Payment**

 - **CP**: credit card bill payment

**Funds Disbursement**

 - **FD**: funds disbursement
 - **GD**: government disbursement
 - **MD**: merchant disbursement

**Money Transfer**

 - **AA**: account to account. Sender and receiver are same person.
 - **PP**: person to person. Sender and receiver are different.

**Prepaid Load**

 - **TU**: top up
 |
| processingInformation.networkRoutingOrder | string | no | This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only.
The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order.
Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.

VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order.
If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer’s preference. 
If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer’s routing priorities. 
 |
| processingInformation.commerceIndicator | string | no | Type of transaction.

Value for an OCT transaction:
- `internet`
 |
| processingInformation.reconciliationId | string | no | Please check with Cybersource customer support to see if your merchant account is configured correctly so you
can include this field in your request.
* For Payouts: max length for FDCCompass is String (22).
 |
| processingInformation.payoutsOptions.acquirerMerchantId | string | no | This field identifies the card acceptor for defining the point of service terminal in both local and interchange environments. An acquirer-assigned code identifying the card acceptor for the transaction. 
Depending on the acquirer and merchant billing and reporting requirements, the code can represent a merchant, a specific merchant location, or a specific merchant location terminal.
Acquiring Institution Identification Code uniquely identifies the merchant.
The value from the original is required in any subsequent messages, including reversals, chargebacks, and representments.
* Applicable only for CTV for Payouts.
 |
| processingInformation.payoutsOptions.acquirerBin | string | no | This code identifies the financial institution acting as the acquirer of this customer transaction. The acquirer is the member or system user that signed the merchant or ADM or dispensed cash. 
This number is usually Visa-assigned.
* Applicable only for CTV for Payouts.
 |
| processingInformation.payoutsOptions.retrievalReferenceNumber | string | no | This field contains a number that is used with other data elements as a key to identify and track all messages related to a given cardholder transaction;
that is, to a given transaction set.

Format:
  Positions 1-4: The `yddd` equivalent of the date, where `y` = 0-9 and `ddd` = 001 – 366.
  Positions 5-12: A unique identification number generated by the merchant

* Applicable only for CTV for Payouts.
 |
| processingInformation.payoutsOptions.accountFundingReferenceId | string | no | Visa (maxLength of 15) or MasterCard (maxLength of 40) generated transaction identifier (TID) that is unique for each original authorization and financial request.
* Applicable only for CTV for Payouts.
 |
| processingInformation.payoutsOptions.deferredDateTime | string | no | #### Visa Platform Connect

Contains date and time value indicating scheduled deferred OCT.

Format is : 'yyyyMMddHHmm', where

'YYYY' = year
'MM' = month
'DD' = day
'hh' = hour
'mm' = minutes
 |
| processingInformation.transactionReason | string | no | Transaction reason code.
 |
| processingInformation.purposeOfPayment | string | no | This field is applicable for AFT and OCT transactions. For list of supported values, please refer to Developer Guide.
 |
| processingInformation.fundingOptions.initiator | object | no |  |
| processingInformation.languageCode | string | no | Contains the ISO 639-2 defined language Code
 |
| processingInformation.purchaseOptions.benefitAmount | string | no | Workplace benefit amount. |
| processingInformation.purchaseOptions.benefitType | string | no | Workplace benefit type.
Possible values:
- 70 = employee benefit
- 4T = transportation / transit
- 52 = general benefit
- 53 = meal voucher
- 54 = fuel
- 55 = ecological / sustainability
- 58 = philanthropy / patronage / consumption
- 59 = gift
- 5S = sport / culture
- 5T = book / education
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
| paymentInformation.card.type | string | no | Three-digit value that indicates the card type.

**IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is
optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.

Possible values:
- `001`: Visa. Use card type value `001` for Visa Electron.
- `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard.
- `003`: American Express
- `004`: Discover
- `005`: Diners Club
- `006`: Carte Blanche[^1]
- `007`: JCB[^1]
- `008`: Optima
- `009`: GE Private Label
- `010`: Beneficial Private Label
- `011`: Twinpay Credit Card
- `012`: Twinpay Debit Card
- `013`: WalMart
- `014`: Enroute[^1]
- `015`: Lowe's Consumer
- `016`: Home Depot Consumer
- `017`: MBNA
- `018`: Dick's Sportswear
- `019`: Casual Corner
- `020`: Sears
- `021`: JAL[^1]
- `023`: Disney Card
- `024`: Maestro (UK Domestic)[^1]
- `025`: Sam's Club Consumer
- `026`: Sam's Club Business
- `027`: Nico's
- `028`: Paymentech Bill Me Later
- `029`: Bebe
- `030`: Restoration Hardware
- `031`: Delta Online
- `032`: Solo
- `033`: Visa Electron[^1]. Do not use this value. Use `001` for all Visa card types.
- `034`: Dankort[^1]
- `035`: Laser
- `036`: Cartes Bancaires[^1,4]
- `037`: Carta Si[^1]
- `038`: Pinless Debit
- `039`: Encoded account number[^1]
- `040`: UATP[^1]
- `041`: HOUSEHOLD
- `042`: Maestro (International)[^1]
- `043`: GE MONEY
- `044`: Korean Cards
- `045`: Style Cards
- `046`: JCrew
- `047`: Payeasecn eWallet
- `048`: Payeasecn Bank Transfer
- `049`: Meijer
- `050`: Hipercard[^2,3]
- `051`: Aura
- `052`: Redecard
- `053`: Orico card
- `054`: Elo[^3]
- `055`: Capitol One Private Label
- `056`: Carnet
- `057`: Costco Private Label
- `058`: Carnet
- `059`: ValueLink
- `060`: MADA
- `061`: RuPay
- `062`: China UnionPay
- `063`: Falabella Private Label
- `064`: Prompt Card
- `065`: Korean Domestic
- `066`: Banricompras
- `067`: MEEZA
- `068`: PayPak
- `070`: EFTPOS
- `071`: Codensa
- `072`: Olimpica
- `073`: Colsubsidio
- `074`: Tuya
- `075`: Sodexo
- `076`: Naranja
- `077`: Cabal
- `078`: DINELCO
- `079`: PANAL
- `080`: EPM
- `081`: Jaywan

[^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit.
[^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5.
[^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit.
[^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.

#### Used by
**Authorization**
Required for Carte Blanche and JCB.
Optional for all other card types.

#### Card Present reply
This field is included in the reply message when the client software that is installed on the POS terminal uses
the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to
have your account enabled to receive these fields in the credit reply message.

Returned by the Credit service.

This reply field is only supported by the following processors:
- American Express Direct
- Credit Mutuel-CIC
- FDC Nashville Global
- OmniPay Direct
- SIX

#### Google Pay transactions
For PAN-based Google Pay transactions, this field is returned in the API response.

#### GPX
This field only supports transactions from the following card types:
- Visa
- Mastercard
- AMEX
- Discover
- Diners
- JCB
- Union Pay International
 |
| paymentInformation.card.number | string | no | The customer’s payment card number, also known as the Primary Account Number (PAN). You can also use this field
for encoded account numbers.

#### FDMS Nashville
Required. String (19)

#### GPX
Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured
for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine
whether a field is required for the transaction you are requesting.

#### All other processors
Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured
for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine
whether a field is required for the transaction you are requesting.
 |
| paymentInformation.card.expirationMonth | string | no | Two-digit month in which the payment card expires.

Format: `MM`.

Valid values: `01` through `12`. Leading 0 is required.

#### Barclays and Streamline
For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value
(`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is
in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause
the issuer to reject your request.

#### Encoded Account Numbers
For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.

#### FDMS Nashville
Required field.

#### All other processors
Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured
for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine
whether a field is required for the transaction you are requesting.

#### Google Pay transactions
For PAN-based Google Pay transactions, this field is returned in the API response.
 |
| paymentInformation.card.expirationYear | string | no | Four-digit year in which the payment card expires.

Format: `YYYY`.

#### Barclays and Streamline
For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.

#### Encoded Account Numbers
For encoded account numbers (**_type_**`=039`), if there is no expiration date on the card, use `2021`.

#### FDMS Nashville
Required field.

#### FDC Nashville Global and FDMS South
You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.

#### All other processors
Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured
for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine
whether a field is required for the transaction you are requesting.

#### Google Pay transactions
For PAN-based Google Pay transactions, this field is returned in the API response.
 |
| paymentInformation.card.sourceAccountType | string | no | Flag that specifies the type of account associated with the card. 
The cardholder provides this information during the payment process.

This field is required in the following cases:
  - Debit transactions on Cielo and Comercio Latino.
  - Transactions with Brazilian-issued cards on CyberSource through VisaNet.
  - Applicable only for CyberSource through VisaNet (CtV).

**Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank
identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or
credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends
that you include this field for combo card transactions.

Possible values include the following.

 - `CH`: Checking account
 - `CR`: Credit card account
 - `SA`: Saving account
 - `LI`: Line of credit or credit portion of combo card
 - `PP`: Prepaid card account or prepaid portion of combo card
 - `UA`: Universal account

If useAs is set to credit/debit and there is a value in SourceAccountType, the value in the SourceAccountType field will take precedence.
If useAs is set to CR/DB and there is a value in SourceAccountType, the value in the useAs field will take precedence.
 |
| paymentInformation.customer.customerId | string | no | Unique identifier for the customer's card and billing information.

When you use Payment Tokenization or Recurring Billing and you include this value in
your request, many of the fields that are normally required for an authorization or credit
become optional.

**NOTE** When you use Payment Tokenization or Recurring Billing, the value for the Customer ID is actually the Cybersource payment token for a customer. This token stores information such as the consumer’s card number so it can be applied towards bill payments, recurring payments, or one-time payments. By using this token in a payment API request, the merchant doesn't need to pass in data such as the card number or expiration date in the request itself.
 |
| paymentInformation.customer.id | string | no | Unique identifier for the Customer token used in the transaction.
When you include this value in your request, many of the fields that are normally required for an authorization or credit
become optional.
 |
| paymentInformation.paymentInstrument.id | string | no | Unique identifier for the Payment Instrument token used in the transaction.
When you include this value in your request, many of the fields that are normally required for an authorization or credit
become optional.
 |
| paymentInformation.instrumentIdentifier.id | string | no | Unique identifier for the Instrument Identifier token used in the transaction.
When you include this value in your request, many of the fields that can be supplied for an authorization or credit
become optional.
 |
| paymentInformation.instrumentIdentifier.state | string | no | Issuers state for the card number.
Valid values:
- ACTIVE
- CLOSED : The account has been closed.
 |
| paymentInformation.tokenizedCard.number | string | no | Customer’s payment network token value.
 |
| paymentInformation.tokenizedCard.expirationMonth | string | no | One of two possible meanings:
- The two-digit month in which a token expires.
- The two-digit month in which a card expires.
Format: `MM`
Possible values: `01` through `12`

**NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.

#### Barclays and Streamline
For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.

#### Encoded Account Numbers
For encoded account numbers (`card_type=039`), if there is no expiration date on the card, use `12`.\
**Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.

#### Samsung Pay and Apple Pay
Month in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.
 |
| paymentInformation.tokenizedCard.expirationYear | string | no | One of two possible meanings:
- The four-digit year in which a token expires.
- The four-digit year in which a card expires.
Format: `YYYY`
Possible values: `1900` through `3000`
Data type: Non-negative integer

**NOTE** The meaning of this field is dependent on the payment processor that is returning the value in an authorization reply. Please see the processor-specific details below.

#### Barclays and Streamline
For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (1900 through
3000) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.

#### Encoded Account Numbers
For encoded account numbers (`card_ type=039`), if there is no expiration date on the card, use `2021`.

#### FDC Nashville Global and FDMS South
You can send in 2 digits or 4 digits. When you send in 2 digits, they must be the last 2 digits of
the year.

#### Samsung Pay and Apple Pay
Year in which the token expires. CyberSource includes this field in the reply message when it decrypts the payment blob for the tokenized transaction.

**Important** It is your responsibility to determine whether a field is required for the transaction
you are requesting.
 |
| paymentInformation.tokenizedCard.type | string | no | Three-digit value that indicates the card type.

**IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is
optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.

Possible values:
- `001`: Visa. Use card type value `001` for Visa Electron.
- `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard.
- `003`: American Express
- `004`: Discover
- `005`: Diners Club
- `006`: Carte Blanche[^1]
- `007`: JCB[^1]
- `008`: Optima
- `009`: GE Private Label
- `010`: Beneficial Private Label
- `011`: Twinpay Credit Card
- `012`: Twinpay Debit Card
- `013`: WalMart
- `014`: Enroute[^1]
- `015`: Lowe's Consumer
- `016`: Home Depot Consumer
- `017`: MBNA
- `018`: Dick's Sportswear
- `019`: Casual Corner
- `020`: Sears
- `021`: JAL[^1]
- `023`: Disney Card
- `024`: Maestro (UK Domestic)[^1]
- `025`: Sam's Club Consumer
- `026`: Sam's Club Business
- `027`: Nico's
- `028`: Paymentech Bill Me Later
- `029`: Bebe
- `030`: Restoration Hardware
- `031`: Delta Online
- `032`: Solo
- `033`: Visa Electron[^1]. Do not use this value. Use `001` for all Visa card types.
- `034`: Dankort[^1]
- `035`: Laser
- `036`: Cartes Bancaires[^1,4]
- `037`: Carta Si[^1]
- `038`: Pinless Debit
- `039`: Encoded account number[^1]
- `040`: UATP[^1]
- `041`: HOUSEHOLD
- `042`: Maestro (International)[^1]
- `043`: GE MONEY
- `044`: Korean Cards
- `045`: Style Cards
- `046`: JCrew
- `047`: Payeasecn eWallet
- `048`: Payeasecn Bank Transfer
- `049`: Meijer
- `050`: Hipercard[^2,3]
- `051`: Aura
- `052`: Redecard
- `053`: Orico card
- `054`: Elo[^3]
- `055`: Capitol One Private Label
- `056`: Carnet
- `057`: Costco Private Label
- `058`: Carnet
- `059`: ValueLink
- `060`: MADA
- `061`: RuPay
- `062`: China UnionPay
- `063`: Falabella Private Label
- `064`: Prompt Card
- `065`: Korean Domestic
- `066`: Banricompras
- `067`: MEEZA
- `068`: PayPak
- `070`: EFTPOS
- `071`: Codensa
- `072`: Olimpica
- `073`: Colsubsidio
- `074`: Tuya
- `075`: Sodexo
- `076`: Naranja
- `077`: Cabal
- `078`: DINELCO
- `079`: PANAL
- `080`: EPM
- `081`: Jaywan

[^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit.
[^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5.
[^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit.
[^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.

#### Used by
**Authorization**
Required for Carte Blanche and JCB.
Optional for all other card types.

#### Card Present reply
This field is included in the reply message when the client software that is installed on the POS terminal uses
the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to
have your account enabled to receive these fields in the credit reply message.

Returned by the Credit service.

This reply field is only supported by the following processors:
- American Express Direct
- Credit Mutuel-CIC
- FDC Nashville Global
- OmniPay Direct
- SIX

#### Google Pay transactions
For PAN-based Google Pay transactions, this field is returned in the API response.

#### GPX
This field only supports transactions from the following card types:
- Visa
- Mastercard
- AMEX
- Discover
- Diners
- JCB
- Union Pay International
 |
| paymentInformation.tokenizedCard.cryptogram | string | no | This field contains token information. |
| paymentInformation.tokenizedCard.requestorId | string | no | Value that identifies your business and indicates that the cardholder’s account number is tokenized. This value
is assigned by the token service provider and is unique within the token service provider’s database.

**Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.

#### PIN debit
Optional field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used.
 |
| paymentInformation.tokenizedCard.transactionType | string | no | Type of transaction that provided the token data. This value does not specify the token service provider; it specifies the entity that
provided you with information about the token.

Possible value:
- `2`: Near-field communication (NFC) transaction. The customer’s mobile device provided the token data for a contactless EMV transaction. For recurring
transactions, use this value if the original transaction was a contactless EMV transaction.

#### Visa Platform Connect
- `1`: For Rupay and In App tokenization. Example: InApp apple pay.
- `3`: Card/Credential On File Tokenization.

**NOTE** No CyberSource through VisaNet acquirers support EMV at this time.

Required field for PIN debit credit or PIN debit purchase transactions that use payment network tokens; otherwise, not used.

#### Rupay
- `3`: Card/Credential On File Tokenization.
- `4`: Tokenizined Transaction. Should be used for Guest Checkout transactions with token.
 |
| paymentInformation.tokenizedCard.assuranceLevel | string | no | Confidence level of the tokenization. This value is assigned by the token service provider.

**Note** This field is supported only for **CyberSource through VisaNet** and **FDC Nashville Global**.

Returned by PIN debit credit or PIN debit purchase.

**Note** Merchants supported for **CyberSource through VisaNet**/**Visa Platform Connect** are advised not to use this field.
 |
| paymentInformation.tokenizedCard.storageMethod | string | no | Type of technology used in the device to store token data. Possible values:

- `001`: Secure Element (SE). Smart card or memory with restricted access and encryption to prevent data tampering. For storing payment
   credentials, a SE is tested against a set of requirements defined by the payment networks.

   **Note** This field is supported only for _FDC Compass_.

- 002: Host Card Emulation (HCE). Emulation of a smart card by using software to create a virtual and exact representation of the card.
Sensitive data is stored in a database that is hosted in the cloud. For storing payment credentials, a database
must meet very stringent security requirements that exceed PCI DSS.

**Note** This field is supported only for _FDC Compass_.
 |
| paymentInformation.tokenizedCard.securityCode | string | no | Card Verification Number (CVN).

#### Ingenico ePayments
Do not include this field when **commerceIndicator=recurring**.
**Note** Ingenico ePayments was previously called _Global Collect_.
 |
| paymentInformation.tokenizedCard.securityCodeIndicator | string | no | Indicates whether a CVN code was sent. Possible values:

 - `0` (default): CVN service not requested. This default value is used when you do not include
     `securityCode` field in the request.
 - `1` (default): CVN service requested and supported. This default value is used when you include
     `securityCode` field in the request.
 - `2`: CVN on credit card is illegible.
 - `9`: CVN was not imprinted on credit card.

#### FDMS Nashville
Required for American Express cards; otherwise, optional.

#### TSYS Acquiring Solutions
Optional if `pointOfSaleInformation.entryMode=keyed`; otherwise, not used.

#### All other processors
Optional.
 |
| paymentInformation.tokenizedCard.assuranceMethod | string | no | Confidence level of the tokenization. This value is assigned by the token service provider.

**Note** This field is supported only for **Visa Platform Connect**
 |
| aggregatorInformation.aggregatorId | string | no | Value that identifies you as a payment aggregator. Get this value from the processor.
 |
| aggregatorInformation.name | string | no | Your payment aggregator business name. This field is conditionally required when aggregator id is present.
 |
| aggregatorInformation.independentSalesOrganizationID | string | no | Independent sales organization ID.
This field is only used for Mastercard transactions submitted through PPGS.
 |
| aggregatorInformation.subMerchant.id | string | no | The ID you assigned to your sub-merchant.
 |
| aggregatorInformation.streetAddress | string | no | Acquirer street name. |
| aggregatorInformation.city | string | no | Acquirer city. |
| aggregatorInformation.state | string | no | Acquirer state. |
| aggregatorInformation.postalCode | string | no | Acquirer postal code. |
| aggregatorInformation.country | string | no | Acquirer country. |

## Response

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| _links.self.href | string | no | This is the endpoint of the resource that was created by the successful request. |
| _links.self.method | string | no | `method` refers to the HTTP method that you can send to the `self` endpoint to retrieve details of the resource. |
| id | string | no | An unique identification number generated by Cybersource to identify the submitted request. Returned by all services.
It is also appended to the endpoint of the resource.
On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.
 |
| submitTimeUtc | string | no | Time of request in UTC. `Format: YYYY-MM-DDThh:mm:ssZ`

Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the
time. The Z indicates UTC.
 |
| status | string | no | The status of the submitted transaction.

Possible values:
 - ACCEPTED
 - DECLINED
 - INVALID_REQUEST
 |
| reconciliationId | string | no | Cybersource or merchant generated transaction reference number. This is sent to the processor and is echoed back in the response to the merchant. This is
This value is used for reconciliation purposes.
 |
| errorInformation.reason | string | no | The reason of the status.

Possible values:
 - EXPIRED_CARD
 - PROCESSOR_DECLINED
 - STOLEN_LOST_CARD
 - UNAUTHORIZED_CARD
 - CVN_NOT_MATCH
 - INVALID_CVN
 - BLOCKED_BY_CARDHOLDER
 - BLACKLISTED_CUSTOMER
 - INVALID_ACCOUNT
 - GENERAL_DECLINE
 - RISK_CONTROL_DECLINE
 - PROCESSOR_RISK_CONTROL_DECLINE
 - ALLOWABLE_PIN_RETRIES_EXCEEDED
 - PROCESSOR_ERROR
 |
| errorInformation.message | string | no | The detail message related to the status and reason listed above. |
| errorInformation.details | array | no |  |
| clientReferenceInformation.code | string | no | Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each
transaction so that you can perform meaningful searches for the transaction.

#### Used by
**Authorization**
Required field.

#### PIN Debit
Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being
reversed.

Required field for all PIN Debit requests (purchase, credit, and reversal).

#### FDC Nashville Global
Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports.
 |
| clientReferenceInformation.submitLocalDateTime | string | no | Date and time at your physical location.

Format: `YYYYMMDDhhmmss`, where YYYY = year, MM = month, DD = day, hh = hour, mm = minutes ss = seconds

#### PIN Debit
Optional field for PIN Debit purchase and credit requests.
 |
| clientReferenceInformation.ownerMerchantId | string | no | Merchant ID that was used to create the subscription or customer profile for which the service was requested.

If your CyberSource account is enabled for Recurring Billing, this field is returned only if you are using
subscription sharing and if your merchant ID is in the same merchant ID pool as the owner merchant ID.

If your CyberSource account is enabled for Payment Tokenization, this field is returned only if you are using
profile sharing and if your merchant ID is in the same merchant ID pool as the owner merchant ID.
 |
| merchantInformation.merchantDescriptor.name | string | no | Your merchant name.

**Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22.

#### PIN debit
Your business name. This name is displayed on the cardholder’s statement. When you
include more than one consecutive space, extra spaces are removed.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

Optional field for PIN debit credit or PIN debit purchase requests.

#### Airline processing
Your merchant name. This name is displayed on the cardholder’s statement. When you include more than one consecutive space, extra spaces are removed.

**Note** Some airline fee programs may require the original ticket number (ticket identifier) or the ancillary service description in positions 13 through 23 of this field.

**Important** This value must consist of English characters.

Required for captures and credits.
 |
| merchantInformation.merchantDescriptor.locality | string | no | Merchant's City.

#### PIN debit
City for your business location. This value might be displayed on the cardholder’s statement.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.

Optional field for PIN debit credit or PIN debit purchase requests.
 |
| merchantInformation.merchantDescriptor.country | string | no | Merchant's country.

#### PIN debit
Country code for your business location. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)
This value might be displayed on the cardholder’s statement.

When you do not include this value in your PIN debit request, the merchant name from your account is used.
**Important** This value must consist of English characters.
**Note** If your business is located in the U.S. or Canada and you include this field in a
request, you must also include `merchantInformation.merchantDescriptor.administrativeArea`.

Optional field for PIN debit credit or PIN debit purchase.
 |
| orderInformation.amountDetails.totalAmount | string | no | Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters.
CyberSource truncates the amount to the correct number of decimal places.

**Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.

**Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths.

If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. 

#### Card Present
Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.

#### Invoicing / Pay By Link
Required for creating a new invoice or payment link.

#### PIN Debit
Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.

Required field for PIN Debit purchase and PIN Debit credit requests.
Optional field for PIN Debit reversal requests.

#### GPX
This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.

#### DCC with a Third-Party Provider
Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. 

#### DCC for First Data
Not used.
 |
| orderInformation.amountDetails.currency | string | no | Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)

#### Used by
**Authorization**
Required field.

**Authorization Reversal**
For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.

#### PIN Debit
Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).
Returned by PIN debit purchase.

For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing.
For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).

Required field for PIN Debit purchase and PIN Debit credit requests.
Optional field for PIN Debit reversal requests.

#### GPX
This field is optional for reversing an authorization or credit.

#### DCC for First Data
Your local currency.

#### Tax Calculation
Required for international tax and value added tax only.
Optional for U.S. and Canadian taxes.
Your local currency.
 |
| orderInformation.amountDetails.settlementAmount | string | no | This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder’s account.
This field is returned for OCT transactions.
 |
| orderInformation.amountDetails.settlementCurrency | string | no | This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account.
This field is returned for OCT transactions.
 |
| processorInformation.approvalCode | string | no | Issuer-generated approval code for the transaction. |
| processorInformation.responseCode | string | no | Transaction status from the processor. |
| processorInformation.transactionId | string | no | Network transaction identifier (TID). This value can be used to identify a specific transaction when
you are discussing the transaction with your processor.
 |
| processorInformation.systemTraceAuditNumber | string | no | This field is returned only for **American Express Direct** and **CyberSource through VisaNet**.
Returned by authorization and incremental authorization services.

#### American Express Direct

System trace audit number (STAN). This value identifies the transaction and is useful when investigating a
chargeback dispute.

#### CyberSource through VisaNet

System trace number that must be printed on the customer’s receipt.
 |
| processorInformation.responseCodeSource | string | no | Used by Visa only and contains the response source/reason code that identifies the source of the response decision.
 |
| processorInformation.merchantAdvice.code | string | no | - Merchant should update their retry logic to ensure retry is not attempted for the cards for which Issuer won’t approve the transactions and where the retry is allowed.
- Card Processing Associations provides this data which is being passed through in the following data element irrespective of the Card Associations.   Usage of this data must be always associated with the Card Associations card types for merchant processing retry logic.
- In additions to the Merchant Advice code, Associations also provides the decline response codes which provides the reason for decline.  Association response code will be a pass-through value.

#### Processors supported:
  - HSBC
  - Barclays
  - FDC Nash
  - FDI Global
  - Elavon America
  - VPC
  - Rede
  - Payment tech Salem


#### Possible values:
| Card Type   | Advice Code   |  Description                                |
| ----------- | ------------- | ------------------------------------------- |
| VISA        | 1             | Issuer never approves                       |
| VISA        | 2             | Issuer cannot approve at this time          |
| VISA        | 3             | Data quality/revalidate payment information |
| MasterCard  | 01            | New account information available           |
| MasterCard  | 02            | Try Again Later                             |
| MasterCard  | 03            | Do Not Try Again                            |
| MasterCard  | 04            | Token not supported                         |
| MasterCard  | 21            | Do not honor                                |
| MasterCard  | 22            | Merchant does not qualify for product code  |
| MasterCard  | 24            | Retry after 1 hour                          |
| MasterCard  | 25            | Retry after 24 hours                        |
| MasterCard  | 26            | Retry after 2 days                          |
| MasterCard  | 27            | Retry after 4 days                          |
| MasterCard  | 28            | Retry after 6 days                          |
| MasterCard  | 29            | Retry after 8 days                          |
| MasterCard  | 30            | Retry after 10 days                         |
| MasterCard  | 40            | Consumer non-reloadable prepaid card        |
| MasterCard  | 41            | Consumer single-use virtual card number     |
| MasterCard  | 42            | Sanctions score exceeds threshold value     |
| MasterCard  | 99            | Do Not Try Again                            |

#### Possbile values for Barclays processor:
- 00: No information, or response not provided.
- 01: New account information available
- 02: Try again later
- 03: Do not try again
- 05: Payment blocked by the payment card company
 |
| processorInformation.merchantAdvice.codeRaw | string | no | Raw merchant advice code sent directly from the processor. This field is used only for Mastercard.

#### CyberSource through VisaNet
The value for this field corresponds to the following data in the TC 33 capture file1:
- Record: CP01 TCR7
- Position: 96-99
- Field: Response Data-Merchant Advice Code

#### Possbile values for Barclays processor:
- 01: Updated/additional information needed
- 02: Cannot approve at this time; try again later
- 04: Do not try again
- 08: Payment blocked by card scheme
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
| recipientInformation.card.balance | string | no | This field shows the available balance in the prepaid account.
Acquirers always receive the available balance in the transaction currency.
 |
| recipientInformation.card.currency | string | no | This field indicates the 3-letter [ISO Standard Currency Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) for the card currency.
 |
| issuerInformation.octDomesticParticipantIndicator | boolean | no | Domestic indicator for Push funds (OCT). If no Funds Transfer Attributes Inquiry data is available
for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octCrossBorderParticipantIndicator | boolean | no | Cross-border indicator for push funds (OCT). If no Funds Transfer Attributes Inquiry data is available
for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octMoneyTransferDomesticIndicator | boolean | no | Indicates whether domestic money transfer OCTs (push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted.
      
Supported for Visa Direct.
 |
| issuerInformation.octMoneyTransferCrossBorderIndicator | boolean | no | Indicates whether cross-border money transfer OCTs (push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octMoneyTransferFastFundsDomesticIndicator | boolean | no | Indicates whether domestic money transfer OCTs (fast push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octMoneyTransferFastFundsCrossBorderIndicator | boolean | no | Indicates whether cross-border money transfer OCTs (fast push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octMoneyTransferMerchantCountryRestricted | boolean | no | This field indicates if the recipient issuer can accept push funds (OCT) transactions from the merchant country. 
If no Funds Transfer Attributes Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octNonMoneyTransferDomesticIndicator | boolean | no | Indicates whether domestic non-money transfer OCTs (push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octNonMoneyTransferCrossBorderIndicator | boolean | no | Indicates whether cross-border non-money transfer OCTs (push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octNonMoneyTransferFastFundsDomesticIndicator | boolean | no | Indicates whether domestic non-money transfer OCTs (fast push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octNonMoneyTransferFastFundsCrossBorderIndicator | boolean | no | Indicates whether cross-border non-money transfer OCTs (fast push funds) are allowed. If no Funds Transfer
Attributes Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octOnlineGamblingDomesticIndicator | boolean | no | Indicates whether domestic gambling OCTs (push funds) are allowed. If no Funds Transfer Attributes Inquiry
data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octOnlineGamblingCrossBorderIndicator | boolean | no | Indicates whether cross-border gambling OCTs (push funds) are allowed. If no Funds Transfer Attributes Inquiry
data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octOnlineGamblingFastFundsDomesticIndicator | boolean | no | Indicates whether domestic gambling OCTs (fast push funds) are allowed. If no Funds Transfer Attributes Inquiry
data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.octOnlineGamblingFastFundsCrossBorderIndicator | boolean | no | Indicates whether cross-border gambling OCTs (fast push funds) are allowed. If no Funds Transfer Attributes
Inquiry data is available for this card account, the field is omitted. 

Supported for Visa Direct.
 |
| issuerInformation.serviceProcessingType | string | no | This field contains values that identify the service type under which the transaction should be processed.
The valid value for the Visa Alias Directory Service is A0 (Alias) and 00 (normal transaction).
 |
| tokenInformation.instrumentidentifierNew | boolean | no | A value of true means the card number or bank account used to create an Instrument Identifier was new and did not already exist in the token vault.
A value of false means the card number or bank account used to create an Instrument Identifier already existed in the token vault.
 |
| tokenInformation.customer.id | string | no | Unique identifier for the Customer token that was created as part of a bundled TOKEN_CREATE action.
 |
| tokenInformation.paymentInstrument.id | string | no | Unique identifier for the Payment Instrument token that was created as part of a bundled TOKEN_CREATE action.
 |
| tokenInformation.shippingAddress.id | string | no | Unique identifier for the Customers Shipping Address token that was created as part of a bundled TOKEN_CREATE action.
 |
| tokenInformation.instrumentIdentifier.id | string | no | Unique identifier for the Instrument Identifier token that was created as part of a bundled TOKEN_CREATE action.
 |
| tokenInformation.instrumentIdentifier.state | string | no | Issuers state for the card number.
Valid values:
- ACTIVE
- CLOSED : The account has been closed.
 |
| tokenInformation.thirdPartyToken.source | string | no | This field identifies the third party that provided the Third Party Token identification value.
 |
| tokenInformation.thirdPartyToken.id | string | no | When a third party is being used for tokenization, this field contains the token ID. See tokenInformation.thirdPartyToken.source to identify the provider.
 |
| processingInformation.purchaseOptions.benefitAmount | string | no | Workplace benefit amount. |
| processingInformation.purchaseOptions.benefitType | string | no | Workplace benefit type.
Possible values:
- 70 = employee benefit
- 4T = transportation / transit
- 52 = general benefit
- 53 = meal voucher
- 54 = fuel
- 55 = ecological / sustainability
- 58 = philanthropy / patronage / consumption
- 59 = gift
- 5S = sport / culture
- 5T = book / education
 |

## Errors

- `unspecified`: No explicit error schema in fixture — recovery: Treat non-2xx as failure; do not log secrets

## Evidence (from spec)

> "Process a Payout"

> "Send funds from a selected funding source to a designated credit/debit card account or a prepaid card using an Original Credit Transaction (OCT).
The availability of API features f"

## Provenance

- `lineage_origin`: `generated_from_spec`
- `unit_id`: `cybersource-payments-openapi:ref:octCreatePayment`
- `api_name`: CyberSource Payments API (/pts)

Every fact on this page traces to the OpenAPI-derived reference unit. Sandbox only — do not use production credentials from these docs.

<!-- /section:facts -->
