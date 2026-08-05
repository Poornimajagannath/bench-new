Sessions API - Capture Context {#ctp-setup-capture-context}
===========================================================

This section contains the information you need to request the capture context using the `sessions` API. The capture context request contains all of the merchant-specific parameters that tell the frontend JavaScript library how to behave within your payment experience.  
The capture context is a signed JSON Web Token (JWT) containing this information:

* Merchant-specific parameters that dictate the customer payment experience for the current payment transaction.
* A one-time public key that secures the information flow during the current payment transaction.

The capture context request includes these elements:

* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigins  
  For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Target Origin
:
The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain) and port number (if used).

    You must use the https:// protocol. Sub domains must also be included in the target origin.

    Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.

    For example, if you are launching `Click to Pay` on example.com, the target origin could be any of the following:

    * [https://example.com](https://example.com/ "")
    * [https://subdomain.example.com](https://subdomain.example.com/ "")
    * [https://example.com:8080](https://example.com:8080/ "")

:
You can supply up to seven origins within the targetOrigins field for nested iframes. To do this, you must do the following:

    * Compare the list of origins in the `v1/sessions` targetOrigins field against the location.ancestorOrigins of the browser.
    * Ensure that the count of origins and their content matches in the targetOrigins field against the location.ancestorOrigins of the browser. If any origins are missing or mismatched, the system prevents `Unified Checkout` from loading and displays a client-side error message.
    {#ctp-setup-capture-context_ul_ijc_2tj_2jc}

    You must::

Allowed Card Networks
:
Use the allowedCardNetworks field to define the card types. `Click to Pay` supports American Express, Mastercard, and Visa. The `Click to Pay Drop-In UI` manually captures the other card types that are listed in the capture context request. This enables you to process the payment through the chosen gateway but the cardholder is not able to enroll these cards in `Click to Pay`.

    These card networks are available for card entry:

    * American Express
    * Carnet
    * Cartes Bancaires
    * China UnionPay
    * Diners Club
    * Discover
    * EFTPOS
    * ELO
    * Jaywan
    * JCB
    * KCP
    * mada
    * Maestro
    * Mastercard
    * Meeza
    * PayPak
    * UATP
    * Visa

    To support dual-branded or co-badged cards, you must list your supported card types values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Visa and EFTPOS and EFTPOS is listed first, the card type is set to EFTPOS after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-tokens-intro/ctp-dual-co-brand-card-support.md "").

    When a Cartes Bancaires dual-branded card is entered in the `Click to Pay Drop-In UI`, the `Click to Pay Drop-In UI` provides a radio selector button to enable the cardholder to select which scheme they want to use to process the payment. The radio selector defaults to the card scheme that appears first in the allowedCardNetworks field.

    Cartes Bancaires is not supported for `Click to Pay`. If a cardholder selects to process a payment with Cartes Bancaires it is processed as a one-time guest checkout and the user is not enrolled in `Click to Pay`. If a cardholder chooses to process with Visa or Mastercard instead of Cartest Bancaires, they are given the option to enroll their card in `Click to Pay`.

:
> IMPORTANT
> Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). If you include only card types that do not have security codes in the allowedCardNetworks field, ` Unified Checkout ` does not display the security code field in the UI.  
> If you include card types that do not have security codes and cards types that do have security codes in the allowedCardNetworks field, ` Unified Checkout ` displays the security code field in the UI. The field is disabled in the UI when the cardholder enters a card number for a card type with no security code.

Include Card Prefix
:
You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

    * 6 digits
    * 8 digits
    * no prefix at all


    > IMPORTANT
    > When you request the card number prefix for a ` Click to Pay ` tokenized credential, 6 digits are returned. ` Click to Pay ` does not return 8 digits.
    To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.

:
**If you want to receive a 6-digit card number prefix in the response**

    * Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.
    * This example shows how a 6-digit card number prefix `411111` is returned in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111”,
                          "bin" : "411111"
      ```

:
**If you want to receive an 8-digit card number prefix in the response**

    * Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `true`. IMPORTANT
      > Per PCI DSS requirements, this requirement applies only to card numbers longer than 15 digits and for Discover, JCB, Mastercard, UnionPay, and Visa brands.
      > * If the card type entered is not part of these brands, a 6-digit card number prefix is returned instead.
      > * If the card type entered is not part of these brands but is *co-branded* with these brands, an 8-digit card number prefix is returned.
    * This example shows how an 8-digit card prefix `41111102` is returned in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111”,
                          "prefix" : "41111102"
      ```

:
**If you do not want to receive a card number prefix in the response**

    * Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `false`.
    * This example shows how a card number is returned without a card number prefix in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111"
      ```

:
**Best practice:** If your application does not require card number prefix information for routing or identification purposes, `Cybersource` recommends that you include the transientTokenResponseOptions.includeCardPrefix field in the capture context request and set its value to `false`. Doing so limits the exposure of payment data to only what is necessary for your processing needs.  
For more information about PCI DSS, see [Frequently Asked Questions](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers "") on the PCI Security Standards Council site.

Allowed Payment Types
:
You can specify the type of `Unified Checkout` digital payment methods that you want to accept in the capture context.
:
Use the allowedPaymentTypes field to define the payment type. The `Click to Pay Drop-In UI` accepts these payment types:

    * `CLICKTOPAY`
    * `PANENTRY`


    > IMPORTANT
    > When you include ` CLICKTOPAY `, it supports both ` Click to Pay ` and ` PANENTRY ` in the UI.

> IMPORTANT
> When integrating with ` Cybersource ` APIs, ` Cybersource ` insists that you dynamically parse the response for the fields that you are looking for. Additional fields may be added in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. While the underlying data structures will not change, you must also ensure that your integration can handle changes to the order in which the data is returned.

