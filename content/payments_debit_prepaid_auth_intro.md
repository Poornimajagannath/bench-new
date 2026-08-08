---
title: Processing Debit and Prepaid Authorizations
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_debit_prepaid_auth_intro
lineage_origin: generated_from_endpoint_fact
---

# Processing Debit and Prepaid Authorizations

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-auth-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-auth-intro)  

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
| paymentInformation.card.number |  | yes | Country Specific Required Fields to Process Debit and Prepaid Authorizations ============================================================================================================================ |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| merchantInformation.transactionLocalDateTime |  | yes | Required in Argentina when the time zone is not included in your account. Otherwise, this field is optional. |
| paymentInformation.card.sourceAccountType |  | yes | Required for combo card transactions. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| merchantInformation.taxId |  | yes | Required for Mastercard transactions. |
| processingInformation.authorizationOptions.transactionMode |  | yes | Taiwan ------ |
| paymentInformation.card.hashedNumber |  | yes | Optional Field for Processing Debit and Prepaid Authorizations ====================================================================================================== |
| processingInformation.linkId |  | yes | Set this field to the request ID that was returned in the response message from the original authorization request. |

## Example request

```json
{
  "orderInformation" : {
    "billTo" : {
      "country" : "US",
      "firstName" : "John",
      "lastName" : "Deo",
      "address1" : "901 Metro Center Blvd",
      "postalCode" : "40500",
      "locality" : "Foster City",
      "administrativeArea" : "CA",
      "email" : "test@cybs.com"
},
    "amountDetails" : {
      "totalAmount" : "100.00",
      "currency" : "USD"
    }
  },
  "paymentInformation" : {
    "card" : {
      "expirationYear" : "2031",
      "number" : "CARD_NUMBER",
      "securityCode" : "123",
      "expirationMonth" : "12",
      "type" : "001"
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
      "href" : "/pts/v2/payments/6595482584316313203494/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6595482584316313203494"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6595482584316313203494/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "RTS-Auth"
  },
  "consumerAuthenticationInformation" : {
    "token" : "Axj/7wSTZYq1MhJBMfMmAEQs2auWrRwyauGjNi2ZsWbJgzaOWiaVA+JbK
               AU0qB8S2VpA6cQIp4ZNvG2YbC9eM4E5NlirUyEkEx8yYAAA4A1c"
  },
  "id" : "6595482584316313203494",
  "orderInformation" : {
    "amountDetails" : {
      "authorizedAmount" : "100.00",
      "currency" : "USD"
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
  "processorInformation" : {
    "systemTraceAuditNumber" : "853428",
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
    "retrievalReferenceNumber" : "221517853428",
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
  }
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:4ff47631`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
