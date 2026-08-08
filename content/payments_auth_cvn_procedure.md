---
title: Authorization with a Card Verification Number
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_auth_cvn_procedure
lineage_origin: generated_from_endpoint_fact
---

# Authorization with a Card Verification Number

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-auth-cvn-procedure](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-auth-cvn-procedure)  

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
| paymentInformation.card.securityCode |  | yes |  |
| paymentInformation.card.type |  | yes |  |
| paymentInformation.card.securityCode |  | yes | Optional Fields for Processing an Authorization with a Card Verification Number ============================================================================================================= |
| paymentInformation.card.securityCodeIndicator |  | yes |  |
| processingInformation.authorizationOptions.ignoreCvResult |  | yes |  |

## Example request

```json
{
    "paymentInformation": {
        "card": {
        "number": "CARD_NUMBER",
        "expirationMonth": "12",
        "expirationYear": "2031",
        "type": "001",
        "securityCode": "999"
        }
    },
    "orderInformation": {
        "amountDetails": {
        "totalAmount": "49.95",
        "currency": "USD"
    },
     "billTo": {
        "firstName": "John",
        "lastName": "Doe",
        "address1": "1295 Charleston Rd.",
        "locality": "Mountain View",
        "administrativeArea": "CA",
        "postalCode": "94043",
        "country": "US",
        "email": "jdoe@example.com",
        "phoneNumber": "650-965-6000"
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
            "href": "/pts/v2/payments/6554147587216874903954/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6554147587216874903954"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6554147587216874903954/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "1655414758839"
    },
    "id": "6554147587216874903954",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "49.95",
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
    "reconciliationId": "67546603C43Z6JWN",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2022-06-16T21:25:58Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:6f875721`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
