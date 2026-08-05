DCC Offer {#dcc-merchant-offer-post}
====================================

A DCC offer creates a new offer record in your system. Request the DCC Offer service to determine the eligibility of the transaction for DCC and to convert the price from the local payment currency to the DCC billing currency for eligible transactions.

Header Fields {#dcc-merchant-offer-post_section_b1w_5s1_5gc}
------------------------------------------------------------

DCC Offer calls require these header fields:

Authorization
:
{#dcc-merchant-offer-post_dl_lln_vqp_vgc}

keyId
:

Endpoint {#dcc-merchant-offer-post_section_rgf_pq1_5gc}
-------------------------------------------------------

**Test:** `POST `https://apitest.cybersource.com`/vas/v1/currencyconversion`  
**Production:** `POST `https://api.cybersource.com`/vas/v1/currencyconversion`

Required Fields for DCC Offer POST Request {#dcc-merchant-offer-post-request-api-req-fields}
============================================================================================

[orderInformation.amountDetails.originalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-orginal-amount.md "")
:

[orderInformation.amountDetails.originalCurrency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-original-currency.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

Optional Fields for DCC Offer POST Request {#dcc-merchant-offer-post-request-api-optional-fields}
=================================================================================================

[clientReferenceInformation.applicationName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-name.md "")
:

[clientReferenceInformation.applicationUser](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-user.md "")
:

[clientReferenceInformation.applicationVersion](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-application-version.md "")
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[clientReferenceInformation.partner.developerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-developer-id.md "")
:

[clientReferenceInformation.partner.solutionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-partner-solution-id.md "")
:

orderInformation.currencyConversion.type
:
This field is required when MCP is enabled.
:
Default value:

    * `DCC`: Dynamic Currency Conversion
    {#dcc-merchant-offer-post-request-api-optional-fields_ul_zyt_ycb_tgc}

[pointOfSaleInformation.entryMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-entry-mode.md "")
:
Possible values:

    * `KEYED`: may refer to MOTO on a terminal, MOTO on a virtual terminal, or eCommerce.
    * `SWIPED`
    * `CONTACT`
    * `CONTACTLESS`
    {#dcc-merchant-offer-post-request-api-optional-fields_ul_yzh_2bb_tgc}

[pointOfSaleInformation.terminalId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/pos-info-aa/pos-info-terminal-id.md "")
:

REST Example: DCC Offer POST {#dcc-merchant-offer-post-api-ex-rest}
===================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "REF-101-USD-909",
    "partner": {
      "developerId": "123456",
      "solutionId": "123456"
    },
    "applicationName": "REST API",
    "applicationVersion": "1.23.44",
    "applicationUser": "Bob"
  },
  "paymentInformation": {
    "card": {
      "number": "41111111111"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "originalAmount": "100.00",
      "originalCurrency": "USD"
    },
    "currencyConversion": {
      "type": "DCC"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "12345678",
    "entryMode": "CONTACT"
  }
}
```

Response

```
{
  "clientReferenceInformation": {
    "code": "REF-101-USD-909"
  },
  "id": "6843379070056369304008",
  "submitTimeUtc": "2023-05-17T22:47:57Z",
  "status": "PENDING",
  },
  "orderInformation": {
    "currencyConversion": {
      "type": "DCC",
      "reconciliationId": "ABC123",
      "offer": [
        {
          "originalAmount": "100.00",
          "originalCurrency": "USD",
          "amount": "157.00",
          "currency": "AUD",
          "exchangeRate": "1.57",
          "marginRate": "3.0",
          "rateSource": "Wholesale Exchange Rate",
          "exchangeRateTimeUtc": "2023-05-17T23:47:57Z",
          "exchangeRateExpirationTimeUtc": "2024-05-18T22:47:57Z",
          "exchangeRateInverted": true,
          "rateId": "009F303309AF07234520190628143445"
        }
      ],
      "disclaimer": "SAMPLE ONLY: I have been offered a choice of currencies and choose to pay in the selected currency above. Dynamic Currency Conversion (DCC) is provided by the &lt;MERCHANT&gt;."
    }
  }
}
```

