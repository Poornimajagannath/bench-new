Payment Credentials API {#uc-token-get-pymnt-credentials}
=========================================================

This section contains the information you need to retrieve the full payment credentials collected by the `Unified Checkout` tool using the payment credentials API. The payment information is returned in a redundantly signed and encrypted payment object. It uses the JSON Web Tokens (JWTs) as the data standard for communicating this sensitive data.

> IMPORTANT
> Payment information returned by the ` payment-credentials ` endpoint will contain Personal Identifiable Information (PII). Retrieving this sensitive information requires your system to comply with PCI security standards. For more information on PCI security standards, see: <https://www.pcisecuritystandards.org/>  
> The response is returned using a JWE data object that is encrypted with your public key created during the `Unified Checkout` tool's integration. For more information, see [Upload Your Encryption Key](/docs/gateway/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-upload-encrypt-key-intro.md "").  
> To decrypt the JWE response, use your private key created during the `Unified Checkout` tool's integration. The decrypted content is a JWS data object containing a JSON payload. This payload can be validated with the `Unified Checkout` public signature key.  
> IMPORTANT  
> ` Payment Gateway ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Payment Gateway ` APIs. ` Payment Gateway ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Payment Gateway ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Returned Credentials
--------------------

A payment account number (PAN) or network token is returned on your request depending on your payment method and `Click to Pay` account status:

|     `Click to Pay` Account Status      | American Express |  Mastercard   |     Relay      |
|----------------------------------------|------------------|---------------|---------------|
| New card not saved in `Click to Pay`   | PAN              | PAN           | PAN           |
| New card saved in `Click to Pay`       | PAN              | Network Token | Network Token |
| Existing card stored in `Click to Pay` | PAN              | Network Token | Network Token |
[Payment Credentials Returned by Card Type and `Click to Pay` Account Status]

When you retrieve PAN information from the Payment Credentials API, the response includes the PAN, card expiration date, and the card verification value (CVV). When you retrieve network token information, the response includes the network token and network token cryptogram.

> IMPORTANT Relay and Mastercard always attempt to provision a network token. When a network token is not provisioned, the default payment method is the PAN. When there is a PAN transaction, the PAN is not stored in the consumers wallet and it is treated as a single transaction.
> Network tokens are generated in the wallet of the `Click to Pay` token requestor ID (TRID). When tokenization is successful, Relay attempts to complete authentication during the `Click to Pay` experience. For information on authentication, see [Click to Pay Customer Authentication](/docs/gateway/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-authentication.md "").  
> You must meet these requirements for tokenization to be successfully configured for your merchant ID (MID):

* `Click to Pay` is enabled as a digital payment in the `Business Center`.
* The transacting MID is configured for tokenization with `Click to Pay`. Contact your Implementation Consultant or Technical Account Manager to configure tokenization with `Click to Pay`.
* The allowedPaymentTypes field value is set to `CLICKTOPAY` in the capture context. For information on the capture context, see [Capture Context API](/docs/gateway/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context.md "").

Endpoint {#uc-token-get-pymnt-credentials_d14e634}
--------------------------------------------------

**Production:** `GET ``https://api.example.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d14e641}  
**Test:** `GET ``https://apitest.example.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d14e653}  
**Production in Saudi Arabia:** `GET ``https://api.sa.example.com``/flex/v2/payment-credentials/`*{ReferenceID}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.example.com``/flex/v2/payment-credentials/`*{ReferenceID}*  
The *{ReferenceID}* is the reference ID returned in the `id` field when you created the payment credentials.
