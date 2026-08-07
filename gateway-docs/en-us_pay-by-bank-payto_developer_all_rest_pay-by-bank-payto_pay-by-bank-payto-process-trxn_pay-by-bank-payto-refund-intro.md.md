Refund a Payment {#pay-by-bank-payto-refund-intro}
==================================================

Request a refund to return the funds from a completed payment. Refunding a payment requires the transaction ID from a capture or sale response.

Supported Refund Services
-------------------------

These refund services are available with PayTo Pay by Bank:

* Full refunds for the same amount of the original sale
* Partial refunds for an amount less than the original sale
  {#pay-by-bank-payto-refund-intro_ul_qhr_1vz_4gc}

Endpoints {#pay-by-bank-payto-refund-intro_section_l3f_xrs_fgc}
---------------------------------------------------------------

**Production:** `POST ``https://api.example.com``/pts/v2/payments`{#pay-by-bank-payto-refund-intro_d7e345}  
**Test:** `POST ``https://apitest.example.com``/pts/v2/payments`{#pay-by-bank-payto-refund-intro_d7e355}

Required Fields for Refunding a Payment {#pay-by-bank-payto-refund-req-fields}
==============================================================================

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set to an 18-character value or less.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:
Set to `AUD`.

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `payToPayByBank`.

[paymentInformation.paymentType.name](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `bankTransfer`.

[processingInformation.actionList](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_REFUND`.
{#pay-by-bank-payto-refund-req-fields_dl_pvj_hhl_fgc}

Example: Refunding a Payment {#pay-by-bank-payto-refund-ex-rest}
================================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "name": "bankTransfer",
      "method": {
        "name": "payToPayByBank"
      }
    }
  },
  "processingInformation": {
    "actionList": ["AP_REFUND"]
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "AUD"
    }
  }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "responseCode": "00001",
        "transactionId": "9af6bd29-8ea9-4f30-b6d4-58313566bcb0"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "AUD"
        }
    },
    "reconciliationId": "KOZX0DMQKX0D",
    "message": "Request was processed successfully.",
    "status": "PENDING",
    "id": "7544094135706957804805",
    "submitTimeUtc": "2025-08-05T17:52:08Z"
}
```

