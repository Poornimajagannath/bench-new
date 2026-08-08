---
title: Authorize a Bonus Payment with Japanese Payment Options
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_jpo_auth_bonus
lineage_origin: generated_from_endpoint_fact
---

# Authorize a Bonus Payment with Japanese Payment Options

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-jpo-auth-bonus](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-jpo-auth-bonus)  

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
| paymentInformation.card.type |  | yes |  |
| processingInformation.japanPaymentOptions.businessName |  | yes | Business name in kanji characters. |
| processingInformation.japanPaymentOptions.businessNameAlphaNumeric |  | yes |  |
| processingInformation.japanPaymentOptions.businessNameKatakana |  | yes |  |
| processingInformation.japanPaymentOptions.paymentMethod |  | yes | Set this field to `21`, `22`, `23`, or `24`. |
| processingInformation.japanPaymentOptions.terminalId |  | yes | Required for card-present transactions. Unique Japan Credit Card Association (JCCA) terminal identifier that is provided by `Cybersource`. |

## Example request

```json
{
    "orderInformation": {
        "billTo": {
            "country": "US",
            "lastName": "Kim",
            "address1": "201 S. Division St.",
            "postalCode": "48104-2201",
            "locality": "Ann Arbor",
            "administrativeArea": "MI",
            "firstName": "Kyong-Jin",
            "email": "test@cybs.com"
        },
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "jpy"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "CARD_NUMBER",
            "expirationMonth": "12",
            "type": "001"
        }
    },
    "processingInformation": {
        "japanPaymentOptions": {
            "businessName": "我社",
            "businessNameAlphaNumeric": "OurStore",
            "businessNameKatakana": "わが社の場合",
            "paymentMethod": "21"
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
      "href" : "/pts/v2/payments/6843556498736135003059/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6843556498736135003059"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6843556498736135003059/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "RTS-Auth"
  },
  "id" : "6843556498736135003059",
  "orderInformation" : {
    "invoiceDetails" : {
      "salesSlipNumber" : "56307"
    },
    "amountDetails" : {
      "authorizedAmount" : "100",
      "currency" : "jpy"
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
    "salesSlipNumber" : "56307",
    "approvalCode" : "123456",
    "cardVerification" : {
      "resultCode" : "3"
    },
    "responseCategoryCode" : "000",
    "forwardedAcquirerCode" : "Sumitomo",
    "avs" : {
      "code" : "2"
    }
  },
  "reconciliationId" : "0020230518053410000000000001",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2023-05-17T20:34:10Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:82bfd8b7`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
