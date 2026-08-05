Server-Side Set Up {#uc-getting-started-ss-setup}
=================================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the Sessions API. This step authenticates your merchant credentials, and establishes how the `Unified Checkout` frontend components will function. The Sessions API request contains parameters that define how `Unified Checkout` performs.  
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

{#uc-getting-started-ss-setup_ul_atq_bwq_npb}  
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").

Capture Context {#uc-capture-context-intro}
===========================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the Sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The Sessions API request contains parameters that define how `Unified Checkout` performs.  
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.  
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types.

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Safari 16
* Firefox 121
* Google Chrome/Chium-based browsers 118
* Microsoft Edge 118

Capture Context Example {#uc-capture-context-intro_uc-capture-context-codeblock}
--------------------------------------------------------------------------------

Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context. Use the completeMandate to orchestrate follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `TMS`. The data that is included in the capture context are configured in the merchant experience. For information about how to configure these fields, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "") [Configure Customer Data and Payment Flow](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-customer-data.md ""). For information about what fields can be overridden by what is included in the capture context, see [Capture Context Fields in the Business Center](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-ebc-api-info.md "").  
This example shows a capture context with the minimum required fields:

```
{
  "targetOrigins": ["https://merchant.com", "https://reseller.com:8443"],
  "locale": "en_US",
  "country": "US",
  "data": {
	"orderInformation": {
    	"amountDetails": {
      	"totalAmount": "21.00",
      	"currency":  "USD"
          }
      }
  }
}
```

Card Entry Form {#uc-capture-context-intro_uc-capture-context-diagram}
----------------------------------------------------------------------

This diagram shows how elements of the capture context request appear in the card entry form.

#### Figure:

Anatomy of a Manual Card Entry Form ![Image of the capture context request code and how it appears in the
entry form elements.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/anatomy-of-manual-card-entry-form-685x575.svg/jcr:content/renditions/original)

Versioning {#uc_versioning}
===========================

`Unified Checkout` uses [Semantic Versioning](http://semver.org/spec/v2.0.0.md "") (SemVer). Version numbers use the `MAJOR.MINOR.PATCH` format:

* **MAJOR**: breaking changes that require code modifications
* **MINOR**: new features that are backwards compatible
* **PATCH**: bug fixes and improvements that are backwards compatible  
  The server controls which SDK version is loaded for each session that you request. When your server creates a session, the response JWT includes a clientLibrary field that contains the full URL to the correct version of the SDK. Your server parses the JWT, extracts the URL, and passes it to the frontend to load dynamically.

> IMPORTANT
> The ` clientVersion ` field in the session request is optional. When you do not include this field, the server automatically resolves the appropriate version for every session. This ensures that the client-side library and server-side features are compatible.` Cybersource ` recommends that you do not include the ` clientVersion ` field in your request and that you use the most recent version. When you do this, your integration benefits from new features, payment methods, and improvements and there are no code changes required.

Pin to a Version
----------------

If you must set your integration to a specific version, you can set the `clientVersion` field to a `MAJOR` version such as `1`, or a `MAJOR.MINOR` version such as `1.2`. The server uses the latest compatible patch release within that range. This ensures that you continue to receive security fixes and bug fixes.

> IMPORTANT
> You cannot pin to a specific patch version (` MAJOR.MINOR.PATCH `). This ensures that all integrations receive critical patches. ` Cybersource ` recommends omitting clientVersion from your request unless you have a specific need for pinned behavior.  
> For information about the latest releases, see [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").

Client Version History {#uc-capture-context-versions}
=====================================================

Below is a list of client versions and the features that are included in each version.

> IMPORTANT
> ` Cybersource ` recommends that you use the most recent client version in your integration.

0.23
:
Accepts these card networks in the allowedCardNetworks field for manual card entry:

    * Carnet
    * Cartes Bancaires
    * China UnionPay with card verification value (CVV)
    * EFTPOS
    * ELO
    * JCrew PLCC
    * mada
    * Meeza

:
Ordering controls for the allowedPaymentTypes button.
:
De-coupling of PANENTRY from other payment types in the allowedPaymentTypes field.

0.24
:
Support for enabling combo cards in the capture context.
:
Support for eight-digit BINs.
:
Support for enabling card save in the capture context.

0.25
:
Addition of **Skip Verification next time** in the `Click to Pay` payment flow.
:
Support for CPF in the capture context.

0.26
:
Support for auto-lookup in `Click to Pay` when an email is included in the capture context.
:
Inclusion of the cardDetails field object in the transient token response.
:
Support for the cardholderAuthenticationStatus field object in the transient token response.
:
Support for the complete mandate.

0.28
:
Complete mandate enhancement to support `Payer Authentication` for manual card entry for Visa, Mastercard, American Express, Discover, JCB, Cartes Bancaires, China UnionPay, and ELO card brands.
:
Support for Afterpay as an allowedPaymentType.
:
Support for PayPak as an allowedCardNetwork.
:
Auto-enrollment for `Click to Pay` in supported markets.
:
Removal of the confirm or continue screen for specific use cases.
:
Static button for `Click to Pay` flows.

0.30
:
Support for iDeal, Multibanco, and Przelewy24\|P24.
:
Complete mandate enhancement to support `Payer Authentication` for Google Pay and `Click to Pay`.
:
Support for Pakistan locales (en_PK and ur_PK).
:
New look and feel of `Unified Checkout` in line with EMVCO best practices.

0.31
:
Addition of the data object of the orderInformation field object and pass-through fields.
:
Support for tokenCreate in the complete mandate.
:
Support of pass-through fields, including challenge codes and data only, for `Payer Authentication`.
:
Support for Jaywan as an allowedCardNetwork.
:
Updated the payment details response to return detected card types. Multiple card types are shown when more than one card type is detected.
:
Support for Bancontact, Dragonpay, MyBank, and Tink Pay By Bank.

0.32
:
Support for KCP and UATP in the allowedCardNetwork field.
:
Support for Konbini as a post-pay reference payment method.
:
A radio button in the UI for Cartes Bancaires dual-branded cards.

0.33
:
Support for mobile as identity for `Click to Pay` accounts.
:
Japanese language translation updates.
:
UX captures billing and shipping information when they are not included in the capture context.

0.34
:
Iframes are used instead of pop-ups to reduce pop-up blocking and streamlining mobile deployment.
:
Additional BIN range for Jaywan card types.

0.35
:
Look and feel customization.

1.0
:
Configure payment options.
:
Configure customer data and payment flow.
