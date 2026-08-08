---
title: Void a Payment
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_sale_void_intro
lineage_origin: generated_from_endpoint_fact
---

# Void a Payment

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/credits/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/credits/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-sale-void-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-sale-void-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |

## Example request

```json
{
    "clientReferenceInformation": {
        "code": "123456789012"
    }
}
```

## Example response

```json
{
    "submitTimeUtc": "2025-03-11T16:39:30Z",
    "processorInformation": {
        "approvalCode": "OK1272",
        "responseCode": "000"
    },
    "consumerAuthenticationResponse": {
        "systemTraceAuditNumber": "500036"
    },
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "110.00"
        }
    },
    "message": "Successful transaction.",
    "clientReferenceInformation": {
        "code": "123456789012"
    },
    "reconciliationId": "000000050000771",
    "id": "7417111702443232235535",
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/voids/7417111702443232235535"
        }
    },
    "status": "VOIDED"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:b70bcadc`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
