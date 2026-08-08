---
title: Requirement
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_mc_ems_intro_section_f35_1ps_5xb
lineage_origin: generated_from_endpoint_fact
---

# Requirement

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-mc-ems-intro_section_f35_1ps_5xb](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-mc-ems-intro_section_f35_1ps_5xb)  

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
| paymentInformation.card.number |  | yes | Response Field for Authorizations with Mastercard Expert Monitoring Solutions =============================================================================================================== |
| processorInformation.emsTransactionRiskScore |  | yes | Fraud score for a Mastercard transaction. |

## Example request

```json
{
    "orderInformation": {
        "billTo": {
            "country": "US",
            "lastName": "Kim",
            "address1": "201 S. Division St.",
            "postalCode": "48104-2201",
            "locality": "Ann Arbor",
            "administrativeArea": "MI",
            "firstName": "Kyong-Jin",
            "email": "kim.test@cybs.com"/&gt;"
        },
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "usd"
        }
    },
    "paymentInformation": {
        "card": {
            "number": "555555555555xxxx",
            "expirationYear": "2031",
            "expirationMonth": "12",
            "type": "002"
        }
    }
}
```

## Example response

```json
{
  "_links" : {
    "authReversal" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6461731521426399003473/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6461731521426399003473"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6461731521426399003473/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "1646173152047"
  },
  "id" : "6461731521426399003473",
  "orderInformation" : {
    "amountDetails" : {
      "authorizedAmount" : "100.00",
      "currency" : "usd"
    }
  },
  "paymentAccountInformation" : {
    "card" : {
      "type" : "002"
    }
  },
  "paymentInformation" : {
    "tokenizedCard" : {
      "type" : "002"
    },
    "card" : {
      "type" : "002"
    }
  },
 "paymentInsightsInformation" : {
    "responseInsights" : {
      "categoryCode" : "01"
    }
  },
  "processorInformation" : {
    "emsTransactionRiskScore": "84309",
    "systemTraceAuditNumber" : "862481",
    "approvalCode" : "831000",
    "merchantAdvice" : {
      "code" : "01",
      "codeRaw" : "M001"
    },
    "responseDetails" : "ABC",
    "networkTransactionId" : "016153570198200",
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
  "reconciliationId" : "6461731521426399003473",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2023-06-09T22:19:12Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:8bd9c494`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
