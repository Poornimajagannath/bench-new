---
title: Time-Out Void for a Capture, Sale, Refund, or Credit
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_timeout_void_intro
lineage_origin: generated_from_endpoint_fact
---

# Time-Out Void for a Capture, Sale, Refund, or Credit

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/voids/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/voids/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-timeout-void-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-timeout-void-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.transactionId |  | yes |  |

## Example request

```json
{
  "clientReferenceInformation": {
    "transactionId": "987654321"
  }
}
```

## Example response

```json
{
  "_links": {
    "self": {
      "method": "GET",
        "href": "/pts/v2/voids/6541933390746728203005"
    }
  },
  "clientReferenceInformation": {
    "code": "1654193339056"
  },
  "id": "6541933390746728203005",
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    }
  },
  "status": "VOIDED",
  "submitTimeUtc": "2022-06-02T18:08:59Z",
  "voidAmountDetails": {
    "currency": "usd",
    "voidAmount": "100.00"
  }
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:63f1f445`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
