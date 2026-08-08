---
title: Follow-On Refund
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_refund_intro
lineage_origin: generated_from_endpoint_fact
---

# Follow-On Refund

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-refund-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-refund-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |

## Example request

```json
{
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "EUR"
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
            "href": "/pts/v2/credits/6699964581696622603955/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/credits/6699964581696622603955"
        }
    },
    "clientReferenceInformation": {
        "code": "1669996458298"
    },
    "creditAmountDetails": {
        "currency": "eur",
        "creditAmount": "100.00"
    },
    "id": "6699964581696622603955",
    "orderInformation": {
        "amountDetails": {
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
        "approvalCode": "888888",
        "networkTransactionId": "016153570198200",
        "responseCode": "100"
    },
    "reconciliationId": "61873329OAILG3Q6",
    "status": "PENDING",
    "submitTimeUtc": "2022-12-02T15:54:18Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:51bd9f69`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
