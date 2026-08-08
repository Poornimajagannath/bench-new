---
title: Sale with Payment Network Tokens
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: pnt_sale_intro
lineage_origin: generated_from_endpoint_fact
---

# Sale with Payment Network Tokens

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-sale-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-sale-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| processingInformation.capture |  | yes | Set the value to `true`. |

## Example request

```json
{
  "orderInformation" : {
    "billTo": {
      "country": "US",
      "lastName": "Kim",
      "address1": "201 S. Division St.",
      "postalCode": "48104-2201",
      "locality": "Ann Arbor",
      "administrativeArea": "MI",
      "firstName": "Smith",
      "email": "test@cybs.com"
    },
    "amountDetails" : {
      "totalAmount" : "100",
      "currency" : "USD"
    }
  },
    "paymentInformation" : {
    "tokenizedCard" : {
      "expirationYear" : "2031",
      "number" : "CARD_NUMBER",
      "expirationMonth" : "12",
      "transactionType" : "1",
      "cryptogram" : "qE5juRwDzAUFBAkEHuWW9PiBkWv="
    }
  }
}
```

## Example response

```json
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6838294805206235603954/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6838294805206235603954"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6838294805206235603954/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "1683829480593"
    },
    "id": "6838294805206235603954",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
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
    "reconciliationId": "60332034UHI9PRJ0",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-05-11T18:24:40Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:6530c927`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
