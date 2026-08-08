---
title: Card Types
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_processing_zero_auth_ani_intro_ani_card_rules
lineage_origin: generated_from_endpoint_fact
---

# Card Types

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-zero-auth-ani-intro_ani-card-rules](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-zero-auth-ani-intro_ani-card-rules)  

## Request body fields

| Name | Type | Required | Notes |
| --- | --- | --- | --- |
| orderInformation.amountDetails.currency |  | yes |  |
| orderInformation.amountDetails.totalAmount |  | yes | Set the value to `0`. |
| orderInformation.billTo.address1 |  | yes |  |
| orderInformation.billTo.address2 |  | yes |  |
| orderInformation.billTo.administrativeArea |  | yes |  |
| orderInformation.billTo.country |  | yes |  |
| orderInformation.billTo.email |  | yes |  |
| orderInformation.billTo.firstName |  | yes |  |
| orderInformation.billTo.lastName |  | yes |  |
| orderInformation.billTo.locality |  | yes |  |
| orderInformation.billTo.phoneNumber |  | yes |  |
| orderInformation.billTo.postalCode |  | yes |  |
| paymentInformation.card.expirationMonth |  | yes |  |
| paymentInformation.card.expirationYear |  | yes |  |
| paymentInformation.card.number |  | yes |  |
| paymentInformation.card.securityCode |  | yes |  |
| paymentInformation.card.type |  | yes | processingInformation.cardVerification.checkANI Set to `Y`. |
| orderInformation.billTo.middleName |  | yes | processingInformation.authorizationOptions.declineAniFlags Possible values separated by a space: |
| recipientInformation.firstName |  | yes | recipientInformation.middleName |
| senderInformation.firstName |  | yes | senderInformation.middleName |

## Example request

```json
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "paymentInformation": {
    "card": {
      "number": "CARD_NUMBER",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "securityCode": "501"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "0.00",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com",
      "phoneNumber": "4158880000"
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
      "href": "/pts/v2/payments/7664012361876450803814/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7664012361876450803814"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7664012361876450803814/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7664012361876450803814",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "0.00",
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
    "systemTraceAuditNumber": "065281",
    "electronicVerificationResults": {
      "lastName": "Y",
      "firstName": "Y",
      "code": "Y",
      "middleNameRaw": "01",
      "firstNameRaw": "01",
      "lastNameRaw": "01",
      "codeRaw": "01",
      "middleName": "Y"
    },
    "merchantNumber": "123456789012",
    "approvalCode": "831000",
    "cardVerification": {
      "resultCodeRaw": "M",
      "resultCode": "M"
    },
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001",
      "nameMatch": "00"
    },
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "535611065281",
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
  "reconciliationId": "7664012361876450803814",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-12-22T11:00:36Z"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:5211b842`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
