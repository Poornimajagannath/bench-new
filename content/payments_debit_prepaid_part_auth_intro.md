---
title: Enabling Debit and Prepaid Partial Authorizations
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_debit_prepaid_part_auth_intro
lineage_origin: generated_from_endpoint_fact
---

# Enabling Debit and Prepaid Partial Authorizations

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-part-auth-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-part-auth-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |
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
| paymentInformation.card.type |  | yes |  |
| paymentInformation.card.expirationMonth |  | yes |  |
| paymentInformation.card.expirationYear |  | yes |  |
| paymentInformation.card.number |  | yes |  |
| processingInformation.authorizationOptions.partialAuthIndicator |  | yes | Set the value to `true`. |
| processingInformation.linkId |  | yes | Set this field to the request ID that was returned in the response message from the original authorization request. |

## Example request

```json
{
  "clientReferenceInformation" : {
    "code" : "TC50171_3"
  },
  "orderInformation" : {
    "billTo" : {
      "country" : "US",
      "lastName" : "Deo",
      "address2" : "Address 2",
      "address1" : "201 S. Division St.",
      "postalCode" : "48104-2201",
      "locality" : "Ann Arbor",
      "administrativeArea" : "MI",
      "firstName" : "John",
      "phoneNumber" : "999999999",
      "district" : "MI",
      "buildingNumber" : "123",
      "company" : "Visa",
      "email" : "test@cybs.com"
    },
    "amountDetails" : {
      "totalAmount" : "1000.00",
      "currency" : "USD"
    }
  },
  "paymentInformation" : {
    "card" : {
      "expirationYear" : "2031",
      "number" : "5555555555xxxxxx",
      "securityCode" : "123",
      "expirationMonth" : "12",
      "type" : "002"
    }
  },
"processingInformation" : {
  "authorizationOptions" : {
      "partialAuthIndicator" : "true"
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
      "href" : "/pts/v2/payments/6595549144566655003494"
    }
  },
  "clientReferenceInformation" : {
    "code" : "TC50171_3"
  },
  "id" : "6595549144566655003494",
  "orderInformation" : {
    "amountDetails" : {
      "totalAmount" : "1000.00",
      "authorizedAmount" : "499.01",
      "currency" : "USD"
    }
  },
  "paymentInformation" : {
    "accountFeatures" : {
      "currency" : "usd",
      "balanceAmount" : "0.00"
    }
  },
  "pointOfSaleInformation" : {
    "terminalId" : "261996"
  },
  "processorInformation" : {
    "merchantNumber" : "000000092345678",
    "approvalCode" : "888888",
    "cardVerification" : {
      "resultCode" : ""
    },
    "networkTransactionId" : "123456789619999",
    "transactionId" : "123456789619999",
    "responseCode" : "100",
    "avs" : {
      "code" : "X",
      "codeRaw" : "I1"
    }
  },
  "reconciliationId" : "56059417N6C86KTJ",
  "status" : "PARTIAL_AUTHORIZED",
  "submitTimeUtc" : "2022-08-03T19:28:34Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:6f3c108b`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
