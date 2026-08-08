---
title: Basic Authorization
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_basic_auth_intro
lineage_origin: generated_from_endpoint_fact
---

# Basic Authorization

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-basic-auth-intro)  

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
| paymentInformation.card.number |  | yes | Country-Specific Required Fields for Processing a Basic Authorization ======================================================================================================================== |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| merchantInformation.transactionLocalDateTime |  | yes | Required in Argentina when the time zone is not included in your account. Otherwise, this field is optional. |
| paymentInformation.card.sourceAccountType |  | yes | Required for combo card transactions. |
| paymentInformation.card.sourceAccountTypeDetails |  | yes | Required for combo card line-of-credit and prepaid-card transactions. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| paymentInformation.card.cardType |  | yes | Required for Meeza transactions. Set the value to `067`. |
| merchantInformation.merchantDescriptor.country |  | yes | Required for Meeza transactions. Set the value to `EG`. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| processingInformation.authorizationOptions.transactionMode |  | yes | Required only for merchants in Saudi Arabia. |
| paymentInformation.card.hashedNumber |  | yes | Required only for merchants in Taiwan. |

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
            "email": "test@cybs.com"
        },
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "usd"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "CARD_NUMBER",
            "expirationMonth": "12",
            "type": "001"
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
      "type" : "001"
    }
  },
  "paymentInformation" : {
    "tokenizedCard" : {
      "type" : "001"
    },
    "card" : {
      "type" : "001"
    }
  },
 "paymentInsightsInformation" : {
    "responseInsights" : {
      "categoryCode" : "01"
    }
  },
  "processorInformation" : {
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
  "submitTimeUtc" : "2022-03-01T22:19:12Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:ee783368`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
