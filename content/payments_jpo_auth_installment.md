---
title: Authorize an Installment Payment with Japanese Payment Options
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_jpo_auth_installment
lineage_origin: generated_from_endpoint_fact
---

# Authorize an Installment Payment with Japanese Payment Options

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-jpo-auth-installment](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-jpo-auth-installment)  

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
| paymentInformation.card.type |  | yes |  |
| processingInformation.japanPaymentOptions.businessName |  | yes | Business name in kanji characters. |
| processingInformation.japanPaymentOptions.businessNameAlphaNumeric |  | yes |  |
| processingInformation.japanPaymentOptions.businessNameKatakana |  | yes |  |
| processingInformation.japanPaymentOptions.firstBillingMonth |  | yes | If you do not specify this field, it is set by default to the number of the next month. |
| processingInformation.japanPaymentOptions.installments |  | yes | Number of monthly payments. |
| processingInformation.japanPaymentOptions.paymentMethod |  | yes | Set the value to `61`. |
| processingInformation.japanPaymentOptions.terminalId |  | yes | Required for card-present transactions. Unique Japan Credit Card Association (JCCA) terminal identifier that is provided by `Cybersource`. |

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
            "currency": "jpy"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "CARD_NUMBER",
            "expirationMonth": "12",
            "type": "001"
        }
    },
    "processingInformation": {
        "japanPaymentOptions": {
            "businessName": "我社",
            "businessNameAlphaNumeric": "OurStore",
            "businessNameKatakana": "わが社の場合",
            "firstBusinessMonth": "04",
            "installments": "12",
            "paymentMethod": "31"
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
      "href" : "/pts/v2/payments/6843585327946622203059/reversals"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/6843585327946622203059"
    },
    "capture" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/6843585327946622203059/captures"
    }
  },
  "clientReferenceInformation" : {
    "code" : "RTS-Auth"
  },
  "id" : "6843585327946622203059",
  "orderInformation" : {
    "invoiceDetails" : {
      "salesSlipNumber" : "56311"
    },
    "amountDetails" : {
      "authorizedAmount" : "100",
      "currency" : "jpy"
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
    "salesSlipNumber" : "56311",
    "approvalCode" : "123456",
    "cardVerification" : {
      "resultCode" : "3"
    },
    "responseCategoryCode" : "000",
    "forwardedAcquirerCode" : "Sumitomo",
    "avs" : {
      "code" : "2"
    }
  },
  "reconciliationId" : "0020230518062213000000000001",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2023-05-17T21:22:13Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:e0137fcd`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
