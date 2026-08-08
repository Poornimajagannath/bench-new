---
title: Mastercard Identity Check
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_pa_mc_intro
lineage_origin: generated_from_endpoint_fact
---

# Mastercard Identity Check

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro)  

## Request body fields

_**Gap:** no Required Fields list in the product-root guide for this endpoint._

## Example request

```json
{
  "clientReferenceInformation" : {
    "code" : "TC50171_6"
  },
  "consumerAuthenticationInformation" : {
    "ucafCollectionIndicator" : "2",
    "ucafAuthenticationData" : "EHuWW9PiBkWvqE5juRwDzAUFBAk",
    "directoryServerTransactionId" : "f38e6948-5388-41a6-bca4-b49723c19437",
    "paSpecificationVersion" : "2.2.0"
  },
  "processingInformation" : {
    "commerceIndicator" : "spa"
    },
    "orderInformation" : {
      "billTo" : {
        "country" : "US",
        "lastName" : "Deo",
        "address1" : "201 S. Division St.",
        "postalCode" : "48104-2201",
        "locality" : "Ann Arbor",
        "administrativeArea" : "MI",
        "firstName" : "John",
        "email" : test@cybs.com
      },
      "amountDetails" : {
        "totalAmount" : "105.00",
        "currency" : "USD"
      }
    },
    "paymentInformation" : {
      "card" : {
        "expirationYear" : "2031",
        "number" : "555555555555XXXX",
        "securityCode" : "123",
        "expirationMonth" : "12",
        "type" : "002"
    }
  }
}
```

## Example response

```json
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/6758990751436655004951/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6758990751436655004951"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6758990751436655004951/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "6758990751436655004951",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "100.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "002"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "type": "002"
    },
    "card": {
      "type": "002"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "111111"
  },
  "processorInformation": {
    "approvalCode": "888888",
    "authIndicator": "1",
    "networkTransactionId": "123456789619999",
    "transactionId": "123456789619999",
    "responseCode": "100",
    "avs": {
      "code": "X",
      "codeRaw": "I1"
    }
  },
  "reconciliationId": "71183995FDU0YRTK",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-02-08T23:31:15Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:46e33c56`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
