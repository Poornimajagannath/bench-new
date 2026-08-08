---
title: Capture
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_capture_intro
lineage_origin: generated_from_endpoint_fact
---

# Capture

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-capture-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-capture-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes | This field value maps from the original authorization, sale, or credit transaction. |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |

## Example request

```json
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

## Example response

```json
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

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:b050fd41`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
