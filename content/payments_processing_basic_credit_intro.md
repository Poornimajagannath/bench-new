---
title: Stand-Alone Credit
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_credit_intro
lineage_origin: generated_from_endpoint_fact
---

# Stand-Alone Credit

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/credits/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/credits/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-credit-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-credit-intro)  

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

## Example request

```json
{
  "orderInformation" : {
    "billTo" : {
      "country" : "US",
      "lastName" : "Kim",
      "address1" : "201 S. Division St.",
      "postalCode" : "48104-2201",
      "locality" : "Ann Arbor",
      "administrativeArea" : "MI",
      "firstName" : "Kyong-Jin",
      "email" : "test@cybs.com"
    },
    "amountDetails" : {
      "totalAmount" : "100.00",
      "currency" : "eur"
    }
  },
  "paymentInformation" : {
    "card" : {
      "expirationYear" : "2031",
      "number" : "CARD_NUMBER",
      "expirationMonth" : "12"
    }
  }
}
```

## Example response

```json
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/credits/6663069906146706403954/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/credits/6663069906146706403954"
        }
    },
    "clientReferenceInformation": {
        "code": "1666306990717"
    },
    "creditAmountDetails": {
        "currency": "eur",
        "creditAmount": "100.00"
    },
    "id": "6663069906146706403954",
    "orderInformation": {
        "amountDetails": {
            "currency": "eur"
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
        "approvalCode": "888888",
        "networkTransactionId": "016153570198200",
        "responseCode": "100"
    },
    "reconciliationId": "66490108K9CLFJPN",
    "status": "PENDING",
    "submitTimeUtc": "2022-10-20T23:03:10Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:a429ccd1`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
