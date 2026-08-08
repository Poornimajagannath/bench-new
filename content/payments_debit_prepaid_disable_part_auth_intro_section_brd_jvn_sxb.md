---
title: Field Specific to this Use Case
generated: true
source: en-us_payments_developer_ctv_rest_payments.md.md
operation_id: payments_debit_prepaid_disable_part_auth_intro_section_brd_jvn_sxb
lineage_origin: generated_from_endpoint_fact
---

# Field Specific to this Use Case

<!-- section:prose -->
## Overview

Guide-derived reference for `POST /pts/v2/payments`.

<!-- /section:prose -->

<!-- section:facts -->
**Method:** `POST`  
**Path:** `/pts/v2/payments`  
**test host:** `https://apitest.cybersource.com`  
**Source:** [https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb)  

## Request body fields

_**Gap:** no Required Fields list in the product-root guide for this endpoint._

## Example request

```json
{
    "processingInformation":{
		"authorizationOptions":{
			"partialAuthIndicator": "false"
		}
	},
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
      "totalAmount" : "501.00",
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
  }
}
```

## Example response

```json
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6595545423896900104953"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "errorInformation": {
        "reason": "PROCESSOR_DECLINED",
        "message": "Decline - General decline of the card. 
                    No other information provided by the issuing bank."
    },
    "id": "6595545423896900104953",
    "pointOfSaleInformation": {
        "terminalId": "111111"
    },
    "processorInformation": {
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "X",
            "codeRaw": "I1"
        }
    },
    "status": "DECLINED"
}
```

## Provenance

- `lineage_origin`: `generated_from_endpoint_fact`
- `unit_id`: `payments:endpoint:post:a5122230`
- `claim source`: `en-us_payments_developer_ctv_rest_payments.md.md`

Every fact on this page traces to an `endpoint_fact` extracted from the payments product root. Not the OpenAPI fixture path.

<!-- /section:facts -->
