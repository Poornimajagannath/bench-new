DCC Capture {#dcc-merchant-capture}
===================================

A DCC capture request indicates an accepted order. This request is sent when a DCC transaction is successfully authorized.  
When processing a capture, apply the **same exchange rate** used at the time of payment authorization. Ensure the captured amount does **not exceed** the originally authorized amount.  
See the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "") for more information.

Required Fields for DCC Capture {#dcc-merchant-capture-request-api-req-fields}
==============================================================================

In addition to the normal fields required for a regular capture, these fields are required when DCC has been offered and the cardholder has chosen to pay in their billing currency.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.exchangeRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
:

[orderInformation.amountDetails. exchangeRateTimeStamp](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-time-stamp.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. foreignAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-foreign-amount.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. foreignCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-foreign-currency.md "")
:
Required for FDI Global transactions.

[orderInformation.amountDetails. originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:
Required for VPC transactions.

[orderInformation.amountDetails. originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:
Required for VPC transactions.

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

Example: DCC Capture {#dcc-merchant-api-ex-vpc-capture}
=======================================================

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
      "href": "/pts/v2/captures/7625576567396098504806/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/captures/7625576567396098504806"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7625576567396098504806",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "157.00",
      "currency": "AUD"
    }
  },
  "reconciliationId": "7625574701416008504806",
  "status": "PENDING",
  "submitTimeUtc": "2025-11-07T23:20:56Z"
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
    "void": {
      "method": "POST",
      "href": "/pts/v2/captures/7625562821436326504806/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/captures/7625562821436326504806"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7625562821436326504806",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "USD"
    }
  },
  "reconciliationId": "76706982",
  "status": "PENDING",
  "submitTimeUtc": "2025-11-07T22:58:02Z"
}
```

