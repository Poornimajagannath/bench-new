---
title: Incremental Authorization
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_auth_inc_intro
lineage_origin: generated_from_endpoint_fact
---

# Incremental Authorization

<!-- section:prose -->
## Overview

Guide-derived reference for `PATCH /pts/v2/payments/`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `PATCH`  
**Path:** `/pts/v2/payments/`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-inc-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-inc-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes |  |
| orderInformation.amountDetails.currency |  | yes |  |
| merchantInformation.transactionLocalDateTime |  | yes | Required in Argentina when the time zone is not included in your account. Otherwise, this field is optional. |
| clientReferenceInformation.transactionId |  | yes |  |

## Example request

```json
{
  "clientReferenceInformation": {
    "code": "33557799"
  },
  "orderInformation" : {
    "amountDetails" : {
      "totalAmount": "105.00",
      "currency" : "USD"
    }
  }
  "merchantInformation": {
    "transactionLocalDateTime": "20261002080000"
  }
}
```

## Example response

```json
{
  "_links" : {
    "authReversal" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6479624584536070903093/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6479624584536070903093"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6479624584536070903093/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "33557799"
  },
  "id" : "6479624584536070903093",
  "orderInformation" : {
    "amountDetails" : {
      "authorizedAmount" : "105.00",
      "currency" : "USD"
    }
  },
  "paymentAccountInformation" : {
    "card" : {
      "type" : "00X"
    }
  },
  "paymentInformation" : {
    "tokenizedCard" : {
      "type" : "00X"
    },
    "card" : {
      "type" : "00X"
    }
  },
  "processorInformation" : {
    "systemTraceAuditNumber" : "819203",
    "approvalCode" : "831000",
    "cardVerification" : {
      "resultCodeRaw" : "M",
      "resultCode" : "M"
    },
    "merchantAdvice" : {
      "code" : "01",
      "codeRaw" : "M001"
    },
    "responseDetails" : "ABC",
    "networkTransactionId" : "016153570198200",
    "retrievalReferenceNumber" : "208115819203",
    "consumerAuthenticationResponse" : {
      "code" : "2",
      "codeRaw" : "2"
    },
    "transactionId" : "016153570198200",
    "responseCode" : "00",
    "avs" : {
      "code" : "Y",
      "codeRaw" : "Y"
    }
  },
  "reconciliationId" : "6479624584536070903093",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2026-03-22T15:20:58Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:patch:e3835daa`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
