---
title: Pre-Authorization
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_pre_auth_intro
lineage_origin: generated_from_endpoint_fact
---

# Pre-Authorization

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pre-auth-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pre-auth-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |
| orderInformation.billTo.address1 |  | yes |  |
| orderInformation.billTo.administrativeArea |  | yes |  |
| orderInformation.billTo.country |  | yes |  |
| orderInformation.billTo.email |  | yes |  |
| orderInformation.billTo.firstName |  | yes |  |
| orderInformation.billTo.lastName |  | yes |  |
| orderInformation.billTo.locality |  | yes |  |
| orderInformation.billTo.postalCode |  | yes |  |
| paymentInformation.card.expirationMonth |  | yes |  |
| paymentInformation.card.expirationYear |  | yes |  |
| paymentInformation.card.number |  | yes |  |
| processingInformation.authorizationOptions.authIndicator |  | yes | Set the value to `0`. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| merchantInformation.transactionLocalDateTime |  | yes | Required in Argentina when the time zone is not included in your account. Otherwise, this field is optional. |
| paymentInformation.card.sourceAccountType |  | yes | Required for combo card transactions. |
| paymentInformation.card.sourceAccountTypeDetails |  | yes | Required for combo card line-of-credit and prepaid-card transactions. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| paymentInformation.card.cardType |  | yes | Required for Meeza transactions. Set the value to `067`. |
| merchantInformation.merchantDescriptor.country |  | yes | Required for Meeza transactions. Set the value to `EG`. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| processingInformation.authorizationOptions.transactionMode |  | yes | Required only for merchants in Saudi Arabia. |
| paymentInformation.card.hashedNumber |  | yes | Required only for merchants in Taiwan. |

## Example request

```json
{
  "clientReferenceInformation" : {
    "code" : "Pre-Auth"
  },
  "orderInformation" : {
    "billTo" : {
      "country" : "US",
      "lastName" : "Doe",
      "address1" : "201 S. Division St.",
      "postalCode" : "48104-2201",
      "locality" : "Ann Arbor",
      "administrativeArea" : "MI",
      "firstName" : "Joan",
      "phoneNumber" : "999999999",
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
      "number" : "CARD_NUMBER",
      "securityCode" : "123",
      "expirationMonth" : "12",
      "type" : "001"
    }
  },
"processingInformation": {
    "authorizationOptions": {
      "authIndicator": "0"
    }
  }
}
```

## Example response

```json
{
  "_links" : {
    "authReversal" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/7709386742016723603091/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/7709386742016723603091"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/7709386742016723603091/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "Pre-Auth"
  },
  "id" : "7709386742016723603091",
  "orderInformation" : {
    "amountDetails" : {
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
  "pointOfSaleInformation" : {
    "terminalId" : "04980992"
  },
  "processorInformation" : {
    "paymentAccountReferenceNumber" : "V0010013018036776997406844475",
    "merchantNumber" : "6817027800",
    "approvalCode" : "100",
    "cardVerification" : {
      "resultCodeRaw" : "3",
      "resultCode" : "2"
    },
    "merchantAdvice" : {
      "code" : "00",
      "codeRaw" : "0"
    },
    "networkTransactionId" : "123456789012345",
    "transactionId" : "123456789012345",
    "responseCode" : "0",
    "avs" : {
      "code" : "U",
      "codeRaw" : "00"
    }
  },
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2026-02-12T23:24:34Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:2dae1f4d`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
