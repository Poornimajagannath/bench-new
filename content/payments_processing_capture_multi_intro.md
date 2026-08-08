---
title: Multiple Partial Capture
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_capture_multi_intro
lineage_origin: generated_from_endpoint_fact
---

# Multiple Partial Capture

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-capture-multi-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-capture-multi-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes | Set to clientReferenceInformation.code value used in corresponding authorization request. |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |
| processingInformation.captureOptions. captureSequenceNumber |  | yes | For the final capture request, set this field and processingInformation.captureOptions.totalCaptureCount to the same value. |
| processingInformation.captureOptions. totalCaptureCount |  | yes | When you do not know the total number of captures that you are going to request, set this field to at least one more than the processingInformation.captureOptions. captureSequenceNumber field until you reach the final capture. For the final capture request, set this field and processingInformation.captureOptions. captureSequenceNumber to the same value. |

## Example request

```json
{
  {
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "processingInformation": {
    "captureOptions": {
      "captureSequenceNumber": "2",
      "totalCaptureCount": "3"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
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
      "href": "/pts/v2/captures/6742496815656503003954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/captures/6742496815656503003954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "6742496815656503003954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    }
  },
  "reconciliationId": "67332020GD2G1OO1",
  "status": "PENDING",
  "submitTimeUtc": "2023-01-20T21:21:21Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:fa0fe448`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
