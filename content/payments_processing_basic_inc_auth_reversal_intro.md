---
title: Partial Authorization Reversal
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_inc_auth_reversal_intro
lineage_origin: generated_from_endpoint_fact
---

# Partial Authorization Reversal

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/reversals`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/reversals`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-inc-auth-reversal-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-inc-auth-reversal-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |
| orderInformation.amountDetails.currency |  | yes |  |
| reversalInformation.amountDetails.totalAmount |  | yes | Set to the amount that you want to reverse that does not exceed the amount of remaining authorized funds. |

## Example request

```json
{
  "clientReferenceInformation": {
    "code": "test123"
  },
  "reversalInformation": {
    "amountDetails": {
      "totalAmount": "20.00"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    }
  }
}
```

## Example response

```json
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
        "reversedAmount" : "20.00",
        "currency" : "USD"
    },
    "status" : "REVERSED",
    "submitTimeUtc" : "2026-06-16T20:07:02Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:96c5a3a6`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
