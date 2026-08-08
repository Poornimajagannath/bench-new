---
title: Authorization Reversal
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_auth_reversal_intro
lineage_origin: generated_from_endpoint_fact
---

# Authorization Reversal

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-reversal-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-reversal-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |
| clientReferenceInformation.partner.thirdPartyCertificationNumber |  | yes | `Cybersource` provides the value for this field. |
| reversalInformation.amountDetails.currency |  | yes |  |
| reversalInformation.amountDetails.totalAmount |  | yes | The amount of the reversal must be the same as the authorization amount that was included in the authorization response message. Do not use the amount that was requested in the authorization request message. |

## Example request

```json
{ 
    "clientReferenceInformation": { 
      "code": "test123"
    } 
    "reversalInformation" : { 
        "amountDetails" : { 
            "totalAmount" : "100.00",
            "currency" : "USD"
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
        "reversedAmount" : "100.00",
        "currency" : "USD"
    },
    "status" : "REVERSED",
    "submitTimeUtc" : "2023-06-16T20:07:02Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:2eb1c22e`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
