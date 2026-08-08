---
title: Fields Specific to the Strong Customer Authentication Exemptions
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_pa_sca_exempts_intro_fields_specific_to_auth
lineage_origin: generated_from_endpoint_fact
---

# Fields Specific to the Strong Customer Authentication Exemptions

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-sca-exempts-intro_fields-specific-to-auth](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-sca-exempts-intro_fields-specific-to-auth)  

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

## Example request

```json
{
  "consumerAutenticationInformation" : {
  	"strongAuthentication" : {
  	  "lowValueExemptionIndicator" : "1"
  	}
  },
  "orderInformation" : {
    "billTo" : {
      "country" : "US",
      "lastName" : "Kim",
      "address1" : "201 S. Division St.",
      "postalCode" : "48104-2201",
      "locality" : "Ann Arbor",
      "administrativeArea" : "MI",
      "firstName" : "Kyong-Jin",
      "email" : "test@cybs.com"
    },
    "amountDetails" : {
      "totalAmount" : "100.00",
      "currency" : "eur"
    }
  },
  "paymentInformation" : {
    "card" : {
      "expirationYear" : "2031",
      "number" : "CARD_NUMBER",
      "expirationMonth" : "12"
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
            "href": "/pts/v2/payments/6709780221406171803955/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6709780221406171803955"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6709780221406171803955/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "1670978022258"
    },
    "id": "6709780221406171803955",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "100.00",
            "currency": "eur"
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
    "pointOfSaleInformation": {
        "terminalId": "123456"
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
    "reconciliationId": "62859554PBDEMI43",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-12-14T00:33:42Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:66095066`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
