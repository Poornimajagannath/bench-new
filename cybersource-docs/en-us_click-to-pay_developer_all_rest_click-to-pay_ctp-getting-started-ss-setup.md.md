Server-Side Set Up {#ctp-getting-started-ss-setup}
==================================================

This section contains the information you need to set up your server. Initializing `Click to Pay Drop-In UI` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how the `Click to Pay Drop-In UI` performs.  
The server-side component provides this information:

* A transaction-specific public key that is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and interaction methods.

{#ctp-getting-started-ss-setup_ul_atq_bwq_npb}  
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Capture Context Using the Sessions API {#ctp-capture-context-intro}
===================================================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the Sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The Sessions API request contains parameters that define how `Unified Checkout` performs.  
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.  
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types. The capture context request includes these elements:
* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigin
  Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context.  
  When you configure the merchant settings using the Merchant Experience section of the `Business Center`, your request to the `sessions` API must include these required fields. All other values are determined from the settings that are configured in the `Business Center`:

```
{
  "targetOrigins": ["https://merchant.com", "https://reseller.com:8443"],
  "locale": "en_US",
  "country": "US",
    "data": {
        "orderInformation": {
          "amountDetails": {
            "totalAmount": "21.00",
            "currency": "USD"
      }
    }
  }
}
```

{#ctp-capture-context-intro_codeblock_kxt_pcj_2jc}  
When you use only the sessions API to generate the capture context, your request must include these required fields:

```
{
  "targetOrigins": [
    "https://yourCheckoutPage.com"
  ],
  "allowedCardNetworks": [
    "VISA",
    "MASTERCARD",
    "AMEX"
  ],
  "allowedPaymentTypes": [
    "CLICKTOPAY"
  ],
  "country": "US",
  "locale": "en_US",
  "captureMandate": {
    "billingType": "FULL",
    "requestEmail": true,
    "requestPhone": true,
    "requestShipping": true,
    "shipToCountries": [
      "US",
      "GB"
    ],
    "showAcceptedNetworkIcons": true
  },
  "data": {
    "orderInformation": {
      "amountDetails": {
        "totalAmount": "21.00",
        "currency": "USD"
      }
    }
  }
}
```

{#ctp-capture-context-intro_codeblock_nfk_rcj_2jc}  
For information about requesting the capture context using the `sessions` API, see the [API Reference](https://developer.cybersource.com/api-reference-assets/index.md#unified-checkout "") in the `Cybersource` Developer Center. For more information on requesting the capture context, see [Sessions API - Capture Context](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context.md "").
