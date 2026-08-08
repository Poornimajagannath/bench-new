---
title: Visa Secure
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_pa_visa_intro
lineage_origin: generated_from_endpoint_fact
---

# Visa Secure

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-visa-intro](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-visa-intro)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| clientReferenceInformation.code |  | yes |  |
| consumerAuthenticationInformation.cavv |  | yes | This field is required when payer authentication is successful. Otherwise, this field is optional. |
| consumerAuthenticationInformation.xid |  | yes |  |
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
| processingInformation.commerceIndicator |  | yes | Set this field to one of these values: |

## Example request

```json
{
    "clientReferenceInformation": {
        "code": "test"
    },
    "processingInformation": {
        "capture": "true",
        "authorizationOptions": {
            "ignoreAvsResult": "true"
        },
        "actionList": [
            "VALIDATE_CONSUMER_AUTHENTICATION"
        ]
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "4XXXXXXXXXXX25X3",
            "securityCode": "123",
            "expirationMonth": "12",
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "GBP"
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Smith",
            "address1": "201 S. Division St._1",
            "address2": "Suite 500",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "postalCode": "94404",
            "country": "US",
            "email": "accept@email.com",
            "phoneNumber": "6504327113"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "2b4eAa4K3H778X34Ciy0"
    }
}
```

## Example response

```json
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7478305945626990404807/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7478305945626990404807"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "indicator": "vbv",
        "eciRaw": "05",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "eci": "05",
        "token": "Axj//wSTlWZX08jkcOTHAAIU3YMmzhgzcN2ie/LXsgSgKe/LXsgS50OnEFBWGTSTL0Yua1eAwHScqzK+nkcjhyY4wDi0",
        "cavv": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "paresStatus": "Y",
        "xid": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "fa628ed8-ad77-4723-b28f-91952eaca8fe",
        "threeDSServerTransactionId": "71399671-8456-4c97-b056-e127622a5e26",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "5f9fb589-08cc-4952-866d-30939868f411"
    },
    "id": "7478305945626990404807",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "authorizedAmount": "100.00",
            "currency": "GBP"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "brandName": "VISA",
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "bin": "400000",
            "type": "VISA"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678"
    },
    "processorInformation": {
        "paymentAccountReferenceNumber": "V0010013018036776997406844475",
        "merchantNumber": "12345678",
        "approvalCode": "100",
        "cardVerification": {
            "resultCodeRaw": "3",
            "resultCode": "2"
        },
        "merchantAdvice": {
            "code": "00",
            "codeRaw": "0"
        },
        "networkTransactionId": "123456789012345",
        "transactionId": "123456789012345",
        "responseCode": "0",
        "avs": {
            "code": "U",
            "codeRaw": "00"
        }
    },
    "reconciliationId": "7026803874",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-05-21T12:29:54Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:0aea3651`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
