---
title: Authorization with Line Items
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_auth_lineitem_intro
lineage_origin: generated_from_endpoint_fact
---

# Authorization with Line Items

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-lineitem-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-lineitem-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| orderInformation.amountDetails.currency |  | yes |  |
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
| paymentInformation.card.number |  | yes | Country-Specific Required Fields for Processing an Authorization with Line Items ======================================================================================================================================= |

## Example request

```json
{
  "currencyConversion": {
    "indicator": "Y"
  },
  "paymentInformation": {
    "card": {
      "number": "CARD_NUMBER",
      "expirationMonth": "12",
      "expirationYear": "2031"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "exchangeRate": ".91",
      "originalAmount": "107.33",
      "originalCurrency": "eur"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com"
    },
    "lineItems": [
      {
        "unitPrice": "10.00"
      },
      {
        "unitPrice": "5.99",
        "quantity": "3",
        "productCode": "shipping_only"
      },
      {
        "unitPrice": "29.99",
        "quantity": "3",
        "productCode": "electronic_good",
        "productSku": "12384569",
        "productName": "receiver"
      }
    ]
  }
}
```

## Example response

```json
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/6482385519226028804003/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/6482385519226028804003"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/6482385519226028804003/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "1648238551902"
  },
  "id": "6482385519226028804003",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "117.94",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "001"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "processorInformation": {
    "systemTraceAuditNumber": "191521",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "consumerAuthenticationResponse": {
      "code": "2",
      "codeRaw": "2"
    },
    "transactionId": "016153570198200",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "6482385519226028804003",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2022-03-25T20:02:32Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:610ade4f`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
