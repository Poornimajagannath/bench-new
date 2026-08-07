DCC Authorization {#dcc-merchant-authorization}
===============================================

A DCC authorization authorizes the amount for the transaction. The payment response includes the status of the request. It also includes processor-specific information when the request is successful, and error information when the request is unsuccessful.  
See the [Payments Developer Guide](https://developer.example.com/docs/gateway/en-us/payments/developer/ctv/rest/payments/payments-intro.md "") for more information.

Required Fields for DCC Authorization {#dcc-merchant-auth-api-req-fields}
=========================================================================

In addition to the normal fields required for a regular authorization, these fields are required when DCC has been offered and the cardholder has chosen to pay in their billing currency.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

orderInformation.amountDetails. currencyConversion.indicator
:
Set this field to `1` when cardholders opt to use DCC.

[orderInformation.amountDetails.exchangeRate](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-a.md "")
:

[orderInformation.amountDetails.exchangeRateTimeStamp](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-exchange-rate-time-stamp.md "")
:

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

Example: DCC Authorization {#dcc-merchant-api-ex-vpc-auth}
==========================================================

Request for `Platform Connect`

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "157.00",
      "currency": "AUD",
      "exchangeRate": "1.57",
      "exchangeRateTimeStamp": "20251108121232",
      "originalAmount": "100.00",
      "originalCurrency": "USD",
      "currencyConversion": {
        "indicator": "1",
        "reconciliationId": "ABC123",
        "id": "6843379070056369304008"
      }
    }
  },
  "billTo": {
    "firstName": "John",
    "lastName": "Doe",
    "address1": "1 Market St",
    "locality": "San Francisco",
    "administrativeArea": "CA",
    "postalCode": "94105",
    "country": "US",
    "email": "test@pgw.com",
    "phoneNumber": "4158880000"
  }
}
```

Response for `Platform Connect`

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7625574701416008504806/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7625574701416008504806"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7625574701416008504806/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7625574701416008504806",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "157.00",
      "currency": "AUD"
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
    "systemTraceAuditNumber": "866090",
    "merchantNumber": "123456789",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "531123866090",
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
  "reconciliationId": "7625574701416008504806",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-11-07T23:17:50Z"
}
```

Request for `FDC Nashville Global`

```
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "USD",
      "foreignAmount": "157.00",
      "foreignCurrency": "AUD",
      "exchangeRate": "1.57",
      "exchangeRateTimeStamp": "20251108 12:12",
      "currencyConversion": {
        "indicator": "1"
      }
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@pgw.com",
      "phoneNumber": "4158880000"
    }
  }
}
```

Response for `FDC Nashville Global`

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7625543558656491904805/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7625543558656491904805"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7625543558656491904805/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "id": "7625543558656491904805",
  "issuerInformation": {
    "responseRaw": "0110322000000E10000200000000000001570011072225553898395333383745484F43544357433833313030303030000159004400223134573031363135303730333830323039344730363400103232415050524F56414C0006564943524320"
  },
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "100.00",
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
    "terminalId": "01411543"
  },
  "processorInformation": {
    "merchantNumber": "000846649116882",
    "approvalCode": "831000",
    "networkTransactionId": "016150703802094",
    "transactionId": "016150703802094",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "S387EHOCTCWC",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-11-07T22:25:55Z"
}
```

