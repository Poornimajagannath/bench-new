Processing a Healthcare Sale {#healthcare-sale-intro}
=====================================================

This section provides the information you need to process a healthcare sale transaction.  
A sale combines an authorization and a capture into a single transaction.

Endpoint {#healthcare-sale-intro_d15e240}
-----------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#healthcare-sale-intro_d15e248}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#healthcare-sale-intro_d15e258}

Required Fields for Processing a Healthcare Sale {#healthcare-sale-reqfields}
=============================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[healthCareInformation.amountDetails.amount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/healthcare-info-aa/healthcare-info-amount-details-amount-a.md "")
:

[healthCareInformation.amountDetails.amountType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/healthcare-info-aa/healthcare-info-amount-details-amount-type.md "")
:
Possible values:

    * `clinic`
    * `dental`
    * `healthcare`: The amount for this type should be greater than or equal to the sum of all amount types included in the request.
    * `prescription`
    * `vision`
    These values cannot be repeated in the request. Example: If there are two vision items purchased for 10.00, send one vision amount for 20.00.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](URL "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.productSubtype](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-product-subtype.md "")
:
Set the value to `HC`.

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.capture](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true`.
{#healthcare-sale-reqfields_dl_uc5_btg_rdc}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Processing a Healthcare Sale {#healthcare-sale-ex-rest}
=====================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "HC-sale"
  },
  "processingInformation": {
    "capture": true
  },
  "orderInformation": {
    "billTo": {
      "country": "US",
      "lastName": "VDP",
      "address2": "test",
      "address1": "201 S. Division St.",
      "postalCode": "48104-2201",
      "locality": "Ann Arbor",
      "administrativeArea": "MI",
      "firstName": "RTS",
      "phoneNumber": "999999999",
      "district": "MI",
      "buildingNumber": "123",
      "company": "Relay",
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
      "number": "4111111111111111",
      "securityCode": "123",
      "expirationMonth": "12",
      "type": "001",
      "productSubtype": "HC"
    }
  },
  "healthCareInformation": {
    "amountDetails": [
      {
        "amountType": "healthcare",
        "amount": "100"
      },
      {
        "amountType": "prescription",
        "amount": "50"
      },
      {
        "amountType": "clinic",
        "amount": "20"
      },
      {
        "amountType": "dental",
        "amount": "25"
      },
      {
        "amountType": "vision",
        "amount": "5"
      }
    ]
  }
}
```

Response to a Successful Request

```
{
  "_links" : {
    "void" : {
      "method" : "POST",
      "href" : "/pts/v2/payments/7338783664396669903091/voids"
    },
    "self" : {
      "method" : "GET",
      "href" : "/pts/v2/payments/7338783664396669903091"
    }
  },
  "clientReferenceInformation" : {
    "code" : "HC-sale"
  },
  "id" : "7338783664396669903091",
  "orderInformation" : {
    "amountDetails" : {
      "totalAmount" : "100.00",
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
  "pointOfSaleInformation" : {
    "terminalId" : "261996"
  },
  "processorInformation" : {
    "merchantNumber" : "000000092345678",
    "approvalCode" : "888888",
    "networkTransactionId" : "123456789619999",
    "transactionId" : "123456789619999",
    "responseCode" : "100",
    "avs" : {
      "code" : "X",
      "codeRaw" : "I1"
    }
  },
  "reconciliationId" : "57223666D4F86E0S",
  "status" : "AUTHORIZED",
  "submitTimeUtc" : "2024-12-11T00:52:46Z"
}
```

