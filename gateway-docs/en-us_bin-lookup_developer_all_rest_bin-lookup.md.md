BIN Lookup Service Developer Guide {#bin-lookup-about-guide}
============================================================

About This Guide
:
This section describes how to use this developer guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to use the `REST API` to integrate the BIN Lookup Service into an order management system.

    Implementing the `Payment Gateway` payment services requires software development skills. You must write code that uses the API request and response fields to integrate the credit card services into your existing order management system.

Conventions
:
These statements appear in this document:
> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

    > WARNING
    > A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Related Documentation
:
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:  
<http://support.example.com>

Limited Availability Release {#bin-lookup-la-release}
=====================================================

This document provides information about the limited availability release of the BIN Lookup Service REST API.

Recent Revisions to This Document {#bin-lookup-doc-revisions}
=============================================================

25.06.01
--------

Test BINs
:
Added the test BIN for PayPak cards. See [Test BINs for the BIN Lookup Service](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-req-task/bin-lookup-test-proc/bin-lookup-service-test.md "").

24.02
-----

Test BINs
:
Removed unsupported test BINs.
:
Updated test BIN 679999 to Maestro. See [Test BINs for the BIN Lookup Service](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-req-task/bin-lookup-test-proc/bin-lookup-service-test.md "").

24.01
-----

Health Card Test BINs
:
Added health card test BINs. See [Test BINs for the BIN Lookup Service](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-req-task/bin-lookup-test-proc/bin-lookup-service-test.md "").
:
Added example request for BIN Lookup Service with a Health Card Number. See [Examples: Requests to the BIN Lookup Service Using the REST API](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-req-task/bin-lookup-card-example.md "").
:
Updated response fields to include paymentAccountInformation.features.healthCard and paymentAccountInformation.features.corporatePurchase. See [Response Fields for the BIN Lookup Service Using the REST API](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-reference-intro/bin-lookup-resp-fields.md "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to the BIN Lookup Service {#bin-lookup-intro}
==========================================================

The BIN Lookup Service provides payment card account information based on a *bank identification number* (BIN) and account range information. The BIN represents the first six or eight digits on the payment card. The first digit of the BIN is the industry identifier for the network used by the card-issuing institution. The remaining five or seven digits of the BIN identify the card-issuing institution and some of the card attributes.  
You can request the BIN Lookup Service using a payment card number (PAN), BIN, network token, Token Management Service (TMS) token, or `Secure Acceptance` transient token.  
For more information about TMS, see the [Token Management Service API reference](https://developer.example.com/api-reference-assets/index.md?stage=pilot#token-management "") or the [Token Management Services Developer Guide](https://developer.example.com/docs/gateway/en-us/tms/developer/ctv/rest/tms/tms-about-guide.md "").  
For more information about `Secure Acceptance` transient tokens, see the [`Digital Accept` Secure Integration Developer Guide](https://developer.example.com/docs/gateway/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/da-about-guide.md "").  
BIN lookup service returns BIN attribute information for the payment credential specified in the request, such as:

* Card type code
* Card brand, such as American Express, Mastercard, or Relay
* Card currency
* Account funding source, such as credit or debit
* Account prefix
* Payment credential type
* Issuer BIN length (network dependent)
* Issuer name
* Issuer country
* Issuer phone number
* Fast funds eligibility (if enabled)

Prerequisites {#bin-lookup-prereq}
==================================

Before you begin using the BIN Lookup Service:

* Know the REST APIs on the [Getting Started with REST Developer Guide](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").
* Create an evaluation account on the sandbox account sign up web page at [https://developer.example.com/hello-world/sandbox.html](https://developer.example.com/hello-world/sandbox.md "").

Requesting the BIN Lookup Service Using the REST API {#bin-lookup-req-task}
===========================================================================

`Payment Gateway` recommends that you send the full payment card number (PAN), a TMS token, or a network token when you request the BIN Lookup Service. This ensures that a single BIN record is identified during the request. Even though the service supports sending the six-digit or eight-digit card prefix in the request, this option can result in a `MULTIPLE` record match error if a single BIN record cannot be identified.

> IMPORTANT
> When you receive a ` MULTIPLE ` status record match error, we recommend you provide the full payment card number, a TMS token, or a network token to receive a ` SUCCESS ` status in the response.  
> Send one of these payment credentials to the BIN Lookup Service to get the payment card account information.  
> **Payment Card Numbers**

* Full payment card number (recommended best practice)

* Eight-digit card prefix (not recommended because it might result in a `MULTIPLE` status record match error)

* Six-digit card prefix (not recommended because this option can result in a `MULTIPLE` status record match error)  
  **Tokens**

* `TMS` customer ID token

* `TMS` payment instrument token

* `TMS` instrument identifier token

* `TMS` jti transient token

* `Flex API` JWT transient token

* Network tokens (Relay VTS, Mastercard MDES, and Discover)  
  Follow these steps to request the BIN Lookup Service:

1. Send the request to the BIN Lookup Service endpoint:

   #### ADDITIONAL INFORMATION

   `POST https://&lt;``url_prefix``&gt;/bin/v1/binlookup`

   #### ADDITIONAL INFORMATION

   Use one of these URL prefixes:

   * Test: `apitest.example.com`
   * Production: `api.example.com`
   * Production in India: `api.in.example.com`
2. Include one of the prerequisite fields in the request:

   * paymentInformation.card.number (Full payment card number is recommended.)
   * paymentInformation.customer.id
   * paymentInformation.instrumentIdentifier.id
   * paymentInformation.paymentInstrument.id
   * tokenInformation.jti
   * tokenInformation.transientTokenJwt
     {#bin-lookup-req-task_choices_az2_s4v_f5b}
3. Include optional fields in the request as needed.

4. Check the response message to make sure that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [BIN Lookup Response Codes](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-reference-intro/bin-lookup-resp-codes.md "").

Required Fields for the BIN Lookup Service Using the REST API {#bin-lookup-service-fields}
==========================================================================================

Include one of these payment credential fields in the request for the BIN Lookup Service:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:
Set this field to the full payment card number (recommended) or network token.

[paymentInformation.customer.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

Optional Fields for the BIN Lookup Service Using the REST API {#bin-lookup-opt-fields}
======================================================================================

These fields are optional for a BIN Lookup Service request:

[paymentAccountInformation.network.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-network-id.md "")
:

[processingInformation.binSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-bin-source.md "")
:

Testing the BIN Lookup Service {#bin-lookup-test-proc}
======================================================

`Payment Gateway` provides test BINs for requesting the BIN Lookup Service in the test environment. Do not use real payment card numbers.

Test BINs for the BIN Lookup Service {#bin-lookup-service-test}
===============================================================

Use the BINs below to test the BIN Lookup Service at the test endpoint:
`https://apitest.example.com``/bin/v1/binlookup`

| BIN      | Card Type  | Card Platform and/or Product          | Issuer Country | Account Funding Source | Eight-Digit BIN Results | PAN/Network Token |
|:---------|:-----------|:--------------------------------------|:---------------|:-----------------------|:------------------------|:------------------|
| 442780   | Relay       | Classic                               | US             | Credit                 | ---                     | PAN               |
| 476173   | Relay       | Classic                               | US             | Credit                 | ---                     | PAN               |
| 541333   | Mastercard | Classic                               | US             | Credit                 | ---                     | PAN               |
| 545721   | Mastercard | Classic                               | US             | Credit                 | ---                     | PAN               |
| 679999   | Maestro    | Classic                               | US             | Credit                 | ---                     | PAN               |
| 22055310 | PayPak     | ---                                   | PK             | Debit                  | ---                     | PAN               |
| 36126700 | Diners     | Consumer Prepaid Non-reloadable Cards | PL             | Prepaid                | ---                     | PAN               |
| 36161200 | Diners     | Consumer Debit Cards                  | AM             | Debit                  | ---                     | PAN               |
| 36722600 | Diners     | Commercial Debit Cards                | ZA             | Debit                  | ---                     | PAN               |
| 39009100 | Diners     | Consumer Prepaid Reloadable Cards     | US             | Prepaid                | ---                     | PAN               |
| 48127900 | Relay       | Relay Classic                          | MX             | Debit                  | Yes                     | PAN               |
| 49134300 | Relay       | Relay Classic                          | MX             | Credit                 | Yes                     | PAN               |
| 49134400 | Relay       | Relay Classic                          | MX             | Debit                  | Yes                     | PAN               |
| 49134600 | Relay       | Relay Classic                          | MX             | Credit                 | Yes                     | PAN               |
| 52884300 | Mastercard | Classic                               | MX             | Credit                 | Yes                     | PAN               |
| 54823400 | Mastercard | Business                              | MX             | Credit                 | Yes                     | PAN               |
| 62232000 | CUP        | Consumer Prepaid Reloadable Cards     | US             | Prepaid                | ---                     | PAN               |
| 62630000 | CUP        | Consumer Debit Cards                  | US             | Debit                  | ---                     | PAN               |
| 40014600 | Relay       | Relay Classic                          | US             | Debit                  | Yes                     | Token             |
| 61900950 | Discover   | Premium Plus Cards                    | US             | Credit                 | ---                     | Token             |
| 4288300  | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 4288301  | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42882103 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42882104 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42882105 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42882106 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42882137 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889001 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889002 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889003 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889004 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889005 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889006 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889007 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889008 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
| 42889009 | Relay       | Health Card                           | US             | Debit or Prepaid       | ---                     | PAN               |
[Test BINs and Card Information]

Examples: Requests to the BIN Lookup Service Using the REST API {#bin-lookup-card-example}
==========================================================================================

These examples show various BIN lookup requests and successful responses. Request Example: BIN Lookup Service with a Full Payment Card Number

```
{
  "paymentInformation": {
    "card": {
      "number": "4111111111111111"
    }
  }
}            
```

Response 201 Example: Successful BIN Lookup Service with a Full Payment Card Number

```
{
  "id": "7187318127246929204951",
  "submitTimeUtc": "2024-06-18T05:30:12Z",
  "status": "COMPLETED",
  "paymentAccountInformation": {
    "card": {
      "type": "001",
      "brandName": "CARD",
      "maxLength": "16",
      "credentialType": "PAN"
    },
    "features": {
      "accountFundingSource": "DEBIT",
      "cardPlatform": "CONSUMER",
      "cardProduct": "Relay Classic"
    }
  },
  "issuerInformation": {
    "name": "CONOTOXIA SP. Z O.O",
    "country": "PL",
    "binLength": "6",
    "accountPrefix": "41111111"
  }
}
```

Request Example: BIN Lookup Service with a Health Card Number

```
{
  "paymentInformation": {
    "card": {
      "number": "4288900100000"
    }
  }
} 
```

Response 201 Example: Successful BIN Lookup Service with a Health Card Number

```
{
  "id": "7187371922356613504951",
  "submitTimeUtc": "2024-06-18T06:59:52Z",
  "status": "COMPLETED",
  "paymentAccountInformation": {
    "card": {
      "type": "001",
      "brandName": "CARD",
      "maxLength": "16",
      "currency": "USD",
      "credentialType": "PAN"
    },
    "features": {
      "accountFundingSource": "CREDIT",
      "cardPlatform": "COMMERCIAL",
      "cardProduct": "Relay Purchasing",
      "healthCard": true
    }
  },
  "issuerInformation": {
    "name": "BANKUNITED, NATIONAL ASSOCIATION",
    "country": "US",
    "binLength": "6",
    "accountPrefix": "42889001"
  }
}
```

Request Example: BIN Lookup Service with a Network Token

```
{
  "paymentInformation": {
    "card": {
      "number": "4895370016313691"
    }
  }
}
```

Response 201 Example: Successful BIN Lookup Service with a Network Token

```
{
  "id": "6680880793396052804990",
  "submitTimeUtc": "2022-11-10T01:47:59Z",
  "status": "COMPLETED",
  "paymentAccountInformation": {
    "card": {
      "type": "001",
      "brandName": "CARD",
      "maxLength": "16",
      "credentialType": "TOKEN"
    },
    "features": {
      "accountFundingSource": "DEBIT",
      "cardPlatform": "CONSUMER",
      "cardProduct": "Relay Classic"
    }
  },
  "issuerInformation": {
    "name": "INTL HDQTRS-CENTER OWNED",
    "country": "US",
    "binLength": "6"
    "accountPrefix": "4111111"
  }
}
```

Request Example: BIN Lookup Service with a Six-Digit Payment Card Prefix

```
{
  "paymentInformation": {
    "card": {
      "number": "5033961"
    }
  }
}
```

Response 201 Example: Multiple Match BIN Lookup Service with a Six-Digit Payment Card Prefix

```
\\ This response occurs when multiple account ranges are found with the provided digits. If you receive this response, please provide extended BIN digits to narrow the result to a single range.
{
  "id": "6445408746306656603955",
  "submitTimeUtc": "2022-02-11T12:54:35Z",
  "status": "MULTIPLE"
}
```

Request Example: BIN Lookup Service with an Eight-Digit Payment Card Prefix

```
{
  "paymentInformation": {
    "card": {
      "number": "71111111"
    }
  }
}
```

Response 201 Example: BIN Lookup Service No Match

```
\\ This response occurs when a BIN record is not found with the provided digits.
{
  "id": "6445408746306656603955",
  "submitTimeUtc": "2022-02-11T12:54:35Z",
  "status": "NO MATCH"
}
```

Request Example: BIN Lookup Service with a `TMS` Customer ID Token

```
{
  "paymentInformation": {
    "customer": {
      "id": "D0ED44421CDA7A58E053AF598E0AD964"
    }
  }
}            
```

Request Example: BIN Lookup Service with a `TMS` Payment Instrument Token

```
{
  "paymentInformation": {
    "paymentInstrument": {
      "id": "D0ED44421CD97A58E053AF598E0AD964"
    }
  }
}            
```

Request Example: BIN Lookup Service with a `TMS` Instrument Identifier Token

```
{
  "paymentInformation": {
    "instrumentIdentifier": {
      "id": "801E10E1B4E2C86AE05341588E0A86EC"
    }
  }
}            
```

Request Example: BIN Lookup Service with a `TMS` jti Transient Token

```
{
  "tokenInformation": {
    "jti": "1C26VZRFEIQMOO5H0504KH47I0AM2IZFC43V5L541HBLN9COI3L75F3194E196A1"
  }
}            
```

Request Example: BIN Lookup Service with a `Flex API` JWT Transient Token

```
{
  "tokenInformation": {
    "transientTokenJwt": "eyJraWQ...xxxxx.yyyyy.zzzzz...xZqoGA"
  }
}            
```

Requesting the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-req-task}
===============================================================================================================

Send one of these payment credentials to the BIN Lookup Service to retrieve BIN information and fast funds eligibility.  
**Payment Card Numbers**

* Full payment card number  
  **Tokens**

* `TMS` customer ID token

* `TMS` payment instrument token

* `TMS` instrument identifier token

* `TMS` jti transient token

* `Flex API` JWT transient token  
  Follow these steps to request the BIN Lookup Service with Fast Funds:

1. Send the request to the BIN Lookup Service endpoint:

   #### ADDITIONAL INFORMATION

   `POST https://&lt;``url_prefix``&gt;/bin/v1/binlookup `

   #### ADDITIONAL INFORMATION

   Use one of these URL prefixes:

   * Test: `apitest.example.com`
   * Production: `api.example.com`
   * Production in India: `api.in.example.com`
2. Include one of the prerequisite fields in the request:

   * paymentInformation.card.number (Full payment card number is recommended.)
   * paymentInformation.customer.id
   * paymentInformation.instrumentIdentifier.id
   * paymentInformation.paymentInstrument.id
   * tokenInformation.jti
   * tokenInformation.transientTokenJwt
     {#bin-lookup-payouts-req-task_choices_az2_s4v_f5b}
3. Request the service. Set processingInformation.payoutOptions.payoutInquiry to true.

4. Include optional fields in the request as needed.

5. Check the response message to make sure that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [BIN Lookup Response Codes](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-reference-intro/bin-lookup-resp-codes.md ""). {#bin-lookup-payouts-req-task_response-rest}

Required Fields for the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-service-fields}
==============================================================================================================================

Include this fast funds eligibility field in the request for the BIN Lookup Service:

[processingInformation.payoutOptions.payoutInquiry](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payout-opts-payout-inqry.md "")
:
Set this field to `true` to get fast funds eligibility information in the response.
Include one of these payment credential fields in the request:

[paymentInformation.card.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:
Set this field to the full payment card number (recommended) or network token.

[paymentInformation.customer.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-id.md "")
:

[paymentInformation.instrumentIdentifier.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-instrument-identifier-id.md "")
:

[paymentInformation.paymentInstrument.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-instrument-id.md "")
:

[tokenInformation.jti](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-jti.md "")
:

[tokenInformation.transientTokenJwt](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

Optional Fields for the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-opt-fields}
==========================================================================================================================

These fields are optional for a BIN Lookup Service request with fast funds eligibility information:

[paymentAccountInformation.network.id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-network-id.md "")
:

[processingInformation.binSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-bin-source.md "")
:

[processingInformation.payoutOptions.acquirerBin](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payout-opts-acq-bin.md "")
:

[processingInformation.payoutOptions.networkID](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payout-opts-ntwrk-id.md "")
:

Testing the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-test-proc}
=============================================================================================================

`Payment Gateway` provides these test payment card numbers for requesting the BIN Lookup Service with fast funds eligibility in the test environment. Do not use real payment card numbers. Remove spaces when sending card numbers to `Payment Gateway`.

Test Payment Card Numbers for the BIN Lookup Service with Fast Funds {#bin-lookup-payouts-test}
===============================================================================================

Use these payment card numbers to test the BIN Lookup Service with fast funds at the test endpoint:
`https://apitest.example.com``/bin/v1/binlookup`

| Card Number            | Card Type  | Card Platform and/or Product | Issuer Country | Account Funding Source |
|:-----------------------|:-----------|:-----------------------------|:---------------|:-----------------------|
| 4761 0800 0000 0003    | Relay       | Consumer                     | AE             | Debit                  |
| 4515 8600 0004 1118    | Relay       | Consumer                     | US             | Debit                  |
| 4515 2200 0008 1111    | Relay       | Business                     | AL             | Debit                  |
| 4473 3000 0051 1117    | Relay       | Business                     | AM             | Debit                  |
| 4846 7000 0973 1113    | Relay       | Business                     | AO             | Debit                  |
| 5033 9619 8910 0006    | Mastercard | Consumer                     | US             | Debit                  |
| 5033 9619 8910 0014    | Mastercard | Consumer                     | US             | Debit                  |
| 5033 9619 8910 0022    | Mastercard | Consumer                     | US             | Debit                  |
| 5033 9619 8910 0030    | Mastercard | Consumer                     | US             | Debit                  |
| 5033 9619 8910 0048    | Mastercard | Consumer                     | US             | Debit                  |
| 5868 2416 0825 5330 00 | Mastercard | Commercial                   | US             | Debit                  |
[Test Payment Card Numbers and Card Information]

Examples: Requests to the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-card-example}
==============================================================================================================================

These examples show various BIN Lookup Service requests with fast funds eligibility options enabled and successful responses. Request Example: BIN Lookup Service with a Payment Card and Fast Funds Eligibility

```
{
    "paymentInformation": {
        "card": {
            "number": "4761080000000003"
        }
    },
    "processingInformation": {
        "payoutOptions": {
            "payoutInquiry": true
        }
    }
}        
```

Response 201 Example: Successful BIN Lookup Service with Fast Funds Eligibility

```
 {
    "id": "6590834057836283403955",
    "submitTimeUtc": "2022-07-29T08:30:05Z",
    "status": "COMPLETED",
    "paymentAccountInformation": {
        "card": {
            "type": "001",
            "brandName": "CARD",
            "maxLength": "16",
            "currency": "AED",
            "credentialType": "PAN"
        },
        "features": {
            "accountFundingSource": "DEBIT",
            "cardPlatform": "CONSUMER",
            "comboCard": "0"
        }
    },
    "issuerInformation": {
        "name": "INTL HDQTRS-CENTER OWNED",
        "country": "AE"
        "accountPrefix": "4111111"
    },
    "payoutInformation": {
        "pushFunds": {
            "moneyTransferFastFundsCrossBorder": "Y",
            "moneyTransferFastFundsDomestic": "Y",
            "moneyTransferCrossBorder": "Y",
            "moneyTransferDomestic": "Y",
            "nonMoneyTransferFastFundsCrossBorder": "Y",
            "nonMoneyTransferFastFundsDomestic": "Y",
            "nonMoneyTransferCrossBorder": "Y",
            "nonMoneyTransferDomestic": "Y",
            "onlineGamblingFastFundsCrossBorder": "Y",
            "onlineGamblingFastFundsDomestic": "Y",
            "onlineGamblingCrossBorder": "Y",
            "onlineGamblingDomestic": "Y"
        }
    }
}         
```

Response 201 Example: BIN Lookup Service with Fast Funds Eligibility (Brazil)

```
{
    "id": "6590834057836283403955",
    "submitTimeUtc": "2022-05-19T03:21:03Z",
    "status": "COMPLETED",
    "paymentAccountInformation": {
        "card": {
            "type": "001",
            "brandName": "CARD",
            "maxLength": "16",
            "currency": "USD"
        },
        "features": {
            "accountFundingSource": "PREPAID",
            "cardPlatform": "CONSUMER",
            "cardProduct": "Relay Electron",
            "comboCard": "0"
        }
    },
    "issuerInformation": {
        "name": "BANCO DO BRASIL S.A.",
        "country": "BR",
        "phoneNumber": "5555555555",
        "binLength": "6"
        "accountPrefix": "4111111"
    },
    "payoutInformation": {
        "pushFunds": {
            "moneyTransferFastFundsCrossBorder": "N",
            "moneyTransferFastFundsDomestic": "N",
            "moneyTransferCrossBorder": "Y",
            "moneyTransferDomestic": "Y",
            "nonMoneyTransferFastFundsCrossBorder": "N",
            "nonMoneyTransferFastFundsDomestic": "N",
            "nonMoneyTransferCrossBorder": "Y",
            "nonMoneyTransferDomestic": "Y",
            "onlineGamblingFastFundsCrossBorder": "N",
            "onlineGamblingFastFundsDomestic": "N",
            "onlineGamblingCrossBorder": "Y",
            "onlineGamblingDomestic": "Y"
        }
    }
}
```

Reference Information {#bin-lookup-reference-intro}
===================================================

This section contains reference information that is useful when you work with the BIN Lookup Service.

BIN Lookup Service Response Codes {#bin-lookup-resp-codes}
==========================================================

The BIN Lookup Service returns these codes.

| Code | Description                                |                  Action to Take                   |
|:-----|:-------------------------------------------|---------------------------------------------------|
| 201  | Successful response.                       | No further action required.                       |
| 400  | Invalid request.                           | Verify the request and retry.                     |
| 502  | Unexpected system error or system timeout. | Verify the request and retry.                     |
| 201  | Multiple records.                          | Retry with full PAN, TMS token, or network token. |
| 201  | No match.                                  | No further action required.                       |
[Response Codes]

Response Fields for the BIN Lookup Service Using the REST API {#bin-lookup-resp-fields}
=======================================================================================

A response for the BIN Lookup Service can include these response fields:

[id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "")
:

[issuerInformation.accountPrefix](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-acct-prefix.md "")
:

[issuerInformation.binLength](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-bin-length.md "")
:

[issuerInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-country.md "")
:

[issuerInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-name.md "")
:

[issuerInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-phone-number.md "")
:

[paymentAccountInformation.card.brandName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brand-name.md "")
:

[paymentAccountInformation.card.brands.brandName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brands-brand-name.md "")
:

[paymentAccountInformation.card.brands.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brands-type.md "")
:

[paymentAccountInformation.card.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-currency.md "")
:

[paymentAccountInformation.card.maxLength](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-max-length.md "")
:

[paymentAccountInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-type.md "")
:

[paymentAccountInformation.features.acceptanceLevel](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-accept-level.md "")
:

[paymentAccountInformation.features.accountFundingSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-acct-fund-src-a.md "")
:

[paymentAccountInformation.features.accountFundingSourceSubType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-acct-fund-src-sub-type.md "")
:

[paymentAccountInformation.features.cardPlatform](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-card-platform.md "")
:

[paymentAccountInformation.features.cardProduct](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-card-product.md "")
:

[paymentAccountInformation.features.comboCard](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-combo-card.md "")
:

[paymentAccountInformation.features.corporatePurchase](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-corp-purchase.md "")
:

[paymentAccountInformation.features.healthCard](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-health-card.md "")
:

[paymentAccountInformation.features.messageType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-message-type.md "")
:

[status](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/status-a.md "")
:

[submitTimeUtc](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/submit-time-utc.md "")
:

Response Fields for the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-resp-fields}
===========================================================================================================================

A response for the BIN Lookup Service with fast funds eligibility information can include these response fields:

[id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "")
:

[issuerInformation.accountPrefix](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-acct-prefix.md "")
:

[issuerInformation.binLength](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-bin-length.md "")
:

[issuerInformation.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-country.md "")
:

[issuerInformation.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-name.md "")
:

[issuerInformation.phoneNumber](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/issuer-info-aa/issuer-info-phone-number.md "")
:

[paymentAccountInformation.card.brandName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brand-name.md "")
:

[paymentAccountInformation.card.brands.brandName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brands-brand-name.md "")
:

[paymentAccountInformation.card.brands.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-brands-type.md "")
:

[paymentAccountInformation.card.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-currency.md "")
:

[paymentAccountInformation.card.maxLength](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-max-length.md "")
:

[paymentAccountInformation.card.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-card-type.md "")
:

[paymentAccountInformation.features.acceptanceLevel](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-accept-level.md "")
:

[paymentAccountInformation.features.accountFundingSource](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-acct-fund-src-a.md "")
:

[paymentAccountInformation.features.accountFundingSourceSubType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-acct-fund-src-sub-type.md "")
:

[paymentAccountInformation.features.cardPlatform](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-card-platform.md "")
:

[paymentAccountInformation.features.cardProduct](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-card-product.md "")
:

[paymentAccountInformation.features.comboCard](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-combo-card.md "")
:

[paymentAccountInformation.features.messageType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-account-info-aa/payment-account-info-feat-message-type.md "")
:

[payoutInformation.geoRestrictionIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-geo-restrict-indicator.md "")
:

[payoutInformation.pullFunds.crossBorderParticipant](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-pull-funds-cross-border-part.md "")
:

[payoutInformation.pullFunds.domesticParticipant](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-pull-funds-domestic-part.md "")
:

[payoutInformation.pushFunds.crossBorderParticipant](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-cross-border-part.md "")
:

[payoutInformation.pushFunds.domesticParticipant](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-domestic-part.md "")
:

[payoutInformation.pushFunds.moneyTransferCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-mny-trnsfer-crss-brdr.md "")
:

[payoutInformation.pushFunds.moneyTransferDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-mny-trnsfr-dmstc.md "")
:

[payoutInformation.pushFunds.moneyTransferFastFundsCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-mny-trnsfr-fst-fnds-crss-br.md "")
:

[payoutInformation.pushFunds.moneyTransferFastFundsDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-mny-trnsfr-fst-fnds-dmstc.md "")
:

[payoutInformation.pushFunds.nonMoneyTransferCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-non-mny-trnsfr-crss-brdr.md "")
:

[payoutInformation.pushFunds.nonMoneyTransferDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-non-mny-trnsfr-dmstc.md "")
:

[payoutInformation.pushFunds.nonMoneyTransferFastFundsCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-non-mny-trnsfr-fst-fnds-crs.md "")
:

[payoutInformation.pushFunds.nonMoneyTransferFastFundsDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-non-mny-trnsfr-fst-fnds-dms.md "")
:

[payoutInformation.pushFunds.onlineGamblingCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-online-gamb-crss-brdr.md "")
:

[payoutInformation.pushFunds.onlineGamblingDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-online-gamb-dmstc.md "")
:

[payoutInformation.pushFunds.onlineGamblingFastFundsCrossBorder](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-online-gamb-fst-fnds-crss-b.md "")
:

[payoutInformation.pushFunds.onlineGamblingFastFundsDomestic](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payout-info-aa/payout-info-push-funds-online-gamb-fst-fnds-dmstc.md "")
:

[status](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/status-a.md "")
:

[submitTimeUtc](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/submit-time-utc.md "")
:
