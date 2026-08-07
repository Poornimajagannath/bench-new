Google Pay Developer Guide {#googpay-about-guide}
=================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
--------------------

This document is written for merchants who want to enable customers to use Google Pay to pay for in-app purchases. This document provides an overview of integrating the Google API and describes how to request the `Cybersource` API to process an authorization.  
This document describes the Google Pay service and the `Cybersource` API. You must request the Google API to receive the customer's encrypted payment data before requesting the `Cybersource` API to process the transaction.

Conventions
-----------

The following special statements are used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
---------------------

For further technical documentation, visit the `Cybersource` Technical Documentation Portal:  
[https://docs.cybersource.com/en/index.html](https://docs.cybersource.com/en/index.md "")

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#googpay-doc-revisions}
==========================================================

25.04.01
--------

:
This revision contains only editorial changes and no technical updates.

24.09.01
--------

This revision contains only editorial changes and no technical updates.

24.06.01
--------

Corrected URL to setting up Sandbox Account.

24.02.01
--------

Fixed typo in Javascript sample. See [Formatting Payment Blobs](/docs/cybs/en-us/google-pay/developer/ctv/rest/googlepay/googpay-pay-data-intro/googpay-pay-data-formatting-blobs.md "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.

Introduction {#googpay-intro}
=============================

You can use the `Cybersource` platform to process and manage Google Pay transactions.

Google Pay Overview
-------------------

Google Pay is a simple, secure in-app mobile and Web payment solution. You can choose `Cybersource` to process Google Pay transactions through all e-commerce channels.  
You can simplify your payment processing by allowing `Cybersource` to decrypt the payment data for you during processing.  
This method integrates simply and enables you to process transactions without seeing the payment network token and transaction data.

1. Using the Google API, request the customer's encrypted payment data.
2. Using the `Cybersource` API, construct and submit the authorization request, and include the encrypted payment data from the Google Pay callback.
3. `Cybersource` decrypts the encrypted payment data to create the payment network token and processes the authorization request.

Payment Network Tokens {#googpay-pmnt-network-tokens}
=====================================================

Authorizations with payment network tokens enable you to securely request a payment transaction with a payment network token instead of a customer's primary account number (PAN).  
The payment network token is included in the customer's encrypted payment data, which is returned by the payment processor.

Prerequisite Requirements {#googpay-requirements}
=================================================

Before using Google Pay, you must have:

* A `Cybersource` merchant evaluation account.
  * To register, go to: [https://developer.cybersource.com/hello-world/sandbox.html](https://developer.cybersource.com/hello-world/sandbox.md "")
* A [merchant evaluation account](https://ebc2.cybersource.com/ebc2/registration/external "") with a supported processor. See [Supported Processors](/docs/cybs/en-us/google-pay/developer/ctv/rest/googlepay/googpay-intro/googpay-processors.md "").
* The `Cybersource` `REST API` Client installed on your system.
* A Google developer account.
* Google Pay APIs embedded into your application or website. For details about integrating Google Pay, see the [Google Pay API](https://developers.google.com/pay/api "") documentation.

Supported Processors {#googpay-processors}
==========================================

|                                                                                                                                                                                                                                                                                        Processor                                                                                                                                                                                                                                                                                         |                        Card Types                        |                     Optional Features                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| `Platform Connect` Supported acquirers: * Advanced Bank of Asia Cambodia (ABA Bank) on Platform Connect * BAC Credomatic Cost Rica and BAC Credomatic Panama on Platform Connect * BAC Credomatic Guatemala on Platform Connect * BAC Credomatic Honduras on Platform Connect * BAC Credomatic Nicaragua on Platform Connect * BAC Credomatic El Salvador on Platform Connect * BC Card Co., Ltd on Platform Connect * Commercial Bank of Qatar on Platform Connect * Maybank on Platform Connect {#googpay-processors_ul_p5b_fgm_zwb} | * Mastercard * Relay {#googpay-processors_ul_jh1_dwq_l4b} | * Recurring Payments {#googpay-processors_ul_qh1_dwq_l4b} |

How Google Pay Works {#googpay-how-it-works}
============================================

The following figure describes the Google Pay workflow:  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/googlepay/images/trans_flow.png/jcr:content/renditions/original)

1. The customer chooses the Google Pay button. Using the Google API, your system initiates the Google Pay request identifying `Cybersource` as your payment gateway, passing your `Cybersource` merchant ID as the gateway merchant ID.
2. The customer confirms the payment. The Google API contacts Google Pay services to retrieve the consumer's payment parameters.
3. If the customer's selected payment credentials are tokenized, or you are tokenizing new payment credentials, the Google Pay service contacts the appropriate payment network to retrieve the appropriate cryptogram.
4. The payment network returns the appropriate token and cryptogram to the Google Pay service.
5. Google creates encrypted payment data using the gateway-specific key that is supplied in the Wallet request and includes it in the Google API response.
6. The Google Pay callback returns the encrypted payment data.
7. Your system prepares the Google Pay response information for submission to the `Cybersource` service.
8. 1. `Cybersource` sends the authorization request to the acquirer.
   2. The acquirer processes the request from `Cybersource` and creates the payment network authorization request.
   3. The payment network processes the request from the acquirer and creates the issuer authorization request.
   4. The issuer processes the request from the payment network. The issuer looks up the payment information and returns an approved or declined authorization message to the payment network.
   5. The payment network returns the authorization response to the acquirer.
   6. The acquirer returns the authorization response to `Cybersource`.
9. `Cybersource` returns the authorization response to your system.
10. Your system returns the authorization response to the payment application.
11. The payment application displays the confirmation or decline message to the customer.
    1. The acquirer submits the settlement request to the issuer for funds.
12. The issuer supplies the funds to the acquirer for the authorized transactions.

Additional Services {#googpay-avail-svcs}
=========================================

These additional services can be used with Google Pay.

Follow-on Services
------------------

After the authorization is requested, you can request follow-on services to complete the transaction. For more information on these services, see [Follow-on Services](/docs/cybs/en-us/google-pay/developer/ctv/rest/googlepay/googpay-follow-on-intro.md "").

Authorized Reversal
:
An authorized reversal is a follow-on service that uses the request ID returned from the previous authorization. An authorization reversal releases the hold that the authorization placed on the customer's credit card funds. Use this service to reverse an unnecessary or undesired authorization.

Capture
:
A capture is a follow-on service that uses the request ID returned from the previous authorization. The request ID links the capture to the authorization. This service transfers funds from the customer's account to your bank and usually takes two to four days to complete.

Sale
:
A sale is a bundled authorization and capture. Request the authorization and capture services at the same time. `Cybersource` processes the capture immediately.

Follow-on Transactions {#id_ltm_ltt_gyb}
----------------------------------------

After the payment transaction is complete, additional follow-on transactions can be made as Merchant-Initiated Transactions (MITs).  
For more information on how to process MITs, see [Merchant-Initiated Transactions](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/credentials/credentials-mit-intro.md "").  
MITs include:

* Delayed Authorizations
* Incremental Transactions
* Installment Payments
* No-Show Transactions
* Reauthorizations
* Recurring Transactions
* Resubmissions
* Unscheduled Transactions
  {#id_ltm_ltt_gyb_d12e28}

Formatting Encrypted Payment Data {#googpay-pay-data-intro}
===========================================================

This section shows you how to format encrypted payment data using these procedures:

* [Configuring Google Pay](/docs/cybs/en-us/google-pay/developer/ctv/rest/googlepay/googpay-pay-data-intro/googpay-pay-data-config.md "")
* [Formatting Payment Blobs](/docs/cybs/en-us/google-pay/developer/ctv/rest/googlepay/googpay-pay-data-intro/googpay-pay-data-formatting-blobs.md "")
  {#googpay-pay-data-intro_ul_kkj_ckx_1xb}

Configuring Google Pay {#googpay-pay-data-config}
=================================================

You must provide your `Cybersource` merchant ID to Google in order to ensure proper encryption of the Google Pay payload and authenticity of the request.  
For a Google Pay tutorial, see [Google Pay for Payments](https://developers.google.com/pay/api "").  
Set the gateway and gateway merchant ID to the appropriate indicators. The following code examples show how to configure the PaymentMethodTokenizationParameters object using `Cybersource` as the gateway.  
Example: Java Code

```keyword
.setPaymentMethodTokenizationType(WalletConstants.PAYMENT_METHOD_TOKENIZATION_TYPE_PAYMENT_GATEWAY)
     .addParameter("gateway", "")
     .addParameter("gatewayMerchantId", "[yourCybersourceMID]")
```

Example: JavaScript Code

```keyword
tokenizationType: 'PAYMENT_GATEWAY',
     parameters: {
     gateway: 'cybersource',
          gatewayMerchantId: '[yourCybersourceMID]'
```

Formatting Payment Blobs {#googpay-pay-data-formatting-blobs}
=============================================================

> IMPORTANT
> This section is only applicable if you are using the ` Cybersource ` decryption method.  
> To prepare the Google Pay payload for submission to `Cybersource`, you must extract the token data element from the Google Pay payload and encode the token data element using Base64.  
> These samples can be used to Base64-encode payment responses:  
> JavaScript

```
let token = paymentData.paymentMethodData.tokenizationData.token;
console.log(token);
var enc=window.btoa(token);
```

Android with Java  
This sample uses the Android Studio Base64 utility.

```
public static &lt;outputString&gt; encodeToString (byte[] &lt;inputToken&gt;, int DEFAULT)
```

Apple iPhone with Swift 3  
This sample requires the Foundation utility.

```
extension String {
     func base64Encoded() -&gt; &lt;outputString&gt;
          if let data = self.dat(using:.utf8) {
               return data.base64EncodedString()
          }
          return nil
}
```

Examples of Google Pay Responses {#googpay-pay-data-config-ex-b64-response}
===========================================================================

Decrypted Google Pay Response

```
{"signature":"MEUCIQDhTxhHqwY8pXB9hpYxaSK5jFgsqpG2E1rX77QXssK8tAIgUBvYYAI/
bnBS8T/Tfxnm2AF981Mv5y0pHyGexM5dMJk\u003d","protocolVersion":"ECv1","
signedMessage":"{\"encryptedMessage\":\"
odyUGGA7B+blletYcJbS43AQUFQJpWEFCN4UuUExQ5LX0\/
XcLwKElXcB95nMnmPO9lM2KGp13FYsL768ccCzAjBGLYF+
fugcJTcvkrUhcNSyXr7hwf12BEsrweqJM6I7Vs5lfrPAukRJeLDQG4FxmTLW49QyP8vIZC+
tz2c+Z3zozzI5oB9jE8fA2dolFa13Cu6gXqdKH\/
IHRh7UniLUuTy+0G5FQV2pwST2uBSNNkZhb8WYJDHbxBjz0UebVP+
ObmT5cc8AKU5dgHRdfr4GKpEZ4EBzB90 BPxLqYHpopriJ6lbFgFVsQQ6\/
8HBqQ7ImIMH5y7G8p8qAFkWnB78ZcL0Fh5BjXojkxGoFp2gjAsrhhttHAFbe3WQBuPkwJu09\/
6\/MyJpCSrpMHFouF\/dj0SYjQ+xI097lCHZec7jQrAhISLWZ9DZkuMvGKPWpu0CKn2XqTXQ=\
",\"ephemeralPublicKey\":\
"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEnn4yjy0N6xlXO8\/8j7\/
4jvmLJCYAqgXLwP1FhjuTgIM9oCtPijZfI9so2QEOs2ZnVp3D0dl3JYIDVe+396KkAQ==\
",\"tag\":\"DRp cc+YQ33RNgsTcxztnJbMJnirbU5DW3dStjfhFiwc=\"}"}
```

Base64-Encoded Google Pay Response

```
eyJzaWduYXR1cmUiOiJNRVVDSVFEaFR4aEhxd1k4cFhCOWhwWXhhU0s1akZnc3FwRzJ
FMXJYNzdRWHNzSzh0QUlnVUJ2WVlBSS9ibkJTOFQvVGZ4bm0yQUY5ODFNdjV5MHBIeU
dleE01ZE1Ka1x1MDAzZCIsInByb3RvY29sVmVyc2lvbiI6IkVDdjEiLCJzaWduZWRNZ
XNzYWdlIjoie1wiZW5jcnlwdGVkTWVzc2FnZVwiOlwib2R5VUdHQTdCK2JsbGV0WWNK
YlM0M0FRVUZRSnBXRUZDTjRVdVVFeFE1TFgwXC9YY0x3S0VsWGNCOTVuTW5tUE85bE0
yS0dwMTNGWXNMNzY4Y2NDekFqQkdMWUYrZnVnY0pUY3ZrclVoY05TeVhyN2h3ZjEyQk
VzcndlcUpNNkk3VnM1bGZyUEF1a1JKZUxEUUc0RnhtVExXNDlReVA4dklaQyt0ejJjK
1ozem96ekk1b0I5akU4ZkEyZG9sRmExM0N1NmdYcWRLSFwvSUhSaDdVbmlMVXVUeSsw
RzVGUVYycHdTVDJ1QlNOTmtaaGI4V1lKREhieEJqejBVZWJWUCtPYm1UNWNjOEFLVTV
kZ0hSZGZyNEdLcEVaNEVCekI5MEJQeExxWUhwb3ByaUo2bGJGZ0ZWc1FRNlwvOEhCcV
E3SW1JTUg1eTdHOHA4cUFGa1duQjc4WmNMMEZoNUJqWG9qa3hHb0ZwMmdqQXNyaGh0d
EhBRmJlM1dRQnVQa3dKdTA5XC82XC9NeUpwQ1NycE1IRm91RlwvZGowU1lqUSt4STA5
N2xDSFplYzdqUXJBaElTTFdaOURaa3VNdkdLUFdwdTBDS24yWHFUWFE9XCIsXCJlcGh
lbWVyYWxQdWJsaWNLZXlcIjpcIk1Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMERBUW
NEUWdBRW5uNHlqeTBONnhsWE84XC84ajdcLzRqdm1MSkNZQXFnWEx3UDFGaGp1VGdJT
TlvQ3RQaWpaZkk5c28yUUVPczJablZwM0QwZGwzSllJRFZlKzM5NktrQVE9PVwiLFwi
dGFnXCI6XCJEUnBjYytZUTMzUk5nc1RjeHp0bkpiTUpuaXJiVTVEVzNkU3RqZmhGaXd
jPVwifSJ9
```

Google Pay Authorizations {#googpay-pay-auth-intro}
===================================================

This section shows you how to make a successful authorization request.  
After you send the request, check the response messages to make sure that the request was successful. A 200-level HTTP response code indicates success.  
For information about response codes, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md ""). .

Follow-on Transactions
----------------------

After the initial transaction is complete, additional follow-on transactions can be made as Merchant-Initiated Transactions (MITs).  
For more information on how to process MITs, see [Merchant-Initiated Transactions](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/credentials/credentials-mit-intro.md "").

Endpoint {#googpay-pay-auth-intro_d9e16}
----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#googpay-pay-auth-intro_d9e25}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#googpay-pay-auth-intro_d9e35}

Required Fields for a Google Pay Authorization {#googpay-pay-auth-req-fields}
=============================================================================

Include these required fields to request a successful authorization.

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.totalAmount
:

orderInformation.billTo.address1
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.country
:

orderInformation.billTo.email
:

orderInformation.billTo.firstName
:

orderInformation.billTo.lastName
:

orderInformation.billTo.locality
:

orderInformation.billTo.postalCode
:

paymentInformation.fluidData.value
:
Set to the string value generated from the full wallet response.

processingInformation.paymentSolution
:
Set to `012`.
{#googpay-pay-auth-req-fields_dl_ujf_qjh_1xb}

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")

REST Example: Google Pay Authorization {#googpay-pay-auth-ex-rest}
==================================================================

Request

```keyword
{
  "processingInformation": {
    "paymentSolution": "012"
  },
  "paymentInformation": {
    "fluidData": {
      "value": "ABCDEFabcdefABCDEFabcdef0987654321234567"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "123 Happy Street",
      "locality": "Ann Arbor",
      "administrativeArea": "MI",
      "postalCode": "48104-2201",
      "country": "US",
      "email": "test@cybs.com"
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
      "href": "/pts/v2/payments/6805343125426255503955/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6805343125426255503955"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6805343125426255503955/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "6805343125426255503955",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "102.21",
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
      "code": "X",
      "codeRaw": "I1"
    }
  },
  "reconciliationId": "65301815QFTXZAN6",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-04-03T15:05:12Z"
}
```

Follow-on Services {#googpay-follow-on-intro}
=============================================

This section provides information about and procedures for requesting these follow-on services:

* **Authorization Reversal:** A follow-on service that uses the request ID returned from the previous authorization. An authorization reversal releases the hold that the authorization placed on the customer's credit card funds. Use this service to reverse an unnecessary or undesired authorization.
* **Capture:** A follow-on service that uses the request ID returned from the previous authorization. The request ID links the capture to the authorization. This service transfers funds from the customer's account to your bank and usually takes two to four days to complete.
* **Sale:** A sale is a bundled authorization and capture. Request the authorization and capture services at the same time. `Cybersource` processes the capture immediately.
  {#googpay-follow-on-intro_ul_c4k_fqn_hsb}

Authorization Reversal {#payments-processing-basic-auth-reversal-intro}
=======================================================================

This section provides the information about how to process an authorization reversal.  
Reversing an authorization releases the hold on the customer's payment card funds that the issuing bank placed when processing the authorization.  
For a debit card or prepaid card in which only a partial amount was approved, the amount of the reversal must be the amount that was authorized, not the amount that was requested.

Supported Card Types
--------------------

All supported card types can process reversals.

Endpoint {#payments-processing-basic-auth-reversal-intro_d7e85}
---------------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#payments-processing-basic-auth-reversal-intro_d7e94}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`{#payments-processing-basic-auth-reversal-intro_d7e107}  
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

Captures {#payments-processing-basic-capture-intro}
===================================================

This section provides the information you need in order to capture an authorized transaction.

Supported Card Types
--------------------

All supported card types can process captures. .

Endpoint {#payments-processing-basic-capture-intro_d7e127}
----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#payments-processing-basic-capture-intro_d7e136}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#payments-processing-basic-capture-intro_d7e149}  
The *{id}* is the transaction ID returned in the authorization response.

Required Fields for Capturing an Authorization {#payments-processing-basic-capture-required-fields}
===================================================================================================

Use these required fields for capturing an authorization.

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

Sales {#payments-processing-basic-sale-intro}
=============================================

This section provides the information you need in order to process a sale transaction.  
A sale combines an authorization and a capture into a single transaction.

Supported Card Types
--------------------

All supported card types can process sales. .

Endpoint {#payments-processing-basic-sale-intro_d7e240}
-------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#payments-processing-basic-sale-intro_d7e248}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#payments-processing-basic-sale-intro_d7e258}

Required Fields for Processing a Sale {#payments-processing-basic-sale-reqfields}
=================================================================================

Use these required fields for processing a sale.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.

Related Information {#payments-processing-basic-sale-reqfields_section_sjf_tbv_sxb}
-----------------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#payments-processing-basic-sale-reqfields_ul_x5z_1bv_sxb}

REST Example: Processing a Sale {#payments-processing-basic-sale-ex-rest}
=========================================================================

Request

```keyword
{
  "processingInformation": {
    "capture": true
  },
  "orderInformation" : {
    "billTo" : {
    "country" : "US",
    "lastName" : "VDP",
    "address1" : "201 S. Division St.",
    "postalCode" : "48104-2201",
    "locality" : "Ann Arbor",
    "administrativeArea" : "MI",
    "firstName" : "RTS",
    "email" : "test@cybs.com"
  },
    "amountDetails" : {
      "totalAmount" : "100.00",
      "currency" : "usd"
     }
   },
  "paymentInformation" : {
    "card" : {
      "expirationYear" : "2031",
      "number" : "4111111111111111",
      "expirationMonth" : "12",
      "type" : "001
    }
  }
}
```

Response to a Successful Request  
Most processors do not return all of the fields that are shown in this example.

```
{
  "_links" : {
    "void" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6485004068966546103093/voids"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6485004068966546103093"
    }
  },
  "clientReferenceInformation" : {
    "code" : "RTS-Auth"
  },
  "id" : "6485004068966546103093",
  "orderInformation" : {
    "amountDetails" : {
      "totalAmount" : "100.00",
      "authorizedAmount" : "100.00",
      "currency" : "usd"
    }
  },
  "paymentAccountInformation" : {
    "card" : {
      "type" : "001"
    }
  },
  "paymentInformation" : {
    "tokenizedCard" : {
      "type" : "001"
    },
    "card" : {
      "type" : "001"
    }
  },
  "processorInformation" : {
    "systemTraceAuditNumber" : "841109",
    "approvalCode" : "831000",
    "merchantAdvice" : {
      "code" : "01",
      "codeRaw" : "M001"
    },
    "responseDetails" : "ABC",
    "networkTransactionId" : "016153570198200",
    "retrievalReferenceNumber" : "208720841109",
    "consumerAuthenticationResponse" : {
      "code" : "2",
      "codeRaw" : "2"
    },
    "transactionId" : "016153570198200",
    "responseCode" : "00",
    "avs" : {
      "code" : "Y",
      "codeRaw" : "Y"
    }
  },
  "reconciliationId" : "6485004068966546103093",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2022-03-28T20:46:47Z"
}
```

Follow-on Transactions {#googpay-follow-on-trans}
=================================================

After the payment transaction is complete, additional follow-on transactions can be made as Merchant-Initiated Transactions (MITs).  
For more information on how to process MITs, see [Merchant-Initiated Transactions](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/credentials/credentials-mit-intro.md "").  
MITs include:

* Delayed Authorizations
* Incremental Transactions
* Installment Payments
* No-Show Transactions
* Reauthorizations
* Recurring Transactions
* Resubmissions
* Unscheduled Transactions
  {#googpay-follow-on-trans_ul_akj_3tt_zxb}

