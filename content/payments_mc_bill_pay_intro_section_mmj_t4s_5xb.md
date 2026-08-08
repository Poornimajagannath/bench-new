---
title: Requirements
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_mc_bill_pay_intro_section_mmj_t4s_5xb
lineage_origin: generated_from_endpoint_fact
---

# Requirements

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-mc-bill-pay-intro_section_mmj_t4s_5xb](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-mc-bill-pay-intro_section_mmj_t4s_5xb)  

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
| paymentInformation.card.number |  | yes |  |
| processingInformation.authorizationOptions.billPaymentType |  | yes | Set the value to indicate the type of bill that the cardholder is paying. |

## Example request

```json
{
    "orderInformation": {
        "billTo": {
            "country": "BR",
            "lastName": "Doe",
            "firstName": "John",
            "address1": "Av Pres Juscelino Kubistchek 1909",
            "address2": "",
            "postalCode": "04543907",
            "locality": "Sao Paulo",
            "administrativeArea": "SP",
            "email": "john.doe@company.com"
        },
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "BRL"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2031",
            "number": "555555555555xxxx",
            "securityCode": "123",
            "type": "002"
        }
    },
    "processingInformation": {
        "authorizationOptions": {
            "billPaymentType": "001"
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
      "href" : "/pts/v2/payments/6863356803746501803955/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6863356803746501803955"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6863356803746501803955/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "1686335680358"
  },
  "id" : "6863356803746501803955",
  "orderInformation" : {
    "amountDetails" : {
      "authorizedAmount" : "100.00",
      "currency" : "brl"
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
  "processorInformation" : {
    "approvalCode" : "010012",
    "networkTransactionId" : "999010012",
    "transactionId" : "72b2900a9f316142b627a21031b48b0c259f08ffba0004172a04450c5d212345",
    "responseCode" : "400",
    "avs" : {
      "code" : "2"
    }
  },
  "reconciliationId" : "NHRRGOVtUxkb",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2023-06-09T18:34:40Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:604974ad`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
