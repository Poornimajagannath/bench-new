---
title: JCB J/Secure
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_pa_jcb_intro
lineage_origin: generated_from_endpoint_fact
---

# JCB J/Secure

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro)  

## Request body fields

_**Gap:** no Required Fields list in the product-root guide for this endpoint._

## Example request

```json
{
  "clientReferenceInformation": {
     "code": "TC50171_3"
  },
  "processingInformation": {
      "commerceIndicator": "js"
  },
  "paymentInformation": {
      "card": {
      "number": "3400000XXXXXXX8",
      "expirationMonth": "01",
      "expirationYear": "2025"
   }
 },
   "orderInformation": {
      "amountDetails": {
      "totalAmount": "100",
      "currency": "USD"
   },
   "billTo": {
      "firstName": "John",
      "lastName": "Smith",
      "address1": "201 S. Division St._1",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "accept@who.com",
      "phoneNumber": "6504327113"
    }
  },
      "consumerAuthenticationInformation": {
      "cavv": "1234567890987654321ABCDEFabcdefABCDEF123",
      "xid": "1234567890987654321ABCDEFabcdefABCDEF123"
      }
  }
```

## Example response

```json
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/6783071542936193303955/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6783071542936193303955"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6783071542936193303955/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "6783071542936193303955",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "100.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "003"
    }
  },
  "paymentInformation": {
    "accountFeatures": {
      "currency": "usd",
      "balanceAmount": "70.00"
    },
    "tokenizedCard": {
      "type": "003"
    },
    "card": {
      "type": "003"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "111111"
  },
  "processorInformation": {
    "approvalCode": "888888",
    "networkTransactionId": "123456789619999",
    "transactionId": "123456789619999",
    "responseCode": "100",
    "avs": {
      "code": "X",
      "codeRaw": "I1"
    }
  },
  "reconciliationId": "62427259FEYR18Q2",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2023-03-08T20:25:54Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:2105ea0b`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
