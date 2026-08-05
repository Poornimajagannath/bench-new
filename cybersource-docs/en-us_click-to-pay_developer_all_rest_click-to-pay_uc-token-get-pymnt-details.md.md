Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the payment details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d14e1140}
-----------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1147}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1159}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
The `{jti}` is the ID of the JWT within the transient token that is returned by `Unified Checkout`. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.
