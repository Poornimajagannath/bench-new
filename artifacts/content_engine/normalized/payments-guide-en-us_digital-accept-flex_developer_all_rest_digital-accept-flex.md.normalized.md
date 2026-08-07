`Digital Accept` Secure Integration Developer Guide {#da-about-guide}
=====================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This document is written for merchants who want to enable `Digital Accept` digital payment methods on their e-commerce page.

Conventions
:
This special statement is used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional processor-specific versions of this guide and additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.visaacceptance.com>

Recent Revisions to This Document {#uc-doc-revisions}
=====================================================

25.12.01
--------

`Microform Integration`
:
Added the `.flex-microform-incomplete` class. See [Styling](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-next-steps/styling-v2.md "").
:
Updated the default aria-label property value to `true`. See [Class: Microform](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md "").
:
Added `incomplete` as a CSS property. See [Global](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/global-v2.md "").
:
Added information about Web Content Accessibility Guidelines (WCAG) 2.2 compliance. See [WCAG 2.2 Compliance](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/wcag-compliance-v2.md "").
:
Updated the client-side setup code examples for accepting eCheck information. See [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "").

`Unified Checkout`
:
Added information about supported browsers. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").
:
Added support for clientVersion `0.34`. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-capture-context-versions.md "").
:
Added information about Cartes Bancaires dual-branded cards. See [Dual-Branded Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-tokens-intro/dual-co-brand-card-support.md "").
:
Added information about Konbini. See [Konbini](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-ppr/uc-pay-methods-ppr-konbini.md "").

Click to Pay Drop-In UI
:
Added support for clientVersion `0.34`. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context/ctp-capture-context-versions.md "").
:
Added information about supported browsers. See [Introduction to the Click to Pay Drop-In UI](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro.md "").
:
Removed reference to the complete mandate from JavaScript Examples. See [JavaScript Example: Setting Up with Full Sidebar](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-cs-setup-intro/ctp-getting-started-button-widget-intro/ctp-getting-started-button-widget-sidebar.md "") and [JavaScript Example: Setting Up with the Embedded Component](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-cs-setup-intro/ctp-getting-started-button-widget-intro/ctp-getting-started-button-widget-embedded.md "").
:
Added support for the removal of the confirm and continue screen and mobile as identity for `Click to Pay`. See [Features](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context/ctp-capture-context-features.md "").
:
Added the JavaScript API reference. See [JavaScript API Reference](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-appendix-js-reference.md "").
:
Updated the steps for configuration customer authentication for Visa `Click to Pay`. See [Click to Pay Customer Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/ctp-authentication.md "").
:
Updated the test cards for testing authentication. See [Test Payment Details](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-testing-intro/ctp-reference-test-cards.md "").

25.11.02
--------

`Unified Checkout`
:
Added a complete capture context request example with all possible fields. See [Example: Unified Checkout Complete Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-uc-examples/uc-appendix-complete-cc-ex.md "").
:
Updated the capture context examples for clientVersion `0.31`. See these topics:

    * [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "")
    * [Requesting the Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-setup-capture-context-intro.md "")
    * [Unified Checkout Integration Examples](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-uc-examples.md "")

:
Added information about available capture context fields. See [Unified Checkout Field Reference](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-pass-through-fields.md "").
:
Added information about testing your authentication method. See [Test Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-authentication.md "").
:
Added information about customizing the `Click to Pay` UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-ui-ux.md "").

25.11.01
--------

`Unified Checkout`
:
Updated the list of allowed card networks. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").
:
Added support for clientVersion `0.31`. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-capture-context-versions.md "").
:
Added information about Bancontact, Dragonpay and MyBank. See these topics:

    * [Bancontact](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-bancontact.md "")
    * [DragonPay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-dragonpay.md "")
    * [MyBank](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-mybank.md "")

25.10.02
--------

`Unified Checkout`
:
Added support for clientVersion `0.30`. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-capture-context-versions.md "").

Click to Pay Drop-In UI
:
Added support for clientVersion `0.30`. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context/ctp-capture-context-versions.md "").

25.10.01
--------

`Unified Checkout`
:
Added properties to [Class: AcceptError](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix-js-reference/uc-appendix-js-class-accept-error.md "").
:
Added missing reason codes. See [Reason Codes](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-reason-codes.md "").
:
Updated the clientVersion field value to `0.30` in examples.
:
Added Pakistan locales. See [Supported Locales](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-languages.md "").
:
Added information about handling responses for Online Bank Transfers and Buy Now, Pay Later. See [Handle Responses](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-handle-response.md "") and [Handle Responses](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-bnpl/uc-pay-methods-bnpl-handle-response.md "").

Click to Pay Drop-In UI
:
Updated the clientVersion field value to `0.30` in examples.

25.08.02
--------

`Flex API` v2
:
Added more information about JSON Web Tokens. See [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2-jwts.md "").

`Microform Integration`
:
Added more information about JSON Web Tokens. See [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

`Unified Checkout`
:
Added more information about JSON Web Tokens. See [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

`Click to Pay Drop-In UI`
:
Added more information about JSON Web Tokens. See [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

25.08.01
--------

`Unified Checkout`
:
Added support for different payment methods. See [Payment Methods](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro.md "").
:
Added support for creating a trigger. See [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").
:
Added PayPak as a supported payment method. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").
:
Added support for client version 0.28. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-capture-context-versions.md "").

`Microform Integration`
:
Added PayPak as a supported payment method. See [Creating the Server-Side Capture Context for Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/creating-server-side-context-v2-card.md "")and [Creating the Server-Side Capture Context for Checks](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-ss-setup/creating-server-side-context-v2-bank.md "").

25.06.01
--------

`Microform Integration`
:
Added more information about the transient token time limit. See these topics:

    * [Transient Token Time Limit for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-time-limit-pay-card.md "")
    * [Using the Transient Token to Process a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/using-transient-token-pay-card.md "")
    * [Transient Token Time Limit for Accepting eCheck Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-time-limit-pay-bank.md "")

`Flex API` v2
:
Added more information about the transient token time limit. See these topics:

    * [Tokenizing Payment Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-tokenize-payment-info.md "")
    * [Validate the Transient Token](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-validate-token.md "")
    * [Using the Transient Token to Process a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-payment.md "")

25.05.01
--------

This revision contains only editorial changes and no technical updates.

25.04.02
--------

`Unified Checkout`
:
Added a client version history and the features included in each version. See [Client Version History](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-capture-context-versions.md "").

    Added information on the available features and the fields specific to each feature to the Capture Context API. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "")

`Microform Integration`
:
Added more information on nested iframes in the capture context. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/micro-capture-context-card-intro.md "").

`Click to Pay Drop-In UI`
:
Added more information on nested iframes in the capture context. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-ss-setup/ctp-capture-context-intro.md "").

25.04.01
--------

`Unified Checkout`
:
Added more information on nested iframes in the capture context. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").

`Microform Integration`
:
Added more information on nested iframes in the capture context. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/micro-capture-context-card-intro.md "").

`Click to Pay Drop-In UI`
:
Added more information on nested iframes in the capture context. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-ss-setup/ctp-capture-context-intro.md "").

25.03.01
--------

`Microform Integration` v2
:
Added information about choosing your preferred card number prefix length and supported scenarios. See the Include Card Prefix sections of these topics:

    * [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/micro-capture-context-card-intro.md "") (server-side set up for the capture context)
    * [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-capture-context-api-intro.md "") (requesting the capture context using the capture context API)

:
Updated the description of Transient Token Time Limit for accepting card information and for accepting `eCheck` information. See these topics:

    * [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-time-limit-pay-card.md "") (server-side set up for accepting card information)
    * [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-time-limit-pay-bank.md "") (server-side set up for accepting eCheck information)

:
Replaced the term *check information* with *`eCheck` information* throughout the section [Microform Integration v2](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2.md "").
:
Updated code examples for accepting card information with `Microform Integration`:

    * Example Code for Loading the Script Dynamically Following JWT Extraction Tags, in [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-cs-setup.md "")
    * Example: Creating the Pay Button with Event Listener for Accepting Card Information, in [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-time-limit-pay-card.md "")

:
Updated code examples for accepting `eCheck` information with `Microform Integration`:

    * Example Code for Loading the Script Dynamically Following JWT Extraction Tags, in [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "")
    * Example: Creating the Pay Button with Event Listener for Accepting `eCheck` Information, in [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-time-limit-pay-bank.md "")

`Unified Checkout`
:
Added information about choosing your preferred card number prefix length and supported scenarios. See the Include Card Prefix sections of these topics:

    * [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "") (server-side set up for the capture context)
    * [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "") (requesting the capture context using the capture context API)

:
Replaced *check* digital payment method with *`eCheck`* digital payment method throughout [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").
:
Corrected the example code in [REST Example: Requesting the Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context/uc-setup-capture-context-intro/uc-setup-capture-context-example.md "").
:
Added information on using customer authentication with Click to Pay for Visa transactions. See [Click to Pay Customer Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication.md "").

`Click to Pay Drop-In UI`
:
Added information about choosing your preferred card number prefix length and supported scenarios. See the Include Card Prefix sections of these topics:

    * [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-ss-setup/ctp-capture-context-intro.md "") (server-side set up for the capture context)
    * [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "") (requesting the capture context using the capture context API)

25.01.02
--------

`Unified Checkout`
:
Added optional set-up parameters to control the types of credentials that Google Pay on `Unified Checkout` receives from Google. See [Managing Google Pay Authentication Types](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-googlepay-manage-authenticat.md "").
:
Added test card numbers. See [Test Your Unified Checkout Configuration](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-reference-test-cards.md "").

`Microform Integration`
:
Added test card numbers. See [Test Card Numbers for `Microform Integration`](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/da-reference-test-cards.md "").

25.01.01
--------

`Microform Integration`
:
Updated the JWT examples for encrypting the accept card information capture context. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-capture-context-api-intro.md "").
:
Updated the JWT examples for validating server-side capture contexts for accepting card and `eCheck` information. See these topics:

    * [Validating the Server-Side Capture Context for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/validate-capture-context-microv2-card.md "")
    * [Validating the Server-Side Capture Context for Accepting `eCheck` Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-ss-setup/validate-capture-context-microv2-bank.md "")

:
Clarified the first step for creating the server-side capture context and updated encrypted JWT examples. See these topics:

    * [Creating the Server-Side Capture Context for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/creating-server-side-context-v2-card.md "")
    * [Creating the Server-Side Capture Context for Accepting `eCheck` Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-ss-setup/creating-server-side-context-v2-bank.md "")

:
Updated the steps for client-side setup. See these topics:

    * [Client-Side Setup for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-cs-setup.md "")
    * [Client-Side Setup for Accepting `eCheck` Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "")

:
Updated the card detection event example. See [Events](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-next-steps/events-v2.md "").
:
Removed the Node.js REST code snippet. See [Getting Started Examples](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-getting-started-examples-v2.md "").
:
Updated the Class: Microform examples and added the aria-label and aria-required properties. See [Class: Microform](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md "").

`Unified Checkout`
:
Added steps for enrolling in Apple Pay. See [Preparing a Device for Testing Apple Pay on Unified Checkout](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-applepay-prep-test-device.md "").

    Updated the Important note about China UnionPay cards that do not have CVNs. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").

24.12.02
--------

`Microform Integration`
:
Added capture context requests for accepting card and `eCheck` information. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-capture-context-api-intro.md "").

24.12.01
--------

`Microform Integration`
:
Added information about dual-branded card support. See the *Support for Dual-Branded Cards* section in [Events](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-next-steps/events-v2.md "").
:
Added support for accepting `eCheck` information. See [Accept eCheck Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank.md "").
:
Added information on the clientLibrary and clientLibraryIntegrity field and values. See [Client-Side Setup for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-cs-setup.md "") and [Client-Side Setup for Accepting `eCheck` Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "").

`Unified Checkout`
:
Updated the capture context request sections to include the most recent client version and allowed payment types. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "") and [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

`Click to Pay Drop-In UI`
:
Updated the capture context request sections to include the most recent client version and allowed payment types. See [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-ss-setup/ctp-capture-context-intro.md "") and [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "").

24.11.01
--------

`Microform Integration`
:
Added information on server-side setup and the capture context. See [Server-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup.md "") and [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/micro-capture-context-card-intro.md "").
:
Added `Microform Integration` workflows. See [Microform Integration v2](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2.md "") and [Getting Started](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-getting-started-v2.md "").

`Unified Checkout`
:
Added information about China UnionPay cards that do not have a card verification number (CVN) and expiration date. See the Important note in [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").

24.09.01
--------

`Microform Integration`
:
Removed information about Microform version numbering.
:
Updated supported browser versions. See [Microform Integration v2](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2.md "").
:
Updated the clientVersion field value to `v2`. See [Creating the Server-Side Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/creating-server-side-context-v2-card.md "").
:
Updated the supported event types. See [Class: Field](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/Class--Field-v2.md "").

`Unified Checkout`
:
Added a note about transient token expiration. See [Authorizations with a Transient Token](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-auth-tokens.md "").

24.08.01
--------

This revision contains only editorial changes and no technical updates.

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Visa Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Visa Platform Connect ACQUIRER.

Introducing `Digital Accept` Secure Integration Product Suite {#payments_intro_digt_accpt_sec_intg}
===================================================================================================

The Secure Integration Product Suite allows you to simplify the acceptance of sensitive customer payment information. When a customer enters their payment details on your webpage, app, or elsewhere, it is replaced with a transient token. Tokenization ensures that the card data can be transported securely, which limits your exposure and significantly reduces your Payment Card Industry Data Security Standard (PCI DSS) compliance burden.
The Secure Integration Product Suite consists of three products that can be used in a variety of scenarios: `Unified Checkout`, `Microform Integration`, and `Flex API`.

`Unified Checkout`
------------------

`Unified Checkout` is a pre-configured drop-in UI for accepting online payments. It supports multiple payment methods including traditional cards and digital wallets such as Google Pay and Visa Click to Pay. Because it is pre-configured with digital payment support, `Unified Checkout` enables you to go live faster and substantially reduce the development burden of accepting a multitude of payment options. This solution is ideal for sellers looking for a complete payment acceptance technology with support for multiple payment methods.

#### Figure: {#payments_intro_digt_accpt_sec_intg_uc-ui-ux}

`Unified Checkout` Button Widget Interface ![Example of the button widget interface with various payment options and
callouts for features.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/digital-accept/images/uc-ui-ux.png/jcr:content/renditions/original)
`Unified Checkout` includes these features:

* Leading security technology
* Simple front-end integration
* Integrated with emerging digital standards
* Integrated with a range of payment methods
* Payment option presentation is optimized
  For more information, see [Introduction to Unified Checkout](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro.md "").

`Microform Integration`
-----------------------

`Microform Integration` is a payment card and card verification acceptance solution that can be embedded. Use it to securely accept payment information at your web page and have complete control over the look and feel of your payment form. `Microform Integration` captures the card number and card verification number fields from within your existing user interface. This solution is for sellers looking for a secure way to capture sensitive payment data from within their own customized payment form.

#### Figure: {#payments_intro_digt_accpt_sec_intg_microform-ui}

`Microform Integration` Payment Form Interface ![Example of the Microform payment form Interface with callout that states
secure Microform fields can be seamlessly inserted into your payment
page.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/digital-accept/images/microform-ui.png/jcr:content/renditions/original)
`Microform Integration` includes these features:

* Leading security technology
* Seamlessly integrated into existing payment pages
* Fully customizable

For more information, see [Microform Integration v2](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2.md "").

`Flex API`
----------

`Flex API` can be used to securely capture and transport payment data between systems. This solution is ideal for Internet of Things (IoT) and third-party integrations. For more information, see [Flex API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/da-flex-api-intro.md "").

`Digital Accept` Product Comparison
-----------------------------------

This chart compares `Digital Accept` products and features.

#### Figure: {#payments_intro_digt_accpt_sec_intg_da-prod-chart}

Products and Features Comparison Chart ![Comparison chart of Digital Accept products and features.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/digital-accept/images/da-prod-chart.png/jcr:content/renditions/original)

`Flex API` v2 {#flex-api-2_FlexAPI}
===================================

The `Flex API` v2 suite enables a merchant to ensure secure transmission of payment information captured from client-side code. Integrate your system with `Flex API` v2 to enable `Cybersource` to protect your customer's primary account number (PAN), card verification number (CVN), and other payment information when payment processing activity crosses the Web.

> IMPORTANT
> ` Flex API ` is not designed to be used from the browser. For securing payment information from the browser, please see the ` Microform Integration ` product.
> Use the APIs in this suite to secure your customer's payment information, and exchange this sensitive data for a *transient token* . A transient token is a temporary reference to sensitive data that `Cybersource` has securely stored on your behalf. A transient token can be transported and stored safely without adding risk to your PCI DSS burden.
> IMPORTANT The transient token response can be cryptographically validated to ensure that payload injection attacks can be mitigated.
> Before you capture the payment data from the client application, generate the context in which the data is to be captured and tokenized. The *capture context* can help you to limit PCI exposure to the context in which it is captured.
> After you capture the payment data from the client application, the `Flex API` v2 can secure and tokenize the data:

* `Cybersource` secures your customer's card data at the device using one-time public encryption keys.
* `Cybersource` then replaces the card data in the client application form with a transient token. A transient token can only be accessed by the merchant.
  {#flex-api-2_ul_zdk_1tn_qqb}
  After you tokenize the payment information, you can initiate `Cybersource` services that use transient tokens in place of your customer's payment information.

`Flex API` v2 Integration Task List {#flex-api-2-task-list}
===========================================================

The `Flex API` v2 is a suite of APIs that enables a merchant to safely and securely accept customer payment information from within a client application. The objective is to replace sensitive payment information with a transient token that can be transmitted without exposing the payment information.
Integrating your system with the `Flex API` v2 consists of these tasks:

1. **Use the `/sessions` API endpoint to generate the capture context.**
   See [Generating the Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-generate-capture-context.md "").
2. **Use the `/public-keys{}` API endpoint to validate the capture context.**
   See [Validating the Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/validate-capture-context-flexv2.md "").
3. **Compile the payment information in the appropriate JWE format.**
   The data must match the data you specified in [Generating the Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-generate-capture-context.md "").
4. **Use the `/tokens` API endpoint to tokenize the payment information.**
   See [Tokenizing Payment Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/flex-api-2/flex-api-2-tokenize-payment-info.md "").
5. Validate the Transient Token
6. Using the Transient Token to Process a Payment

Generating the Capture Context {#flex-api-2-generate-capture-context}
=====================================================================

The first step to Flex API v2 is to generate the context of the customer payment information that is to be captured and tokenized.
IMPORTANT Declaring the capture context ensures that no data can be injected into the process by a malicious actor.
To generate the capture context, use the `/sessions` API endpoint to specify the payment data to be captured. The API returns a JSON Web Token (JWT) data object that contains the authentication component of the interactions and the one-time public encryption keys to which the payment information is to be secured.

> IMPORTANT The internal data structure of the JWT can expand to contain additional data elements. Ensure that your integration and validation rules do not limit the data elements contained in responses.

Resource
--------

Send a fully authenticated POST request from your backend system to the `/sessions` API:

* Test: `https://apitest.cybersource.com``/flex/v2/sessions`
* Production: `https://api.cybersource.com``/flex/v2/sessions`

The resource returns a capture context, which is a JWT date element containing the keys necessary to encrypt the payment data.

Payment API Fields {#flex-api-2-generate-capture-context_payment-api-fields}
----------------------------------------------------------------------------

This is the list of possible fields to capture and tokenize.

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.totalAmount
:

orderInformation.billTo.address1
:

orderInformation.billTo.address2
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.buildingNumber
:

orderInformation.billTo.company
:

orderInformation.billTo.country
:

orderInformation.billTo.district
:

orderInformation.billTo.email
:

orderInformation.billTo.firstName
:

orderInformation.billTo.lastName
:

orderInformation.billTo.locality
:

orderInformation.billTo.phoneNumber
:

orderInformation.billTo.postalCode
:

orderInformation.shipTo.address1
:

orderInformation.shipTo.address2
:

orderInformation.shipTo.administrativeArea
:

orderInformation.shipTo.buildingNumber
:

orderInformation.shipTo.company
:

orderInformation.shipTo.country
:

orderInformation.shipTo.district
:

orderInformation.shipTo.firstName
:

orderInformation.shipTo.lastName
:

orderInformation.shipTo.locality
:

orderInformation.shipTo.postalCode
:

paymentInformation.card.expirationMonth
:

paymentInformation.card.expirationYear
:

paymentInformation.card.number
:

paymentInformation.card.securityCode
:

paymentInformation.card.type
:
This example shows the JWT decoded, containing the JSON Web Key (JWK) encryption keys:

```
{
  "flx" : {
    "path" : "/flex/v2/tokens",
    "data" : "NTaTH27qZUlODxRUBEKIrhAAEFAAlrh8y17ghNZnyYVQb8vzBGNPWSmlznzPqC93XfuMJb+s7DTykZ5Q+yjPoF03Blczt5VviIGUcKh60cSgsHI=",
    "origin" : "https://sl73flxapq002.visa.com:8443",
    "jwk" : {
      "kty" : "RSA",
      "e" : "AQAB",
      "use" : "enc",
      "n" : "pFrA5Lsl22p3gNL5iPjBOYEuXs7z9P-dv7AICTGzlgNyNvyfF_tWGaLqS-lf2QgDvVW3cU0mqVxJXLE1FcJZj71d1sgZB1n4irWsqPq54cfwEx425DDFZaiwQ_Fv1v1mAN3TRT2kaQK-_2dYMNLIWHqj93aw_bLTQT_zo1jcaLTRje6xz7T4CqIQZ6KB_W21tcsMDGUbJ-v6yUpY2EmmcLp_vqIpsEBiCNocDGlnvMJdRyhBb8thqiXrZjTLoOoWtiaHoAlLWL3cUoGRVGtWdEf-I-HfPDpO2HBFiFulwbv54Pjac_sVoGFzGglGrwIWB241c95u-bZUedpN_6ig0Q",
      "kid" : "00SvIaGIfyaw897rDeG9eFdODKaCKc1q"
    }
  },
  "ctx" : [ {
    "data" : {
      "requiredFields" : [ "paymentInformation.card.number" ],
      "optionalFields" : [ "paymentInformation.card.expirationYear", "paymentInformation.card.expirationMonth", "paymentInformation.card.type", "paymentInformation.card.securityCode" ]
    },
    "type" : "api-0.1.0"
  } ],
  "iss" : "Flex API",
  "exp" : 1614792268,
  "iat" : 1614791368,
  "jti" : "rOAksGcp8Bgg6WLj"
}
```

Related Information {#flex-api-2-generate-capture-context_section_enx_z4k_byb}
------------------------------------------------------------------------------

* [REST API Field Reference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")
  {#flex-api-2-generate-capture-context_ul_dbn_bpk_byb}

REST Example: Generating the Capture Context {#flex-api-2-generate-capture-context-example}
===========================================================================================

Minimum Request

```
{
  "paymentInformation" : {
    "card" : {
      "number" : {
      },
      "securityCode" : {
        "required" : false
      },
      "expirationMonth" : {
        "required" : false
      },
      "expirationYear" : {
        "required" : false
      },
      "type" : {
        "required" : false
      }
    }
  }
}
```

Maximum Request

```
{
  "paymentInformation" : {
    "card" : {
      "number" : {
      },
        "securityCode" : {
          "required" : false
        },
        "expirationMonth" : {
          "required" : false
        },
        "expirationYear" : {
          "required" : false
        },
        "type" : {
          "required" : false
        }
      }
    },
    "orderInformation" : {
      "amountDetails" : {
        "totalAmount" : {
          "required" : false
        },
        "currency" : {
          "required" : false
        }
      },
      "billTo" : {
        "address1" : {
          "required" : false
        },
        "address2" : {
          "required" : false
        },
        "administrativeArea" : {
          "required" : false
        },
        "buildingNumber" : {
          "required" : false
        },
        "country" : {
          "required" : false
        },
        "district" : {
          "required" : false
        },
        "locality" : {
          "required" : false
        },
        "postalCode" : {
          "required" : false
        },
        "email" : {
          "required" : false
        },
        "firstName" : {
          "required" : false
        },
        "lastName" : {
          "required" : false
        },
        "phoneNumber" : {
          "required" : false
        },
        "company" : {
          "required" : false
        }
      },
      "shipTo" : {
        "address1" : {
          "required" : false
        },
        "address2" : {
          "required" : false
        },
        "administrativeArea" : {
          "required" : false
        },
        "buildingNumber" : {
          "required" : false
        },
        "country" : {
          "required" : false
        },
        "district" : {
          "required" : false
        },
        "locality" : {
          "required" : false
        },
        "postalCode" : {
          "required" : false
        },
        "firstName" : {
          "required" : false
        },
        "lastName" : {
          "required" : false
        },
        "company" : {
          "required" : false
        }
      }
    }
  }
}
```

Response Payload

```
eyJraWQiOiJzbiIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJOVGFUSDI3cVpVbE9EeFJVQkVLSXJoQUFFRkFBbHJoOHkxN2doTlpueVlWUWI4dnpCR05QV1NtbHpuelBxQzkzWGZ1TUpiK3M3RFR5a1o1USt5alBvRjAzQmxjenQ1VnZpSUdVY0toNjBjU2dzSElcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3NsNzNmbHhhcHEwMDIudmlzYS5jb206ODQ0MyIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJwRnJBNUxzbDIycDNnTkw1aVBqQk9ZRXVYczd6OVAtZHY3QUlDVEd6bGdOeU52eWZGX3RXR2FMcVMtbGYyUWdEdlZXM2NVMG1xVnhKWExFMUZjSlpqNzFkMXNnWkIxbjRpcldzcVBxNTRjZndFeDQyNURERlphaXdRX0Z2MXYxbUFOM1RSVDJrYVFLLV8yZFlNTkxJV0hxajkzYXdfYkxUUVRfem8xamNhTFRSamU2eHo3VDRDcUlRWjZLQl9XMjF0Y3NNREdVYkotdjZ5VXBZMkVtbWNMcF92cUlwc0VCaUNOb2NER2xudk1KZFJ5aEJiOHRocWlYclpqVExvT29XdGlhSG9BbExXTDNjVW9HUlZHdFdkRWYtSS1IZlBEcE8ySEJGaUZ1bHdidjU0UGphY19zVm9HRnpHZ2xHcndJV0IyNDFjOTV1LWJaVWVkcE5fNmlnMFEiLCJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSJ9fSwiY3R4IjpbeyJkYXRhIjp7InJlcXVpcmVkRmllbGRzIjpbInBheW1lbnRJbmZvcm1hdGlvbi5jYXJkLm51bWJlciJdLCJvcHRpb25hbEZpZWxkcyI6WyJwYXltZW50SW5mb3JtYXRpb24uY2FyZC5leHBpcmF0aW9uWWVhciIsInBheW1lbnRJbmZvcm1hdGlvbi5jYXJkLmV4cGlyYXRpb25Nb250aCIsInBheW1lbnRJbmZvcm1hdGlvbi5jYXJkLnR5cGUiLCJwYXltZW50SW5mb3JtYXRpb24uY2FyZC5zZWN1cml0eUNvZGUiXX0sInR5cGUiOiJhcGktMC4xLjAifV0sImlzcyI6IkZsZXggQVBJIiwiZXhwIjoxNjE0NzkyMjY4LCJpYXQiOjE2MTQ3OTEzNjgsImp0aSI6InJPQWtzR2NwOEJnZzZXTGoifQ.uHMrYZFoqqDiiic-s-29GAI0V5Ex1361Izzhxiqt6eMZcTW-bApAxgfTe0eBK3vi9s6VZbm1fgE1dh8BdMeo2AkF-_Q4c3wch2YPOMhcuOpstZyLj22tnrmaLXmcHwTorDBMA3fVH_8EIn8T4gonZ-ItTa05sxAk5rLVEWywlau5-Gi74tuxtDQOPIc7F9SzmqwGmLCuUZ6JuJf8bExAyL5ChiqQ9MDsbP6Q2jtDXok4VAHVkJR3uRJvmblHfgRM1LRVH8XGv9GX69b30_rQ4Md5xOugvI6Hu7X30qo9fFpfT3v9qQ6wocnJpowKe2v0u7rcid_GqqjZckbEVb47VQ
```

Validating the Capture Context {#validate-capture-context-flexv2}
=================================================================

The capture context that you generated is a JSON Web Token (JWT) data object. The JWT is digitally signed using a public key. The purpose is to ensure the validity of the JWT and confirm that it comes from `Cybersource`. When you do not have a key specified locally in the JWT header, you should follow best cryptography practices and validate the capture context signature.
To validate a JWT, you can obtain its public key. This public RSA key is in JSON Web Key (JWK) format. This public key is associated with the capture context on the `Cybersource` domain.
To get the public key of a capture context from the header of the capture context itself, retrieve the key ID associated with the public key. Then, pass the key ID to the `public-keys` endpoint.
**Example**
From the header of the capture context, get the key ID (`kid`) as shown in this example:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Append the key ID to the endpoint `/flex/v2/public-keys/`**3g**. Then, call this endpoint to get the public key. IMPORTANT

> Depending on the cryptographic method you use to validate the public key, you might need to convert the key to privacy-enhanced mail (PEM) format. {#validate-capture-context-flexv2_d63e59}

Resource {#validate-capture-context-flexv2_d63e63}
--------------------------------------------------

Pass the key ID (kid), that you obtained from the capture context header, as a path parameter, and send a GET request to the `/public-keys` endpoint:

* Test: `https://apitest.cybersource.com``/flex/v2/public-keys/`*{kid}*
* Production: `https://api.cybersource.com``/flex/v2/public-keys/`*{kid}*

The resource returns the public key. Use this public RSA key to validate the capture context.

Example {#validate-capture-context-flexv2_d63e99}
-------------------------------------------------

```
eyJraWQiOiIzZyIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiI2bUFLNTNPNVpGTUk5Y3RobWZmd2doQUFFRGNqNU5QYzcxelErbm8reDN6WStLOTVWQ2c5bThmQWs4czlTRXBtT21zMmVhbEx5NkhHZ29oQ0JEWjVlN3ZUSGQ5YTR5a2tNRDlNVHhqK3ZoWXVDUmRDaDhVY1dwVUNZWlZnbTE1UXVFMkEiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJyQmZwdDRjeGlkcVZwT0pmVTlJQXcwU1JCNUZqN0xMZjA4U0R0VmNyUjlaajA2bEYwTVc1aUpZb3F6R3ROdnBIMnFZbFN6LVRsSDdybVNTUEZIeTFJQ3BfZ0I3eURjQnJ0RWNEanpLeVNZSTVCVjNsNHh6Qk5CNzRJdnB2Smtqcnd3QVZvVU4wM1RaT3FVc0pfSy1jT0xpYzVXV0ZhQTEyOUthWFZrZFd3N3c3LVBLdnMwNmpjeGwyV05STUIzTS1ZQ0xOb3FCdkdCSk5oYy1uM1lBNU5hazB2NDdiYUswYWdHQXRfWEZ0ZGItZkphVUVUTW5WdW9fQmRhVm90d1NqUFNaOHFMOGkzWUdmemp2MURDTUM2WURZRzlmX0tqNzJjTi1OaG9BRURWUlZyTUtiZ3QyRDlwWkJ1d2gzZlNfS3VRclFWTVdPelRnT3AzT2s3UVFGZ1EiLCJraWQiOiIwOEJhWXMxbjdKTUhjSDh1bkcxc1NDUVdxN2VveWQ1ZyJ9fSwiY3R4IjpbeyJkYXRhIjp7InRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly93d3cudGVzdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSJ9LCJ0eXBlIjoibWYtMC4xMS4wIn1dLCJpc3MiOiJGbGV4IEFQSSIsImV4cCI6MTYxNjc3OTA5MSwiaWF0IjoxNjE2Nzc4MTkxLCJqdGkiOiJ6SG1tZ25uaTVoN3ptdGY0In0.GvBzyw6JKl3b2PztHb9rZXawx2T817nYqu6goxpe4PsjqBY1qeTo19R-CP_DkJXov9hdJZgdlzlNmRY6yoiziSZnGJdpnZ-pCqIlC06qrpJVEDob3O_efR9L03Gz7F5JlLOiTXSj6nVwC5mRlcP032ytPDEx5TMI9Y0hmBadJYnhEMwQnn_paMm3wLh2v6rfTkaBqd8n6rPvCNrWMOwoMdoTeFxku-d27jlA95RXqJWfhJSN1MFquKa7THemvTX2tnjZdTcrTcpgHlxi22w7MUFcnNXsbMouoaYiEdAdSlCZ7LCXrS1Brdr_FWDp7v0uwqHm7OALsGrw8QbGTafF8w
```

Base64 decode the capture context to get the key ID (`kid`) from its header:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Get its public key from `/flex/v2/public-keys/3g`:

```
{
    "kty":"RSA",
    "use":"enc",
    "kid":"3g",
    "n":"ir7Nl1Bj8G9rxr3co5v_JLkP3o9UxXZRX1LIZFZeckguEf7Gdt5kGFFfTsymKBesm3Pe
     8o1hwfkq7KmJZEZSuDbiJSZvFBZycK2pEeBjycahw9CqOweM7aKG2F_bhwVHrY4YdKsp
     _cSJe_ZMXFUqYmjk7D0p7clX6CmR1QgMl41Ajb7NHI23uOWL7PyfJQwP1X8HdunE6ZwK
     DNcavqxOW5VuW6nfsGvtygKQxjeHrI-gpyMXF0e_PeVpUIG0KVjmb5-em_Vd2SbyPNme
     nADGJGCmECYMgL5hEvnTuyAybwgVwuM9amyfFqIbRcrAIzclT4jQBeZFwkzZfQF7MgA6QQ",
     "e":"AQAB"
}
```

Securing Payment Information {#flex-api-2-secure-payment-info}
==============================================================

After you compile and encrypt the customer payment information, secure the payment information.
IMPORTANT Payment information must be secured before it is tokenized so that data in transit cannot be compromised and exposed to malicious actors.
To secure the payment information for transport, you must encrypt the data using the one-time public encryption keys provided in the capture context.

Process Overview
----------------

The process for securing the payment information consists of these steps:

1. Construct the payment JSON payload.
2. Extract the one-time public encryption keys from the capture context.
3. Use the keys to generate a JWE (JSON Web Encryption) data object.

Internal Structure
------------------

The encrypted payment data consists of these parts:

* **data**---Structure that specifies the data to capture and store.
* **context** ---Structure that specifies the capture context that you obtained from the `/sessions` API request.
* **index** ---Component that must be set to **0**.

This example shows basic structure of the payload:

```
{
"data": {
},
"context": "",
"index": 0
}
```

Example
-------

This example shows a fully populated request payload prior to encryption:

```
{
"data": {
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "type": "",
      "securityCode": ""
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@email.com",
      "phoneNumber": "4158880000"
    }
  }
},
"context": "eyJraWQiOiIzZyIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJyMlh5b2QxUk9SdUEyajFwUnA0cUpoQUFFSkFvUVN1QzZzZXFkVHpMaUJuTmZrMzljOXJQSHJnQTRsSEZ1QXRrS0JiRmpqa0tHV2tmNUVjNHhBRVBMTzc0b0NsdjhneUhueFJOb1E1dHYwVnpNYU5pOWNxd21EWmJReExENW5pVk1SWGMiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJqYlA4dHpIX21FQUloYUdmcXJ3TEQtZHZsbTZSLXgySWVaVDNweUU2YXF2SkxkY0h4bzRQZktOSXpMZ0hfZEJVTjZENGxFc2dTY3NoT1RVOVVGVVQyVERpZUlaMVJjNW5rclNub2lYcmR5MFJscUlrS3BCa2h1WXRsSWM4OTZQb3JYVENmUk45MmpXOXgzN2dUUnRBc2l2QXJQR2p0WGV4QnhaN29SWkFXRVY5Yy1FYVFybU55N2ZzTnJxdEZMR2xVbXdEQ05ONEVERXdjaWd3ck5JUlJQaHpPQkJ5UWFvenB6VlhXSVctS3RRb2otSHFfTmk2YUN0MXkwdWVLZjFkZ0dyUHpibDV6WVNFYUJtM3gzdGZzTmM3MXVQbGJXZzY0LU83SnlMcFJWVU5UYnR1NC1ONWNic0ZaMnZBeGYwWTdWRnRaclZiR0ZTRmFLQjZPWVdWVnciLCJraWQiOiIwOGlHZEN2Z2lCWEM4YXd6U0szWjRoUm9hbElKTzVvMSJ9fSwiY3R4IjpbeyJkYXRhIjp7InRhcmdldE9yaWdpbnMiOlsiaHR0cDovL2xvY2FsaG9zdDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo1MDAwIl0sIm1mT3JpZ2luIjoiaHR0cHM6Ly90ZXN0ZmxleC5jeWJlcnNvdXJjZS5jb20ifSwidHlwZSI6Im1mLTAuMTEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE2MDQ2MTc4MjgsImlhdCI6MTYwNDYxNjkyOCwianRpIjoiR1oxb1dCbTVBbHkzendwOCJ9.ZF9-CG_FvIQTMocIMwcBH6IMWBiFfl-ufPj0TdXFuTSpusL6fAsxnyxdlf6V6i6wO0PDgv6SY-2MWP-Q600WAjFZfmR1y3r13Tig9Ldql4WOp8zhIb6klLD01PYWeyXYZ0xqRQL0_eYTliDrV66P72PVX6DqCeoJFYnh_csEcAChmyBVRqI2Gxd9zelALqBNU6WeHiN8FT36xRHHruxRJ2hBCI_OE0p9haQjuD4qtfk9grfhnt2mFpiC4s0j0yHaHCgiVm5NPuPecpS7t47cjsSG6PfIHNbBAjdIVcNpmFFyH6sCLRplOgW0vPYw4nUOgtq7y_voHe_nOal6eHFr4A",
"index": 0
}
```

JSON Web Encryption Payload
---------------------------

The `/tokens` API endpoint accepts a JSON Web Encryption (JWE) data object that has been encrypted using the RsaOaep encryption scheme and the JSON Web Key (JWK) provided in the capture context. JWE is a standard that defines how data can be encrypted using JSON-based data structures. For details, see IETF RFC 7516 at <https://tools.ietf.org/html/rfc7516>.
The JWE format consists of five sections separated by a period (**.** ) delimiters:

header . encrypted_key . cypher_text . iv . auth_tag
The payload for the `/tokens` request is a JWE data object.
This shows an encrypted payload in a fully formed JWE data object:

```
eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImVuYyI6IkEyNTZHQ00iLCJhbGciOiJSU0EtT0FFUCJ9.juQDhF5XcZ1rDbupn1nZ1qHhephzWpa8FumH4KrsD0yF1tCOD0L8WfpSyd5VGIewb4I1IipmSB5vV0O3Cb6FrNLipjFq-oexFRwSK92NbB88ySFO-7FyvPddiqaQFkA81xn8nwdoHMwUsQuqe8Ts_krLsvYghmscxXKkwcEKqxoWbmD-yEfvKxGyHACLprAKLm-xusexaJLF42OTxYuEhzzrSe6MRll0zXuk2DAhtUL2oHCgu8P3shgJBJqsOPcAFtwtLBRoDwlDt0ybOHjd34Svbpgf_3ncFnDkEQYe5QeElEHaB2a0Nbwo61I1UETfhedHQc8IMtDmVuKk9pgCTg.uWrwGp2jZxZd5wF0.oFzZ3I2ry77jf-3wB_2q8G-0tbYJWQj88NdzRmVNO34JbreX5WOCju7ntvN8h83NJXEA_cQech2PEGIZV_tADBaLbSxJeitYKwaQhs_tRVrzrcd8Qhgs4OADfky2m310eV8bUG8D4GZBKRHL6ScLf5p30b6Hoa5fDYsU7IHNyCReiaiGPExlY4luwL9QQxrfY2LTv74Pcqyh-B4byNxR5hTw3SJm7DT7YQLl6_-2ROqJhJoweTdDJtmJoM-LxKEij2TLgHBdqso9f036dfn0SHLl1vG86C1-6DA9yFIZB3gLYnyom1jZuGxUOPXDojUfXo0OpUj8OI6CnQWdhKpC9X19s8xAhIAUYYdvWrEqFfBzd9S-4E-ZdyUGfxG7fLQuLZKQJeYBbGCssLGSIXLOb15sKOopIgqCTU7M5EN_F7zW0IwJ4-b8OVf_J80-hW1e043RlzBoMr3aGdXFIaLmVbEIzTNeZrulYTTWWLbQlcLTXqAM0yFlKmIrpq55VruvVR8i_iju5MFzzTYuLut9ecvYbFFeUkUaUBihNXg4Np57Ix23gaJuMcPBgUqkH3nCTZQE7yQOynzO-lho_jAHy1xcwV_DJhhAJnACO5HUDAjVKmr-GKqxvDZWVzrqjFkPArX81eRSnn9Dr2Ahozehn9FTB37AJV3BEC2i7WMvAbQE1EpPVGTdvVDhH2xlLAHqHTBeQakzY4e81h2L3EDCmdjx_yZdZOUUSG3mLQSp864OV5pHc2X22ZRadGbrLwnA-m2W1oDZIzh2t5nZdJhePnNzHbNXTf0xWSklxdgJdfG52FVSH-cKiJQnDhmCH6nPVK7NKnL0vRuZ-uuOa4PJQDoT2H8eSjpvo8fo9rwfLYmQJa042t7OSE95bER9k1oJTUm83LNA3bxhWk5en2UFgcip3z3KlOmFwPLVNCpzitULzAEHwBJlrB0aGXkQi1bJMxo9XZNREnFyYAlX3-aruXIe47pwAyOEX-hd-3Y7UsxBVYB86se51q2-VUldR0zj6cwZvrTxhFM_gAsD0HisAGa6E3n3n3w1JAvjuZdHRoQqaT00YFmTdSbocmTOEUammYmBjagKKycOzgmoZSaYpffQl_R06tEZke6uhJrPQuTwLwivZMtnWE8O16VIRX4cG3OfzaRYs0GvPWumDlrSbM8FugMIEaUTng5T9CdkixegRmszDELzNjNTJLe2WwxJG4Kb_1-yGMRlhFys4FEwVMk8AWJJRDpwG0jdmHkBz9l7z1PFdIcidbIpmgH7m5RD6kwRSxaG_BJWDc2IkIFyNa2G_-gHjQh_utablUOL9CXxxFCKD9UHojtsHneFt1bhV2P_sfYYhtZo5XloKAAEXqmOSY2boYyj0hMlKNuVqukrnWG6-bV-LBf9DvpYNKO9YeU6rYD_WOxSQlliqVvEK8n9xLCmQQKsK2Xj2WGh7wWTQTMh18hcsNENN3Loq9DofAbOrCXqdREAshxg_MOI5vGe0JvIR9Gj6kAhKGFf2DYBqMynbb9jWJnjCzFXBCqXXjTOuCoZdzlV9RbLxIBOOojIfLfdtVLGKPLKizXaSQ8YrLiBATarkpO7WFSSF66lvezwDZlfDErA-0kij1n2poKqDLYL3vNfX8vU33ef96VQc9I3auTpiWd0NLa5yw0RWREAjqa4pHYTEZDiLcD0vETt84_aon3U7co_8fAYrztokTIJ2ORuhN_xA0rV1MbOZIwW6m-duqYLFLQlcwjxNwTdaberNy6bCg9otljd5l7nSbzZ6UpHrHDF02LrM41NmQUx9tZFHypYjFdgiKKgqk-kTe3pq6ithsTPvcDvDkNgCSb9H_X30qm2-0VXaGIcYBcmJdsbBt7VJuYVZ1I_2l4-_6glgvgQz9d5KaHyZeJimSXqOsbqUQzNKWC7_K81Z5XmqCPJByrOiROkO6iEe_poqRgVzHETHYmstAzUlgUvPD3XocZdlHuPHArQe6GddVmxnhTDV1M0TmXwK03f0jGg7LMjWjU1k15X8xYZTk_HMo76IetUOdf9BIoaMBqMHJkk936uzjIeiW1DbEb4ExLtpIeSoq_fnelAWoVEDMa_XoVkWCR5R7wTJjGyZKjJJkJ6UqYQguS9oO95MZp8N0Qa41wKCvztLbFKtEU7sPz3pU5oUVbn9cZS7WCzCUNWGxb3PO0nTzPsP_MhD71JcuAEFSLS05m1hkoNiYe_6pmLv8Rrgp71kFsTOIOUrcUvwdJRikDOLdNbO5b-_6HjczDPzx9PaM_Zn-34mfOQPthWAfum3YvpmthuKxAWfdBChZXe9oCMeBGewGl7mKMh9H5SP6su5yw-IFe7iBd338LVVPjRXif1rNsU631YXBu9Lz-l6o4cuGuYPVHPhHf4lifFXvlvi702wD7fbYn3cZ55_yGVJvcFPq6OMUGJUSy5ncj-n7a8-IcGmSFpMtgnMc1ycJa_0N1vtwyjm0WvdzkUrBNC_OoCmHlLaG3XTRenL_WYhzxDUdQQBuSC3acFu28x3NL8cmR5iqy7sBGUKcwt_ogX9ZoQyFzUTFOw.QqKIuF8EnuhOTM8PvGEs8A
```

Tokenizing Payment Information {#flex-api-2-tokenize-payment-info}
==================================================================

After the payment information is secured in a JWE data object, it can be tokenized. Use the resulting transient token within `Cybersource` [APIs](https://developer.cybersource.com/api-reference-assets/index.md#staticContentRHSSection "") in place of the payment information associated with it.
To tokenize the payment information, send the encrypted payment data to the `/tokens` API endpoint. The API responds to the request with a transient token in the form of a JSON Web Token (JWT).

> IMPORTANT The internal data structure of the JWT can expand to contain additional data elements. Ensure that your integration and validation rules do not limit the data elements contained in responses.

Resource
--------

> IMPORTANT
> ` Flex API ` is not designed to be used from the browser. For securing payment information from the browser, please see the ` Microform Integration ` product.
> Send an unauthenticated POST request from your customer's device or backend system to the `/tokens` API endpoint:

* Test: `https://apitest.cybersource.com``/flex/v2/tokens`
* Production: `https://api.cybersource.com``/flex/v2/tokens`

The resource returns a transient token that represents the supplied customer card data. The token can replace the payment information in any follow-on `Cybersource` services.

Tokens API Request Payload
--------------------------

The payload for the `/tokens` request is a JWE data object.

Example
-------

```
eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImVuYyI6IkEyNTZHQ00iLCJhbGciOiJSU0EtT0FFUCJ9.juQDhF5XcZ1rDbupn1nZ1qHhephzWpa8FumH4KrsD0yF1tCOD0L8WfpSyd5VGIewb4I1IipmSB5vV0O3Cb6FrNLipjFq-oexFRwSK92NbB88ySFO-7FyvPddiqaQFkA81xn8nwdoHMwUsQuqe8Ts_krLsvYghmscxXKkwcEKqxoWbmD-yEfvKxGyHACLprAKLm-xusexaJLF42OTxYuEhzzrSe6MRll0zXuk2DAhtUL2oHCgu8P3shgJBJqsOPcAFtwtLBRoDwlDt0ybOHjd34Svbpgf_3ncFnDkEQYe5QeElEHaB2a0Nbwo61I1UETfhedHQc8IMtDmVuKk9pgCTg.uWrwGp2jZxZd5wF0.oFzZ3I2ry77jf-3wB_2q8G-0tbYJWQj88NdzRmVNO34JbreX5WOCju7ntvN8h83NJXEA_cQech2PEGIZV_tADBaLbSxJeitYKwaQhs_tRVrzrcd8Qhgs4OADfky2m310eV8bUG8D4GZBKRHL6ScLf5p30b6Hoa5fDYsU7IHNyCReiaiGPExlY4luwL9QQxrfY2LTv74Pcqyh-B4byNxR5hTw3SJm7DT7YQLl6_-2ROqJhJoweTdDJtmJoM-LxKEij2TLgHBdqso9f036dfn0SHLl1vG86C1-6DA9yFIZB3gLYnyom1jZuGxUOPXDojUfXo0OpUj8OI6CnQWdhKpC9X19s8xAhIAUYYdvWrEqFfBzd9S-4E-ZdyUGfxG7fLQuLZKQJeYBbGCssLGSIXLOb15sKOopIgqCTU7M5EN_F7zW0IwJ4-b8OVf_J80-hW1e043RlzBoMr3aGdXFIaLmVbEIzTNeZrulYTTWWLbQlcLTXqAM0yFlKmIrpq55VruvVR8i_iju5MFzzTYuLut9ecvYbFFeUkUaUBihNXg4Np57Ix23gaJuMcPBgUqkH3nCTZQE7yQOynzO-lho_jAHy1xcwV_DJhhAJnACO5HUDAjVKmr-GKqxvDZWVzrqjFkPArX81eRSnn9Dr2Ahozehn9FTB37AJV3BEC2i7WMvAbQE1EpPVGTdvVDhH2xlLAHqHTBeQakzY4e81h2L3EDCmdjx_yZdZOUUSG3mLQSp864OV5pHc2X22ZRadGbrLwnA-m2W1oDZIzh2t5nZdJhePnNzHbNXTf0xWSklxdgJdfG52FVSH-cKiJQnDhmCH6nPVK7NKnL0vRuZ-uuOa4PJQDoT2H8eSjpvo8fo9rwfLYmQJa042t7OSE95bER9k1oJTUm83LNA3bxhWk5en2UFgcip3z3KlOmFwPLVNCpzitULzAEHwBJlrB0aGXkQi1bJMxo9XZNREnFyYAlX3-aruXIe47pwAyOEX-hd-3Y7UsxBVYB86se51q2-VUldR0zj6cwZvrTxhFM_gAsD0HisAGa6E3n3n3w1JAvjuZdHRoQqaT00YFmTdSbocmTOEUammYmBjagKKycOzgmoZSaYpffQl_R06tEZke6uhJrPQuTwLwivZMtnWE8O16VIRX4cG3OfzaRYs0GvPWumDlrSbM8FugMIEaUTng5T9CdkixegRmszDELzNjNTJLe2WwxJG4Kb_1-yGMRlhFys4FEwVMk8AWJJRDpwG0jdmHkBz9l7z1PFdIcidbIpmgH7m5RD6kwRSxaG_BJWDc2IkIFyNa2G_-gHjQh_utablUOL9CXxxFCKD9UHojtsHneFt1bhV2P_sfYYhtZo5XloKAAEXqmOSY2boYyj0hMlKNuVqukrnWG6-bV-LBf9DvpYNKO9YeU6rYD_WOxSQlliqVvEK8n9xLCmQQKsK2Xj2WGh7wWTQTMh18hcsNENN3Loq9DofAbOrCXqdREAshxg_MOI5vGe0JvIR9Gj6kAhKGFf2DYBqMynbb9jWJnjCzFXBCqXXjTOuCoZdzlV9RbLxIBOOojIfLfdtVLGKPLKizXaSQ8YrLiBATarkpO7WFSSF66lvezwDZlfDErA-0kij1n2poKqDLYL3vNfX8vU33ef96VQc9I3auTpiWd0NLa5yw0RWREAjqa4pHYTEZDiLcD0vETt84_aon3U7co_8fAYrztokTIJ2ORuhN_xA0rV1MbOZIwW6m-duqYLFLQlcwjxNwTdaberNy6bCg9otljd5l7nSbzZ6UpHrHDF02LrM41NmQUx9tZFHypYjFdgiKKgqk-kTe3pq6ithsTPvcDvDkNgCSb9H_X30qm2-0VXaGIcYBcmJdsbBt7VJuYVZ1I_2l4-_6glgvgQz9d5KaHyZeJimSXqOsbqUQzNKWC7_K81Z5XmqCPJByrOiROkO6iEe_poqRgVzHETHYmstAzUlgUvPD3XocZdlHuPHArQe6GddVmxnhTDV1M0TmXwK03f0jGg7LMjWjU1k15X8xYZTk_HMo76IetUOdf9BIoaMBqMHJkk936uzjIeiW1DbEb4ExLtpIeSoq_fnelAWoVEDMa_XoVkWCR5R7wTJjGyZKjJJkJ6UqYQguS9oO95MZp8N0Qa41wKCvztLbFKtEU7sPz3pU5oUVbn9cZS7WCzCUNWGxb3PO0nTzPsP_MhD71JcuAEFSLS05m1hkoNiYe_6pmLv8Rrgp71kFsTOIOUrcUvwdJRikDOLdNbO5b-_6HjczDPzx9PaM_Zn-34mfOQPthWAfum3YvpmthuKxAWfdBChZXe9oCMeBGewGl7mKMh9H5SP6su5yw-IFe7iBd338LVVPjRXif1rNsU631YXBu9Lz-l6o4cuGuYPVHPhHf4lifFXvlvi702wD7fbYn3cZ55_yGVJvcFPq6OMUGJUSy5ncj-n7a8-IcGmSFpMtgnMc1ycJa_0N1vtwyjm0WvdzkUrBNC_OoCmHlLaG3XTRenL_WYhzxDUdQQBuSC3acFu28x3NL8cmR5iqy7sBGUKcwt_ogX9ZoQyFzUTFOw.QqKIuF8EnuhOTM8PvGEs8A
```

Tokens API Response Payload
---------------------------

Example
-------

```
eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJVldBSURPSkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRIVZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTuq41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcKLr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ
```

Validating the Transient Token
------------------------------

After receiving the transient token, validate its integrity using the public key embedded within the capture context created at the beginning of this flow. This verifies that `Cybersource` issued the token and that no data tampering occurred during transit.

Example: Capture Context Public Key
-----------------------------------

```
"jwk": {
    "kty": "RSA",
    "e": "AQAB",
    "use": "enc",
    "n": "3DhDtIHLxsbsSygEAG1hcFqnw64khTIZ6w9W9mZNl83gIyj1FVk-H5GDMa85e8RZFxUwgU_zQ0kHLtON
          o8SB52Z0hsJVE9wqHNIRoloiNPGPQYVXQZw2S1BSPxBtCEjA5x_-bcG6aeJdsz_cAE7OrIYkJa5Fphg9
         _pxgYRod6JCFjgdHj0iDSQxtBsmtxagAGHjDhW7UoiIig71SN-f-gggaCpITem4zlb5kkRVvmKMUANe4B
         36v4XSSSpwdP_H5kv4JDz_cVlp_Vy8T3AfAbCtROyRyH9iH1Z-4Yy6T5hb-9y3IPD8vlc8E3JQ4qt6U46
         EeiKPH4KtcdokMPjqiuQ",
    "kid": "00UaBe20jy9VkwZUQPZwNNoKFPJA4Qhc"
}
```

Use the capture context public key to cryptographically validate the JWT provided from a successful `/tokens` call.
You might have to convert the JSON Web Key (JWK) to privacy-enhanced mail (PEM) format for compatibility with some JWT validation software libraries.

Using the Transient Token to Process a Payment
----------------------------------------------

After you validate the transient token, you can use it in place of the PAN with payment services for 15 minutes. The transient token can be used multiple times within the 15-minute period.
When the consuming service receives a request containing a transient token, it retrieves the tokenized data and injects the values into your request before processing, and none of the sensitive data is stored on your systems.
In some scenarios, the jti value contained in the JWT transient token response must be extracted and used instead of the entire JWT.
**REST API with Transient Token JSON Web Token**

```
"tokenInformation": {
     "transientTokenJwt": "eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFs
     ZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS
     4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJ
     VldBSURPSkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRI
     VZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTu
     q41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2
     OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcK
     Lr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ"
}
```

**REST API withJSON Web Token ID**

```
"tokenInformation": {
    "jti": "1E3GQY1RNKBG6IBD2EP93C43PIZ2NQ6SQLUIM3S16BGLHTY4IIEK5EB 1AE5D73A4",
}
```

Validate the Transient Token {#flex-api-2-validate-token}
=========================================================

After receiving the transient token, validate its integrity using the public key embedded within the capture context created at the beginning of this flow. This verifies that `Cybersource` issued the token and that no data tampering occurred during transit.

Example: Capture Context Public Key
-----------------------------------

```
"jwk": {
    "kty": "RSA",
    "e": "AQAB",
    "use": "enc",
    "n": "3DhDtIHLxsbsSygEAG1hcFqnw64khTIZ6w9W9mZNl83gIyj1FVk-H5GDMa85e8RZFxUwgU_zQ0kHLtON
          o8SB52Z0hsJVE9wqHNIRoloiNPGPQYVXQZw2S1BSPxBtCEjA5x_-bcG6aeJdsz_cAE7OrIYkJa5Fphg9
         _pxgYRod6JCFjgdHj0iDSQxtBsmtxagAGHjDhW7UoiIig71SN-f-gggaCpITem4zlb5kkRVvmKMUANe4B
         36v4XSSSpwdP_H5kv4JDz_cVlp_Vy8T3AfAbCtROyRyH9iH1Z-4Yy6T5hb-9y3IPD8vlc8E3JQ4qt6U46
         EeiKPH4KtcdokMPjqiuQ",
    "kid": "00UaBe20jy9VkwZUQPZwNNoKFPJA4Qhc"
}
```

Use the capture context public key to cryptographically validate the JWT provided from a successful `/tokens` call.
You might have to convert the JSON Web Key (JWK) to privacy-enhanced mail (PEM) format for compatibility with some JWT validation software libraries.

Using the Transient Token to Process a Payment
----------------------------------------------

After you validate the transient token, you can use it in place of the PAN with payment services for 15 minutes. The transient token can be used multiple times within the 15-minute period.
When the consuming service receives a request containing a transient token, it retrieves the tokenized data and injects the values into your request before processing, and none of the sensitive data is stored on your systems.
In some scenarios, the jti value contained in the JWT transient token response must be extracted and used instead of the entire JWT.
**REST API with Transient Token JSON Web Token**

```
"tokenInformation": {
     "transientTokenJwt": "eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFs
     ZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS
     4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJ
     VldBSURPSkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRI
     VZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTu
     q41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2
     OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcK
     Lr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ"
}
```

**REST API withJSON Web Token ID**

```
"tokenInformation": {
    "jti": "1E3GQY1RNKBG6IBD2EP93C43PIZ2NQ6SQLUIM3S16BGLHTY4IIEK5EB 1AE5D73A4",
}
```

Using the Transient Token to Process a Payment {#flex-api-2-validate-token}
===========================================================================

After you validate the transient token, you can use it in place of the PAN with payment services for 15 minutes. The transient token can be used multiple times within the 15-minute period.
When the consuming service receives a request containing a transient token, it retrieves the tokenized data and injects the values into your request before processing, and none of the sensitive data is stored on your systems.
In some scenarios, the jti value contained in the JWT transient token response must be extracted and used instead of the entire JWT.
**REST API with Transient Token JSON Web Token**

```
"tokenInformation": {
     "transientTokenJwt": "eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFs
     ZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS
     4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJ
     VldBSURPSkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRI
     VZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTu
     q41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2
     OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcK
     Lr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ"
}
```

**REST API with JSON Web Token ID**

```
"tokenInformation": {
    "jti": "1E3GQY1RNKBG6IBD2EP93C43PIZ2NQ6SQLUIM3S16BGLHTY4IIEK5EB 1AE5D73A4",
}
```

`Microform Integration` v2 {#microform-integ-v2}
================================================

`Microform Integration` replaces the sensitive payment input fields of a client application with secure `Cybersource`-hosted fields. These fields securely accept payment information, including card and check data, and replaces it with a non-sensitive tokens.
You can style these fields to look and behave like any other field on your website, which could qualify you for PCI DSS assessments based on [SAQ A](https://www.pcisecuritystandards.org/documents/Understanding_SAQs_PCI_DSS_v3.pdf "").
`Microform Integration` provides the most secure method for tokenizing card and check data. Sensitive data is encrypted on the customer's device before HTTPS transmission to `Cybersource`. This method reduces the potential for man-in-the middle attacks on the HTTPS connection.

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

How It Works {#microform-integ-how-works-v2}
============================================

You can use the `Microform Integration` JavaScript library to securely replace sensitive input fields with `Cybersource`-hosted secure iframes. These iframes capture payment information, including card numbers and `eCheck` data. This ensures that sensitive data is handled securely within your checkout process.

Accepting Card Information
--------------------------

For card transactions, the captured card number is replaced with a mathematically irreversible token that only you can use. This token can be used in place of the card number for follow-on transactions in existing `Cybersource` APIs.
`Microform Integration` replaces the following card payment fields in your input form:

* Payment Card (PAN)
* CVN
* Month (non-sensitive)
* Year (non-sensitive)
  With this option you can pass imonth and year in the request (if required), but these fields are non-sensitive.
  This figure shows the `Microform Integration` process for accepting card information.

#### Figure:

`Microform Integration` Process with Card Information ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/flexible-token/images/mf-flow-cc-cybs-600x285.svg/jcr:content/renditions/original)

Accepting `eCheck` Information
------------------------------

`Microform Integration` also supports the acceptance of `eCheck` information. As with card transactions, the sensitive `eCheck` data is securely captured and replaced with a token.
Accepting `eCheck` information enables merchants to collect funds from a customer's bank account through both the ACH service and eCheck service (US only) for either of these flows:

* **ACH services** are a set of connections composed of the legacy gateway solutions where `Cybersource` serves as the gateway.

* **`eCheck`** , the new service on Payments 2.0, is the acquirer solution where `Cybersource` is the acquirer.
  `Microform Integration` replaces these `eCheck` information fields in your payment input form:

* Routing Number

* Account Number

* Account type (non-sensitive)
  This figure shows the `Microform Integration` process for accepting `eCheck` information.

#### Figure:

`Microform Integration` Process with `eCheck` Information ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/flexible-token/images/mf-flow-echeck-cybs-600x285.png/jcr:content/renditions/original)

PCI Compliance {#microform-integ-pci-comp-v2}
=============================================

The least burdensome level of PCI compliance is SAQ A. To achieve this compliance, you must securely capture sensitive payment data using a validated payment provider.
To meet this requirement, `Microform Integration` renders secure iframes for the payment information as follows:

* Card information input fields:
  * Payment card or PAN
  * CVN
* `eCheck` information input fields:
  * Routing number
  * Account number
    {#microform-integ-pci-comp-v2_ul_qb4_rz5_k2c}
    These iframes are hosted by `Microform Integration`, and the payment data is submitted directly to `Cybersource` through the secure Flex API v2 suite. This means that this data never passes through your systems.

Getting Started {#microform-integ-getting-started-v2}
=====================================================

`Microform Integration` replaces the primary account number (PAN) or card verification number (CVN) field, or both, in your payment input form. It has two components:

* Server-side component to create a capture context request that contains limited-use public keys from the `Flex API` v2 suite.
* Client-side JavaScript library that you integrate into your digital payment acceptance web page for the secure acceptance of payment information:
  * Card information input fields:
    * Payment card or PAN
    * CVN
  * `eCheck` information input fields:
    * Routing number
* Account number

Accept Card Information {#micro-getting-started-pay-card}
=========================================================

This section covers the implementation steps needed to complete the server-side and client-side setup for accepting card information with `Microform Integration`.
Implementing `Microform Integration` is a three-step process:

1. [Creating the Server-Side Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/creating-server-side-context-v2-card.md "")
2. [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-cs-setup.md "")
3. [Validating the Transient Token](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/validating-the-transient-token-pay-card.md "")
   This figure shows the flow for implementing `Microform Integration`:

#### Figure:

`Microform Integration` Implementation Workflow ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/flexible-token/images/microform-v2-overview-cybs.svg/jcr:content/renditions/original)

Server-Side Setup {#micro-getting-started-pay-card-ss-setup}
============================================================

This section contains the information you need to set up your server. Initializing `Microform Integration` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials and establishes how the `Microform Integration` front-end components will function. The sessions API request contains parameters that define how `Microform Integration` performs.
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

{#micro-getting-started-pay-card-ss-setup_d7e30}
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information about JWTs, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

Capture Context {#micro-capture-context-card-intro}
===================================================

The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the front-end JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Microform Integration`, in addition to allowed card networks and payment types (card or check).
These fields are available for requesting the capture context for accepting card information:

Required fields:
:
allowedCardNetworks
:
clientVersion
:
targetOrigins

Optional fields:
:
allowedPaymentTypes
:
transientTokenResponseOptions
For information about JWTs, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
For more information on requesting the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-capture-context-api-intro.md "").

Creating the Server-Side Capture Context {#creating-server-side-context-v2-card}
================================================================================

The first step in integrating with `Microform Integration` is to develop the server-side code that generates the capture context. The capture context is also known as a *session*.
You can use the SDK or call the API directly to generate the capture context.
To use the SDK to generate the capture context, use the sample code here: [Flex Samples on Github](https://github.com/CyberSource#flex-api-sample-applications "").
Follow these steps to call the API directly to generate the capture context:

1. Send an authenticated POST request to the `/sessions` endpoint to create your capture context session:

   * **Production** : `https://api.cybersource.com``/microform/v2/sessions`
   * **Test** : `https://apitest.cybersource.com``/microform/v2/sessions`

   Include the target origin URL and at least one accepted card type in the content of the body of the request. You must also include the type of `Microform Integration` you want to include in the capture context for accepting card information. If you do not include the **allowedPaymentTypes** field in your capture request, the value defaults to `CARD`.
   For example:

   ```
   {
   	"clientVersion": "v2",
   	"targetOrigins": ["https://www.example.com"],
   	"allowedCardNetworks": ["VISA"],
   	"allowedPaymentTypes": ["CARD"]
   }
   ```

   To embed the target origin URL within multiple nested iframes, you must specify the origins of all the browser contexts used. For example:

   ```
   {
   	"clientVersion": "v2",
   	"targetOrigins": ["https://www.example.com", "https://www.basket.example.com", "https://ecom.example.com"],
   	"allowedCardNetworks": ["VISA",
   		"MASTERCARD",
   		"AMEX",
   		"CARTESBANCAIRES",
   		"CARNET",
   		"CUP",
   		"DINERSCLUB",
   		"DISCOVER",
   		"EFTPOS",
   		"ELO",
                 "JAYWAN",
   		"JCB",
   		"JCREW",
                 "KSCP",
   		"MADA",
   		"MAESTRO",
   		"MEEZA",
                 "PAYPAK",
                 "UATP"
   	],
   	"allowedPaymentTypes": ["CARD"]
   }
   ```
2. Pass the capture context response data object to your front-end application. The capture context is valid for 15 minutes.
   **Successful Encrypted JWT Response**

   ```
   eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJ1Q0RERW94M2dDQk1VaHI2T1ZDVGt4QUFFS1pHSTRHcDFvQ2pyYXlVb1MxQzdGOXE2WFpyYXhGbGxMVDMvenE2cjFnNXoxS1U2UDZseldqRVFTVVJoZUtxUThoVWJkZVNNdmt5SERTTXUwV01tMzhcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoiMXNDY3NZNC1WZTNWU0VKekhnelJ5WjVDOURrM0VHZ2ZPOGd5SDc5bVJfSlN6NzdmWTdfV1loM3psdTkyTFVfeU5KVTBUMzdOQmVzd0szU2c0YnRNaU41Q0FCbWNXLWNSckhta2k0MVZoNUZRMmtjcWZSSlgxNVhZN1A3R25GTnd4QzVkUG9UM29NM1czRFVHaUMyYW56enhIN3pNNlA3N2hFbnc2TkZHSXlBdXhJRWFwRG9DaXlEVW5NdFRwV2lBV3YzTF9OVHZOaHRkVE4tNm1GRWU1RmdVYmlzeWtrTzlWMHZaS0d6SWRWWmdTdE42cHlnUGhVbnlNXzJIVmIxQmkyWjNKaElhZDFLUW02SGl0NklwYjNyUTBHRWZsN0ZWOUV3NGZyNzJpekQ0WVg2WHo0V3ZuMzlLN3J3WkhCRXdNM3l5Wl9ELTBUbjM1MFhvUlBUVjB3Iiwia2lkIjoiMDB4V1A1eUh1UE1kNkFkNHdwVzNzQkt1bWFaQ01zYWMifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIiwiTUFFU1RSTyIsIkRJU0NPVkVSIiwiRElORVJTQ0xVQiIsIkpDQiIsIkNVUCIsIkNBUlRFU0JBTkNBSVJFUyJdLCJ0YXJnZXRPcmlnaW5zIjpbImh0dHBzOi8vdGhlLXVwLWRlbW8uYXBwc3BvdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJhbGxvd2VkUGF5bWVudFR5cGVzIjpbIkNBUkQiXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzY0MzA0MTQsImlhdCI6MTczNjQyOTUxNCwianRpIjoiZDVZbzVhNU0wWFBPQ1BxZiJ9.G4Ea-gIk6SG5ULE4NE5OsdPI41YaAuTEMHDstBgkFzczIWwzJScvXs4hgWiyA-1ZLGITedlumGj-0x8jxmYTWeTm7D0fP8RL0w148EpDLMD8xMHpAJMdMqZTmYHyichsy8uOZKVOn9NbnuQqfDeQS_rLpJV3tMe2NwJL3RdBXdJ894ihKpFP2yXE1wQeLekNiYJ6s-Uuxwf0jf2CSN_TJAjnfVR6bqlpWbUpiUaBLcqDsHHe_pcrd5g2r-1LEfCiOV9RIw7844XKFNLQZvt_alQjItuMy8M9LVhnlRWCSnTKB1iV1RUxuTWtMzTvHmQWPx4nShqzE3j0Hp61c0PmBw
   ```

#### AFTER COMPLETING THE TASK

> IMPORTANT
>
> * Ensure that all endpoints within your ownership are secure with some kind of authentication so they cannot be called at will by bad actors.

* Do not pass the ` targetOrigin ` field in any external requests. Hard code it on the server side.
  For more information on requesting the capture context, see [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-ss-setup/micro-capture-context-card-intro.md "").

Validating the Server-Side Capture Context {#validate-capture-context-microv2-card}
===================================================================================

The capture context that you generated is a JSON Web Token (JWT) data object. The JWT is digitally signed using a public key. The purpose is to ensure the validity of the JWT and confirm that it comes from `Cybersource`. When you do not have a key specified locally in the JWT header, you should follow best cryptography practices and validate the capture context signature.
To validate a JWT, you can obtain its public key. This public RSA key is in JSON Web Key (JWK) format. This public key is associated with the capture context on the `Cybersource` domain.
To get the public key of a capture context from the header of the capture context itself, retrieve the key ID associated with the public key. Then, pass the key ID to the `public-keys` endpoint.
**Example**
From the header of the capture context, get the key ID (`kid`) as shown in this example:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Append the key ID to the endpoint `/flex/v2/public-keys/`**3g**. Then, call this endpoint to get the public key. IMPORTANT

> Depending on the cryptographic method you use to validate the public key, you might need to convert the key to privacy-enhanced mail (PEM) format. {#validate-capture-context-microv2-card_d23e59}

Resource
--------

Pass the key ID (kid), that you obtained from the capture context header, as a path parameter, and send a GET request to the `/public-keys` endpoint:

* Test: `https://apitest.cybersource.com``/flex/v2/public-keys/`*{kid}*
* Production: `https://api.cybersource.com``/flex/v2/public-keys/`*{kid}*

The resource returns the public key. Use this public RSA key to validate the capture context.

Example {#validate-capture-context-microv2-card_validate-capture-context-example}
---------------------------------------------------------------------------------

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJ1Q0RERW94M2dDQk1VaHI2T1ZDVGt4QUFFS1pHSTRHcDFvQ2pyYXlVb1MxQzdGOXE2WFpyYXhGbGxMVDMvenE2cjFnNXoxS1U2UDZseldqRVFTVVJoZUtxUThoVWJkZVNNdmt5SERTTXUwV01tMzhcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoiMXNDY3NZNC1WZTNWU0VKekhnelJ5WjVDOURrM0VHZ2ZPOGd5SDc5bVJfSlN6NzdmWTdfV1loM3psdTkyTFVfeU5KVTBUMzdOQmVzd0szU2c0YnRNaU41Q0FCbWNXLWNSckhta2k0MVZoNUZRMmtjcWZSSlgxNVhZN1A3R25GTnd4QzVkUG9UM29NM1czRFVHaUMyYW56enhIN3pNNlA3N2hFbnc2TkZHSXlBdXhJRWFwRG9DaXlEVW5NdFRwV2lBV3YzTF9OVHZOaHRkVE4tNm1GRWU1RmdVYmlzeWtrTzlWMHZaS0d6SWRWWmdTdE42cHlnUGhVbnlNXzJIVmIxQmkyWjNKaElhZDFLUW02SGl0NklwYjNyUTBHRWZsN0ZWOUV3NGZyNzJpekQ0WVg2WHo0V3ZuMzlLN3J3WkhCRXdNM3l5Wl9ELTBUbjM1MFhvUlBUVjB3Iiwia2lkIjoiMDB4V1A1eUh1UE1kNkFkNHdwVzNzQkt1bWFaQ01zYWMifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIiwiTUFFU1RSTyIsIkRJU0NPVkVSIiwiRElORVJTQ0xVQiIsIkpDQiIsIkNVUCIsIkNBUlRFU0JBTkNBSVJFUyJdLCJ0YXJnZXRPcmlnaW5zIjpbImh0dHBzOi8vdGhlLXVwLWRlbW8uYXBwc3BvdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJhbGxvd2VkUGF5bWVudFR5cGVzIjpbIkNBUkQiXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzY0MzA0MTQsImlhdCI6MTczNjQyOTUxNCwianRpIjoiZDVZbzVhNU0wWFBPQ1BxZiJ9.G4Ea-gIk6SG5ULE4NE5OsdPI41YaAuTEMHDstBgkFzczIWwzJScvXs4hgWiyA-1ZLGITedlumGj-0x8jxmYTWeTm7D0fP8RL0w148EpDLMD8xMHpAJMdMqZTmYHyichsy8uOZKVOn9NbnuQqfDeQS_rLpJV3tMe2NwJL3RdBXdJ894ihKpFP2yXE1wQeLekNiYJ6s-Uuxwf0jf2CSN_TJAjnfVR6bqlpWbUpiUaBLcqDsHHe_pcrd5g2r-1LEfCiOV9RIw7844XKFNLQZvt_alQjItuMy8M9LVhnlRWCSnTKB1iV1RUxuTWtMzTvHmQWPx4nShqzE3j0Hp61c0PmBw
```

Parse the JWT capture context to get the key ID (`kid`) from its header:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Get its public key from `/flex/v2/public-keys/3g`:

```
{
    "kty":"RSA",
    "use":"enc",
    "kid":"3g",
    "n":"ir7Nl1Bj8G9rxr3co5v_JLkP3o9UxXZRX1LIZFZeckguEf7Gdt5kGFFfTsymKBesm3Pe
     8o1hwfkq7KmJZEZSuDbiJSZvFBZycK2pEeBjycahw9CqOweM7aKG2F_bhwVHrY4YdKsp
     _cSJe_ZMXFUqYmjk7D0p7clX6CmR1QgMl41Ajb7NHI23uOWL7PyfJQwP1X8HdunE6ZwK
     DNcavqxOW5VuW6nfsGvtygKQxjeHrI-gpyMXF0e_PeVpUIG0KVjmb5-em_Vd2SbyPNme
     nADGJGCmECYMgL5hEvnTuyAybwgVwuM9amyfFqIbRcrAIzclT4jQBeZFwkzZfQF7MgA6QQ",
     "e":"AQAB"
}
```

Related Information
-------------------

* [*Introduction to JSON Web Tokens*](https://jwt.io/introduction "")
* [IETF RFC 7515: JSON Web Signature (JWS) Signature](https://tools.ietf.org/html/rfc7515 "")
* [IETF RFC 7517: JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517 "")

Client-Side Setup {#micro-getting-started-pay-card-cs-setup}
============================================================

You can integrate `Microform Integration` with your native payment acceptance web page or mobile application.

Web Page {#setting-up-client-side-v2-web-card-task1}
----------------------------------------------------

Initiate and embed `Microform Integration` into your payment acceptance web page.

1. Decode the JWT from the `/microform/v2/sessions` response to get the capture context.

2. Use the clientLibrary and clientLibraryIntegrity values that are returned in the JWT from `/microform/v2/sessions` response to obtain the `Microform Integration` JavaScript library URL and integrity value that you use to create your script tags.

   > IMPORTANT You must use these values for every transaction. These values can be unique for each transaction.
   > IMPORTANT
   > Do not hard code these values, because doing so can result in client-side ` Microform Integration ` errors. If you do not hard code these values for all transactions, you can load a JavaScript library that is incompatible with the version you requested in the ` /sessions ` request.
   > **Example `/sessions` Response:**

   ```
   "data":{ "clientLibrary":"[EXTRACT clientLibrary VALUE from here]", "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]" }
   ```

   **Example Script Tags**

   ```
   &lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt; &lt;/script&gt;
   ```

   **Example Code for Loading the Script Dynamically Following JWT Extraction Tags**

   ```
   // values read from capture context
   const clientLibrary = " ";
   const clientLibraryIntegrity = " ";
   // create script tag
   const script = document.createElement("script");
   script.src = clientLibrary;
   script.type = "text/javascript";
   script.async = true;
   script.integrity = clientLibraryIntegrity;
   script.crossOrigin = "anonymous";
   // run setup code after script has loaded successfully
   script.onload = function () {
     // SETUP
   };
   // insert to document
   document.head.appendChild(script);
   ```
3. Create the HTML placeholder objects to attach to the microforms.
   `Microform Integration` attaches the microform fields to containers within your HTML. Within your HTML checkout, replace the payment card and CVN tag with a simple container. `Microform Integration` uses the container to render an iframe for secured credit card input. This example contains simple `div` tags to define where to place the PAN and CVN fields within the payment acceptance page: `&lt;div id="number-container" class="form-control"&gt;&lt;/div&gt;`.
   **Example: Accept Card Information Checkout Form**

   ```
   &lt;h1&gt;Checkout Page&lt;/h1&gt;
   &lt;div id="errors-output" role="alert"&gt;&lt;/div&gt;
   &lt;form action="/token" id="my-sample-form" method="post"&gt;
       &lt;div class="form-group"&gt;
           &lt;label for="cardholderName"&gt;Name&lt;/label&gt;
           &lt;input id="cardholderName" class="form-control" name="cardholderName" placeholder="Name on the card"&gt;
           &lt;label id="cardNumber-label"&gt;Card Number&lt;/label&gt;
           &lt;div id="number-container" class="form-control"&gt;&lt;/div&gt;
           &lt;label for="securityCode-container"&gt;Security Code&lt;/label&gt;
           &lt;div id="securityCode-container" class="form-control"&gt;&lt;/div&gt;
       &lt;/div&gt;

       &lt;div class="form-row"&gt;
           &lt;div class="form-group col-md-6"&gt;
               &lt;label for="expMonth"&gt;Expiry month&lt;/label&gt;
               &lt;select id="expMonth" class="form-control"&gt;
                   &lt;option&gt;01&lt;/option&gt;
                   &lt;option&gt;02&lt;/option&gt;
                   &lt;option&gt;03&lt;/option&gt;
                   &lt;option&gt;04&lt;/option&gt;
                   &lt;option&gt;05&lt;/option&gt;
                   &lt;option&gt;06&lt;/option&gt;
                   &lt;option&gt;07&lt;/option&gt;
                   &lt;option&gt;08&lt;/option&gt;
                   &lt;option&gt;09&lt;/option&gt;
                   &lt;option&gt;10&lt;/option&gt;
                   &lt;option&gt;11&lt;/option&gt;
                   &lt;option&gt;12&lt;/option&gt;
               &lt;/select&gt;
           &lt;/div&gt;
           &lt;div class="form-group col-md-6"&gt;
               &lt;label for="expYear"&gt;Expiry year&lt;/label&gt;
               &lt;select id="expYear" class="form-control"&gt;
                   &lt;option&gt;2021&lt;/option&gt;
                   &lt;option&gt;2022&lt;/option&gt;
                   &lt;option&gt;2023&lt;/option&gt;
               &lt;/select&gt;
           &lt;/div&gt;
       &lt;/div&gt;

       &lt;button type="button" id="pay-button" class="btn btn-primary"&gt;Pay&lt;/button&gt;
       &lt;input type="hidden" id="flexresponse" name="flexresponse"&gt;
   &lt;/form&gt;
   ```
4. Invoke the Flex SDK by passing the capture context that was generated in the previous step to the microform object.
   `const flex = new Flex(captureContext);`

5. Initiate the microform object with styling to match your web page.
   After you create a new Flex object, you can begin creating your Microform. You will pass your baseline styles and ensure that the button matches your merchant page:
   `const microform = flex.microform("card", { styles: myStyles });`

6. Create and attach the microform fields to the HTML objects through the Microform Integration JavaScript library.

   ```
   const number = microform.createField('number', { placeholder: 'Enter card number' });
   const securityCode = microform.createField('securityCode', { placeholder: '•••' });
               number.load('#number-container');
               securityCode.load('#securityCode-container');
   ```
7. Create a function for the customer to submit their payment information, and invoke the tokenization request to `Microform Integration` for the transient token.
   {#setting-up-client-side-v2-web-card-task1_setting-up-client-side-v2-steps}

Mobile Application {#setting-up-client-side-v2-web-mobile-task2}
----------------------------------------------------------------

To initiate and embed `Microform Integration` into a native payment acceptance mobile application, follow the steps for web page set up, and ensure that these additional requirements are met:

* The card information acceptance fields of PAN and CVV must be hosted on a web page.
* The `eCheck` information acceptance fields of routing number, account number, and confirmed account number must be hosted on a web page.
* The native application must load the hosted card entry form web page in a web view.

Transient Tokens for Accepting Card Information {#micro-getting-started-pay-card-trans-tkn}
===========================================================================================

The response to a successful customer interaction with `Microform Integration` is a transient token. The transient token is a reference to the payment data that is collected on your behalf. Tokens allow secure card or check payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.

Transient Token Time Limit {#transient-token-time-limit-pay-card_time-limit}
============================================================================

The sensitive data associated with the transient token is available for use in API requests for a 15-minute duration. The transient token can be used multiple times within the 15-minute period. After 15 minutes, you must prompt the customer to restart the checkout flow.
**Example: Creating the Pay Button with Event Listener for Accepting Card Information**

```
const button = document.querySelector("#myButton");

button.addEventListener("click", function () {
  // Compiling MM & YY into optional parameters
  const options = {
    expirationMonth: document.querySelector("#expMonth").value,
    expirationYear: document.querySelector("#expYear").value,
  };
  //
  microform.createToken(options, function (err, token) {
    // handle err
    if (err) {
      console.error(err);
      errorsOutput.textContent = err.message;
      return;
    }

    // At this point you may pass the token back to your server as you wish.
    // In this example we append a hidden input to the form and submit it.
    console.log(JSON.stringify(token));
    flexResponse.value = JSON.stringify(token);
    form.submit();
  });
});
```

When the customer submits the form, `Microform Integration` securely collects and tokenizes the data in the loaded fields as well as the options supplied to the `createToken()` function. The Account Type is included in the request. If tokenization succeeds, your callback receives the token as its second parameter. Send the token to your server, and use it in place of the card information when you use supported payment services.
**Example: Customer-Submitted Form for Accepting Card Information**

```
&lt;script&gt;
    // Variables from the HTML form
    const form = document.querySelector('#my-sample-form');
    const payButton = document.querySelector('#pay-button');
    const flexResponse = document.querySelector('#flexresponse');
    const expMonth = document.querySelector('#expMonth');
    const expYear = document.querySelector('#expYear');
    const errorsOutput = document.querySelector('#errors-output');

    // the capture context that was requested server-side for this transaction
    const captureContext = &lt;% -keyInfo %&gt; ;
    // custom styles that will be applied to each field we create using Microform
    const myStyles = {
        'input': {
            'font-size': '14px',
            'font-family': 'helvetica, tahoma, calibri, sans-serif',
            'color': '#555'
        },
        ':focus': { 'color': 'blue' },
        ':disabled': { 'cursor': 'not-allowed' },
        'valid': { 'color': '#3c763d' },
        'invalid': { 'color': '#a94442' }
    };
    // setup Microform
    const flex = new Flex(captureContext);
    const microform = flex.microform({ styles: myStyles });
    const number = microform.createField('number', { placeholder: 'Enter card number' });
    const securityCode = microform.createField('securityCode', { placeholder: '•••' });
    number.load('#number-container');
    securityCode.load('#securityCode-container');


    // Configuring a Listener for the Pay button
    payButton.addEventListener('click', function () {

        // Compiling MM & YY into optional parameters
        const options = {
            expirationMonth: document.querySelector('#expMonth').value,
            expirationYear: document.querySelector('#expYear').value
        };
        //
        microform.createToken(options, function (err, token) {
            if (err) {
                // handle error
                console.error(err);
                errorsOutput.textContent = err.message;
            } else {
                // At this point you may pass the token back to your server as you wish.
                // In this example we append a hidden input to the form and submit it.
                console.log(JSON.stringify(token));
                flexResponse.value = JSON.stringify(token);
                form.submit();
            }
        });
    });
&lt;/script&gt;
```

Transient Token Response Format {#transient-token-response-format-pay-card}
===========================================================================

The transient token is issued as a JSON Web Token ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). A JWT is a string consisting of three parts that are separated by dots:

* Header
* Payload
* Signature
  {#transient-token-response-format-pay-card_ul_lvk_ksf_4nb}
  JWT example: `xxxxx.yyyyy.zzzzz`
  The payload portion of the token is an encoded Base64url JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

> IMPORTANT
> When you integrate with ` Cybersource ` APIs, ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for. Additional fields may be added in the future.
> You must ensure that your integration can handle new fields that are returned in the response. While the underlying data structures will not change, you must also ensure that your integration can handle changes to the order in which the data is returned.
> The internal data structure of the JWT can expand to contain additional data elements. Ensure that your integration and validation rules do not limit the data elements contained in responses.
> **Example: Token Payload for Accepting Card Information**

```
{
  "iss": "Flex/00",
  "exp": 1728911080,
  "type": "mf-2.0.0",
  "iat": 1728910180,
  "jti": "1D1S6JK9RL6EK667H1I370689A63I2I8YLFJSPJ1EUSKIPMJJWEL670D16E89AF8",
  "content": {
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2025"
        },
        "number": {
          "detectedCardTypes": [
            "001"
          ],
          "maskedValue": "XXXXXXXXXXXX1111",
          "bin": "411111"
        },
        "securityCode": {},
        "expirationMonth": {
          "value": "01"
        }
      }
    }
  }
}
```

Validating the Transient Token {#validating-the-transient-token-pay-card}
=========================================================================

After receiving the transient token, validate its integrity using the public key embedded within the capture context created at the beginning of this flow. This verifies that `Cybersource` issued the token and that no data tampering occurred during transit.
**Example: Capture Context Public Key**

```
"jwk": {
                "kty": "RSA",
                "e": "AQAB",
                "use": "enc",
                "n": "3DhDtIHLxsbsSygEAG1hcFqnw64khTIZ6w9W9mZNl83gIyj1FVk-H5GDMa85e8RZFxUwgU_zQ0kHLtONo8SB52Z0hsJVE9wqHNIRoloiNPGPQYVXQZw2S1BSPxBtCEjA5x_-bcG6aeJdsz_cAE7OrIYkJa5Fphg9_pxgYRod6JCFjgdHj0iDSQxtBsmtxagAGHjDhW7UoiIig71SN-f-gggaCpITem4zlb5kkRVvmKMUANe4B36v4XSSSpwdP_H5kv4JDz_cVlp_Vy8T3AfAbCtROyRyH9iH1Z-4Yy6T5hb-9y3IPD8vlc8E3JQ4qt6U46EeiKPH4KtcdokMPjqiuQ",
                "kid": "00UaBe20jy9VkwZUQPZwNNoKFPJA4Qhc"    }
```

Use the capture context public key to cryptographically validate the JWT provided from a successful `microform.createToken` call. You might have to convert the JSON Web Key (JWK) to privacy-enhanced mail (PEM) format for compatibility with some JWT validation software libraries.
The `Cybersource` SDK has functions that verify the token response. You must verify the response to ensure that no tampering occurs as it passes through the cardholder device. Do so by using the public key generated at the start of the process.

Using the Transient Token to Process a Payment {#using-transient-token-pay-card}
================================================================================

After you validate the transient token, you can use it in place of the PAN with payment services for 15 minutes. The transient token can be used multiple times within the 15-minute period.
When the consuming service receives a request containing a transient token, it retrieves the tokenized data and injects the values into your request before processing, and none of the sensitive data is stored on your systems. In some scenarios, the `jti` value contained in the JWT transient token response must be extracted and used instead of the entire JWT.

| Connection Method                            | Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:---------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simple Order API                             | tokenSource_transientToken                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SCMP API                                     | transient_token                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| REST API with Transient Token JSON Web Token | "tokenInformation": { "transientTokenJwt": "eyJraWQiOiIwNzRsM3p5M2xCRWN5d1gxcnhXNFFoUmJFNXJLN1NmQiIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjp7ImV4cGlyYXRpb25ZZWFyIjoiMjAyMSIsIm51bWJlciI6IjQxMTExMVhYWFhYWDExMTEiLCJleHBpcmF0aW9uTW9udGgiOiIwNSIsInR5cGUiOiIwMDEifSwiaXNzIjoiRmxleC8wOCIsImV4cCI6MTU4ODcwMjkxNSwidHlwZSI6Im1mLTAuMTEuMCIsImlhdCI6MTU4ODcwMjAxNSwianRpIjoiMUU0Q0NMSUw4NFFXM1RPSTFBM0pUU1RGMTZGQUNVNkUwNU9VRVNGWlRQNUhIVkJDWTQwUTVFQjFBRUMzNDZBMCJ9.FB3b2r8mjtvqo3_k05sRIPGmCZ_5dRSZp8AIJ4u7NKb8E0-6ZOHDwEpxtOMFzfozwXMTJ3C6yBK9vFIPTIG6kydcrWNheE2Pfort8KbxyUxG-PYONY-xFnRDF841EFhCMC4nRFvXEIvlcLnSK6opUUe7myKPjpZI1ijWpF0N-DzZiVT8JX-9ZIarJq2OI0S61Y3912xLJUKi5c2VpRPQOS54hRr5GHdGJ2fV8JZ1gTuup_qLyyK7uE1VxI0aucsyH7yeF5vTdjgSd76ZJ1OUFi-3Ij5kSLsiX4j-D0T8ENT1DbB_hPTaK9o6qqtGJs7QEeW8abtnKFsTwVGrT32G2w" } |
| REST API with JSON Web Token ID              | "tokenInformation": { "jti": "1E3GQY1RNKBG6IBD2EP93C43PIZ2NQ6SQLUIM3S16BGLHTY4IIEK5EB1AE5D73A4", }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**Example: Authorization with a Transient Token Using the REST API**

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "102.21",
            "currency": "USD"
        },
        "billTo": {
            "firstName": "Tanya",
            "lastName": "Lee",
            "address1": "1234 Main St.",
            "locality": "Small Town",
            "administrativeArea": "MI",
            "postalCode": "98765-4321",
            "country": "US",
            "district": "MI",
            "buildingNumber": "123",
            "email": "tanyalee@example.com",
            "phoneNumber": "987-654-3210"
        }
    },
    "tokenInformation": {
        "transientTokenJwt": "eyJraWQiOiIwN0JwSE9abkhJM3c3UVAycmhNZkhuWE9XQlhwa1ZHTiIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjp7ImV4cGlyYXRpb25ZZWFyIjoiMjAyMCIsIm51bWJlciI6IjQxMTExMVhYWFhYWDExMTEiLCJleHBpcmF0aW9uTW9udGgiOiIxMCIsInR5cGUiOiIwMDEifSwiaXNzIjoiRmxleC8wNyIsImV4cCI6MTU5MTc0NjAyNCwidHlwZSI6Im1mLTAuMTEuMCIsImlhdCI6MTU5MTc0NTEyNCwianRpIjoiMUMzWjdUTkpaVjI4OVM5MTdQM0JHSFM1T0ZQNFNBRERCUUtKMFFKMzMzOEhRR0MwWTg0QjVFRTAxREU4NEZDQiJ9.cfwzUMJf115K2T9-wE_A_k2jZptXlovls8-fKY0muO8YzGatE5fu9r6aC4q7n0YOvEU6G7XdH4ASG32mWnYu-kKlqN4IY_cquRJeUvV89ZPZ5WTttyrgVH17LSTE2EvwMawKNYnjh0lJwqYJ51cLnJiVlyqTdEAv3DJ3vInXP1YeQjLX5_vF-OWEuZfJxahHfUdsjeGhGaaOGVMUZJSkzpTu9zDLTvpb1px3WGGPu8FcHoxrcCGGpcKk456AZgYMBSHNjr-pPkRr3Dnd7XgNF6shfzIPbcXeWDYPTpS4PNY8ZsWKx8nFQIeROMWCSxIZOmu3Wt71KN9iK6DfOPro7w"
    }
}
```

Accept `eCheck` Information {#micro-getting-started-pay-bank}
=============================================================

This section covers the implementation steps needed to complete the server-side and client-side setup for accepting `eCheck` information with `Microform Integration`.
Implementing `Microform Integration` is a three-step process:

1. [Creating the Server-Side Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-ss-setup/creating-server-side-context-v2-bank.md "")
2. [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "")
3. [Validating the Transient Token](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/validating-the-transient-token-pay-bank.md "")
   This figure shows the flow for implementing `Microform Integration`:

#### Figure:

`Microform Integration` Implementation Workflow ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/flexible-token/images/microform-v2-overview-cybs.svg/jcr:content/renditions/original)

Server-Side Setup {#micro-getting-started-pay-bank-ss-setup}
============================================================

This section contains the information you need to set up your server. Initializing `Microform Integration` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials and establishes how the `Microform Integration` front-end components will function. The sessions API request contains parameters that define how `Microform Integration` performs.
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

{#micro-getting-started-pay-bank-ss-setup_d7e30}
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information about JWTs, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

Capture Context {#micro-capture-context-bank-intro}
===================================================

The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the front-end JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Microform Integration`, in addition to allowed card networks and payment types.
These fields are available for requesting the capture context for accepting eCheck information:

Required fields:
:
allowedPaymentTypes
:
clientVersion
:
targetOrigins

Optional fields:
:
allowedCardNetworks
:
transientTokenResponseOptions
For information about JWTs, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
For more information on requesting the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/flex-capture-context-api-intro.md "").

Creating the Server-Side Capture Context {#creating-server-side-context-v2-bank}
================================================================================

The first step in integrating with `Microform Integration` is to develop the server-side code that generates the capture context. The capture context is also known as a session.
You can use the SDK or call the API directly to generate the capture context.
To use the SDK to generate the capture context, use the sample code here: [Flex Samples on Github](https://github.com/CyberSource#flex-api-sample-applications "").
Follow these steps to call the API directly to generate the capture context:

1. Send an authenticated POST request to the `/sessions` endpoint to create your capture context session:

   * **Production** : `https://api.cybersource.com``/microform/v2/sessions`
   * **Test** : `https://apitest.cybersource.com``/microform/v2/sessions`

   Include the target origin URL and at least one accepted card type in the content of the body of the request. You must also include the type of `Microform Integration` you want to include in the capture context for accepting `eCheck` information. If you do not include the **allowedPaymentTypes** field in your capture request, the value defaults to `CARD`.
   For example:

   ```
   {
   	"clientVersion": "v2",
   	"targetOrigins": [
   		"https://www.example.com"
   	],
   	"allowedCardNetworks": [
   		"VISA"
   	],
   	"allowedPaymentTypes": [
   		"CHECK"
   	]
   }
   ```

   To embed within multiple nested iframes, you must specify the origins of all the browser contexts used. For example:

   ```
   {
   	"clientVersion": "v2",
   	"targetOrigins": [
   		"https://www.example.com",
   		"https://www.basket.example.com",
   		"https://ecom.example.com"
   	],
   	"allowedCardNetworks": [
   		"VISA",
   		"MASTERCARD",
   		"AMEX",
   		"CARTESBANCAIRES",
   		"CARNET",
   		"CUP",
   		"DINERSCLUB",
   		"DISCOVER",
   		"EFTPOS",
   		"ELO",
   		"JCB",
   		"JCREW",
   		"MADA",
   		"MAESTRO",
   		"MEEZA",
                 "PAYPAK"
   	],
   	"allowedPaymentTypes": [
   		"CHECK"
   	]
   }
   ```
2. Pass the capture context response data object to your front-end application. The capture context is valid for 15 minutes.
   **Successful Encrypted JWT Response**

   ```
   eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJtdnkwVk9OVk40bzA4bTRGQjhmU3FCQUFFS0JWOTdlNnR2VDd4cHdqaFkwMDRydFJ1dGI0R2YwWlNwNGdNeEkvanBVSWxFblZKa2JtUVNHaWFnUEdGc0NPazdMbHJGTHFKcXN2eitoTHhrY08xRkFcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoidmRpN0gtM1MzMTkyZlc5WC1BTmpvdjlFdXU4ZGxPOTBtU2gyUGVyMF9PdHZ4YlJITTBrakZpTHlKaGQwUUR3VlNWbUlhRFc2aGtCa1k2Ui1lcWRnaTdUVUNGZEQ3UUU1ckNkZGhZZTIycTh0RUNQZkpOWWJ6STZZTVBxTkFyYWc5LUhhWVo1X2tOX0JvMm5EclN4RFJ0MHBDbGxyd2d2Q1ZLb2M0RWF6ZE93QUE4dnI2VVh4Ty1SWVI2Z1R5VEZia244Q2hDVHNvWDByam5VWVI1VjdRaE95YzMzWEJUTVNDYTVBOHFQNDZnZXpvQjZ0dDA0SlQtRVVMWE9vYndVcVdvd0E3TTJzWUYydkFoQkVuMmt0REJFWVJSN3E0aWEyVHRIS1JPUW9FTjhZNjNiNFNaTGZDQk82cEc2QXpnSWpya3RkQXhIOXR0WURYdFJYS1YxeTN3Iiwia2lkIjoiMDBiQlN1d3VpdGtYeExROGFISWloMm5qMFhQNFpXYUsifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsInRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly90aGUtdXAtZGVtby5hcHBzcG90LmNvbSJdLCJtZk9yaWdpbiI6Imh0dHBzOi8vc3RhZ2VmbGV4LmN5YmVyc291cmNlLmNvbSIsImFsbG93ZWRQYXltZW50VHlwZXMiOlsiQ0hFQ0siXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzM0OTAxODEsImlhdCI6MTczMzQ4OTI4MSwianRpIjoiSXdEdHAxZkVZM2QwYUh6OSJ9.arokacvdTSUIehBY0ICi-QYynhFj7_0k-G39qbkNJydB3UyF2qJSaqwZiopO27kuqk8u9Z0cY-V9Nu04JgaV4s18doxnzx6vdTCC3krrIcxeINi23Qu-Szcpg7aaGvPVXMC0DVC14WUQiGJkOakJ54jWtl2VoFAgYziUMcYYpk4hxLVxurBtT7lvrfCXKoyWtxiUxoEpOc_Td_qi5nA8ByWUaieQmp1Zej61khQJ_hmXtlsAt4BqxeJWoJeR_5Sjz0vD5y4-oAeNNrAulDem7CKiRJQbI9fyqT-
   ```

#### AFTER COMPLETING THE TASK

**Important Security Note:**

* Ensure that all endpoints within your ownership are secure with some kind of authentication so they cannot be called at will by bad actors.
* Do not pass the `targetOrigin` in any external requests. Hard code it on the server side.

{#creating-server-side-context-v2-bank_ul_csl_pyx_pnb}
For more information on requesting the capture context, see [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-ss-setup/micro-capture-context-bank-intro.md "").

Validating the Server-Side Capture Context {#validate-capture-context-microv2-bank}
===================================================================================

The capture context that you generated is a JSON Web Token (JWT) data object. The JWT is digitally signed using a public key. The purpose is to ensure the validity of the JWT and confirm that it comes from `Cybersource`. When you do not have a key specified locally in the JWT header, you should follow best cryptography practices and validate the capture context signature.
To validate a JWT, you can obtain its public key. This public RSA key is in JSON Web Key (JWK) format. This public key is associated with the capture context on the `Cybersource` domain.
To get the public key of a capture context from the header of the capture context itself, retrieve the key ID associated with the public key. Then, pass the key ID to the `public-keys` endpoint.
**Example**
From the header of the capture context, get the key ID (`kid`) as shown in this example:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Append the key ID to the endpoint `/flex/v2/public-keys/`**3g**. Then, call this endpoint to get the public key. IMPORTANT

> Depending on the cryptographic method you use to validate the public key, you might need to convert the key to privacy-enhanced mail (PEM) format. {#validate-capture-context-microv2-bank_d23e59}

Resource
--------

Pass the key ID (kid), that you obtained from the capture context header, as a path parameter, and send a GET request to the `/public-keys` endpoint:

* Test: `https://apitest.cybersource.com``/flex/v2/public-keys/`*{kid}*
* Production: `https://api.cybersource.com``/flex/v2/public-keys/`*{kid}*

The resource returns the public key. Use this public RSA key to validate the capture context.

Example {#validate-capture-context-microv2-bank_validate-capture-context-example}
---------------------------------------------------------------------------------

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJtdnkwVk9OVk40bzA4bTRGQjhmU3FCQUFFS0JWOTdlNnR2VDd4cHdqaFkwMDRydFJ1dGI0R2YwWlNwNGdNeEkvanBVSWxFblZKa2JtUVNHaWFnUEdGc0NPazdMbHJGTHFKcXN2eitoTHhrY08xRkFcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoidmRpN0gtM1MzMTkyZlc5WC1BTmpvdjlFdXU4ZGxPOTBtU2gyUGVyMF9PdHZ4YlJITTBrakZpTHlKaGQwUUR3VlNWbUlhRFc2aGtCa1k2Ui1lcWRnaTdUVUNGZEQ3UUU1ckNkZGhZZTIycTh0RUNQZkpOWWJ6STZZTVBxTkFyYWc5LUhhWVo1X2tOX0JvMm5EclN4RFJ0MHBDbGxyd2d2Q1ZLb2M0RWF6ZE93QUE4dnI2VVh4Ty1SWVI2Z1R5VEZia244Q2hDVHNvWDByam5VWVI1VjdRaE95YzMzWEJUTVNDYTVBOHFQNDZnZXpvQjZ0dDA0SlQtRVVMWE9vYndVcVdvd0E3TTJzWUYydkFoQkVuMmt0REJFWVJSN3E0aWEyVHRIS1JPUW9FTjhZNjNiNFNaTGZDQk82cEc2QXpnSWpya3RkQXhIOXR0WURYdFJYS1YxeTN3Iiwia2lkIjoiMDBiQlN1d3VpdGtYeExROGFISWloMm5qMFhQNFpXYUsifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsInRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly90aGUtdXAtZGVtby5hcHBzcG90LmNvbSJdLCJtZk9yaWdpbiI6Imh0dHBzOi8vc3RhZ2VmbGV4LmN5YmVyc291cmNlLmNvbSIsImFsbG93ZWRQYXltZW50VHlwZXMiOlsiQ0hFQ0siXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzM0OTAxODEsImlhdCI6MTczMzQ4OTI4MSwianRpIjoiSXdEdHAxZkVZM2QwYUh6OSJ9.arokacvdTSUIehBY0ICi-QYynhFj7_0k-G39qbkNJydB3UyF2qJSaqwZiopO27kuqk8u9Z0cY-V9Nu04JgaV4s18doxnzx6vdTCC3krrIcxeINi23Qu-Szcpg7aaGvPVXMC0DVC14WUQiGJkOakJ54jWtl2VoFAgYziUMcYYpk4hxLVxurBtT7lvrfCXKoyWtxiUxoEpOc_Td_qi5nA8ByWUaieQmp1Zej61khQJ_hmXtlsAt4BqxeJWoJeR_5Sjz0vD5y4-oAeNNrAulDem7CKiRJQbI9fyqT-
```

Parse the JWT capture context to get the key ID (`kid`) from its header:

```
{
  "kid": "3g",
  "alg": "RS256"
}
```

Get its public key from `/flex/v2/public-keys/3g`:

```
{
    "kty":"RSA",
    "use":"enc",
    "kid":"3g",
    "n":"ir7Nl1Bj8G9rxr3co5v_JLkP3o9UxXZRX1LIZFZeckguEf7Gdt5kGFFfTsymKBesm3Pe
     8o1hwfkq7KmJZEZSuDbiJSZvFBZycK2pEeBjycahw9CqOweM7aKG2F_bhwVHrY4YdKsp
     _cSJe_ZMXFUqYmjk7D0p7clX6CmR1QgMl41Ajb7NHI23uOWL7PyfJQwP1X8HdunE6ZwK
     DNcavqxOW5VuW6nfsGvtygKQxjeHrI-gpyMXF0e_PeVpUIG0KVjmb5-em_Vd2SbyPNme
     nADGJGCmECYMgL5hEvnTuyAybwgVwuM9amyfFqIbRcrAIzclT4jQBeZFwkzZfQF7MgA6QQ",
     "e":"AQAB"
}
```

Client-Side Setup {#micro-getting-started-pay-bank-cs-setup}
============================================================

You can integrate `Microform Integration` with your native payment acceptance web page or mobile application.

Web Page {#setting-up-client-side-v2-web-bank-task1}
----------------------------------------------------

Initiate and embed `Microform Integration` into your payment acceptance web page.

1. Decode the JWT from the `/microform/v2/sessions` response to get the capture context.

2. Use the clientLibrary and clientLibraryIntegrity values that are returned in the JWT from `/microform/v2/sessions` response to obtain the `Microform Integration` JavaScript library URL and integrity value that you use to create your script tags.

   > IMPORTANT
   > You must do this for every transaction as these values can be unique for each transaction. Do not hard code these values, as this can result in client-side ` Microform Integration ` errors. If you do not do this for every transaction, you may load a JavaScript library that is incompatible with the version you requested in the ` /sessions ` request.
   > **Example `/sessions` Response:**

   ```
   "data":{ "clientLibrary":"[EXTRACT clientLibrary VALUE from here]", "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]" }
   ```

   **Example Script Tags**

   ```
   &lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt; &lt;/script&gt;
   ```

   **Example Code for Loading the Script Dynamically Following JWT Extraction Tags**

   ```
   // values read from capture context
   const clientLibrary = " ";
   const clientLibraryIntegrity = " ";
   // create script tag
   const script = document.createElement("script");
   script.src = clientLibrary;
   script.type = "text/javascript";
   script.async = true;
   script.integrity = clientLibraryIntegrity;
   script.crossOrigin = "anonymous";
   // run setup code after script has loaded successfully
   script.onload = function () {
     // SETUP
   };
   // insert to document
   document.head.appendChild(script);
   ```
3. Create the HTML placeholder objects to attach to the microforms.
   Within your HTML checkout, replace the routing number, account number, and confirm account number tag with a simple container. `Microform Integration` uses the container to render an iframe for secured credit card input. This example contains simple `div` tags to define where to place the routing number, account number, and confirm account number fields within the payment acceptance page: `&lt;div id="number-container" class="form-control"&gt;&lt;/div&gt;`.
   **Example: Accept `eCheck` Information Checkout Form**

   ```
   &lt;h1&gt;Checkout Page&lt;/h1&gt;
   &lt;div id="errors-output" role="alert"&gt;&lt;/div&gt;
   &lt;form action="/token" id="my-sample-form" method="post"&gt;
       &lt;div class="form-group"&gt;
           &lt;label id="routingNumber-label"&gt;Routing Number&lt;/label&gt;
           &lt;div id="routingNumber-container" class="form-control"&gt;&lt;/div&gt;
           &lt;label for="accountNumber-label"&gt;Account Number&lt;/label&gt;
           &lt;div id="accountNumber-container" class="form-control"&gt;&lt;/div&gt;
           &lt;label for="accountNumberConfirm-label"&gt;Account Number Confirm&lt;/label&gt;
           &lt;div id="accountNumberConfirm-container" class="form-control"&gt;&lt;/div&gt;
       &lt;/div&gt;

       &lt;div class="form-row"&gt;
           &lt;div class="form-group col-md-6"&gt;
               &lt;label for="accountType"&gt;Account Type&lt;/label&gt;
               &lt;select id="accountType" name="accountType" class="form-control"&gt;
                   &lt;option value="C"&gt;Checking&lt;/option&gt;
                   &lt;option value="S"&gt;Savings&lt;/option&gt;
                   &lt;option value="X"&gt;Corporate checking&lt;/option&gt;
               &lt;/select&gt;
           &lt;/div&gt;
       &lt;/div&gt;

       &lt;button type="button" id="pay-button" class="btn btn-primary"&gt;Pay&lt;/button&gt;
       &lt;input type="hidden" id="flexresponse" name="flexresponse"&gt;
   &lt;/form&gt;
   ```
4. Invoke the Flex SDK by passing the capture context that was generated in the previous step to the microform object.
   `const flex = new Flex(captureContext);`

5. Initiate the microform object with styling to match your web page.
   After you create a new Flex object, you can begin creating your Microform. You will pass your baseline styles and ensure that the button matches your merchant page:
   `const microform = flex.microform("check", { styles: myStyles });`

6. Create and attach the microform fields to the HTML objects through the Microform Integration JavaScript library.

   ```
   const routingNumber = microform.createField("routingNumber", { placeholder: "Enter routing number" });
   const accountNumber = microform.createField("accountNumber", { placeholder: "Enter account number" });
   const accountNumberConfirm = microform.createField("accountNumberConfirm", { placeholder: "accountNumberConfirm" });

   routingNumber.load('#routingNumber-container');
   accountNumber.load('#accountNumber-container');
   accountNumberConfirm.load('#accountNumberConfirm-container');
   ```
7. Create a function for the customer to submit their payment information, and invoke the tokenization request to `Microform Integration` for the transient token.
   {#setting-up-client-side-v2-web-bank-task1_setting-up-client-side-v2-steps}

Mobile Application {#setting-up-client-side-v2-web-bank-task2}
--------------------------------------------------------------

To initiate and embed `Microform Integration` into a native payment acceptance mobile application, follow the steps for web page setup, and ensure that these additional requirements are met:

* The card information acceptance fields of routing number, account number, and confirm account number must be hosted on a web page.
* The `eCheck` information acceptance fields of routing number, account number, and confirmed account number must be hosted on a web page.
* The native application must load the hosted `eCheck` entry form web page in a web view.

Transient Tokens for Accepting `eCheck` Information {#micro-getting-started-pay-bank-trans-tkn}
===============================================================================================

The response to a successful customer interaction with `Microform Integration` is a transient token. The transient token is a reference to the payment data that is collected on your behalf. Tokens allow secure card or check payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.

Transient Token Time Limit {#transient-token-time-limit-pay-bank_time-limit}
============================================================================

The sensitive data associated with the transient token is available for use in API requests for a 15-minute duration. The transient token can be used multiple times within the 15-minute period. After 15 minutes, you must prompt the customer to restart the checkout flow.
**Example: Creating the Pay Button with Event Listener for Accepting `eCheck` Information**

```
const button = document.querySelector("#myButton");

button.addEventListener("click", function () {
  // Compiling accounttype into optional parameters
  const options = {
    accountType: document.querySelector(“#accountType”).value,
  };
  //
  microform.createToken(options, function (err, token) {
    // handle err
    if (err) {
      console.error(err);
      errorsOutput.textContent = err.message;
      return;
    }

    // At this point you may pass the token back to your server as you wish.
    // In this example we append a hidden input to the form and submit it.
    console.log(JSON.stringify(token));
    flexResponse.value = JSON.stringify(token);
    form.submit();
  });
});
```

When the customer submits the form, `Microform Integration` securely collects and tokenizes the data in the loaded fields as well as the options supplied to the `createToken()` function. If tokenization succeeds, your callback receives the token as its second parameter. Send the token to your server, and use it in place of the `eCheck` information when you use supported payment services.
**Example: Customer-Submitted Form for Accepting `eCheck` Information**

```
&lt;script&gt;
    // Variables from the HTML form
    const form = document.querySelector('#my-sample-form');
    const payButton = document.querySelector('#pay-button');
    const flexResponse = document.querySelector('#flexresponse');
    const accountType = document.querySelector('#accountType')
    const errorsOutput = document.querySelector('#errors-output');

    // the capture context that was requested server-side for this transaction
    const captureContext = &lt;% -keyInfo %&gt; ;
    // custom styles that will be applied to each field we create using Microform
    const myStyles = {
        'input': {
            'font-size': '14px',
            'font-family': 'helvetica, tahoma, calibri, sans-serif',
            'color': '#555'
        },
        ':focus': { 'color': 'blue' },
        ':disabled': { 'cursor': 'not-allowed' },
        'valid': { 'color': '#3c763d' },
        'invalid': { 'color': '#a94442' }
    };
    // setup Microform
    const flex = new Flex(captureContext);
    const microform = flex.microform("check", { styles: myStyles });
    const routingNumber = microform.createField("routingNumber", { placeholder: "Enter routing number" });
    const accountNumber = microform.createField("accountNumber", { placeholder: "Enter account number" });
    const accountNumberConfirm = microform.createField("accountNumberConfirm", { placeholder: "accountNumberConfirm" });
    routingNumber.load('#routingNumber-container')
    accountNumber.load('#accountNumber-container')
    accountNumberConfirm.load('#accountNumberConfirm-container')


    // Configuring a Listener for the Pay button
    payButton.addEventListener('click', function () {

        // Compiling MM & YY into optional parameters
        const options = {
            accountType: document.querySelector('#accountType').value,
        };
        //
        microform.createToken(options, function (err, token) {
            if (err) {
                // handle error
                console.error(err);
                errorsOutput.textContent = err.message;
            } else {
                // At this point you may pass the token back to your server as you wish.
                // In this example we append a hidden input to the form and submit it.
                console.log(JSON.stringify(token));
                flexResponse.value = JSON.stringify(token);
                form.submit();
            }
        });
    });
&lt;/script&gt;
```

Transient Token Response Format {#transient-token-response-format-pay-bank}
===========================================================================

The transient token is issued as a JSON Web Token ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). A JWT is a string consisting of three parts that are separated by dots:

* Header
* Payload
* Signature
  {#transient-token-response-format-pay-bank_ul_lvk_ksf_4nb}
  JWT example: `xxxxx.yyyyy.zzzzz`
  The payload portion of the token is an encoded Base64URL JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

> IMPORTANT
> When you integrate with ` Cybersource ` APIs, ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for. Additional fields may be added in the future.
> You must ensure that your integration can handle new fields that are returned in the response. While the underlying data structures will not change, you must also ensure that your integration can handle changes to the order in which the data is returned.
> The internal data structure of the JWT can expand to contain additional data elements. Ensure that your integration and validation rules do not limit the data elements contained in responses.
> **Example: Token Payload for Accepting `eCheck` Information**

```
{
  "iss" : "Flex/00",
  "exp" : 1732527524,
  "type" : "mf-2.1.0",
  "iat" : 1732526624,
  "jti" : "1D3HRVI3KM4HFWQAZ2JFI993NEVBAH5NYJFIH82RAMYWDUJ444KT674445A4EAC0",
  "content" : {
    "paymentInformation" : {
      "bank" : {
        "routingNumber" : { },
        "account" : {
          "number" : { },
          "type" : { }
        }
      },
      "paymentType" : {
        "name" : {
          "value" : "CHECK"
        }
      }
    }
  }
}
```

Validating the Transient Token {#validating-the-transient-token-pay-bank}
=========================================================================

After receiving the transient token, validate its integrity using the public key embedded within the capture context created at the beginning of this flow. This verifies that `Cybersource` issued the token and that no data tampering occurred during transit.
**Example: Capture Context Public Key**

```
"jwk": {
                "kty": "RSA",
                "e": "AQAB",
                "use": "enc",
                "n": "3DhDtIHLxsbsSygEAG1hcFqnw64khTIZ6w9W9mZNl83gIyj1FVk-H5GDMa85e8RZFxUwgU_zQ0kHLtONo8SB52Z0hsJVE9wqHNIRoloiNPGPQYVXQZw2S1BSPxBtCEjA5x_-bcG6aeJdsz_cAE7OrIYkJa5Fphg9_pxgYRod6JCFjgdHj0iDSQxtBsmtxagAGHjDhW7UoiIig71SN-f-gggaCpITem4zlb5kkRVvmKMUANe4B36v4XSSSpwdP_H5kv4JDz_cVlp_Vy8T3AfAbCtROyRyH9iH1Z-4Yy6T5hb-9y3IPD8vlc8E3JQ4qt6U46EeiKPH4KtcdokMPjqiuQ",
                "kid": "00UaBe20jy9VkwZUQPZwNNoKFPJA4Qhc"    }
```

Use the capture context public key to cryptographically validate the JWT provided from a successful `microform.createToken` call. You might have to convert the JSON Web Key (JWK) to privacy-enhanced mail (PEM) format for compatibility with some JWT validation software libraries.
The `Cybersource` SDK has functions that verify the token response. You must verify the response to ensure that no tampering occurs as it passes through the cardholder device. Do so by using the public key generated at the start of the process.

Next Steps {#microform-integ-next-steps}
========================================

After you complete the server-side and client-side setup for accepting payment information with `Microform Integration`, you can customize your configuration:

* **Styling** : Customize the style and behavior of `Microform Integration` on your site. For information, see [Styling](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-next-steps/styling-v2.md "").
* **Events** : Subscribe to `Microform Integration` events and obtain them through event listeners. For information, see [Events](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-next-steps/events-v2.md "").

Styling {#styling-v2}
=====================

`Microform Integration` can be styled to look and behave like any other input field on your site.

General Appearance {#styling-v2_id18AB90TB05Z}
----------------------------------------------

The `&lt;iframe&gt;` element rendered by Microform has an entirely transparent background that completely fills the container you specify. By styling your container to look like your input fields, your customer will be unable to detect any visual difference. You control the appearance using your own stylesheets. With stylesheets, there are no restrictions and you can often re-use existing rules.

Explicitly Setting Container Height {#styling-v2_id18AB90UF0Y4}
---------------------------------------------------------------

Typically, input elements calculate their height from font size and line height (and a few other properties), but `Microform Integration` requires explicit configuration of height. Make sure you style the height of your containers in your stylesheets.

Managed Classes {#styling-v2_id18AB90W0LHS}
-------------------------------------------

In addition to your own container styles, `Microform Integration` automatically applies some classes to the container in response to internal state changes.

| Class                          | Description                                                       |
|:-------------------------------|:------------------------------------------------------------------|
| `.flex-microform`              | Base class added to any element in which a field has been loaded. |
| `.flex-microform-autocomplete` | The field has been filled using an `autocomplete/autofill` event. |
| `.flex-microform-disabled`     | The field has been disabled.                                      |
| `.flex-microform-focused`      | The field has user focus.                                         |
| `.flex-microform-incomplete`   | The field is incomplete and could be valid.                       |
| `.flex-microform-invalid`      | The input card number invalid.                                    |
| `.flex-microform-valid`        | The input card number is valid.                                   |

To make use of these classes, include overrides in your application's stylesheets. You can combine these styles using regular CSS rules. Here is an example of applying CSS transitions in response to input state changes:

```
.flex-microform {
  height: 20px;
  background: #ffffff;
  -webkit-transition: background 200ms;
  transition: background 200ms;
}

/* different styling for a specific container */
#securityCode-container.flex-microform {
  background: purple;
}

.flex-microform-focused {
  background: lightyellow;
}

.flex-microform-valid {
  background: green;
}

.flex-microform-valid.flex-microform-focused {
  background: lightgreen;
}

.flex-microform-autocomplete {
  background: #faffbd;
}
```

Input Field Text {#styling-v2_id18AB90000UI}
--------------------------------------------

To style the text within the iframe element, use the JavaScript library. The `styles` property in the set-up options accepts a CSS-like object that allows customization of the text. Only a subset of the CSS properties is supported.

```
const customStyles = {
  'input': {
    'font-size': '16px',
    'color': '#3A3A3A'
  },
  '::placeholder': {
    'color': 'blue'
  },
  ':focus': {
    'color': 'blue'
  },
  ':hover': {
    'font-style': 'italic'
  },
  ':disabled': {
    'cursor': 'not-allowed',
  },
  'valid': {
    'color': 'green'
  },
  'invalid': {
    'color': 'red'
  }
};

const flex = new Flex('..........');
// apply styles to all fields
const microform = flex.microform({ styles: customStyles });
const securityCode = microform.createField('securityCode');

// override the text color for the card number field
const number = microform.createField('number', { styles: { input: { color: '#000' }}});
```

Supported Properties {#styling-v2_id18AB9A005YK}
------------------------------------------------

These CSS properties are supported in the `styles: { ... }` configuration hash. Unsupported properties are not added to the inner field, and a warning is output to the console.

* `color`
* `cursor`
* `font`
* `font-family`
* `font-kerning`
* `font-size`
* `font-size-adjust`
* `font-stretch`
* `font-style`
* `font-variant`
* `font-variant-alternates`
* `font-variant-caps`
* `font-variant-east-asian`
* `font-variant-ligatures`
* `font-variant-numeric`
* `font-weight`
* `line-height`
* `opacity`
* `text-shadow`
* `text-rendering`
* `transition`
* `-moz-osx-font-smoothing`
* `-moz-tap-highlight-color`
* `-moz-transition`
* `-o-transition`
* `-webkit-font-smoothing`
* `-webkit-tap-highlight-color`
* `-webkit-transition`

Events {#events-v2_Events}
==========================

You can subscribe to `Microform Integration` events and obtain them through event listeners. Using these events, you can easily enable your checkout user interface to respond to any state changes as soon as they happen.

| Event Name           | Emitted When                                                                                                                                                                         |
|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `autocomplete`       | Customer fills the credit card number using a browser or third-party extension. This event provides a hook onto the additional information provided during the `autocomplete` event. |
| `blur`               | Field loses focus.                                                                                                                                                                   |
| `change`             | Field contents are edited by the customer. This event contains various data such as validation information and details of any detected card types.                                   |
| `focus`              | Field gains focus.                                                                                                                                                                   |
| `inputSubmitRequest` | Customer requests submission of the field by pressing the Return key or similar.                                                                                                     |
| `load`               | Field has been loaded on the page and is ready for user input.                                                                                                                       |
| `unload`             | Field is removed from the page and no longer available for user input.                                                                                                               |
| `update`             | Field configuration was updated with new options.                                                                                                                                    |
[Events]

Some events may return data to the event listener's callback as described in the next section.

Subscribing to Events {#events-v2_id18ABA0R07HT}
------------------------------------------------

Using the `.on()` method provided in the `microformInstance` object, you can easily subscribe to any of the supported events.
For example, you could listen for the `change` event and in turn display appropriate card art and display brand-specific information.

```
const secCodeLbl = document.querySelector('#mySecurityCodeLabel');
const numberField = microform.createField('number');

// Update your security code label to match the detected card type's terminology
numberField.on('change', function(data) {
	secCodeLbl.textContent = (data.card && data.card.length &gt; 0) ? data.card[0].securityCode.name : 'CVN';
});

numberField.load('#myNumberContainer');
```

The `data` object supplied to the event listener's callback includes any information specific to the triggered event.

Card Detection {#events-v2_id18ABA0UC0PF}
-----------------------------------------

By default, `Microform Integration` attempts to detect the card type as it is entered. As card numbers are entered, detection information is sent back in the `change` event. You can use this information to build a dynamic user experience by providing feedback to the user as they type their card number.

```
{
   "card": [
       {
           "name": "visa",
           "brandedName": "Visa",
           "cybsCardType": "001",
           "spaces": [ 4, 8, 12 ],
           "blocks": [ 4, 4, 4, 7 ],
           "lengths": [ 13, 14, 15, 16, 17, 18, 19 ],
           "securityCode": {
               "name": "CVV",
               "length": 3
           },
           "luhn": true,
           "valid": true,
           "couldBeValid": true
       },
       {
           "name": "cartesbancaires",
           "brandedName": "Cartes Bancaires",
           "cybsCardType": "036",
           "spaces": [ 4, 8, 12 ],
           "blocks": [ 4, 4, 4, 7 ],
           "lengths": [ 13, 14, 15, 16, 17, 18, 19 ],
           "securityCode": {
               "name": "CVV",
               "length": 3
           },
           "luhn": true,
           "valid": true,
           "couldBeValid": true
       }
   ],
   "empty": false,
   "couldBeValid": true,
   "valid": true
}
```

If `Microform Integration` is unable to determine a single card type, you can use this information to prompt the customer to choose from a possible range of values.
If type is specified in the `microformInstance.createToken(options,...)` method, the specified value always takes precedence over the detected value.
It is up to the merchant to then take the results from cardDetection and pass that into the **type** parameter within the `microformInstance.createToken(options,...)` method. `Microform Integration` no longer attempts to determine a single card type by default. Instead, it returns detectedCardTypes, in the transient token response and the merchant can decide how to handle this information.

Support for Dual-Branded Cards
------------------------------

`Microform Integration` supports dual-branded cards. To utilize this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["VISA", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, `Microform Integration` returns the detected card types based on the order specified in the allowedCardNetworks array. You must then decide which card type to pass.

Support for Card Types without Security Code
--------------------------------------------

Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). `Microform Integration` supports these card types and provides automatic card detection. This enables you to dynamically display the fields that are relevant for the detected card type.
If you support only card types that do not have security codes, you must render only the card number field and the required fields. Do not render the security code field.
If you support card types that do not have security codes as well as cards types that do have security codes, you can use card detection to determine if the security code field should be enabled or disabled based on the card details that are entered by the customer.
This example shows an implementation that accounts for both cards that do and do not have security codes:

```
const numberField = microform.createField('number');
const securityCodeField = microform.createField('securityCode');

numberField.on('change', function (data) {
  // Check if detected cards don't have a security code
  const allCardsWithoutSecurityCode =
    data.card &&
    data.card.length &gt; 0 &&
    data.card.every(function (card) {
      return card.securityCode === false;
    });

  if (allCardsWithoutSecurityCode) {
    // Disable the security code field only when detected cards don't require a security code
    securityCodeField.update({ disabled: true });
  } else {
    // Enable the security code field when any card requires CVV
    securityCodeField.update({ disabled: false });
  }
});
```

Autocomplete {#events-v2_id18ABA0X05PN}
---------------------------------------

By default, `Microform Integration` supports the autocomplete event of the cardnumber field provided by certain browsers and third-party extensions. An `autocomplete` event is provided to allow easy access to the data that was provided to allow integration with other elements in your checkout process.
The format of the data provided in the event might be as follows:

```
{
name: '_____',
expirationMonth: '__',
expirationYear: '____'
}
```

These properties are in the object only if they contain a value; otherwise, they are undefined. Verify the properties before using the event. This example displays how to use this event to update other fields in your checkout process:

```
const number = microform.createField('number');
number.on('autocomplete', function(data) {
	if (data.name) document.querySelector('#myName').value = data.name;
	if (data.expirationMonth) document.querySelector('#myMonth').value = data.expirationMonth;
	if (data.expirationYear) document.querySelector('#myYear').value = data.expirationYear;
});
```

Security Recommendations {#security-recommendations-v2_SecurityRecommendations}
===============================================================================

By implementing a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP ""), you can make use of browser features to mitigate many [cross-site scripting attacks](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS) "").
The full set of directives required for `Microform Integration` is:

| Policy     | Sandbox                             | Production                      |
|:-----------|:------------------------------------|:--------------------------------|
| frame-src  | https://testflex.`cybersource`.com/ | https://flex.`cybersource`.com/ |
| child-src  | https://testflex.`cybersource`.com/ | https://flex.`cybersource`.com/ |
| script-src | https://testflex.`cybersource`.com/ | https://flex.`cybersource`.com/ |
[Security Policy Locations]

Reference {#micro-v2-reference}
===============================

This reference provides additional information for creating `Microform Integration` web pages.

JavaScript API Reference {#api-reference-v2_api_reference}
==========================================================

This reference provides details about the JavaScript API for creating `Microform Integration` web pages.

Class: Field {#class--field-v2}
===============================

An instance of this class is returned when you add a Field to a Microform integration using [microform.createField](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md ""). With this object, you can then interact with the Field to subscribe to events, programmatically set properties in the Field, and load it to the DOM.

Methods
-------

`clear()`
Programmatically clear any entered value within the field.
**Example**

```
field.clear();
```

`dispose()`
Permanently remove this field from your Microform integration.
**Example**

```
field.dispose();
```

`focus()`
Programmatically set user focus to the Microform input field.
**Example**

```
field.focus();
```

`load(container)`
Load this field into a container element on your page.
Successful loading of this field will trigger a load event.

| Name      | Type                  | Description                                                                                                                                     |
|:----------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| container | HTMLElement \| string | Location in which to load this field. It can be either an HTMLElement reference or a CSS selector string that will be used to load the element. |
[Parameters]

**Examples**
*Using a CSS selector*

```
field.load('.form-control.card-number');
```

*Using an HTML element*

```
const container = document.getElementById('container');
field.load(container);
```

`off(type, listener)`
Unsubscribe an event handler from a Microform Field.

| Name     | Type     | Description                                     |
|:---------|:---------|:------------------------------------------------|
| type     | string   | Name of the event you wish to unsubscribe from. |
| listener | function | The handler you wish to be unsubscribed.        |
[Parameter]

**Example**

```
// subscribe to an event using .on() but keep a reference to the handler that was supplied.
const focusHandler = function() { console.log('focus received'); }
field.on('focus', focusHandler);

// then at a later point you can remove this subscription by supplying the same arguments to .off()
field.off('focus', focusHandler);
```

`on(type, listener)`
Subscribe to events emitted by a Microform Field. Supported eventTypes are:

* autocomplete
* blur
* change
* focus
* inputSubmitRequest
* load
* unload
* update

{#class--field-v2_ul_2}
Some events may return data as the first parameter to the callback otherwise this will be undefined. For further details see each event's documentation using the links above.

| Name     | Type     | Description                                 |
|:---------|:---------|:--------------------------------------------|
| type     | string   | Name of the event you wish to subscribe to. |
| listener | function | Handler to execute when event is triggered. |
[Parameters]

**Example**

```
field.on('focus', function() {
  console.log('focus received'); });
```

`unload()`
Remove a the Field from the DOM. This is the opposite of a load operation.
**Example**

```
field.unload();
```

`update(options)`
Update the field with new configuration options. This accepts the same parameters as microform.createField(). New options will be merged into the existing configuration of the field.

| Name    | Type   | Description                                           |
|:--------|:-------|:------------------------------------------------------|
| options | object | New options to be merged with previous configuration. |
[Parameter]

**Example**

```
// field initially loaded as disabled with no placeholder
const number = microform.createField('number', { disabled: true });
number.load('#container');

// enable the field and set placeholder text
number.update({ disabled: false, placeholder: 'Please enter your card number' });
```

**Events**
`autocomplete`
Emitted when a customer has used a browser or third-party tool to perform an autocomplete/autofill on the input field. Microform will attempt to capture additional information from the autocompletion and supply these to the callback if available. Possible additional values returned are:

* name
* expirationMonth
* expirationYear

{#class--field-v2_ul_4}
If a value has not been supplied in the autocompletion, it will be undefined in the callback data. As such you should verify that it exists before use.
**Examples**
*Possible format of data supplied to callback*

```
{
  name: '_____',
  expirationMonth: '__',
  expirationYear: '____'
}
```

*Updating the rest of your checkout after an autocomplete event*

```
field.on('autocomplete', function(data) {
if (data.name) document.querySelector('#myName').value = data.name;
if (data.expirationMonth) document.querySelector('#myMonth').value = data.expirationMonth;
if (data.expirationYear) document.querySelector('#myYear').value = data.expirationYear;
});
```

`blur`
This event is emitted when the input field has lost focus.
**Example**

```
field.on('blur', function() {
  console.log('Field has lost focus');
});

// focus the field in the browser then un-focus the field to see your supplied handler execute
```

`change`
Emitted when some state has changed within the input field. The payload for this event contains several properties.
**Type:** object

| Name         | Type    |
|:-------------|:--------|
| card         | object  |
| valid        | boolean |
| couldBeValid | boolean |
| empty        | boolean |
[Properties]

**Examples**
*Minimal example:*

```
field.on('change', function(data) {
  console.log('Change event!');
  console.log(data);
});
```

*Use the card detection result to update your UI.*

```
const cardImage = document.querySelector('img.cardDisplay');
const cardSecurityCodeLabel = document.querySelector('label[for=securityCode]');

// create an object to map card names to the URL of your custom images
const cardImages = {
	visa: '/your-images/visa.png',
	mastercard: '/your-images/mastercard.png',
	amex: '/your-images/amex.png',
	maestro: '/your-images/maestro.png',
	discover: '/your-images/discover.png',
	dinersclub: '/your-images/dinersclub.png',
	jcb: '/your-images/jcb.png'
};

field.on('change', function(data) {
	if (data.card.length === 1) {
		// use the card name to set the correct image src
		cardImage.src = cardImages[data.card[0].name];

		// update the security code label to match the detected card's naming convention
		cardSecurityCodeLabel.textContent = data.card[0].securityCode.name;
	} else {
		// show a generic card image
		cardImage.src = '/your-images/generic-card.png';
	}
});
```

*Use the card detection result to filter select element in another part of your checkout.*

```
const cardTypeOptions = document.querySelector('select[name=cardType] option');

field.on('change', function(data) {
  // extract the identified card types
  const detectedCardTypes = data.card.map(function(c) { return c.cybsCardType; });

  // disable any select options not in the detected card types list
  cardTypeOptions.forEach(function (o) {
    o.disabled = detectedCardTypes.includes(o.value);
  });
});
```

*Updating validation styles on your form element.*

```
const myForm = document.querySelector('form');

field.on('change', function(data) {
	myForm.classList.toggle('cardIsValidStyle', data.valid);
	myForm.classList.toggle('cardCouldBeValidStyle', data.couldBeValid);
});
```

`focus`
Emitted when the input field has received focus.
**Example**

```
field.on('focus', function() {
	console.log('Field has received focus');
});

// focus the field in the browser to see your supplied handler execute
```

`inputSubmitRequest`
Emitted when a customer has requested submission of the input by pressing Return key or similar. By subscribing to this event you can easily replicate the familiar user experience of pressing enter to submit a form. Shown below is an example of how to implement this. The `inputSubmitRequest` handler will:

1. Call `Microform.createToken()`.
2. Call [Microform.createToken()](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md ""). For more information, see these topics:
   * [Module: FLEX](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/module-flex-v2.md "")
   * [Class: Microform](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md "")
3. Take the result and add it to a hidden input on your checkout.
4. Trigger submission of the form containing the newly created token for you to use server-side.

{#class--field-v2_ol_4}
**Example**

```
const form = document.querySelector('form');
const hiddenInput = document.querySelector('form input[name=token]');

field.on('inputSubmitRequest', function() {
	const options = {
		//
	};

	microform.createToken(options, function(response) {
		hiddenInput.value = response.token;
		form.submit();
	});
});
```

`load`
This event is emitted when the field has been fully loaded and is ready for user input.
**Example**

```
field.on('load', function() {
	console.log('Field is ready for user input');
});
```

`unload`
This event is emitted when the field has been unloaded and no longer available for user input.
**Example**

```
field.on('unload', function() {
	console.log('Field has been removed from the DOM');
});
```

`update`
This event is emitted when the field has been updated. The event data will contain the settings that were successfully applied during this update.
**Type:** object
**Example**

```
field.on('update', function(data) {
	console.log('Field has been updated. Changes applied were:');
	console.log(data);
});
```

Module: FLEX {#module-flex-v2_module_flex_v044}
===============================================

**Flex(captureContext)**
`new Flex(captureContext)`
For detailed setup instructions, see [Getting Started](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/microform-integ-getting-started-v2.md "").
**Parameters:**

| Name           | Type   | Description                                                                                           |
|:---------------|:-------|:------------------------------------------------------------------------------------------------------|
| captureContext | String | JWT string that you requested via a server-side authenticated call before starting the checkout flow. |

**Example**
*Basic Setup*

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt;
&lt;/script&gt;//Note: Script location and integrity value should be sourced from the capture context response clientLibrary and clientLibraryIntegrity values.
&lt;script&gt; const flex = new Flex('captureContext');&lt;/script&gt;
```

Methods {#module-flex-v2_id1949GM0705Z}
---------------------------------------

`microform(optionsopt) &gt; {Microform}`{#module-flex-v2_staticmicroformoptionscallbackvoid}
This method is the main setup function used to initialize `Microform Integration`. Upon successful setup, the callback receives a `microform`, which is used to interact with the service and build your integration. For details, see [Class: Microform](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md "").

| Name    | Type   | Description |
|:--------|:-------|:------------|
| options | Object |             |
[**Parameter**]

| Name   | Type   | Attributes         | Description                                                 |
|:-------|:-------|:-------------------|:------------------------------------------------------------|
| styles | Object | \&lt;optional\&gt; | Apply custom styling to all the fields in your integration. |
[**Property**]

***Returns:***
Type: Microform
**Examples**
*Minimal Setup*

```
const flex = new Flex('header.payload.signature');
const microform = flex.microform();
```

*Custom Styling*

```
const flex = new Flex('header.payload.signature');
const microform = flex.microform({
	styles: {
		input: {
			color: '#212529',
			'font-size': '20px'
		}
	}
});
```

Class: Microform {#class-microform-v2_Id18AFA4004NW}
====================================================

An instance of this class is returned when you create a Microform integration using `flex.microform`. This object allows the creation of Microform Fields. For details, see [Module: Flex](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/module-flex-v2.md "").

Methods {#class-microform-v2_id1949H00N0HT}
-------------------------------------------

`createField(fieldType, optionsopt) &gt; {Field}`{#class-microform-v2_clear}
Create a field for this Microform integration.
**Parameters**

| Name      | Type   | Attributes         | Description                                                        |
|:----------|:-------|:-------------------|:-------------------------------------------------------------------|
| fieldType | string |                    | Supported values: * `number` * `securityCode`                      |
| options   | object | \&lt;optional\&gt; | To change these options after initialization use `field.update()`. |

**Properties**

| Name          | Type           | Attributes         | Default | Description                                                                                                                                                                                                                                           |
|:--------------|:---------------|:-------------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| aria-label    | string         | \&lt;optional\&gt; | `true`  | Set the input's label for use by assistive technologies using the [aria-label attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-label_attribute "").                                          |
| aria-required | boolean        | \&lt;optional\&gt; | `true`  | Used to indicate through assistive technologies that this input is required for submission using the [aria-required attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques/Using_the_aria-required_attribute ""). |
| autoformat    | Boolean        | \&lt;optional\&gt; | `true`  | Enable or disable automatic formatting of the input field. This is only supported for number fields and will automatically insert spaces based on the detected card type.                                                                             |
| description   | string         | \&lt;optional\&gt; |         | Sets the input's description for use by assistive technologies using the [aria-describedby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby "") attribute.                                                |
| disabled      | Boolean        | \&lt;optional\&gt; | false   | Sets the `disabled` attribute on the input.                                                                                                                                                                                                           |
| maxLength     | number         | \&lt;optional\&gt; | 3       | Sets the maximum length attribute on the input. This is only supported for `securityCode` fields and may take a value of `3` or `4`.                                                                                                                  |
| placeholder   | string         | \&lt;optional\&gt; |         | Sets the `placeholder` attribute on the input.                                                                                                                                                                                                        |
| styles        | stylingOptions | \&lt;optional\&gt; |         | Apply custom styling to this field.                                                                                                                                                                                                                   |
| title         | string         | \&lt;optional\&gt; |         | Sets the [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title "") attribute on the input. Typically used to display tooltip text on hover.                                                                               |

**Returns**
Type: Field
***Examples***
*Minimal Setup*

```
const= new Flex('.........');
const microform = flex.microform('card');
const number = microform.createField('number');
```

*Providing Custom Styles*

```
const flex = new Flex('.........');
const microform = flex.microform();
const number = microform.createField('number', {
	styles: {
		input: {
			'font-family': '"Courier New", monospace'
		}
	}
});
```

*Providing Custom Styles to All Fields within the `Microform Integration`*

```
const= new Flex('.........');

// apply styles to all fields
const microform = flex.microform('card', { styles: customStyles });

// override the text color for the card number field only
const number = microform.createField('number', { styles: { input: { color: '#000' }}});
```

*Providing Custom Styles to A Specific Field within the `Microform Integration`*

```
const= new Flex('.........');
const microform = flex.microform('card');

const number = microform.createField('number'), {
    styles: {
        input: {
            'font-family': '"Courier New", monospace'
               }
         }});
```

*Setting the Length of a Security Code Field*

```
const= new Flex('.........');
const microform = flex.microform('card');

const securityCode = microform.createField('securityCode', {maxlength:4});
```

`createToken(options, callback)`{#class-microform-v2_createTokenoptionscallback}
Request a token using the card data captured in the Microform fields. A successful token creation will receive a transient token as its second callback parameter.
**Parameter**

| Name     | Type     | Description                                                                                                                                          |
|:---------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| options  | object   | Additional tokenization options.                                                                                                                     |
| callback | callback | Any error will be returned as the first callback parameter. Any successful creation of a token will be returned as a string in the second parameter. |

**Properties**

| Name            | Type   | Attributes         | Description                                                                            |
|:----------------|:-------|:-------------------|:---------------------------------------------------------------------------------------|
| type            | string | \&lt;optional\&gt; | Three-digit card type string. If set, this will override any automatic card detection. |
| expirationMonth | string | \&lt;optional\&gt; | Two-digit month string. Must be padded with leading zeros if single digit.             |
| expirationYear  | string | \&lt;optional\&gt; | Four-digit year string.                                                                |

**Examples**
*Minimal example omitting all optional parameters.*

```
microform.createToken({}, function(err, token) {
	if (err) {
		console.error(err);
		return;
	}

	console.log('Token successfully created!');
	console.log(token);
});
```

*Override the **cardType** parameter using a select element that is part of your checkout.*

```
// Assumes your checkout has a select element with option values that are  card type codes:
// &lt;select id="cardTypeOverride"&gt;
//   &lt;option value="001"&gt;Visa&lt;/option&gt;
//   &lt;option value="002"&gt;Mastercard&lt;/option&gt;
//   &lt;option value="003"&gt;American Express&lt;/option&gt;
//    etc...
// &lt;/select&gt;

const options = {
	type: document.querySelector('#cardTypeOverride').value
};
microform.createToken(options, function(err, token) {
	// handle errors & token response
});
```

*Handling error scenarios*

```
microform.createToken(options, function(err, token) {
  if (err) {
    switch (err.reason) {
      case 'CREATE_TOKEN_NO_FIELDS_LOADED':
        break;
      case 'CREATE_TOKEN_TIMEOUT':
        break;
      case 'CREATE_TOKEN_NO_FIELDS':
        break;
      case 'CREATE_TOKEN_VALIDATION_PARAMS':
        break;
      case 'CREATE_TOKEN_VALIDATION_FIELDS':
        break;
      case 'CREATE_TOKEN_VALIDATION_SERVERSIDE':
        break;
      case 'CREATE_TOKEN_UNABLE_TO_START':
        break;
      default:
        console.error('Unknown error');
        break;
  } else {
    console.log('Token created: ', token);
  }
});
```

Class: MicroformError {#class-microform-error-v2_Id18AFA0Z01BI}
===============================================================

This class defines how error scenarios are presented by Microform, primarily as the first argument to callbacks. See [callback(erropt, nullable, dataopt, nullable) \&gt; {void}](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/global-v2.md "").

Members {#class-microform-error-v2_id1949H0V0BYK}
-------------------------------------------------

`(static, readonly)`Reason Codes - Field Load Errors
Possible errors that can occur during the loading or unloading of a field.
**Properties**

| Name                              | Type   | Description                                                                         |
|:----------------------------------|:-------|:------------------------------------------------------------------------------------|
| FIELD_UNLOAD_ERROR                | string | Occurs when you attempt to unload a field that is not currently loaded.             |
| FIELD_ALREADY_LOADED              | string | Occurs when you attempt to load a field which is already loaded.                    |
| FIELD_LOAD_CONTAINER_SELECTOR     | string | Occurs when a DOM element cannot be located using the supplied CSS Selector string. |
| FIELD_LOAD_INVALID_CONTAINER      | string | Occurs when an invalid container parameter has been supplied.                       |
| FIELD_SUBSCRIBE_UNSUPPORTED_EVENT | string | Occurs when you attempt to subscribe to an unsupported event type.                  |
| FIELD_SUBSCRIBE_INVALID_CALLBACK  | string | Occurs when you supply a callback that is not a function.                           |

`(static, readonly)`Reason Codes - Field object Creation
Possible errors that can occur during the creation of a Field object [createField(fieldType, optionsopt) \&gt; {Field}](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-v2.md#class-microform-v2_clear "").
**Properties**

| Name                            | Type   | Description                                                                       |
|:--------------------------------|:-------|:----------------------------------------------------------------------------------|
| CREATE_FIELD_INVALID_FIELD_TYPE | string | Occurs when you try to create a field with an unsupported type.                   |
| CREATE_FIELD_DUPLICATE          | string | Occurs when a field of the given type has already been added to your integration. |

`(static, readonly)`Reason Codes - Flex object Creation
Possible errors that can occur during the creation of a Flex object.
**Properties**

| Name                    | Type   | Description                               |
|:------------------------|:-------|:------------------------------------------|
| CAPTURE_CONTEXT_INVALID | string | Occurs when you pass an invalid JWT.      |
| CAPTURE_CONTEXT_EXPIRED | string | Occurs when the JWT you pass has expired. |

`(static, readonly)`Reason Codes - Iframe validation errors
Possible errors that can occur during the loading of an iframe.
**Properties**

| Name                          | Type   | Description                                                              |
|:------------------------------|:-------|:-------------------------------------------------------------------------|
| IFRAME_JWT_VALIDATION_FAILED  | string | Occurs when the iframe cannot validate the JWT passed.                   |
| IFRAME_UNSUPPORTED_FIELD_TYPE | string | Occurs when the iframe is attempting to load with an invalid field type. |

`(static, readonly)`Reason Codes - Token creation
Possible errors that can occur during the request to create a token.
**Properties**

| Name                               | Type   | Description                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CREATE_TOKEN_NO_FIELDS_LOADED      | string | Occurs when you try to request a token, but no fields have been loaded.                                                                                                                                                                                                                                                 |
| CREATE_TOKEN_TIMEOUT               | string | Occurs when the `createToken` call was unable to proceed Within Capture Context Validity (15 mins): : Do NOT resend the capture context or reload Microform. Instruct the customer to retry until successful. After Capture Context Validity (\&gt;15 mins): : Resend the capture context request and reload Microform. |
| CREATE_TOKEN_XHR_ERROR             | string | Occurs when there is a network error when attempting to create a token. Resend the capture context request and reload Microform.                                                                                                                                                                                        |
| CREATE_TOKEN_NO_FIELDS             | string | Occurs when the data fields are unavailable for collection.                                                                                                                                                                                                                                                             |
| CREATE_TOKEN_VALIDATION_PARAMS     | string | Occurs when there's an issue with parameters supplied to `createToken`.                                                                                                                                                                                                                                                 |
| CREATE_TOKEN_VALIDATION_FIELDS     | string | Occurs when there's a validation issue with data in your loaded fields. Instruct the customer to enter valid data.                                                                                                                                                                                                      |
| CREATE_TOKEN_VALIDATION_SERVERSIDE | string | Occurs when server-side validation rejects the `createToken` request.                                                                                                                                                                                                                                                   |
| CREATE_TOKEN_UNABLE_TO_START       | string | Occurs when no loaded field was able to handle the `createToken` request.                                                                                                                                                                                                                                               |

`(nullable)correlationID :string`
The correlationId of any underlying API call that resulted in this error.
***Type***
String
`(nullable)details :array`
Additional error specific information.
***Type***
Array
`(nullable)informationLink :string`
A URL link to general online documentation for this error.
***Type***
String
`message :string`
A simple human-readable description of the error that has occurred.
***Type***
String
`reason :string`
A reason corresponding to the specific error that has occurred.
***Type***
String

Global {#global-v2_Id18AFF0N0A8T}
=================================

Type Definitions {#global-v2_TypeDefinitions}
---------------------------------------------

`callback(erropt, nullable, dataopt, nullable) &gt; {void}`{#global-v2_callbackerroptnullabledataoptnullablevoid}
Microform uses the error-first callback pattern, as commonly used in [Node.js](https://nodejs.org/api/errors.md#errors_error_first_callbacks "").
If an error occurs, it is returned by the first `err` argument of the callback. If no error occurs, `err` has a null value and any return data is provided in the second argument.
***Parameters***

| Name | Type                                                                                                                                                                                                                                              | Attributes                            | Description                                                                                              |
|:-----|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|:---------------------------------------------------------------------------------------------------------|
| err  | MicroformError. See [Class: MicroformError](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/api-reference-v2/class-microform-error-v2.md ""). | \&lt;optional\&gt; \&lt;nullable\&gt; | An Object detailing occurred errors, otherwise null.                                                     |
| data | \*                                                                                                                                                                                                                                                | \&lt;optional\&gt; \&lt;nullable\&gt; | In success scenarios, this is whatever data has been returned by the asynchronous function call, if any. |

**Returns**
Type: void
**Example**
This example shows how to make use of this style of error handling in your code:

```
foo(function (err, data) {
    // check for and handle any errors
    if (err) throw err;

    // otherwise use the data returned
    console.log(data);
});
```

`StylingOptions`
Styling options are supplied as an object that resembles CSS but is limited to a subset of CSS properties that relate only to the text within the iframe.
Supported CSS selectors:

* input
* ::placeholder
* :hover
* :focus
* :disabled
* valid
* invalid
* incomplete

Supported CSS properties:

* `color`
* `cursor`
* `font`
* `font-family`
* `font-kerning`
* `font-size`
* `font-size-adjust`
* `font-stretch`
* `font-style`
* `font-variant`
* `font-variant-alternates`
* `font-variant-caps`
* `font-variant-east-asian`
* `font-variant-ligatures`
* `font-variant-numeric`
* `font-weight`
* `incomplete`
* `line-height`
* `opacity`
* `text-shadow`
* `text-rendering`
* `transition`
* `-moz-osx-font-smoothing`
* `-moz-tap-highlight-color`
* `-moz-transition`
* `-o-transition`
* `-webkit-font-smoothing`
* `-webkit-tap-highlight-color`
* `-webkit-transition`

Any unsupported properties will not be applied and will raise a `console.warn()` alert.
**Properties**

| Name          | Type   | Attributes         | Description                                                                                                                     |
|:--------------|:-------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| input         | object | \&lt;optional\&gt; | Main styling applied to the input field.                                                                                        |
| ::placeholder | object | \&lt;optional\&gt; | Styles for the ::placeholder pseudo-element within the main input field. This also adds vendor prefixes for supported browsers. |
| :hover        | object | \&lt;optional\&gt; | Styles to apply when the input field is hovered over.                                                                           |
| :focus        | object | \&lt;optional\&gt; | Styles to apply when the input field has focus.                                                                                 |
| :disabled     | object | \&lt;optional\&gt; | Styles applied when the input field has been disabled.                                                                          |
| valid         | object | \&lt;optional\&gt; | Styles applied when Microform detects that the input card number is valid. Relies on card detection being enabled.              |
| invalid       | object | \&lt;optional\&gt; | Styles applied when Microform detects that the input card number is invalid. Relies on card detection being enabled.            |

**Example**

```
const styles = {
	'input': {
		'color': '#464646',
		'font-size': '16px',
		'font-family': 'monospace'
	},
	':hover': {
		'font-style': 'italic'
	},
	'invalid': {
		'color': 'red'
	}
};
```

Capture Context API {#flex-capture-context-api-intro}
=====================================================

The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the front-end JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Microform Integration`, in addition to allowed card networks and payment types (card or check). The capture context request includes these elements:

* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigins
* transientTokenResponseOptions.includeCardPrefix
  For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-v2-reference/micro-appendix-jwts.md "").

Target Origin
:
The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain) and port number (if used).

    You must use the https:// protocol. Sub domains must also be included in the target origin.

    Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.

    For example, if you are launching `Microform Integration` on example.com, the target origin could be any of the following:

    * [https://example.com](https://example.com/ "")
    * [https://subdomain.example.com](https://subdomain.example.com/ "")
    * [https://example.com:8080](https://example.com:8080/ "")


    You can define the payment cards and digital payments that you want to accept in the capture context.

    You can provide up to nine origins in the targetOrigins field for nested iframes. If your list of origins in the targetOrigins field contains more than five entries, you must do the following:

    * Compare the list of origins in the `v2/sessions` targetOrigins field with the location.ancestorOrigins of the browser and ensure that they match. For more information, see [this description](https://developer.mozilla.org/en-US/docs/Web/API/Location/ancestorOrigins "") about the location.ancestorOrigins property on the Mozilla Developer website.
    * Confirm that the count of origins in the targetOrigins field matches that in the content. If any origins are missing or are mismatched, the system will not allow Microform to load and a client-side error message appears.

    If your application does not require up to nine nested iframes, `Cybersource` recommends that you minimize the number of nested iframes to maintain optimal performance.

Allowed Card Networks
:
Use the allowedCardNetworks field to define the card types.

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
    * JCrew
    * KCP
    * Mada
    * Maestro
    * Mastercard
    * Meeza
    * PayPak
    * UATP
    * Visa

:
When you integrate with `Microform Integration` to accept card or `eCheck` information, you must include at least one card network in the allowedCardNetworks field in the capture context request.

Allowed Payment Types
:
You can specify the type of `Microform Integration` you want to accept in the capture context. You can accept card and `eCheck` information.
:
Use the allowedPaymentTypes field to define the payment type:

    * `CARD`
    * `CHECK`

:
The allowedPaymentTypes field is optional. When this field is provided in the capture context, the `Microform Integration` defaults the field value to `CARD` and is returned in the response.

Include Card Prefix
:
You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

    * 6 digits
    * 8 digits
    * no prefix at all

    To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.

:
**If you want to receive a 6-digit card number prefix in the response:**

    * Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.
    * This example shows how a 6-digit card number prefix `411111` is returned in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111”,
      "prefix" : "411111"
      ```

:
**If you want to receive an 8-digit card number prefix in the response:**

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

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/microform/v2/sessions`
**Test:** `POST ``https://apitest.cybersource.com``/microform/v2/sessions`

Required Fields for Requesting the Capture Context {#flex-capture-context-api-intro_req-fields-uc-capture-ctx}
--------------------------------------------------------------------------------------------------------------

Your capture context request for accepting card and `eCheck` information must include these fields:

[allowedCardNetworks](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/allowed-card-networks.md "")
:
This field is required only for accepting card information.

[allowedPaymentTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/allowed-payment-types.md "")
:
This field is required only for accepting `eCheck` information.

[clientVersion](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-version.md "")
:

[targetOrigins](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/target-origins.md "")
:
The URL in this field value must contain `https`.
For a complete list of fields you can include in your request, see the [`Cybersource` REST API Reference](https://developer.cybersource.com/api-reference-assets/index.md#unified-checkout "").

REST Example: Requesting the Capture Context {#flex-capture-context-api-ex-rest}
================================================================================

Capture Context Request for Accepting Card and `eCheck` Information

```
{
  "clientVersion": "v2",
  "targetOrigins": [
    "https://www.example.com",
    "https://www.basket.example.com",
    "https://ecom.example.com"
  ],
  "allowedCardNetworks": [
    "VISA",
    "MASTERCARD",
    "AMEX",
    "CARTESBANCAIRES",
    "CARNET",
    "CUP",
    "DINERSCLUB",
    "DISCOVER",
    "EFTPOS",
    "ELO",
    "JCB",
    "JCREW",
    "MADA",
    "MAESTRO",
    "MEEZA"
  ],
  "allowedPaymentTypes": [
    "CARD",
    "CHECK"
  ]
}
```

Successful Encrypted JWT Response for Accepting Card and `eCheck` Information

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJ4Sy9RZzJzcWNiajNaODdIS0VwZGpSQUFFUEJLenFVaUlrdXdrelRadVNQeG9GWDNOK0VtT3k2ZGlBSXhwMHhvQStJc1Y5czlZZmRZVUJmbDFpV01kRVVmekhMTmhLQ1ZiOFAzSHg0bTQxejl6aEVcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoiaTI5NmZmbUdiVkVRbG5zanNrQnBrajRCU1pRbE9Vd2Z2SUpsdUNIaHVkTEsxQmk4MEtpOVVfb0h2Mmxsd0NJSXFUMHdJWTBvaS1HM0xVc09BUUpjNUpwX08tY1VIdzFjeXV3aDVtWXZkUWZFM0JlcnRUcDZHQ1JLcFVyUjlDOGZoaTNfV1lQTDMwNjMxMGJXajh4OXY0UnlpR1BYUHdnUlJhVDlmbXJRV1diTHZaeFNZQ0Zpal9lSEZaYXQxa1JNdG5pTk5IUTNlV1ViWUV5QWZPSExOWDhUUmN6cjYybkdpeGh4NEFNYVB5YlEtTy0wM1pjRER4UldTLTI0UGhheVVYRjZnVlAydzNHc2hhOFQxSklnYlZSc253bHVuZ01jRExtZFI1cF9ITFlRdnNyX3BFS3pZd2tDQmFOUXA0ZjRkbXhyaVIyT2IyUU5fMXRkU2FUVzN3Iiwia2lkIjoiMDBXSXlhTndYcUJhdHNuYkVmMVNFTjFncHREbDExOUYifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIiwiTUFFU1RSTyIsIkRJU0NPVkVSIiwiRElORVJTQ0xVQiIsIkpDQiIsIkNVUCIsIkNBUlRFU0JBTkNBSVJFUyJdLCJ0YXJnZXRPcmlnaW5zIjpbImh0dHBzOi8vdGhlLXVwLWRlbW8uYXBwc3BvdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJhbGxvd2VkUGF5bWVudFR5cGVzIjpbIkNBUkQiLCJDSEVDSyJdfSwidHlwZSI6Im1mLTIuMS4wIn1dLCJpc3MiOiJGbGV4IEFQSSIsImV4cCI6MTczMzQ5MDQwNywiaWF0IjoxNzMzNDg5NTA3LCJqdGkiOiJZcHdxWlNaTTZ1T1FBV1RoIn0.f24avtv-oUGfSaGqlQZfOZ4B6A-6E6yWymdgUtZmDDOVNanx5uLt5fxSBzAdmtC4em0kORatiS5pMhE66bCJT-ujIMHtdPITq9JJuE4Tm-NdfzznXlhz-qMM_setgmDXYLIIAeaUmSVebMwWqxBVmpQHRIBq2plwfB5dAH411aO-U1_DDJi14sIOLzUr_xhgfLJWsJ_B3gZkSaHrRaHWpnO-okCanTrVKCaFP1X5rKUilGII4wcJLdUyU3f9zFwteQ7wFfG81mRRWz4Gb4YgLt43TCD-jSigCAtgX_mqRyMqzCJtZXkf0Nf-o0bJLAc8-ce8MmeZD8H4uG42Eu-0UA
```

Decrypted Capture Context Header for Accepting Card and `eCheck` Information

```
{
  "kid": "j4",
  "alg": "RS256"
}
```

Decrypted Capture Context Body with Selected Fields for Accepting Card and `eCheck` Information

```
{
  "flx": {
    "path": "/flex/v2/tokens",
    "data": "xK/Qg2sqcbj3Z87HKEpdjRAAEPBKzqUiIkuwkzTZuSPxoFX3N+EmOy6diAIxp0xoA+IsV9s9YfdYUBfl1iWMdEUfzHLNhKCVb8P3Hx4m41z9zhE=",
    "origin": "https://example.com",
    "jwk": {
      "kty": "RSA",
      "e": "AQAB",
      "use": "enc",
      "n": "i296ffmGbVEQlnsjskBpkj4BSZQlOUwfvIJluCHhudLK1Bi80Ki9U_oHv2llwCIIqT0wIY0oi-G3LUsOAQJc5Jp_O-cUHw1cyuwh5mYvdQfE3BertTp6GCRKpUrR9C8fhi3_WYPL306310bWj8x9v4RyiGPXPwgRRaT9fmrQWWbLvZxSYCFij_eHFZat1kRMtniNNHQ3eWUbYEyAfOHLNX8TRczr62nGixhx4AMaPybQ-O-03ZcDDxRWS-24PhayUXF6gVP2w3Gsha8T1JIgbVRsnwlungMcDLmdR5p_HLYQvsr_pEKzYwkCBaNQp4f4dmxriR2Ob2QN_1tdSaTW3w",
      "kid": "00WIyaNwXqBatsnbEf1SEN1gptDl119F"
    }
  },
  "ctx": [
    {
      "data": {
        "clientLibraryIntegrity": "CLIENT LIBRARY INTEGRITY VALUE GOES HERE",
        "clientLibrary": "CLIENT LIBRARY VALUE GOES HERE",
        "allowedCardNetworks": [
          "VISA",
          "MASTERCARD",
          "AMEX",
          "MAESTRO",
          "DISCOVER",
          "DINERSCLUB",
          "JCB",
          "CUP",
          "CARTESBANCAIRES"
        ],
        "targetOrigins": [
          "https://the-up-demo.appspot.com"
        ],
        "mfOrigin": "https://example.com",
        "allowedPaymentTypes": [
          "CARD",
          "CHECK"
        ]
      },
      "type": "mf-2.1.0"
    }
  ],
  "iss": "Flex API",
  "exp": 1733490407,
  "iat": 1733489507,
  "jti": "YpwqZSZM6uOQAWTh"
}
```

Capture Context Request for Accepting Card Information

```
{
  "clientVersion": "v2",
  "targetOrigins": [
    "https://www.example.com",
    "https://www.basket.example.com",
    "https://ecom.example.com"
  ],
  "allowedCardNetworks": [
    "VISA",
    "MASTERCARD",
    "AMEX",
    "CARTESBANCAIRES",
    "CARNET",
    "CUP",
    "DINERSCLUB",
    "DISCOVER",
    "EFTPOS",
    "ELO",
    "JCB",
    "JCREW",
    "MADA",
    "MAESTRO",
    "MEEZA"
  ],
  "allowedPaymentTypes": [
    "CARD"
  ]
}
```

Successful Encrypted JWT Response for Accepting Card Information

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJ1Q0RERW94M2dDQk1VaHI2T1ZDVGt4QUFFS1pHSTRHcDFvQ2pyYXlVb1MxQzdGOXE2WFpyYXhGbGxMVDMvenE2cjFnNXoxS1U2UDZseldqRVFTVVJoZUtxUThoVWJkZVNNdmt5SERTTXUwV01tMzhcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoiMXNDY3NZNC1WZTNWU0VKekhnelJ5WjVDOURrM0VHZ2ZPOGd5SDc5bVJfSlN6NzdmWTdfV1loM3psdTkyTFVfeU5KVTBUMzdOQmVzd0szU2c0YnRNaU41Q0FCbWNXLWNSckhta2k0MVZoNUZRMmtjcWZSSlgxNVhZN1A3R25GTnd4QzVkUG9UM29NM1czRFVHaUMyYW56enhIN3pNNlA3N2hFbnc2TkZHSXlBdXhJRWFwRG9DaXlEVW5NdFRwV2lBV3YzTF9OVHZOaHRkVE4tNm1GRWU1RmdVYmlzeWtrTzlWMHZaS0d6SWRWWmdTdE42cHlnUGhVbnlNXzJIVmIxQmkyWjNKaElhZDFLUW02SGl0NklwYjNyUTBHRWZsN0ZWOUV3NGZyNzJpekQ0WVg2WHo0V3ZuMzlLN3J3WkhCRXdNM3l5Wl9ELTBUbjM1MFhvUlBUVjB3Iiwia2lkIjoiMDB4V1A1eUh1UE1kNkFkNHdwVzNzQkt1bWFaQ01zYWMifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIiwiTUFFU1RSTyIsIkRJU0NPVkVSIiwiRElORVJTQ0xVQiIsIkpDQiIsIkNVUCIsIkNBUlRFU0JBTkNBSVJFUyJdLCJ0YXJnZXRPcmlnaW5zIjpbImh0dHBzOi8vdGhlLXVwLWRlbW8uYXBwc3BvdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJhbGxvd2VkUGF5bWVudFR5cGVzIjpbIkNBUkQiXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzY0MzA0MTQsImlhdCI6MTczNjQyOTUxNCwianRpIjoiZDVZbzVhNU0wWFBPQ1BxZiJ9.G4Ea-gIk6SG5ULE4NE5OsdPI41YaAuTEMHDstBgkFzczIWwzJScvXs4hgWiyA-1ZLGITedlumGj-0x8jxmYTWeTm7D0fP8RL0w148EpDLMD8xMHpAJMdMqZTmYHyichsy8uOZKVOn9NbnuQqfDeQS_rLpJV3tMe2NwJL3RdBXdJ894ihKpFP2yXE1wQeLekNiYJ6s-Uuxwf0jf2CSN_TJAjnfVR6bqlpWbUpiUaBLcqDsHHe_pcrd5g2r-1LEfCiOV9RIw7844XKFNLQZvt_alQjItuMy8M9LVhnlRWCSnTKB1iV1RUxuTWtMzTvHmQWPx4nShqzE3j0Hp61c0PmBw
```

Decrypted Capture Context Body with Selected Fields for Accepting Card Information

```
{
  "flx": {
    "path": "/flex/v2/tokens",
    "data": "gEQUL6QggbM2m8R3/KhDLxAAEOmhvNFhDd+amn9NHURTfjqqN8+7dy/YKQXz0Ik2yhRVQ8omdKZ8VojIYkwOB9yUo/8LdddXruIQ3O5dSfmbW6A=",
    "origin": "https://example.com",
    "jwk": {
      "kty": "RSA",
      "e": "AQAB",
      "use": "enc",
      "n": "vHtaFM0e1ljAQ1Lnza95LdsBh10p78lz13rUdMe29vBESIeI912Fix514WXa97Ijh-pBuonFRcsyL0_-CF98rdhow6sZMhPdyOA9ud-PcAOwSHm-HrUUU_XkHGUVslBINAFOpOCYZh9qZ7jk6-5-Gk6MeyD4ok0BNz4XIKht_hj8yJQhphPz17hjguL9KPqK45HTl_D3SEStkbSaPK4fe-glMv2YJRh3nvdQYXkm-0cDmx4nets_4SH8U5DUwoFAB-Zh30-KHHe2nGbCYNrh7oUOEoC7mmF90HG0jwsbI5KSNDStckQ8pEZhpppVWyPh0CjzOmDidlkjUZ8hMJARWw",
      "kid": "008vKoQ3ycDeaUxLN6bPlfk9cjIjqSrb"
    }
  },
  "ctx": [
    {
      "data": {
        "clientLibraryIntegrity": " CLIENT LIBRARY INTEGRITY VALUE GOES HERE",
        "clientLibrary": "CLIENT LIBRARY VALUE GOES HERE",
        "allowedCardNetworks": [
          "VISA",
          "MASTERCARD",
          "AMEX",
          "MAESTRO",
          "DISCOVER",
          "DINERSCLUB",
          "JCB",
          "CUP",
          "CARTESBANCAIRES"
        ],
        "targetOrigins": [
          "https://example.com"
        ],
        "mfOrigin": "https://example.com",
        "allowedPaymentTypes": [
          "CARD"
        ]
      },
      "type": "mf-2.1.0"
    }
  ]
}
```

Capture Context Request for Accepting `eCheck` Information

```
{
  "clientVersion": "v2",
  "targetOrigins": [
    "https://www.example.com",
    "https://www.basket.example.com",
    "https://ecom.example.com"
  ],
  "allowedPaymentTypes": ["CHECK"]
}
```

Successful Encrypted JWT Response for Accepting `eCheck` Information

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiJtdnkwVk9OVk40bzA4bTRGQjhmU3FCQUFFS0JWOTdlNnR2VDd4cHdqaFkwMDRydFJ1dGI0R2YwWlNwNGdNeEkvanBVSWxFblZKa2JtUVNHaWFnUEdGc0NPazdMbHJGTHFKcXN2eitoTHhrY08xRkFcdTAwM2QiLCJvcmlnaW4iOiJodHRwczovL3N0YWdlZmxleC5jeWJlcnNvdXJjZS5jb20iLCJqd2siOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJuIjoidmRpN0gtM1MzMTkyZlc5WC1BTmpvdjlFdXU4ZGxPOTBtU2gyUGVyMF9PdHZ4YlJITTBrakZpTHlKaGQwUUR3VlNWbUlhRFc2aGtCa1k2Ui1lcWRnaTdUVUNGZEQ3UUU1ckNkZGhZZTIycTh0RUNQZkpOWWJ6STZZTVBxTkFyYWc5LUhhWVo1X2tOX0JvMm5EclN4RFJ0MHBDbGxyd2d2Q1ZLb2M0RWF6ZE93QUE4dnI2VVh4Ty1SWVI2Z1R5VEZia244Q2hDVHNvWDByam5VWVI1VjdRaE95YzMzWEJUTVNDYTVBOHFQNDZnZXpvQjZ0dDA0SlQtRVVMWE9vYndVcVdvd0E3TTJzWUYydkFoQkVuMmt0REJFWVJSN3E0aWEyVHRIS1JPUW9FTjhZNjNiNFNaTGZDQk82cEc2QXpnSWpya3RkQXhIOXR0WURYdFJYS1YxeTN3Iiwia2lkIjoiMDBiQlN1d3VpdGtYeExROGFISWloMm5qMFhQNFpXYUsifX0sImN0eCI6W3siZGF0YSI6eyJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LXZkWWkxaDV1ZTNwcm5iVC8xYThJSkxlUkNrSGVqSHBkRGR3My95RkxaREFcdTAwM2QiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL21pY3JvZm9ybS9idW5kbGUvdjIuNS4xL2ZsZXgtbWljcm9mb3JtLm1pbi5qcyIsInRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly90aGUtdXAtZGVtby5hcHBzcG90LmNvbSJdLCJtZk9yaWdpbiI6Imh0dHBzOi8vc3RhZ2VmbGV4LmN5YmVyc291cmNlLmNvbSIsImFsbG93ZWRQYXltZW50VHlwZXMiOlsiQ0hFQ0siXX0sInR5cGUiOiJtZi0yLjEuMCJ9XSwiaXNzIjoiRmxleCBBUEkiLCJleHAiOjE3MzM0OTAxODEsImlhdCI6MTczMzQ4OTI4MSwianRpIjoiSXdEdHAxZkVZM2QwYUh6OSJ9.arokacvdTSUIehBY0ICi__2szuCdrvykJZq4T69n4OcWGym5PErJO0moJD-QYynhFj7_0k-G39qbkNJydB3UyF2qJSaqwZiopO27kuqk8u9Z0cY-V9Nu04JgaV4s18doxnzx6vdTCC3krrIcxeINi23Qu-Szcpg7aaGvPVXMC0DVC14WUQiGJkOakJ54jWtl2VoFAgYziUMcYYpk4hxLVxurBtT7lvrfCXKoyWtxiUxoEpOc_Td_qi5nA8ByWUaieQmp1Zej61khQJ_hmXtlsAt4BqxeJWoJeR_5Sjz0vD5y4-oAeNNrAulDem7CKiRJQbI9fyqT-H5Cmjd6YQchxQ
```

Decrypted Capture Context Body with Selected Fields for Accepting `eCheck` Information

```
{
  "flx": {
    "path": "/flex/v2/tokens",
    "data": "mvy0VONVN4o08m4FB8fSqBAAEKBV97e6tvT7xpwjhY004rtRutb4Gf0ZSp4gMxI/jpUIlEnVJkbmQSGiagPGFsCOk7LlrFLqJqsvz+hLxkcO1FA=",
    "origin": "https://example.com",
    "jwk": {
      "kty": "RSA",
      "e": "AQAB",
      "use": "enc",
      "n": "vdi7H-3S3192fW9X-ANjov9Euu8dlO90mSh2Per0_OtvxbRHM0kjFiLyJhd0QDwVSVmIaDW6hkBkY6R-eqdgi7TUCFdD7QE5rCddhYe22q8tECPfJNYbzI6YMPqNArag9-HaYZ5_kN_Bo2nDrSxDRt0pCllrwgvCVKoc4EazdOwAA8vr6UXxO-RYR6gTyTFbkn8ChCTsoX0rjnUYR5V7QhOyc33XBTMSCa5A8qP46gezoB6tt04JT-EULXOobwUqWowA7M2sYF2vAhBEn2ktDBEYRR7q4ia2TtHKROQoEN8Y63b4SZLfCBO6pG6AzgIjrktdAxH9ttYDXtRXKV1y3w",
      "kid": "00bBSuwuitkXxLQ8aHIih2nj0XP4ZWaK"
    }
  },
  "ctx": [
    {
      "data": {
        "clientLibraryIntegrity": "CLIENT LIBRARY INTEGRITY VALUE GOES HERE",
        "clientLibrary": "CLIENT LIBRARY VALUE GOES HERE ",
        "targetOrigins": [
          "https://the-up-demo.appspot.com"
        ],
        "mfOrigin": "https://example.com",
        "allowedPaymentTypes": [
          "CHECK"
        ]
      },
      "type": "mf-2.1.0"
    }
  ],
  "iss": "Flex API",
  "exp": 1733490181,
  "iat": 1733489281,
  "jti": "IwDtp1fEY3d0aHz9"
}
```

Getting Started Examples {#flex-getting-started-examples-v2}
============================================================

Example: Checkout Payment Form for Accepting Card Information
This simple payment form captures the name, PAN, CVN, month, and year, and a pay button for submitting the information.
Back to [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-cs-setup.md "").

```
&lt;h1&gt;Checkout&lt;/h1&gt;
&lt;div id="errors-output" role="alert"&gt;&lt;/div&gt;
&lt;form action="/token" id="my-sample-form" method="post"&gt;
    &lt;div class="form-group"&gt;
        &lt;label for="cardholderName"&gt;Name&lt;/label&gt;
        &lt;input id="cardholderName" class="form-control" name="cardholderName" placeholder="Name on the card"&gt;
        &lt;label id="cardNumber-label"&gt;Card Number&lt;/label&gt;
        &lt;div id="number-container" class="form-control"&gt;&lt;/div&gt;
        &lt;label for="securityCode-container"&gt;Security Code&lt;/label&gt;
        &lt;div id="securityCode-container" class="form-control"&gt;&lt;/div&gt;
    &lt;/div&gt;

    &lt;div class="form-row"&gt;
        &lt;div class="form-group col-md-6"&gt;
            &lt;label for="expMonth"&gt;Expiry month&lt;/label&gt;
            &lt;select id="expMonth" class="form-control"&gt;
                &lt;option&gt;01&lt;/option&gt;
                &lt;option&gt;02&lt;/option&gt;
                &lt;option&gt;03&lt;/option&gt;
                &lt;option&gt;04&lt;/option&gt;
                &lt;option&gt;05&lt;/option&gt;
                &lt;option&gt;06&lt;/option&gt;
                &lt;option&gt;07&lt;/option&gt;
                &lt;option&gt;08&lt;/option&gt;
                &lt;option&gt;09&lt;/option&gt;
                &lt;option&gt;10&lt;/option&gt;
                &lt;option&gt;11&lt;/option&gt;
                &lt;option&gt;12&lt;/option&gt;
            &lt;/select&gt;
        &lt;/div&gt;
        &lt;div class="form-group col-md-6"&gt;
            &lt;label for="expYear"&gt;Expiry year&lt;/label&gt;
            &lt;select id="expYear" class="form-control"&gt;
                &lt;option&gt;2021&lt;/option&gt;
                &lt;option&gt;2022&lt;/option&gt;
                &lt;option&gt;2023&lt;/option&gt;
            &lt;/select&gt;
        &lt;/div&gt;
    &lt;/div&gt;

    &lt;button type="button" id="pay-button" class="btn btn-primary"&gt;Pay&lt;/button&gt;
    &lt;input type="hidden" id="flexresponse" name="flexresponse"&gt;
&lt;/form&gt;
```

Example: Checkout Payment Form for Accepting `eCheck` Information
This simple payment form captures the name, PAN, CVN, month, and year, and a pay button for submitting the information.
Back to [Client-Side Setup](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-cs-setup.md "").

```
&lt;h1&gt;Checkout&lt;/h1&gt;
&lt;div id="errors-output" role="alert"&gt;&lt;/div&gt;
&lt;form action="/token" id="my-sample-form" method="post"&gt;
    &lt;div class="form-group"&gt;
        &lt;label id="routingNumber-label"&gt;Routing Number&lt;/label&gt;
        &lt;div id="routingNumber-container" class="form-control"&gt;&lt;/div&gt;
        &lt;label for="accountNumber-label"&gt;Account Number&lt;/label&gt;
        &lt;div id="accountNumber-container" class="form-control"&gt;&lt;/div&gt;
        &lt;label for="accountNumberConfirm-label"&gt;Account Number Confirm&lt;/label&gt;
        &lt;div id="accountNumberConfirm-container" class="form-control"&gt;&lt;/div&gt;
    &lt;/div&gt;

    &lt;div class="form-row"&gt;
        &lt;div class="form-group col-md-6"&gt;
            &lt;label for="accountType"&gt;Account Type&lt;/label&gt;
            &lt;select id="accountType" name="accountType" class="form-control"&gt;
                &lt;option value="C"&gt;Checking&lt;/option&gt;
                &lt;option value="S"&gt;Savings&lt;/option&gt;
                &lt;option value="X"&gt;Corporate checking&lt;/option&gt;
            &lt;/select&gt;
        &lt;/div&gt;
    &lt;/div&gt;

    &lt;button type="button" id="pay-button" class="btn btn-primary"&gt;Pay&lt;/button&gt;
    &lt;input type="hidden" id="flexresponse" name="flexresponse"&gt;
&lt;/form&gt;
```

Example: Creating the Pay Button with Event Listener for Cards
Back to [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-time-limit-pay-card.md "").

```
payButton.('click', function () {

    // Compiling MM & YY into optional parameters
    const options = {
        expirationMonth: document.querySelector('#expMonth').value,
        expirationYear: document.querySelector('#expYear').value
    };
    //
    microform.createToken(options, function (err, token) {
        if (err) {
            // handle error
            console.error(err);
            errorsOutput.textContent = err.message;
        } else {
            // At this point you may pass the token back to your server as you wish.
            // In this example we append a hidden input to the form and submit it.
            console.log(JSON.stringify(token));
            flexResponse.value = JSON.stringify(token);
            form.submit();
        }
    });
});
```

Example: Creating the Pay Button with Event Listener for Checks
Back to [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-time-limit-pay-bank.md "").

```
payButton.('click', function () {

  // Compiling account type into optional parameters
  var options = {
    accountType: document.querySelector('#accountType').value,
  };
  //
  microform.createToken(options, function (err, token) {
    if (err) {
      // handle error
      console.error(err);
      errorsOutput.textContent = err.message;
    } else {
      // At this point you may pass the token back to your server as you wish.
      // In this example we append a hidden input to the form and submit it.
      console.log(JSON.stringify(token));
      flexResponse.value = JSON.stringify(token);
      form.submit();
    }
  });
});
```

Example: Customer-Submitted Form with Card Information
Back to [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-time-limit-pay-card.md "").

```
&lt;script&gt;
    // Variables from the HTML form
    const form = document.querySelector('#my-sample-form');
    const payButton = document.querySelector('#pay-button');
    const flexResponse = document.querySelector('#flexresponse');
    const expMonth = document.querySelector('#expMonth');
    const expYear = document.querySelector('#expYear');
    const errorsOutput = document.querySelector('#errors-output');

    // the capture context that was requested server-side for this transaction
    const captureContext = &lt;% -keyInfo %&gt; ;
    // custom styles that will be applied to each field we create using Microform
    const myStyles = {
        'input': {
            'font-size': '14px',
            'font-family': 'helvetica, tahoma, calibri, sans-serif',
            'color': '#555'
        },
        ':focus': { 'color': 'blue' },
        ':disabled': { 'cursor': 'not-allowed' },
        'valid': { 'color': '#3c763d' },
        'invalid': { 'color': '#a94442' }
    };
    // setup Microform
    const flex = new Flex(captureContext);
    const microform = flex.microform({ styles: myStyles });
    const number = microform.createField('number', { placeholder: 'Enter card number' });
    const securityCode = microform.createField('securityCode', { placeholder: '•••' });
    number.load('#number-container');
    securityCode.load('#securityCode-container');


    // Configuring a Listener for the Pay button
    payButton.addEventListener('click', function () {

        // Compiling MM & YY into optional parameters
        const options = {
            expirationMonth: document.querySelector('#expMonth').value,
            expirationYear: document.querySelector('#expYear').value
        };
        //
        microform.createToken(options, function (err, token) {
            if (err) {
                // handle error
                console.error(err);
                errorsOutput.textContent = err.message;
            } else {
                // At this point you may pass the token back to your server as you wish.
                // In this example we append a hidden input to the form and submit it.
                console.log(JSON.stringify(token));
                flexResponse.value = JSON.stringify(token);
                form.submit();
            }
        });
    });
&lt;/script&gt;
```

Example: Customer-Submitted Form with `eCheck` Information
Back to [Transient Token Time Limit](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-time-limit-pay-bank.md "").

```
&lt;script&gt;
    // Variables from the HTML form
    const form = document.querySelector('#my-sample-form');
    const payButton = document.querySelector('#pay-button');
    const flexResponse = document.querySelector('#flexresponse');
    const accountType = document.querySelector('#accountType')
    const errorsOutput = document.querySelector('#errors-output');

    // the capture context that was requested server-side for this transaction
    const captureContext = &lt;% -keyInfo %&gt; ;
    // custom styles that will be applied to each field we create using Microform
    const myStyles = {
        'input': {
            'font-size': '14px',
            'font-family': 'helvetica, tahoma, calibri, sans-serif',
            'color': '#555'
        },
        ':focus': { 'color': 'blue' },
        ':disabled': { 'cursor': 'not-allowed' },
        'valid': { 'color': '#3c763d' },
        'invalid': { 'color': '#a94442' }
    };
    // setup Microform
    const flex = new Flex(captureContext);
    const microform = flex.microform("check", { styles: myStyles });
    const routingNumber = microform.createField("routingNumber", { placeholder: "Enter routing number" });
    const accountNumber = microform.createField("accountNumber", { placeholder: "Enter account number" });
    const accountNumberConfirm = microform.createField("accountNumberConfirm", { placeholder: "accountNumberConfirm" });
    routingNumber.load('#routingNumber-container')
    accountNumber.load('#accountNumber-container')
    accountNumberConfirm.load('#accountNumberConfirm-container')


    // Configuring a Listener for the Pay button
    payButton.addEventListener('click', function () {

        // Compiling MM & YY into optional parameters
        const options = {
            accountType: document.querySelector('#accountType').value,
        };
        //
        microform.createToken(options, function (err, token) {
            if (err) {
                // handle error
                console.error(err);
                errorsOutput.textContent = err.message;
            } else {
                // At this point you may pass the token back to your server as you wish.
                // In this example we append a hidden input to the form and submit it.
                console.log(JSON.stringify(token));
                flexResponse.value = JSON.stringify(token);
                form.submit();
            }
        });
    });
&lt;/script&gt;
```

Example: Token Payload with Card Information
Back to [Transient Token Response Format](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-response-format-pay-card.md "").

```
{
  "iss": "Flex/00",
  "exp": 1728911080,
  "type": "mf-2.0.0",
  "iat": 1728910180,
  "jti": "1D1S6JK9RL6EK667H1I370689A63I2I8YLFJSPJ1EUSKIPMJJWEL670D16E89AF8",
  "content": {
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2025"
        },
        "number": {
          "detectedCardTypes": [
            "001"
          ],
          "maskedValue": "XXXXXXXXXXXX1111",
          "bin": "411111"
        },
        "securityCode": {},
        "expirationMonth": {
          "value": "01"
        }
      }
    }
  }
}

```

Example: Token Payload with `eCheck` Information
Back to [Transient Token Response Format](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/transient-token-response-format-pay-bank.md "").

```
{
  "iss" : "Flex/00",
  "exp" : 1732527524,
  "type" : "mf-2.1.0",
  "iat" : 1732526624,
  "jti" : "1D3HRVI3KM4HFWQAZ2JFI993NEVBAH5NYJFIH82RAMYWDUJ444KT674445A4EAC0",
  "content" : {
    "paymentInformation" : {
      "bank" : {
        "routingNumber" : { },
        "account" : {
          "number" : { },
          "type" : { }
        }
      },
      "paymentType" : {
        "name" : {
          "value" : "CHECK"
        }
      }
    }
  }
}
```

Example: Token Payload with Multiple Card Types
Back to [Transient Token Response Format](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/transient-token-response-format-pay-card.md "").

```
{
  "iss": "Flex/08",
  "exp": 1661350495,
  "type": "mf-2.0.0",
  "iat": 1661349595,
  "jti": "1C174LLWIFFR9OV0V0IJQOY0IB1JQP70ZNF4TBI3V6H3AIOY0W1T6306325F91C0",
  "content": {
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2023"
        },
        "number": {
          "detectedCardTypes": [
            "042",
            "036"
          ],
          "maskedValue": "XXXXXXXXXXXX1800",
          "bin": "501767"
        },
        "securityCode": {},
        "expirationMonth": {
          "value": "01"
        }
      }
    }
  }
}
```

Example: Capture Context Public Key
Back to [Validating the Transient Token for Accepting Card Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/validating-the-transient-token-pay-card.md "") and [Validating the Transient Token for Accepting `eCheck` Information](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-bank/micro-getting-started-pay-bank-trans-tkn/validating-the-transient-token-pay-bank.md "").

```
"jwk": {
                "kty": "RSA",
                "e": "AQAB",
                "use": "enc",
                "n": "3DhDtIHLxsbsSygEAG1hcFqnw64khTIZ6w9W9mZNl83gIyj1FVk-H5GDMa85e8RZFxUwgU_zQ0kHLtONo8SB52Z0hsJVE9wqHNIRoloiNPGPQYVXQZw2S1BSPxBtCEjA5x_-bcG6aeJdsz_cAE7OrIYkJa5Fphg9_pxgYRod6JCFjgdHj0iDSQxtBsmtxagAGHjDhW7UoiIig71SN-f-gggaCpITem4zlb5kkRVvmKMUANe4B36v4XSSSpwdP_H5kv4JDz_cVlp_Vy8T3AfAbCtROyRyH9iH1Z-4Yy6T5hb-9y3IPD8vlc8E3JQ4qt6U46EeiKPH4KtcdokMPjqiuQ",
                "kid": "00UaBe20jy9VkwZUQPZwNNoKFPJA4Qhc"    }
```

Example: Authorization with a Transient Token Using the REST API
Back to [Using the Transient Token to Process a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/microform-integ-v2/micro-getting-started-pay-card/micro-getting-started-pay-card-trans-tkn/using-transient-token-pay-card.md "").

```
{
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "102.21",
            "currency": "USD"
        },
        "billTo": {
            "firstName": "Tanya",
            "lastName": "Lee",
            "address1": "1234 Main St.",
            "locality": "Small Town",
            "administrativeArea": "MI",
            "postalCode": "98765-4321",
            "country": "US",
            "district": "MI",
            "buildingNumber": "123",
            "email": "tanyalee@example.com",
            "phoneNumber": "987-654-3210"
        }
    },
    "tokenInformation": {
        "transientTokenJwt": "eyJraWQiOiIwN0JwSE9abkhJM3c3UVAycmhNZkhuWE9XQlhwa1ZHTiIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjp7ImV4cGlyYXRpb25ZZWFyIjoiMjAyMCIsIm51bWJlciI6IjQxMTExMVhYWFhYWDExMTEiLCJleHBpcmF0aW9uTW9udGgiOiIxMCIsInR5cGUiOiIwMDEifSwiaXNzIjoiRmxleC8wNyIsImV4cCI6MTU5MTc0NjAyNCwidHlwZSI6Im1mLTAuMTEuMCIsImlhdCI6MTU5MTc0NTEyNCwianRpIjoiMUMzWjdUTkpaVjI4OVM5MTdQM0JHSFM1T0ZQNFNBRERCUUtKMFFKMzMzOEhRR0MwWTg0QjVFRTAxREU4NEZDQiJ9.cfwzUMJf115K2T9-wE_A_k2jZptXlovls8-fKY0muO8YzGatE5fu9r6aC4q7n0YOvEU6G7XdH4ASG32mWnYu-kKlqN4IY_cquRJeUvV89ZPZ5WTttyrgVH17LSTE2EvwMawKNYnjh0lJwqYJ51cLnJiVlyqTdEAv3DJ3vInXP1YeQjLX5_vF-OWEuZfJxahHfUdsjeGhGaaOGVMUZJSkzpTu9zDLTvpb1px3WGGPu8FcHoxrcCGGpcKk456AZgYMBSHNjr-pPkRr3Dnd7XgNF6shfzIPbcXeWDYPTpS4PNY8ZsWKx8nFQIeROMWCSxIZOmu3Wt71KN9iK6DfOPro7w"
    }
}
```

JSON Web Tokens {#micro-appendix-jwts}
======================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```
* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```
* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#micro-appendix-jwts_d35e34}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

Browser Support {#microform-integ-browsers-v2}
==============================================

Microform Integration is supported on these browsers and versions:

* Chrome 80 or later
* Edge 109 or later
* Firefox 115 or later
* Opera 106 or later
* Safari 13 or later

PCI DSS Guidance {#pcidss-guidance-v2_PCIDSSGuidance}
=====================================================

Any merchant accepting payments must comply with the PCI Data Security Standards (PCI DSS). `Microform Integration`'s approach facilitates PCI DSS compliance through self-assessment and the storage of sensitive PCI information.

Self-Assessment Questionnaire {#pcidss-guidance-v2_id18ABAB0M030}
-----------------------------------------------------------------

`Microform Integration` handles the card number input and transmission from within iframe elements served from `Cybersource` controlled domains. This approach can qualify merchants for [SAQ A](https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf "")-based assessments. Related fields, such as card holder name or expiration date, are not considered sensitive when not accompanied by the PAN.

Storing Returned Data {#pcidss-guidance-v2_id18ABAC0B0RO}
---------------------------------------------------------

Responses from `Microform Integration` are stripped of sensitive PCI information such as card number. Fields included in the response, such as card type and masked card number, are not subject to PCI compliance and can be safely stored within your systems. If you collect the CVN, note that it can be used for the initial authorization but not stored for subsequent authorizations.

WCAG 2.2 Compliance {#WCAG_compliance_v2}
=========================================

Your integration must be compliant with the Web Content Accessibility Guidelines (WCAG 2.2) in order to meet accessibility standards and regulations. `Microform Integration` is designed with these guidelines in mind but some accessibility compliance is dependent on your integration, particularly the custom styling of fields. This section contains the minimum required information to ensure that `Microform Integration` is compliant with WCAG 2.2.
`Microform Integration` automatically handles many accessibility requirements, but the hosting page and custom styling elements are your responsibility. The parent page that contains `Microform Integration` must meet WCAG 2.2 standards. This includes proper heading structure, page titles, and other accessibility requirements. All fields that are rendered in `Microform Integration` are automatically assigned as aria-required set to `true`. The parent page must implement clear visual indicators to indicate that these fields are required for users. For information about WCAG 2.2 guidelines, see the [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/ "") on the W3C website.

Font Configuration
------------------

You must follow these guidelines when you apply custom styles to `Microform Integration`:

* Set the font size to at least 16px (1rem) for input fields.
* Select font families that are compatible with screen readers and assistive technologies.
* Set a line height that is at least 1.5 times the font size.

This is an example `Microform Integration` font configuration:

```
// define accessible custom styles
var customStyles = {
    'input': {
        'font-size': '16px',
        'family': 'Arial, sans-serif',
        'lineHeight': '1.5'
    }
}
// apply styles to all fields
var microform = flex.microform({ styles: customStyles });
```

Color and Contrast
------------------

Follow these guidelines to ensure that visibility is compliant for all users:

* Maintain a minimum contrast ratio of 4.5:1 between text and background colors.
* Do not rely solely on color to convey information.
* Implement distinct focus states using both color changes and other visual indicators.
* Use the `flex-microform-focused` class for consistent focus indication.

This is an example of color and contrast configuration for `Microform Integration`:

```
/* add a visual indicator for focus */
.flex-microform-focused {
  background: lightyellow;
}
```

Handle Errors
-------------

`Microform Integration` provides managed classes to indicate field validation states. You must handle any errors that are returned by the createToken method. Follow these guidelines to handle errors:

* Implement error handling that programmatically associates error messages with their respective form fields.
* Associate all helper text with its corresponding form control by setting aria-describedby to `helperTextId`. `helperTextId` is the unique ID of the helper text container element.
* Use the MicroformError object to determine to which fields the error applies.
* Ensure that all error messages are clear, descriptive, and concise.
* Make error messages visible and properly announced by screen readers.

This is an example MicroformError object:

```
{
  "name": "MicroformError",
  "reason": "CREATE_TOKEN_VALIDATION_FIELDS",
  "message": "One or more fields have a validation error.",
  "informationLink": "https://www.cybersource.com/products/payment_security/secure_acceptance",
  "details": [
    {
      "message": "Validation error",
      "location": "number"
    }
  ]
}
```

Testing
-------

Follow these guidelines to verify that your integration is compliant before you deploy:

* Test keyboard navigation through the entire payment form.


* Validate that your implementation works with screen readers (NVDA, JAWS, VoiceOver).


* Run automated accessibility checks with tools such as Axe or Lighthouse.


* Conduct manual testing with common assistive technologies.
  When you follow these guidelines, your `Microform Integration` implementation maintains compliance with WCAG 2.2 while you provide an accessible payment experience for all users.

Test Card Numbers {#da-reference-test-cards}
============================================

Use these test card numbers to test your `Microform Integration` configuration.
Combine the BIN with the card number when sending to `Microform Integration`.

|    Card Brand    |  BIN   | Card Number  | Expiration Date | CVV  |
|------------------|--------|--------------|-----------------|------|
| Visa             | 424242 | 4242424242   | 12/2024         | 123  |
| Mastercard       | 555555 | 5555554444   | 02/2025         | 265  |
| American Express | 378282 | 246310005    | 03/2026         | 7890 |
| Cartes Bancaires | 436000 | 0001000005   | 04/2040         | 123  |
| Carnet           | 506221 | 0000000009   | 04/2024         | 123  |
| China UnionPay   | 627988 | 6248094966   | 04/2040         | 123  |
| Diners Club      | 305693 | 09025904     | 04/2040         | 123  |
| Discover         | 644564 | 4564456445   | 04/2040         | 123  |
| JCB              | 353011 | 13333 0000   | 04/2040         | 123  |
| Maestro          | 675964 | 9826438453   | 04/2040         | 123  |
| Mada             | 446404 | 0000000007   | 04/2040         | 123  |
| ELO              | 451416 | 0000000003   | 04/2040         | 123  |
| JCrew            | 515997 | 1500000005   | 04/2040         | 123  |
| EFTPOS           | 401795 | 000000000009 | 04/2040         | 123  |
| Meeza            | 507808 | 3000000002   | 04/2040         | 123  |
[Test Card Numbers]

Introduction to `Unified Checkout` {#uc-intro}
==============================================

`Unified Checkout` provides a single interface with which you can accept numerous types of digital payments. `Unified Checkout` calls other follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `Token Management Service` (`TMS`).
`Unified Checkout` consists of a server-side component and a client-side JavaScript library.
The server-side component authenticates your merchant identity and instructs the system to act within your payment environment. The response contains limited-use public keys. The keys are for end-to-end encryption and contain merchant-specific payment information that drives the interaction of the application. The client-side JavaScript library dynamically and securely places digital payment options onto your e-commerce page.
The provided JavaScript library enables you to securely accept many payment options within your e-commerce environment. `Unified Checkout` can be embedded seamlessly into your existing webpage, simplifying payment acceptance.
When a customer selects a payment method from the button widget, `Unified Checkout` handles all of the interactions with the digital payment that was chosen. `Unified Checkout` is also able to orchestrate requests for to follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `TMS` before it provides a response to your e-commerce system.
The figure below shows `Unified Checkout` with customer checkout payment options.

#### Figure: {#uc-intro_fig-1}

Button Widget ![Example of the button widget interface and flow with various payment
options.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/button-widget-flow-865x475.svg/jcr:content/renditions/original)
For examples of different payment method UIs through `Unified Checkout`, see [Unified Checkout UI](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-ui-screens.md "").

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

`Unified Checkout` Flow {#uc-getting-started-integration-flow}
==============================================================

To integrate `Unified Checkout` into your platform, you must follow several integration steps. This section gives a high-level overview of how to integrate and launch `Unified Checkout` on your webpage and process a transaction. You can find the detailed specifications of the APIs later in this document.
The integration flow consists of four events:

1. You send a server-to-server API request for a capture context. This request is fully authenticated and returns a JSON Web Token (JWT) that is necessary in order to invoke the frontend JavaScript library. For information on setting up the server side, see [Server-Side Set Up](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup.md "").
2. You invoke the `Unified Checkout` JavaScript library using the JWT response from the capture context request. For information on setting up the client side, see [Client-Side Set Up](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro.md "").
3. You process the payment through the `Unified Checkout` complete mandate feature and interpret the response of the transaction flow that is displayed on your browser.

   > IMPORTANT
   > If you do not use the complete mandate for ` Unified Checkout `, you must request follow-on services using a transient token to process the payment.

4. **Optional:** `Cybersource` recommends that you capture the full payment response through webhook notifications.
   {#uc-getting-started-integration-flow_ol_p5w_55q_npb} Information that is captured by `Unified Checkout`, including the billing and shipping address, can be retrieved using the payment details API.
   The figure below shows the `Unified Checkout` payment flow.

#### Figure: {#uc-getting-started-integration-flow_fig_uc-payment-flow}

`Unified Checkout` Payment Flow
![Diagram that shows the sequence and flow of a Unified Checkout payment.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-srvorch-authdm-600x700.svg/jcr:content/renditions/original) For more information on the specific APIs referenced, see these topics:

* [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "")
* [Payment Details API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-token-get-pymnt-details.md "")

Enabling `Unified Checkout` in the `Business Center` {#uc-enabling-ebc}
=======================================================================

To begin using `Unified Checkout`, you must first ensure that your merchant ID (MID) is configured to use the service and that any payment methods you intend to use are properly set up.

1. Log in to the `Business Center`:
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc-enabling-ebc_ebc-test-cybs}
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc-enabling-ebc_ebc-prod-cybs}
   If you are unable to access this page, contact your sales representative. {#uc-enabling-ebc_step-1}
   {#uc-enabling-ebc_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout.{#uc-enabling-ebc_step-2}
   {#uc-enabling-ebc_step-2}

3. You can configure various payment methods such as Apple Pay, `Click to Pay`, and Google Pay. Click Manage and follow the instructions for your selected payment methods. When payment methods are enabled, they appear on the payment configuration page.
   IMPORTANT You must configure payment methods you want to use for each transacting MID.

   #### Figure: {#uc-enabling-ebc_uc-ui}

   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original) {#uc-enabling-ebc_step-3}

4. Click Manage to edit your existing payment method configurations or enroll in new payment methods as they are released.{#uc-enabling-ebc_step-4}
   {#uc-enabling-ebc_enable-uc}

Server-Side Set Up {#uc-getting-started-ss-setup}
=================================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the `Unified Checkout` frontend components will function. The sessions API request contains parameters that define how `Unified Checkout` performs.
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

{#uc-getting-started-ss-setup_ul_atq_bwq_npb}
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Capture Context {#uc-capture-context-intro}
===========================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how `Unified Checkout` performs.
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types. The capture context request includes these elements:
* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigin
* completeMandate

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Safari 16
* Firefox 121
* Google Chrome/Chium-based browsers 118
* Microsoft Edge 118

Capture Context Example {#uc-capture-context-intro_uc-capture-context-codeblock}
--------------------------------------------------------------------------------

Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context. Use the completeMandate to orchestrate follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `TMS`. For example:

```
{
  "targetOrigins" : [ "https://test.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "CAPTURE",
        "decisionManager": true,
        "consumerAuthentication": true,
        "tms": {
            "tokenCreate": true,
            "tokenTypes": [
                "customer",
                "paymentInstrument",
                "instrumentIdentifier",
                "shippingAddress"
            ]
        }
    },
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

Card Entry Form {#uc-capture-context-intro_uc-capture-context-diagram}
----------------------------------------------------------------------

This diagram shows how elements of the capture context request appear in the card entry form.

#### Figure:

Anatomy of a Manual Card Entry Form ![Image of the capture context request code and how it appears in the
entry form elements.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/anatomy-of-manual-card-entry-form-685x575.svg/jcr:content/renditions/original)

Client-Side Set Up {#uc-getting-started-cs-setup-intro}
=======================================================

This section contains the information you need to set up the client side. You use the `Unified Checkout` JavaScript library to add the payment interface to your e-commerce site. It has two primary components:

* The button widget, which lists the payment methods available to the customer.
* The payment acceptance page, which captures payment information from the cardholder. You can set up the payment acceptance page to be embedded with your webpage or added as a sidebar.

Follow these steps to set up the client:

1. Load the JavaScript library.
2. Initialize the accept object, the capture context JWT. For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
3. Initialize the unified payment object with optional parameters.
4. Show the button list or payment acceptance page or both.
5. Process the payment request using the instructions included within the capture mandate.

{#uc-getting-started-cs-setup-intro_ul_m5t_gwq_npb}
The response to these interactions is a transient token that you can use to retrieve the payment information captured by the UI.

Loading the JavaScript Library and Invoking the Accept Function {#uc-getting-started-cs-js-library-intro}
=========================================================================================================

Use the client library asset path and client library integrity value that is returned by the capture context response to invoke `Unified Checkout` on your page.
You can retrieve these values from the clientLibrary and clientLibraryIntegrity fields that are returned in the JWT from `https://apitest.cybersource.com``/up/v1/capture-contexts`. You can use these values to create your script tags.
You must perform this process for each transaction, as these values may be unique for each transaction. You must avoid hard-coding values for the clientLibrary and clientLibraryIntegrity fields to prevent client-side errors.
For example, a response from `https://apitest.cybersource.com``/up/v1/capture-contexts` would include:

```
"data": {
    "clientLibrary":"[EXTRACT clientLibrary VALUE from here]",
    "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]"
}
```

Below is an example script tag:

```
&lt;script src="[INSERT clientLibrary VALUE HERE]"
    integrity=”[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous”&gt;&lt;/script&gt;
```

> IMPORTANT
> Use the clientLibrary and clientLibraryIntegrity parameter values in the capture context response to obtain the ` Unified Checkout ` JavaScript library URL and the integrity value. This ensures that you are always using the most up-to-date library and protects against fraud. Do not hard-code the ` Unified Checkout ` JavaScript library URL or integrity value.
> When you load the library, the capture context from your initial server-side request is used to invoke the accept function.

JavaScript Example: Initializing the SDK {#uc-getting-started-cs-js-library-example}
====================================================================================

```
try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);


      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
```

In this example, `captureContext` refers to the capture context JWT.

JavaScript Example: Displaying the Button List {#uc-getting-started-cs-js-button-example}
=========================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the embedded `Unified Checkout` tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named components that are replaced with `Unified Checkout`'s iframes.

```
try {
    const accept = await Accept(captureContext);
    const up = await accept.unifiedPayments(sidebar);
    const tt = await up.show(showArgs);
} catch (error) {
    // merchant logic for handling issues
    console.error("something went wrong: " + error);
}
```

To display the `Unified Checkout` Button List within your payment page, a call is made to the unifiedPayments.Show() function. This function accepts a JSON object that links the `&lt;div&gt;` tags within your payment page to place the `Unified Checkout` button list and optional embeddable payment page.

```
const showArgs = {
    containers: {
        paymentSelection: '#buttonPaymentListContainer',
        paymentScreen: '#embeddedPaymentContainer'
    }
};
```

The response to the unifiedPayment.show() method is a JWT data object referred to here as a transient token. The transient token contains all the payment information captured during the `Unified Checkout` payment journey.

JavaScript Example: Client-Defined Trigger for `Click to Pay` or PAN Entry {#uc-getting-started-cs-js-trigger-ctp-pan-exampl}
=============================================================================================================================

When you display `CLICKTOPAY` or `PANENTRY` as allowed payment types, you can load the UI without displaying the `Unified Checkout` checkout button. You can do this by creating a trigger that defines what event loads the UI.
You can create a trigger by calling the `createTrigger()` method on an existing unified payments object and pass in these two parameters:

* The payment method that the trigger is linked to. This is required.
* The container for the payment screen. It is required when you are in embedded mode. IMPORTANT

  > You can create a trigger only for ` CLICKTOPAY ` or ` PANENTRY ` payment methods.

```
// Example: Basic usage with full sidebar experience
// Create a trigger
const trigger = up.createTrigger("CLICKTOPAY");

// Show the trigger
// In this example, when a button in your UI is clicked
const myButton = document.getElementById("myButton");

myButton.addEventListener("click", async () =&gt; {
  const transientToken = await trigger.show();
  console.log(transientToken);
})
```

```
// Example: Payment screen in a container
// Define the container for the payment screen to be rendered in
var options = { containers: { paymentScreen: '#paymentScreenContainer' } };
// Create the trigger
const trigger = up.createTrigger("CLICKTOPAY", options);

// Show the trigger
// In this example, when a button in your UI is clicked
const myButton = document.getElementById("myButton");

myButton.addEventListener("click", async () =&gt; {
  const transientToken = await trigger.show();
  console.log(transientToken);
})
```

> IMPORTANT
> When you use the ` createTrigger() ` method for ` Click to Pay `, you must create a custom UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-ui-ux.md "").

JavaScript Example: Processing a Payment {#uc-getting-started-cs-js-payment-example}
====================================================================================

Payment is initiated when `Unified Checkout` captures the customer's payment information by calling the `unifiedPayment.complete()` function and passing the transient token. IMPORTANT

> If you are updating an existing ` Unified Checkout ` configuration to use the complete mandate, you must update your JavaScript to include the unifedPayment.complete() function.

```
try {
    const accept = await Accept(captureContext);
    const up = await accept.unifiedPayments(sidebar);
    const tt = await up.show(showArgs);
    const completeResponse = await up.complete(tt);

    console.log(completeResponse); // merchant logic for handling complete response
} catch (error) {
    // merchant logic for handling issues
    console.error("something went wrong: " + error);
}
}
```

When you include this in your capture context, `Unified Checkout` is leveraged to initiate payment and any follow-on services that you include in your capture context request. Alternatively, you can call the payment APIs directly. See [Authorizations with a Transient Token](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-auth-tokens.md "").

Complete Integration Examples {#uc-getting-started-button-widget-intro}
=======================================================================

These examples show a full `Unified Checkout` integration and use the complete method for processing a payment.

JavaScript Example: Setting Up with Full Sidebar {#uc-getting-started-button-widget-sidebar}
============================================================================================

```
&lt;html&gt;
&lt;head&gt;
  &lt;script
    src="[INSERT clientLibrary VALUE HERE]"
    integrity="[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Unified Checkout Integration&lt;/h1&gt;
  &lt;input
    type="hidden"
    name="captureContext"
    value="[INSERT captureContext HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
const showArgs = { containers: {
paymentSelection: '#buttonPaymentListContainer',
}
};

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);

        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
```

JavaScript Example: Setting Up with the Embedded Component {#uc-getting-started-button-widget-embedded}
=======================================================================================================

The main difference between using an embedded component and the sidebar is that the accept.unifiedPayments object is set to `false`, and the location of the payment screen is passed in the containers argument.

> IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the side bar.

```
&lt;html&gt;
&lt;head&gt;
  &lt;script
    src="[INSERT clientLibrary VALUE HERE]"
    integrity="[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Unified Checkout Integration&lt;/h1&gt;
  &lt;input
    type="hidden"
    name="captureContext"
    value="[INSERT captureContext HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sidebar = false;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer",
paymentScreen:	'#embeddedPaymentContainer' }
    };

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);

        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
```

Transient Tokens {#uc-tokens-intro}
===================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the unifiedPayment.show() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.

Transient Token Format {#uc-tokens-format}
==========================================

The transient token is issued as a JSON Web Token (JWT) ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
The payload portion of the token is a Base64URL-encoded JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Example: Transient Token Format {#uc-trans-tkn-ex}
==================================================

Transient Token Payload

```
{
  "metadata" : {
    "sequenceNumber" : "1",
    "cardholderAuthenticationStatus" : false,
    "paymentType" : "PANENTRY"
  },
  "iss" : "Flex/00",
  "exp" : 1762870464,
  "type" : "gda-0.10.0",
  "iat" : 1762869564,
  "jti" : "1D4Q8FJSSZ9ASKQ9ZCJ7E13IFOITOOH2GGHY6TRZ3O28TUQ1BN8H691344C098CA",
  "content" : {
    "deviceInformation" : {
      "fingerprintSessionId" : { }
    },
    "orderInformation" : {
      "billTo" : {
        "country" : { },
        "lastName" : { },
        "firstName" : { },
        "phoneNumber" : { },
        "address1" : { },
        "postalCode" : { },
        "locality" : { },
        "buildingNumber" : { },
        "company" : {
          "name" : { }
        },
        "administrativeArea" : { },
        "email" : { }
      },
      "amountDetails" : {
        "totalAmount" : { },
        "currency" : { }
      },
      "shipTo" : {
        "firstName" : { },
        "lastName" : { },
        "country" : { },
        "address1" : { },
        "postalCode" : { },
        "locality" : { },
        "buildingNumber" : { },
        "administrativeArea" : { }
      }
    },
    "paymentInformation" : {
      "card" : {
        "expirationYear" : {
          "value" : "2027"
        },
        "number" : {
          "maskedValue" : "XXXXXXXXXXXX1111",
          "bin" : "411111"
        },
        "securityCode" : { },
        "expirationMonth" : {
          "value" : "03"
        },
        "typeSelectionIndicator" : {
          "value" : "1"
        },
        "type" : {
          "value" : "001"
        }
      }
    }
  }
}
```

IMPORTANT The empty field values in the transient token indicate which fields were captured by the application without exposing you to personally identifiable information directly.
PAN BIN in `metadata` Object
The `cardDetails` object, including the PAN BIN, is included in the transient token `metadata` when a `Click to Pay` network token is used as a payment method. This allows you to display information about the card on invoices and see the BIN details that are linked to the underlying card.

```
"metadata": {
  "cardDetails": {
    "suffix": "9876",
    "prefix": "123456",
    "expirationMonth": "MM",
    "expirationYear": "YYYY"
  }
}
```

Authentication Status in metadata Object
The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.
If you are using `Unified Checkout` with unifiedPayment.complete() and consumerAuthentication is set to `true` in the complete mandate request, then `Payer Authentication` is called automatically if it is available for the selected payment method and card network. If you use a transient token to request follow-on services directly, the value of this field indicates if the transaction has been authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

Token Verification {#uc-tokens-verification}
============================================

When you receive the transient token, you should cryptographically verify its integrity using the public key embedded within the capture context. Doing so verifies that `Cybersource` issued the token and that the data has not been tampered with in transit. Verifying the transient token JWT involves verifying the signature and various claims within the token. Programming languages each have their own specific libraries to assist. For an example in Java, see: [Java Example in Github](https://github.com/CyberSource/cybersource-unified-checkout-sample-java/blob/main/src/main/java/com/cybersource/example/service/JwtProcessorService.java "").

Dual-Branded Cards {#dual-co-brand-card-support}
================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["VISA", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Visa.
During the transaction, the card type is populated with the first network in the list, and the **detectedCardTypes** field returned in the transient token includes all of the detected card types in the transient token.
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Visa and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option selected by the customer during checkout.

Authorizations with a Transient Token {#uc-auth-tokens}
=======================================================

This section provides the information required in order to perform a successful authorization with a `Unified Checkout` transient token. You can use this method to construct more complex payment scenarios that are not supported by the `unifiedPayment.complete()` payment method.

> IMPORTANT
> When you process payments through ` Unified Checkout ` using unifiedPayments.complete() , ` Unified Checkout ` invokes service orchestration directly. When you send an authorization request using a transient token, you must request the follow-on services that you want to use. For information about the required fields for the payment services that you request, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").
> The transient token is a short-term token that expires after 15 minutes. Doing so eliminates the need to send sensitive payment data along with the request. For more information on transient tokens, see [Transient Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-tokens-intro.md "").
> To send the transient token with a request, use the tokenInformation.transientTokenJwt field.
> This example shows a transient token in the context of an authorization request:

```
"tokenInformation": {
    "transientTokenJwt": "eyJraWQiOiIwOG4zUnVsRTJGQXJDRktycVRkZFlkWGZSWFhMNXFoNSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzA3IiwiZXhwIjoxNTk3MDg0ODk3LCJ0eXBlIjoiZ2RhLTAuMS4xIiwiaWF0IjoxNTk3MDgzOTk3LCJqdGkiOiIxQzI2VlpSkVJUU1PTzVIMDUwNEtINDdJMEFNMklaRkM0M1Y1TDU0MUhCTE45Q09JM0w3NUYzMTk0RTE5NkExIn0.SNm1VZaZr3DkTqUg9CdV0F5arRe-uQU9oUWPKfWIpbIzIPZutRokv5DSDcM7asZIKNJyNIBx5DLsl_yQPrKgzhwQxZ8qbhto7cu3t-v8DHG2yO951plPQVQnj7x-vEDcXkLUL1F8sqY23R5HW-xSDAQ3AFLawCckn7Q2eudRGeuMhLWH742Gflf9Hz3KyKnmeNKA3o9yW2na16nmeVZaYGqbUSPVITdl5cMA0o9lEob8E3OQH0HHdmIsu5uMA4x7DeBjfTKD1rQxFP3JBNVcv30AIMLkNcw0pHbtHDVzKBWxUVxvnm3zFEdiBuSAco2uWhC9zFqHrrp64ZvzxZqoGA"
}
```

To retrieve non-sensitive data from a `Unified Checkout` transient token, use the `payment-details` endpoint. This data includes cardholder name and billing and shipping details. For more information, see [Payment Details API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-token-get-pymnt-details.md "").

> IMPORTANT Fields supplied directly in an API request supersede those that are also present in the transient token. For example, in the request below, the total amount might have been overridden because of a tax calculation.

Endpoint {#uc-auth-tokens_d9e16}
--------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#uc-auth-tokens_d9e25}
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#uc-auth-tokens_d9e35}
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/up/v1/capture-contexts`
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/up/v1/capture-contexts`

Required Field for an Authorization with a Transient Token {#uc-auth-tokens_auth-reqfields-rest}
------------------------------------------------------------------------------------------------

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

REST Example: Requesting an Authorization with a Transient Token {#uc-auth-tokens-ex-rest}
==========================================================================================

```keyword
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "processingInformation": {
    "commerceIndicator": "internet"
  },
  "tokenInformation": {
    "transientTokenJwt": "eyJraWQiOiIwOG4zUnVsRTJGQXJDRktycVRkZFlkWGZSWFhMNXFoNSIsImFs
ZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzA3IiwiZXhwIjoxNTk3MDg0ODk3LCJ0eXBlIjoiZ2RhLTAuMS4xIi
wiaWF0IjoxNTk3MDgzOTk3LCJqdGkiOiIxQzI2VlpSRkVJUU1PTzVIMDUwNEtINDdJMEFNMklaRkM0M1Y1TDU0
MUhCTE45Q09JM0w3NUYzMTk0RTE5NkExIn0.SNm1VZaZr3DkTqUg9CdV0F5arRe-uQU9oUWPKfWIpbIzIPZutR
okv5DSDcM7asZIKNJyNIBx5DLsl_yQPrKgzhwQxZ8qbhto7cu3t-v8DHG2yO951plPQVQnj7x-vEDcXkLUL1F8
sqY23R5HW-xSDAQ3AFLawCckn7Q2eudRGeuMhLWH742Gflf9Hz3KyKnmeNKA3o9yW2na16nmeVZaYGqbUSPVIT
dl5cMA0o9lEob8E3OQH0HHdmIsu5uMA4x7DeBjfTKD1rQxFP3JBNVcv30AIMLkNcw0pHbtHDVzKBWxUVxvnm3z
FEdiBuSAco2uWhC9zFqHrrp64ZvzxZqoGA"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "21.00",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1Market St",
      "address2": "Address 2",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com",
      "phoneNumber": "4158880000"
    }
  }
}
```

Capture Context API {#uc-setup-capture-context}
===============================================

The capture context request contains all of the merchant-specific parameters that tell the front-end JavaScript library what to do within your payment experience.
The capture context is a signed JSON Web Token (JWT) containing this information:

* Merchant-specific parameters that dictate the customer payment experience for the current payment transaction.
* A one-time public key that secures the information flow during the current payment transaction.

The capture context request includes these fields:

* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigins
  For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Allowed Card Networks
:
Use the allowedCardNetworks field to define the card types.

    These card networks are available for card entry:

    * American Express
    * Cartes Bancaires
    * Carnet
    * China UnionPay
    * Diners Club
    * Discover
    * EFTPOS
    * ELO
    * Jaywan
    * JCB
    * JCrew
    * KCP
    * mada
    * Maestro
    * Mastercard
    * Meeza
    * PayPak
    * UATP
    * Visa

    To support dual-branded or co-badged cards, you must list your supported card type values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Visa and Cartes Bancaires, and Cartes Bancaires is listed first, the card type is set to Cartes Bancaires after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-tokens-intro/dual-co-brand-card-support.md "").

    > IMPORTANT
    > Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). If you include only card types that do not have security codes in the allowedCardNetworks field, ` Unified Checkout ` does not display the security code field in the UI.
    > If you include card types that do not have security codes and cards types that do have security codes in the allowedCardNetworks field, ` Unified Checkout ` displays the security code field in the UI. The field is disabled in the UI when the cardholder enters a card number for a card type with no security code.

Target Origin
:
The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain), and port number (if used).

    You must use the https:// protocol. Sub domains must also be included in the target origin.

    Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.

    For example, if you are launching `Unified Checkout` on example.com, the target origin could be any of the following:

    * [https://example.com](https://example.com/ "")
    * [https://subdomain.example.com](https://subdomain.example.com/ "")
    * [https://example.com:8080](https://example.com:8080/ "")


    When you use `Unified Checkout` in an iframe, you must include the domain for the URL that loads the iframe and the iframe URL in the targetOrigins field.

Allowed Payment Types
:
You can specify the type of `Unified Checkout` digital payment methods that you want to accept in the capture context.
:
Use the allowedPaymentTypes field to define the payment type:

    * `AFTERPAY`
    * `APPLEPAY`
    * `BANCONTACT`
    * `CHECK`
    * `CLICKTOPAY`
    * `DRAGONPAY`
    * `GOOGLEPAY`
    * `IDEAL`




    * `KONBINI`
    * `MULTIBANCO`
    * `MYBANK`
    * `P24`
    * `PANENTRY`
    * `PAZE`
    * `TINKPAYBYBANK`


    > IMPORTANT
    > ` Click to Pay ` accepts American Express, Mastercard, and Visa for saved cards. Visa and Mastercard tokenize payment credentials using network tokenization for all ` Click to Pay ` requests. ` Click to Pay ` uses ` Click to Pay ` Token Requester IDs (TRIDs) rather than your existing TRIDs to generate network tokens.

    For more information on enabling and managing these digital payment methods, see these topics:

    * [Enrolling in Apple Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-applepay.md "")
    * [Enabling Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp.md "")
    * [Enrolling in Google Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-google.md "")
    * [Enrolling in Alternative Payment Methods](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-altpay.md "")

Capture Mandate
:
The capture mandate enables you to define which fields are captured within `Unified Checkout`. You must include the fields and set the values in the capture context based on the information that you want `Unified Checkout` to collect. This enables the cardholder to review and edit their details where the UI includes these fields. When the UI is used to capture cardholder information, all captured information is available within the payment details API response. When you want the cardholder to review existing address data, you can include the known customer data in the capture context and this information is pre-filled in the `Unified Checkout` UI. For information about the payment details API, see [Payment Details API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-token-get-pymnt-details.md "").

    | Capture Mandate Field |      Value       |                                                                                                                                                                                                                                                        Outcome                                                                                                                                                                                                                                                         |
    |-----------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | billingType           | `FULL`           | These fields are shown in the UI to capture cardholder billing details. When you include the billing details in the capture context, these details are pre-filled in the `Unified Checkout` UI. All information that is collected from these fields are tokenized in the transient token and sent for payment processing where the Complete Mandate is used.                                                                                                                                                           |
    | billingType           | `NONE`           | No fields are shown in the UI to capture cardholder billing details. If you are using the Complete Mandate, you must provide billing details in the capture context. All information that is collected from these fields is tokenized in the transient token and sent for payment processing. For information about which fields are required for payment processing, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md ""). |
    | billingType           | `PARTIAL`        | Only the billing postal code and billing country are collected in the UI. Set to this value when you use relaxed address verification services (AVS). This includes markets where postal code and billing country are enough for successful payment processing.                                                                                                                                                                                                                                                        |
    | requestEmail          | `true`           | The email address is shown and captured in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account.                                                                                                                                                                                                                                                                                                                                                        |
    | requestEmail          | `false`          | No email address is shown in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account and it appears in the UI when requestEmail is set to `false`.                                                                                                                                                                                                                                                                                                         |
    | requestPhone          | `true`           | The phone number is shown and captured in the UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | requestPhone          | `false`          | No phone number is shown or captured in the UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | requestShipping       | `true`           | Shipping fields are shown in the UI and are collected by `Unified Checkout`. When you include the shipping details in the capture context, the information appears prefilled in the UI.                                                                                                                                                                                                                                                                                                                                |
    | requestShipping       | `false`          | No shipping information is captured in the UI. When shipping details are required for payment processing and are used for follow on services such as `Decision Manager`, you can include these fields in the capture context. These details are tokenized and passed through.                                                                                                                                                                                                                                          |
    | shipToCountries       | ISO country code | When the requestShipping field is set to `true`, only the countries that are included in this field can be selected by the cardholder for their shipping address.                                                                                                                                                                                                                                                                                                                                                      |
    [Capture Mandate Field Values and Outcomes]

Complete Mandate
:
The complete mandate feature provides service orchestration within `Unified Checkout` and simplifies your integration. Service orchestration enables `Unified Checkout` to orchestrate services on your behalf. The complete mandate feature provides instructions to the unifiedPayment.complete() method in the JavaScript. You must include both the unifiedPayment.complete() object in the Javascript and the completeMandate field object in your capture context to enable `Unified Checkout` to initiate services on your behalf from the browser.

    > IMPORTANT
    > If you are updating an existing ` Unified Checkout ` configuration to use the complete mandate, you must update your JavaScript to include the unifedPayment.complete() function.

    > IMPORTANT
    > When the billingType field is set to ` NONE ` you must include the required fields within the capture context request to ensure that the required fields are included for payment processing. For information about the fields that are required for payment services, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").

    The complete mandate feature is defined by these fields:

    * completeMandate.type: This field is required to run the complete mandate and is used to indicate how a payment should be processed.
      Possible values:
      * `AUTH`: Authorize the payment and capture the funds at a later date.
      * `CAPTURE`: Perform a sale. A sale is a combined authorization and capture in a single request.
      * `PREFER_AUTH`: Perform an authorization if possible. If a payment method requires the funds to be captured immediately, then `Unified Checkout` captures the payment.
    * completeMandate.decisionManager: This field determines whether `Decision Manager` is run. Set this field to `true` and include completeMandate.type in your request to run `Decision Manager` and device fingerprinting services. When `Decision Manager` runs, it uses the associated `Decision Manager` configuration based on the merchant ID that is included in the request.
      When this field is set to `false` or is not included in the request, `Decision Manager` and device fingerprinting services do not run.
    * completeMandate.consumerAuthentication: This field determines whether `Payer Authentication` should be used. Set this field to `true` and include completeMandate.type in your request to run `Payer Authentication`. When this field set to `true`, `Payer Authentication` runs. When this field is set to `false` or is not included in the request, `Payer Authentication` does not run.
      When you use `Unified Checkout` with `Payer Authentication`, device data is collected through `Payer Authentication` setup and `Unified Checkout` completes all calls that are associated with `Payer Authentication`.
      `Unified Checkout` supports the pass-through fields that are required for `Payer Authentication` challenge codes. For information about the required fields, see [Unified Checkout Field Reference](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-pass-through-fields.md ""). For information about challenge codes, see consumerAuthenticationInformation.challengeCode in the [REST API Field Reference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md ""). Unified Checkout supports `3-D Secure` data only when your payment processor supports it. For information see [Visa Data Only](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-data-only-intro/pa2-use-data-only-visa-intro.md "") in the *`Payer Authentication` Developer Guide*.
      To test `Payer Authentication`, you must use `Payer Authentication` test cards. See [Test Cases for 3-D Secure 2.x](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "") in the *`Payer Authentication` Developer Guide*.
      Consumer authentication is available for these card types:
      * American Express
      * Cartes Bancaires
      * China UnionPay
      * Diners Club
      * Discover
      * EFTPOS
      * ELO
      * Jaywan
      * JCB
      * mada
      * Maestro
      * Mastercard
      * Visa
      * Jaywan
      Consumer authentication runs for these payment methods when they are supported in your `Unified Checkout` configuration:
      * `PANENTRY`
      * `CLICKTOPAY` when the transaction is not authenticated with `Click to Pay`.
      * `GOOGLEPAY` when the transaction is not authenticated with Google Pay.
      `Unified Checkout` does not attempt to authenticate for `Click to Pay` and Google Pay if the transaction has already been authenticated when it is received by `Unified Checkout`. For information about testing authentication, see [Test Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-authentication.md "").



    * completeMandate.tms.tokenCreate: This field determines if a `TMS` token is created for the customer's selected payment method. When this field is set to `true`, a token is created. When this field is set to `false` or not included in the request, a token is not created.
    * completeMandate.tms.tokenTypes: This is an optional field that you can use to indicate the token type for the token that is created. When this field is not included in the request, a token is created based on your `TMS` vault configuration. You can set this field to these values:
      * `customer`
      * `instrumentIdentifier`
      * `paymentInstrument`
      * `shippingAddress`

      If you want `Unified Checkout` to capture the cardholder's consent to save the card before a request to create a token is completed, then you must set captureMandate.requestSaveCard to `true`. When this field is set to `true`, `Unified Checkout` presents a **Save card for future payments** checkbox within the UI and enables the cardholder to give consent. Do not include captureMandate.requestSaveCard in your request if you have already gained cardholder consent to create a `TMS` token or do not require consent.
      This table indicates if a token is created given the requested payment method:

      |         Payment Method          |                                   Capture Context                                    |                                                                                                    Result                                                                                                    |
      |---------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
      | PAN Entry and `Click to Pay`    | completeMandate.tms.tokenCreate = `true`                                             | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
      | PAN Entry and `Click to Pay`    | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCard = `true` | Cardholder can check **Save Payment Information** in `Unified Checkout`. The request to create a token is made when the cardholder checks this field in the UI. When it is not checked, ni token is created. |
      | Apple Pay, Google Pay, and Paze | completeMandate.tms.tokenCreate = `true`                                             | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
      | Apple Pay, Google Pay, and Paze | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCard = `true` | `Unified Checkout` cannot obtain consent to create a token and no token is created when the customer completes the payment.                                                                                  |
      | Echeck                          | completeMandate.tms.tokenCreate = `true`                                             | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
      | Echeck                          | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCard = `true` | `Unified Checkout` cannot obtain consent to create a token and no token is created when the customer completes the payment.                                                                                  |
      [ ]

Include Card Prefix
:
You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

    * Six digits
    * Eight digits
    * No prefix

    To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.

:
To receive a six-digit card number prefix in the response, follow this step:

    Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.

    This example shows how a six-digit card number prefix `411111` is returned in the transient token response:

    ```
    "maskedValue" : "XXXXXXXXXXXX1111”,
                    "bin" : "411111"
    ```

:
To receive an eight-digit card number prefix in the response, follow this step:

    Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `true`. IMPORTANT
    > This PCI DSS requirement applies only to card numbers longer than 15 digits and only for Discover, JCB, Mastercard, UnionPay, and Visa brands.
    >
    > * If the card type entered is not part of these brands, a six-digit card number prefix is returned instead.
    > * If the card type entered is not part of these brands but is *co-branded* with these brands, an eight-digit card number prefix is returned.
    This example shows how an eight-digit card prefix `41111102` is returned in the transient token response:

    ```
    "maskedValue" : "XXXXXXXXXXXX1111”,
                    "prefix" : "41111102"
    ```

:
To not receive a card number prefix in the response, follow this step:

    Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `false`.

    This example shows how a card number is returned without a card number prefix in the transient token response:

    ```
    "maskedValue" : "XXXXXXXXXXXX1111"
    ```

:
**Best practice:** If your application does not require card number prefix information for routing or identification, `Cybersource` recommends that you include the transientTokenResponseOptions.includeCardPrefix field in the capture context request and set its value to `false`. Doing so limits the exposure of payment data to only what is necessary for your processing needs.
For more information about PCI DSS, see [Frequently Asked Questions](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers "") on the PCI Security Standards Council site.

> IMPORTANT
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Features {#uc-capture-context-features}
=======================================

`Unified Checkout` comprises these features.

Save Card
:
This feature enables you to display a consent option in the `Unified Checkout` UI for the cardholder to save their payment details for future use. If you use the complete mandate to create a token, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

    When you use this field without using the complete mandate, the transient token payload includes the consumerPreference.saveCard field with the value set to `true` when the cardholder has checked to save the payment information for future purchases:

    ```
    "captureMandate" : {
          "requestSaveCard": true
    }
    ```

Email Autolookup
:
When you include `Click to Pay` as an allowedPaymentType, an automatic email lookup occurs when an email address is included in the capture context request. If the user has a `Click to Pay` account but is not on a recognized device, a one-time password (OTP) screen appears and the user is prompted to enter their OTP. If the user does not have a `Click to Pay` account, the user must enter their card information manually. They will have the option to create a `Click to Pay` account.
To enable email autolookup, you must include `CLICKTOPAY` as a value in the allowedPaymentTypes field and include an email address in the capture context.

Removal of Confirm and Continue Screen
:
When showConfirmstionStep is set to `false`, you can remove the final summary confirmation screens from the checkout experience. When the UI displays cardholder data, the cardholder can review and, if necessary, edit their payment details before checkout is complete.

    ```
    {
      "captureMandate": {
        "showConfirmationStep": false
      }
    }
    ```

`Click to Pay` Enrollment Pre-Check
:
You can have the `Click to Pay` box pre-checked when a user is manually entering their card details and `Click to Pay` is enabled. The customer can uncheck the box if necessary, which means the request is processed as a one-time manual PAN transaction. This is available when you set the billingType field to `PARTIAL` or `FULL` in the capture context. This ensures that the customer's billing country can be validated in the UI.
:
`Click to Pay` enrollment pre-check is available in these countries:

    * Argentina
    * Brazil
    * Chile
    * Colombia
    * Kuwait
    * Mexico
    * Peru
    * Qatar
    * Saudi Arabia
    * South Africa
    * Ukraine
    * United Arab Emirates

    ```
    {
      "allowedPaymentTypes": [
        "PANENTRY",
        "GOOGLEPAY",
        {
          "type": "CLICKTOPAY",
          "options": {
            "autoCheckEnrollment": true
          }
        },
        "APPLEPAY",
        "PAZE"
      ]
    }
    ```

`Unified Checkout` Checkout Button Name
:
When `Unified Checkout` loads, the payment buttons displayed are based on what you include in the allowedPaymentTypes object in the capture context. `Unified Checkout` enables you to customize the text on the payment buttons. You can do this by setting the buttonType field object in the capture context to one of these values:

    * `ADD_CARD`
    * `CARD_PAYMENT`
    * `CHECKOUT_AND_CONTINUE`
    * `DEBIT_CREDIT`
    * `DONATE`
    * `PAY`
    * `PAY_WITH_CARD`
    * `SUBSCRIBE_WITH_CARD`

:
If you do not include the buttonType field in your request, the payment button text defaults to **Checkout with card**. For example:

    ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-checkout-card-300x100.svg/jcr:content/renditions/original)

Mobile as Identity for `Click to Pay`
:
`Click to Pay` supports mobile numbers as way to identify a user. This enables cardholders to use their mobile number instead of their email address in certain markets for Visa and Mastercard transactions.
:
When the requestEmail field is set to `false` and the requestPhone field is set to `true`, the cardholder is identified using the provided mobile number. When the requestEmail field is set to `true` and the requestPhone field is set to `false`, the cardholder is identified using the provided email address. When the requestEmail field is set to `true` and the requestPhone field is also set to `true`, the cardholder is identified using the provided email address first and then the mobile number if there is no match.

Features Available in Brazil
----------------------------

These features are available only in Brazil:

Combo Cards
:
A combo card is a single card in Brazil that functions as both a debit and a credit card. `Unified Checkout` enables the cardholder to choose whether to pay for a transaction using a debit or credit card. The cardholder can choose the card that they want to use when they enter their card details or when they choose a stored Visa card from their `Click to Pay` wallet during checkout. While in the card details section of the payment form, the cardholder is prompted for a debit or credit card. Credit is the default option.
To enable combo cards during checkout, you must include the comboCard field in your capture context request and set the field value to `true`. When the comboCard field value is set to `true`, the option to use a debit or credit card appears for all Visa cards that are entered in Unified Checkout and for all cards that are already stored in `Click to Pay`. If you do not want to offer a combo card at checkout, do not include the comboCard field in your capture context request:

    ```
    "captureMandate" : {
          "comboCard": true
    }
    ```

Cadastro de Pessoas Físicas (CPF) -- Brazilian Tax ID
:
The tax ID feature is for customers in Brazil and provides your customers with a way to include their Consumer National Identifier when it is requested at checkout. Include this field in the capture context to display this field within the flow for manual card entry and `Click to Pay` transactions:

    ```
    "captureMandate" : {
        "CPF": {
            "required": true
        }
    }
    ```

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

Requesting the Capture Context {#uc-setup-capture-context-intro}
================================================================

This section contains the information you need in order to request the capture context.

Endpoint {#uc-setup-capture-context-intro_d9e1017}
--------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d9e1024}
**Test:** `POST ``https://apitest.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d9e1034}
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d9e1043}
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d9e1052}

Required Fields for Requesting the Capture Context {#uc-setup-capture-context-req-fields}
=========================================================================================

Use these required fields to request the capture context:

[allowedPaymentTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/allowed-payment-types.md "")
:

[clientVersion](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-version.md "")
:

[country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/country.md "")
:

[locale](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/locale.md "")
:

[data.orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[data.orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[targetOrigins](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/target-origins.md "")
:
The URL in this field value must contain `https`.

[type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/type.md "")
:
Include this field when you use the complete mandate.

Related Information {#uc-setup-capture-context-req-fields_section_ybj_nzz_sxb}
------------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#uc-setup-capture-context-req-fields_ul_zbj_nzz_sxb}

REST Example: Requesting the Capture Context {#uc-setup-capture-context-example}
================================================================================

Request

```ph codeph
{
  "targetOrigins" : [ "https://test.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "CAPTURE",
        "decisionManager": true,
        "consumerAuthentication": true,
        "tms": {
            "tokenCreate": true,
            "tokenTypes": [
                "customer",
                "paymentInstrument",
                "instrumentIdentifier",
                "shippingAddress"
            ]
        }
    },
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

Encrypted JWT Response to a Successful Request

```
eyJraWQiOiJqNCIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImNvbXBsZXRlUGF0aCI6Ii9mbGV4L3YyL2NvbXBsZXRlIiwiZGF0YSI6ImY4TGhHRzFrMzdDMVI5UjM3YVhOQmhBQUVJWldjS1Yya29iUFA1OVlubHVWMUhBZzlDRWtiSlQ0bm1La2tWbEdCM3lhS1J4di83Uis3WWxvMlJsN2kvZXl4blJHMnRxNkhyNDZFREh2a3FlcUgvOWQyS3R2bmZBK25QeFRFZlJRd2F4L2l4ZXNvK3ZkckM4MitITUVmVDM0QTRIWkJHbjBwODFldUowaWVsc2RCdGpCOTJsNkZ1L2cvRkR3S2ZueTY2aDZUbnJ0NTZ1YThnb2p1YjUwRkVKaXpiMGI0S2NNVE4ydjVzWExXZlY5c21VXHUwMDNkICIsIm9yaWdpbiI6Imh0dHBzOi8vc3RhZ2VmbGV4LmN5YmVyc291cmNlLmNvbSIsImNvbXBsZXRlVXJsIjoiaHR0cHM6Ly9zdGFnZWZsZXguY3liZXJzb3VyY2UuY29tL2ZsZXgvdjIvY29tcGxldGUiLCJhdXRoZW50aWNhdGlvblNldHVwUGF0aCI6Ii9mbGV4L3YyL2V4dGVybmFsLXNlc3Npb25zL3NjYSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJ1cU5KWkRFZlNxR0o3UW8wTWxMU2lqZDJGaDdoaldaRDk5N0ZnaHZEbEtfZVdtOG5TS1BZSHJxX0ctN3VmeVJOQmM0aW8xb09NU3VqUE1VSWhsMWNzSXJ4bFJ4RDdDcC15RnlTSncwRHRoM01KNGpwZ1RQTXFLZkwyYi00UmQ1UXl0TFlZWUZVT21Takl3STJLQklERnpGRk5WLTRkcjlmS2ZnNXAzVTBzdmVZYXdtTllDcmQzWXpXaG1xaU9TRFZrTlhIaGQ3OWVBVndpdVJFWlN2T2NVZDR6dXd4RkFvX0N0MVV6aXFuLU9xdkw3UmZLLU9QaDg5N3FfWFFTUFNhYlUwZWltd24yZmpOVkYydnVoZXFDdmFDMmtIS2p0bFczMVMtSHE0MEJUanNsbmUyMUdCV3U0YWc4OHN5LTAxZnR5NzBjVnBXQnFpTVNfY3BYOVh6VlEiLCJraWQiOiIwMDdQS1ZOVk5IVEhzNlJVazNFRUM3YktiNUNKbzJwUSJ9fSwiY3R4IjpbeyJkYXRhIjp7ImFsbG93ZWRQYXltZW50VHlwZXMiOlsiUEFORU5UUlkiLCJDTElDS1RPUEFZIiwiQVBQTEVQQVkiLCJHT09HTEVQQVkiXSwicGF5bWVudENvbmZpZ3VyYXRpb25zIjp7IlNSQ1ZJU0EiOnsib3JpZ2luIjoiaHR0cHM6Ly9zYW5kYm94LWFzc2V0cy5zZWN1cmUuY2hlY2tvdXQudmlzYS5jb20iLCJwYXRoIjoiL2NoZWNrb3V0LXdpZGdldC9yZXNvdXJjZXMvanMvc3JjLWktYWRhcHRlci92aXNhU2RrLmpzP3YyIiwicGFuRW5jcnlwdGlvbktleSI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsImtpZCI6IlNEMVFCNktTRzZIT1BVTElFTVZQMTNFaG1KX1ZKcnhHb19ZR2tFVGVmcnRwanFGNU0iLCJuIjoic1pQSXVzRGY3eVFubmhCa1U5bXUxNFZPTzNDcnVpM2I3ckFmMktZZW9iVVJtWEExN2IxSlg5amcwQ2QtdmdwbXV5VHJ4QlVTYy00YjAtVVBnU3dHRnFQV1VweDA4RXhxcndQRE92Rm9qQm91MndseXE4YmN5MFVzLUJmZUN6U0U1bE1WZFNYVFhYWGNOcXUtcWIyMmpDQ0NKQUxweHNBcnNib01PWHNMZWRoM000WE5RNVhHQXRSZjdiLS11VFk1RHI5S0xZeVV2WktBblkwNE1LSlBFTzU0WWlJRk01RFRBaE5PbXMwODlqZE1keC1VUklLSmpQVTItUnBIRzF1OExDRzAyOFJUSXBQc05iUmFudVM1VEFZX3pseERnYjFoS0ozNlliWkVOSExnOVBYVEJoZE9NbFU5MERUTGxmY2JMVGEtRDdEZ2xqQWFXQ3V2ekxQYUd3In0sInBhcmFtZXRlcnMiOnsic3JjSW5pdGlhdG9ySWQiOiJSNDVOMzQzRDZLWFpSWU1CSVhMSTIxeDgtWGtMaWh4Q21lcFMzaEFlUm91RWcwaTVVIiwic3JjaURwYUlkIjoiOTBhZDlhN2QtOTU5Ni00ZWQxLWE3MTEtMmJjOTllM2JjNWZmIiwic3JjaVRyYW5zYWN0aW9uSWQiOiIxMzRjNTM0Yi1jMWJlLTQyNDgtYjk5NC1iMWZkODcwMmI3OWEiLCJkcGFUcmFuc2FjdGlvbk9wdGlvbnMiOnsiZHBhTG9jYWxlIjoiZW5fVVMiLCJwYXlsb2FkVHlwZUluZGljYXRvciI6IkZVTEwiLCJyZXZpZXdBY3Rpb24iOiJjb250aW51ZSIsImRwYUFjY2VwdGVkQmlsbGluZ0NvdW50cmllcyI6W10sImRwYUFjY2VwdGVkU2hpcHBpbmdDb3VudHJpZXMiOlsiVVMiLCJHQiJdLCJkcGFCaWxsaW5nUHJlZmVyZW5jZSI6IkFMTCIsImRwYVNoaXBwaW5nUHJlZmVyZW5jZSI6IkFMTCIsImNvbnN1bWVyTmFtZVJlcXVlc3RlZCI6dHJ1ZSwiY29uc3VtZXJFbWFpbEFkZHJlc3NSZXF1ZXN0ZWQiOnRydWUsImNvbnN1bWVyUGhvbmVOdW1iZXJSZXF1ZXN0ZWQiOnRydWUsIm1lcmNoYW50Q291bnRyeUNvZGUiOiJVUyIsImN1c3RvbUlucHV0RGF0YSI6eyJjaGVja291dE9yY2hlc3RyYXRvciI6Im1lcmNoYW50In0sInRyYW5zYWN0aW9uQW1vdW50Ijp7InRyYW5zYWN0aW9uQW1vdW50IjoiMTMuMDAiLCJ0cmFuc2FjdGlvbkN1cnJlbmN5Q29kZSI6IlVTRCJ9LCJwYXltZW50T3B0aW9ucyI6eyJkcGFEeW5hbWljRGF0YVR0bE1pbnV0ZXMiOjE1LCJkcGFQYW5SZXF1ZXN0ZWQiOmZhbHNlLCJkeW5hbWljRGF0YVR5cGUiOiJDQVJEX0FQUExJQ0FUSU9OX0NSWVBUT0dSQU1fTE9OR19GT1JNIn19fSwiY2hlY2tvdXRQYXJhbWV0ZXJzIjp7ImRwYVRyYW5zYWN0aW9uT3B0aW9ucyI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6IjEzLjAwIiwidHJhbnNhY3Rpb25DdXJyZW5jeUNvZGUiOiJVU0QifSwiYWNxdWlyZXJNZXJjaGFudElkIjoiMTIzNDU2NzgxMjMiLCJhY3F1aXJlckJJTiI6IjQ1NTU1NSIsIm1lcmNoYW50TmFtZSI6Ik5ld00iLCJhdXRoZW50aWNhdGlvblByZWZlcmVuY2VzIjp7ImF1dGhlbnRpY2F0aW9uTWV0aG9kcyI6W3siYXV0aGVudGljYXRpb25NZXRob2RUeXBlIjoiM0RTIiwiYXV0aGVudGljYXRpb25TdWJqZWN0IjoiQ0FSREhPTERFUiIsIm1ldGhvZEF0dHJpYnV0ZXMiOnsiY2hhbGxlbmdlSW5kaWNhdG9yIjoiMDEifX1dLCJwYXlsb2FkUmVxdWVzdGVkIjoiQVVUSEVOVElDQVRFRCJ9fX19LCJTUkNNQVNURVJDQVJEIjp7Im9yaWdpbiI6Imh0dHBzOi8vc2FuZGJveC5zcmMubWFzdGVyY2FyZC5jb20iLCJwYXRoIjoiL3Nkay9zcmNzZGsubWFzdGVyY2FyZC5qcyIsInBhbkVuY3J5cHRpb25LZXkiOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJraWQiOiIyMDIzMDIwNzIyMzUyMS1zYW5kYm94LWZwYW4tZW5jcnlwdGlvbi1zcmMtbWFzdGVyY2FyZC1pbnQiLCJrZXlfb3BzIjpbImVuY3J5cHQiLCJ3cmFwS2V5Il0sImFsZyI6IlJTQS1PQUVQLTI1NiIsIm4iOiJ0MDZJOHNqbFMtcnJzN3VDYWdIOGV2b2V1bWFSb3ZLemlaU0k5UzJOOUlEUTl0VzJQYXBmUmE5TGMxS3ZlRUJEVnMyN1BraGtVNU95SGdQMGlFalR1S1Zwdmg1OVQ0bGEtbUJTSWxzN1VlY1VRTExhMFdrbWJ0TDdqTmRsdEE1ZnE3QWhjQXI1cWNhOTg4cXJMZDdJeXI5RTBDM1R4YlQ5dG8xaVFjcHo4b2NaT0RSWG9pZEZBbk9WTDVZR0ZtbHNyZURiSjRWaHNpMHBBZGNjUWNpbC15ZFNndXJLQi1ycUtwcGI5ZXBvbXU0UVVoMzM4MkN2OE5vYlltRjNvczhuR0dnR1AtY3lYbzBuc0tjUEFnZnJsUXpvczdxSHhVT3JGZTJ4X2xaMUcxQUUtWHJrcnhqQnlzOXE1M0dNUlNOQ1E4Yy1fbWNGOXBicTRIWUJzLXZENVEifSwicGFyYW1ldGVycyI6eyJzcmNpVHJhbnNhY3Rpb25JZCI6IjEzNGM1MzRiLWMxYmUtNDI0OC1iOTk0LWIxZmQ4NzAyYjc5YSIsInNyY2lEcGFJZCI6Ijk4NDhjZmY0LWM4NjQtNGYxOC05ZjAzLWE4ZjUwYTY5MmVkZF9zeXN0ZW10ZXN0Iiwic3JjSW5pdGlhdG9ySWQiOiI2ZjVkNmMwOS1mOGUyLTQzMzAtYTNkZi0yMGI5YWQ3YTQ1MmIiLCJkcGFUcmFuc2FjdGlvbk9wdGlvbnMiOnsidHJhbnNhY3Rpb25UeXBlIjoiUFVSQ0hBU0UiLCJkcGFMb2NhbGUiOiJlbl9VUyIsImRwYUFjY2VwdGVkU2hpcHBpbmdDb3VudHJpZXMiOlsiVVMiLCJHQiJdLCJjb25zdW1lckVtYWlsQWRkcmVzc1JlcXVlc3RlZCI6dHJ1ZSwiY29uc3VtZXJQaG9uZU51bWJlclJlcXVlc3RlZCI6dHJ1ZSwidHJhbnNhY3Rpb25BbW91bnQiOnsidHJhbnNhY3Rpb25BbW91bnQiOiIxMy4wMCIsInRyYW5zYWN0aW9uQ3VycmVuY3lDb2RlIjoiVVNEIn0sImRwYUFjY2VwdGVkQmlsbGluZ0NvdW50cmllcyI6W10sImRwYUJpbGxpbmdQcmVmZXJlbmNlIjoiRlVMTCIsImRwYVNoaXBwaW5nUHJlZmVyZW5jZSI6IkZVTEwiLCJjb25zdW1lck5hbWVSZXF1ZXN0ZWQiOnRydWUsInBheWxvYWRUeXBlSW5kaWNhdG9yIjoiRlVMTCIsInBheW1lbnRPcHRpb25zIjp7ImR5bmFtaWNEYXRhVHlwZSI6IkNBUkRfQVBQTElDQVRJT05fQ1JZUFRPR1JBTV9TSE9SVF9GT1JNIn19fX0sIkFQUExFUEFZIjp7InNlc3Npb25QYXRoIjoiL2ZsZXgvdjIvYXBwbGUvcGF5bWVudC1zZXNzaW9ucyIsIm1lcmNoYW50SWRlbnRpZmllciI6Im1lcmNoYW50LmNvbS5jeWJlcnNvdXJjZS5zdGFnZWZsZXgiLCJkaXNwbGF5TmFtZSI6Ik5pYW1oIGRpc3BsYXkgbmFtZSB0ZXN0In0sIkdPT0dMRVBBWSI6eyJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9wYXkuZ29vZ2xlLmNvbS9ncC9wL2pzL3BheS5qcyIsInBheW1lbnRPcHRpb25zIjp7ImVudmlyb25tZW50IjoiVEVTVCJ9LCJwYXltZW50RGF0YVJlcXVlc3QiOnsiYXBpVmVyc2lvbiI6MiwiYXBpVmVyc2lvbk1pbm9yIjowLCJtZXJjaGFudEluZm8iOnsibWVyY2hhbnRJZCI6IkJDUjJETjRUN0REWUJUVFYiLCJtZXJjaGFudE5hbWUiOiJVbmlmaWVkIENoZWNrb3V0IE1lcmNoYW50In0sImFsbG93ZWRQYXltZW50TWV0aG9kcyI6W3sidHlwZSI6IkNBUkQiLCJwYXJhbWV0ZXJzIjp7ImFzc3VyYW5jZURldGFpbHNSZXF1aXJlZCI6dHJ1ZSwiYWxsb3dlZEF1dGhNZXRob2RzIjpbIlBBTl9PTkxZIiwiQ1JZUFRPR1JBTV8zRFMiXSwiYWxsb3dlZENhcmROZXR3b3JrcyI6WyJWSVNBIiwiTUFTVEVSQ0FSRCJdLCJiaWxsaW5nQWRkcmVzc1JlcXVpcmVkIjp0cnVlLCJiaWxsaW5nQWRkcmVzc1BhcmFtZXRlcnMiOnsiZm9ybWF0IjoiRlVMTCIsInBob25lTnVtYmVyUmVxdWlyZWQiOnRydWV9fSwidG9rZW5pemF0aW9uU3BlY2lmaWNhdGlvbiI6eyJ0eXBlIjoiUEFZTUVOVF9HQVRFV0FZIiwicGFyYW1ldGVycyI6eyJnYXRld2F5IjoiY3liZXJzb3VyY2UiLCJnYXRld2F5TWVyY2hhbnRJZCI6InBzX2hwYSJ9fX1dLCJ0cmFuc2FjdGlvbkluZm8iOnsidG90YWxQcmljZVN0YXR1cyI6IkZJTkFMIiwidG90YWxQcmljZSI6IjEzLjAwIiwiY291bnRyeUNvZGUiOiJVUyIsImN1cnJlbmN5Q29kZSI6IlVTRCJ9LCJlbWFpbFJlcXVpcmVkIjp0cnVlLCJzaGlwcGluZ0FkZHJlc3NSZXF1aXJlZCI6dHJ1ZSwic2hpcHBpbmdBZGRyZXNzUGFyYW1ldGVycyI6eyJhbGxvd2VkQ291bnRyeUNvZGVzIjpbIlVTIiwiR0IiXSwicGhvbmVOdW1iZXJSZXF1aXJlZCI6dHJ1ZX19fX0sImNhcHR1cmVNYW5kYXRlIjp7InNob3dDb25maXJtYXRpb25TdGVwIjp0cnVlLCJiaWxsaW5nVHlwZSI6IkZVTEwiLCJyZXF1ZXN0RW1haWwiOnRydWUsInJlcXVlc3RQaG9uZSI6dHJ1ZSwicmVxdWVzdFNoaXBwaW5nIjp0cnVlLCJzaGlwVG9Db3VudHJpZXMiOlsiVVMiLCJHQiJdLCJzaG93QWNjZXB0ZWROZXR3b3JrSWNvbnMiOnRydWUsImRldmljZUZpbmdlcnByaW50aW5nIjp7IlRNIjp7InVybCI6Imh0dHBzOi8vdG0uY3liZXJzb3VyY2UuY29tL2ZwL3RhZ3MuanM_b3JnX2lkXHUwMDNkcnB6ZHJ2aXhcdTAwMjZzZXNzaW9uX2lkXHUwMDNkcHNfaHBhYmIxMjhjYmMtOTk0Ni00Mjc1LThmMmMtMWFhNWE5YjQ1NjNjIiwic2Vzc2lvbklkIjoiYmIxMjhjYmMtOTk0Ni00Mjc1LThmMmMtMWFhNWE5YjQ1NjNjIn19fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJhbW91bnREZXRhaWxzIjp7InRvdGFsQW1vdW50IjoiMTMuMDAiLCJjdXJyZW5jeSI6IlVTRCJ9LCJiaWxsVG8iOnsiYWRkcmVzczEiOiI5MDEgTWV0cm8gQ2VudGVyIEJsdmQiLCJhZGRyZXNzMiI6IkRlc2sgTTMtNTU3MyIsImFkbWluaXN0cmF0aXZlQXJlYSI6IkNBIiwiYnVpbGRpbmdOdW1iZXIiOiIxNTAiLCJjb3VudHJ5IjoiVVMiLCJsb2NhbGl0eSI6IkZvc3RlciBDaXR5IiwicG9zdGFsQ29kZSI6Ijk0NDA0IiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiZmlyc3ROYW1lIjoiTkVXIiwibGFzdE5hbWUiOiJUZXN0IiwicGhvbmVOdW1iZXIiOiIxMjM0NTY3ODkwIn0sInNoaXBUbyI6eyJhZGRyZXNzMSI6IjkwMSBNZXRybyBDZW50ZXIgQmx2ZCIsImFkZHJlc3MyIjoiRGVzayBNMy01NTczIiwiYWRtaW5pc3RyYXRpdmVBcmVhIjoiQ0EiLCJidWlsZGluZ051bWJlciI6IjE1MCIsImNvdW50cnkiOiJVUyIsImxvY2FsaXR5IjoiRm9zdGVyIENpdHkiLCJwb3N0YWxDb2RlIjoiOTQ0MDQiLCJmaXJzdE5hbWUiOiJORVciLCJsYXN0TmFtZSI6IlRlc3QifX0sInRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly90aGUtdXAtZGVtby5hcHBzcG90LmNvbSJdLCJpZnJhbWVzIjp7Im1jZSI6Ii9tY2UvbWNlLmh0bWwiLCJidXR0b25zIjoiL2J1dHRvbmxpc3QvYnV0dG9ubGlzdC5odG1sIiwic3JjIjoiL3NlY3VyZS1yZW1vdGUtY29tbWVyY2Uvc3JjLmh0bWwiLCJjdHAiOiIvY3RwL2N0cC5odG1sIiwiZ29vZ2xlcGF5IjoiL2dvb2dsZXBheS9nb29nbGVwYXkuaHRtbCIsImFwcGxlcGF5IjoiL2FwcGxlcGF5L2FwcGxlcGF5Lmh0bWwiLCJwYXplIjoiL3BhemUvcGF6ZS5odG1sIiwiY2hlY2siOiIvY2hlY2svY2hlY2suaHRtbCIsImdhIjoiL2dhL2dhLmh0bWwiLCJvcmMiOiIvb3JjL29yYy5odG1sIiwidG0iOiIvdG0vdG0uaHRtbCIsImFwbSI6Ii9hcG0vYXBtLmh0bWwiLCJhcG0tc3RlcHBlciI6Ii9hcG0tc3RlcHBlci9hcG0tc3RlcHBlci5odG1sIn0sImNsaWVudFZlcnNpb24iOiIwLjMxIiwiY291bnRyeSI6IlVTIiwibG9jYWxlIjoiZW5fVVMiLCJhbGxvd2VkQ2FyZE5ldHdvcmtzIjpbIlZJU0EiLCJNQVNURVJDQVJEIl0sImJ1dHRvblR5cGUiOiJDQVJEX1BBWU1FTlQiLCJjbGllbnRSZWZlcmVuY2VJbmZvcm1hdGlvbiI6eyJjb2RlIjoiVEFHWDAwMSJ9LCJjb21wbGV0ZU1hbmRhdGUiOnsidHlwZSI6IkNBUFRVUkUiLCJ0cmFuc2FjdGlvbklkIjoic0lzNHo2cHlFeUNXT0szZUNRd1BrdGlkYVpQWSIsImNvbnN1bWVyQXV0aGVudGljYXRpb24iOnsiYWxsb3dlZENhcmROZXR3b3JrcyI6WyJWSVNBIiwiTUFTVEVSQ0FSRCJdLCJhbGxvd2VkUGF5bWVudFR5cGVzIjpbIlBBTkVOVFJZIiwiR09PR0xFUEFZIiwiQ0xJQ0tUT1BBWSJdfSwidG1zIjp7InRva2VuVHlwZXMiOlsiY3VzdG9tZXIiLCJwYXltZW50SW5zdHJ1bWVudCIsImluc3RydW1lbnRJZGVudGlmaWVyIiwic2hpcHBpbmdBZGRyZXNzIl0sImFsbG93ZWRQYXltZW50VHlwZXMiOlsiUEFORU5UUlkiLCJHT09HTEVQQVkiLCJDTElDS1RPUEFZIiwiQVBQTEVQQVkiXX19LCJhbmFseXRpY3MiOnsiZ29vZ2xlIjp7InNjcmlwdCI6Imh0dHBzOi8vd3d3Lmdvb2dsZXRhZ21hbmFnZXIuY29tL2d0YWcvanMiLCJpZCI6IkctU1FCMzRERVFHSiJ9fSwiY3IiOiJ1ZVdNd0Z1TjBVeU14MTNlUWhfZ3FVbHA2NFM2Wjk2MWN2WElaeVdZUHZLUEZaUnZVWWtpVGs3bmdoSXBUc1dMY3pqSy05cjM2emhkVXRTYkVWcFBLZno0WDVWS3JyZ3FxM0dJQ01adGg3NXZmT2MzSlFTMnlSVjAzUkJGN3VmdkdnOFh5Nm10blo3TExpYVczUjZjZGw3OTR4cVVtNUtfWnktVGFqdGVUNVlLWEdMWkx1THNOYTQiLCJzZXJ2aWNlT3JpZ2luIjoiaHR0cHM6Ly9nZGEtYmFja2VuZC11cC1kZW1vLmluZ3Jlc3MuY2VsdGljLnZpc2EuY29tOjg0NDMiLCJjbGllbnRMaWJyYXJ5IjoiaHR0cHM6Ly9nZGEtYmFja2VuZC11cC1kZW1vLmluZ3Jlc3MuY2VsdGljLnZpc2EuY29tOjg0NDMvdWMvdjEvYXNzZXRzL2FYMnVseG4yandNbjRoakJ4T2hLYVdoX2lSTVdfY0YwM3pRNUw5WGFVOWg1MF80TmxBb3RKeG1PUWM5WmpYcHlIOTlBWFN4NHl4YXNuMW1PcXR5RWQwTEsxUnIxRDUwRXc3QWRSeFY2QlJDVm9BSnFyVHhLWmFTNjVZNlZ3VkxFWk1UT3ZveTRHMUJaU05RL1NlY3VyZUFjY2VwdGFuY2UuanMiLCJsb2dnaW5nUGF0aCI6Ii91Yy92MS9sb2ctZXZlbnRzIiwiYXNzZXRzUGF0aCI6Ii91Yy92MS9hc3NldHMvYVgydWx4bjJqd01uNGhqQnhPaEthV2hfaVJNV19jRjAzelE1TDlYYVU5aDUwXzRObEFvdEp4bU9RYzlaalhweUg5OUFYU3g0eXhhc24xbU9xdHlFZDBMSzFScjFENTBFdzdBZFJ4VjZCUkNWb0FKcXJUeEtaYVM2NVk2VndWTEVaTVRPdm95NEcxQlpTTlEiLCJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LWRYQ3BRRUlDd1hnT09QR013NE4xSjcyd0hlZ2l4Z2RZL1Y2azR2TG9nenNcdTAwM2QifSwidHlwZSI6ImdkYS0wLjEwLjAifV0sImlzcyI6IkZsZXggQVBJIiwiZXhwIjoxNzYyODk0MzcxLCJpYXQiOjE3NjI4OTM0NzEsImp0aSI6IldkWWR4aDBLVUNtblhDeEIifQ.cWIEtuT_CD4iiqMgFcTLCyV3zbyVxeCflFj2E0Fh3J8sTE4tZDaOBt9IWG-x3LWZ8pQb0g6JEZ-4FRoLpstU9BWJfiPVZQUrdXWLR8pnMLK38AUJI_WP85NYEeSsuaAZkh9elfr47agIB2dx1E3kWjk2IEkJt32WCVsctOrImNSibpkcA3LgfOTjGHVmJ7NqVsbVyxEi3Zg_0D2SACNpKHj0z76yL6Y5JeMe807-43vHithNn_skoVbaRzz3He17Ej497N8-g6EUBSmq8sQAQaI0QbBMCm0EXTH-aI0q2m193XoV2SR8KCn20g4e9ONmspHtEXypaCIqRU8ka2lT4A
```

Decrypted Capture Context Header

```
{
  "kid": "j4",
  "alg": "RS256"
}
```

Decrypted Capture Context Body with Selected Fields

```keyword
{
  "flx" : {
    // filled with token metadata
  },
  "ctx" : [ {
    // filled with data related to your capture context request parameters
    "data" : {
      "clientLibrary" : "https://apitest.cybersource.com/up/v1/assets/0.34.0/SecureAcceptance.js"
    },
    "type" : "gda-0.9.0"
  } ],
  "iss" : "Flex API",
  "exp" : "1762894371",
  "iat" : "1762893471",
  "jti" : "WdYdxh0KUCmnXCxB"
}
```

Validating the Capture Context {#uc-validate-capture-context-intro}
===================================================================

The capture context that you generate is a JSON Web Token (JWT) data object. The JWT is digitally signed using a public key and confirms the validity of the JWT and that it comes from `Cybersource`. When you do not have a key in the JWT header, `Cybersource` recommends that you follow cryptography best practices and validate the capture context signature.
To validate a JWT, you must obtain its public key. This public RSA key is in JSON Web Key (JWK) format. The public key is associated with the capture context on the `Cybersource` domain.
To get the public key of a capture context from the header of the capture context itself, you must retrieve the key ID associated with the public key and then pass the key ID to the `/flex/v2/public-keys` endpoint:

1. From the header of the capture context, get the key ID (kid):

   ```
   {
       "kid": "3g",
       "alg": "RS256"
   }
   ```
2. Send a GET request to the `/flex/v2/public-keys` endpoint and include the key ID. For example:

   * **Test:** `GET ``https://apitest.cybersource.com``/flex/v2/public-keys/{3g}`
   * **Production:** `GET ``https://api.cybersource.com``/flex/v2/public-keys/{3g}`
     Depending on the cryptographic method you use to validate the public key, you might need to convert the key to privacy-enhanced mail (PEM) format.
3. The resource returns the public key:

   ```
   eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiI2bUFLNTNPNVpGTUk5Y3RobWZmd2doQUFFRGNqNU5QYzcxelErbm8reDN6WStLOTVWQ2c5bThmQWs4czlTRXBtT21zMmVhbEx5NkhHZ29oQ0JEWjVlN3ZUSGQ5YTR5a2tNRDlNVHhqK3ZoWXVDUmRDaDhVY1dwVUNZWlZnbTE1UXVFMkEiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJyQmZwdDRjeGlkcVZwT0pmVTlJQXcwU1JCNUZqN0xMZjA4U0R0VmNyUjlaajA2bEYwTVc1aUpZb3F6R3ROdnBIMnFZbFN6LVRsSDdybVNTUEZIeTFJQ3BfZ0I3eURjQnJ0RWNEanpLeVNZSTVCVjNsNHh6Qk5CNzRJdnB2Smtqcnd3QVZvVU4wM1RaT3FVc0pfSy1jT0xpYzVXV0ZhQTEyOUthWFZrZFd3N3c3LVBLdnMwNmpjeGwyV05STUIzTS1ZQ0xOb3FCdkdCSk5oYy1uM1lBNU5hazB2NDdiYUswYWdHQXRfWEZ0ZGItZkphVUVUTW5WdW9fQmRhVm90d1NqUFNaOHFMOGkzWUdmemp2MURDTUM2WURZRzlmX0tqNzJjTi1OaG9BRURWUlZyTUtiZ3QyRDlwWkJ1d2gzZlNfS3VRclFWTVdPelRnT3AzT2s3UVFGZ1EiLCJraWQiOiIwOEJhWXMxbjdKTUhjSDh1bkcxc1NDUVdxN2VveWQ1ZyJ9fSwiY3R4IjpbeyJkYXRhIjp7InRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly93d3cudGVzdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSJ9LCJ0eXBlIjoibWYtMC4xMS4wIn1dLCJpc3MiOiJGbGV4IEFQSSIsImV4cCI6MTYxNjc3OTA5MSwiaWF0IjoxNjE2Nzc4MTkxLCJqdGkiOiJ6SG1tZ25uaTVoN3ptdGY0In0.GvBzyw6JKl3b2PztHb9rZXawx2T817nYqu6goxpe4PsjqBY1qeTo19R-CP_DkJXov9hdJZgdlzlNmRY6yoiziSZnGJdpnZ-pCqIlC06qrpJVEDob3O_efR9L03Gz7F5JlLOiTXSj6nVwC5mRlcP032ytPDEx5TMI9Y0hmBadJYnhEMwQnn_paMm3wLh2v6rfTkaBqd8n6rPvCNrWMOwoMdoTeFxku-
   ```

   Use this public RSA key to validate the capture context.

4. Parse the JWT capture context to get the kid from its header:

   ```
   {
       "kid": "3g",
       "alg": "RS256"
   }
   ```
5. Send a GET request to retrieve the public key from `/flex/v2/public-keys/3g`:

   ```
   {
       "kty":"RSA",
       "use":"enc",
       "kid":"3g",
       "n":"ir7Nl1Bj8G9rxr3co5v_JLkP3o9UxXZRX1LIZFZeckguEf7Gdt5kGFFfTsymKBesm3Pe
        8o1hwfkq7KmJZEZSuDbiJSZvFBZycK2pEeBjycahw9CqOweM7aKG2F_bhwVHrY4YdKsp
        _cSJe_ZMXFUqYmjk7D0p7clX6CmR1QgMl41Ajb7NHI23uOWL7PyfJQwP1X8HdunE6ZwK
        DNcavqxOW5VuW6nfsGvtygKQxjeHrI-gpyMXF0e_PeVpUIG0KVjmb5-em_Vd2SbyPNme
        nADGJGCmECYMgL5hEvnTuyAybwgVwuM9amyfFqIbRcrAIzclT4jQBeZFwkzZfQF7MgA6QQ",
        "e":"AQAB"
   }
   ```

Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the payment details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d9e1088}
----------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/up/v1/payment-details/`*{id}*{#uc-token-get-pymnt-details_d9e1095}
**Test:** `GET ``https://apitest.cybersource.com``/up/v1/payment-details/`*{id}*{#uc-token-get-pymnt-details_d9e1107}
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/up/v1/payment-details/`*{id}*
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/up/v1/payment-details/`*{id}*
The `{id}` is the full JWT received from `Unified Checkout` as the result of capturing payment information. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

REST Example: Retrieving Transient Token Payment Details {#uc-token-get-pymnt-details-ex-rest}
==============================================================================================

Request

```keyword
GET https://apitest.cybersource.com/up/v1/payment-details/{id}
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

JavaScript API Reference {#uc-appendix-js-reference_api_reference}
==================================================================

This reference provides details about the JavaScript API for creating the `Unified Checkout` payment form.

Class: Accept {#uc-appendix-js-class-accept}
============================================

Accept
------

**Returns**
Type: Promise.\&lt;Accept\&gt;
**Example**
*Basic Setup*

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt;&lt;/script&gt;
//Note: Script location and integrity value should be sourced from the capture context response clientLibrary and clientLibraryIntegrity values.
&lt;script&gt; Accept('header.payload.signature').then(function(accept) {
// use accept object
});
&lt;/script&gt;
```

Methods
-------

**dispose()**` → {void}`
Dispose of this Accept instance.
**Returns**
Type: void
**unifiedPayments(sidebar)**` → `**{Promise.&lt;UnifiedPayments&gt;}**
Create a Unified Payments integration.

| Name    | Type    | Attributes         | Description                                                                                                                                                                                                                                                                                      |
|:--------|:--------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sidebar | Boolean | \&lt;optional\&gt; | Set the option to `false` to enable embedded functionality of Unified Checkout. This will configure Unified Checkout to place the Payment Entry form inline. If this value is not set, the default is `true` and Unified Checkout will open the Payment Entry form in the sidebar configuration. |
[Parameters]

**Throws:** AcceptError
**Returns:**
Type: Promise.\&lt;UnifiedPayments\&gt;
**Examples**
*Minimal Setup - sidebar*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
```

*Embedded Payment Entry*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments(false))
```

*Error Handling*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
    .then(up =&gt; up.show(showArgs))
    .then(tt =&gt; {
        document.getElementById('transientToken').value = tt;
        document.getElementById("authForm").submit();
    })
    .catch(error =&gt; {
                console.error(error);
                document.getElementById('logo').text = `Checkout error: ${JSON.stringify(error)}. Try again.`;
            });
```

Class: AcceptError {#uc-appendix-js-class-accept-error}
=======================================================

AcceptError
-----------

This class defines how errors are returned by the Unified Checkout JavaScript.

Members
-------

`(static, readonly) Reason Codes - Accept object creation`
Possible errors that can occur during the creation of an Accept object.

| Name                    | Type   | Description                                                                  |
|:------------------------|:-------|:-----------------------------------------------------------------------------|
| CAPTURE_CONTEXT_INVALID | string | Occurs when you pass an invalid JWT.                                         |
| CAPTURE_CONTEXT_EXPIRED | string | Occurs when the JWT you pass has expired.                                    |
| SDK_XHR_ERROR           | string | Occurs when a network error is encountered while attempting to load the SDK. |
[Properties:]

`(static, readonly) Reason Codes - Show Errors`
Possible errors that can occur during the rendering of payment selection list.

| Name                                 | Type   | Description                                                                         |
|:-------------------------------------|:-------|:------------------------------------------------------------------------------------|
| CHECKOUT_ERROR                       | string | Occurs when checkout failed to load.                                                |
| CLICK_TO_PAY_SDK_LOAD_ERROR          | string | Occurs when the `Click to Pay` SDK fails to load.                                   |
| ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR | string | Occurs when the card encryption for SRC enrollment fails to load.                   |
| LAUNCH_SRC_CHECKOUT_ERROR            | string | Occurs when the SRC checkout fails to load.                                         |
| SHOW_LOAD_CONTAINER_SELECTOR         | string | Occurs when a DOM element cannot be located using the supplied CSS Selector string. |
| SHOW_LOAD_ERROR                      | string | Occurs when there is an issue loading the payment iframe.                           |
| SHOW_LOAD_INVALID_CONTAINER          | string | Occurs when an invalid container parameter is supplied.                             |
| SHOW_LOAD_SIDEBAR_OPTIONS            | string | Occurs when an invalid container parameter is supplied when sidebar is selected.    |
| SHOW_PAYMENT_TIMEOUT                 | string | Occurs when an error is encountered during the handling of a payment option.        |
| SHOW_PAYMENT_UNAVAILABLE             | string | Occurs when no payment types can be presented to the customer.                      |
| SHOW_TOKEN_TIMEOUT                   | string | Occurs when the createToken call is unable to proceed.                              |
| SHOW_TOKEN_XHR_ERROR                 | string | Occurs when a network error is encountered while attempting to create a token.      |
| UNIFIED_PAYMENTS_ALREADY_SHOWN       | string | Occurs when you attempt to show a Unified Payments instance multiple times.         |
| UNKNOWN_ERROR                        | string | Occurs when an unknown error has occurred.                                          |
[Properties:]

`(static, readonly) Reason Codes - Unified Payments Errors`
Possible errors that can occur during the creation of a Unified Payments object.

| Name                                | Type   | Description                                                                               |
|:------------------------------------|:-------|:------------------------------------------------------------------------------------------|
| CREATE_TOKEN_TIMEOUT                | string | Occurs when the createToken call times out.                                               |
| CREATE_TOKEN_XHR_ERROR              | string | Occurs when a network error is encountered while attempting to create a token.            |
| UNIFIED_PAYMENTS_PAYMENT_PARAMETERS | string | Occurs when no valid payment parameters exist while initializing button.                  |
| UNIFIED_PAYMENTS_VALIDATION_PARAMS  | string | Occurs when there's an issue with the parameters supplied to UnifiedPayments constructor. |
[Properties:]

`(nullable) correlationId :string`
The correlationId of any underlying API call that resulted in this error.
**Type:** string
`(nullable) details :array`
Additional error-specific information.
**Type:** array
`(nullable) informationLink :string`
A URL link to online documentation for this error.
**Type:** string
`message :string`
A human-readable explanation of the error that has occurred.
**Type:** string
`reason :string`
A reason corresponding to the specific error that has occurred.
**Type:** string
`(static, readonly) Reason Codes -- Complete API Response Errors`
Possible errors that can occur when calling the complete API.

| Name                             | Type   | Description                                                                                                 |
|:---------------------------------|:-------|:------------------------------------------------------------------------------------------------------------|
| COMPLETE_AUTHENTICATION_CANCELED | string | Occurs when the user cancels the authentication process during Cardinal step-up.                            |
| COMPLETE_AUTHENTICATION_FAILED   | string | Occurs when the complete authentication process fails during Cardinal step-up.                              |
| COMPLETE_ERROR                   | string | Occurs when an error occurs while attempting to process a payment using the complete API.                   |
| COMPLETE_IN_PROGRESS             | string | Occurs when complete has already been invoked but has not yet finished processing.                          |
| COMPLETE_NOT_ALLOWED             | string | Occurs if complete is not allowed for this transaction.                                                     |
| COMPLETE_TRANSACTION_CANCELLED   | string | Occurs when consumer cancelled the transaction.                                                             |
| COMPLETE_TRANSACTION_FAILED      | string | Occurs when consumer transaction fails.                                                                     |
| COMPLETE_VALIDATION_ERROR        | string | Occurs when there is a validation issue relating to the parameters you have supplied in your complete call. |
[Properties:]

Class: UnifiedPayments {#uc-appendix-js-class-unified-payments}
===============================================================

UnifiedPayments
---------------

An instance of this class is returned upon the creation of a Unified Payments integration using accept.unifiedPayments(). Using this object you can add the payment options list to your checkout.

Methods {#uc-appendix-js-class-unified-payments_section_n1t_k5v_ncc}
--------------------------------------------------------------------

`hide() → {Promise}`
Hide button list.
**Returns:** Type Promise
**Example**
Basic Usage

```
up.hide()
  .then(() =&gt; console.log('Hidden'))
  .catch(err =&gt; console.error(err));
```

`show(optionsopt) → {Promise.&lt;UnifiedPayments~TransientToken}`
Show button list.

| Name             | Type   | Attributes         | Description                                                                                                                  |
|:-----------------|:-------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| options          | object | \&lt;optional\&gt; |                                                                                                                              |
| containers       | object | \&lt;optional\&gt; | CSS selectors to locate containers in which to place various UI elements. If not specified, these will operate in a sidebar. |
| paymentSelection | string | \&lt;optional\&gt; | For showing payment buttons.                                                                                                 |
| paymentScreen    | string | \&lt;optional\&gt; | For the main payment flows.                                                                                                  |
[Parameters]

**Returns:** Type Promise
**Examples**
Basic Usage With Full Sidebar Experience

```
const showArgs = {
            containers: {
                paymentSelection: #buttonPaymentListContainer'
            }
        };

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

All Screens Embedded in Containers

```
const showArgs = {
  containers: {
    paymentSelection: '#buttonPaymentListContainer',
    paymentScreen:  '#embeddedPaymentContainer'
  }
};

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

Type Definitions
----------------

**TransientToken**
The response to a successful customer interaction with Unified Checkout is a transient token. The transient token is a reference to the payment data collected on your behalf. Tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that lasts 15 minutes. This reduces your PCI burden and responsibility and ensures that sensitive information is not exposed to your backend systems.
It is in a JSON Web Token format. The payload of the transient token may contain useful metadata in relation to the stored sensitive info. However , all of this info is safe to use and store on your systems.
The transient token can be used to complete a payment or other services, after which the transient data will be evicted from the token store.
**Type:** string
**Examples**
How to Split the Transient Token

```
const transientToken = 'hhhhhhhhhh.pppppppppp.sssssssssss';

const segments = transientToken.split('.');
const urlBase64Decode = (s) =&gt; atob(s.replace(/_/g, '/').replace(/-/g, '+'));

const header = JSON.parse(urlBase64Decode(segments[0]));
const payload = JSON.parse(urlBase64Decode(segments[1]));
const signature = segments[2];
```

Decoded Body

```
{
  "iss" : "Flex/00",
  "exp" : 1706910242,
  "type" : "gda-0.9.0",
  "iat" : 1706909347,
  "jti" : "1D1I2O2CSTMW3UIXOKEQFI4OQX1L7CMSKDE3LJ8B5DVZ6WBJGKLQ65BD6222D426",
  "content" : {
    "orderInformation" : {
      "billTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "amountDetails" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "shipTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      }
    },
    "paymentInformation" : {
      "card" : {
        "expirationYear" : {
          "value" : "2028"
        },
        "number" : {
          "maskedValue" : "XXXXXXXXXXXX1111",
          "bin" : "411111"
        },
        "securityCode" : { },
        "expirationMonth" : {
          "value" : "06"
        },
        "type" : {
          "value" : "001"
        }
      }
    }
  }
}
```

`Unified Checkout` Configuration {#uc-configuration-intro}
==========================================================

This section contains information necessary to configure `Unified Checkout` in the `Business Center`:

* [Enable Digital Payments](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro.md "")
* [Manage Permissions](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-manage-permissions-intro.md "")

Webhooks Support {#uc-appendix-webhooks}
========================================

`Unified Checkout` supports webhooks. You can use webhooks to obtain the complete response from the completeMandate call. To receive a webhook notification, you must first subscribe to the webhook. For information on setting up a webhook, see the [How to Set Up Webhook Subscriptions](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-workflow-options.md "") section of the *Webhooks Developer Guide*. IMPORTANT
Webhook payloads are encrypted. In order to receive a ` Unified Checkout ` webhook notification, you must enabled message-level encryption (MLE). For information about enabling MLE, see [Enable Message-Level Encryption](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "") in the *Getting Started with REST Developer Guide*.

|    Product ID     |          Event Types           |                                  Description                                   |
|-------------------|--------------------------------|--------------------------------------------------------------------------------|
| `unifiedCheckout` | `uc.orders.transactionresults` | Full payload response from the payment service call made by `Unified Checkout` |
[`Unified Checkout` Webhook Events]

**Example: Webhooks Request for `Unified Checkout` Events**

```
{
    "organizationId": "ps_hpa",
    "webhookId": "2d55e648-d96c-d727-e063-3cb8d30a938e",
    "productId": "unifiedCheckout",
    "requestType": "NEW",
    "payload": {
        "details": {
            "_links": {
                "authReversal": {
                    "method": "POST",
                    "href": "/pts/v2/payments/7435188899356405003091/reversals"
                },
                "self": {
                    "method": "GET",
                    "href": "/pts/v2/payments/7435188899356405003091"
                },
                "capture": {
                    "method": "POST",
                    "href": "/pts/v2/payments/7435188899356405003091/captures"
                }
            },
            "clientReferenceInformation": {
                "code": "1743518889914",
                "transactionId": "123456789ABCDEFGHIJKLMNOPQRST1"
            },
            "consumerAuthenticationInformation": {
                "token": "Axj/7wSTkw/5TqVCHfNTABEg1auGjlgybQ3FmNXmxaSiXV63TywFRLq9bp5ekDpxBPjhk23GVpz0tI7gTk5MP+U6lQh3zUwA0TVW"
            },
            "id": "7435188899356405003091",
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
                "scheme": "VISA DEBIT",
                "bin": "411111",
                "accountType": "Visa Classic",
                "issuer": "CONOTOXIA SP. Z O.O",
                "card": {
                    "type": "001"
                },
                "binCountry": "PL"
            },
            "pointOfSaleInformation": {
                "terminalId": "092940"
            },
            "processorInformation": {
                "merchantNumber": "000000012345678",
                "approvalCode": "888888",
                "networkTransactionId": "123456789619999",
                "transactionId": "123456789619999",
                "responseCode": "100",
                "avs": {
                    "code": "X",
                    "codeRaw": "I1"
                }
            },
            "reconciliationId": "55849026C8YFWMER",
            "riskInformation": {
                "localTime": "7:48:10",
                "score": {
                    "result": "0",
                    "factorCodes": [
                        "B",
                        "Q",
                        "Y"
                    ],
                    "modelUsed": "default"
                },
                "infoCodes": {
                    "address": [
                        "INTL-SA",
                        "MM-A",
                        "MM-BIN",
                        "MM-C",
                        "MM-CO",
                        "MM-ST",
                        "MM-Z",
                        "UNV-ADDR"
                    ],
                    "phone": [
                        "RISK-PH",
                        "UNV-OC"
                    ],
                    "globalVelocity": [
                        "VELV-SA"
                    ],
                    "suspicious": [
                        "INTL-BIN",
                        "RISK-SD"
                    ],
                    "identityChange": [
                        "MORPH-B",
                        "MORPH-P",
                        "MORPH-S"
                    ]
                },
                "profile": {
                    "earlyDecision": "ACCEPT",
                    "name": "Rob Demo",
                    "selectorRule": "Rob"
                },
                "casePriority": "1"
            },
            "status": "AUTHORIZED",
            "submitTimeUtc": "2025-04-01T14:48:11Z"
        },
        "id": "7435188899356405003091",
        "message": "Request processed successfully.",
        "outcome": "AUTHORIZED",
        "status": "AUTHORIZED"
    },
    "retryNumber": 0,
    "eventType": "uc.orders.transactionresults",
    "eventDate": "2025-03-27T08:44:55",
    "transactionTraceId": "62dbbee0-c722-4ee0-b60c-1c2a62aff90e"
}
```

Enable Digital Payments {#uc-enable-digital-pay-intro}
======================================================

To enable digital payments on `Unified Checkout`, you must first register for each digital payment method that you would like enabled on your page. This enablement process sends the appropriate information to the digital payment systems and registers your page with each system.
This section contains information about enabling and managing digital payments on `Unified Checkout` in the `Business Center`:

* Apple Pay
  * Enrolling in Apple Pay
  * Preparing a device for testing Apple Pay on `Unified Checkout`
* `Click to Pay`
  * Enabling `Click to Pay`
* Google Pay
  * Enrolling in Google Pay
* Managing Google Pay authentication types

Enrolling in Apple Pay {#uc-enable-digital-pay-applepay}
========================================================

Apple Pay is a digital payment service that enables users to make secure and convenient transactions using their Apple devices. Users can add their credit or debit cards to the Wallet app and use them to pay online or in apps in a safe and convenient consumer experience.
To enable Apple Pay you must first host a public certificate on your web page and then pass your merchant name and domain name to Apple. Apple crawls out to your web page to validate the presence of this certificate to ensure the web pages are properly vetted and registered with Apple.
Follow these steps to validate your domain and enroll in Apple Pay:

1. Navigate to Payment Configuration \&gt; `Unified Checkout`.
2. In the Apple Pay section, click **Set Up**.
3. Follow the link to download the certificate.
4. Upload the *apple-developer-merchantid-domain-association* certificate file to your web server at:
   `/.well-known/apple-developer-merchantid-domain-association`
   You must verify that the file is accessible through HTTPS. You can validate this by visiting `https://&lt;your-domain&gt;/.well-known/apple-developer-merchantid-domain-association`.
5. Click Verify Domain.
6. Enter the domain name where you are hosting Apple Pay. This must be the same domain to which you uploaded the public certificate.
   Your domain is now verified for Apple Pay.

#### AFTER COMPLETING THE TASK

> IMPORTANT
> In order to run an end-to-end test of the Apple Pay service on ` Unified Checkout `, you must perform additional setup steps. See [Preparing a Device for Testing Apple Pay on Unified Checkout](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-applepay-prep-test-device.md "").

Preparing a Device for Testing Apple Pay on `Unified Checkout` {#uc-enable-digital-pay-applepay-prep-test-device}
=================================================================================================================

To run an end-to-end test of the Apple Pay service on `Unified Checkout`, you must prepare an Apple test device by loading Apple Pay test cards onto the device.

1. Follow these steps to prepare your Apple test device for end-to-end testing:

2. Make sure your Apple Developer account is configured for Apple Pay.

3. Register your Apple Pay test device with Apple.

4. Load Apple Pay test cards onto your Apple test device.

   #### ADDITIONAL INFORMATION

   The Apple Developer center provides the instructions in the [Sandbox Testing](https://developer.apple.com/apple-pay/sandbox-testing/ "") page for Apple Pay:

   1. Follow the steps described in Create a Sandbox Tester Account.
5. Follow the steps described in Adding a Test Card Number.

Enabling `Click to Pay` {#uc-enable-digital-pay-ctp}
====================================================

`Click to Pay` is a digital payment solution that allows customers to pay with their preferred card network and issuer without entering their card details on every website. Customers can use Visa, Mastercard, and American Express cards to streamline their purchase experience. `Click to Pay` provides a fast, secure, and consistent checkout experience across devices and browsers.
Follow these steps to enable in `Click to Pay` on `Unified Checkout`:

1. Navigate to Payment Configuration \&gt; `Unified Checkout`.
2. In the Click to Pay section, click **Set Up**.
3. Enter your business name and website URL.
4. Click Submit.
5. Contact your implementation contact or technical account manager to request that you be enabled for tokenization within `Click to Pay`. Your implementation contact or technical account manager will confirm that you were configured successfully and that you can now accept digital payments with `Click to Pay`.

   > IMPORTANT
   > ` Click to Pay ` uses network tokenization for transactions. These network tokens are stored in the vault of the token requestor ID (TRID) for the card scheme.

Set Up Customer Authentication for Visa Click to Pay {#uc-authentication-steps}
===============================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. These authentication methods are available:

* `3-D Secure`
* FIDO
* Card verification value (CVV)
* One-time password (OTP)

> IMPORTANT
> After you complete these steps, Visa determines which authentication method to use. When Visa determines that they will authenticate, they authenticate each Click to Pay transaction through the appropriate method. This may be a frictionless authentication or the customer may need to provide more information when required by the issuer. This is available only through Visa.
> IMPORTANT
> Visa Click to Pay customer authentication is not the same as ` Payer Authentication ` using the complete mandate. See [Test Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-authentication.md "").

1. Log in to the `Business Center`:
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `
   Production URL: ` `<https://businesscenter.cybersource.com>` `
   If you are unable to access this page, contact your sales representative. {#uc-authentication-steps_step-1}
   {#uc-authentication-steps_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)
   If Click to Pay is not enabled, click **On** next to Click to Pay.
   ![Manage Available Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#uc-authentication-steps_step-2}
   {#uc-authentication-steps_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.
   ![Value Added Solutions Page](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Visa the information that is required for authentication. IMPORTANT
   Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.

Click to Pay Customer Authentication {#uc-authentication}
=========================================================

When you enable customer authentication through Click to Pay, you give `Cybersource` permission to send Visa the required authentication information for each transaction. When the customer completes a transaction using a Visa card that is already stored in Click to Pay, authentication is managed with Click to Pay. When the customer checks out using manual card entry and does not save their card to Click to Pay, the transaction is not processed through Click to Pay and you must complete authentication based on your existing authentication method.
Click to Pay authentication is only available for Visa branded cards that are tokenized with Click to Pay. If Click to Pay does not authenticate the transaction, but you are using the complete mandate with the consumerAuthentication field set to `true`, authentication is attempted as part of this request. When you do not use the complete mandate, you must check the result of the cardholderAuthenticationStatus field in the transient token and reqeust `Payer Authentication` directly when it is required.

> IMPORTANT
> American Express and Mastercard card brands cannot be authenticated through Click to Pay customer authentication.

Visa Prerequisites
------------------

Before you can begin customer authentication using Click to Pay, you must meet these requirements:

* The allowPaymentTypes field must include `CLICKTOPAY` in the capture context. For more information, see [Capture Context](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-ss-setup/uc-capture-context-intro.md "").
* The transacting merchant ID that sends the transaction requests must be configured for tokenization with Click to Pay. You must contact your implementation consultant or technical account manager to configure tokenization with Click to Pay.
* Set up Visa customer authentication in the `Business Center`. For information, see [Set Up Customer Authentication for Visa Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication-steps.md "").

Authentication Flow
-------------------

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ctp-auth-flow-740x800.svg/jcr:content/renditions/original)

Enrolling in Google Pay {#uc-enable-digital-pay-google}
=======================================================

Google Pay is a digital payment product offered by Google through Chrome browsers and Android devices.
Follow these steps to enroll in Google Pay on `Unified Checkout`:

1. Navigate to Payment Configuration \&gt; `Unified Checkout`.
2. In the Google Pay section, click **Set Up**.
3. Enter your business name.
4. Click Submit.
   You can now accept digital payments with Google Pay.

#### AFTER COMPLETING THE TASK

> IMPORTANT
> When you enable Google Pay on ` Unified Checkout `, you can specify an optional parameter that defines the types of credentials that Google Pay sends you. See [Managing Google Pay Authentication Types](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-googlepay-manage-authenticat.md "").

Managing Google Pay Authentication Types {#uc-enable-digital-pay-googlepay-manage-authentication}
=================================================================================================

Additional controls are available for Google Pay on `Unified Checkout`. When you enable Google Pay on `Unified Checkout`, you can specify optional parameters that define the types of card authentication you receive from Google Pay. To manage the types of credentials that Google Pay sends, use this expanded payment type object within the allowedPaymentTypes section of the sessions request:

```
{
  "type": "GOOGLEPAY",
  "options": { "allowedAuthMethods": "&lt;authentication type&gt;"
  }
}
```

The expanded payment type object has these parameters:

* type: Defines the type of payment option.
* options: Contains specific payment types parameters.
  For Google Pay, use the new data element allowedAuthMethods within the options section of the payment types object to specify the authentication type you will receive from Google Pay. Possible values:
  * `PAN_ONLY`: Google returns primary account number (PAN) values
  * `CRYPTOGRAM_3DS`: Google returns fully authenticated network token values.
    By default, Google sends both authentication types.
    When the complete mandate is used and Google Pay does not authenticate the transaction, then `Unified Checkout` completes the authentication request as part of the complete mandate.
    REST Example: Specify Only PAN Authentication Accepted from Google
    This sessions request example specifies that Google Pay is to send only PAN values.

```
"allowedPaymentTypes": [
  "PANENTRY" {
    "type": "GOOGLEPAY",
    "options": {
      "allowedAuthMethods": "PAN_ONLY"
    }
  },
  "CLICKTOPAY",
  "PAZE"
]
```

REST Example: Simple Google Pay Request
This sessions request example specifies that Google Pay can send all authentication types.

```
"allowedPaymentTypes": [
  "PANENTRY",
  "GOOGLEPAY",
  "CLICKTOPAY",
  "PAZE",
  "CHECK"
]
```

Enrolling in Echeck/ACH Services {#uc-enable-digital-pay-echeck}
================================================================

`Unified Checkout` can accept bank account payments using the eCheck product. To accept eCheck payments through `Unified Checkout`, you must have the eCheck processing service enabled. To request access to eCheck processing and enable eCheck, you must submit an application in the `Business Center`. Once your application is approved, you can accept eCheck payments.
For step-by-step instructions on enrolling and enabling eCheck, see the "Getting Started with the eCheck Service" section of the *[eCheck Merchant Guide](https://developer.cybersource.com/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-gs.md "")* . If eCheck is not listed in the Available Products section in the `Business Center`, you must contact your portfolio owner to enable your account to apply for eCheck.
IMPORTANT If you have a business account or a financial relationship with Bank of America, Wells Fargo, or Chase, and you would like them to process your transactions, you must contact our Sales or Support team for more information on our ACH product.

Enrolling in Alternative Payment Methods {#uc-enable-altpay}
============================================================

Before you can enroll in alternative payment methods on `Unified Checkout`, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.

Manage Permissions {#uc-manage-permissions-intro}
=================================================

Portfolio administrators can set permissions for new or existing `Business Center` user roles for `Unified Checkout`. Administrators retain full read and write permissions. They enable you to regulate access to specific pages and specify who can access, view, or amend digital products within `Unified Checkout`.
Portfolio administrators must apply the appropriate user role permission for any existing or newly created `Business Center` user roles for `Unified Checkout`. For information on managing permissions as a portfolio administrator, see [Managing Permissions as a Portfolio Administrator](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-manage-permissions-intro/uc-manage-permissions-port.md "").
If you are a transacting merchant, you might find that your permissions are restricted. If your permissions are restricted, a message appears indicating that you do not have access, or buttons might appear gray. To make changes to your digital products within `Unified Checkout` that have restricted permissions, contact your portfolio administrator's customer support representative. For more information, see [Managing Permissions as a Direct Merchant](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-manage-permissions-intro/uc-manage-permissions-merch.md "").

Managing Permissions as a Direct Merchant {#uc-manage-permissions-merch}
========================================================================

Follow these steps to configure and manage user permissions in the `Business Center` for `Unified Checkout` as a direct merchant:

1. On the left navigation panel, navigate to Account Management.

2. Click Roles to display a list of your user roles.

3. Click the pencil icon next to the user role that you want to update.

4. Click Payment Configuration Permission.

5. Select the relevant permission for the specific user role you are editing. You can select from these `Unified Checkout` permissions:

   * Unified Checkout View
   * Unified Checkout Manage

   > IMPORTANT
   > If you are a transacting merchant without view permissions, ` Unified Checkout ` will still appear on the navigation bar, however, a *no access* message appears when you access ` Unified Checkout `.
   > If you are a transacting merchant with view permissions but not management permissions, you can access the ` Unified Checkout ` screens and view the different payment methods configurations, however, you cannot edit or enroll new products.

Managing Permissions as a Portfolio Administrator {#uc-manage-permissions-port}
===============================================================================

Follow these steps to configure and manage user permissions in the `Business Center` for `Unified Checkout` as a portfolio administrator:

1. On the left navigation panel, navigate to Account Management.{#uc-manage-permissions-port_step-1}
   {#uc-manage-permissions-port_step-1}

2. Click Roles to see a list of your user roles.{#uc-manage-permissions-port_step-2}
   {#uc-manage-permissions-port_step-2}

3. Click the pencil icon next to the user role that you want to update.{#uc-manage-permissions-port_step-3}
   {#uc-manage-permissions-port_step-3}

4. Click Payment Configuration Permission. {#uc-manage-permissions-port_step-4}
   {#uc-manage-permissions-port_step-4}

5. Select the relevant permission for the specific user role you are editing. You can choose from these `Unified Checkout` permissions:

   * Unified Checkout View
   * Unified Checkout Manage
   * Unified Checkout Portfolio View (available for portfolio users only)
   * Unified Checkout Portfolio Manage (available for portfolio users only)

   > IMPORTANT
   > If all permissions are left unselected, the user has restricted permission. A *no access* message appears when the user tries to access the ` Unified Checkout ` digital product enablement pages. The user is advised to contact a customer representative.
   > If a portfolio user has view permissions and does not have a management role, they can access the ` Unified Checkout ` pages, but they cannot modify toggles for different digital payments.
   > {#uc-manage-permissions-port_step-5}
   > {#uc-manage-permissions-port_step-5}

Test Your `Unified Checkout` Configuration {#uc-reference-test-cards}
=====================================================================

Use these test card numbers to test your `Unified Checkout` configuration.
Combine the BIN with the card number when sending to `Unified Checkout`.

`Unified Checkout` Test Cards {#uc-reference-test-cards-uc}
===========================================================

To test `Payer Authentication`, you must use `Payer Authentication` test cards. See [Test Cases for 3-D Secure 2.x](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "") in the *`Payer Authentication` Developer Guide*.

|    Card Brand    |  BIN   | Card Number  | Expiration Date | CVV  |
|------------------|--------|--------------|-----------------|------|
| Visa             | 411111 | 1111111111   | 12/2025         | 123  |
| Mastercard       | 555555 | 5555554444   | 02/2026         | 265  |
| American Express | 378282 | 246310005    | 03/2026         | 7890 |
| Cartes Bancaires | 436000 | 0001000005   | 04/2040         | 123  |
| Carnet           | 506221 | 0000000009   | 04/2024         | 123  |
| China UnionPay   | 627988 | 6248094966   | 04/2040         | 123  |
| Diners Club      | 305693 | 09025904     | 04/2040         | 123  |
| Discover         | 644564 | 4564456445   | 04/2040         | 123  |
| JCB              | 353011 | 13333 0000   | 04/2040         | 123  |
| Jaywan           | 679009 | 0000002009   | 04/2040         | 123  |
| Paypak           | 220543 | 0000003002   | 04/2040         | 123  |
| Maestro          | 675964 | 9826438453   | 04/2040         | 123  |
| mada             | 446404 | 0000000007   | 04/2040         | 123  |
| ELO              | 451416 | 0000000003   | 04/2040         | 123  |
| JCrew            | 515997 | 1500000005   | 04/2040         | 123  |
| EFTPOS           | 401795 | 000000000009 | 04/2040         | 123  |
| Meeza            | 507808 | 3000000002   | 04/2040         | 123  |
[Test Card Numbers]

Test Cards for `Click to Pay` Authentication by `Unified Checkout`
------------------------------------------------------------------

se these test cards to test when you use a `Click to Pay` card with authentication performed outside `Click to Pay` and the consumerAuthentication field is set to `true` in the capture context.
Replace the X in the card number with 0.
To manage Visa test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Visa       | 46229431231X2X56 | 12/2026         | 432 |
| Visa       | 46229431231X232X | 12/2026         | 581 |
| Mastercard | 512X35X1XXX64578 | Any future date | Any |
| Mastercard | 512X35X1XXX64552 | Any future date | Any |
[Test Card Numbers for Authentication Outside `Click to Pay` Flow]

Visa and Mastercard `Click to Pay` Test Cards {#uc-reference-test-cards-visa-ctp}
=================================================================================

Visa Test Cards {#uc-reference-test-cards-visa-ctp_uc-reference-test-cards-visa-ctp}
------------------------------------------------------------------------------------

These Visa test cards can be added to your `Click to Pay` wallet.
Replace the X in the card number with 0.
You can manage your Visa `Click to Pay` test cards and account here:

* **Production:** [login](https://src.visa.com/login "")
* **Test:** [login](https://sandbox.src.visa.com/login "")
  To manage Visa test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| 46229431231X2700 | 12/2026         | 938 |
| 46229431231X2718 | 12/2026         | 605 |
| 46229431231X2726 | 12/2026         | 579 |
| 46229431231X2734 | 12/2026         | 141 |
| 46229431231X2742 | 12/2026         | 279 |
| 46229431231X2759 | 12/2026         | 669 |
| 439584XXX449X11X | 12/2025         | 509 |
| 439584XXX282X11X | 12/2025         | 693 |
[Visa Test Card Numbers]

Mastercard Test Cards {#uc-reference-test-cards-visa-ctp_uc-reference-test-cards-visa-ctp-mc}
---------------------------------------------------------------------------------------------

Mastercard test cards can be added to your `Click to Pay` wallet. You must retrieve Mastercard test cards from their `Click to Pay` test page: [#test-cards](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "")
Mastercard has different test cards for retrieving tokenized and non-tokenized data. `Cybersource` recommends that you use these test cards as follows:

* Test cards to retrieve PAN data: Use these cards when the customer is completing checkout as a one-time guest and does not have a `Click to Pay` account or want to create one.

* Test cards to retrieve token data: Use these cards for tokenized `Click to Pay` transactions.
  You can manage your Mastercard `Click to Pay` test cards and account here:

* **Live:** [enroll](https://src.mastercard.com/profile/enroll "")

* **SBX:** [enroll](https://sandbox.src.mastercard.com/profile/enroll "")
  To manage Mastercard test cards for customer authentication, contact your implementation consultant or technical account manager.

Test Cards for Authentication by `Click to Pay` {#uc-reference-test-cards-auth-ctp}
===================================================================================

Use these cards when authentication is performed by `Click to Pay` within the `Click to Pay` flow.
Replace the X in the card number with 0.
To manage Visa test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Visa       | 43958XXX0449X11X | 12/2025         | 509 |
| Visa       | 439584XXX282X11X | 12/2025         | 693 |
| Visa       | 439584XX91X1XX11 | 12/2025         | 676 |
| Visa       | 439584XX9119XX11 | 12/2025         | 789 |
[`Click to Pay` Test Card Numbers for Authentication in `Click to Pay` Flow]

For information about testing authentication, see[Test Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-authentication.md ""). For information about enabling Visa customer authentication, see [Set Up Customer Authentication for Visa Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication-steps.md "").

Echeck Test Values {#uc-reference-test-cards-auth-echeck}
=========================================================

These eCheck test values can be used to process a test eCheck transactions:

* **Routing number:** Set to 071923284
* **Account number:** Set to any supported value. For example, 1234567890.

Payment Methods {#uc-pay-methods-intro}
=======================================

This section describes the payment methods you can use in your `Unified Checkout` integration. After you successfully integrate one payment method, you can add another from the same category with minimal adjustments to your existing configuration.
These payment methods are available:

* [Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-card.md "")
* [Online Bank Transfers](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-obt.md "")
* [Buy Now, Pay Later](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-bnpl.md "")
* [Post-Pay Reference Payments](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-ppr.md "")

Cards {#uc-pay-methods-card}
============================

`Unified Checkout` accepts multiple card types including global networks such as Visa, Mastercard, and American Express. `Unified Checkout` also accepts local schemes such as Cartes Bancaires in France, EFTPOS in Australia, and PayPak in Pakistan.

Card Support
------------

Support for card brands varies based on the payment method for these services:

* Payments
* `Decision Manager`
* `Payer Authentication`
  This table shows which card types are accepted for each payment method and which region:

|      Region       |    Card Brand    |                                                      Manual Card Entry                                                       |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                          Google Pay                                                          |                                                             Paze                                                             |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | EFTPOS           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | JCB              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Meeza            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | American Express | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Diners Club      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Mastercard       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Visa             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | Carnet           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | ELO              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | Discover         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | JCrew            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
[Card Brand by Region and Payment Method]

|      Region       |    Card Brand    |                                                      Manual Card Entry                                                       |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                          Google Pay                                                          |                                                             Paze                                                             |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | EFTPOS           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | JCB              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Meeza            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | American Express | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Diners Club      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Mastercard       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Visa             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | Carnet           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | ELO              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | Discover         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | JCrew            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
[Card Brand by Region and Payment Method]

This table shows which card types are supported for each complete mandate feature by region.

|      Region       |    Card Brand    |                                                        Authorization                                                         |                                                    `Payer Authentication`                                                    |                                                      `Decision Manager`                                                      |                                          Token Create by `Token Management Service`                                          |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | EFTPOS           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | JCB              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| CEMEA             | Meeza            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | American Express | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Diners Club      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Mastercard       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Visa             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | Carnet           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | ELO              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | Discover         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | JCrew            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Card Support for the Complete Mandate]

Online Bank Transfers {#uc-pay-methods-obt}
===========================================

Online bank transfers enable customers to complete their purchase by securely logging into their online banking environment. This method is secure, trusted, and widely used in many European countries.
This is how online bank transfers work:

#### Figure:

Online Bank Transfers ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-obt-650x130.svg/jcr:content/renditions/original)
1. The customer chooses online bank transfer as their payment method during checkout.
2. The customer chooses their bank from the list of available banks and is redirected to their bank's website or application where they are prompted to enter their account credentials.
3. The customer confirms their payment and completes the authorization process.
4. The customer is notified that the payment is complete.
5. The customer returns to your website for payment confirmation.
   `Unified Checkout` supports these online bank transfer payment methods:

* Bancontact
* DragonPay
* iDeal
* Multibanco
* MyBank
* Przelewy24\|P24
* Tink Pay By Bank

| Payment Method  | Method | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer Currency |
|-----------------|--------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|-------------------|
| iDEAL           | `PPRO` | `IDEAL`                             | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Netherlands (NL)                | EUR               |
| Multibanco      | `PPRO` | `MULTIBANCO`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR               |
| Przelewy24\|P24 | `PPRO` | `P24`                               | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Poland (PL)                     | PLN               |
| Bancontact      | `PPRO` | `BANCONTACT`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR               |
| MyBank          | `PPRO` | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Italy (IT)                      | EUR               |
| MyBank          | `PPRO` | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR               |
| MyBank          | `PPRO` | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR               |
| MyBank          | `PPRO` | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Spain (ES)                      | EUR               |
| DragonPay       | `PPRO` | `DRAGONPAY`                         | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Philippines (PH)                | PHP               |
[Online Bank Transfer Payment Methods Enabled by PPRO]

|  Payment Method  | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer Currency |
|------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|-------------------|
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | United Kingdom (GB)             | GBP               |
[Online Bank Transfer Payment Methods Not Enabled by PPRO]

Bancontact {#uc-pay-methods-obt-bancontact}
===========================================

Bancontact enables customers to make secure online and in-store purchases directly from their bank accounts. Bancontact is a leading payment method in Belgium.
When the total amount of the order is outside the range of accepted transaction amounts, the Bancontact payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: Not applicable

Opt in to Bancontact on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Bancontact on `Unified Checkout`:

1. Add Bancontact to your integration by adding `BANCONTACT` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.address1

* orderInformation.billTo.email

DragonPay {#uc-pay-methods-obt-dragonpay}
=========================================

DragonPay provides Filipino customers and businesses with a secure payment channel that does not require customers to be banked or have a credit card. Customers can make purchases online and pay by bank transfer.
When the total amount of the order is outside the range of accepted transaction amounts, the DragonPay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PHP 50.01
* **Maximum transaction amount**: Not applicable

Opt in to DragonPay on `Unified Checkout`
-----------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add DragonPay to your integration by adding `DRAGONPAY` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.address1

* orderInformation.billTo.email

iDeal {#uc-pay-methods-obt-ideal}
=================================

iDEAL enables customers to pay online through their mobile banking app or online bank account and provides you with a payment guarantee. iDEAL supports these banks:

* ABN AMRO

* ASN Bank

* bunq

* ING

* Knab

* Rabobank

* RegioBank

* Revolut

* SNS

* Svenska Handelsbanken

* Triodos Bank

* Van Lanschot
  When the total amount of the order is outside the range of accepted transaction amounts, the iDeal payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01

* **Maximum transaction amount**: Subject to transaction approval from the customer's account.

Opt in to iDeal on `Unified Checkout`
-------------------------------------

Follow these steps to opt in to iDeal on `Unified Checkout`:

1. Add iDeal to your integration by adding `IDEAL` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.address1

* orderInformation.billTo.email

MyBank {#uc-pay-methods-obt-mybank}
===================================

MyBank enables customers to pay for their online purchases in an easy and safe way using real-time bank transfers. MyBank customers complete payments by selecting their bank and logging in with their online banking credentials.
When the total amount of the order is outside the range of accepted transaction amounts, the MyBank payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: EUR 999,999,999.99

Opt in to MyBank on `Unified Checkout`
--------------------------------------

Follow these steps to opt in to MyBank on `Unified Checkout`:

1. Add MyBank to your integration by adding `MYBANK` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.address1

* orderInformation.billTo.email

Multibanco {#uc-pay-methods-obt-multibanco}
===========================================

Multibanco enables customers to pay for a range of goods and services by bank transfer. These services include e-commerce, licenses, and taxes post-purchase. Multibanco is supported by all banks in Portugal.
When the total amount of the order is outside the range of accepted transaction amounts, the Multibanco payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: No minimum
* **Maximum transaction amount**: EUR 99,999

Opt in to Multibanco on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add Multibanco to your integration by adding `MULTIBANCO` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.address1

* orderInformation.billTo.email

Przelewy24\|P24 {#uc-pay-methods-obt-p24}
=========================================

Przelewy24, or P24, is a Poland-based real-time online bank transfer payment method. P24 is one of the most popular payment methods in Poland covering all major consumer banks.
When the total amount of the order is outside the range of accepted transaction amounts, the P24 payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PLN 0.01, EUR 0.01
* **Maximum transaction amount**: PLN 55,000.00, EUR 12,500.00

Opt in to Przelewy24\|P24 on `Unified Checkout`
-----------------------------------------------

Follow these steps to opt in to Przelewy24\|P24 on `Unified Checkout`:

1. Add Przelewy24\|P24 to your integration by adding `P24` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.email
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:

* orderInformation.billTo.address1

Tink Pay By Bank {#uc-pay-methods-obt-tink}
===========================================

Tink is an alternative payment method that uses the *pay by bank* payment method. Tink Pay By Bank enables customers to make payments directly from their bank account to the seller's account and bypasses traditional payment methods such as credit cards.
When the total amount of the order is outside the range of accepted transaction amounts, Tink Pay By Bank is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: Not applicable
* **Maximum transaction amount**: GBP 8,500

Opt in to Tink Pay By Bank on `Unified Checkout`
------------------------------------------------

Follow these steps to opt in to Tink Pay By Bank on `Unified Checkout`:

1. Add Tink Pay by Bank to your integration by adding `TINKPAYBYBANK` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.billTo.country
4. Include this optional field for online bank transfers in the capture context request:
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
   * orderInformation.shipTo.address1
   * orderInformation.shipTo.address2
   * orderInformation.shipTo.country
   * orderInformation.shipTo.district
   * orderInformation.shipTo.firstName
   * orderInformation.shipTo.lastName
   * orderInformation.shipTo.locailty

* orderInformation.shipTo.postalCode

Verify Status for Online Bank Transfers (PPRO Enabled) {#uc-pay-methods-obt-status-ppro}
========================================================================================

When the status of your payment request is `PENDING`, you can verify the status by using the URL method and the payload that is included in the transactionStatus.url field in the webhook response:

```
{
  "payload": {
    "transactionResult": {
      "id": "7557753337236357904806",
      "rootId": "7557753337236357904806",
      "reconciliationId": "XFZ40EJPGL5K",
      "submitTimeUTC": "2025-08-21T11:22:13Z",
      "merchantId": "uc_apm_tester004"
    },
    "transactionStatus": {
      "url": "https://apitest.cybersource.com/tss/v2/transactions/7557753337236357904806",
      "method": "GET"
    }
  }
}
```

For more information, see [Webhooks Support](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-appendix-webhooks.md "").

Verify Status for Online Bank Transfers (Tink Pay By Bank) {#uc-pay-methods-obt-status-non-ppro}
================================================================================================

When the status of your payment request is `PENDING`, you can verify the status by using the URL method and the payload that is included in the transactionStatus.url field in the webhook response:

```
"payload": {
    "transactionResult": {
      "submitTimeUtc": "2025-07-22T08:16:24Z",
      "reconciliationId": "KPUJHD4X2G31",
      "processorInformation": {
        "responseCode": "00004"
      },
      "id": "7531173918516064204807",
      "message": "Request was processed successfully.",
      "status": "SETTLED"
    },
    "transactionStatus": {
      "url": "https://apitest.cybersource.com/pts/v2/refresh-payment-status/7531173918516064204807",
      "method": "POST",
      "payload": {
        "clientReferenceInformation": {
          "applicationName": "unifiedCheckout"
        },
        "processingInformation": "processingInformation",
        "paymentInformation": {
          "paymentType": {
            "method": {
              "name": "tinkPayByBank"
            },
            "name": "bankTransfer"
          }
        }
      }
    }
    }
```

You can also send a request to this endpoint to verify the status:
**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*
The *{id}* is the ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-obt-handle-response}
======================================================

When you process a payment using unifiedPayment.complete() in `Unified Checkout`, you must handle both successful responses and various errors. After the payment is complete, the completeResponse object contains information about the transaction outcome.
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` and `COMPLETE_TRANSACTION_FAILED`. `COMPLETE_TRANSACTION_CANCELED` occurs when the user cancels the transaction and `COMPLETE_TRANSACTION_FAILED` indicates that the consumer's transaction failed.
For PPRO-enabled online bank transfers, only cancellation errors are returned, and Tink Pay By Bank returns failure and cancellation errors. For information about possible errors that can occur when calling the complete API see [Class: AcceptError](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix-js-reference/uc-appendix-js-class-accept-error.md "").

Buy Now, Pay Later {#uc-pay-methods-bnpl}
=========================================

Buy Now, Pay Later payment methods enable customers to purchase goods or services immediately and pay in installments over time. With Buy Now, Pay Later, you are paid immediately and in full, while your customers pay nothing or only a portion of the total at the time of purchase. The remaining balance is typically spread over equal, often interest-free, payments.
Buy Now, Pay Later is increasingly popular for both online and in-store purchases.
This is how Buy Now, Pay Later works:

#### Figure:

Buy Now, Pay Later ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-bnpl-650x150.svg/jcr:content/renditions/original)
1. The customer chooses their Buy Now, Pay Later payment method during checkout.
2. The customer chooses how much they want to pay, such as nothing, installments, or the total amount.
3. The unpaid amount is divided into equal installments that are paid over a fixed amount of time.
4. You receive the full payment after the customer completes checkout, and the Buy Now, Pay Later provider collects the installment payments from your customer.
   `Unified Checkout` supports the Afterpay/Clearpay Buy Now, Pay Later payment method.

|  Payment Method   | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer ISO Country Code | Customer ISO Currency Code |
|-------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------|----------------------------|
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | CA                        | CAD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | CA                        | CAD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | AU                        | AUD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | AU                        | USD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | NZ                        | NZD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | NZ                        | NZD                        |
| Cash App Afterpay | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | US                        | USD                        |
| Cash App Afterpay | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | US                        | USD                        |
| Clearpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | GB                        | GBP                        |
| Clearpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | GB                        | GBP                        |
[Buy Now, Pay Later Payment Method Support]

For information on ISO country codes, see [ISO Standard Country Codes](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.md "").
For information on ISO currency codes, see [ISO Standard Currency Codes](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "").

Afterpay {#uc-pay-methods-bnpl-opt-in}
======================================

Afterpay is a Buy Now, Pay Later service that allows customers to purchase items immediately and pay for them in four interest-free installments over a period of 6 weeks. Afterpay is also known as Clearpay in the UK, and Cash App Afterpay in the US. For more information, see the [*Afterpay and Clearpay Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/afterpay/developer/all/so/afterpay/afterpay-intro.md "").
When the total amount of the order is outside the range of accepted transaction amounts, the Afterppay/Clearpay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: 1 (CAD, AUD, NZD, USD, and GBP)
* **Maximum transaction amount**: Not applicable

Opt in to Afterpay on `Unified Checkout`
----------------------------------------

Follow these steps to opt in to the Afterpay/Clearpay payment method in `Unified Checkout`:

1. Add Afterpay to your integration by adding `AFTERPAY` to the allowedPaymentTypes field within the capture context request. The default field value is `AFTERPAY` even if you want to support Cash App Afterpay in the US or Clear Pay in the UK.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   You can capture the funds later if you include the completeMandate.type field in the capture context request and set the value to `AUTH`. When you capture the funds later, you must perform a capture using the payments API. See [Captures](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-pay-methods-intro/uc-pay-methods-bnpl/uc-pay-methods-captures.md "").
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * orderInformation.billTo.email
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
   * orderInformation.billTo.address1
   * orderInformation.billTo.locality
   * orderInformation.billTo.postalCode
   * orderInformation.billTo.administrativeArea
   * orderInformation.billTo.country
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * orderInformation.shipTo.firstName
   * orderInformation.shipTo.lastName
   * orderInformation.shipTo.address1
   * orderInformation.shipTo.locality
   * orderInformation.shipTo.postalCode
   * orderInformation.shipTo.administrativeArea

* orderInformation.shipTo.country

Handle Responses {#uc-pay-methods-bnpl-handle-response}
=======================================================

When you process a payment using unifiedPayment.complete() in `Unified Checkout`, you must handle both successful responses and various errors. After the payment is complete, the completeResponse object contains information about the transaction outcome.
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` and `COMPLETE_TRANSACTION_FAILED`. `COMPLETE_TRANSACTION_CANCELED` occurs when the user cancels the transaction and `COMPLETE_TRANSACTION_FAILED` indicates that the consumer's transaction failed.

Captures {#uc-pay-methods-captures}
===================================

When you set the completeMandate.type field value to `AUTH` or `PREFER_AUTH`, you must send a request to capture an authorized payment. Full and partial captures are supported.

Endpoint {#uc-pay-methods-captures_d9e145}
------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-captures_d9e154}
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-captures_d9e167}
The *{id}* is the transaction ID returned in the authorization response.

Example: Authorization Response from `Unified Checkout`
-------------------------------------------------------

```
{
  "details": {
    "clientReferenceInformation": {
      "code": "1753351101383"
    },
    "orderInformation": {
      "amountDetails": {
        "currency": "USD",
        "totalAmount": "21.00"
      }
    },
    "processorInformation": {
      "approvalCode": "AUTH456789",
      "responseCode": "00003",
      "responseDetails": "00003",
      "transactionId": "2016011808153910011808153AUTH"
    },
    "reconciliationId": "04RYADD29YRO",
    "submitTimeUtc": "2025-07-24T09:58:21Z"
  },
  "id": "7533511014286971803092",
  "message": "Request processed successfully.",
  "outcome": "AUTHORIZED",
  "status": "AUTHORIZED"
}
```

Response Status
---------------

`Cybersource` responds to your capture request with one of these statuses:

* `FAILED`: The capture request failed.
* `PENDING`: The capture request is accepted but not captured. Send a request to the check status service to retrieve status updates.
* `SETTLED`: The capture request is settled for the amount requested.

Post-Pay Reference Payments {#uc-pay-methods-ppr}
=================================================

Post-pay reference payments provide an alternative way for your customers to complete online purchases using cash. During checkout, customers select a voucher payment option and receive a unique code or payment slip. To finalize their purchase, they visit a designated offline location, such as a convenience store or payment kiosk, and pay the required amount in person. Once the payment is made, the merchant receives a notification that they can process the order.
Post-pay reference payments are widely used in countries where cash transactions are common or where many customers don't have access to credit or debit cards.
This is how post-pay reference payments work:
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-ppr-650x175.svg/jcr:content/renditions/original)
1. The customer selects a convenience store/voucher payment method during checkout.
2. The customer receives their payment code/voucher or QR code.
3. The customer presents the payment code/voucher or QR in-store to complete the payment.
4. The customer receives a notification that the payment is complete.
   `Unified Checkout` supports the Konbini voucher-based payment option:

| Payment Method | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country | Customer Currency |
|----------------|-------------------------------------|--------------------------------------|-------------------|----------------------|------------------|-------------------|
| Konbini        | `KONBINI`                           | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Japan (JP)       | JPY               |
[Post-Pay Reference Payment Support]

Konbini {#uc-pay-methods-ppr-konbini}
=====================================

Konbini is used to make cash payments in Japan. Konbini payments enable your customers to pay for bills and online purchases at convenience stores in Japan.To complete a transaction, your customers receive payment codes for specific convenience stores and a confirmation number. Customers must then bring the information to a convenience store to make a cash payment. Your customers can pay at these convenience stores in Japan:

* 7-Eleven

* Family Mart

* Lawson

* Ministop

* Seicomart
  You receive the payment confirmation immediately and the funds are available after 4 business days.
  When the total amount of the order is outside the range of accepted transaction amounts, the Konbini payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: JPY 1

* **Maximum transaction amount**: Not applicable

Opt in to Konbini on `Unified Checkout`
---------------------------------------

Follow these steps to opt in to the Konbini payment method in `Unified Checkout`:

1. Add Konbini to your integration by adding `KONBINI` to the allowedPaymentTypes field within the capture context request.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * orderInformation.billTo.country
   * orderInformation.billTo.firstName
   * orderInformation.billTo.lastName
   * orderInformation.billTo.phoneNumber
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * orderInformation.billTo.address1

* orderInformation.billTo.email

Verify Status for Post-Pay Reference (PPRO Enabled) {#uc-pay-methods-ppr-status-ppro}
=====================================================================================

When the status of your payment request is `PENDING`, you can verify the status by sending a GET request to the URL that is included in the transactionStatus.url field in the response:

```
"payload": {
    "transactionResult": {
        "id": "7557753337236357904806",
        "rootId": "7557753337236357904806",
        "reconciliationId": "XFZ40EJPGL5K",
        "submitTimeUTC": "2025-08-21T11:22:13Z",
        "merchantId": "uc_apm_tester004"
    },
    "transactionStatus": {
        "url": "https://apitest.cybersource.com/tss/v2/transactions/7557753337236357904806",
        "method": "GET"
      }
    }
}
```

You can also send a request to this endpoint to verify the status:
**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-ppr-status-ppro_restcapture}
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-ppr-status-ppro_restcapture-test}
The *`{id}`* is ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-ppr-handle-response}
======================================================

When you process a payment using unifiedPayment.complete() in `Unified Checkout`, you must handle both successful responses and various errors. After the payment is complete, the completeResponse object contains information about the transaction outcome.
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` which is returned when the user cancels the transaction.
For PPRO-enabled online bank transfers, only cancellation errors are returned. For information about possible errors that can occur when calling the complete API see [Class: AcceptError](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix-js-reference/uc-appendix-js-class-accept-error.md "").

`Unified Checkout` Appendix {#uc-appendix}
==========================================

`Unified Checkout` UI {#uc-ui-screens}
======================================

Completing a payment with `Unified Checkout` requires the customer to navigate through a sequence of interfaces. This section includes examples of the interfaces your customers can expect when completing a payment with these payment methods on `Unified Checkout`:
* Apple Pay
* `Click to Pay`
* Google Pay
* Manual payment entry
* Payment with a bank account
* Paze

Apple Pay UI {#uc-ui-applepay}
==============================

These screen captures show the sequence of events your customer can expect when completing a payment with Apple Pay.

#### Figure: {#uc-ui-applepay_fig-uc-ui-applepay}

Apple Pay UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-apple-pay-865x575.svg/jcr:content/renditions/original)

`Click to Pay` UI {#uc-ui-ctp}
==============================

These screen captures show the sequence of events your customer can expect when completing a payment with `Click to Pay`.

#### Figure: {#uc-ui-ctp_fig-uc-ui-ctp}

`Click to Pay` UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ctp-865x480.svg/jcr:content/renditions/original)

Google Pay UI {#uc-ui-googlepay}
================================

These screen captures show the sequence of events your customer can expect when completing a payment with Google Pay.

#### Figure:

Google Pay UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-google-pay-865x575.svg/jcr:content/renditions/original)

Manual Payment Entry UI {#uc-ui-manualentry}
============================================

These screen captures show the sequence of events your customer can expect when completing a payment by manually entering payment, shipping, and contact information.

#### Figure:

Manual Entry Payment Details ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-manual-card-entry-645x600.svg/jcr:content/renditions/original)

#### Figure:

Manual Entry Contact Details ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-manual-card-entry-contact-details-645x345.svg/jcr:content/renditions/original)

#### Figure:

Manual Entry Review and Confirm ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-manual-card-entry-optional-review-645x345.svg/jcr:content/renditions/original)

Pay with Bank Account UI {#uc-ui-echeck}
========================================

These screen captures show the sequence of events your customer can expect when completing a payment with a bank account.

#### Figure:

Pay with Bank Account Order Summary ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-645x375.svg/jcr:content/renditions/original)

#### Figure:

Pay with Bank Account Checkout ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-manual-entry-645x545.svg/jcr:content/renditions/original)

#### Figure:

Pay with Bank Account Review and Confirm ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-op-review-645x375.svg/jcr:content/renditions/original)

Paze UI {#uc-ui-paze}
=====================

These screen captures show the sequence of events your customer can expect when completing a payment with Paze.

#### Figure:

Paze UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-paze.png/jcr:content/renditions/original)

JSON Web Tokens {#uc-appendix-jwts}
===================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```
* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```
* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#uc-appendix-jwts_ul_ozy_ysn_4pb}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

`Unified Checkout` Integration Examples {#uc-appendix-uc-examples}
==================================================================

This section contains the information you need in order to integrate `Unified Checkout` within your e-commerce experience and use the `unifiedPayment.complete()` method. IMPORTANT
If you want to use the complete mandate, you must ensure that your JavaScript and capture contexts are compatible with the complete mandate. See [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

`Unified Checkout` with Complete Mandate {#uc-appendix-uc-auth-intro}
=====================================================================

This section contains the capture context and JavaScript examples to integrate `Unified Checkout` into your e-commerce page. You can use these examples to collect your customer's payment information and process an authorization. You must initiate a capture request to move funds and complete the transaction.
For information on the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

Example: `Unified Checkout` with Prefer Authorization {#uc-appendix-uc-auth-ex}
===============================================================================

Capture Context Request

```
{
  "targetOrigins" : [ "https://the-up-demo.appspot.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "PREFER_AUTH"

    },
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

{#uc-appendix-uc-auth-ex_codeblock_c51_vmt_gwb}
JavaScript

```
&lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer" }
    };

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);

        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
```

`Unified Checkout` with Sale {#uc-appendix-uc-sale-intro}
=========================================================

This section contains the capture context and JavaScript examples to integrate `Unified Checkout` into your e-commerce page. You can use these examples to collect your customer's payment information and process a sale.
For information on the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

Example: `Unified Checkout` with Sale {#uc-appendix-uc-sale-ex}
===============================================================

Capture Context Request

```
{
  "targetOrigins" : [ "https://the-up-demo.appspot.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "CAPTURE"

    },
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

{#uc-appendix-uc-sale-ex_codeblock_c51_vmt_gwb}
JavaScript

```
&lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer" }
    };

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);

        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
```

`Unified Checkout` with Sale and `Decision Manager` {#uc-appendix-uc-sale-dm-intro}
===================================================================================

This section contains the capture context and JavaScript examples to integrate `Unified Checkout` into your e-commerce page. You can use these examples to collect your customer's payment information and process a sale while also invoking the `Decision Manager` fraud solution. Before the sale is initiated, `Decision Manager` is invoked for fraud screening.
For information on the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

Example: `Unified Checkout` with Sale and `Decision Manager` {#uc-appendix-uc-sale-dm-ex}
=========================================================================================

Capture Context Request

```
{
  "targetOrigins" : [ "https://test.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "CAPTURE",
        "decisionManager": true
        },
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

{#uc-appendix-uc-sale-dm-ex_codeblock_c51_vmt_gwb}
JavaScript

```
&lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer" }
    };

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);

        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
```

`Unified Checkout` without Service Orchestration {#uc-appendix-uc-no-pay-orch-intro}
====================================================================================

This section contains the capture context and JavaScript examples to integrate `Unified Checkout` into your e-commerce page. You can use these examples to collect your customer's payment information. Payment processing and service orchestration are completed through the back end of the integrator.
For information on the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-setup-capture-context.md "").

Example: `Unified Checkout` without Service Orchestration {#uc-appendix-uc-no-pay-orch-ex}
==========================================================================================

Capture Context Request

```
{
  "targetOrigins" : [ "https://test.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
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
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}

```

{#uc-appendix-uc-no-pay-orch-ex_codeblock_c51_vmt_gwb}
JavaScript

```
&lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer" }
    };

    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        console.log(tt); // merchant logic for passing the Transient token to their backend for service orchestration
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }
    // Call the function
    launchCheckout();
  &lt;/script&gt;
```

Echeck Payment with a Transient Token {#uc-appendix-uc-echeck-tt-ex-intro}
==========================================================================

This section contains a request example for making a payment with an eCheck using a transient token. You must meet these requirements to make an eCheck payment with a transient token:

* The paymentType.name.value field value must be set to `CHECK` in the transient token.
* You must include the paymentInformation.paymentType.name field in your request and the value must be set to `CHECK` in your request.

Example: Echeck Payment with a Transient Token {#uc-appendix-uc-echeck-tt-ex}
=============================================================================

Echeck Payment Request with a Transient Token

```
{
  "clientReferenceInformation" : {
    "code" : "tt-1745987284021"
  },
  "orderInformation" : {
    "amountDetails" : {
      "totalAmount" : "289.99",
      "currency" : "USD"
    }
  },
  "tokenInformation" : {
    "transientTokenJwt" : "eyJraWQiOiIwODV4cWN4TWdWRldxdFdnWXBPcElCcENTRGlzb0VkcCIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzA3IiwiZXhwIjoxNzQ1OTg4MTgzLCJ0eXBlIjoiZ2RhLTAuMTAuMCIsImlhdCI6MTc0NTk4NzI4MywianRpIjoiMUUxQ0VJSFVVMDVESTlaNTJWWUw0S1hJVUtSQkJTUFUzT0JGN05aNDA4MEFTNzdCWTZVNjY4MTFBQTU3N0E0QSIsImNvbnRlbnQiOnsib3JkZXJJbmZvcm1hdGlvbiI6eyJiaWxsVG8iOnsibGFzdE5hbWUiOnt9LCJmaXJzdE5hbWUiOnt9LCJjb3VudHJ5Ijp7fSwicGhvbmVOdW1iZXIiOnt9LCJhZGRyZXNzMSI6e30sInBvc3RhbENvZGUiOnt9LCJsb2NhbGl0eSI6e30sImJ1aWxkaW5nTnVtYmVyIjp7fSwiYWRtaW5pc3RyYXRpdmVBcmVhIjp7fSwiZW1haWwiOnt9fSwiYW1vdW50RGV0YWlscyI6eyJ0b3RhbEFtb3VudCI6e30sImN1cnJlbmN5Ijp7fX0sInNoaXBUbyI6eyJsYXN0TmFtZSI6e30sImZpcnN0TmFtZSI6e30sImNvdW50cnkiOnt9LCJhZGRyZXNzMSI6e30sInBvc3RhbENvZGUiOnt9LCJsb2NhbGl0eSI6e30sImJ1aWxkaW5nTnVtYmVyIjp7fSwiYWRtaW5pc3RyYXRpdmVBcmVhIjp7fX19LCJwYXltZW50SW5mb3JtYXRpb24iOnsiYmFuayI6eyJyb3V0aW5nTnVtYmVyIjp7fSwiYWNjb3VudCI6eyJudW1iZXIiOnt9LCJ0eXBlIjp7fX19LCJwYXltZW50VHlwZSI6eyJuYW1lIjp7InZhbHVlIjoiQ0hFQ0sifX19fX0.SmkkDRm9yTYIUnL2R-HslqKQe0CCqm4HVFiGP78WQAE4mMkjwkd6Gu9_T0AvEcuBOTaYQUVofXmILvxlj2T_Yg8hD41LFBof32UlVeo8Wf0qF28cEnTnAXJExDVbxsJnJYTEH9iNwl_8_BTerNy0FzFVcQXJ55jBfdbJ0IeEuG685Wkc2U7Xw_nIgooL544qYmlTGx0Myjf3JVF4WVpM55HfebzDubvbTMMabhC9tA-pWSZOoC_YQcQaipr9gT1CEAeYA39ODQiHhS7EsPKITdTUmmkWqWuZ_HqFS8i8wvKr-HJ1CY0xAhEp7TzeLAxWixuLS00tTDKFZgx7obqA6g"
  },
  "processingInformation" : {
    "bankTransferOptions" : {
      "secCode" : "WEB"
    }
  },
  "paymentInformation" : {
    "paymentType" : {
      "name" : "CHECK"
    }
  }
}
```

{#uc-appendix-uc-echeck-tt-ex_codeblock_c51_vmt_gwb}

Example: `Unified Checkout` Complete Capture Context {#uc-appendix-uc-auth-ex}
==============================================================================

Capture Context Request

```
{
    "country": "US"
    "locale": "en_GB",
    "targetOrigins": [
        "https://merchant.com",
        "https://reseller.com:8443"
    ],
    "clientVersion": "0.34",
    "allowedCardNetworks": [
        "VISA",
        "MASTERCARD",
        "AMEX"
    ],
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
    "completeMandate": {
        "type": "PREFER_AUTH",
        "decisionManager": true,
        "consumerAuthentication": true,
        "tms": {
            "tokenCreate": true,
            "tokenTypes": [
                "customer",
                "paymentInstrument",
                "instrumentIdentifier",
                "shippingAddress"
            ]
        }
    },
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "data": {
        "orderInformation": {
            "amountDetails": {
                "totalAmount": "102.21",
                "currency": "USD",
                "surcharge": {
                    "amount": "2.50"
                },
                "discountAmount": "2.00",
                "serviceFeeAmount": "5.00",
                "taxAmount": "10.00"
            },
            "billTo": {
                "address1": "string",
                "address2": "string",
                "address3": "string",
                "address4": "string",
                "administrativeArea": "st",
                "buildingNumber": "string",
                "country": "US",
                "district": "string",
                "locality": "string",
                "postalCode": "string",
                "company": {
                    "name": "Visa Inc",
                    "address1": "900 Metro Center Blvd",
                    "address2": "address2",
                    "address3": "address3",
                    "address4": "address4",
                    "administrativeArea": "CA",
                    "buildingNumber": "1",
                    "country": "US",
                    "district": "district",
                    "locality": "Foster City",
                    "postalCode": "94404"
                },
                "email": "test@test.com",
                "firstName": "string",
                "lastName": "string",
                "middleName": "string",
                "nameSuffix": "string",
                "title": "string",
                "phoneNumber": "string",
                "phoneType": "string"
            },
            "shipTo": {
                "address1": "string",
                "address2": "string",
                "address3": "string",
                "address4": "string",
                "administrativeArea": "st",
                "buildingNumber": "string",
                "country": "US",
                "district": "string",
                "locality": "string",
                "postalCode": "string",
                "firstName": "string",
                "lastName": "string"
            },
            "lineItems": [
                {
                    "productCode": "string",
                    "productName": "string",
                    "productSku": "string",
                    "quantity": 2,
                    "unitPrice": "string",
                    "unitOfMeasure": "string",
                    "totalAmount": "string",
                    "taxAmount": "string",
                    "taxRate": "string",
                    "taxAppliedAfterDiscount": "y",
                    "taxStatusIndicator": "N",
                    "taxTypeCode": "1234",
                    "amountIncludesTax": true,
                    "typeOfSupply": "12",
                    "commodityCode": "string",
                    "discountAmount": "string",
                    "discountApplied": true,
                    "discountRate": "string",
                    "invoiceNumber": "string",
                    "taxDetails": [
                        {
                            "type": "string",
                            "amount": "string",
                            "rate": "string",
                            "code": "1234",
                            "taxId": "string",
                            "applied": true,
                            "exemptionCode": "1"
                        }
                    ],
                    "fulfillmentType": "string",
                    "weight": "string",
                    "weightIdentifier": "N",
                    "weightUnit": "mg",
                    "referenceDataCode": "string",
                    "referenceDataNumber": "string",
                    "unitTaxAmount": "string",
                    "productDescription": "string",
                    "giftCardCurrency": "USD",
                    "shippingDestinationTypes": "",
                    "gift": false,
                    "passenger": {
                        "type": "string",
                        "status": "string",
                        "phone": "string",
                        "firstName": "string",
                        "lastName": "string",
                        "id": "string",
                        "email": "string",
                        "nationality": "US"
                    }
                }
            ]
        },
        "buyerInformation": {
            "personalIdentification": {
                "cpf": "12345678900"
            },
            "merchantCustomerId": "string",
            "companyTaxId": "string"
        },
        "clientReferenceInformation": {
            "code": "TAGX001",
            "partner": {
                "developerId": "1234",
                "solutionId": "4567"
            }
        },
        "consumerAuthenticationInformation": {
            "challengeCode": "01",
            "messageCategory": "01"
        },
        "merchantInformation": {
            "merchantDescriptor": {
                "name": "Jane Sales"
            }
        },
        "processingInformation": {
            "reconciliationId": "01234567",
            "authorizationOptions": {
                "aftIndicator": true,
                "initiator": {
                    "credentialStoredOnFile": true,
                    "merchantInitiatedTransaction": {
                        "reason": "1"
                    }
                }
            },
            "businessApplicationId": "AA"
        },
        "recipientInformation": {
            "firstName": "John",
            "middleName": "A",
            "lastName": "Buyer",
            "country": "GB",
            "accountId": "acc0123567",
            "administrativeArea": "GB",
            "accountType": "01"
        },
        "merchantDefinedInformation": [
            {
                "key": "1",
                "value": "12345"
            },
            {
                "key": "2",
                "value": "67890"
            },
            {
                "key": "3",
                "value": "DISCOUNT20"
            }
        ]
    }
}
```

Supported Countries for Digital Payments {#uc-appendix-supp-countries}
======================================================================

Apple Pay, `Click to Pay`, `eCheck`, Google Pay, and Paze are supported in different countries.
See these topics for the lists of the countries that support digital payments:

* [Supported Countries for Digital Payments A-D](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-supp-countries/uc-appendix-supp-countries-a-d.md "")
* [Supported Countries for Digital Payments E-K](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-supp-countries/uc-appendix-supp-countries-e-k.md "")
* [Supported Countries for Digital Payments L-R](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-supp-countries/uc-appendix-supp-countries-l-r.md "")
* [Supported Countries for Digital Payments S-Z](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-supp-countries/uc-appendix-supp-countries-s-z.md "")

Supported Countries for Digital Payments A-D {#uc-appendix-supp-countries-a-d}
==============================================================================

|             Country              |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                            eCheck                                                            |                                                          Google Pay                                                          |
|:--------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
|           Afghanistan            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Albania              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Algeria              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Andorra              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Angola              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|       Antigua and Barbuda        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Argentina             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Armenia              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Australia             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Austria              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Azerbaijan            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bahamas              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bahrain              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Bangladesh            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Barbados             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Belarus              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Belgium              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Brazil              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Belize              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Benin               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Bhutan              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Bolivia              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|      Bosnia and Herzegovina      |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Botswana             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|        Brunei Darussalam         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bulgaria             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Burkina Faso           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Burundi              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Cambodia             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Cameroon             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Canada              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Cape Verde            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|     Central African Republic     |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|               Chad               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Chile               | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              China               | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Colombia             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Comoros              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Costa Rica            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|          Côte d'Ivoire           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Croatia              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Cyprus              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|          Czech Republic          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Democratic Republic of the Congo |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Denmark              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Djibouti             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Dominica             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|        Dominican Republic        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (A through D)]

Supported Countries for Digital Payments E-K {#uc-appendix-supp-countries-e-k}
==============================================================================

|      Country      |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                          Google Pay                                                          |
|-------------------|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| Ecuador           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Egypt             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| El Salvador       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Equatorial Guinea |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Eritrea           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Estonia           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Eswatini          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ethiopia          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Faroe Islands     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Fiji              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Finland           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| France            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gabon             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gambia            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Georgia           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Germany           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ghana             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gibraltar         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Greece            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Greenland         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Guernsey          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Grenada           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guatemala         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guinea            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guinea-Bissau     |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guyana            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Haiti             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Honduras          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Hong Kong         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Hungary           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Iceland           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Indonesia         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Iraq              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ireland           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Isle of Man       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Israel            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Italy             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Jamaica           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Japan             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Jersey            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Jordan            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kazakhstan        | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kenya             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kiribati          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kuwait            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kyrgyzstan        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (E through K)]

Supported Countries for Digital Payments L-R {#uc-appendix-supp-countries-l-r}
==============================================================================

|             Country             |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                          Google Pay                                                          |
|---------------------------------|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| Laos                            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latvia                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lebanon                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lesotho                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Liberia                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Libya                           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Liechtenstein                   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lithuania                       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Luxembourg                      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Macau                           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Madagascar                      |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malawi                          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malaysia                        | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Maldives                        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mali                            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malta                           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Marshall Islands                |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mauritania                      |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mauritius                       |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mexico                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Micronesia, Federated States of |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Moldova                         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Monaco                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mongolia                        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Montenegro                      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Morocco                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mozambique                      |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Myanmar                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Namibia                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nauru                           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nepal                           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Netherlands                     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| New Zealand                     | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nicaragua                       |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Niger                           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nigeria                         |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| North Macedonia                 |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Norway                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Oman                            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Pakistan                        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Palau                           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Palestinian Territories         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Panama                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Papua New Guinea                |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Paraguay                        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Peru                            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Philippines                     |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Poland                          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Portugal                        | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Qatar                           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Republic of the Congo           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Romania                         | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Rwanda                          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (L through R)]

Supported Countries for Digital Payments S-Z {#uc-appendix-supp-countries-s-z}
==============================================================================

|             Country              |                                                          Apple Pay                                                           |                                                        `Click to Pay`                                                        |                                                            eCheck                                                            |                                                          Google Pay                                                          |                                                             Paze                                                             |
|:--------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
|      Saint Kitts and Nevis       |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Saint Lucia            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Saint Vincent and the Grenadines |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Samoa               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            San Marino            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|      Sao Tome and Principe       |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Saudi Arabia           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Senegal              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Serbia              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Seychelles            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Sierra Leone           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Singapore             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Slovakia             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Slovenia             | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|         Solomon Islands          |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Somalia              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           South Africa           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|    Korea, Republic of (South)    | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           South Sudan            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Spain               | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Sri Lanka             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Sudan               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Suriname             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Sweden              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Switzerland            | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       Switzerland -Italian       |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Taiwan              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Tajikistan            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Tanzania             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Thailand             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Timor-Leste            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|               Togo               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Tonga               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       Trinidad and Tobago        |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Tunisia              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Turkey              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Turkmenistan           |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Tuvalu              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Uganda              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Ukraine              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       United Arab Emirates       | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|          United Kingdom          | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|          United States           | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Uruguay              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Uzbekistan            |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Vanuatu              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|     Vatican City (Holy See)      | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Venezuela             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Vietnam              | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Yemen               |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Zambia              |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Zimbabwe             |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/new-documentation/documentation/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/new-documentation/documentation/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
[Supported Countries (S through Z)]

Supported Locales {#uc-appendix-languages}
==========================================

The locale field within the capture context request consists of an ISO 639 language code, an underscore (_), and an ISO 3166 region code. The locale controls the language in which the application is rendered. The following locales are supported:

* ar_AE
* bg_BG
* ca_ES
* cs_CZ
* da_DK
* de_AT
* de_DE
* el_GR
* en_AU
* en_CA
* en_GB
* en_IE
* en_NZ
* en_PK
* en_US
* es_AR
* es_CL
* es_CO
* es_ES
* es_MX
* es_PE
* es_US
* fi_FI
* fr_CA
* fr_FR
* he_IL
* hr_HR
* hu_HU
* id_ID
* it_IT
* ja_JP
* km_KH
* ko_KR
* lo_LA
* ms_MY
* nb_NO
* nl_NL
* pl_PL
* pt_BR
* ro_RO
* ru_RU
* sk_SK
* sl_SI
* sv_SE
* th_TH
* tl_PH
* tr_TR
* ur_PK
* vi_VN
* zh_CN
* zh_HK
* zh_MO
* zh_SG
* zh_TW

Reason Codes {#uc-appendix-reason-codes}
========================================

A `Unified Checkout` request response returns one of the following reason codes:

| Reason Code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `200`       | Successful response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `201`       | Capture context created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `400`       | Bad request. Possible reason values: * `CAPTURE_CONTEXT_EXPIRED` * `CAPTURE_CONTEXT_INVALID` * `CHECKOUT_ERROR` * `CLICK_TO_PAY_SDK_LOAD_ERROR` * `COMPLETE_AUTHENTICATION_CANCELED` * `COMPLETE_AUTHENTICATION_FAILED` * `COMPLETE_ERROR` * `COMPLETE_IN_PROGRESS` * `COMPLETE_NOT_ALLOWED` * `COMPLETE_TRANSACTION_CANCELLED` * `COMPLETE_TRANSACTION_FAILED` * `COMPLETE_VALIDATION_ERROR` * `CREATE_TOKEN_TIMEOUT` * `CREATE_TOKEN_XHR_ERROR` * `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` * `GOOGLEPAY_CHECKOUT_ERROR` * `INVALID_APIKEY` * `LAUNCH_SRC_CHECKOUT_ERROR` * `SDK_XHR_ERROR` * `SHOW_LOAD_CONTAINER_SELECTOR` * `SHOW_LOAD_ERROR` * `SHOW_LOAD_INVALID_CONTAINER` * `SHOW_LOAD_SIDEBAR_OPTIONS` * `SHOW_PAYMENT_TIMEOUT` * `SHOW_PAYMENT_UNAVAILABLE` * `SHOW_TOKEN_TIMEOUT` * `SHOW_TOKEN_XHR_ERROR` * `TOKENIZATION_ERROR` * `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` * `UNIFIED_PAYMENTS_ALREADY_SHOWN` * `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS` * `UNIFIED_PAYMENTS_VALIDATION_FIELDS` * `UNIFIED_PAYMENTS_VALIDATION_PARAMS` |
| `404`       | The specified resource not found in the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `500`       | Unexpected server error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
[Reason Codes]

`Unified Checkout` Field Reference {#uc_appendix_pass_through_fields}
=====================================================================

This section includes the fields that you use for `Unified Checkout`.

Main Configuration Fields {#uc_appendix_pass_through_fields_main_fields}
------------------------------------------------------------------------

The following table describes the main configuration fields for `Unified Checkout`:

|           Field Name            | Data Type | Required? |                        Example                         |                                                                                      Details                                                                                      |
|---------------------------------|-----------|-----------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| allowedCardNetworks             | Array     | No        | `["VISA","MASTERCARD","AMEX"]`                         |                                                                                                                                                                                   |
| allowedPaymentTypes             | Array     | Yes       | `["PANENTRY","CLICKTOPAY","APPLEPAY","GOOGLEPAY"]`     | The field value can be an array of strings or an object with options.                                                                                                             |
| buttonType                      | Enum      | No        |                                                        | Possible values: * `ADD_CARD` * `SAVE_CARD` * `CARD_PAYMENT` * `CHECKOUT` * `CHECKOUT_AND_CONTINUE` * `DEBIT_CREDIT` * `DONATE` * `PAY` * `PAY_WITH_CARD` * `SUBSCRIBE_WITH_CARD` |
| clientReferenceInformation.code | String    | No        | `TAGX001`                                              |                                                                                                                                                                                   |
| clientVersion                   | String    | Yes       | `0.31`                                                 |                                                                                                                                                                                   |
| country                         | String    | Yes       | `US`                                                   |                                                                                                                                                                                   |
| locale                          | String    | Yes       | `en_US`                                                |                                                                                                                                                                                   |
| targetOrigins                   | Array     | Yes       | `["https://merchant.com","https://reseller.com:8443"]` | Each origin must contain HTTPS and include the scheme, host, and optional port.                                                                                                   |
[Main Configuration Fields]

Order Information Fields {#uc_appendix_pass_through_fields_order_information_fields}
------------------------------------------------------------------------------------

This table contains information about the data.orderInformation field object:

|                                 Field                                 |  Type   |               Required?                |      Example       |
|-----------------------------------------------------------------------|---------|----------------------------------------|--------------------|
| data.orderInformation.amountDetails.currency                          | String  | Yes                                    | `USD`              |
| data.orderInformation.amountDetails.discountAmount                    | String  | No                                     | `2.00`             |
| data.orderInformation.amountDetails.servieFeeAmount                   | String  | No                                     | `5.00`             |
| data.orderInformation.amountDetails.surcharge.amount                  | String  | No                                     | `4.50`             |
| data.orderInformation.amountDetails.taxAmount                         | String  | No                                     | `10.00`            |
| data.orderInformation.amountDetails.taxDetails\[\].taxId              | String  | No                                     | `1234`             |
| data.orderInformation.amountDetails.taxDetails\[\].type               | String  | No                                     | `N`                |
| data.orderInformation.amountDetails.totalAmount                       | String  | Yes                                    | `102.21`           |
| data.orderInformation.billTo.address1                                 | String  | Required for Afterpay                  | `1 Market St`      |
| data.orderInformation.billTo.address2                                 | String  | No                                     | `Apt B`            |
| data.orderInformation.billTo.address3                                 | String  | No                                     | `Building C`       |
| data.orderInformation.billTo.address4                                 | String  | No                                     | `Floor 2`          |
| data.orderInformation.billTo.administrativeArea                       | String  | Required for Afterpay                  | `CA`               |
| data.orderInformation.billTo.buildingNumber                           | String  | No                                     | `123`              |
| data.orderInformation.billTo.company.address1                         | String  | No                                     | `123 Street Road`  |
| data.orderInformation.billTo.company.address2                         | String  | No                                     | `Suite 100`        |
| data.orderInformation.billTo.company.address3                         | String  | No                                     | `Building A`       |
| data.orderInformation.billTo.company.address4                         | String  | No                                     | `Floor 5`          |
| data.orderInformation.billTo.company.administrativeArea               | String  | No                                     | `CA`               |
| data.orderInformation.billTo.company.buildingNumber                   | String  | No                                     | `900`              |
| data.orderInformation.billTo.company.country                          | String  | No                                     | `US`               |
| data.orderInformation.billTo.company.district                         | String  | No                                     | `Metro`            |
| data.orderInformation.billTo.company.locality                         | String  | No                                     | `Foster City`      |
| data.orderInformation.billTo.company.name                             | String  | No                                     | `Company Name`     |
| data.orderInformation.billTo.company.postalCode                       | String  | No                                     | `12345`            |
| data.orderInformation.billTo.country                                  | String  | Conditional                            | `US`               |
| data.orderInformation.billTo.district                                 | String  | No                                     | `Downtown`         |
| data.orderInformation.billTo.email                                    | String  | Required for Afterpay                  | `user@example.com` |
| data.orderInformation.billTo.firstName                                | String  | Required for Afterpay and iDEAL        | `Jane`             |
| data.orderInformation.billTo.lastName                                 | String  | Required for Afterpay and iDEAL        | `Doe`              |
| data.orderInformation.billTo.locality                                 | String  | Required for Afterpay                  | `San Francisco`    |
| data.orderInformation.billTo.middleName                               | String  | No                                     | `Michael`          |
| data.orderInformation.billTo.nameSuffix                               | String  | No                                     | `Jr.`              |
| data.orderInformation.billTo.phoneNumber                              | String  | No                                     | `111-111-1111`     |
| data.orderInformation.billTo.phoneType                                | String  | No                                     | `day`              |
| data.orderInformation.billTo.postalCode                               | String  | Required for Afterpay                  | `94105`            |
| data.orderInformation.billTo.title                                    | String  | No                                     | `Mr.`              |
| data.orderInformation.lineItems\[\].amountIncludesTax                 | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].commodityCode                     | String  | No                                     | `8471`             |
| data.orderInformation.lineItems\[\].discountAmount                    | String  | No                                     | `3.00`             |
| data.orderInformation.lineItems\[\].discountApplied                   | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].discountRate                      | String  | No                                     | `0.0500`           |
| data.orderInformation.lineItems\[\].fulfillmentType                   | String  | No                                     | `physical`         |
| data.orderInformation.lineItems\[\].gift                              | Boolean | No                                     | `false`            |
| data.orderInformation.lineItems\[\].giftCardCurrency                  | String  | No                                     | `2`                |
| data.orderInformation.lineItems\[\].invoiceDetails.productDescription | String  | No                                     | `Description`      |
| data.orderInformation.lineItems\[\].invoiceNumber                     | String  | No                                     | `INV-1001`         |
| data.orderInformation.lineItems\[\].passenger.email                   | String  | No                                     | `user@example.com` |
| data.orderInformation.lineItems\[\].passenger.firstName               | String  | No                                     | `Jane`             |
| data.orderInformation.lineItems\[\].passenger.id                      | String  | No                                     | `1234567890`       |
| data.orderInformation.lineItems\[\].passenger.lastName                | String  | No                                     | `Doe`              |
| data.orderInformation.lineItems\[\].passenger.nationality             | String  | No                                     | `US`               |
| data.orderInformation.lineItems\[\].passenger.phone                   | String  | No                                     | `111-111-1111`     |
| data.orderInformation.lineItems\[\].passenger.status                  | String  | No                                     | `standard`         |
| data.orderInformation.lineItems\[\].passenger.type                    | String  | No                                     | `ADT`              |
| data.orderInformation.lineItems\[\].productCode                       | String  | Conditional                            | `electronic_good`  |
| data.orderInformation.lineItems\[\].productDescription                | String  | No                                     | `HD Receiver`      |
| data.orderInformation.lineItems\[\].productName                       | String  | No                                     | `Receiver`         |
| data.orderInformation.lineItems\[\].productSku                        | String  | No                                     | `SKU-12345`        |
| data.orderInformation.lineItems\[\].quantity                          | String  | Conditional                            | `2`                |
| data.orderInformation.lineItems\[\].referenceDataCode                 | String  | No                                     | `REF1`             |
| data.orderInformation.lineItems\[\].referenceDataNumber               | String  | No                                     | `123`              |
| data.orderInformation.lineItems\[\].shippingDestinationTypes          | String  | No                                     | `residential`      |
| data.orderInformation.lineItems\[\].taxAmount                         | String  | No                                     | `5.40`             |
| data.orderInformation.lineItems\[\].taxAppliedAfterDiscount           | String  | No                                     | `Y`                |
| data.orderInformation.lineItems\[\].taxDetails\[\].amount             | String  | No                                     | `4.50`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].applied            | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].code               | String  | No                                     | `1234`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].exemptionCode      | String  | No                                     | `1`                |
| data.orderInformation.lineItems\[\].taxDetails\[\].rate               | String  | No                                     | `0.0750`           |
| data.orderInformation.lineItems\[\].taxDetails\[\].taxId              | String  | No                                     | `TX-123456`        |
| data.orderInformation.lineItems\[\].taxDetails\[\].type               | String  | No                                     | `STATE_SALES_TAX`  |
| data.orderInformation.lineItems\[\].taxRate                           | String  | No                                     | `0.0900`           |
| data.orderInformation.lineItems\[\].taxStatusIndicator                | String  | No                                     | `N`                |
| data.orderInformation.lineItems\[\].taxTypeCode                       | String  | No                                     | `1234`             |
| data.orderInformation.lineItems\[\].totalAmount                       | String  | Conditional                            | `59.98`            |
| data.orderInformation.lineItems\[\].typeOfSupply                      | String  | No                                     | `12`               |
| data.orderInformation.lineItems\[\].unitOfMeasure                     | String  | No                                     | `EA`               |
| data.orderInformation.lineItems\[\].unitPrice                         | String  | Required for line-item authorizations. | `29.99`            |
| data.orderInformation.lineItems\[\].unitTaxAmount                     | String  | No                                     | `1.00`             |
| data.orderInformation.lineItems\[\].weight                            | String  | No                                     | `500`              |
| data.orderInformation.lineItems\[\].weightIdentifier                  | String  | No                                     | "N"                |
| data.orderInformation.lineItems\[\].weightUnit                        | String  | No                                     | `mg`               |
| data.orderInformation.shipTo.address1                                 | String  | No                                     | `456 Nice Avenue`  |
| data.orderInformation.shipTo.address2                                 | String  | No                                     | `Unit 7`           |
| data.orderInformation.shipTo.address3                                 | String  | No                                     | `Warehouse B`      |
| data.orderInformation.shipTo.address4                                 | String  | No                                     | `Dock 3`           |
| data.orderInformation.shipTo.administrativeArea                       | String  | No                                     | `CA`               |
| data.orderInformation.shipTo.buildingNumber                           | String  | No                                     |                    |
| data.orderInformation.shipTo.country                                  | String  | No                                     | `US`               |
| data.orderInformation.shipTo.district                                 | String  | No                                     | `Midtown`          |
| data.orderInformation.shipTo.firstName                                | String  | Conditional                            | `John`             |
| data.orderInformation.shipTo.lastName                                 | String  | No                                     | `Buyer`            |
| data.orderInformation.shipTo.locality                                 | String  | No                                     | `Los Angeles`      |
| data.orderInformation.shipTo.postalCode                               | String  | No                                     | `90010`            |
[Order Information Fields]

Capture Mandate Fields {#uc_appendix_pass_through_fields_capture_mandate_fields}
--------------------------------------------------------------------------------

The following table describes the captureMandate object fields. The values in these fields determine which fields `Unified Checkout` displays in the UI:

|                  Field                  | Data Type |  Required?  |    Example    |
|-----------------------------------------|-----------|-------------|---------------|
| captureMandate.billingType              | Enum      | No          | `FULL`        |
| captureMandate.comboCard                | Boolean   | No          | `true`        |
| captureMandate.CPF.required             | Boolean   | Conditional | `true`        |
| captureMandate.requestEmail             | Boolean   | No          | `true`        |
| captureMandate.requestPhone             | Boolean   | No          | `true`        |
| captureMandate.requestSaveCard          | Boolean   | No          | `true`        |
| captureMandate.requestShipping          | Boolean   | No          | `true`        |
| captureMandate.shipToCountries          | Array     | No          | `["US","GB"]` |
| captureMandate.showAcceptedNetworkIcons | Boolean   | No          | `true`        |
| captureMandate.showConfirmationStep     | Boolean   | No          | `true`        |
[Capture Mandate Fields]

Complete Mandate Fields {#uc_appendix_pass_through_fields_complete_mandate_fields}
----------------------------------------------------------------------------------

This table contains information about the completeMandate field object:

|                 Field                  |  Type   |  Required?  |                                     Example                                     |                                                                                                      Details                                                                                                       |
|----------------------------------------|---------|-------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| completeMandate.consumerAuthentication | Boolean | Conditional | `true`                                                                          | Enable `3-D Secure` authentication for supported card types.                                                                                                                                                       |
| completeMandate.decisionManager        | Boolean | Conditional | `true`                                                                          | Enable `Decision Manager` fraud screening with device fingerprinting.                                                                                                                                              |
| completeMandate.tms.tokenCreate        | Boolean | Conditional | `true`                                                                          | Create tokens through the `Token Management Service`.                                                                                                                                                              |
| completeMandate.tms.tokenTypes         | Array   | Conditional | `["customer", "paymentInstrument", "instrumentIdentifier", "shippingAddress" ]` | Types of tokens to create: * Customer * Instrument identifier * Payment instrument * Shipping address When you do not set this field value to a token type, the default value is based on the vault configuration. |
| completeMandate.type                   | Enum    | Conditional | `CAPTURE`                                                                       | Type of transaction required.                                                                                                                                                                                      |
[Complete Mandate Fields]

Buyer Information Fields {#uc_appendix_pass_through_fields_buyer_information_fields}
------------------------------------------------------------------------------------

This table contains information about the buyerInformation field object:

|                    Field                    |  Type  |     Required?      |       Example        |
|---------------------------------------------|--------|--------------------|----------------------|
| buyerInformation.companyTaxId               | String | Regional           | `12.345.678/0001-90` |
| buyerInformation.dateOfBirth                | String | No                 | `19900101`           |
| buyerInformation.language                   | String | No                 | `en-US`              |
| buyerInformation.merchantCustomerId         | String | No                 | `cust_12345`         |
| buyerInformation.personalIdentification.cpf | String | Required in Brazil | `12345678900`        |
[Buyer Information Fields]

Client Reference Information Fields {#uc_appendix_pass_through_fields_client_reference_information_fields}
----------------------------------------------------------------------------------------------------------

This table contains information about the clientReferenceInformation field object:

|                     Field                      |  Type  | Required |  Example  |
|------------------------------------------------|--------|----------|-----------|
| clientReferenceInformation.code                | String | No       | `TAGX001` |
| clientReferenceInformation.partner.developerId | String | No       | `1234`    |
| clientReferenceInformation.partner.solutionId  | String | No       | `4567`    |
[Client Reference Information Fields]

Consumer Authentication Information Fields {#uc_appendix_pass_through_fields_consumer_authentication_fields}
------------------------------------------------------------------------------------------------------------

This table contains information about the consumerAuthenticationInformation field object. These fields are used only for `3-D Secure`:

|                       Field                       |  Type  | Required | Example |
|---------------------------------------------------|--------|----------|---------|
| consumerAuthenticationInformation.challengeCode   | String | Yes      | `01`    |
| consumerAuthenticationInformation.messageCategory | String | Yes      | `01`    |
| consumerAuthenticationInformation.acsWindowSize   | String | No       | `10`    |
[Consumer Authentication Information Fields]

Merchant Information Fields {#uc_appendix_pass_through_fields_merchant_information_fields}
------------------------------------------------------------------------------------------

The following table describes the merchantInformation.merchantDescriptor object fields:

|                           Field                           |  Type  | Required? |      Example      |
|-----------------------------------------------------------|--------|-----------|-------------------|
| merchantInformation.merchantDescriptor.address1           | String | No        | `123 Street Road` |
| merchantInformation.merchantDescriptor.administrativeArea | String | No        | `CA`              |
| merchantInformation.merchantDescriptor.alternateName      | String | No        | `Susan`           |
| merchantInformation.merchantDescriptor.country            | String | No        | `US`              |
| merchantInformation.merchantDescriptor.locality           | String | No        | `Foster City`     |
| merchantInformation.merchantDescriptor.name               | String | No        | `Jane Sales`      |
| merchantInformation.merchantDescriptor.phone              | String | No        | `111-111-1111`    |
| merchantInformation.merchantDescriptor.postalCode         | String | No        | `12345`           |
[Merchant Information Fields]

Processing Information Fields {#uc_appendix_pass_through_fields_processing_information_fields}
----------------------------------------------------------------------------------------------

This table contains information about the processingInformation field object.

|                                          Field                                           |  Type   |            Required?            |      Example      |
|------------------------------------------------------------------------------------------|---------|---------------------------------|-------------------|
| processingInformation.authorizationOptions.aftIndicator                                  | Boolean | Conditional                     | `true`            |
| processingInformation.authorizationOptions.authIndicator                                 | Enum    | No                              | `0`               |
| processingInformation.authorizationOptions.ignoreAvsResult                               | Boolean | No                              | `true`            |
| processingInformation.authorizationOptions.ignoreCvResult                                | Boolean | No                              | `true`            |
| processingInformation.authorizationOptions.initiator.credentialStoredOnFile              | Boolean | Required for stored credentials | `true`            |
| processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason | String  | Required for stored credentials | `1`               |
| processingInformation.businessApplicationId                                              | String  | Required for Payouts            | `AA`              |
| processingInformation.commerceIndicator                                                  | String  | No                              | `retail`          |
| processingInformation.processingInstruction                                              | String  | No                              | `NO_INSTRUCTION`  |
| processingInformation.reconciliationId                                                   | String  | No                              | `123456789012345` |
[Processing Information Fields]

Recipient Information Fields {#uc_appendix_pass_through_fields_recipient_information_fields}
--------------------------------------------------------------------------------------------

This table contains information about the recipientInformation field object. These fields are used only for payouts:

|                  Field                  |  Type  |  Required?  |   Example    |
|-----------------------------------------|--------|-------------|--------------|
| recipientInformation.accountId          | String | Conditional | `acc0123567` |
| recipientInformation.accountType        | String | Conditional | `01`         |
| recipientInformation.administrativeArea | String | No          | `GB`         |
| recipientInformation.country            | String | Conditional | `GB`         |
| recipientInformation.dateOfBirth        | String | No          | `19900101`   |
| recipientInformation.firstName          | String | Conditional | `John`       |
| recipientInformation.lastName           | String | Conditional | `Buyer`      |
| recipientInformation.middleName         | String | No          | `A`          |
| recipientInformation.postalCode         | String | No          | `12345`      |
[Recipient Information Fields]

Merchant Defined Information Fields
-----------------------------------

This table contains information about the merchantDefinedInformation\[\] field array:

|                Field                 |  Type  |                                   Required?                                    |    Example    |
|--------------------------------------|--------|--------------------------------------------------------------------------------|---------------|
| merchantDefinedInformation\[\].key   | String | Required when merchantDefinedInformation\[\].value is included in the request. | `customer_id` |
| merchantDefinedInformation\[\].value | String | Required when merchantDefinedInformation\[\].key is included in the request.   | `12345`       |
[Merchant Defined Information Fields]

Device Information Fields
-------------------------

This table contains information about the deviceInformation field object:

|            Field            |  Type  | Required? |
|-----------------------------|--------|-----------|
| deviceInformation.ipAddress | String | No        |
[Merchant Defined Information Fields]

Payment Information Fields {#uc_appendix_pass_through_fields_merchant_defined_information_fields}
-------------------------------------------------------------------------------------------------

This table contains information about the paymentInformation field object:

|                     Field                      | Type | Required? | Example |
|------------------------------------------------|------|-----------|---------|
| paymentInformation.card.typeSelectionIndicator | Enum | No        | `0`     |
[Merchant Defined Information Fields]

Allowed Payment Types Variations
--------------------------------

This table describes the possible values for the allowedPaymentTypes field object:

|   Payment Type    |                              Value                               |                 Additional Requirements in Capture Context                  |                                        Details                                         |
|-------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Manual card entry | `PANENTRY`                                                       |                                                                             | Basic card entry.                                                                      |
| Click to Pay      | `CLICKTOPAY` or `object { "type":"CLICKTOPAY","options":{...} }` | Include email in for autolookup.                                            | Auto‑check enrollment available is available through options.autoCheckEnrollment.      |
| Apple Pay         | `APPLEPAY`                                                       |                                                                             |                                                                                        |
| Google Pay        | `GOOGLEPAY`                                                      |                                                                             |                                                                                        |
| Paze              | `PAZE`                                                           |                                                                             |                                                                                        |
| iDEAL             | `IDEAL`                                                          | Include these fields: * billTo.firstName * billTo.lastName * billTo.country | Set the completeMandate.type field to `CAPTURE` or `PREFER_AUTH`.                      |
| Afterpay/Clearpay | `AFTERPAY`                                                       |                                                                             | Set the completeMandate.type field to `AUTH`, `CAPTURE` or `PREFER_AUTH`, as required. |
[Payment Types Variations]

Related Information {#uc_appendix_pass_through_fields_section_ybj_nzz_sxb}
--------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#uc_appendix_pass_through_fields_ul_zbj_nzz_sxb}

Test Authentication {#uc_appendix_authentication}
=================================================

Use this table to determine how to test your authentication method.

| Payment Method |                  Authentication                   |        Minimum Follow-On Actions         |                                                                                                 Prerequisites                                                                                                  |                                                                                                                 Test Cards                                                                                                                  |                                                                                                                                                                                                                                                                   Details                                                                                                                                                                                                                                                                    |
|----------------|---------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAN Entry      | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `true`.                                                           | See [Testing `Payer Authentication`](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md "") in the *`Payer Authentication` Developer Guide.*                          | When the complete mandate is not used, `Unified Checkout` does not initiate authentication and you must perform authentication within your own environment.                                                                                                                                                                                                                                                                                                                                                                                  |
| `Click to Pay` | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `true`. Authentication for `Click to Pay` must not be configured. | See [Unified Checkout Test Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-reference-test-cards/uc-reference-test-cards-uc.md "").                         | When authentication is not enabled for `Click to Pay` or `Click to Pay` is not able to perform authentication for `Click to Pay`, `Unified Checkout` performs authentication using `Payer Authentication` when the complete mandate is used with the consumerAuthentication field set to `true`.                                                                                                                                                                                                                                             |
| `Click to Pay` | Visa `Click to Pay`                               | Authorization and `Payer Authentication` | You must configure the authentication for `Click to Pay`. `Click to Pay` performs authentication only if it is a tokenized Visa card.                                                                          | See [Test Cards for Authentication by Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-reference-test-cards/uc-reference-test-cards-auth-ctp.md ""). | When authentication is enabled for `Click to Pay`, authentication is attempted for all `Click to Pay` transactions for Visa cards that are stored in `Click to Pay`. For information about setting up authentication for Visa `Click to Pay`, see [Set Up Customer Authentication for Visa Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication-steps.md ""). |
| Google Pay     | Google Pay                                        | Authorization                            | A Google device must be used with biometric authentication for Google authentication.                                                                                                                          |                                                                                                                                                                                                                                             | A user authenticates themselves on a Google device with a tokenized Google Pay credential -- the returned payload from Google will be Authenticated                                                                                                                                                                                                                                                                                                                                                                                          |
| Google Pay     | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | You must use a device, such as a web browser, that does not authenticate the cardholder as part of the authorization process.                                                                                  |                                                                                                                                                                                                                                             | Google will return an un-authenticated payload to Unified Checkout . Unified Checkout will step in and process Authentication via Payer Authentication when the Complete Mandate function is used with consumerAuthentication                                                                                                                                                                                                                                                                                                                |
[Authentication Testing by Product]

`Click to Pay` UI Guidelines {#uc_appendix_ui_ux}
=================================================

The UI that is built in `Unified Checkout` for `Click to Pay` is built based on the EMV `Click to Pay` XC Guidelines V1.1. `Unified Checkout` has simplified the integration of the UI. The only UI work that you must complete is the placement of the payment option.

> IMPORTANT
> You must include ` Click to Pay ` as one of the presented payment methods and not as a separate payment method.
> `Unified Checkout` captures all card details that are manually entered by the cardholder. This enables the cardholder to enroll in `Click to Pay` and removes the requirement for the cardholder to manually enter their card details the next time they check out.
> `Unified Checkout` provides a standard payment label in the `Unified Checkout` JavaScript that is loaded in your checkout page. One of these scenarios occurs when the cardholder selects the button:

* The cardholder is recognized.
* The cardholder is not recognized but has a `Click to Pay` account.
* The cardholder does not have a `Click to Pay` account.
  You can also trigger the `Unified Checkout` flow using a custom button. If you are using your own custom button, your payment button or widget must display the `Click to Pay` image for the cardholder. For information about a custom button, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

> IMPORTANT
> Your implementation consultant will ask you for a mock-up of your payment flow for confirmation that it is compliant with the ` Click to Pay ` UI design standards.

Recognized `Click to Pay` Customer
----------------------------------

The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#uc_appendix_ui_ux_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer
------------------------------------

When the cardholder has a `Click to Pay` account but is not on a registered device, they receive a one-time password to their registered email address and phone number to authenticate their identity before their stored `Click to Pay` credentials are shown:

#### Figure: {#uc_appendix_ui_ux_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

No `Click to Pay` Account
-------------------------

When the cardholder does not have a `Click to Pay` account, they can provide a new email address to perform a new lookup or they can choose to enter their card details manually. The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use:

#### Figure: {#uc_appendix_ui_ux_fig-ctp-no-account}

No `Click to Pay` Account UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

`Click to Pay` UI Examples {#uc-appendix-ui-ux-ex}
==================================================

This section contains UI examples of how you should display `Click to Pay` on your payment page. For information about how to display the UI, see [JavaScript API Reference](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix-js-reference.md "").

`Click to Pay` Replaces PAN Capture
-----------------------------------

`Click to Pay` is the card entry payment option within your payment page.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex1}

`Click to Pay` Replaces PAN Capture UI Example 1 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex1-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex2}

`Click to Pay` Replaces PAN Capture UI Example 2 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex2-645x375.svg/jcr:content/renditions/original) For information about how to configure this UI, see [Loading the JavaScript Library and Invoking the Accept Function](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro.md "").

`Click to Pay` as Radio Button
------------------------------

`Click to Pay` is a radio button for the card entry payment option within your payment page. When the cardholder selects this option, the `Click to Pay` payment flow is loaded.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex3}

`Click to Pay` Radio Button Example UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex3-645x375.svg/jcr:content/renditions/original)

`Click to Pay` Icon on Radio Button
-----------------------------------

You can host the radio selection option for card payment with the `Click to Pay` icon displayed on the payment label. The `Unified Checkout` flow loads when the cardholder selects this option. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex4}

`Click to Pay` Icon on Radio Button Example UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex4-645x375.svg/jcr:content/renditions/original)

Load `Click to Pay` Automatically From Trigger
----------------------------------------------

You can load the `Unified Checkout` JavaScript flow within your payment page without requiring the cardholder to select a card payment option. This example shows a recognized user payment flow where the cardholder's information is shown automatically next to the other payment methods hosted within your payment page. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex5}

`Click to Pay` Loaded Automatically From Trigger UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

Card Payment Options with `Click to Pay` in UI
----------------------------------------------

Do not present the `Unified Checkout` payment button as a separate payment method from the card payment button. If you do this, the cardholder is not prompted with their `Click to Pay` cards and must manually enter their payment details. They will also not have the option to store their card within `Click to Pay` for future use.
These examples show multiple card payment options and `Click to Pay` in a UI:

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex6}

Multiple Card Payment Options in UI Example 1 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex6-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex7}

Multiple Card Payment Options in UI Example 2 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex7-645x325.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex8}

Multiple Card Payment Options in UI Example 3 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex8-645x375.svg/jcr:content/renditions/original)

Introduction to the `Click to Pay Drop-In UI` {#ctp-intro}
==========================================================

The `Click to Pay Drop-In UI` powered by `Unified Checkout` provides an interface for easy acceptance of `Click to Pay` payments from Visa, Mastercard, and American Express cards. The `Click to Pay Drop-In UI` handles manual card entry for the non-`Click to Pay` payment schemes called out in this guide. Throughout this guide we refer to both *`Click to Pay Drop-In UI`* and *`Unified Checkout`.*
`Click to Pay Drop-In UI` consists of a server-side component and a client-side JavaScript library.
The server-side component authenticates your merchant identity and instructs the system to act within your payment environment. The response contains limited-use public keys. The keys are used for end-to-end encryption and contain merchant-specific payment information that drives the interaction of the application. The client-side JavaScript library dynamically and securely places digital payment options into your e-commerce page.
The provided JavaScript library enables you to place a payment application within your e-commerce environment. This embedded component offers `Click to Pay` and card entry to your customers.
Whether a customer uses a stored `Click to Pay` card or enters their payment information manually, the `Click to Pay Drop-In UI` handles all user interactions and provides a response to your e-commerce system. All UI / UX must follow the UI/UX guidelines. For information about configuring your UI/UX, see [Click to Pay UI Examples](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-ui-ux/uc-appendix-ui-ux-ex.md "").
The `Click to Pay Drop-In UI` enables a portfolio to receive an encrypted payload and send a request to the API to retrieve the payment details. The format of the decrypted payment details are determined by the transaction type. The details are either a network token and cryptogram or the PAN, expiration details, and card verification value (CVV).
The figure below shows the `Click to Pay Drop-In UI` for a recognized user.

#### Figure: {#ctp-intro_fig1}

Embedded Component
![Example of the payment application with Click to Pay.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-mobile-ui-400x475.svg/jcr:content/renditions/original)

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Firefox 121
* GoogleChrome/Chium‑based browsers 118
* MicrosoftEdge 118
* Safari16

`Click to Pay` Customer Workflows {#ctp-walkthrough-intro}
==========================================================

This section provides an overview of the `Click to Pay Drop-In UI` user experience. The `Click to Pay Drop-In UI` is designed to provide customers with a friction-free payment experience across many payment experiences. The user experience has been optimized for mobile use and performs equally well on mobile and desktop devices. `Click to Pay` recognizes customers as follows:
* The customer is a recognized `Click to Pay` customer.

* The customer is not recognized but is a `Click to Pay` customer.

* The customer is a guest at checkout.
  These workflows show you the pages a customer encounters based on their status:

* [Recognized Click to Pay Customer](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-recognized.md "")

* [Unrecognized Click to Pay Customer](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-unrecognized.md "")

* [Guest Customer](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-guest.md "")

Recognized `Click to Pay` Customer {#ctp-walkthrough-recognized}
================================================================

This section provides an overview of the `Click to Pay Drop-In UI` recognized experience. This interaction occurs when a customer's device is recognized by the `Click to Pay Drop-In UI`.
A customer's device is recognized under these conditions:

* When the customer has used `Click to Pay` on their device through any `Click to Pay` channel.
* If the customer chose to have their device remembered during a previous transaction or when they enter their one-time password (OTP).
  The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#ctp-walkthrough-recognized_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer {#ctp-walkthrough-unrecognized}
====================================================================

This section provides an overview of the `Click to Pay Drop-In UI` unrecognized experience. This interaction occurs when a customer's device is not recognized by the `Click to Pay Drop-In UI`. This condition occurs when the customer has a `Click to Pay` account but has not opted to have their details stored on the device. In this flow, the customer receives an OTP on their registered mobile device or their email address.
When the cardholder has a `Click to Pay` account but is not on a registered device, they receive a one-time password to their registered email address and phone number to authenticate their identity before their stored `Click to Pay` credentials are shown:

#### Figure: {#ctp-walkthrough-unrecognized_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

Guest Customer {#ctp-walkthrough-guest}
=======================================

This section provides an overview of the `Click to Pay Drop-In UI` guest experience. This interaction occurs when the customer has not created a `Click to Pay` account, or their issuer has not provisioned their card into `Click to Pay`.
In the guest experience, `Click to Pay Drop-In UI` captures the PAN details and the cardholder chooses to create a `Click to Pay` account or to check out as a guest. In both cases, the payment credentials are available for processing transactions using your payment gateway.
When the cardholder does not have a `Click to Pay` account, they can provide a new email address to perform a new lookup or they can choose to enter their card details manually. The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use:

#### Figure: {#ctp-walkthrough-guest_fig-ctp-no-account}

Guest UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

`Click to Pay Drop-In UI` Flow {#ctp_uc_getting_started_integration_flow}
=========================================================================

To integrate the `Click to Pay Drop-In UI` into your platform, you must follow several integration steps. This section gives a high-level overview of how to integrate and launch `Click to Pay Drop-In UI` on your webpage and process a transaction. You can find the detailed specifications of the APIs later in this document.

1. You send a server-to-server API request for a capture context. This request is fully authenticated and returns a JSON Web Token (JWT) that is necessary to invoke the frontend JavaScript library. For information on setting up the server side, see [Server-Side Set Up](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-ss-setup.md "").
2. You invoke the `Unified Checkout` JavaScript library using the JWT response from the capture context request. For information on setting up the client side, see [Client-Side Set Up](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-getting-started-cs-setup-intro.md "").
3. You use the response from the `Click to Pay Drop-In UI` to retrieve payment credentials for payment processing or other steps.
   This figure illustrates the system's payment flow.

#### Figure: {#ctp_uc_getting_started_integration_flow_fig_uc-payment-flow}

`Click to Pay` Payment Flow
![Diagram that shows the sequence and flow of a Click to Pay payment.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-sequence-diagram.svg/jcr:content/renditions/original)
For more information on the specific APIs referenced, see these topics:

* [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "")
* [Payment Details API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-token-get-pymnt-details.md "")
* [Payment Credentials API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-token-get-pymnt-credentials.md "")

Enabling `Click to Pay` in the `Business Center` {#ctp-uc-enabling-ebc}
=======================================================================

To begin using the `Click to Pay Drop-In UI` powered by `Unified Checkout`, you must first ensure that your merchant ID (MID) is configured to use the service and that `Click to Pay` is properly set up.

1. Log in to the `Business Center`:
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `
   Production URL: ` `<https://businesscenter.cybersource.com>` `
2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout.
3. Click **Setup** and follow the instructions to enroll your business in `Click to Pay`. When `Click to Pay` is enabled, it appears on the payment configuration page.
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original)
4. Click **Manage** to alter your `Click to Pay` enrollment details. For more information on registering for `Click to Pay`, see [Enable Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/ctp-enable-digital-pay-intro.md "").
   After you enable `Click to Pay`, you can enable authentication. For information about enabling authentication for `Click to Pay` in the `Business Center`, see [Set Up Customer Authentication for Visa Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/ctp-authentication/ctp-authentication-steps.md "").

Server-Side Set Up {#ctp-getting-started-ss-setup}
==================================================

This section contains the information you need to set up your server. Initializing `Click to Pay Drop-In UI` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how the `Click to Pay Drop-In UI` performs.
The server-side component provides this information:

* A transaction-specific public key that is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and interaction methods.

{#ctp-getting-started-ss-setup_ul_atq_bwq_npb}
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Capture Context {#ctp-capture-context-intro}
============================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how `Unified Checkout` performs.
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types. The capture context request includes these elements:
* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigin
  Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context. For example:

```
{
  "targetOrigins": [
    "https://test.com"
  ],
  "clientVersion": "0.34",
  "buttonType": "CHECKOUT_AND_CONTINUE",
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
        "totalAmount": "1.01",
        "currency": "USD"
      }
    }
  }
}
```

Card Entry Form {#ctp-capture-context-intro_uc-capture-context-diagram}
-----------------------------------------------------------------------

This diagram shows how elements of the capture context request appear in the card entry form.

#### Figure:

Anatomy of a Manual Card Entry Form ![Image of the capture context request code and how it appears in the entry form
elements.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/anatomy-of-manual-card-entry-form-685x575.svg/jcr:content/renditions/original) For more information on requesting the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "").

Client-Side Set Up {#ctp-getting-started-cs-setup-intro}
========================================================

This section contains the information you need to set up the client side. You use the `Unified Checkout` JavaScript library to integrate with your e-commerce website. It has two primary components:

* The button widget, which lists the payment methods available to the customer.
* The payment acceptance page, which captures payment information from the cardholder. You can integrate the payment acceptance page with your webpage or add it as a sidebar.

The `Unified Checkout` JavaScript library supports `Click to Pay` and manual card entry payment methods.
Follow these steps to set up the client:

1. Load the JavaScript library.
2. Initialize the accept object the capture context JWT. For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
3. Initialize the unified payment object with optional parameters.
4. Show the button list or payment acceptance page or both.

{#ctp-getting-started-cs-setup-intro_ul_m5t_gwq_npb}
The response to these interactions is a transient token that you use to retrieve the payment information captured by the UI.

Loading the JavaScript Library and Invoking the Accept Function {#ctp-getting-started-cs-js-library-intro}
==========================================================================================================

Use the client library asset path and client library integrity value that is returned by the capture context response to invoke `Unified Checkout` on your page.
You can retrieve these values from the clientLibrary and clientLibraryIntegrity fields that are returned in the JWT from `https://apitest.cybersource.com``/up/v1/capture-contexts`. You can use these values to create your script tags.
You must perform this process for each transaction, as these values may be unique for each transaction. You must avoid hard-coding values for the clientLibrary and clientLibraryIntegrity fields to prevent client-side errors.
For example, a response from `https://apitest.cybersource.com``/up/v1/capture-contexts` would include:

```
"data": {
    "clientLibrary":"[EXTRACT clientLibrary VALUE from here]",
    "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]"
}
```

Below is an example script tag:

```
&lt;script src="[INSERT clientLibrary VALUE HERE]"
    integrity=”[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous”&gt;&lt;/script&gt;
```

> IMPORTANT
> Use the clientLibrary and clientLibraryIntegrity parameter values in the capture context response to obtain the ` Unified Checkout ` JavaScript library URL and the integrity value. This ensures that you are always using the most up-to-date library and protects against fraud. Do not hard-code the ` Unified Checkout ` JavaScript library URL or integrity value.
> When you load the library, the capture context from your initial server-side request is used to invoke the accept function.

JavaScript Example: Initializing the SDK {#ctp-getting-started-cs-js-library-example}
=====================================================================================

```
try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);


      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
```

In this example, `captureContext` refers to the capture context JWT.

JavaScript Example: Displaying the Button List {#ctp-getting-started-cs-js-button-example}
==========================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the embedded `Unified Checkout` tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named components that are replaced with `Unified Checkout`'s iframes.

```
try {
    const accept = await Accept(captureContext);
    const up = await accept.unifiedPayments(sidebar);
    const tt = await up.show(showArgs);
} catch (error) {
    // merchant logic for handling issues
    console.error("something went wrong: " + error);
}
```

To display the `Unified Checkout` Button List within your payment page, a call is made to the unifiedPayments.Show() function. This function accepts a JSON object that links the `&lt;div&gt;` tags within your payment page to place the `Unified Checkout` button list and optional embeddable payment page.

```
const showArgs = {
    containers: {
        paymentSelection: '#buttonPaymentListContainer',
        paymentScreen: '#embeddedPaymentContainer'
    }
};
```

The response to the unifiedPayment.show() method is a JWT data object referred to here as a transient token. The transient token contains all the payment information captured during the `Unified Checkout` payment journey.

JavaScript Example: Client-Defined Trigger for `Click to Pay` or PAN Entry {#ctp-getting-started-cs-js-trigger-ctp-pan-example}
===============================================================================================================================

When you display `CLICKTOPAY` or `PANENTRY` as allowed payment types, you can load the UI without displaying the `Unified Checkout` checkout button. You can do this by creating a trigger that defines what event loads the UI.
You can create a trigger by calling the `createTrigger()` method on an existing unified payments object and pass in these two parameters:

* The payment method that the trigger is linked to. This is required.
* The container for the payment screen. It is required when you are in embedded mode. IMPORTANT

  > You can create a trigger only for ` CLICKTOPAY ` or ` PANENTRY ` payment methods.

```
// Example: Basic usage with full sidebar experience
// Create a trigger
const trigger = up.createTrigger("CLICKTOPAY");

// Show the trigger
// In this example, when a button in your UI is clicked
const myButton = document.getElementById("myButton");

myButton.addEventListener("click", async () =&gt; {
  const transientToken = await trigger.show();
  console.log(transientToken);
})
```

```
// Example: Payment screen in a container
// Define the container for the payment screen to be rendered in
var options = { containers: { paymentScreen: '#paymentScreenContainer' } };
// Create the trigger
const trigger = up.createTrigger("CLICKTOPAY", options);

// Show the trigger
// In this example, when a button in your UI is clicked
const myButton = document.getElementById("myButton");

myButton.addEventListener("click", async () =&gt; {
  const transientToken = await trigger.show();
  console.log(transientToken);
})
```

> IMPORTANT
> When you use the ` createTrigger() ` method for ` Click to Pay `, you must create a custom UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-ui-screens.md "").

Adding the Payment Application and Payment Acceptance {#ctp-getting-started-button-widget-intro}
================================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the `Unified Checkout` embedded tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named `&lt;div&gt;` components that are replaced with `Click to Pay Drop-In UI` `iframes`.
IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the sidebar.

JavaScript Example: Setting Up with Full Sidebar {#ctp-getting-started-button-widget-sidebar}
=============================================================================================

```
var authForm = document.getElementById("authForm");
var transientToken = document.getElementById("transientToken");

var cc = document.getElementById("captureContext").value;
var showArgs = {
    containers: {
        paymentSelection: "#buttonPaymentListContainer"
    }
};
Accept(cc)
    .then(function(accept) {
        return accept.unifiedPayments();
    })
    .then(function(up) {
        return up.show(showArgs);
    })
    .then(function(tt) {
        transientToken.value = tt;
        authForm.submit();
    });
```

JavaScript Example: Setting Up with the Embedded Component {#ctp-getting-started-button-widget-embedded}
========================================================================================================

The main difference between using an embedded component and the sidebar is that the accept.unifiedPayments object is set to `false`, and the location of the payment screen is passed in the containers argument.

> IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the side bar.

```
var authForm = document.getElementById("authForm");
var transientToken = document.getElementById("transientToken");

var cc = document.getElementById("captureContext").value;
var showArgs = {
    containers: {
        paymentSelection: "#buttonPaymentListContainer",
        paymentScreen: "#embeddedPaymentContainer"
    }
};
Accept(cc)
    .then(function(accept) {
        // Gets the UC instance (e.g. what card brands I requested, any address information I pre-filled etc.)
        return accept.unifiedPayments();
    })
    .then(function(up) {
        // Display the UC instance
        return up.show(showArgs);
    })
    .then(function(tt) {
        // Return transient token from UC's UI to our app
        transientToken.value = tt;
        authForm.submit();
    }).catch(function(error) {
        //merchant logic for handling issues
        alert("something went wrong");
    });
```

Capture Context API {#ctp_setup_capture_context}
================================================

This section contains the information you need to request the capture context using the capture context API. The capture context request contains all of the merchant-specific parameters that tell the frontend JavaScript library how to behave within your payment experience.
The capture context is a signed JSON Web Token (JWT) containing this information:

* Merchant-specific parameters that dictate the customer payment experience for the current payment transaction.
* A one-time public key that secures the information flow during the current payment transaction.

The capture context request includes these elements:

* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigins
  For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Target Origin
:
The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain) and port number (if used).

    You must use the https:// protocol. Sub domains must also be included in the target origin.

    Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.

    For example, if you are launching `Click to Pay` on example.com, the target origin could be any of the following:

    * [https://example.com](https://example.com/ "")
    * [https://subdomain.example.com](https://subdomain.example.com/ "")
    * [https://example.com:8080](https://example.com:8080/ "")


    You can define the payment cards and digital payments that you want to accept in the capture context.

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
    * JCrew
    * KCP
    * mada
    * Maestro
    * Mastercard
    * Meeza
    * PayPak
    * UATP
    * Visa

    To support dual-branded or co-badged cards, you must list your supported card types values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Visa and EFTPOS and EFTPOS is listed first, the card type is set to EFTPOS after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-tokens-intro/dual-co-brand-card-support.md "").

    When a Cartes Bancaires dual-branded card is entered in the `Click to Pay Drop-In UI`, the `Click to Pay Drop-In UI` provides a radio selector button to enable the cardholder to select which scheme they want to use to process the payment. The radio selector defaults to the card scheme that appears first in the allowedCardNetworks field.

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
    > When you include ` CLICKTOPAY `, ` PANENTRY ` XXX.

> IMPORTANT
> When integrating with ` Cybersource ` APIs, ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for. Additional fields may be added in the future.
> You must ensure that your integration can handle new fields that are returned in the response. While the underlying data structures will not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Features {#uc-capture-context-features}
=======================================

This section includes information on the features that are supported in `Click to Pay`.

Save Card
:
This feature enables you to display an option in the `Unified Checkout` UI for the cardholder to save their payment details for future use. IMPORTANT
> This feature is available only for card credentials that are manually entered during checkout. If ` Click to Pay ` is an available payment method, do **not** select *Save this card with ` Click to Pay `*.

    When the customer selects the checkbox and finalizes their purchase, you receive a notification in the transient token response to your capture context request. The transient token payload includes the consumerPreference.saveCard field value set to `true` when the cardholder selects the option to save their card:

    ```
    "captureMandate": {
        "requestSaveCard": true
      }
    ```

Email Autolookup
:
Automatic email lookup occurs when an email address is included in the capture context request. If the user has a `Click to Pay` account but is not on a recognized device, a one-time password (OTP) screen appears and the user is prompted to enter their OTP. If the user does not have a `Click to Pay` account, the user must enter their card information manually and they will have the option to create a `Click to Pay` account.
To enable email autolookup, you must include `CLICKTOPAY` as a value in the allowedPaymentTypes field and include an email address in the capture context.

Mobile as Identity for `Click to Pay`
:
`Click to Pay` supports mobile numbers as way to identify a user. This enables cardholders to use their mobile number instead of their email address in certain markets for Visa and Mastercard transactions.
:
When the requestEmail field is set to `false` and the requestPhone field is set to `true`, the cardholder is identified using the provided mobile number. When the requestEmail field is set to `true` and the requestPhone field is set to `false`, the cardholder is identified using the provided email address. When the requestEmail field is set to `true` and the requestPhone field is also set to `true`, the cardholder is identified using the provided email address first and then the mobile number if there is no match.

Removal of Confirm and Continue Screen
:
When showConfirmstionStep is set to `false`, you can remove the final summary confirmation screens from the checkout experience. When the UI displays cardholder data, the cardholder can review and, if necessary, edit their payment details before checkout is complete.

    ```
    {
      "captureMandate": {
        "showConfirmationStep": false
      }
    }
    ```

`Click to Pay` Enrollment Pre-Check
:
You can have the `Click to Pay` box pre-checked when a user is manually entering their card details and `Click to Pay` is enabled. The customer can uncheck the box if necessary, which means the request is processed as a one-time manual PAN transaction. This is available when you set the billingType field to `PARTIAL` or `FULL` in the capture context. This ensures that the customer's billing country can be validated in the UI.
:
`Click to Pay` enrollment pre-check is available in these countries:

    * Argentina
    * Brazil
    * Chile
    * Colombia
    * Kuwait
    * Mexico
    * Peru
    * Qatar
    * Saudi Arabia
    * South Africa
    * Ukraine
    * United Arab Emirates

    ```
    {
      "allowedPaymentTypes": [
        "PANENTRY",
        "GOOGLEPAY",
        {
          "type": "CLICKTOPAY",
          "options": {
            "autoCheckEnrollment": true
          }
        },
        "APPLEPAY",
        "PAZE"
      ]
    }
    ```

Checkout Button Name
:
When `Click to Pay Drop-In UI` loads, the payment buttons displayed are based on what you include in the allowedPaymentTypes object in the capture context. You can customize the text on the payment buttons by setting the buttonType field object in the capture context to one of these values:

    * `ADD_CARD`
    * `CARD_PAYMENT`
    * `CHECKOUT_AND_CONTINUE`
    * `DEBIT_CREDIT`
    * `DONATE`
    * `PAY`
    * `PAY_WITH_CARD`
    * `SUBSCRIBE_WITH_CARD`

:
If you do not include the buttonType field in your request, the payment button text defaults to **Checkout with card**. For example:

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-300x100.svg/jcr:content/renditions/original)
\]

Features Available in Brazil
----------------------------

These features are available only in Brazil:

Combo Cards
:
A combo card is a single card that functions as both a debit and a credit card. `Click to Pay` enables the cardholder to choose whether to pay for a transaction using a debit or credit card. The cardholder can select the card type that they want to use when checking out with Visa cards. While in the card details section of the payment form, the cardholder is prompted to decide if they would like to pay using a debit or credit card. Credit is selected as the default option.
> IMPORTANT Combo cards are applicable only for issuers that are located in Brazil.

    To enable combo cards during checkout, you must include the comboCard field in your capture context request and set the field value to `true`:

    ```
    "captureMandate": {
        "comboCard": true
      }
    ```

    When the comboCard field value is set to `true`, the option to use a debit or credit card appears for all Visa cards that are entered in `Click to Pay` and for all cards that are already stored in `Click to Pay`. If you do not want to offer combo card at checkout, do not include the comboCard field in your capture context request.

Cadastro de Pessoas Físicas (CPF) -- Brazilian Tax ID
:
The tax ID feature is for customers in Brazil and provides your customers with a way to include their Consumer National Identifier when it is requested at checkout. Include this field in the capture context to display this field within the flow for manual card entry and `Click to Pay` transactions:

    ```
    "captureMandate" : {
        "CPF": {
            "required": true
        }
    }
    ```


    > IMPORTANT This feature is required for customers in Brazil.

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

0.28
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
Support for Pakistan locales (en_PK and ur_PK).
:
New look and feel of `Unified Checkout` in line with EMVCO best practices.

0.31
:
Addition of the data object of the orderInformation field object and pass-through fields.
:
Support for Jaywan as an allowedCardNetwork.
:
Updated the payment details response to return detected card types. Multiple card types are shown when more than one card type is detected.

0.32
:
Support for KCP and UATP in the allowedCardNetwork field.
:
A radio button in the UI for Cartes Bancaires dual-branded cards.

0.33
:
Support for Mobile as Identity `Click to Pay` lookup.

0.34
:
Additional BIN range for Jaywan card types.

Requesting the Capture Context {#uc-setup-capture-context-intro}
================================================================

This section shows you how to request the capture context.

Endpoint {#uc-setup-capture-context-intro_d33e1017}
---------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d33e1024}
**Test:** `POST ``https://apitest.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d33e1034}
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d33e1043}
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/up/v1/capture-contexts`{#uc-setup-capture-context-intro_d33e1052}

Required Fields for Requesting the Capture Context {#uc-setup-capture-context-req-fields}
=========================================================================================

Use these required fields to request the capture context:

Required Fields for Requesting the Capture Context {#uc-setup-capture-context-req-fields_req-fields-uc-capture-ctx}
-------------------------------------------------------------------------------------------------------------------

Your capture context request must include these fields:

[allowedPaymentTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/allowed-payment-types.md "")
:
Set to `CLICKTOPAY`.

[clientVersion](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-version.md "")
:

[country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/country.md "")
:

[data.orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[data.orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[locale](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/locale.md "")
:

[targetOrigins](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/target-origins.md "")
:
The URL in this field value must contain `https`.

Related Information {#uc-setup-capture-context-req-fields_section_ybj_nzz_sxb}
------------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#uc-setup-capture-context-req-fields_ul_zbj_nzz_sxb}

REST Example: Requesting the Capture Context {#ctp-setup-capture-context-example}
=================================================================================

Request

```
{
  {
    "targetOrigins": [
      "https://unified-payments.appspot.com"
    ],
    "clientVersion": "0.34",
    "allowedCardNetworks" : [ "VISA", "MASTERCARD", "AMEX" ],
    "allowedPaymentTypes" : [ "CLICKTOPAY" ],
    "country": "US",
    "locale": "en_US",
    "captureMandate": {
      "billingType": "FULL",
      "requestEmail": true,
      "requestPhone": true,
      "requestShipping": true,
      "shipToCountries": [
        "US",
        "UK"
      ],
      "showAcceptedNetworkIcons": true
    },
    "orderInformation": {
      "amountDetails": {
        "totalAmount": "21.00",
        "currency": "USD"
      },
      "billTo": {
        "address1": "1111 Park Street",
        "address2": "Apartment 24B",
        "administrativeArea": "NY",
        "country": "US",
        "district": "district",
        "locality": "New York",
        "postalCode": "00000",
        "company": {
          "name": "Visa Inc",
          "address1": "900 Metro Center Blvd",
          "administrativeArea": "CA",
          "buildingNumber": "1",
          "country": "US",
          "district": "district",
          "locality": "Foster City",
          "postalCode": "94404"
        },
        "email": "maya.tran@company.com",
        "firstName": "Maya",
        "lastName": "Tran",
        "middleName": "S",
        "title": "Ms",
        "phoneNumber": "1234567890",
        "phoneType": "phoneType"
      },
      "shipTo": {
        "address1": "Visa",
        "address2": "123 Main Street",
        "address3": "Apartment 102",
        "administrativeArea": "CA",
        "buildingNumber": "string",
        "country": "US",
        "locality": "Springfield",
        "postalCode": "99999",
        "firstName": "Joe",
        "lastName": "Soap"
      }
    }
  }
}
```

Successful Encrypted JWT Response to Request
eyJraWQiOiJ6dSIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImNvbXBsZXRlUGF0aCI6Ii9mbGV4L3YyL2NvbXBsZXRlIiwiZGF0YSI6Im4xWnFrVXFNaTJSTjVjVXJBTmp1aUJBQUVLVTY0blNKSjFDRDdBaDFvbW9nVFFTWk4zVE1uLzVpc201WEN6TTlzMitVcUdkaERCSCtEMmNPY3A2TmgyZmNRa0NnUUUzT3dicXJFdUpxdHBCZ2ZSU1h0aXI0Z0RUY0dEMHhCcndGNmdDN1plbk8zS2s3NUw3ZG1hZ2VkNm9hQ09mVkVwSThhYnZRWTRBcDdvTGdKdEpOYnViNFU2M3hzZ3B3NWdHbXhEY1ZyanlmN0FqeitvdFRLUU1UcHpnT1ByTVhxaitPbHV6VERZSTltbFdEQi9pRjlaNUF6SGZoOHdtWm9vVHBIb1ZxT1hZY1NJa1JIRWNqemZBQ2c5WFUrZ1lrTlE1MjlaOWhEemtvZ2RvMmxkNFx1MDAzZCIsIm9yaWdpbiI6Imh0dHBzOi8vdGVzdGZsZXguY3liZXJzb3VyY2UuY29tIiwidHJhbnNpZW50VG9rZW5PcGVyYXRpb25zIjpbeyJzdWIiOiIwNDA0X3Rlc3RjdHBkaXVpMDAxIiwiYXVkIjoibmFfcGFydG5lcl9jdHAyIiwia2lkIjoiMTE3ZjY5ZWMtYTA1ZS00MDM0LThhNzAtYWNjMWViOGM5ZThiIiwidHlwZSI6IlNUT1JFIn1dLCJjb21wbGV0ZVVybCI6Imh0dHBzOi8vdGVzdGZsZXguY3liZXJzb3VyY2UuY29tL2ZsZXgvdjIvY29tcGxldGUiLCJhdXRoZW50aWNhdGlvblNldHVwUGF0aCI6Ii9mbGV4L3YyL2V4dGVybmFsLXNlc3Npb25zL3NjYSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJwbFc2THMxa2oyXzdJM096Y3l6YXZoblpJUUhrUDFhMU10Um1nYUswSm1yaUlRUkFBdzhRMUlQV2xTQTI0Y2s0VGxBY2JVeW5nRzJTeWJmc3o4NDZfWlVMb19PZzBwaVlvazhOVl9uMEVPNHFtMDhtblNFMzZJRGdweldSa3E0QkFHMmpqY3cyclNzbHAwY05TQmxLb1B1ZDZSYUsxSUJHNGVMN3hFTmVvR0VZTzByZ0NyZFUtWHlTTGZxYlZaNkNiODNLZFFxeXI3VUZFa0FWc0xETkpKSU1yTnB0SGtmZ0xFejlIV1FmRkNHZUYzWVRBNGc1Ri1DLXNraHJNNkRSMDZKdENiOUFsZzljRVlpNklhTHJPYmNMXzlvLU95bG5xclBSeld6WHA3RnI4WGNUVmgyNkx0S3BzRDZGQUliUVdBaGNkYklwTGJoMktzRy03VjBBcXciLCJraWQiOiIwODM2TExkMnZFRDNWWE5jNlFWUmJXNVk5TlM3a2RPayJ9fSwiY3R4IjpbeyJkYXRhIjp7ImFsbG93ZWRQYXltZW50VHlwZXMiOlsiQ0xJQ0tUT1BBWSIsIlBBTkVOVFJZIl0sInBheW1lbnRDb25maWd1cmF0aW9ucyI6eyJTUkNWSVNBIjp7Im9yaWdpbiI6Imh0dHBzOi8vc2FuZGJveC1hc3NldHMuc2VjdXJlLmNoZWNrb3V0LnZpc2EuY29tIiwicGF0aCI6Ii9jaGVja291dC13aWRnZXQvcmVzb3VyY2VzL2pzL3NyYy1pLWFkYXB0ZXIvdmlzYVNkay5qcz92MiIsInBhbkVuY3J5cHRpb25LZXkiOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJraWQiOiJXMFBaOFZYVVZFQlU5NUpPNlpEWTEzc3E1Si1keFRuNTZmSWJEWDZObWMzWmo5V3FjIiwibiI6InNaUEl1c0RmN3lRbm5oQmtVOW11MTRWT08zQ3J1aTNiN3JBZjJLWWVvYlVSbVhBMTdiMUpYOWpnMENkLXZncG11eVRyeEJVU2MtNGIwLVVQZ1N3R0ZxUFdVcHgwOEV4cXJ3UERPdkZvakJvdTJ3bHlxOGJjeTBVcy1CZmVDelNFNWxNVmRTWFRYWFhjTnF1LXFiMjJqQ0NDSkFMcHhzQXJzYm9NT1hzTGVkaDNNNFhOUTVYR0F0UmY3Yi0tdVRZNURyOUtMWXlVdlpLQW5ZMDRNS0pQRU81NFlpSUZNNURUQWhOT21zMDg5amRNZHgtVVJJS0pqUFUyLVJwSEcxdThMQ0cwMjhSVElwUHNOYlJhbnVTNVRBWV96bHhEZ2IxaEtKMzZZYlpFTkhMZzlQWFRCaGRPTWxVOTBEVExsZmNiTFRhLUQ3RGdsakFhV0N1dnpMUGFHdyJ9LCJwYXJhbWV0ZXJzIjp7InNyY0luaXRpYXRvcklkIjoiSkZDWjhRVk9KQTc2TlhaNjhGWkQyMVJZSXhqM3lQWmRpVXhrZE51aWJCbHhnd2FQNCIsInNyY2lEcGFJZCI6Ijc3NWIyMWYyLTRkMDMtNGM1MC1iY2JiLWIyNjQ0ZGFhZWY2NSIsInNyY2lUcmFuc2FjdGlvbklkIjoiMDRlYTNhMjctZmI3OS00YjBiLWFiOTUtZmVhNzdkMDY3MDZmIiwiZHBhVHJhbnNhY3Rpb25PcHRpb25zIjp7ImRwYUxvY2FsZSI6ImVuX1VTIiwicGF5bG9hZFR5cGVJbmRpY2F0b3IiOiJGVUxMIiwicmV2aWV3QWN0aW9uIjoiY29udGludWUiLCJkcGFBY2NlcHRlZEJpbGxpbmdDb3VudHJpZXMiOltdLCJkcGFBY2NlcHRlZFNoaXBwaW5nQ291bnRyaWVzIjpbIlVTIiwiR0IiXSwiZHBhQmlsbGluZ1ByZWZlcmVuY2UiOiJBTEwiLCJkcGFTaGlwcGluZ1ByZWZlcmVuY2UiOiJBTEwiLCJjb25zdW1lck5hbWVSZXF1ZXN0ZWQiOnRydWUsImNvbnN1bWVyRW1haWxBZGRyZXNzUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lclBob25lTnVtYmVyUmVxdWVzdGVkIjp0cnVlLCJtZXJjaGFudENvdW50cnlDb2RlIjoiVVMiLCJjdXN0b21JbnB1dERhdGEiOnsiY2hlY2tvdXRPcmNoZXN0cmF0b3IiOiJtZXJjaGFudCJ9LCJ0cmFuc2FjdGlvbkFtb3VudCI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6IjIxLjAwIiwidHJhbnNhY3Rpb25DdXJyZW5jeUNvZGUiOiJVU0QifSwicGF5bWVudE9wdGlvbnMiOnsiZHBhRHluYW1pY0RhdGFUdGxNaW51dGVzIjoxNSwiZHBhUGFuUmVxdWVzdGVkIjpmYWxzZSwiZHluYW1pY0RhdGFUeXBlIjoiQ0FSRF9BUFBMSUNBVElPTl9DUllQVE9HUkFNX0xPTkdfRk9STSJ9fX0sImNoZWNrb3V0UGFyYW1ldGVycyI6eyJkcGFUcmFuc2FjdGlvbk9wdGlvbnMiOnsidHJhbnNhY3Rpb25BbW91bnQiOnsidHJhbnNhY3Rpb25BbW91bnQiOiIyMS4wMCIsInRyYW5zYWN0aW9uQ3VycmVuY3lDb2RlIjoiVVNEIn0sImFjcXVpcmVyTWVyY2hhbnRJZCI6IjEyMzQ1Njc4IiwiYWNxdWlyZXJCSU4iOiIxMjM0NTYiLCJtZXJjaGFudE5hbWUiOiJUZXN0IE1lcmNoYW50IiwiYXV0aGVudGljYXRpb25QcmVmZXJlbmNlcyI6eyJhdXRoZW50aWNhdGlvbk1ldGhvZHMiOlt7ImF1dGhlbnRpY2F0aW9uTWV0aG9kVHlwZSI6IjNEUyIsImF1dGhlbnRpY2F0aW9uU3ViamVjdCI6IkNBUkRIT0xERVIiLCJtZXRob2RBdHRyaWJ1dGVzIjp7ImNoYWxsZW5nZUluZGljYXRvciI6IjAxIn19XSwicGF5bG9hZFJlcXVlc3RlZCI6IkFVVEhFTlRJQ0FURUQifX19fSwiU1JDTUFTVEVSQ0FSRCI6eyJvcmlnaW4iOiJodHRwczovL3NhbmRib3guc3JjLm1hc3RlcmNhcmQuY29tIiwicGF0aCI6Ii9zZGsvc3Jjc2RrLm1hc3RlcmNhcmQuanMiLCJwYW5FbmNyeXB0aW9uS2V5Ijp7Imt0eSI6IlJTQSIsImUiOiJBUUFCIiwidXNlIjoiZW5jIiwia2lkIjoiMjAyMzAyMDcyMjM1MjEtc2FuZGJveC1mcGFuLWVuY3J5cHRpb24tc3JjLW1hc3RlcmNhcmQtaW50Iiwia2V5X29wcyI6WyJlbmNyeXB0Iiwid3JhcEtleSJdLCJhbGciOiJSU0EtT0FFUC0yNTYiLCJuIjoidDA2SThzamxTLXJyczd1Q2FnSDhldm9ldW1hUm92S3ppWlNJOVMyTjlJRFE5dFcyUGFwZlJhOUxjMUt2ZUVCRFZzMjdQa2hrVTVPeUhnUDBpRWpUdUtWcHZoNTlUNGxhLW1CU0lsczdVZWNVUUxMYTBXa21idEw3ak5kbHRBNWZxN0FoY0FyNXFjYTk4OHFyTGQ3SXlyOUUwQzNUeGJUOXRvMWlRY3B6OG9jWk9EUlhvaWRGQW5PVkw1WUdGbWxzcmVEYko0VmhzaTBwQWRjY1FjaWwteWRTZ3VyS0ItcnFLcHBiOWVwb211NFFVaDMzODJDdjhOb2JZbUYzb3M4bkdHZ0dQLWN5WG8wbnNLY1BBZ2ZybFF6b3M3cUh4VU9yRmUyeF9sWjFHMUFFLVhya3J4akJ5czlxNTNHTVJTTkNROGMtX21jRjlwYnE0SFlCcy12RDVRIn0sInBhcmFtZXRlcnMiOnsic3JjaVRyYW5zYWN0aW9uSWQiOiIwNGVhM2EyNy1mYjc5LTRiMGItYWI5NS1mZWE3N2QwNjcwNmYiLCJzcmNpRHBhSWQiOiI3NzViMjFmMi00ZDAzLTRjNTAtYmNiYi1iMjY0NGRhYWVmNjUiLCJzcmNJbml0aWF0b3JJZCI6Ijg0NGY3ZTNkLTA3ZjAtNDRiMS1hMjM3LWU2NDI0NDRlMDUxMiIsImRwYVRyYW5zYWN0aW9uT3B0aW9ucyI6eyJ0cmFuc2FjdGlvblR5cGUiOiJQVVJDSEFTRSIsImRwYUxvY2FsZSI6ImVuX1VTIiwiZHBhQWNjZXB0ZWRTaGlwcGluZ0NvdW50cmllcyI6WyJVUyIsIkdCIl0sImNvbnN1bWVyRW1haWxBZGRyZXNzUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lclBob25lTnVtYmVyUmVxdWVzdGVkIjp0cnVlLCJ0cmFuc2FjdGlvbkFtb3VudCI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6IjIxLjAwIiwidHJhbnNhY3Rpb25DdXJyZW5jeUNvZGUiOiJVU0QifSwiZHBhQWNjZXB0ZWRCaWxsaW5nQ291bnRyaWVzIjpbXSwiZHBhQmlsbGluZ1ByZWZlcmVuY2UiOiJGVUxMIiwiZHBhU2hpcHBpbmdQcmVmZXJlbmNlIjoiRlVMTCIsImNvbnN1bWVyTmFtZVJlcXVlc3RlZCI6dHJ1ZSwicGF5bG9hZFR5cGVJbmRpY2F0b3IiOiJGVUxMIiwicGF5bWVudE9wdGlvbnMiOnsiZHluYW1pY0RhdGFUeXBlIjoiQ0FSRF9BUFBMSUNBVElPTl9DUllQVE9HUkFNX1NIT1JUX0ZPUk0ifX19fSwiU1JDQU1FWCI6eyJvcmlnaW4iOiJodHRwczovL3F3d3cuYWV4cC1zdGF0aWMuY29tIiwicGF0aCI6Ii9ha2FtYWkvcmVtb3RlY29tbWVyY2Uvc2NyaXB0cy9hbWV4U0RLLTEuMC4wLmpzIiwicGFuRW5jcnlwdGlvbktleSI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsImtpZCI6InNyYy1hbWV4LWNhcmQtZW5jLTIwMjYiLCJhbGciOiJSU0EtT0FFUC0yNTYiLCJuIjoicFpNa2VwaUY5TnM4QTBnQlhDWGkwV1dzZnZZOXJSNUVJdHpGbXV0RkVkNlFHMHItVkYtSUJhRFNkM091RHdUVGRzeURySVh4cUR5eUs0Wm1neTI3QzdpT2dYZi1OZmZELU9UOWxuVUxOMV8xa3NrR0ROZEhLUWVFd2FsS0JrNkhPcTFCZGZQak9mTkg5WmJ6TS1HbnZMdWpzWkJLMHpveWhCcGdpZmh5R043SGdNRmFCZXJTeld5T0Q4aVAyZENERzNkMTIxRklnbm9waXVLZmdQaWIyZkZqQjBIeWJEOXVHZ0NocWRrYmxiOENja2pwZWJpYzZFbmdjc2lOYlR3UHAtT2tpMmlDN1FaRUljOWZ1eko1SGllb0JWX3Fha3lfUF9qUkJRSkRmSThhMnVlaDBUaG9rbllORFB6ZXlGV1dCZTZmYndLblZjT0lpaDc3WXF3YTR5bHczTVJWblJnVzMxU0JDX0owWVh5UzJnTFdMY3dUMU1hSGQ0WXdVbW43bjVZWWZYak5rTDg5X2ZycDcyc3ItSmlQbmZMUHBvQ204UHJiZTJWcTJ3VnhkMjc0bUd5X3I3S2pfWnIwY3UwaGlTem1jTnFZbWdITG8xUTc4UnhaaXlKMWNnWU5pXy1EQWR6cnE3dGxnRkR6eHVZTHRBVUhYZ1prdUxlVS13Q0wifSwicGFyYW1ldGVycyI6eyJzcmNpVHJhbnNhY3Rpb25JZCI6IjA0ZWEzYTI3LWZiNzktNGIwYi1hYjk1LWZlYTc3ZDA2NzA2ZiIsInNyY0luaXRpYXRvcklkIjoiOGVjMmM4ODgtNjRjYy00ZWZjLTkxNzUtYjMzNzQ1MmIyOGM4IiwiZHBhRGF0YSI6eyJkcGFOYW1lIjoiMDQwNCBUZXN0IENUUERJVUkgIiwiZHBhTG9nb1VyaSI6Imh0dHBzOi8vd3d3LnRlc3QuY29tLyIsImRwYVByZXNlbnRhdGlvbk5hbWUiOiIwNDA0IFRlc3QgQ1RQRElVSSAiLCJkcGFVcmkiOiJodHRwczovL3d3dy50ZXN0LmNvbS8ifSwiZHBhVHJhbnNhY3Rpb25PcHRpb25zIjp7ImRwYUxvY2FsZSI6ImVuX1VTIiwiZHBhQWNjZXB0ZWRCaWxsaW5nQ291bnRyaWVzIjpbXSwiZHBhQWNjZXB0ZWRTaGlwcGluZ0NvdW50cmllcyI6WyJVUyIsIkdCIl0sImRwYUJpbGxpbmdQcmVmZXJlbmNlIjoiQUxMIiwiZHBhU2hpcHBpbmdQcmVmZXJlbmNlIjoiQUxMIiwiY29uc3VtZXJOYW1lUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lckVtYWlsQWRkcmVzc1JlcXVlc3RlZCI6dHJ1ZSwiY29uc3VtZXJQaG9uZU51bWJlclJlcXVlc3RlZCI6dHJ1ZSwicmV2aWV3QWN0aW9uIjoiY29udGludWUiLCJ0aHJlZURzUHJlZmVyZW5jZSI6Ik5PTkUifX19fSwiY2FwdHVyZU1hbmRhdGUiOnsic2hvd0NvbmZpcm1hdGlvblN0ZXAiOnRydWUsImJpbGxpbmdUeXBlIjoiRlVMTCIsInJlcXVlc3RFbWFpbCI6dHJ1ZSwicmVxdWVzdFBob25lIjp0cnVlLCJyZXF1ZXN0U2hpcHBpbmciOnRydWUsInNoaXBUb0NvdW50cmllcyI6WyJVUyIsIkdCIl0sInNob3dBY2NlcHRlZE5ldHdvcmtJY29ucyI6dHJ1ZSwiY29tYm9DYXJkIjpmYWxzZSwicmVxdWVzdFNhdmVDYXJkIjpmYWxzZSwiZGV2aWNlRmluZ2VycHJpbnRpbmciOnsiVE0iOnsidXJsIjoiaHR0cHM6Ly90bS5jeWJlcnNvdXJjZS5jb20vZnAvdGFncy5qcz9vcmdfaWRcdTAwM2Qxc25uNW45d1x1MDAyNnNlc3Npb25faWRcdTAwM2QwNDA0X3Rlc3RjdHBkaXVpMDAxMjNlYTc4ZDctNDJlMi00MTZhLTkwYjAtNTAzOTI1OGQ4MTkwIiwic2Vzc2lvbklkIjoiMjNlYTc4ZDctNDJlMi00MTZhLTkwYjAtNTAzOTI1OGQ4MTkwIn19fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJhbW91bnREZXRhaWxzIjp7InRvdGFsQW1vdW50IjoiMjEuMDAiLCJjdXJyZW5jeSI6IlVTRCJ9LCJiaWxsVG8iOnsiYWRkcmVzczEiOiIxMjMgQ29vbCBTdHJlZXQiLCJhZG1pbmlzdHJhdGl2ZUFyZWEiOiJOWSIsImJ1aWxkaW5nTnVtYmVyIjoiMTIiLCJjb3VudHJ5IjoiVVMiLCJkaXN0cmljdCI6ImRpc3RyaWN0IiwibG9jYWxpdHkiOiJOZXcgWW9yayIsInBvc3RhbENvZGUiOiIxMDE3MiIsImVtYWlsIjoiYm9sdG9uakB2aXNhLmNvbSIsImZpcnN0TmFtZSI6IlZpa3RvciIsImxhc3ROYW1lIjoiVmF1Z2huIiwibWlkZGxlTmFtZSI6IkYiLCJuYW1lU3VmZml4IjoiSnIiLCJ0aXRsZSI6Ik1yIiwicGhvbmVOdW1iZXIiOiIrMTEyMzQ1Njc4OTAiLCJwaG9uZVR5cGUiOiJtb2JpbGUifSwic2hpcFRvIjp7ImFkZHJlc3MxIjoiNDU2IE5pY2UgQXZlbnVlIiwiYWRtaW5pc3RyYXRpdmVBcmVhIjoiQ0EiLCJidWlsZGluZ051bWJlciI6IjQwOSIsImNvdW50cnkiOiJVUyIsImRpc3RyaWN0IjoiVXB0b3duIiwibG9jYWxpdHkiOiJMb3MgQW5nZWxlcyIsInBvc3RhbENvZGUiOiI5MDAxMCIsImZpcnN0TmFtZSI6IkFsYW4iLCJsYXN0TmFtZSI6IlR1cmluZyJ9fSwidGFyZ2V0T3JpZ2lucyI6WyJodHRwczovL3Zhc2RlbW9zLnZpc2EuY29tIl0sImlmcmFtZXMiOnsibWNlIjoiL21jZS9tY2UuaHRtbCIsImJ1dHRvbnMiOiIvYnV0dG9ubGlzdC9idXR0b25saXN0Lmh0bWwiLCJzcmMiOiIvc2VjdXJlLXJlbW90ZS1jb21tZXJjZS9zcmMuaHRtbCIsImN0cCI6Ii9jdHAvY3RwLmh0bWwiLCJnb29nbGVwYXkiOiIvZ29vZ2xlcGF5L2dvb2dsZXBheS5odG1sIiwiYXBwbGVwYXkiOiIvYXBwbGVwYXkvYXBwbGVwYXkuaHRtbCIsInBhemUiOiIvcGF6ZS9wYXplLmh0bWwiLCJjaGVjayI6Ii9jaGVjay9jaGVjay5odG1sIiwiZ2EiOiIvZ2EvZ2EuaHRtbCIsIm9yYyI6Ii9vcmMvb3JjLmh0bWwiLCJ0bSI6Ii90bS90bS5odG1sIiwiYXBtIjoiL2FwbS9hcG0uaHRtbCIsImFwbS1zdGVwcGVyIjoiL2FwbS1zdGVwcGVyL2FwbS1zdGVwcGVyLmh0bWwifSwiY2xpZW50VmVyc2lvbiI6IjAuMzMiLCJjb3VudHJ5IjoiVVMiLCJsb2NhbGUiOiJlbl9VUyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIl0sImNvbXBsZXRlTWFuZGF0ZSI6eyJ0eXBlIjoiUFJFRkVSX0FVVEgiLCJ0cmFuc2FjdGlvbklkIjoiNWZqT2s0MEhFSTV5czRISFBWRFphR2NlMHYwWiIsImNvbnN1bWVyQXV0aGVudGljYXRpb24iOnsiYWxsb3dlZENhcmROZXR3b3JrcyI6WyJWSVNBIiwiQU1FWCIsIk1BU1RFUkNBUkQiXSwiYWxsb3dlZFBheW1lbnRUeXBlcyI6WyJDTElDS1RPUEFZIiwiUEFORU5UUlkiXX19LCJhbmFseXRpY3MiOnsiZ29vZ2xlIjp7InNjcmlwdCI6Imh0dHBzOi8vd3d3Lmdvb2dsZXRhZ21hbmFnZXIuY29tL2d0YWcvanMiLCJpZCI6IkctVEY4MDRETlY5OSJ9LCJldmVudEdyb3VwSWQiOiIxWUdTbGE0TTdmS3pqTV9pdlBMV2ZaeXVaT2ZFOV85S0FNZ3JZVjAweF96SWFhcEtPbU9SbnZ4LVVKdU1KU080In0sImNyIjoiNUYxZ3ZCeWJmTmZBcThIaEx5V1hlQmJVNFUtd2ZVSERkMDc1RThBMTRxdlpLWmdZQlJoQ0ltSkI0YklsbE95UFlWMzdvNVdSaURZYVpsaGJidXhZR1V5MVZvd1ZibUZOZjkxTk84MVVoRGhUc3NVN3pkbElUQkc1dFVwdmljMVVXb0dROXBWaDZ4eTZTLXZWNHFNIiwic2VydmljZU9yaWdpbiI6Imh0dHBzOi8vdGVzdHVwLmN5YmVyc291cmNlLmNvbSIsImNsaWVudExpYnJhcnkiOiJodHRwczovL3Rlc3R1cC5jeWJlcnNvdXJjZS5jb20vdWMvdjEvYXNzZXRzL2FwdzFIMHVjVThUbDl2MHBYX055MjJPRUcwR0RLcG9pQ01aTFNvd1ZUZXZCQUVBbml6Y2ptd25aNjZwaWdLcnl4TE45QzZ4alRwbUUybkxrY21ySzk1VlZDM0E1VWp6V0htbG4zaERyNFF0ZWYtQVM3eWNOTDN5ZXd2aGliTzR1ekJhdlpTSnc5VG1wd2FybkF6c1pSNnQ0L1NlY3VyZUFjY2VwdGFuY2UuanMiLCJsb2dnaW5nUGF0aCI6Ii91Yy92MS9sb2ctZXZlbnRzIiwiYXNzZXRzUGF0aCI6Ii91Yy92MS9hc3NldHMvYXB3MUgwdWNVOFRsOXYwcFhfTnkyMk9FRzBHREtwb2lDTVpMU293VlRldkJBRUFuaXpjam13blo2NnBpZ0tyeXhMTjlDNnhqVHBtRTJuTGtjbXJLOTVWVkMzQTVVanpXSG1sbjNoRHI0UXRlZi1BUzd5Y05MM3lld3ZoaWJPNHV6QmF2WlNKdzlUbXB3YXJuQXpzWlI2dDQiLCJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LWNRMXQ2R1FjTjVFbDRtbDFIMTBlYVNWK1R1Uy9oRnJ5YmxMTGw5cy94allcdTAwM2QifSwidHlwZSI6ImdkYS0wLjEwLjAifV0sImlzcyI6IkZsZXggQVBJIiwiZXhwIjoxNzY1ODI3MTQ0LCJpYXQiOjE3NjU4MjYyNDQsImp0aSI6Ims3b3kzcmh5S25McjQ0cGYifQ.Xa1Rw64mKGk9lr-25KWbbARmCTIF1wEabTxrRGU3tE_Pk1g0bPZP67T5vau81BNOn2pd2aaSKSQvywyuOMvgObkmg-vVKrasZtxHFGQUz-3F16j8y85p2fNElUwzl1s12dbPaA6IgsvZ47k2QGBmYcVq7aBAb9ia4zhORqHPb8B_gWuZoaMtBeH59DyLg1184XUiZ7-vEOaepZTJUcjH4g8DXlaOlwO0h8bHQTpLnjvHGyBU0ltNdePR-FoPUn0ZjnE22H-Mg0vncpE1V2qymtBMEXiESZjrz1SbYx3Wp1oYhCOvnikyxs4yH1eJPqrlRUw7eyPyRGjjecTe1S3aoA
Decrypted Capture Context Header

```
{
          "kid": "zu",
          "alg": "RS256"
          }
```

Decrypted Capture Context Body with Selected Fields

```
{
  "flx": {
    // filled with token metadata
  },
  "ctx": [
    {
      // filled with data related to your capture context request parameters
      "data": {
        "clientLibrary": // taken dynamically from response ,
        "clientLibraryIntegrity": //taken dynamically from response: "sha256-cQ1t6GQcN5El4ml1H10eaSV+TuS/hFryblLLl9s/xjY="
      },
      "type": "gda-0.10.0"
    }
  ],
  "iss": "Flex API",
  "exp": 1765827144,
  "iat": 1765826244,
  "jti": "k7oy3rhyKnLr44pf"
}
```

Transient Tokens {#ctp-tokens-intro}
====================================

The response to a successful customer interaction with the `Unified Checkout` is a transient token. This is returned in the response from the `unifiedPayments.show()` function. The transient token is a reference to the payment data collected on your behalf. Transient tokens enable secure card payments without risking exposure to sensitive payment information. The transient token is a short-term token with a duration of 15 minutes.

Transient Token Format {#ctp-tokens-format}
===========================================

The transient token is issued as a JSON Web Token (JWT) ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").
The payload portion of the token is a Base64URL-encoded JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-jwts.md "").

Example: Transient Token Format {#uc-trans-tkn-ex}
==================================================

Transient Token Payload

```
eyJraWQiOiIwMEl1NWJDT2NINVpPWjFNYldsQktodzFZeFFjSkVlZSIsImFsZyI6IlJTMjU2In0.eyJtZXRhZGF0YSI6eyJzZXF1ZW5jZU51bWJlciI6IjEiLCJjYXJkaG9sZGVyQXV0aGVudGljYXRpb25TdGF0dXMiOmZhbHNlLCJwYXltZW50VHlwZSI6IlNSQ01BU1RFUkNBUkQifSwiaXNzIjoiRmxleC8wMCIsInBheW1lbnRDcmVkZW50aWFsc1JlZmVyZW5jZSI6eyJ1Y19hZ25vc3RpY19wb3J0Zm9saW9fdmFsaWQiOiJXaWUyM2NBS3RGblFlSXpqeDRFUXgifSwiZXhwIjoxNzY1ODg1MDcyLCJ0eXBlIjoiZ2RhLTAuMTAuMCIsImlhdCI6MTc2NTg4NDE3MywianRpIjoiMUQwMlk4Q09FQURYS1k5VjRHTjRNUDJOSVNMVjNQM1dSUUNEV0VZNDJHUjNBRzIzTUI3WjY5NDE0NDkwQkI1MSIsImNvbnRlbnQiOnsiZGV2aWNlSW5mb3JtYXRpb24iOnsiZmluZ2VycHJpbnRTZXNzaW9uSWQiOnt9fSwicHJvY2Vzc2luZ0luZm9ybWF0aW9uIjp7InBheW1lbnRTb2x1dGlvbiI6eyJ2YWx1ZSI6IjAyNyJ9fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJiaWxsVG8iOnsiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiZmlyc3ROYW1lIjp7fSwicGhvbmVOdW1iZXIiOnt9LCJhZGRyZXNzMSI6e30sInBvc3RhbENvZGUiOnt9LCJsb2NhbGl0eSI6e30sImFkbWluaXN0cmF0aXZlQXJlYSI6e30sImVtYWlsIjp7fX0sImFtb3VudERldGFpbHMiOnsidG90YWxBbW91bnQiOnt9LCJjdXJyZW5jeSI6e319LCJzaGlwVG8iOnsiZmlyc3ROYW1lIjp7fSwiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiYWRkcmVzczEiOnt9LCJwb3N0YWxDb2RlIjp7fSwibG9jYWxpdHkiOnt9LCJhZG1pbmlzdHJhdGl2ZUFyZWEiOnt9fX0sInBheW1lbnRJbmZvcm1hdGlvbiI6eyJjYXJkIjp7ImV4cGlyYXRpb25ZZWFyIjp7InZhbHVlIjoiMjAyNyJ9LCJudW1iZXIiOnsibWFza2VkVmFsdWUiOiJYWFhYWFhYWFhYWFg5OTA4IiwiYmluIjoiNTE4NjAwIn0sImV4cGlyYXRpb25Nb250aCI6eyJ2YWx1ZSI6IjAzIn0sInR5cGUiOnsidmFsdWUiOiIwMDIifSwidHlwZVNlbGVjdGlvbkluZGljYXRvciI6eyJ2YWx1ZSI6IjEifX19fSwiXyI6IkwrYnlQL2FIRnhEUDRPc0NGNFI5RkhjbElkZkFXR0g4VkF3NGdta0NubGRyZzQ3WDdnR1hseUZRTWM4aU5KWjBzSlNhTlFOTzM5RHVCVWdWaW1SeC9zRUJJS2VQYXFvRVRoWDZpRjFrWWs1ZkxjWDRqU1gvTmtzb1U0bGQzU0RNTnJHcS8ybDRoM0laTjd1WEVON1g5azA5K3FaRFNaWVk3S1dzaVJXeXNwcHpFZE5uQy9ORGYxY1ZqNUJHZTZnN3Jjckt0THYyT1VzYUIyb3hicVkwL2VuUFY4N0JHakMrUk9lSmFYa3VGeml0RDVrQ0paZHdoYnorRStRVmtnejdBVTZnNG5pa0dsWDFNUklkeXVVNnY4QlJsWG42ZEF3c252TW5pZ3Yvc05NUE4zV0hSaUhZWHZubTdramVOd2k2YW1EbkdTSzVqY3RFMmJPWDZUU0RmWG5RSE01eVhWcFdMRHZxa0VQOVZzM2NBNmhTbTlZcHFaaXRSSjZ5OWtMSGFNemsydm9TWlhUV1JQU210UkZ2TWdcdTAwM2RcdTAwM2QifQ.M1ttoaMyKz9NjQ7nYfhGqrt7Gga1YvUph8FH4-0aV98tNbZilEqF4ANQHKFjNQavJ5_EKB_4cDayuwa7xyZzrz2WNXSlRS97EJYfvFAYza8cq2SpvHlR1DvJdMuYsyui-fZafdkxqTudsAUUYJErWezliWOvCw2gi18hb3bS3V_evt8zznRdgbwd7Q1BgSmQwgnIDI-H4wdZMByMbpG1zC8UjbvyPB5OUQxOTCljmbsiAquSI_8LFJoasRUK9txVjezO49E_DX1ClETbnzuiUlJ6MzBlTNAtdbxGB5ELjuf8-SSj4ojlZZTMWARllskZsx_DUtqLBUdNXKpPKEJtzg
```

EPC Token Payload

```
eyJhdWQiOiJ1Y19hZ25vc3RpY19wb3J0Zm9saW9fdmFsaWQiLCJzdWIiOiJ1Y19hZ25vc3RpY192YWxpZDAwMSIsImtpZCI6IjIwMjMwNTE0LWRyYWZ0LXBzcC1lbmNyeXB0IiwiY3R5IjoiSldUIiwiZW5jIjoiQTI1NkdDTSIsImV4cCI6MTc2NTg4NDc3MiwiYWxnIjoiUlNBLU9BRVAtMjU2IiwianRpIjoiV2llMjNjQUt0Rm5RZUl6ang0RVF4In0.H4UAdHUKUm4DRDfTnxQkRG9swxVBFWd63ikf4wo4niF7mBb4sMsm0SVrILu3IbWb6SThDJUnjyfE84QbJ5UmXBSk9k585n9iJYNCMq_-OE72N9MxOwg9rSrO302TkH1Nob7pvENm0AaMPk3SLeYzBur6fVvxj7sf2Ybl8ZnoTME_f_c2XVzZh5JzruamR5Y4_i7T90GRFxYlGpXFbm1WQcJdLkVumWp9My8rubk4fkgkKFUVT76J_dSXPIPqEiSM8NyGtXw-fkhXqq-iTzqDxd07Cp1PMrqFgKsSWUhV647TmnnUmC0bQ8GrMW2Bag18q9UNmEJl5alb-CE_WW1H6A.h__wQ3yafSI9TD-3.t3zvYlmp4G24HYG08OHBVh-tlX120MqXe_IK5dmUuOTzk-v3nWOU7mdp6cM66mwGSPOlie9rUn_oZG34gxMXK-uxGuOo4d-D1SvYaPfhGLyq_LQRIO1iCtdKaKNIyU7AuWkg3G0IS4TMb3hqxG0mMI0XzCbOyEkZzPjkwPFkyE-T1cScesuiK8_qRhQjGNRT57WIhemI64eNUoLaBjTv6HrHTYVGBHgR7J49quaTkVbv9IJaU4qklQUuT4HMWCr6YapApRpuuqGXgJ7_f4oLPJC4UpoxE5cJypdm3lJRFBPp4JZmod9nfA8onRIJbWSC6EdU7SscIV2yEFJybqUGED70fBgBL4rwWMxxw81aEK41CEqlr1XgWAARA1bVsljsrmAsYRLZ38lM1hqZrspENW8hVBLzcO_wyuCQRNZOIufOhl_CCc3Xnq0LKlLR6_hCcafcg2Skxqm4m2_E_iiYWVPSy_DQIVErvidQ9JDjKDdNxTJkhiBe1q4RKs5bNmy4KajKJ2gdOnwblFcxYTB3hs4kuIZdHvU-Lw2UjohCQkv0RtO5QziS_RQAxbT0FG8hHJFnMDR83YU1-38mpM2xSQPaGhQ_2Vzyz7Uwt-fS7gfISg8pF4JX1X4s4n3_bCUfuK1RF2CGOIQdtyxYvdA6iTypH55tDa51idfRS7URmKacsvofB6IavM9sCNcFpe8J0lX3UOQ0H_AIFG9XSs1iu-ct2xAQduOPgeUUkmEMBYUl245Y2dIY0NUrwWZJ_y_13WA6hs1r8Nu2S5E547u-_XhVCuXkuBluhO24UetZbr8pm1B0-YxKtIMLMeUDEyUvLHcihYhRcC02rI8KDl9Nl-NGXenxFf5X6Bhapla7HHCbpd7lrf8MpYCqs7mpO6EHJgDDZxW1mEzcB4x9-ZeTeThJ8_Dwl3E-LtqOcgHbC7PI_QGqMdPKWeEyQqKv-m7KRnEL-fsPT2s9SMtxrxPonGCHtnQ3LqUKqmRIbx0-yalxa6fGGu-od83OMR9FbKhKcAKmk14bIFo8LCkjG3siSjbVr3lK65kmfRoQdiBGOw2Uzb_613dwDLh2yjjpFuuZLS9Bn1lkzxZq5qtNLIKw8CMJ5k_BD8LIGR7iuYB9iRCJiWFjUVj8yVW2zKpk1tdfx_2fhQu13cIUZRx-nOQqYgrfv2KEwfeuJPdSmlzHbN7YplEA2ZvSdIc08rteZaRkVXcWK7rp3Wt7I4AUwUVV8i--Ep6X8SgytFP_FHN4-S_xGAJmljKf9XpBUBvmXxt-Lrba_xnKW1aaGtz-8iOQ4V0K5Gmao7E1gUpta6BjXIXV1HqNLusavOUpTbTTk-CtJnCHZ4BkoAWCPa3QxLQZ0jQAYg71aoi2thSNcTL7_3Qgrxj5nsGMX_cBBSRhCDS8G6Zq0ZLf2sJYK2lNMwax6EwK0NGi8KMUt_X6-lsk2d00ha43fKdtyKqRtB5nnwmD0ONZC2Qp6OsQUxnn066on0jY4khUydBejypMd_93D8rb60q7FHRbGPKpo4aKVvsOp_A0FMWBTR9TTjwIvB3psvSgZChoDO0qZW_RgDHCVDiJbA4umeTCvhTmLgToay1JH7IBH_BBiCm-GADIsIf0is2BFswZIy8PAqpw4DKk164Gw16KHZt7ukZ7uIz6t_HIatBGAEzKav5Xcy33XUfp_SDrOr-QruYQ22kb0TKE9yjfj_dwjEz4VEAJQqnP_ci9_YeLz2VCFY23mGVtgyvcwmJ-L7U4QlVVeUOWIuxl63wWJSZIfm_0H5VYvJo_O9uI7kvccayhaWwHqaSKytefQZ-_HU5EiELxArQziIPByqR97DdDgmutRBxNnGBvLPRwytMGVwmVZOxafrkN5xVLrkif7yRqP3mr5KhUvcTN9zhfWh3s-SqESHL1G-XjET1FpG-TdwVP7ZK3VYFuaoCx2_11U3H1N7FcFXuQqeVvkwEZpvmPd4bFAN9az2q0C8_HyKkjsyvGAuBFerhYrGQQ3lDWIvwcGu09VygK_COH7ZIK212B8F0wFllbyuJW1z4i9-fv8f0KCewyVU7lzwGDLXIR.qJp4DNmwKcsTj_q0Xj8TJw
```

Encrypted Transient Token Payload

```
{
  "metadata": {
    "sequenceNumber": "1",
    "cardholderAuthenticationStatus": false,
    "paymentType": "PANENTRY"
  },
  "iss": "Flex/00",
  "exp": 1762870464,
  "type": "gda-0.10.0",
  "iat": 1762869564,
  "jti": "1D4Q8FJSSZ9ASKQ9ZCJ7E13IFOITOOH2GGHY6TRZ3O28TUQ1BN8H691344C098CA",
  "content": {
    "deviceInformation": {
      "fingerprintSessionId": {}
    },
    "orderInformation": {
      "billTo": {
        "country": {},
        "lastName": {},
        "firstName": {},
        "phoneNumber": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "company": {
          "name": {}
        },
        "administrativeArea": {},
        "email": {}
      },
      "amountDetails": {
        "totalAmount": {},
        "currency": {}
      },
      "shipTo": {
        "firstName": {},
        "lastName": {},
        "country": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {}
      }
    },
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2027"
        },
        "number": {
          "maskedValue": "XXXXXXXXXXXX1111",
          "bin": "411111"
        },
        "securityCode": {},
        "expirationMonth": {}
      }
    }
  }
}
```

IMPORTANT The empty field values in the transient token indicate which fields were captured by the application without exposing you to personally identifiable information directly.
PAN BIN in `metadata` Object
The `cardDetails` object, including the PAN BIN, is included in the transient token `metadata` when a `Click to Pay` network token is used as a payment method. This allows you to display information about the card on invoices and see the BIN details that are linked to the underlying card.

```
"metadata": {
  "cardDetails": {
    "suffix": "9876",
    "prefix": "123456",
    "expirationMonth": "MM",
    "expirationYear": "YYYY"
  }
}
```

Authentication Status in metadata Object
The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.
If you are using `Unified Checkout` with unifiedPayment.complete() and consumerAuthentication is set to `true` in the complete mandate request, then `Payer Authentication` is called automatically if it is available for the selected payment method and card network. If you use a transient token to request follow-on services directly, the value of this field indicates if the transaction has been authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

Token Verification {#ctp-tokens-verification}
=============================================

When you receive the transient token, you should cryptographically verify its integrity using the public key embedded within the capture context. Doing so verifies that `Cybersource` issued the token and that the data has not been tampered with in transit. Verifying the transient token JWT involves verifying the signature and various claims within the token. Programming languages each have their own specific libraries to assist. For an example in Java, see: [Java Example in Github](https://github.com/CyberSource/cybersource-unified-checkout-sample-java/blob/main/src/main/java/com/cybersource/example/service/JwtProcessorService.java "").

PAN BIN in metadata Object
--------------------------

The `cardDetails` object, including the PAN BIN, is included in the transient token `metadata` when a `Click to Pay` network token is used as a payment method. This allows you to display information about the card on invoices and see the BIN details that are linked to the underlying card.

```
"metadata": {
  "cardDetails": {
    "suffix": "9876",
    "prefix": "123456",
    "expirationMonth": "MM",
    "expirationYear": "YYYY"
  }
}
```

The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.
If you are using `Unified Checkout` with unifiedPayment.complete() and consumerAuthentication is set to `true` in the complete mandate request, then `Payer Authentication` is called automatically if it is available for the selected payment method and card network. If you use a transient token to request follow-on services directly, the value of this field indicates if the transaction has been authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

Dual-Branded Cards {#dual-co-brand-card-support}
================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["VISA", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Visa.
During the transaction, the card type is populated with the first network in the list, and the detectedCardTypes field returned in the transient token includes all of the detected card types in the transient token.
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Visa and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option that the customer selects during checkout.

Payment Details API {#ctp-token-get-pymnt-details}
==================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the payment details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#ctp-token-get-pymnt-details_d33e1088}
------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/up/v1/payment-details/`*{id}*{#ctp-token-get-pymnt-details_d33e1095}
**Test:** `GET ``https://apitest.cybersource.com``/up/v1/payment-details/`*{id}*{#ctp-token-get-pymnt-details_d33e1107}
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/up/v1/payment-details/`*{id}*
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/up/v1/payment-details/`*{id}*
The `{id}` is the full JWT received from `Unified Checkout` as the result of capturing payment information. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

Required Field for Retrieving Transient Token Payment Details {#ctp-token-get-pymnt-details-required}
=====================================================================================================

Your payment credentials request must include this field:

id
:
The `{id}` is the full JWT received from `Unified Checkout` as the result of capturing payment information.

REST Example: Retrieving Transient Token Payment Details {#ctp-token-get-pymnt-details-ex-rest}
===============================================================================================

Request

```keyword
GET https://apitest.cybersource.com/up/v1/payment-details/{id}
```

{#ctp-token-get-pymnt-details-ex-rest_codeblock_c51_vmt_gwb}
Response to Successful Request

```
{
  "paymentInformation": {
    "card": {
      "expirationYear": "2027",
      "number": "XXXXXXXXXXXX9908",
      "expirationMonth": "03",
      "type": "002",
      "typeSelectionIndicator": "1"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "21.00",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "Jane",
      "country":  "USD"
      "lastName": "Doe",
      "phoneNumber": "+44-1234567890",
      "address1": "900 Metro Center Boulevard",
      "postalCode": "94404",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "email": "example@email.com"
    },
    "shipTo": {
      "firstName": "Jane",
      "country": "US",
      "lastName": "Doe",
      "address1": "123 Main Street",
      "postalCode": "10789",
      "locality": "New York",
      "administrativeArea": "NY"
    }
  }
}
```

Payment Credentials API {#ctp-token-get-pymnt-credentials}
==========================================================

This section contains the information you need to retrieve the full payment credentials collected by the `Unified Checkout` tool using the payment credentials API. The payment information is returned in a redundantly signed and encrypted payment object. It uses the JSON Web Tokens (JWTs) as the data standard for communicating this sensitive data.

> IMPORTANT
> Payment information returned by the ` payment-credentials ` endpoint will contain Personal Identifiable Information (PII). Retrieving this sensitive information requires your system to comply with PCI security standards. For more information on PCI security standards, see: <https://www.pcisecuritystandards.org/>
> The response is returned using a JWE data object that is encrypted with your public key created during the `Unified Checkout` tool's integration. For more information, see [Upload Your Encryption Key](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/uc-upload-encrypt-key-intro.md "").
> To decrypt the JWE response, use your private key created during the `Unified Checkout` tool's integration. The decrypted content is a JWS data object containing a JSON payload. This payload can be validated with the `Unified Checkout` public signature key.
> IMPORTANT
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Returned Credentials
--------------------

A payment account number (PAN) or network token is returned on your request depending on your payment method and `Click to Pay` account status:

|     `Click to Pay` Account Status      | American Express |  Mastercard   |     Visa      |
|----------------------------------------|------------------|---------------|---------------|
| New card not saved in `Click to Pay`   | PAN              | PAN           | PAN           |
| New card saved in `Click to Pay`       | PAN              | Network Token | Network Token |
| Existing card stored in `Click to Pay` | PAN              | Network Token | Network Token |
[Payment Credentials Returned by Card Type and `Click to Pay` Account Status]

When you retrieve PAN information from the Payment Credentials API, the response includes the PAN, card expiration date, and the card verification value (CVV). When you retrieve network token information, the response includes the network token and network token cryptogram.

> IMPORTANT
> Visa and Mastercard always attempt to provision a network token. A PAN is returned when a network token is not provisioned before checkout or when the cardholder did not request to enroll the card in ` Click to Pay `.
> Network tokens are generated in the wallet of the `Click to Pay` token requestor ID (TRID). When tokenization is successful, Visa can also complete authentication during the `Click to Pay` experience to acquire an EC105 payload. For information on authentication, see [Click to Pay Customer Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication.md "").

Endpoint {#ctp-token-get-pymnt-credentials_d33e632}
---------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#ctp-token-get-pymnt-credentials_d33e639}
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#ctp-token-get-pymnt-credentials_d33e651}
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*
The *{ReferenceID}* is the reference ID returned in the `id` field when you created the payment credentials.

Required Field for Retrieving Payment Credentials {#ctp-token-get-payment-credentials-required}
===============================================================================================

Your payment credentials request must include this field:

ReferenceID
:
The reference ID that is returned in the `id` field when you created the payment credentials.

REST Example: Retrieving Payment Credentials {#ctp-token-get-payment-credentials-example-rest}
==============================================================================================

Request

```keyword
https://api.cybersource.com/flex/v2/payment-credentials/E-firqlLk7GiziQwXxAsq
```

Encrypted Response to Successful Request

```
eyJhdWQiOiJwc3AiLCJzdWIiOiJwc19ocGEiLCJraWQiOiIyMDIzMDUxNC1kcmFmdC1wc3AtZW5jcnlwdCIsI
mN0eSI6IkpXVCIsImVuYyI6IkEyNTZHQ00iLCJleHAiOjE2ODQxNDk2NjQsImFsZyI6IlJTQS1PQUVQLTI1Ni
IsImp0aSI6IjA0NDUwNWNiLTM1ZDYtNDU2ZS05OTBlLWRkZjQwYzI5NzlhNCJ9.enhUfZJOjbMX-wZPIOb1zj
8sFZiix6JSJyNw2i9QJ4k_hd7Iy_UMYvOmS-X1FJwjH0IQxMIblSV8XqMegIOm5dYBYdqouUfC8zq4Zm_dsMo
Tp3m9T6z-A_eJ8MGaxqTHSf2vWiXB-EMrww2eCXPyVTBkI1OdmYIX-s85vsqYpW-s0ThlCKaGI7B4_rJKNa7m
ou9VMBtBnfzhHLtnHDW8vsX8rLmTT76Ct2jMdIoQnlQRgEOi-zYu0Jm0gHERavUtq_7lDw9Ta73_TFw3KA2fs
G13CURyR7ZXoZy9_nRifwHjwNVbaFRceAzXoVtvM8H8F-ZzIC8AdA1FRye7RqcK9Q.OlrMxOMDkVDU6goS.TP
fBhm1eBfRjCSSvuT6SxFeZ3SGwOC6qX2Z4rlAEY9lOor2Q2E1CMqB6o-q6DNkGtASFONBzKtoB0yAgXBpx3S7
2FltR8bd40qmRnPyTOAscXa3eWbP45EqZqHW58lwUtMwcBORcfSjxPnWUo-OGmKCtIgiUO4MTlBsl9HdCLx7R
Wpwslo0pKQAuFrURHJyhdE1JUArgjNQMdQwPvCjoZ2RxTzECEqE1l0KmBGM-w8suowrnTNZl8cwVUZKzHQEJV
-twAGykQIIRCI3ydHfCupyUuA-5-Wvlk6nhcL3qND4JF-E3EIRpzm7WH8pCV5nzByUue-grHejg774c7fi1eh
fTBUZ8v6X7rTZUBLL0V5343X3zQQy_G-vq5qcaJZ8AS2XWSi17r8UEHoU5emYu5QAuXy1AhL32nDRZuXzOzQ1
9JsrTN2CD8qxU7tDpkUCEmY2GEMp4sd-rfu_2qBZDdr74tjYNgMsTIXSpgGDiwjLMJu4r460YencO6-JweGCT
8woIySjBRYpX1_axxcO6I9RUTSopPbslZwq_zpy3UuDa9InlSexM--fatYfAehY857F7bFVXlnXeqr7X0_Lri
bJsx6CWJU1ihjMVtnF-SxeE3IdpJxyFYBb7D1iL3ywFooxcGqarXU-3_CBuDHvnJFDC_iQPaeH7csb-EMeNqF
TmFf8dWNQYG7IJDfEnrnRW_XtnczH-ZS67iVuGzGwJZDQfJZ-KLhnWr6FE1EnT1VLyXPM78WeocT7cnLXmr9B
gevNmU3q_SV5nxlDLPuCqF0PmFNxaTjqfF2Qw_zOCvazwFWuBdUDdHilPqhj3gfsOesAJVA7VoTDw2U3zte3V
09KcJLaHygwPomopWOODinKzcZeWfJ39984pQa5cOMSEToGegkRZyvSxpf5PTht30uB3F3qC4cVLOu4qukYsr
jXqOtxg3icde7lXywfAtEZgf54jAP2Cl8JFmGWL5YnIY44-zj-GVz2C8iCN1CCUP3U4eVxz2GtxNNSXuwY8OR
Udino4rF-OpqqdjX5F0Uw6J2D3uR9cWB4Ee3v8TIA3-tRkG4ScAcclEwjkwsILPgVLU57HOm0AnaEsznyHrd9
-Qfz_p-UjbsaD3e-_sr56-x2UZVVL6TAMmJqmS2C55CHgkkhtHBCu-vb0KOmssopIvaQA5jK6ZoCftewE8-98
816ZmoU8Sty05PSeK0yBlxFwTIeJxt-moszRawFuBrLAbOu72y_eeUtk1tHpHV2Db7T6XvaRD4NvOFZg8ianY
Y6uHidoTl1ApjCp8VG9oTJ-uKWAEp9TU6qEHUswZZUIBeGTKjzBkRAQ20cZs5POb-qtjteoWo9QdnczipZ8de
my-FSZwNRFPkeedl3oHLepeTgwVnmij9ovk0e5Wqq2GVUMe8sLa-4eEnjliIjAVUQ9YNJBeqLf6_wo3HF8o2k
4ZgSJTuPHAuP41-D6sYrOcM6WvkCfKRTXw7ue5unri3M0Rpd2TEnzyw.TaLt6G8QyRykbrxb0iV9Jg
```

Decrypted Response to Successful Request

```
{ // header
  kid = "zu"
  cty = "json+pc"
}.
{
  // registered claims
  iss = "https://flex.visa.com"
  sub = "ps_hpa"                                  // Merchant ID
  aud = "https://online.MyBank.com"
  exp = 1683105553                                // expiry of payment credentials
  iat = 1683104035                                // timestamp when JWT was created
  jti = "ae798686-a849-4dfa-836d-43e09cb183a4"    // transaction id

  "paymentInformation": {
    "tokenizedCard": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "type": "001",
      "cryptogram": "",
      "transactionType": "1"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com",
      "phoneNumber": "4158880000"
    }
  }
}
.SIGNATURE
```

Decrypted Response to Successful Request with EPC Token

```
{
    "aud": "uc_agnostic_portfolio_valid",
    "sub": "uc_agnostic_valid001",
    "deviceInformation": {"fingerprintSessionId": "61f4c1b9-a582-49e7-9854-60ab58d1c792"},
    "processingInformation": {"paymentSolution": "027"},
    "orderInformation": {
        "billTo": {
            "firstName": "Jane",
            "lastName": "Doe",
            "country": "US",
            "phoneNumber": "+44-1234567890",
            "address1": "900 Metro Center Boulevard",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "example@email.com"
        },
        "amountDetails": {
            "totalAmount": "21.00",
            "currency": "USD"
        },
        "shipTo": {
            "lastName": "Doe",
            "country": "US",
            "firstName": "Jane",
            "address1": "123 Main Street",
            "postalCode": "10789",
            "locality": "New York",
            "administrativeArea": "NY"
        }
    },
    "paymentInformation": {"card": {
        "expirationYear": "2027",
        "number": "&lt;mc card number&gt;",
        "expirationMonth": "03",
        "typeSelectionIndicator": "1",
        "type": "002"
    }},
    "exp": 1765884772,
    "jti": "Wie23cAKtFnQeIzjx4EQx"
}
```

JavaScript API Reference {#ctp-appendix-js-reference_api_reference}
===================================================================

This reference provides details about the JavaScript API for creating the `Unified Checkout` payment form.

Class: Accept {#ctp-appendix-js-class-accept}
=============================================

Accept
------

**Returns**
Type: Promise.\&lt;Accept\&gt;
**Example**
*Basic Setup*

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt;&lt;/script&gt;
//Note: Script location and integrity value should be sourced from the capture context response clientLibrary and clientLibraryIntegrity values.
&lt;script&gt; Accept('header.payload.signature').then(function(accept) {
// use accept object
});
&lt;/script&gt;
```

Methods
-------

**dispose()**` → {void}`
Dispose of this Accept instance.
**Returns**
Type: void
**unifiedPayments(sidebar)**` → `**{Promise.&lt;UnifiedPayments&gt;}**
Create a Unified Payments integration.

| Name    | Type    | Attributes         | Description                                                                                                                                                                                                                                                                                      |
|:--------|:--------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sidebar | Boolean | \&lt;optional\&gt; | Set the option to `false` to enable embedded functionality of Unified Checkout. This will configure Unified Checkout to place the Payment Entry form inline. If this value is not set, the default is `true` and Unified Checkout will open the Payment Entry form in the sidebar configuration. |
[Parameters]

**Throws:** AcceptError
**Returns:**
Type: Promise.\&lt;UnifiedPayments\&gt;
**Examples**
*Minimal Setup - sidebar*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
```

*Embedded Payment Entry*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments(false))
```

*Error Handling*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
    .then(up =&gt; up.show(showArgs))
    .then(tt =&gt; {
        document.getElementById('transientToken').value = tt;
        document.getElementById("authForm").submit();
    })
    .catch(error =&gt; {
                console.error(error);
                document.getElementById('logo').text = `Checkout error: ${JSON.stringify(error)}. Try again.`;
            });
```

Class: AcceptError {#ctp-appendix-js-class-accept-error}
========================================================

AcceptError
-----------

This class defines how errors are returned by the Unified Checkout JavaScript.

Members
-------

`(static, readonly) Reason Codes - Accept object creation`
Possible errors that can occur during the creation of an Accept object.

| Name                    | Type   | Description                                                                  |
|:------------------------|:-------|:-----------------------------------------------------------------------------|
| CAPTURE_CONTEXT_INVALID | string | Occurs when you pass an invalid JWT.                                         |
| CAPTURE_CONTEXT_EXPIRED | string | Occurs when the JWT you pass has expired.                                    |
| SDK_XHR_ERROR           | string | Occurs when a network error is encountered while attempting to load the SDK. |
[Properties:]

`(static, readonly) Reason Codes - Show Errors`
Possible errors that can occur during the rendering of payment selection list.

| Name                                 | Type   | Description                                                                         |
|:-------------------------------------|:-------|:------------------------------------------------------------------------------------|
| CHECKOUT_ERROR                       | string | Occurs when checkout failed to load.                                                |
| CLICK_TO_PAY_SDK_LOAD_ERROR          | string | Occurs when the `Click to Pay` SDK fails to load.                                   |
| ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR | string | Occurs when the card encryption for SRC enrollment fails to load.                   |
| LAUNCH_SRC_CHECKOUT_ERROR            | string | Occurs when the SRC checkout fails to load.                                         |
| SHOW_LOAD_CONTAINER_SELECTOR         | string | Occurs when a DOM element cannot be located using the supplied CSS Selector string. |
| SHOW_LOAD_ERROR                      | string | Occurs when there is an issue loading the payment iframe.                           |
| SHOW_LOAD_INVALID_CONTAINER          | string | Occurs when an invalid container parameter is supplied.                             |
| SHOW_LOAD_SIDEBAR_OPTIONS            | string | Occurs when an invalid container parameter is supplied when sidebar is selected.    |
| SHOW_PAYMENT_TIMEOUT                 | string | Occurs when an error is encountered during the handling of a payment option.        |
| SHOW_PAYMENT_UNAVAILABLE             | string | Occurs when no payment types can be presented to the customer.                      |
| SHOW_TOKEN_TIMEOUT                   | string | Occurs when the createToken call is unable to proceed.                              |
| SHOW_TOKEN_XHR_ERROR                 | string | Occurs when a network error is encountered while attempting to create a token.      |
| UNIFIED_PAYMENTS_ALREADY_SHOWN       | string | Occurs when you attempt to show a Unified Payments instance multiple times.         |
| UNKNOWN_ERROR                        | string | Occurs when an unknown error has occurred.                                          |
[Properties:]

`(static, readonly) Reason Codes - Unified Payments Errors`
Possible errors that can occur during the creation of a Unified Payments object.

| Name                                | Type   | Description                                                                               |
|:------------------------------------|:-------|:------------------------------------------------------------------------------------------|
| CREATE_TOKEN_TIMEOUT                | string | Occurs when the createToken call times out.                                               |
| CREATE_TOKEN_XHR_ERROR              | string | Occurs when a network error is encountered while attempting to create a token.            |
| UNIFIED_PAYMENTS_PAYMENT_PARAMETERS | string | Occurs when no valid payment parameters exist while initializing button.                  |
| UNIFIED_PAYMENTS_VALIDATION_PARAMS  | string | Occurs when there's an issue with the parameters supplied to UnifiedPayments constructor. |
[Properties:]

`(nullable) correlationId :string`
The correlationId of any underlying API call that resulted in this error.
**Type:** string
`(nullable) details :array`
Additional error-specific information.
**Type:** array
`(nullable) informationLink :string`
A URL link to online documentation for this error.
**Type:** string
`message :string`
A human-readable explanation of the error that has occurred.
**Type:** string
`reason :string`
A reason corresponding to the specific error that has occurred.

Class: UnifiedPayments {#ctp-appendix-js-class-unified-payments}
================================================================

UnifiedPayments
---------------

An instance of this class is returned upon the creation of a Unified Payments integration using accept.unifiedPayments(). Using this object you can add the payment options list to your checkout.

Methods {#ctp-appendix-js-class-unified-payments_section_n1t_k5v_ncc}
---------------------------------------------------------------------

`hide() → {Promise}`
Hide button list.
**Returns:** Type Promise
**Example**
Basic Usage

```
up.hide()
  .then(() =&gt; console.log('Hidden'))
  .catch(err =&gt; console.error(err));
```

`show(optionsopt) → {Promise.&lt;UnifiedPayments~TransientToken}`
Show button list.

| Name             | Type   | Attributes         | Description                                                                                                                  |
|:-----------------|:-------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| options          | object | \&lt;optional\&gt; |                                                                                                                              |
| containers       | object | \&lt;optional\&gt; | CSS selectors to locate containers in which to place various UI elements. If not specified, these will operate in a sidebar. |
| paymentSelection | string | \&lt;optional\&gt; | For showing payment buttons.                                                                                                 |
| paymentScreen    | string | \&lt;optional\&gt; | For the main payment flows.                                                                                                  |
[Parameters]

**Returns:** Type Promise
**Examples**
Basic Usage With Full Sidebar Experience

```
const showArgs = {
            containers: {
                paymentSelection: #buttonPaymentListContainer'
            }
        };

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

All Screens Embedded in Containers

```
const showArgs = {
  containers: {
    paymentSelection: '#buttonPaymentListContainer',
    paymentScreen:  '#embeddedPaymentContainer'
  }
};

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

Type Definitions
----------------

**TransientToken**
The response to a successful customer interaction with Unified Checkout is a transient token. The transient token is a reference to the payment data collected on your behalf. Tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that lasts 15 minutes. This reduces your PCI burden and responsibility and ensures that sensitive information is not exposed to your backend systems.
It is in a JSON Web Token format. The payload of the transient token may contain useful metadata in relation to the stored sensitive info. However , all of this info is safe to use and store on your systems.
The transient token can be used to complete a payment or other services, after which the transient data will be evicted from the token store.
**Type:** string
**Examples**
How to Split the Transient Token

```
const transientToken = 'hhhhhhhhhh.pppppppppp.sssssssssss';

const segments = transientToken.split('.');
const urlBase64Decode = (s) =&gt; atob(s.replace(/_/g, '/').replace(/-/g, '+'));

const header = JSON.parse(urlBase64Decode(segments[0]));
const payload = JSON.parse(urlBase64Decode(segments[1]));
const signature = segments[2];
```

Decoded Body

```
{
  "iss" : "Flex/00",
  "exp" : 1706910242,
  "type" : "gda-0.9.0",
  "iat" : 1706909347,
  "jti" : "1D1I2O2CSTMW3UIXOKEQFI4OQX1L7CMSKDE3LJ8B5DVZ6WBJGKLQ65BD6222D426",
  "content" : {
    "orderInformation" : {
      "billTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "amountDetails" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "shipTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      }
    },
    "paymentInformation" : {
      "card" : {
        "expirationYear" : {
          "value" : "2028"
        },
        "number" : {
          "maskedValue" : "XXXXXXXXXXXX1111",
          "bin" : "411111"
        },
        "securityCode" : { },
        "expirationMonth" : {
          "value" : "06"
        },
        "type" : {
          "value" : "001"
        }
      }
    }
  }
}
```

`Unified Checkout` Configuration {#ctp-configuration-intro}
===========================================================

This section contains information necessary to configure `Unified Checkout` in the `Business Center`:

* [Upload Your Encryption Key](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/uc-upload-encrypt-key-intro.md "")
* [Enable Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/ctp-enable-digital-pay-intro.md "")
* [Manage Permissions](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-manage-permissions-intro.md "")

Upload Your Encryption Key {#uc-upload-encrypt-key-intro}
=========================================================

Payment information can be retrieved from the `Unified Checkout` platform by invoking the Payment Credentials API. This API retrieves all of the data captured by `Unified Checkout`. This information is transmitted in an encrypted format to ensure the security of the payment information while in transit.
You must generate an encryption key pair to retrieve this encrypted payment information, and the public encryption key must uploaded to the `Unified Checkout` system.

Generate a Public Private Key Pair {#uc-generate-keypair}
=========================================================

You must generate a public-private key pair to upload to the `Unified Checkout` system. The public key is uploaded to the `Unified Checkout` platform and is used to encrypt sensitive information in transit. The private key is used to decrypt the sensitive payment information on your server. Only the private key can properly decrypt the payment information.
IMPORTANT You must secure your private decryption key. This key must never be exposed to any external systems or it will risk the integrity of the secure channel.
`Unified Checkout` accepts only keys that meet these requirements:
* Only RSA keys are supported. Elliptical curves are not supported.
* The minimum accepted RSA key size is 2048 bits.
  * RSA keys must be in JWK format. More information on JWK format is available here:
    [rfc7517](https://datatracker.ietf.org/doc/html/rfc7517 "").
* The key ID must be a valid UUID.

Uploading Your Key Pair {#uc-upload-key}
========================================

When you have generated your encryption key pairs, you can upload your key to the `Unified Checkout` platform. Keys can be loaded at any hierarchy that is enabled for them and are used for all child entities that do not have keys loaded. You can upload a key at parent and child levels, but child keys override parent keys.
Follow these steps to upload your key pair:

1. Navigate to Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` configuration page opens.
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-decrypt-pay-details.png/jcr:content/renditions/original)
2. Click Enabled. You can upload your key in the appropriate section.
3. Upload the public encryption key in JWK format, and click Save.
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-upload-pub-key.png/jcr:content/renditions/original)

Enable `Click to Pay` {#ctp_enable_digital_pay_intro}
=====================================================

To enable `Click to Pay` on `Unified Checkout`, you must first register `Click to Pay`. This process sends the appropriate information to the digital payment systems and registers your page with each system.
Enable `Click to Pay` for `Unified Checkout` in the `Business Center`. `Click to Pay` is listed as an available digital payment method offered by `Unified Checkout`.

Click to Pay Customer Authentication {#uc-authentication}
=========================================================

When you enable customer authentication through Click to Pay, you give `Cybersource` permission to send Visa the required authentication information for each transaction.
Click to Pay authentication is only available for Visa branded cards that are tokenized with Click to Pay. If Click to Pay does not authenticate the transaction then you must authenticate it using another authentication method other than Click to Pay, if required.

> IMPORTANT
> American Express and Mastercard card types cannot be authenticated through Click to Pay Drop-In UI . You must use another authentication method for these card types.
> When the customer completes a transaction using a Visa card that is already stored in Click to Pay, authentication can be managed with Click to Pay. When the customer checks out using manual card entry and does not save their card to Click to Pay, the transaction is not processed through Click to Pay and you must complete authentication based on your existing authentication method.

Visa Prerequisites
------------------

Before you can begin customer authentication using Click to Pay, you must meet these requirements:

* The allowPaymentTypes field must include `CLICKTOPAY` in the capture context. For more information, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "").
* Set up Visa customer authentication in the `Business Center`. For information, see [Set Up Customer Authentication for Visa Click to Pay](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication-steps.md "").

Authentication Flow
-------------------

![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-auth-flow-600x680.svg/jcr:content/renditions/original)

Set Up Customer Authentication for Visa Click to Pay {#uc-authentication-steps}
===============================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. These authentication methods are available:

* `3-D Secure`
* FIDO
* Card verification value (CVV)
* One-time password (OTP)

> IMPORTANT
> After you complete these steps, Visa determines which authentication method to use. When Visa determines that they will authenticate, they authenticate each Click to Pay transaction through the appropriate method. This may be a frictionless authentication or the customer may need to provide more information when required by the issuer. This is available only through Visa.
> IMPORTANT
> Visa Click to Pay customer authentication is not the same as ` Payer Authentication ` using the complete mandate. See [Test Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-appendix/uc-appendix-authentication.md "").

1. Log in to the `Business Center`:
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `
   Production URL: ` `<https://businesscenter.cybersource.com>` `
   If you are unable to access this page, contact your sales representative. {#uc-authentication-steps_step-1}
   {#uc-authentication-steps_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)
   If Click to Pay is not enabled, click **On** next to Click to Pay.
   ![Manage Available Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/click-to-pay/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#uc-authentication-steps_step-2}
   {#uc-authentication-steps_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.
   ![Value Added Solutions Page](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Visa the information that is required for authentication. IMPORTANT
   Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.

Authentication Methods {#uc-authentication-methods}
===================================================

`Cybersource` recommends that you review the response in the transient token and compare it with the information below in order to determine the authentication status. For more information about transient tokens, see [Transient Tokens](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-tokens-intro.md ""). This table describes the possible authentication results and the associated processingInformation.commerceIndicator.value field values in the transient token.

|   Authentication Result   |                          `Unified Checkout` Commerce Indicator Value                           |
|---------------------------|------------------------------------------------------------------------------------------------|
| Successful authentication | processingInformation.commerceIndicator.value field value set to `VBV` in the transient token. |
| No authentication         | No commerce indicator in transient token.                                                      |
[Responses for Visa `Click to Pay` Transactions for `Unified Checkout`]

For more information about the authentication methods that are supported for Visa, see this page: <https://developer.visa.com/capabilities/visa-secure-remote-commerce/docs-use-cases>

Authentication Test Cards
-------------------------

Use these test cards to test these authentication methods. Replace the X with a 0.

|     Authentication Method      |   Card Number    | CVV | Expiration Date |
|--------------------------------|------------------|-----|-----------------|
| `3-D Secure`/Passkey Challenge | 43958XXX0449X11X | 509 | 12/25           |
| `3-D Secure`/Passkey Challenge | 439584XXX282X11X | 693 | 12/25           |
| Frictionless                   | 439584XX91X1XX11 | 676 | 12/25           |
| Frictionless                   | 439584XX9119XX11 | 789 | 12/25           |
[Authentication Test Cards]

Test Your `Click to Pay` Configuration {#ctp-testing-intro}
===========================================================

This section contains information about testing your `Click to Pay` configuration.

Test Payment Details {#ctp_reference_test_cards}
================================================

Use these test card numbers to test your `Click to Pay` configuration.
Combine the BIN with the card number when sending to `Click to Pay`.

Visa `Click to Pay` Test Cards
------------------------------

These Visa test cards can be added to your `Click to Pay` wallet.
Replace the X in the card number with 0.
You can manage your Visa `Click to Pay` test cards and account here:

* **Production:** [login](https://src.visa.com/login "")
* **Test:** [login](https://sandbox.src.visa.com/login "")
  To manage Visa test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| 46229431231X2700 | 12/2026         | 938 |
| 46229431231X2718 | 12/2026         | 605 |
| 46229431231X2726 | 12/2026         | 579 |
| 46229431231X2734 | 12/2026         | 141 |
| 46229431231X2742 | 12/2026         | 279 |
| 46229431231X2759 | 12/2026         | 669 |
| 439584XXX449X11X | 12/2025         | 509 |
| 439584XXX282X11X | 12/2025         | 693 |
[Visa Test Card Numbers]

These Visa test card numbers can be used to test ECI05 frictionless authentication. Replace the X in the card number with 4.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| X6229X3123113723 | 12/2027         | 929 |
| X6229X3123113731 | 12/2027         | 217 |
[ECI05 Authentication Test Card Numbers]

These Visa test card numbers can be used to enroll in Passkey Service. Replace the X in the card number with 4.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| X3958X0327800110 | 12/2027         | 832 |
| X3958X0328300110 | 12/2027         | 474 |
[Passkey Enrollment Test Card Numbers]

Mastercard Test Cards
---------------------

Mastercard test cards can be added to your `Click to Pay` wallet. You must retrieve Mastercard test cards from their `Click to Pay` test page: [#test-cards](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "")
Mastercard has different test cards for retrieving tokenized and non-tokenized data. `Cybersource` recommends that you use these test cards as follows:

* Test cards to retrieve PAN data: Use these cards when the customer is completing checkout as a one-time guest and does not have a `Click to Pay` account or want to create one.

* Test cards to retrieve token data: Use these cards for tokenized `Click to Pay` transactions.
  You can manage your Mastercard `Click to Pay` test cards and account here:

* **Live:** [enroll](https://src.mastercard.com/profile/enroll "")

* **SBX:** [enroll](https://sandbox.src.mastercard.com/profile/enroll "")
  To manage Mastercard test cards for customer authentication, contact your implementation consultant or technical account manager.

Supported Countries for `Click to Pay` {#uc_appendix_supp_countries}
====================================================================

`Click to Pay` is supported in these countries:

* Argentina
* Australia
* Austria
* Brazil
* Bulgaria
* Canada
* China
* Colombia
* Costa Rica
* Czech Republic
* Denmark
* Dominican Republic
* Ecuador
* El Salvador
* Finland
* France
* Germany
* Greece
* Honduras
* Hong Kong
* Hungary
* Indonesia
* Ireland
* Italy
* Japan
* Jordan
* Kuwait
* Malaysia
* Mexico
* Netherlands
* New Zealand
* Nicaragua
* Norway
* Panama
* Paraguay
* Peru
* Poland
* Qatar
* Romania
* Saudi Arabia
* Singapore
* Slovakia
* Slovenia
* South Africa
* Spain
* Sweden
* Switzerland
* Thailand
* Ukraine
* United Arab Emirates
* United Kingdom
* United States
* Uruguay
* Vietnam

Supported Locales {#ctp-appendix-languages}
===========================================

The locale field within the capture context request consists of an ISO 639 language code, an underscore (_), and an ISO 3166 region code. The locale controls the language in which the application is rendered. The following locales are supported:

* ar_AE
* bg_BG
* ca_ES
* cs_CZ
* da_DK
* de_AT
* de_DE
* el_GR
* en_AU
* en_CA
* en_GB
* en_IE
* en_NZ
* en_PK
* en_US
* es_AR
* es_CL
* es_CO
* es_ES
* es_MX
* es_PE
* es_US
* fi_FI
* fr_CA
* fr_FR
* he_IL
* hr_HR
* hu_HU
* id_ID
* it_IT
* ja_JP
* km_KH
* ko_KR
* lo_LA
* ms_MY
* nb_NO
* nl_NL
* pl_PL
* pt_BR
* ro_RO
* ru_RU
* sk_SK
* sl_SI
* sv_SE
* th_TH
* tl_PH
* tr_TR
* ur_PK
* vi_VN
* zh_CN
* zh_HK
* zh_MO
* zh_SG
* zh_TW

Processing Authorizations with a Transient Token {#da-processing-payments}
==========================================================================

After you validate the transient token, you can use it in place of the PAN with payment services for 15 minutes. The transient token can be used multiple times within the 15-minute period.

Authorization with a Transient Token {#da-processing-auth-token-task}
=====================================================================

This section provides the minimal set of information required to perform a successful authorization with a transient token that is generated by the Flex API.

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Endpoint {#da-processing-auth-token-task_d19e16}
------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#da-processing-auth-token-task_d19e25}
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#da-processing-auth-token-task_d19e35}
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/up/v1/capture-contexts`
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/up/v1/capture-contexts`

Required Field for an Authorization with a Transient Token {#da-auth-token-required}
====================================================================================

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

REST Interactive Example: Authorization with a Transient Token {#da-auth-token-ex-rest-live}
============================================================================================

```
Payment with Flex Token
```

Live Console URL: [index.html#payments_payments_process-a-payment_samplerequests-dropdown_payment-with-flex-token_liveconsole-tab-request-body](https://developer.cybersource.com/api-reference-assets/index.md#payments_payments_process-a-payment_samplerequests-dropdown_payment-with-flex-token_liveconsole-tab-request-body "")

REST Example: Authorization with a Transient Token {#da-auth-token-ex-rest}
===========================================================================

Request

> IMPORTANT The transient token may already contain information such as billing address and total amount. Any fields included in the request will supersede the information contained in the transient token.

```
{
  "tokenInformation": {
    "transientTokenJwt": "eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJVldBSURPkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRIVZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTuq41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcKLr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ"
  }
}
```

Response to Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6826225725096718703955/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6826225725096718703955"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6826225725096718703955/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "6826225725096718703955",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "102.21",
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
        },
        "customer": {
            "id": "AAE3DD3DED844001E05341588E0AD0D6"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "111111"
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "X",
            "codeRaw": "I1"
        }
    },
    "reconciliationId": "68450467YGMSJY18",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-04-27T19:09:32Z"
    }
}
```

Authorization and Creating TMS Tokens with a Transient Token {#da-processing-auth-token-create-tms-task}
========================================================================================================

This section provides the minimal information required in order to perform a successful authorization and create `TMS` tokens (customer, payment instrument, and shipping address) with a transient token.

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Endpoint {#da-processing-auth-token-create-tms-task_d19e16}
-----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#da-processing-auth-token-create-tms-task_d19e25}
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#da-processing-auth-token-create-tms-task_d19e35}
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/up/v1/capture-contexts`
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/up/v1/capture-contexts`

Required Fields for an Authorization and Creating TMS Tokens with a Transient Token {#da-auth-token-create-tms-required}
========================================================================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.smartpayfuse.barclaycard/docs/barclays/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")orderInformation.shipTo.locality
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info_/processing-info-action-list.md "")
:
Set this field to `TOKEN_CREATE`.

[processingInformation.actionTokenTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-token-types.md "")
:
Set to one of these values:

    * `customer`
    * `paymentInstrument`
    * `shippingAddress`

[tokenInformation.transientTokenJwt](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")[tokenInformation.transientTokenJwt](https://developer.smartpayfuse.barclaycard/docs/barclays/en-us/api-fields/reference/all/rest/api-fields/token-info-aa/token-info-transient-token-jwt.md "")
:

REST Interactive Example: Authorization and Creating TMS Tokens with a Transient Token {#da-auth-token-create-tms-ex-rest-live}
===============================================================================================================================

```
Payment with Flex Token(Create Permanent TMS token)
```

Live Console URL: [index.html#payments_payments_process-a-payment_samplerequests-dropdown_payment-with-flex-token-create-permanent-tms-token_liveconsole-tab-request-body](https://developer.cybersource.com/api-reference-assets/index.md#payments_payments_process-a-payment_samplerequests-dropdown_payment-with-flex-token-create-permanent-tms-token_liveconsole-tab-request-body "")

REST Example: Authorization and Creating TMS Tokens with a Transient Token {#da-auth-token-create-tms-ex-rest}
==============================================================================================================

Request

```keyword
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "processingInformation": {
    "actionList": [
      "TOKEN_CREATE"
    ],
    "actionTokenTypes": [
      "customer",
      "paymentInstrument",
      "shippingAddress"
    ]
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@cybs.com",
      "phoneNumber": "4158880000"
    },
    "shipTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1 Market St",
      "locality": "san francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US"
    }
  },
  "tokenInformation": {
    "transientTokenJwt": "eyJraWQiOiIwMFN2SWFHSWZ5YXc4OTdyRGVHOWVGZE9ES2FDS2MxcSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzAwIiwiZXhwIjoxNjE0NzkyNTQ0LCJ0eXBlIjoiYXBpLTAuMS4wIiwiaWF0IjoxNjE0NzkxNjQ0LCJqdGkiOiIxRDBWMzFQMUtMRTNXN1NWSkJZVE04VUcxWE0yS0lPRUhJVldBSURPkhLNjJJSFQxUVE1NjAzRkM3NjA2MDlDIn0.FrN1ytYcpQkn8TtafyFZnJ3dV3uu1XecDJ4TRIVZN-jpNbamcluAKVZ1zfdhbkrB6aNVWECSvjZrbEhDKCkHCG8IjChzl7Kg642RWteLkWz3oiofgQqFfzTuq41sDhlIqB-UatveU_2ukPxLYl87EX9ytpx4zCJVmj6zGqdNP3q35Q5y59cuLQYxhRLk7WVx9BUgW85tl2OHaajEc25tS1FwH3jDOfjAC8mu2MEk-Ew0-ukZ70Ce7Zaq4cibg_UTRx7_S2c4IUmRFS3wikS1Vm5bpvcKLr9k_8b9YnddIzp0p0JOCjXC_nuofQT7_x_-CQayx2czE0kD53HeNYC5hQ"
  }
}
```

Response

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/6826220442936119603954/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/6826220442936119603954"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/6826220442936119603954/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "TC50171_3"
    },
    "id": "6826220442936119603954",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "102.21",
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
        "terminalId": "111111"
    },
    "processorInformation": {
        "approvalCode": "888888",
        "networkTransactionId": "123456789619999",
        "transactionId": "123456789619999",
        "responseCode": "100",
        "avs": {
            "code": "X",
            "codeRaw": "I1"
        }
    },
    "reconciliationId": "68449782YGMSJXND",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2023-04-27T19:00:44Z",
    "tokenInformation": {
        "instrumentidentifierNew": false,
        "instrumentIdentifier": {
            "state": "ACTIVE",
            "id": "7010000000016241111"
        },
        "shippingAddress": {
            "id": "FA56F3248492C901E053A2598D0A99E3"
        },
        "paymentInstrument": {
            "id": "FA56E8725B06A553E053A2598D0A2105"
        },
        "customer": {
            "id": "FA56DA959B6AC8FBE053A2598D0AD183"
        }
    }
}
```

`Flex API` {#da-flex-api-intro}
===============================

The `Flex API` enables merchants to securely accept customer payment information captured within a server-side application using a set of APIs. These APIs protect your customer's primary account number (PAN), card verification number (CVN), and other payment information by embedding it within a transient token. This allows payment data to be stored and transported and complies with the Payment Card Industry Data Security Standard (PCI DSS) policies and procedures. These transient tokens can be validated by the receiver to ensure the data integrity and protect against data injection attacks.

> WARNING
> ` Flex API ` is intended for server-side applications only. Do not use the ` Flex API ` in client-side applications. To add secure payments directly into client-side code, use ` Unified Checkout `.
> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

How It Works
------------

Follow these steps to capture payments using the `Flex API`:

1. Establish a payment session with a predefined customer context.
2. Validate the JSON Web Token.
3. Populate the JSON Web Token with customer information.

Customer Context
----------------

An important benefit of the `Flex API` is managing Personal Identifiable Information (PII). You can set up your customer context to include all PII associated with transactions, protecting this information from third parties.

JSON Web Tokens {#flex-api-2-jwts}
==================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```
* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```
* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#flex-api-2-jwts_d12e34}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

Payment Credentials API {#uc-token-get-pymnt-credentials}
=========================================================

This section contains the information you need to retrieve the full payment credentials collected by the `Unified Checkout` tool using the payment credentials API. The payment information is returned in a redundantly signed and encrypted payment object. It uses the JSON Web Tokens (JWTs) as the data standard for communicating this sensitive data.

> IMPORTANT
> Payment information returned by the ` payment-credentials ` endpoint will contain Personal Identifiable Information (PII). Retrieving this sensitive information requires your system to comply with PCI security standards. For more information on PCI security standards, see: <https://www.pcisecuritystandards.org/>
> The response is returned using a JWE data object that is encrypted with your public key created during the `Unified Checkout` tool's integration. For more information, see [Upload Your Encryption Key](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-configuration-intro/uc-upload-encrypt-key-intro.md "").
> To decrypt the JWE response, use your private key created during the `Unified Checkout` tool's integration. The decrypted content is a JWS data object containing a JSON payload. This payload can be validated with the `Unified Checkout` public signature key.
> IMPORTANT
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Returned Credentials
--------------------

A payment account number (PAN) or network token is returned on your request depending on your payment method and `Click to Pay` account status:

|     `Click to Pay` Account Status      | American Express |  Mastercard   |     Visa      |
|----------------------------------------|------------------|---------------|---------------|
| New card not saved in `Click to Pay`   | PAN              | PAN           | PAN           |
| New card saved in `Click to Pay`       | PAN              | Network Token | Network Token |
| Existing card stored in `Click to Pay` | PAN              | Network Token | Network Token |
[Payment Credentials Returned by Card Type and `Click to Pay` Account Status]

When you retrieve PAN information from the Payment Credentials API, the response includes the PAN, card expiration date, and the card verification value (CVV). When you retrieve network token information, the response includes the network token and network token cryptogram.

> IMPORTANT Visa and Mastercard always attempt to provision a network token. When a network token is not provisioned, the default payment method is the PAN. When there is a PAN transaction, the PAN is not stored in the consumers wallet and it is treated as a single transaction.
> Network tokens are generated in the wallet of the `Click to Pay` token requestor ID (TRID). When tokenization is successful, Visa attempts to complete authentication during the `Click to Pay` experience. For information on authentication, see [Click to Pay Customer Authentication](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/uc-intro/uc-configuration-intro/uc-enable-digital-pay-intro/uc-enable-digital-pay-ctp/uc-authentication.md "").
> You must meet these requirements for tokenization to be successfully configured for your merchant ID (MID):

* `Click to Pay` is enabled as a digital payment in the `Business Center`.
* The transacting MID is configured for tokenization with `Click to Pay`. Contact your Implementation Consultant or Technical Account Manager to configure tokenization with `Click to Pay`.
* The allowedPaymentTypes field value is set to `CLICKTOPAY` in the capture context. For information on the capture context, see [Capture Context API](/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/ctp-intro/ctp-setup-capture-context.md "").

Endpoint {#uc-token-get-pymnt-credentials_d9e632}
-------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d9e639}
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d9e651}
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*
The *{ReferenceID}* is the reference ID returned in the `id` field when you created the payment credentials.

`Click to Pay` UI Guidelines {#uc_ui_screens}
=============================================

This section includes examples of the interfaces that your customers can expect when completing a payment with `Click to Pay`.
Completing a payment with `Unified Checkout` requires the customer to navigate through a sequence of interfaces:

#### Figure: {#uc_ui_screens_fig-uc-ui-ctp}

`Click to Pay` UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ctp-865x480.svg/jcr:content/renditions/original)
