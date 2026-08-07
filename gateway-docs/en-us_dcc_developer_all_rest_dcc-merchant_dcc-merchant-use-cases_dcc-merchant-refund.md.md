DCC Refund {#dcc-merchant-refund}
=================================

A DCC refund request refunds a captured DCC offer. These requests are used for both full and partial refunds.  
When processing a refund, apply the **same exchange rate** used at the time of payment authorization. Ensure the refunded amount does **not exceed** the originally captured amount.  
See the [Payments Developer Guide](https://developer.example.com/docs/gateway/en-us/payments/developer/ctv/rest/payments/payments-intro.md "") for more information.

Required Fields for DCC Refund {#dcc-merchant-refund-request-api-req-fields}
============================================================================

In addition to the normal fields required for a regular refund, these fields are required when DCC has been offered and the cardholder has chosen to pay in their billing currency.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.exchangeRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
:

[orderInformation.amountDetails. exchangeRateTimeStamp](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-time-stamp.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. foreignAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-foreign-amount.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. foreignCurrency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-foreign-currency.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. originalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:
Required for VPC transactions.

[orderInformation.amountDetails. originalCurrency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:
Required for VPC transactions.

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Example: DCC Refund {#dcc-merchant-api-ex-vpc-refund}
=====================================================

Request for Platform Connect

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "157.00",
      "currency": "AUD",
      "exchangeRate": "1.57",
      "originalAmount": "100.00",
      "originalCurrency": "USD"
    }
  }
}
```

Response for Platform Connect

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/refunds/7625571873626990704805/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/refunds/7625571873626990704805"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7625571873626990704805",
  "orderInformation": {
    "amountDetails": {
      "currency": "AUD"
    }
  },
  "reconciliationId": "7624789441456188503813",
  "refundAmountDetails": {
    "currency": "AUD",
    "refundAmount": "157.00"
  },
  "status": "PENDING",
  "submitTimeUtc": "2025-11-07T23:13:07Z"
}
```

Request for FDC Nashville Global

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "USD",
      "foreignAmount": "157.00",
      "foreignCurrency": "AUD",
      "exchangeRate": "1.57",
      "exchangeRateTimeStamp": "20251108 12:12"
    }
  }
}
```

Response for FDC Nashville Global

```
{
  "_links": {
    "self": {
      "href": "/pts/v2/refunds/4963014779006178301545",
      "method": "GET"
    },
    "void": {
      "href": "/pts/v2/refunds/4963014779006178301545/voids",
      "method": "POST"
    }
  },
  "id": "4963014779006178301545",
  "submitTimeUtc": "2017-06-01T071757Z",
  "status": "200",
  "reconciliationId": "39571012D3DFEKS0",
  "statusInformation": {
    "reason": "SUCCESS",
    "message": "Successful transaction."
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    }
  },
  "refundAmountDetails": {
    "currency": "USD",
    "refundAmount": "100.00"
  }
}
```

