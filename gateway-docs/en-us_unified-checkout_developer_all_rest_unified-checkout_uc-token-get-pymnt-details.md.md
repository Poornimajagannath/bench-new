Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the Payment Details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT  
> ` Payment Gateway ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Payment Gateway ` APIs. ` Payment Gateway ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Payment Gateway ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d8e1140}
----------------------------------------------

**Production:** `GET ``https://api.example.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d8e1147}  
**Test:** `GET ``https://apitest.example.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d8e1159}  
**Production in Saudi Arabia:** `GET ``https://api.sa.example.com``/flex/v2/payment-details/`*{jti}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.example.com``/flex/v2/payment-details/`*{jti}*  
The `{jti}` is the ID of the JWT within the transient token that is returned by `Unified Checkout`. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

REST Example: Retrieving Transient Token Payment Details {#uc-token-get-pymnt-details-ex-rest}
==============================================================================================

Request

```keyword
GET https://apitest.example.com/flex/v2/payment-details/{jti}
```

{#uc-token-get-pymnt-details-ex-rest_codeblock_c51_vmt_gwb}  
Response to Successful Request

```
{
  "paymentInformation": {
    "card": {
      "expirationYear": "2026",
      "number": "XXXXXXXXXXXX1111",
      "expirationMonth": "05",
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "21.00",
      "currency": "USD"
    },
    "billTo": {
      "lastName": "Lee",
      "country": "US",
      "firstName": "Tanya",
      "email": "tanyalee@example.com"
    },
    "shipTo": {
      "locality": "Small Town",
      "country": "US",
      "administrativeArea": "CA",
      "address1": "123 Main Street",
      "postalCode": "98765"
    }
  }
}
```

