`Unified Checkout` Developer Guide {#uc-about-guide}
====================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This document is written for merchants who want to enable `Unified Checkout` so that they can accept payments on their e-commerce page. Merchants use the `Unified Checkout` JavaScript SDK to place a digital button widget on their e-commerce site, allowing `Cybersource` to capture payment data on their behalf.

Conventions
:
This statement is used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#uc-doc-revisions}
=====================================================

26.07.01 {#uc-doc-revisions_section_fvr_nyv_ljc}
------------------------------------------------

Payment Methods
:
Updated the list of supported card types for Apple Pay. See [Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-card.md "").

Integration Methods
:
Added information about the `Unified Checkout` integration methods. See [Integration Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro.md "").

Configuration
:
Updated the steps for setting up a webhooks subscriptions. See [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Sessions API
:
Added information about values greater than or equal to 0.00 in the data.orderInformation.amountDetails.totalAmount field in the capture context. See [Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features.md "").
:
Added information about passkey authentication. See [completeMandate.consumerAuthentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features/uc-cc-complete-mandate/uc-cc-complete-auth.md "").
:
Added information about the removal of the contact details page during `Click to Pay` autolookup. See [Email Autolookup](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features/uc-cc-email-autolookup.md "").

Test Your Configuration
:
Added support for testing Mastercard cards. See [Relay and Mastercard Click to Pay Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-relay-ctp.md "") and [Test Cards for Authentication by Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-auth-ctp.md "").

Appendix
:
Added support for these locales:

    * `ar_JO`
    * `ar_QA`
    * `en_AE`
    * `en_LK`
    * `en_QA`
    * `si_LK`
    * `ta_LK`

    {#uc-doc-revisions_ul_ncz_5xv_ljc}Added information about right-to-left Arabic language support. See [Supported Locales](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-languages.md "").

{#uc-doc-revisions_dl_arg_zyv_ljc}

26.05.01 {#uc-doc-revisions_section_ebl_njy_hjc}
------------------------------------------------

Payment Methods
:
Added information about expanded regional support Tink Pay By Bank. See [Tink Pay By Bank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-tink.md "").

26.04.01 {#uc-doc-revisions_section_jzm_k4c_1jc}
------------------------------------------------

Payment Methods
:
Added information about using Tink Pay By Bank in the UK. See [Tink Pay By Bank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-tink.md "").
:
Added support for PayPal and Venmo. See [PayPal](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets/uc-pay-methods-bnpl-paypal.md "") and [Venmo](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets/uc-pay-methods-obt-venmo.md "").

Test Your Configuration
:
Updated the Relay `Click to Pay` test card numbers. See [Relay and Mastercard Click to Pay Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-relay-ctp.md "").

26.03.01
--------

Appendix
:
Added information about how to update your integration to Version 1. See [Update to Unified Checkout Version 1](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-v1-migration-intro.md "").
:
Added information about security recommendations and PCI compliance. See [Security Recommendations](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-security-recs.md "").
:

Capture Context
:
Added information to the capture context section for Version 1. See [Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features.md "").
:
Added support for client version `1.0`. See [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").
:
Added information about semantic versioning. See [Versioning](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-versioning.md "").
:
Added endpoints for Saudi Arabia. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "") and [Validating the Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-validate-capture-context-intro.md "")

Client-Side Setup
:
Updated the JavaScript examples and reference for Version 1. See [Loading the JavaScript Library](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro.md "") and [JavaScript API Reference](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix-js-reference-v1.md "").

Merchant Experience
:
Added support for the merchant experience in the `Business Center`. See [Configure the Unified Checkout Merchant Experience](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc.md "").
:
Added information about processing payments with `Unified Checkout`. See [Process Payments with Unified Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-pay-processing-intro.md "").

Payment Details
:
Updated the endpoint for retrieving payment details and added endpoints for Saudi Arabia. See [Payment Details API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md "").

Payment Methods
:
Added support for paying with tokens. See [Pay with Token](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-pay-tkn.md "").

Quick Start
:
Added a quick-start section. See [Unified Checkout Quick Start](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro.md "").

Test Your Configuration
:
Added information about handling errors. See [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").
:
Updated the reason codes to include Version 1 reason codes. See [Reason Codes](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-v1-reason-codes.md "").

Transient Tokens
:
Added endpoints for Saudi Arabia. See [Authorizations with a Transient Token](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro/uc-auth-tokens.md "").

25.12.01
--------

Server-Side Set Up
:
Added information about supported browsers. See [Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-intro.md "").

Capture Context
:
Added support for up to clientVersion `0.34`. See [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").

Transient Tokens
:
Added information about Cartes Bancaires dual-branded cards. See [Dual-Branded Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro/dual-co-brand-card-support.md "").

Payment Methods
:
Added information about Konbini. See [Konbini](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-ppr/uc-pay-methods-ppr-konbini.md "").

Test Your `Unified Checkout` Configuration
:
Added test payment information for testing Relay `Click to Pay` authentication within the `Click to Pay` flow and outside of the flow. See [Test Your Configuration](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards.md "").

25.11.02
--------

Capture Context
:
Added a complete capture context request example with all possible fields. See [Example: Unified Checkout Complete Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-appendix-complete-cc-ex.md "").
:
Updated the capture context examples for clientVersion `0.31`. See [Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-intro.md "").

Appendix
:
Added information about testing your authentication method. See [Test Authentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-authentication.md "").
:
Added information about customizing the `Click to Pay` UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-appendix-ui-ux.md "").

25.11.01
--------

Capture Context
:
Updated the list of allowed card networks. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").

Payment Methods
:
Added information about Bancontact, Dragonpay and MyBank. See these topics:

    * [Bancontact](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-bancontact.md "")
    * [DragonPay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-dragonpay.md "")
    * [MyBank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-mybank.md "")

25.10.02
--------

Capture Context
:
Added support for clientVersion `0.30`. See [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").

Payment Methods
:
Added information about Tink Pay By Bank. See [Tink Pay By Bank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-tink.md "").

25.10.01
--------

`Unified Checkout` Appendix
:
Added missing reason codes. See [Reason Codes](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-v1-reason-codes.md "").
:
Updated the clientVersion field value to `0.30` in examples.
:
Added Pakistan locales. See [Supported Locales](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-languages.md "").

Payment Methods
:
Added information about handling responses for Online Bank Transfers and Buy Now, Pay Later. See [Handle Responses for Online Bank Transfers](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-handle-response.md "") and [Handle Responses for Buy Now, Pay Later](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-bnpl/uc-pay-methods-bnpl-handle-response.md "").

25.08.02
--------

Added more information about JSON Web Tokens. See [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").

25.08.01
--------

Client-Side Setup
:
Added information for creating a trigger. See [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

Capture Context
:
Added PayPak as a payment method. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").
:
Added information for client version 0.28. See [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").

Payment Methods
:
Added information for alternative payment methods. See [Payment Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro.md "").

25.05.01
--------

Capture Context
:
Added information for the complete mandate. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").
:
Added information on the available features and the fields specific to each feature to the Capture Context API. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").
:
Added Paze to the list of allowed payment types. See [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").
:
Added capture context validation. See [Validating the Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-validate-capture-context-intro.md "").

`Unified Checkout` Appendix
:
Added a client version history and the features included in each version. See [Client Version History](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-capture-context-versions.md "").
:
Updated the list of supported languages. See [Supported Locales](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-languages.md "").

Client-Side Set Up
:
Updated the examples for loading the JavaScript library:

    * [JavaScript Example: Initializing the SDK](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-library-example.md "")
    * [JavaScript Example: Displaying the Button List](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-button-example.md "")
    * [JavaScript Example: Processing a Payment](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").

`Click to Pay`
:
Updated the list of supported countries to include Bulgaria, Greece, Japan, Romania, Slovenia, Thailand, and Vietnam. See [Supported Countries for Digital Payments](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-supp-countries.md "").

Introduction to `Unified Checkout` {#uc-intro}
==============================================

`Unified Checkout` provides a single interface with which you can accept numerous types of card, digital, and alternative payments. `Unified Checkout` calls other follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `Token Management Service` (`TMS`).  
`Unified Checkout` consists of a server-side component and a client-side JavaScript library.  
The server-side component authenticates your merchant identity and instructs the system to act within your payment environment. The response contains limited-use public keys. The keys are for end-to-end encryption and contain merchant-specific payment information that drives the interaction of the application. The client-side JavaScript library dynamically and securely places digital payment options onto your e-commerce page.  
The provided JavaScript library enables you to securely accept many payment options within your e-commerce environment. `Unified Checkout` can be embedded seamlessly into your existing webpage, simplifying payment acceptance.  
When a customer selects a payment method from the button widget, `Unified Checkout` handles all interactions with the payment method that was chosen. `Unified Checkout` is also able to orchestrate requests for to follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `TMS` before it provides a response to your e-commerce system.  
The figure below shows `Unified Checkout` with customer checkout payment options.

#### Figure: {#uc-intro_fig-1}

Button Widget ![Example of the button widget interface and flow with various payment
options.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/button-widget-flow-865x475.svg/jcr:content/renditions/original)  
For examples of different payment method UIs through `Unified Checkout`, see these topics:

* [Click to Pay UI](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-ui-ctp.md "")
* [Google Pay UI](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay/uc-ui-googlepay.md "")
* [Pay with eCheck/ACH Service UI](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-echeck/uc-ui-echeck.md "")
* [Paze UI](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-paze/uc-ui-paze.md "")
* [Apple Pay UI](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay/uc-ui-applepay.md "")
  .

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Key Features
------------

![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-intro-600x100.svg/jcr:content/renditions/original)
* **Low-code integration**: You can use as few as three lines of JavaScript to accept payments, as well as add or remove payment methods through portal configuration without changing your integration code.
* **PCI SAQ-A compliant**: Payment data never touches your systems.
* **Fully customizable**: You can match the payment experience to your brand with theming, fonts, and layout options. Embed inline or display as a sidebar overlay.
* **Service orchestration** : You can use `Decision Manager`, `Payer Authentication` (`3-D Secure`), and `Token Management Service` (`TMS`) throughout the session.

`Unified Checkout` Quick Start {#uc-qs-intro}
=============================================

`Unified Checkout` is a powerful and flexible payment solution that simplifies the integration process and enhances the customer checkout experience. This guide will help you get up and running with `Unified Checkout`.

Key Features {#uc-qs-intro_section_tkt_rgg_gfc}
-----------------------------------------------

* Seamless integration with your existing e-commerce platform.
* Support for multiple payment methods.
* Customizable checkout flow.
* Enhanced security features.
* Responsive design for mobile and desktop.
  {#uc-qs-intro_ul_ukt_rgg_gfc}

Benefits {#uc-qs-intro_section_vkt_rgg_gfc}
-------------------------------------------

* Simplified integration process.
* Improved conversion rates.
* Reduced cart abandonment.
* Enhanced customer experience.
* Compliance with industry security standards.
  {#uc-qs-intro_ul_wkt_rgg_gfc} This graphic provides an overview of the steps you must follow to get set up with `Unified Checkout`:

#### Figure:

`Unified Checkout`Integration Overview ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-quickstart-600x110.svg/jcr:content/renditions/original)

Step 1: Enable `Unified Checkout` {#uc-qsg-step1}
=================================================

To begin using `Unified Checkout`, you must first ensure that your merchant ID (MID) is configured to use the service and that any payment methods you intend to use are properly set up.

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc-qsg-step1_d15e36}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc-qsg-step1_d15e45}  
   If you are unable to access this page, contact your sales representative. {#uc-qsg-step1_d15e26}
   {#uc-qsg-step1_d15e26}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original) {#uc-qsg-step1_d15e56}
   {#uc-qsg-step1_d15e56}

3. The `Unified Checkout` configuration interface provides complete low-code control over your checkout experience by using dedicated configuration screens accessible through the `Business Center`. The configuration interface is organized into separate screens, each accessible from the *My customer experience* page. Configure each of these components of the checkout experience:

   * **Payment Options** : Add, remove, and arrange payment methods. For information about configuring payment methods, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").
   * **Look \& feel** : Configure visual appearance and branding. For information about configuring the look and feel, see [Customize the Unified Checkout Look and Feel](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-look-and-feel.md "").
   * **Customer information and payment flow** : Control data collection and manage payment processing service. For information about configuring customer data, see [Configure Customer Data and Payment Flow](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-customer-data.md "").
     {#uc-qsg-step1_d15e94}
     {#uc-qsg-step1_d15e94}

{#uc-qsg-step1_steps_o34_43h_gfc}

#### AFTER COMPLETING THE TASK

Proceed to [Step 2: Set Up the Server-Side Component](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro/uc-qsg-step2.md "").

Step 2: Set Up the Server-Side Component {#uc-qsg-step2}
========================================================

To initialize `Unified Checkout` within your webpage, you need to set up the server-side component. This task involves generating a capture context. A capture context is a signed JSON Web Token (JWT) that contains your merchant configuration, one-time encryption keys, and payment parameters.  
Follow these steps to make a server-to-server call to the Sessions API to authenticate your merchant credentials and establish how the `Unified Checkout` front-end components will function:

1. Implement a server-to-server call to the Sessions API.

   #### ADDITIONAL INFORMATION

   This call should include parameters that define how `Unified Checkout` performs.

2. Handle the response from the Sessions API.

   #### ADDITIONAL INFORMATION

   The response will contain:

   * A transaction-specific public key for securing the transaction in the customer's browser.
   * An authenticated context description package that manages the payment experience on the client side, including available payment options, interface styling, and payment methods.
3. Store and manage the JSON Web Token (JWT) object, referred to as the *capture context*.  
   This JWT contains all the functions compiled from the Sessions API response:

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

   The targetOrigins array must include every origin that will host the SDK. The response JWT is passed to the client-side library.  
   This capture context contains only the minimum required fields. For information about the components of the capture context and how to create one using the Sessions API, see [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md ""). For a complete capture context with all available fields, see [Example: Unified Checkout Complete Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-appendix-complete-cc-ex.md "").

#### AFTER COMPLETING THE TASK

Proceed to [Step 3: Set Up the Client-Side Component](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro/uc-qsg-step3.md "").

Step 3: Set Up the Client-Side Component {#uc-qsg-step3}
========================================================

To add the payment interface to your e-commerce site, you need to set up the client-side component using the `Unified Checkout` JavaScript library. This setup involves two primary components:

* The button widget, which lists available payment methods for the customer.
* The payment acceptance page, which captures payment information from the cardholder. This can be integrated with your webpage or added as a sidebar.

This example shows a complete client-side integration:

```
async function launchCheckout() {
  try {
    const client = await VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout();
    const result = await checkout.mount('#payment-buttons');

    // result contains the completed payment result JWT
    // Send result to your server for verification
    sendToServer(result);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

Follow these steps to create the client-side integration:

1. Load the `Unified Checkout` JavaScript library:

   #### ADDITIONAL INFORMATION

   ```keyword
   &lt;script src="https://apitest.cybersource.com/uc/v1/assets/1.0.0/UnifiedCheckout.js"&gt;&lt;/script&gt;
   ```

   Replace the domain with the production URL for live environments:

   * **Test** : `https://apitest.cybersource.com`
   * **Production** : `https://api.cybersource.com`

   You must include the library in your webpage's HTML.

2. Initialize the SDK by calling `VAS.UnifiedCheckout()`. This returns a client instance:

   #### ADDITIONAL INFORMATION

   ```
   const client = await VAS.UnifiedCheckout(sessionJWT);
   ```

   Use the JWT obtained from the server-side setup in [Step 2: Set Up the Server-Side Component](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro/uc-qsg-step2.md "").  
   Initialization validates the JWT signature, checks that the current page origin matches `targetOrigins`, and prepares the SDK for use. If the JWT is invalid or expired, a `UnifiedCheckoutError` is returned.

3. Create a checkout to render a list of available payment methods and handles the payment flow:

   #### ADDITIONAL INFORMATION

   ```
   const checkout = await client.createCheckout();
   ```

   When you include `autoProcessing` and set it to `true`, `mount()` returns the completed payment result:

   ```
   // Explicit auto-processing
   const checkout = await client.createCheckout({ autoProcessing: true });
   ```

   When you include it and set it to `false`, `mount()` returns a transient token that you pass to `checkout.complete()`:

   ```
   // Explicit manual processing
   const checkout = await client.createCheckout({ autoProcessing: false });
   ```

   The default value of `autoProcessing` us `true` when a completeMandate is included in the session.

4. Mount the checkout by calling `mount()`. This attaches the payment UI to your page. The argument determines the display mode:

   **Sidebar Mode**
   :
   The payment screen appears as an overlay sidebar. Pass a CSS selector for the payment button list, or omit it entirely:

       ```
       // Full sidebar — buttons and payment screen both in sidebar
       const result = await checkout.mount();

       // Buttons embedded, payment screen in sidebar
       const result = await checkout.mount('#payment-buttons');
       ```

   **Embedded Mode**
   :
   Both the button list and payment screen render inline within your page layout:

       ```
       const result = await checkout.mount({
         paymentSelection: '#payment-buttons',
         paymentScreen: '#payment-form'
       });
       ```

   **Mount Result**
   :
   When `autoProcessing` is enabled, `mount()` resolves with the completed payment result JWT once the customer finishes the payment flow.

       When `autoProcessing` is disabled, `mount()` resolves with a transient token JWT. You then call checkout.complete() to finish the payment:

       ```
       const checkout = await client.createCheckout({ autoProcessing: false });
       const transientToken = await checkout.mount('#payment-buttons');

       // Later, complete the payment
       const result = await checkout.complete(transientToken);
       ```

   **Unmount**
   :
   You can remove the payment UI from the page without destroying the checkout:

       ```
       checkout.unmount();

       // Later, mount again
       const result = await checkout.mount('#payment-buttons');
       ```

#### AFTER COMPLETING THE TASK

For more information about setting up the client side, see [Client-Side Set Up](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro.md ""). For information about handling errors on the client side, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md ""). Proceed to [Step 4: Configure Unified Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro/uc-qsg-step4.md "").

Step 4: Configure Unified Checkout {#uc-qsg-step4}
==================================================

Proper configuration ensures that your checkout process aligns with your business needs and provides a smooth experience for your customers. You can configure the checkout process in the `Business Center`:

1. Select and configure the payment methods you support:

   1. Log in to the `Business Center` and navigate to the `Unified Checkout` configuration section.

   2. Select the payment methods you want to use:

      * Credit and debit cards. See [Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-card.md "").
      * eCheck/ACH Services. See [eCheck/ACH Service](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-echeck.md "").
      * Digital wallets such as Apple Pay, `Click to Pay`, and Google Pay. See [Digital Wallets](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets.md "").
      * Alternative payment methods. See [Alternative Payment Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro.md "").

      {#uc-qsg-step4_choices_qy4_nfh_gfc}

      > IMPORTANT  
      > You must configure the payment methods you want to use for each transacting MID.  
      > For information about which payment methods are supported on ` Unified Checkout `, see [Payment Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro.md "").

   3. Configure the settings for each selected payment method.

   {#uc-qsg-step4_substeps_gv2_pgh_gfc}  
   For information about configuring `Unified Checkout` in the `Business Center`, see [Configure the Unified Checkout Merchant Experience](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc.md "").

#### AFTER COMPLETING THE TASK

Proceed to [Step 5: Test Your Unified Checkout Integration](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-qs-intro/uc-qsg-step5.md "").

Step 5: Test Your Unified Checkout Integration {#uc-qsg-step5}
==============================================================

After configuring `Unified Checkout`, it's crucial to thoroughly test your integration to ensure it works correctly and provides a smooth checkout experience for your customers. This section outlines the steps to test your `Unified Checkout` integration.

1. Set up your test environment:
   1. Log in to the `Business Center` account using your test credentials.
   2. Switch to the test environment if not already in test mode.
   3. Set up a test website or application that integrates `Unified Checkout`.
2. Use test card numbers to simulate different payment scenarios.  
   For more test payment data, see [Unified Checkout Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-uc.md "").
3. Test different payment scenarios:
   * Successful transactions
   * Declined transactions
   * `3-D Secure` authentication, if applicable
   * Different card brands
   * Digital wallet payments, if configured
     {#uc-qsg-step5_ul_yj5_jwm_gfc}
4. Verify that the capture context object that you get from the sessions API is correct and that your integration can handle tokens.  
   Ensure that your integration correctly handles the capture context and transient tokens throughout the payment process.
5. Test error handling and edge cases.  
   Simulate various error scenarios to ensure your integration gracefully handles and reports errors to the user.
6. Verify webhook notifications, if configured.  
   If you set up webhook notifications, ensure that your system correctly receives and processes them for various transaction events. For information about configuring your webhook notifications, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

#### AFTER COMPLETING THE TASK

After completing these testing steps, you should have confidence in your integration. Remember to test in both the test and production environments before going live.

`Unified Checkout` Flow {#uc-getting-started-integration-flow}
==============================================================

To integrate `Unified Checkout` into your platform, you must follow several integration steps. This section gives a high-level overview of how to integrate and launch `Unified Checkout` on your webpage and process a transaction. You can find the detailed specifications of the APIs later in this document. Information that is captured by `Unified Checkout`, including the billing and shipping address, can be retrieved using the Payment Details API.  
The figure below shows the `Unified Checkout` payment flow using the Sessions API to generate the capture context:

#### Figure: {#uc-getting-started-integration-flow_fig_uc-payment-flow}

`Unified Checkout` Payment Flow  
![Diagram that shows the sequence and flow of a Unified Checkout payment.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-srvorch-authdm-600x680.svg/jcr:content/renditions/original) For more information on the specific APIs referenced, see these topics:

* [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md ""): This generates the capture context and determines what fields are displayed to the customer in the UI during checkout.
* [Payment Details API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md ""): This API can be used to retrieve personally identifiable information that is associated with a `Unified Checkout` transient token, such as the cardholder name and billing and shipping details, without retrieving payment credentials.

Payment Methods {#uc-pay-methods-intro}
=======================================

This section describes the payment methods you can use in your `Unified Checkout` integration. After you successfully integrate one payment method, you can add another from the same category with minimal adjustments to your existing configuration.  
These payment methods are available:

* [Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-card.md "")
* [eCheck/ACH Service](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-echeck.md "")
* [Apple Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay.md "")
* [Google Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay.md "")
* [Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp.md "")
* [Paze](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-paze.md "")
* [Online Bank Transfers](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt.md "")
* [Buy Now, Pay Later](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-bnpl.md "")
* [Post-Pay Reference Payments](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-ppr.md "")
* [PayPal](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets/uc-pay-methods-bnpl-paypal.md "")
* [Venmo](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets/uc-pay-methods-obt-venmo.md "")

Cards {#uc-pay-methods-card}
============================

`Unified Checkout` accepts multiple card types including global networks such as Relay, Mastercard, and American Express. `Unified Checkout` also accepts local schemes such as Cartes Bancaires in France, EFTPOS in Australia, and PayPak in Pakistan.

Card Support
------------

Support for card brands varies based on the payment method for these services:

* Payments
* `Decision Manager`
* `Payer Authentication`  
  This table shows which card types are accepted for each payment method and which region:

|      Region       |    Card Brand    |                                                Manual Card Entry                                                |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                   Google Pay                                                    |                                                      Paze                                                       |
|-------------------|------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | EFTPOS           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | JCB              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Meeza            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | American Express | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Diners Club      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Mastercard       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Relay             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | Carnet           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | ELO              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | Discover         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | JCrew            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
[Card Brand by Region and Payment Method]

This table shows which card types are supported for each complete mandate feature by region.

|      Region       |    Card Brand    |                                                  Authorization                                                  |                                             `Payer Authentication`                                              |                                               `Decision Manager`                                                |                                   Token Create by `Token Management Service`                                    |
|-------------------|------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | EFTPOS           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | JCB              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| CEMEA             | Meeza            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | American Express | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Diners Club      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Mastercard       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Relay             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | Carnet           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | ELO              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | Discover         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | JCrew            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Card Support for the Complete Mandate]

Pay with Token {#uc_pay_methods_pay_tkn}
========================================

You can use `Unified Checkout` to pass through a single token ID to be shown within the `Unified Checkout` UI. To display a payment instrument in the `Unified Checkout` UI, you must include `TMS_TOKEN` as an allowed payment type in the allowedPaymentTypes field object and the details of the `Token Management Service` (`TMS`) token in the paymentConfigurations field object in the capture context request:

```
{
"allowedPaymentTypes": [

    "PANENTRY",
    "TMS_TOKEN"
 ]
},
"paymentConfigurations": {
    "TMS_TOKEN": {
      "instrumentIdentifiers": [
        {
          "id": "4B1BCB328D52ED86E063AF598E0A99A5"
        }
      ]
    }
}
```

This is an example UI with a payment instrument:

#### Figure:

Pay with Token in `Unified Checkout` UI ![Image showing the Unified Checkout UI that includes a payment
instrument, card payment, Apple Pay, and Google Pay.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-pay-with-token-733x1507.png/jcr:content/renditions/original)  
You can use these token types to pay with a token in `Unified Checkout`:

Customer Tokens
:
When you include the customer token, your UI displays the default payment instrument that is inked to a customer. To display a customer token, you must include the paymentConfigurations.TMS_TOKEN.customer.id field in your Sessions API request.

    > IMPORTANT
    > When you include a customer token ID here with tokenCreate for a paymentInstrument or instrumentIdentifier , the complete mandate creates a new payment instrument or instrument identifier within the level of the customer token that you provide.

    ```
    {
    "allowedPaymentTypes": [
        "PANENTRY",
        "TMS_TOKEN"
     ]
    },
    "paymentConfigurations": {

        "TMS_TOKEN": {
          "customer": [
            {
              "id": "4B1BCB328D52ED86E063AF598E0A99A5"
            }
          ]
        }
    }
    ```

Instrument Identifier Tokens
:
When you include an instrument identifier token, your UI displays the payment credential that is associated with the specified instrument identifier. To display an instrument identifier token, you must include the paymentConfigurations.TMS_TOKEN.instrumentIdentifiers.id field in your Sessions API request.

    ```
    {
    "allowedPaymentTypes": [
        "PANENTRY",
        "TMS_TOKEN"
     ]
    },
    "paymentConfigurations": {

        "TMS_TOKEN": {
          "instrumentIdentifiers": [
            {
              "id": "4B1BCB328D52ED86E063AF598E0A99A5"
            }
          ]
        }
    }
    ```

Payment Instruments
:
When you include a payment instrument, your UI displays the payment instrument that is associated with the specified payment instrument token identifier. To display a payment instrument, you must include the paymentConfigurations.TMS_TOKEN.paymentInstruments.id field in your Sessions API request.

    ```
    {
    "allowedPaymentTypes": [
        "PANENTRY",
        "TMS_TOKEN"
     ]
    },
    "paymentConfigurations": {

        "TMS_TOKEN": {
          "paymentInstruments": [
            {
              "id": "4B1BCB328D52ED86E063AF598E0A99A5"
            }
          ]
        }
    }
    ```

> IMPORTANT
> To make a new payment instrument or instrument identifier under an existing customer during the complete mandate, you must meet these requirements:
>
> * You must include the customer token ID as the TMS_TOKEN.customer.id field in the paymentConfigurations field object.
>
> * ` TMS_TOKEN ` must be included in the allowedPaymentTypes field object.
>
> * tokenCreate must be set to ` true ` and ` paymentInstrument ` and ` instrumentIdentifier ` must be included as values in the tms.tokenTypes field array. For example:
>
>   ```
>         "tms": {
>         "tokenCreate": true,
>         "tokenTypes": [
>           "paymentInstrument",
>           "instrumentIdentifier",
>         ]
>       }
>
>   ```

When you meet these requirements, a new payment instrument or instrument identifier is created under the specified customer token.

eCheck/ACH Service {#uc-pay-methods-echeck}
===========================================

`Unified Checkout` supports the acceptance of eCheck information. Sensitive eCheck data is securely captured and replaced with a token. Acceptance of eCheck information enables merchants to collect funds from a customer's bank account through both the ACH service and eCheck service (US only) for either of these flows:

* ACH services are a set of connections composed of the legacy gateway solutions where `Cybersource` serves as the gateway.

* eCheck, the new service on Payments 2.0, is the acquirer solution where `Cybersource` is the acquirer.  
  Unified Checkout replaces these eCheck information fields in your payment input form:

* Routing number

* Account number

* Account type (non-sensitive)

Enrolling in eCheck/ACH Services {#uc-enable-digital-pay-echeck}
================================================================

`Unified Checkout` can accept bank account payments using the eCheck product. To accept eCheck payments through `Unified Checkout`, you must have the eCheck processing service enabled. To request access to eCheck processing and enable eCheck, you must submit an application in the `Business Center`. Once your application is approved, you can accept eCheck payments.  
For step-by-step instructions on enrolling and enabling eCheck, see the "Getting Started with the eCheck Service" section of the *[eCheck Merchant Guide](https://developer.cybersource.com/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-gs.md "")* . If eCheck is not listed in the Available Products section in the `Business Center`, you must contact your portfolio owner to enable your account to apply for eCheck.  
IMPORTANT If you have a business account or a financial relationship with Bank of America, Wells Fargo, or Chase, and you would like them to process your transactions, you must contact our Sales or Support team for more information on our ACH product.

Pay with eCheck/ACH Service UI {#uc-ui-echeck}
==============================================

These screen captures show the sequence of events your customer can expect when completing a payment with the eCheck/ACH service.

#### Figure:

eCheck/ACH Service Account Order Summary ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-645x375.svg/jcr:content/renditions/original)

#### Figure:

Pay with eCheck/ACH Service Checkout ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-manual-entry-645x545.svg/jcr:content/renditions/original)

#### Figure:

Pay with eCheck/ACH Service Review and Confirm ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-echeck-op-review-645x375.svg/jcr:content/renditions/original)

Digital Wallets {#uc-pay-methods-dig-wallets}
=============================================

Digital wallets are secure applications or services that enable users to store payment details, such as debit or credit cards electronically.  
Digital wallets such as Apple Pay, and Google Pay are accessible with smartphones, computers, or even directly in web browsers. Digital wallets allow customers to pay for goods and services both online and in physical stores without a physical card, often using biometrics, a device passcode, or wallet login, and approve the payment in just a few clicks.  
For online transactions, the wallet securely passes a payment token to the merchant or payment processor. This means that you do not handle sensitive customer data directly. This reduces friction at checkout, improves conversion rates, and enhances security through built‑in authentication and tokenization.  
Wallets are best suited for one‑time online purchases and express checkout experiences. Support for subscriptions and recurring payments varies by wallet, so you must ensure compatibility if future charges or merchant‑initiated transactions are required.  
`Unified Checkout` supports these wallet-based payment options:

* Apple Pay
* Google Pay
* `Click to Pay`
* Paze  
  This is how payments with digital wallets work:  
  ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-wallet-flow-600x500.svg/jcr:content/renditions/original)

Apple Pay {#uc-pay-methods-dig-wallets-applepay}
================================================

Apple Pay is a digital payment solution that enables your customers to make secure and convenient purchases without requiring them to enter their card details or shipping information. This section includes information about accepting Apple Pay payments with your `Unified Checkout` integration.

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
> In order to run an end-to-end test of the Apple Pay service on ` Unified Checkout `, you must perform additional setup steps. See [Preparing a Device for Testing Apple Pay on Unified Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay/uc-enable-digital-pay-applepay-prep-test-device.md "").

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

Apple Pay UI {#uc-ui-applepay}
==============================

These screen captures show the sequence of events your customer can expect when completing a payment with Apple Pay.

#### Figure: {#uc-ui-applepay_fig-uc-ui-applepay}

Apple Pay UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-apple-pay-865x575.svg/jcr:content/renditions/original)

Google Pay {#uc-pay-methods-dig-wallets-googlepay}
==================================================

Google Pay is a simple, secure in-app mobile and Web payment solution. This section includes information about accepting Google Pay payments with your `Unified Checkout` integration.

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
> When you enable Google Pay on ` Unified Checkout `, you can specify an optional parameter that defines the types of credentials that Google Pay sends you. See [Managing Google Pay Authentication Types](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay/uc-enable-digital-pay-googlepay-manage-authenticat.md "").

Managing Google Pay Authentication Types {#uc-enable-digital-pay-googlepay-manage-authentication}
=================================================================================================

Additional controls are available for Google Pay on `Unified Checkout`. When you enable Google Pay on `Unified Checkout`, you can specify optional parameters that define the types of card authentication you receive from Google Pay. To manage the types of credentials that Google Pay sends, use this expanded payment type object within the allowedPaymentTypes section of the sessions request:

```
"paymentConfigurations": {
    "GOOGLEPAY": {
      "allowedAuthMethods": "&lt;authentication type&gt;"
    }
```

The expanded payment type object has these parameters:

* type: Defines the type of payment option.
* options: Contains specific payment types parameters.  
  For Google Pay, use the new data element allowedAuthMethods within the options section of the payment types object to specify the authentication type you will receive from Google Pay. Possible values:
  * `PAN_ONLY`: Google returns primary account number (PAN) values
  * `CRYPTOGRAM_3DS`: Google returns fully authenticated network token values.
    By default, Google sends both authentication types.

  > IMPORTANT
  > When the complete mandate is used and Google Pay does not authenticate the transaction, then ` Unified Checkout ` completes the authentication request as part of the complete mandate.
  > REST Example: Specify Only PAN Authentication Accepted from Google  
  > This sessions request example specifies that Google Pay is to send only PAN values.

```
"allowedPaymentTypes": [
  "GOOGLEPAY"
],
"paymentConfigurations": {
    "GOOGLEPAY": {
      "allowedAuthMethods": [
        "PAN_ONLY",
        "CRYPTOGRAM_3DS"
      ]
    }
  }
```

REST Example: Simple Google Pay Request  
This sessions request example specifies that Google Pay can send all authentication types. This can be enabled and configured in the `Business Center`. For information about configuring your allowed payment types, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").

```
"allowedPaymentTypes": [
  "PANENTRY",
  "GOOGLEPAY",
  "CLICKTOPAY",
  "PAZE",
  "CHECK"
]
```

Google Pay UI {#uc-ui-googlepay}
================================

These screen captures show the sequence of events your customer can expect when completing a payment with Google Pay.

#### Figure:

Google Pay UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-google-pay-865x575.svg/jcr:content/renditions/original)

`Click to Pay` {#uc-pay-methods-dig-wallets-ctp}
================================================

`Click to Pay` is a secure online checkout method that enables customers to make purchases without entering their payment details for every purchase. This section includes information about accepting `Click to Pay` payments with your `Unified Checkout` integration.

Enabling `Click to Pay` in the `Business Center` {#uc-enable-digital-pay-ctp}
=============================================================================

To begin your integration, you must first enable `Click to Pay`. `Click to Pay` is a digital payment solution that allows customers to pay with their preferred card network and issuer without entering their card details on every website. Customers can use Relay, Mastercard, and American Express cards to streamline their purchase experience. `Click to Pay` provides a fast, secure, and consistent checkout experience across devices and browsers.  
Follow these steps to enable in `Click to Pay` on `Unified Checkout`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-enable-digital-pay-ctp_step-1}
   {#uc-enable-digital-pay-ctp_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original) {#uc-enable-digital-pay-ctp_step-2}
   {#uc-enable-digital-pay-ctp_step-2}

3. In the Payment Options section, click **Manage**. The Payment Options page appears.

4. Click **Manage** next to `Click to Pay`. The `Click to Pay` configuration page appears.

5. Enter your business name and website URL.

6. Click Submit.

   > IMPORTANT
   > ` Click to Pay ` uses network tokenization for transactions. These network tokens are stored in the vault of the token requestor ID (TRID) for the card scheme.

Set Up Customer Authentication for Click to Pay {#uc-authentication-steps}
==========================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. Click to Pay authentication is available for Relay and Mastercard card types. IMPORTANT
This authentication method is different from the authentication that is completed entirely in the ` Cybersource ` platform. To authenticate within the ` Cybersource ` platform, you must include the consumerAuthentication field in your request.  
These authentication methods are available:

* `3-D Secure`
* FIDO/Passkey
* Card verification value (CVV)
* One-time password (OTP)

{#uc-authentication-steps_ul_jtp_yvq_vjc} IMPORTANT

> After you complete these steps, the card issuer determines which authentication method to use. When the issuer determines that they will authenticate, they authenticate each Click to Pay transaction through the appropriate method. This may be a frictionless authentication or the customer may need to provide more information when required by the issuer.
> IMPORTANT
> Click to Pay authentication is not the same as consumer authentication using the complete mandate. See [Test Authentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-authentication.md "").

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-authentication-steps_step-1}
   {#uc-authentication-steps_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.  
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.  
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)  
   If Click to Pay is not enabled, click **On** next to Click to Pay.  
   ![Manage Available Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#uc-authentication-steps_step-2}
   {#uc-authentication-steps_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.  
   ![Value Added Solutions Page](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Relay and Mastercard the information that is required for authentication. IMPORTANT
   Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.

Click to Pay Customer Authentication {#uc-authentication}
=========================================================

When you enable customer authentication through Click to Pay, you give `Cybersource` permission to send Relay and Mastercard the required authentication information for each transaction. When the customer completes a transaction using a Relay or Mastercard card that is already stored in Click to Pay, authentication is managed within Click to Pay.  
Click to Pay authentication is only available for Relay branded cards that are tokenized with Click to Pay. If Click to Pay does not authenticate the transaction, but you are using the complete mandate with the consumerAuthentication field set to `3DS`, authentication is attempted as part of this request. When you do not use the complete mandate, you must check the result of the cardholderAuthenticationStatus field in the transient token and request `Payer Authentication` directly when it is required.

> IMPORTANT
> American Express card brands cannot be authenticated through Click to Pay customer authentication.

Authentication Flow
-------------------

![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/uc-ctp-auth-complete-flow-vas-740x370.svg/jcr:content/renditions/original)

`Click to Pay` UI {#uc-ui-ctp}
==============================

These screen captures show the sequence of events your customer can expect when completing a payment with `Click to Pay`.

#### Figure: {#uc-ui-ctp_fig-uc-ui-ctp}

`Click to Pay` UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ctp-865x480.svg/jcr:content/renditions/original)

`Click to Pay` UI Guidelines {#uc-appendix-ui-ux}
=================================================

The UI that is built in `Unified Checkout` for `Click to Pay` is built based on the EMV `Click to Pay` XC Guidelines V1.1. `Unified Checkout` has simplified the integration of the UI. The only UI work that you must complete is the placement of the payment option.

> IMPORTANT
> You must include ` Click to Pay ` as one of the presented payment methods and not as a separate payment method.  
> `Unified Checkout` captures all card details that are manually entered by the cardholder. This enables the cardholder to enroll in `Click to Pay` and removes the requirement for the cardholder to manually enter their card details the next time they check out.  
> `Unified Checkout` provides a standard payment label in the `Unified Checkout` JavaScript that is loaded in your checkout page. One of these scenarios occurs when the cardholder selects the button:

* The cardholder is recognized.
* The cardholder is not recognized but has a `Click to Pay` account.
* The cardholder does not have a `Click to Pay` account.  
  You can also trigger the `Unified Checkout` flow using a custom button. If you are using your own custom button, your payment button or widget must display the `Click to Pay` image for the cardholder. For information about a custom button, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

> IMPORTANT
> Your implementation consultant will ask you for a mock-up of your payment flow for confirmation that it is compliant with the ` Click to Pay ` UI design standards.

Recognized `Click to Pay` Customer
----------------------------------

The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer
------------------------------------

When the cardholder has a `Click to Pay` account but is not on a registered device, they receive a one-time password to their registered email address and phone number to authenticate their identity before their stored `Click to Pay` credentials are shown:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

No `Click to Pay` Account
-------------------------

When the cardholder does not have a `Click to Pay` account, they can provide a new email address to perform a new lookup or they can choose to enter their card details manually. The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-no-account}

No `Click to Pay` Account UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

`Click to Pay` UI Examples {#uc-appendix-ui-ux-ex}
==================================================

This section contains UI examples of how you should display `Click to Pay` on your payment page. For information about how to display the UI, see [JavaScript API Reference](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix-js-reference-v1.md "").

`Click to Pay` Replaces PAN Capture
-----------------------------------

`Click to Pay` is the card entry payment option within your payment page.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex1}

`Click to Pay` Replaces PAN Capture UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex1-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex2}

`Click to Pay` Replaces PAN Capture UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex2-645x375.svg/jcr:content/renditions/original) For information about how to configure this UI, see [Loading the JavaScript Library](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro.md "").

`Click to Pay` as Radio Button
------------------------------

`Click to Pay` is a radio button for the card entry payment option within your payment page. When the cardholder selects this option, the `Click to Pay` payment flow is loaded.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex3}

`Click to Pay` Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex3-645x375.svg/jcr:content/renditions/original)

`Click to Pay` Icon on Radio Button
-----------------------------------

You can host the radio selection option for card payment with the `Click to Pay` icon displayed on the payment label. The `Unified Checkout` flow loads when the cardholder selects this option. For information about customizing how to trigger `Unified Checkout`, see [Trigger](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-trigger.md "") and [Components](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-components.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex4}

`Click to Pay` Icon on Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex4-645x375.svg/jcr:content/renditions/original)

Load `Click to Pay` Automatically From Trigger or Components
------------------------------------------------------------

You can load the `Unified Checkout` JavaScript flow within your own payment button without requiring the cardholder to select a card payment option. This example shows a recognized user payment flow where the cardholder's information is shown automatically next to the other payment methods hosted within your payment page. For information about customizing how to trigger `Unified Checkout`, see [Trigger](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-trigger.md "") and [Components](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-components.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex5}

`Click to Pay` Loaded Automatically From Trigger or Components UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

Card Payment Options with `Click to Pay` in UI
----------------------------------------------

Do not present the `Unified Checkout` payment button as a separate payment method from the card payment button. If you do this, the cardholder is not prompted with their `Click to Pay` cards and must manually enter their payment details. They will also not have the option to store their card within `Click to Pay` for future use.  
These examples show multiple card payment options and `Click to Pay` in a UI:

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex6}

Multiple Card Payment Options in UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex6-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex7}

Multiple Card Payment Options in UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex7-645x325.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex8}

Multiple Card Payment Options in UI Example 3 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex8-645x375.svg/jcr:content/renditions/original)

Paze {#uc-pay-methods-dig-wallets-paze}
=======================================

Paze is an online checkout option, or *digital wallet* , that enables you to offer customers a fast and secure way to make purchases online. This section includes information about accepting Paze payments with your `Unified Checkout` integration.

Paze UI {#uc-ui-paze}
=====================

These screen captures show the sequence of events your customer can expect when completing a payment with Paze.

#### Figure:

Paze UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-paze.png/jcr:content/renditions/original)

Alternative Payment Methods {#uc-altpay-methods-intro}
======================================================

This section describes the alternative payment methods you can use in your `Unified Checkout` integration. After you successfully integrate one payment method, you can add another from the same category with minimal adjustments to your existing configuration.
* [Online Bank Transfers](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt.md "")
* [Buy Now, Pay Later](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-bnpl.md "")
* [Post-Pay Reference Payments](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-ppr.md "")
* [Alternative Payment Wallets](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets.md "")

Online Bank Transfers {#uc-pay-methods-obt}
===========================================

Online bank transfers enable customers to complete their purchase by securely logging into their online banking environment. This method is secure, trusted, and widely used in many European countries.

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how online bank transfers work:

#### Figure:

Online Bank Transfers ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-obt-650x130.svg/jcr:content/renditions/original)
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

|  Payment Method  | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| iDEAL            | `IDEAL`                             | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Netherlands (NL)                | EUR                        |
| Multibanco       | `MULTIBANCO`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR                        |
| Przelewy24       | `PRZELEWY24`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Poland (PL)                     | PLN                        |
| Bancontact       | `BANCONTACT`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Italy (IT)                      | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Spain (ES)                      | EUR                        |
| DragonPay        | `DRAGONPAY`                         | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Philippines (PH)                | PHP                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | France (FR)                     | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Germany (DE)                    | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Ireland (IE)                    | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Netherlands (NL)                | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Spain (ES)                      | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | United Kingdom (GB)             | GBP                        |
[Online Bank Transfer Payment Methods]

Bancontact {#uc-pay-methods-obt-bancontact}
===========================================

Bancontact enables customers to make secure online and in-store purchases directly from their bank accounts. Bancontact is a leading payment method in Belgium.  
When the total amount of the order is outside the range of accepted transaction amounts, the Bancontact payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: Not applicable

Opt in to Bancontact on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Bancontact on `Unified Checkout`:

1. Add Bancontact to your integration by adding `BANCONTACT` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

DragonPay {#uc-pay-methods-obt-dragonpay}
=========================================

DragonPay provides Filipino customers and businesses with a secure payment channel that does not require customers to be banked or have a credit card. Customers can make purchases online and pay by bank transfer.  
When the total amount of the order is outside the range of accepted transaction amounts, the DragonPay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PHP 50.01
* **Maximum transaction amount**: Not applicable

Opt in to DragonPay on `Unified Checkout`
-----------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add DragonPay to your integration by adding `DRAGONPAY` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Tink Pay By Bank {#uc-pay-methods-obt-tink}
===========================================

Tink is an alternative payment method that uses the *pay by bank* payment method. Tink Pay By Bank enables customers to make payments directly from their bank account to the seller's account and bypasses traditional payment methods such as credit cards.  
When the total amount of the order is outside the range of accepted transaction amounts, Tink Pay By Bank is not displayed in `Unified Checkout`.  
These are the accepted transaction amounts for the United Kingdom (GB):

* **Minimum transaction amount**: Not applicable

* **Maximum transaction amount**: GBP 8,500
  {#uc-pay-methods-obt-tink_ul_nhn_33y_hjc}  
  These are the accepted transaction amounts for the European Union (EU):

* **Minimum transaction amount**: Not applicable

* **Maximum transaction amount**: EUR 10,000
  {#uc-pay-methods-obt-tink_ul_v4p_j3y_hjc}

Opt in to Tink Pay By Bank on `Unified Checkout`
------------------------------------------------

You can enable Tink Pay By Bank from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Tink Pay By Bank using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").  
You can also enable Tink Pay By Bank using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Tink Pay By Bank payment method using the API:

1. Add Tink Pay by Bank to your integration by adding `TINKPAYBYBANK` to the allowedPaymentTypes field object within the capture context request.

2. To use Tink Pay By Bank in your selected country, you must set the country field value to the correct value in the capture context request:

   |    Country     | country Field Value |
   |----------------|---------------------|
   | France         | `FR`                |
   | Germany        | `DE`                |
   | Ireland        | `IE`                |
   | Netherlands    | `NL`                |
   | Spain          | `ES`                |
   | United Kingdom | `GB`                |
   [Tink Pay By Bank country Field Values]

3. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.

4. To use Tink Pay By Bank in your selected country, you must set the data.orderInformation.billTo.country field value to the correct value in the capture context request:

   |    Country     | data.orderInformation.billTo.country Field Value |
   |----------------|--------------------------------------------------|
   | France         | `FR`                                             |
   | Germany        | `DE`                                             |
   | Ireland        | `IE`                                             |
   | Netherlands    | `NL`                                             |
   | Spain          | `ES`                                             |
   | United Kingdom | `GB`                                             |
   [Tink Pay By Bank data.orderInformation.billTo.country Field Values]

5. To use Tink Pay By Bank in your selected country, you must set the data.orderInformation.amountDetails.currency field value to the correct value in the capture context request:

   |    Country     | data.orderInformation.amountDetails.currency Field Value |
   |----------------|----------------------------------------------------------|
   | France         | `EUR`                                                    |
   | Germany        | `EUR`                                                    |
   | Ireland        | `EUR`                                                    |
   | Netherlands    | `EUR`                                                    |
   | Spain          | `EUR`                                                    |
   | United Kingdom | `GBP`                                                    |
   [Tink Pay By Bank data.orderInformation.amountDetails.currency Field Values]

6. Include this optional field for online bank transfers in the capture context request:

   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.shipTo.address1
   * data.orderInformation.shipTo.address2
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.district
   * data.orderInformation.shipTo.firstName
   * data.orderInformation.shipTo.lastName
   * data.orderInformation.shipTo.locailty

* data.orderInformation.shipTo.postalCode

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

1. Add iDeal to your integration by adding `IDEAL` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

MyBank {#uc-pay-methods-obt-mybank}
===================================

MyBank enables customers to pay for their online purchases in an easy and safe way using real-time bank transfers. MyBank customers complete payments by selecting their bank and logging in with their online banking credentials.  
When the total amount of the order is outside the range of accepted transaction amounts, the MyBank payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: EUR 999,999,999.99

Opt in to MyBank on `Unified Checkout`
--------------------------------------

Follow these steps to opt in to MyBank on `Unified Checkout`:

1. Add MyBank to your integration by adding `MYBANK` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Multibanco {#uc-pay-methods-obt-multibanco}
===========================================

Multibanco enables customers to pay for a range of goods and services by bank transfer. These services include e-commerce, licenses, and taxes post-purchase. Multibanco is supported by all banks in Portugal.  
When the total amount of the order is outside the range of accepted transaction amounts, the Multibanco payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: No minimum
* **Maximum transaction amount**: EUR 99,999

Opt in to Multibanco on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add Multibanco to your integration by adding `MULTIBANCO` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Przelewy24\|P24 {#uc-pay-methods-obt-p24}
=========================================

Przelewy24, or P24, is a Poland-based real-time online bank transfer payment method. P24 is one of the most popular payment methods in Poland covering all major consumer banks.  
When the total amount of the order is outside the range of accepted transaction amounts, the P24 payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PLN 0.01, EUR 0.01
* **Maximum transaction amount**: PLN 55,000.00, EUR 12,500.00

Opt in to Przelewy24\|P24 on `Unified Checkout`
-----------------------------------------------

Follow these steps to opt in to Przelewy24\|P24 on `Unified Checkout`:

1. Add Przelewy24\|P24 to your integration by adding `PRZELEWY24` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:

* data.orderInformation.billTo.address1

Verify Status for Online Bank Transfers {#uc-pay-methods-obt-status-ppro}
=========================================================================

When the status of your payment request is `PENDING`, you can verify the status by using the URL method and the payload that is included in the transactionStatus.url field in the webhook response: Webhook Response

```keyword
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

{#uc-pay-methods-obt-status-ppro_codeblock_hr4_bl4_53c}  
You can also send a request to this endpoint to verify the status:  
**Production:** `GET ``https://api.cybersource.com``/tss/v2/transactions/`*{id}*  
**Test:** `GET ``https://apitest.cybersource.com``/tss/v2/transactions/`*{id}*  
The *{id}* is the ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Verify Status for Online Bank Transfers (Tink Pay By Bank) {#uc-pay-methods-obt-status-non-ppro}
================================================================================================

When the status of your payment request is `PENDING`, you can verify the status by using the URL method and the payload that is included in the transactionStatus.url field in the webhook response: Webhook Response

```keyword
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
      "url": "https://api.cybersource.com/pts/v2/refresh-payment-status/7531173918516064204807",
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

{#uc-pay-methods-obt-status-non-ppro_codeblock_kk3_cl4_53c}  
You can also send a request to this endpoint to verify the status:  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*  
The *{id}* is the ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-obt-handle-response}
======================================================

When `Unified Checkout` automatically processes a payment with `autoProcessing` is set to `true` or you have set `autoProcessing` to `false` and are using checkout.Complete(), you must handle both successful responses and various errors. After the payment is complete, the completeResponse field object contains information about the transaction outcome.  
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").  
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` and `COMPLETE_TRANSACTION_FAILED`. `COMPLETE_TRANSACTION_CANCELED` occurs when the user cancels the transaction and `COMPLETE_TRANSACTION_FAILED` indicates that the consumer's transaction failed.  
For PPRO-enabled online bank transfers, only cancellation errors are returned, and Tink Pay By Bank returns failure and cancellation errors. For information about possible errors that can occur when calling the complete API see [UnifiedCheckoutError](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors/uc-handle-errors-uc-checkout.md "") in [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

Buy Now, Pay Later {#uc-pay-methods-bnpl}
=========================================

Buy Now, Pay Later payment methods enable customers to purchase goods or services immediately and pay in installments over time. With Buy Now, Pay Later, you are paid immediately and in full, while your customers pay nothing or only a portion of the total at the time of purchase. The remaining balance is typically spread over equal, often interest-free, payments.  
Buy Now, Pay Later is increasingly popular for both online and in-store purchases.

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how Buy Now, Pay Later works:

#### Figure:

Buy Now, Pay Later ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-bnpl-650x150.svg/jcr:content/renditions/original)
1. The customer chooses their Buy Now, Pay Later payment method during checkout.
2. The customer chooses how much they want to pay, such as nothing, installments, or the total amount.
3. The unpaid amount is divided into equal installments that are paid over a fixed amount of time.
4. You receive the full payment after the customer completes checkout, and the Buy Now, Pay Later provider collects the installment payments from your customer.  
   `Unified Checkout` supports the Afterpay/Clearpay and Paypal Buy Now, Pay Later payment methods.

|  Payment Method   | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|-------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Canada (CA)                     | CAD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Canada (CA)                     | CAD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Australia (AU)                  | AUD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Australia (AU)                  | AUD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | New Zealand (NZ)                | NZD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | New Zealand (NZ)                | NZD                        |
| Cash App Afterpay | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | United States (US)              | USD                        |
| Cash App Afterpay | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | United States (US)              | USD                        |
| Clearpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Great Britain (GB)              | GBP                        |
| Clearpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Great Britain (GB)              | GBP                        |
[Buy Now, Pay Later Payment Method Support]

For information on ISO country codes, see [ISO Standard Country Codes](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.md "").  
For information on ISO currency codes, see [ISO Standard Currency Codes](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "").

Afterpay {#uc-pay-methods-bnpl-afterpay}
========================================

Afterpay is a Buy Now, Pay Later service that allows customers to purchase items immediately and pay for them in four interest-free installments over a period of 6 weeks. Afterpay is also known as Clearpay in the UK, and Cash App Afterpay in the US. For more information, see the [*Afterpay and Clearpay Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/afterpay/developer/all/so/afterpay/afterpay-intro.md "").  
When the total amount of the order is outside the range of accepted transaction amounts, the Afterpay/Clearpay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: 1 (CAD, AUD, NZD, USD, and GBP)
* **Maximum transaction amount**: Not applicable

Opt in to Afterpay on `Unified Checkout`
----------------------------------------

Follow these steps to opt in to the Afterpay/Clearpay payment method in `Unified Checkout`:

1. Add Afterpay to your integration by adding `AFTERPAY` to the allowedPaymentTypes field within the capture context request. The default field value is `AFTERPAY` even if you want to support Cash App Afterpay in the US or Clear Pay in the UK.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.  
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   You can capture the funds later if you include the completeMandate.type field in the capture context request and set the value to `AUTH`. When you capture the funds later, you must perform a capture using the payments API. See [Captures](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-bnpl/uc-pay-methods-bnpl-captures.md "").  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.postalCode
   * data.orderInformation.billTo.administrativeArea
   * data.orderInformation.billTo.country
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * data.orderInformation.shipTo.firstName
   * data.orderInformation.shipTo.lastName
   * data.orderInformation.shipTo.address1
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * data.orderInformation.shipTo.administrativeArea

* data.orderInformation.shipTo.country

Verify Status for Afterpay {#uc-pay-methods-bnpl-afterpay-status}
=================================================================

When the status of your payment request is `PENDING`, you can verify the status by sending a POST request to the URL that is included in the transactionStatus.url field in the webhook response. Webhook Response

```keyword
{
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
        "processingInformation": {
          "actionList": [
            "AP_STATUS"
          ]
        },
        "paymentInformation": {
          "paymentType": {
            "method": {
              "name": "AFTERPAY"
            },
            "name": "INVOICE"
          }
        }
      }
    }
  }
}
```

{#uc-pay-methods-bnpl-afterpay-status_codeblock_pkj_wk4_53c} You can also send a request to this endpoint to verify the status:  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-bnpl-afterpay-status_restcapture}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-bnpl-afterpay-status_restcapture-test}
The *`{id}`* is ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-bnpl-handle-response}
=======================================================

When `Unified Checkout` automatically processes a payment with `autoProcessing` is set to `true` or you have set `autoProcessing` to `false` and are using checkout.Complete(), you must handle both successful responses and various errors. After the payment is complete, the completeResponse field object contains information about the transaction outcome.  
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").  
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` and `COMPLETE_TRANSACTION_FAILED`. `COMPLETE_TRANSACTION_CANCELED` occurs when the user cancels the transaction and `COMPLETE_TRANSACTION_FAILED` indicates that the consumer's transaction failed.

Captures {#uc-pay-methods-bnpl-captures}
========================================

When you set the completeMandate.type field value to `AUTH` or `PREFER_AUTH`, you must send a request to capture an authorized payment. Full and partial captures are supported.

Endpoint {#uc-pay-methods-bnpl-captures_d8e147}
-----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-bnpl-captures_d8e156}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-bnpl-captures_d8e169}  
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

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how post-pay reference payments work:  
> ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-ppr-650x175.svg/jcr:content/renditions/original)

1. The customer selects a convenience store/voucher payment method during checkout.
2. The customer receives their payment code/voucher or QR code.
3. The customer presents the payment code/voucher or QR in-store to complete the payment.
4. The customer receives a notification that the payment is complete.  
   `Unified Checkout` supports the Konbini voucher-based payment option:

| Payment Method | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|----------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| Konbini        | `KONBINI`                           | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Japan (JP)                      | JPY                        |
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
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.phoneNumber
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Verify Status for Post-Pay Reference {#uc-pay-methods-ppr-status-ppro}
======================================================================

When the status of your payment request is `PENDING`, you can verify the status by sending a POST request to the URL that is included in the transactionStatus.url field in the webhook response: Webhook Response

```keyword
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

{#uc-pay-methods-ppr-status-ppro_codeblock_ppt_yk4_53c}  
You can also send a request to this endpoint to verify the status:  
**Production:** `GET ``https://api.cybersource.com``/tss/v2/transactions/`*{id}*  
**Test:** `GET ``https://apitest.cybersource.com``/tss/v2/transactions/`*{id}*  
The *{id}* is the ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-ppr-handle-response}
======================================================

When `Unified Checkout` automatically processes a payment with `autoProcessing` is set to `true` or you have set `autoProcessing` to `false` and are using checkout.Complete(), you must handle both successful responses and various errors. After the payment is complete, the completeResponse field object contains information about the transaction outcome.  
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").  
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` which is returned when the user cancels the transaction.  
For PPRO-enabled online bank transfers, only cancellation errors are returned. For information about possible errors that can occur when calling the complete API see [UnifiedCheckoutError](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors/uc-handle-errors-uc-checkout.md "") in [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

Alternative Payment Wallets {#uc-pay-methods-wallets}
=====================================================

Digital wallets are secure applications or services that enable users to store payment details, such as debit or credit cards electronically.  
For online transactions, the wallet securely passes a payment token to the merchant or payment processor. This means that you do not handle sensitive customer data directly. This reduces friction at checkout, improves conversion rates, and enhances security through built‑in authentication and tokenization.  
Wallets are best suited for one‑time online purchases and express checkout experiences. Support for subscriptions and recurring payments varies by wallet, so you must ensure compatibility if future charges or merchant‑initiated transactions are required.  
`Unified Checkout` supports these wallet-based payment options:

* PayPal
* Venmo
  This is how payments with digital wallets work:  
  ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-wallet-flow-600x500.svg/jcr:content/renditions/original)

| Payment Method | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) |                        Customer ISO Currency Code                        |
|----------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|--------------------------------------------------------------------------|
| PayPal         | `PAYPAL`                            | `AUTH` `PREFER_AUTH`                 | Yes               | Delayed              | Global                          | AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, NOK, NZD, PLN, SEK, SGD, and USD |
| PayPal         | `PAYPAL`                            | `CAPTURE`                            | No                | Immediate            | Global                          | AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, NOK, NZD, PLN, SEK, SGD, and USD |
| Venmo          | `VENMO`                             | `AUTH` `PREFER_AUTH`                 | Yes               | Delayed              | United States (US)              | USD                                                                      |
| Venmo          | `VENMO`                             | `CAPTURE`                            | No                | Immediate            | United States (US)              | USD                                                                      |
[Digital Wallet Payment Support]

PayPal {#uc-pay-methods-bnpl-paypal}
====================================

PayPal is a secure and convenient payment service that your customers can use to make payments without directly using their bank accounts or credit cards. PayPal gives yours customers the option to pay in installments over time with PayPal Pay Later while also giving you the full payment immediately. These installments are available:

* **Pay in 3**: Pay in three installments. Available in the UK.
* **Pay in 4**: Pay in four installments. Available in the US.
* **Pay Monthly**: Pay in monthly recurring installments.

Opt in to Paypal on `Unified Checkout`
--------------------------------------

You can enable Paypal from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Paypal using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").  
You can also enable Paypal using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Paypal payment method using the API:

1. Add Paypal to your integration by adding `PAYPAL` to the allowedPaymentTypes field within the capture context request.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.  
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   You can capture the funds later if you include the completeMandate.type field in the capture context request and set the value to `AUTH`. When you capture the funds later, you must perform a capture using the payments API. See [Captures](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-wallets/uc-pay-methods-wallet-captures.md "").  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * orderInformation.amountDetails.currency
   * orderInformation.amountDetails.taxAmount
     * This field is the sum of all orderInformation.lineItems\[\].taxAmount values.
       {#uc-pay-methods-bnpl-paypal_ul_sk5_zjq_cjc}
   * orderInformation.amountDetails.totalAmount
     * This field is the sum of (orderInformation.lineItems\[\].quantity × orderInformation.lineItems\[\].unitPrice) + orderInformation.lineItems\[\].taxAmount for all line items.
       {#uc-pay-methods-bnpl-paypal_ul_h22_zjq_cjc}
   * orderInformation.lineItems\[\].productDescription
   * orderInformation.lineItems\[\].productName
   * orderInformation.lineItems\[\].productSKU
   * orderInformation.lineItems\[\].quantity
   * orderInformation.lineItems\[\].taxAmount

     > IMPORTANT
     > This field is required for all line items when you include orderInformation.lineItems\[\].taxAmount for one line item.

     * You can set this field value to `0.00`.
       {#uc-pay-methods-bnpl-paypal_ul_lwq_r53_cjc}
   * orderInformation.lineItems\[\].typeOfSupply
   * orderInformation.lineItems\[\].unitPrice
4. Include these optional fields in the capture context request:
   * buyerInformation.dateOfBirth
   * buyerInformation.language
   * buyerInformation.personalIdentification\[\].id
   * buyerInformation.personalIdentification\[\].type
   * clientReferenceInformation.reconciliationId
   * merchantInformation.merchantDescriptor.name
     * This field affects the name that the customers see on their card statement. If the merchant is Candy Shop and passes this as their name - customer will see `PAYPAL * Candy Shop` in their bank statement.
   * orderInformation.amountDetails.taxDetails.taxId
   * orderInformation.amountDetails.taxDetails.type
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.company.name
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.phoneNumber
   * orderInformation.invoiceDetails.invoiceNumber
   * orderInformation.invoiceDetails.productDescription
   * orderInformation.lineItems\[\].totalAmount
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * paymentInformation.customer.customerid
   * processingInformation.processingInstruction
     * Set this field to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

Example: Multiple Line-Items {#uc-pay-methods-bnpl-paypal_section_zfp_mv3_cjc}
------------------------------------------------------------------------------

This example includes multiple line items in the amountDetails field object:

```
{
  "amountDetails": {
    "totalAmount": "221.91",
    "currency": "USD",
    "taxAmount": "14.42"
  },
  "lineItems": [
    {
      "productName": "501 Original Fit Jeans Blues",
      "productSku": "00501019403432",
      "quantity": 1,
      "unitPrice": "100.0",
      "totalAmount": "100.00",
      "taxAmount": "8.63"
    },
    {
      "productName": "Levi Blue shirt Plaid",
      "productSku": "0094784142",
      "quantity": 1,
      "unitPrice": "100.00",
      "totalAmount": "100.00",
      "taxAmount": "5.79"
    },
    {
      "productName": "shipping_and_handling",
      "productSku": "shipping_and_handling",
      "quantity": 1,
      "unitPrice": "7.49",
      "totalAmount": "7.49",
      "taxAmount": "0.00"
    }
  ]
}
```

{#uc-pay-methods-bnpl-paypal_codeblock_n2l_qz3_cjc}

Venmo {#uc-pay-methods-obt-venmo}
=================================

Venmo is a mobile payment service that is owned by PayPal and enables your customers to make payments from their Venmo mobile application. Customers link their Venmo accounts to their bank accounts, debit cards, and credit cards to send and receive payments. Venmo is a secure and convenient payment service for your customers to make payments without directly using their bank accounts or credit cards.

Opt in to Venmo on `Unified Checkout`
-------------------------------------

You can enable Venmo from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Venmo using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").  
You can also enable Venmo using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Venmo payment method using the API:

1. Add Venmo to your integration by adding `VENMO` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.amountDetails.currency
   * orderInformation.amountDetails.taxAmount
     * This field is the sum of all orderInformation.lineItems\[\].taxAmount values.
       {#uc-pay-methods-obt-venmo_ul_myc_rcj_cjc}
   * orderInformation.amountDetails.totalAmount
     * This field is the sum of (orderInformation.lineItems\[\].quantity × orderInformation.lineItems\[\].unitPrice) + orderInformation.lineItems\[\].taxAmount for all line items.
       {#uc-pay-methods-obt-venmo_ul_g4t_scj_cjc}
   * orderInformation.lineItems\[\].productDescription
   * orderInformation.lineItems\[\].productName
   * orderInformation.lineItems\[\].productSKU
   * orderInformation.lineItems\[\].quantity
   * orderInformation.lineItems\[\].taxAmount

     > IMPORTANT
     > This field is required for all line items when you include orderInformation.lineItems\[\].taxAmount for one line item.

     * You can set this field value to `0.00`.
       {#uc-pay-methods-obt-venmo_ul_lwq_r53_cjc}
   * orderInformation.lineItems\[\].unitPrice
4. Include these optional fields in the capture context request:
   * buyerInformation.dateOfBirth
   * buyerInformation.language
   * buyerInformation.personalIdentification\[\].id
   * buyerInformation.personalIdentification\[\].type
   * clientReferenceInformation.reconciliationId
   * merchantInformation.merchantDescriptor.name
     * This field affects the name that the customers see on their card statement. If the merchant is Candy Shop and passes this as their name - customer will see `PAYPAL * Candy Shop` in their bank statement.
   * orderInformation.amountDetails.taxDetails.taxId
   * orderInformation.amountDetails.taxDetails.type
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.company.name
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.phoneNumber
   * orderInformation.invoiceDetails.invoiceNumber
   * orderInformation.invoiceDetails.productDescription
   * orderInformation.lineItems\[\].totalAmount
   * orderInformation.lineItems\[\].typeOfSupply.type
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * paymentInformation.customer.customerid
   * processingInformation.processingInstruction
     * Set this field to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

Example: Multiple Line-Items {#uc-pay-methods-obt-venmo_section_ar5_zbj_cjc}
----------------------------------------------------------------------------

This example includes multiple line items in the amountDetails field object:

```
{
  "amountDetails": {
    "totalAmount": "221.91",
    "currency": "USD",
    "taxAmount": "14.42"
  },
  "lineItems": [
    {
      "productName": "501 Original Fit Jeans Blues",
      "productSku": "00501019403432",
      "quantity": 1,
      "unitPrice": "100.0",
      "totalAmount": "100.00",
      "taxAmount": "8.63"
    },
    {
      "productName": "Levi Blue shirt Plaid",
      "productSku": "0094784142",
      "quantity": 1,
      "unitPrice": "100.00",
      "totalAmount": "100.00",
      "taxAmount": "5.79"
    },
    {
      "productName": "shipping_and_handling",
      "productSku": "shipping_and_handling",
      "quantity": 1,
      "unitPrice": "7.49",
      "totalAmount": "7.49",
      "taxAmount": "0.00"
    }
  ]
}
```

{#uc-pay-methods-obt-venmo_codeblock_br5_zbj_cjc}

Verify Status for PayPal and Venmo {#uc-pay-methods-paypal-venmo-status}
========================================================================

When the status of your payment request is `PENDING`, you can verify the status by sending a POST request to the URL that is included in the transactionStatus.url field in the webhook response: Webhook Response

```keyword
{
  "transactionStatus": {
    "url": "https://apitest.cybersource.com/pts/v2/refresh-payment-status/76406322771491323955899488",
    "method": "POST",
    "payload": {
      "clientReferenceInformation": {
        "applicationName": "unifiedCheckout"
      },
      "processingInformation": {
        "actionList": [
          "AP_STATUS"
        ]
      },
      "paymentInformation": {
        "paymentType": {
          "method": {
            "name": "payPal"
          },
          "name": "eWallet"
        }
      }
    }
  },
  "transactionResult": {
    "details": {
      "submitTimeUtc": "2025-11-25T09:31:14Z",
      "processorInformation": {
        "sellerProtection": {
          "eligibility": "ELIGIBLE",
          "disputeCategories": [
            "ITEM_NOT_RECEIVED",
            "UNAUTHORIZED_TRANSACTION"
          ]
        },
        "transactionId": "14815899TN877504A",
        "orderStatus": "COMPLETED",
        "orderId": "74902340T07048209",
        "updateTimeUtc": "2025-11-25T09:33:48Z",
        "expirationTimeUtc": "2025-12-24T09:33:48Z"
      },
      "orderInformation": {
        "amountDetails": {
          "totalAmount": "0.11",
          "currency": "USD"
        },
        "billTo": {
          "email": "jane.doe@relay.com",
          "lastName": "Doe",
          "firstName": "Jane"
        }
      },
      "updateTimeUtc": "2025-11-25T09:33:48Z",
      "buyerInformation": {
        "merchantCustomerId": "JS4EXZRT68ED8"
      },
      "message": "Successful",
      "createTimeUtc": "2025-11-25T09:33:48Z",
      "clientReferenceInformation": {
        "code": "default"
      },
      "reconciliationId": "76406307371191323955899488",
      "status": "COMPLETED",
      "id": "76406322771491323955899488"
    },
    "id": "76406322771491323955899488",
    "message": "Successful",
    "outcome": "COMPLETED",
    "status": "COMPLETED"
  }
}
```

{#uc-pay-methods-paypal-venmo-status_codeblock_itw_5l4_53c} You can also send a request to this endpoint to verify the status:  
**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-paypal-venmo-status_restcapture}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#uc-pay-methods-paypal-venmo-status_restcapture-test}
The *`{id}`* is ID that is returned in the webhook response. For more information, see [Webhooks Support](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-appendix-webhooks.md "").

Handle Responses {#uc-pay-methods-wallet-handle-response}
=========================================================

When `Unified Checkout` automatically processes a payment with `autoProcessing` is set to `true` or you have set `autoProcessing` to `false` and are using checkout.Complete(), you must handle both successful responses and various errors. After the payment is complete, the completeResponse field object contains information about the transaction outcome.  
When a payment is processed successfully, you must parse the response to confirm the payment status, update their order records, and trigger any post-payment workflows. Post-payment workflows include sending confirmation emails or updating inventory. See [JavaScript Example: Processing a Payment](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-cs-setup-intro/uc-getting-started-cs-js-library-intro/uc-getting-started-cs-js-payment-example.md "").  
Your error handling should account for specific cases such as `COMPLETE_TRANSACTION_CANCELED` and `COMPLETE_TRANSACTION_FAILED`. `COMPLETE_TRANSACTION_CANCELED` occurs when the user cancels the transaction and `COMPLETE_TRANSACTION_FAILED` indicates that the consumer's transaction failed.  
For wallet based payments, only cancellation errors are returned. For information about possible errors that can occur when calling the complete API, see [UnifiedCheckoutError](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors/uc-handle-errors-uc-checkout.md "") in [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

Captures {#uc-pay-methods-wallet-captures}
==========================================

When you set the completeMandate.type field value to `AUTH` or `PREFER_AUTH`, you must send a request to capture an authorized payment. Full and partial captures are supported.

Endpoint {#uc-pay-methods-wallet-captures_d8e147}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-wallet-captures_d8e156}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-wallet-captures_d8e169}  
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

Integration Methods {#uc-integration-methods-intro}
===================================================

`Unified Checkout` offers flexible integration methods for your page's checkout experience. This section contains information about each integration method and the JavaScript that is required for each one.  
This table outlines the different integration methods offered by `Unified Checkout`:

|                                     |                                                                                        Checkout                                                                                        |                                                                                       Button                                                                                        |                                                                                       Trigger                                                                                        |                                                                                                   Components                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What does it do?**                | Displays all configured payment methods in a single `Unified Checkout` experience. The display order is determined from the `Business Center`Merchant Experience or the Sessions API.  | Enables you to place individual `Unified Checkout` payment buttons on your payment page.                                                                                            | Enables you to use your own button to launch the hosted payment experience, for example card entry or `Click to Pay`, in a sidebar.                                                  | Enables you to embed individual payment form elements, for example, card fields or the `Click to Pay` experience, directly into your page for full control over the checkout experience.                        |
| **What is it best for?**            | When you want a quick out-of- the-box checkout with a list of payment methods.                                                                                                         | Merchants that want flexibility in how payment buttons are displayed across their page.                                                                                             | Merchants that want to keep their own checkout button but use `Unified Checkout` to handle the payment flow.                                                                         | Merchants that want full control over the UI and want to fully embed the payment form into their own checkout.                                                                                                  |
| **Who owns the payment button(s)?** | `Unified Checkout`                                                                                                                                                                     | `Unified Checkout`                                                                                                                                                                  | Merchant                                                                                                                                                                             | Merchant                                                                                                                                                                                                        |
| **Display modes**                   | Sidebar or embedded                                                                                                                                                                    | Embedded                                                                                                                                                                            | Sidebar                                                                                                                                                                              | Embedded                                                                                                                                                                                                        |
| **Supported payment methods**       | All configured methods                                                                                                                                                                 | All available methods                                                                                                                                                               | Card payment and `Click to Pay`                                                                                                                                                      | Card payment, `Click to Pay`, and eCheck/ACH service                                                                                                                                                            |
| **Example uses**                    | A merchant that requires a button list of all accepted payment methods in `Unified Checkout`.                                                                                          | A merchant that wants to host buttons separately on their page. For example, displaying Apple Pay at the top of the page and card entry at the bottom of the page.                  | A merchant that has an existing pay by card/`Click to Pay`button that they want to launch into the payment UI using a sidebar view.                                                  | A merchant that wants to embed `Unified Checkout` payment components directly into their page without the standard header. This integration method is ideal for a user that offers a radio button/drop-down UI. |
| **Summary**                         | **Full out-of-the-box checkout**                                                                                                                                                       | **Flexible placement of payment buttons**                                                                                                                                           | **Use your own button to launch the payment UI**                                                                                                                                     | **Fully embedded and customized payment experience**                                                                                                                                                            |
| **Documentation**                   | [Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-checkout.md "") | [Button](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-buttons.md "") | [Trigger](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-trigger.md "") | [Components](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-integration-methods-intro/uc-integration-methods-components.md "")                      |
[`Unified Checkout` Integration Methods]

Checkout {#uc-integration-methods-checkout}
===========================================

Checkout UI {#uc-integration-methods-checkout_section_rrx_wlh_njc}
------------------------------------------------------------------

This image shows an example of the `Unified Checkout` checkout UI. You can display the checkout UI in embedded or sidebar mode.

#### Figure:

`Unified Checkout` Checkout UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-int-checkout-750x300.svg/jcr:content/renditions/original)

Checkout Integration JavaScript Example {#uc-integration-methods-checkout_section_iqk_xlh_njc}
----------------------------------------------------------------------------------------------

```
// ============================================================
// CHECKOUT API - USAGE GUIDE
// ============================================================

// ============================================================
// FLOW 1: AUTO-PROCESSING (autoProcessing: true)
// Mount returns complete payment result
// Defaults to true when completeMandate is in session
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create checkout with auto-processing enabled
const checkout = await client.createCheckout({ autoProcessing: true });

// Mount - automatically processes payment and returns complete result
const paymentResult = await checkout.mount('#payment-buttons');
console.log('Payment complete:', paymentResult);

// Clean up
checkout.destroy();
client.destroy();


// ============================================================
// FLOW 2: MANUAL COMPLETE (autoProcessing: false)
// Mount returns transient token, then the merchant can manually complete payment
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create checkout with auto-processing disabled
const checkout = await client.createCheckout({ autoProcessing: false });

// Mount - returns transient token only
const token = await checkout.mount('#payment-buttons');
console.log('Received token:', token);

// Manually complete the payment
const paymentResult = await checkout.complete(token);
console.log('Payment complete:', paymentResult);

// Clean up
checkout.destroy();
client.destroy();


// ============================================================
// FLOW 3: TRANSIENT TOKEN ONLY (autoProcessing: false, no complete)
// Mount returns transient token only — server handles payment authorization
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create checkout with auto-processing disabled
const checkout = await client.createCheckout({ autoProcessing: false });

// Mount - returns transient token only
const transientToken = await checkout.mount('#payment-buttons');
console.log('Received token:', transientToken);

// Pass transient token to your server for payment authorization
sendToServer(transientToken);

// Clean up
checkout.destroy();
client.destroy();


// ============================================================
// MOUNT OPTIONS
// ============================================================

// Sidebar - payment selection and form rendered in the same container
const result = await checkout.mount('#payment-buttons');

// Embedded - payment selection and form rendered in separate containers
const result = await checkout.mount({
    paymentSelection: '#payment-buttons',
    paymentScreen: '#payment-form'
});


// ============================================================
// LIFECYCLE METHODS (available in all flows)
// ============================================================

// Mount - display the checkout
const result = await checkout.mount('#payment-buttons');

// Destroy checkout instance
checkout.destroy();

// Destroy client instance
client.destroy();


// ============================================================
// ERROR HANDLING
// ============================================================

try {
    const client = await window.VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout();
    const result = await checkout.mount('#payment-buttons');
    sendToServer(result);
} catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
        handleError(error.reason, error.message);
    }
} finally {
    checkout.destroy();
    client.destroy();
}


// ============================================================
// SUPPORTED PAYMENT TYPES
// ============================================================

// All payment types configured in the session are displayed
// checkout.mount() renders buttons for every type in the session
```

{#uc-integration-methods-checkout_codeblock_and_3jr_vjc}

Button {#uc-integration-methods-buttons}
========================================

Button UI {#uc-integration-methods-buttons_section_rrx_wlh_njc}
---------------------------------------------------------------

This image shows the `Unified Checkout` button UI.

#### Figure: {#uc-integration-methods-buttons_fig_j5v_dqh_njc}

`Unified Checkout` Button UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-int-buttons-750x400.svg/jcr:content/renditions/original)

Button Integration JavaScript Example {#uc-integration-methods-buttons_section_iqk_xlh_njc}
-------------------------------------------------------------------------------------------

```
// ============================================================
// BUTTON API - USAGE GUIDE
// ============================================================

// ============================================================
// FLOW 1: AUTO-PROCESSING (autoProcessing: true)
// Mount returns complete payment result
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create button with auto-processing enabled
const button = client.createButton('GOOGLEPAY', {
    autoProcessing: true
});

// Mount - automatically processes payment and returns complete result
const paymentResult = await button.mount('#payment-container');
console.log('Payment complete:', paymentResult);

// Clean up
button.destroy();


// ============================================================
// FLOW 2: MANUAL COMPLETE (autoProcessing: false)
// Mount returns transient token, then the merchant can manually complete payment
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create button with auto-processing disabled
const button = client.createButton('GOOGLEPAY', {
    autoProcessing: false
});

// Mount - returns transient token only
const token = await button.mount('#payment-container');
console.log('Received token:', token);

// Manually complete the payment
const paymentResult = await button.complete(token);
console.log('Payment complete:', paymentResult);

// Clean up
button.destroy();


// ============================================================
// FLOW 3: TRANSIENT TOKEN ONLY (autoProcessing: false, no complete)
// Mount returns transient token only.
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create button with auto-processing disabled
const button = client.createButton('GOOGLEPAY', {
    autoProcessing: false
});

// Mount - returns transient token only
const token = await button.mount('#payment-container');
console.log('Received token:', token);

// Clean up
button.destroy();


// ============================================================
// LIFECYCLE METHODS (available in all flows)
// ============================================================

// Mount - display the payment button
const result = await button.mount('#payment-container');

// Unmount - hide the button without destroying it
button.unmount();

// Remount - can mount again after unmounting
await button.mount('#payment-container');

// Check mounted state
const mounted = button.isMounted();  // true or false

// Destroy - permanently destroy the button
button.destroy();

// Check destroyed state
const destroyed = button.isDestroyed();  // true or false


// ============================================================
// EVENT HANDLING (optional for all flows)
// ============================================================

// Subscribe to events
button.on('mounted', () =&gt; console.log('Button displayed'));
button.on('unmounted', () =&gt; console.log('Button hidden'));
button.on('destroyed', () =&gt; console.log('Button destroyed'));


// ============================================================
// SUPPORTED PAYMENT TYPES
// ============================================================

client.createButton('GOOGLEPAY');  // Google Pay
client.createButton('APPLEPAY');   // Apple Pay
```

{#uc-integration-methods-buttons_codeblock_fnn_3jr_vjc}

Trigger {#uc-integration-methods-trigger}
=========================================

Trigger UI {#uc-integration-methods-trigger_section_rrx_wlh_njc}
----------------------------------------------------------------

This image shows the `Unified Checkout` trigger UI.

#### Figure: {#uc-integration-methods-trigger_fig_unb_2qh_njc}

`Unified Checkout` Trigger UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-int-trigger-750x315.svg/jcr:content/renditions/original)

Trigger Integration JavaScript Example {#uc-integration-methods-trigger_section_iqk_xlh_njc}
--------------------------------------------------------------------------------------------

```
// ============================================================
// TRIGGER API - USAGE GUIDE V2
// ============================================================

// Triggers load the payment UI without displaying the Unified Checkout
// button. Use when a custom event should initiate the payment flow.
// Supported payment types: PANENTRY and CLICKTOPAY only.

// IMPORTANT: Trigger always opens in SIDEBAR mode only.
// The displayMode: 'sidebar' option must be set when creating the trigger.
// The merchant provides their own button/element to launch the payment flow.

// ============================================================
// FLOW 1: AUTO-PROCESSING (autoProcessing: true)
// Mount returns complete payment result
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create trigger — sidebar is the only supported display mode for Trigger
const trigger = client.createTrigger('PANENTRY', {
    displayMode: 'sidebar',
    autoProcessing: true
});

// Mount is called when the merchant's own button is clicked
// This opens the sidebar payment UI and resolves when payment is complete
document.getElementById('your-pay-button').addEventListener('click', async () =&gt; {
    const paymentResult = await trigger.mount('#payment-container');
    console.log('Payment complete:', paymentResult);
});

// Clean up
trigger.destroy();


// ============================================================
// FLOW 2: MANUAL COMPLETE (autoProcessing: false)
// Mount returns transient token, then the merchant can manually complete payment
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create trigger with auto-processing disabled
const trigger = client.createTrigger('PANENTRY', {
    displayMode: 'sidebar',
    autoProcessing: false
});

// Mount is called when the merchant's own button is clicked
document.getElementById('your-pay-button').addEventListener('click', async () =&gt; {
    const token = await trigger.mount('#payment-container');
    console.log('Received token:', token);

    // Manually complete the payment
    const paymentResult = await trigger.complete(token);
    console.log('Payment complete:', paymentResult);
});

// Clean up
trigger.destroy();


// ============================================================
// FLOW 3: TRANSIENT TOKEN ONLY (autoProcessing: false, no complete)
// Mount returns transient token only — server handles payment authorisation
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create trigger with auto-processing disabled
const trigger = client.createTrigger('PANENTRY', {
    displayMode: 'sidebar',
    autoProcessing: false
});

// Mount is called when the merchant's own button is clicked
document.getElementById('your-pay-button').addEventListener('click', async () =&gt; {
    const token = await trigger.mount('#payment-container');
    console.log('Received token:', token);

    // Pass transient token to your server for payment authorisation
    sendToServer(token);
});

// Clean up
trigger.destroy();


// ============================================================
// LIFECYCLE METHODS (available in all flows)
// ============================================================

// Mount - opens the sidebar payment UI (called from merchant's own click handler)
const result = await trigger.mount('#payment-container');

// Unmount - hide the form without destroying it
trigger.unmount();

// Remount - can mount again after unmounting
await trigger.mount('#payment-container');

// Check mounted state
const mounted = trigger.isMounted();  // true or false

// Destroy - permanently destroy the trigger
trigger.destroy();

// Check destroyed state
const destroyed = trigger.isDestroyed();  // true or false


// ============================================================
// EVENT HANDLING (optional for all flows)
// ============================================================

// Subscribe to events
trigger.on('mounted', () =&gt; console.log('Sidebar payment UI displayed'));
trigger.on('unmounted', () =&gt; console.log('Sidebar payment UI hidden'));
trigger.on('error', (err) =&gt; console.error('Trigger error:', err.code, err.message));
trigger.on('destroyed', () =&gt; console.log('Trigger destroyed'));


// ============================================================
// SUPPORTED TRIGGER TYPES
// ============================================================

// IMPORTANT: When using createTrigger() for Click to Pay,
// you must create a custom UI. See Click to Pay UI Guidelines.

client.createTrigger('PANENTRY', { displayMode: 'sidebar' });   // Manual card entry
client.createTrigger('CLICKTOPAY', { displayMode: 'sidebar' }); // Click to Pay


// ============================================================
// CAPTURE CONTEXT REQUIREMENT
// ============================================================

// The capture context allowedPaymentTypes must include the payment type
// used in createTrigger(). For PANENTRY, ensure your session request includes:
//
// "allowedPaymentTypes": ["PANENTRY", ...]
//
// Without PANENTRY in allowedPaymentTypes, createTrigger('PANENTRY') will
// fail silently and the sidebar will not open.
```

Components {#uc-integration-methods-components}
===============================================

Components UI {#uc-integration-methods-components_section_rrx_wlh_njc}
----------------------------------------------------------------------

This image shows the `Unified Checkout` components UI.

#### Figure: {#uc-integration-methods-components_fig_tvf_2qh_njc}

`Unified Checkout` Components UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-int-components-750x400.svg/jcr:content/renditions/original)

Components Integration JavaScript Example {#uc-integration-methods-components_section_iqk_xlh_njc}
--------------------------------------------------------------------------------------------------

```
// ============================================================
// COMPONENTS API - USAGE GUIDE
// ============================================================

// ============================================================
// FLOW 1: AUTO-PROCESSING (autoProcessing: true)
// Mount returns complete result
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create component with auto-processing enabled
const component = client.createComponent('PANENTRY', {
    autoProcessing: true
});

// Mount - automatically processes payment and returns complete result
const paymentResult = await component.mount('#payment-container');
console.log('Payment complete:', paymentResult);

// Clean up
component.destroy();


// ============================================================
// FLOW 2: MANUAL COMPLETE (autoProcessing: false)
// Mount returns transient token, then the merchant can manually complete payment
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create component with auto-processing disabled
const component = client.createComponent('PANENTRY', {
    autoProcessing: false
});

// Mount - returns transient token only
const token = await component.mount('#payment-container');
console.log('Received token:', token);

// Manually complete the payment
const paymentResult = await component.complete(token);
console.log('Payment complete:', paymentResult);

// Clean up
component.destroy();


// ============================================================
// FLOW 3: TRANSIENT TOKEN ONLY (autoProcessing: false, no complete)
// Mount returns transient token only.
// ============================================================

// Initialize the Unified Checkout client
const client = await window.VAS.UnifiedCheckout(sessionJWT);

// Create component with auto-processing disabled
const component = client.createComponent('PANENTRY', {
    autoProcessing: false
});

// Mount - returns transient token only
const token = await component.mount('#payment-container');
console.log('Received token:', token);

// Clean up
component.destroy();


// ============================================================
// LIFECYCLE METHODS (available in all flows)
// ============================================================

// Mount - display the payment form
const result = await component.mount('#payment-container');

// Unmount - hide the form without destroying it
component.unmount();

// Remount - can mount again after unmounting
await component.mount('#payment-container');

// Check mounted state
const mounted = component.isMounted();  // true or false

// Destroy - permanently destroy the component
component.destroy();

// Check destroyed state
const destroyed = component.isDestroyed();  // true or false


// ============================================================
// EVENT HANDLING (optional for all flows)
// ============================================================

// Subscribe to events
component.on('mounted', () =&gt; console.log('Form displayed'));
component.on('unmounted', () =&gt; console.log('Form hidden'));
component.on('destroyed', () =&gt; console.log('Component destroyed'));

// ============================================================
// SUPPORTED PAYMENT TYPES
// ============================================================

client.createComponent('PANENTRY');    // Manual card entry
client.createComponent('CLICKTOPAY');  // Click to Pay
client.createComponent('CHECK');       // Check payment (US & CA Only)
```

{#uc-integration-methods-components_codeblock_y3v_3sh_njc}  
When `CLICKTOPAY` is included in allowedPaymentTypes, use `client.createComponent('CLICKTOPAY')` and not `client.createComponent('PANENTRY')`. `CLICKTOPAY` renders the full `Click to Pay` lookup flow and automatically displays an option to pay with a new card for users without a `Click to Pay` profile. This option ensures that the PAN entry flow is also included. Using only `PANENTRY` bypasses `Click to Pay`, even if it is included in your capture context.  
This table provides an overview of how to use the components integration method:

|       allowedPaymentTypes Method        |                                   Components Use                                   |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `CLICKTOPAY` with or without `PANENTRY` | `createComponent('CLICKTOPAY', ...)`                                               |
| `PANENTRY` only                         | `createComponent(PANENTRY, ...)`                                                   |
| Multiple wallets + `CLICKTOPAY`         | `createCheckout(...)` The Checkout API renders all checkout options automatically. |
[Components Integration Method]

> IMPORTANT
> There is no error if you load ` PANENTRY ` when ` CLICKTOPAY ` is included in your capture context. The component will be mounted successfully, but ` Click to Pay ` is not shown in the UI. This may result in one-time password emails on the server-side but no ` Click to Pay ` UI displaying on the client side.

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
Complete mandate enhancement to support `Payer Authentication` for manual card entry for Relay, Mastercard, American Express, Discover, JCB, Cartes Bancaires, China UnionPay, and ELO card brands.
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

Client-Side Set Up {#uc-getting-started-cs-setup-intro}
=======================================================

This section contains the information you need to set up the client side. You use the `Unified Checkout` JavaScript library to add the payment interface to your e-commerce site. It has two primary components:

* The button widget, which lists the payment methods available to the customer.
* The payment acceptance page, which captures payment information from the cardholder. You can set up the payment acceptance page to be embedded with your webpage or added as a sidebar.

Follow these steps to set up the client:

1. Load the JavaScript library.
2. Initialize the accept object, the capture context JWT. For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").
3. Initialize the unified payment object with optional parameters.
4. Show the button list or payment acceptance page or both.
5. Process the payment request using the instructions included within the capture mandate.

{#uc-getting-started-cs-setup-intro_ul_m5t_gwq_npb}  
The response to these interactions is a transient token that you can use to retrieve the payment information captured by the UI.  
For information about handling the errors that may occur on the client-side, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

Loading the JavaScript Library {#uc-getting-started-cs-js-library-intro}
========================================================================

Use the client library asset path and client library integrity value that is returned by the capture context response to invoke `Unified Checkout` on your page.  
You must retrieve these values from the clientLibrary and clientLibraryIntegrity fields that are returned in the JWT from `https://apitest.cybersource.com``/uc/v1/sessions`. You can use these values to create your script tags.  
You must perform this process for each transaction, as these values are unique for each transaction. You must avoid hard-coding values for the clientLibrary and clientLibraryIntegrity fields to prevent client-side errors.  
For example, a response from `https://apitest.cybersource.com``/uc/v1/sessions` would include:

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
> For information about the client-side API, see [JavaScript API Reference](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix-js-reference-v1.md "").

JavaScript Example: Initializing the SDK {#uc-getting-started-cs-js-library-example}
====================================================================================

```
const client = await VAS.UnifiedCheckout(sessionJWT);
```

In this example, `sessionJWT` refers to the capture context JWT.

JavaScript Example: Displaying the Button List {#uc-getting-started-cs-js-button-example}
=========================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the embedded `Unified Checkout` tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named components that are replaced with `Unified Checkout`'s iframes.

```
// Sidebar
const result = await checkout.mount('#buttons');

// Embedded
const result = await checkout.mount({
  paymentSelection: '#buttons',
  paymentScreen: '#form'
});
```

JavaScript Example: Client-Defined Trigger for `Click to Pay` or PAN Entry {#uc-getting-started-cs-js-trigger-ctp-pan-example}
==============================================================================================================================

When you display `CLICKTOPAY` or `PANENTRY` as allowed payment types, you can load the UI without displaying the `Unified Checkout` checkout button. You can do this by creating a trigger that defines what event loads the UI.  
You can create a trigger only for `CLICKTOPAY` or `PANENTRY` payment methods:

```
//PAN Entry

const trigger = client.createTrigger('PANENTRY');

//Click to Pay

const trigger = client.createTrigger('CLICKTOPAY');
```

> IMPORTANT
> When you use the ` client.createTrigger() ` method for ` Click to Pay `, you must create a custom UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-appendix-ui-ux.md "").

JavaScript Example: Processing a Payment {#uc-getting-started-cs-js-payment-example}
====================================================================================

Payment is initiated when `Unified Checkout` captures the customer's payment information by calling the `client.createCheckout()`. When `autoProcessing` is set to `true`, the payment is completed. When `autoProcessing` is set to `false`, you can manually complete the payment using `checkout.complete(token)`. See [Authorizations with a Transient Token](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro/uc-auth-tokens.md "").

```
// Automatic (default when completeMandate is in session)
const checkout = await client.createCheckout({ autoProcessing: true });
const result = await checkout.mount('#buttons');
// result is the completed transaction — no need to call complete()

// Manual - similar to v0
const checkout = await client.createCheckout({ autoProcessing: false });
const token = await checkout.mount('#buttons');
const result = await checkout.complete(token);
```

JavaScript Example: Authorization {#uc-session-integrate-ex-auth}
=================================================================

Collect payment information and process an authorization. You must initiate a separate capture request to move funds and complete the transaction.

```
async function launchCheckout() {
  try {
    const client = await VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout();
    const result = await checkout.mount('#payment-buttons');

    // result contains the completed payment result JWT
    // Send result to your server for verification
    sendToServer(result);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

Because the session includes completeMandate, `autoProcessing` defaults to `true` and `mount()` returns the completed payment result directly.

JavaScript Example: Sale {#uc-session-integrate-ex-sale}
========================================================

Collect payment information and process a sale. A sale is a combined authorization and capture in a single step.

```
async function launchCheckout() {
  try {
    const client = await VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout();
    const result = await checkout.mount('#payment-buttons');

    // result contains the completed payment result JWT
    // Send result to your server for verification
    sendToServer(result);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

JavaScript Example: Sale with `Decision Manager` {#uc-session-integrate-ex-sale-dm}
===================================================================================

Collect payment information and process a sale while running `Decision Manager` fraud screening before the payment is initiated.

```
async function launchCheckout() {
  try {
    const client = await VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout();
    const result = await checkout.mount('#payment-buttons');

    // result contains the completed payment result JWT
    // Send result to your server for verification
    sendToServer(result);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

JavaScript Example: No Service Orchestration {#uc-session-integrate-ex-manual-tkn}
==================================================================================

Collect payment information and receive a transient token. Your server handles payment authorization and any follow-on services directly.

```
async function launchCheckout() {
  try {
    const client = await VAS.UnifiedCheckout(sessionJWT);
    const checkout = await client.createCheckout({ autoProcessing: false });
    const transientToken = await checkout.mount('#payment-buttons');

    // transientToken is a JWT — send it to your server
    // Your server uses the transient token to authorize the payment
    sendToServer(transientToken);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

Without a completeMandate, `autoProcessing` defaults to `false` and the `mount()` call returns a transient token that you pass to your server for payment authorization. For information about how to use the transient token in an authorization request, see [Transient Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro.md "").

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
    name="sessionJWT"
    value="[INSERT sessionJWT HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sessionJWT = document.getElementById("sessionJWT").value;
    
    async function launchCheckout() {
      try {
        const client = await VAS.UnifiedCheckout(sessionJWT);
        const checkout = await client.createCheckout();
        const result = await checkout.mount('#payment-buttons');

        // result contains the completed payment result JWT
        // Send result to your server for verification
        sendToServer(result);
      } catch (error) {
        if (error.name === 'UnifiedCheckoutError') {
          handleError(error.reason, error.message);
        }
      } finally {
        checkout.destroy();
        client.destroy();
      }
    }

    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

JavaScript Example: Setting Up with the Embedded Component {#uc-getting-started-button-widget-embedded}
=======================================================================================================

The main difference between using an embedded component and the sidebar is that the `VAS.UnifiedCheckout(sessionJWT)` object is set to `false`, and the location of the payment screen is passed in the containers argument.

> IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the side bar.

```
&lt;html&gt;
&lt;head&gt;
  &lt;script
    src="[INSERT clientLibrary VALUE HERE]"
    integrity="[INSERT clientLibraryIntegrity VALUE HERE]"
    crossorigin="anonymous"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Unified Checkout Integration&lt;/h1&gt;
  &lt;input
    type="hidden"
    id="sessionJWT"
    name="sessionJWT"
    value="[INSERT sessionJWT HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sessionJWT = document.getElementById("sessionJWT").value;

    async function launchCheckout() {
      let client;
      let checkout;

      try {
        client = await VAS.UnifiedCheckout(sessionJWT);
        checkout = await client.createCheckout();
        const result = await checkout.mount('#payment-buttons');

        // result contains the completed payment result JWT
        // Send result to your server for verification
        sendToServer(result);
      } catch (error) {
        if (error.name === 'UnifiedCheckoutError') {
          handleError(error.reason, error.message);
        }
      } finally {
        if (checkout) {
          checkout.destroy();
        }

        if (client) {
          client.destroy();
        }
      }
    }

    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

Configuration {#uc_intro_setup}
===============================

This section contains the information required to configure `Unified Checkout`.

Configure the `Unified Checkout` Merchant Experience {#uc-intro-setup-ebc}
==========================================================================

The `Unified Checkout` merchant experience interface provides complete control over your checkout experience by using dedicated configuration screens accessible through the `Business Center`:

#### Figure:

`Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original)  
This option is low-code and provides a user-friendly approach to customization of your `Unified Checkout` UI.  
Configure each of these components of the checkout experience:

* **Payment Options** : Add, remove, and arrange payment methods. For information about configuring payment methods, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "") and [Process Payments with Unified Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-pay-processing-intro.md "").
* **Look \& feel** : Configure visual appearance and branding. For information about configuring the look and feel, see [Customize the Unified Checkout Look and Feel](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-look-and-feel.md "").
* **Customer information and payment flow** : Control data collection and manage payment processing service. For information about configuring customer data, see [Configure Customer Data and Payment Flow](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-customer-data.md "").

You can also manage permissions as a direct merchant or as a portfolio administrator. For information about managing permissions, see [Manage Permissions](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-manage-permissions-intro.md "").

Enable `Unified Checkout` {#uc-enabling-ebc}
============================================

To begin using `Unified Checkout`, you must first ensure that your merchant ID (MID) is configured to use the service and that any payment methods you intend to use are properly set up.

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc-enabling-ebc_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc-enabling-ebc_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc-enabling-ebc_step-1}
   {#uc-enabling-ebc_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original) {#uc-enabling-ebc_step-2}
   {#uc-enabling-ebc_step-2}

3. The `Unified Checkout` configuration interface provides complete low-code control over your checkout experience by using dedicated configuration screens accessible through the `Business Center`. The configuration interface is organized into separate screens, each accessible from the *My customer experience* page. Configure each of these components of the checkout experience:

   * **Payment Options** : Add, remove, and arrange payment methods. For information about configuring payment methods, see [Configure Payment Options](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-payment-options.md "").
   * **Look \& feel** : Configure visual appearance and branding. For information about configuring the look and feel, see [Customize the Unified Checkout Look and Feel](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-look-and-feel.md "").
   * **Customer information and payment flow** : Control data collection and manage payment processing service. For information about configuring customer data, see [Configure Customer Data and Payment Flow](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-intro-customer-data.md "").
     {#uc-enabling-ebc_step-3}
     {#uc-enabling-ebc_step-3} {#uc-enabling-ebc_enable-uc}

Configure Payment Options {#uc_intro_payment_options}
=====================================================

Payment Options in the `Business Center` enable you to control which payment methods appear in your checkout and in what order. Follow these steps to customize the available payment options in `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_payment_options_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_payment_options_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_payment_options_step-1}
   {#uc_intro_payment_options_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Payment Options Merchant Experience ![Image that shows the Unified Checkout payment options
   page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-payment-800x875.png/jcr:content/renditions/original) {#uc_intro_payment_options_step-2}
   {#uc_intro_payment_options_step-2}

3. In the Payment Options section, click **Manage**. The Payment Options page appears.{#uc_intro_payment_options_step-3}
   {#uc_intro_payment_options_step-3}

4. Under Payment options, click the checkbox next to each payment method that you want to display in your checkout UI. Click the drag icon ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-drag-icon-15x25.svg/jcr:content/renditions/original) ) to rearrange the order of the payment options.  
   IMPORTANT Some payment options are set at the portfolio level and cannot be reordered. When you see a pin icon next to a payment option, you cannot move that payment option in the list of available methods. You must contact your portfolio administrator if you want to reorder the list of available payment options.  
   These payment options are supported by `Unified Checkout`:

   * [Apple Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay/uc-enable-digital-pay-applepay.md "")
   * [`Click to Pay`](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-enable-digital-pay-ctp.md "")
   * [Google Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay/uc-enable-digital-pay-google.md "")
   * [eCheck](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-echeck/uc-enable-digital-pay-echeck.md "")
   * [Konbini](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-ppr/uc-pay-methods-ppr-konbini.md "")
   * [Bancontact](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-bancontact.md "")
   * [DragonPay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-dragonpay.md "")
   * [iDeal](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-ideal.md "")
   * [MyBank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-mybank.md "")
   * [Multibanco](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-multibanco.md "")
   * [Przelewy24\|P24](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-p24.md "")
   * [Tink Pay By Bank](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-obt/uc-pay-methods-obt-tink.md "")
   * [Afterpay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro/uc-pay-methods-bnpl/uc-pay-methods-bnpl-afterpay.md "")
     {#uc_intro_payment_options_step-4}
     {#uc_intro_payment_options_step-4}
5. Click **Manage** next to each payment type that you want to configure. The configuration page for the selected payment type appears.{#uc_intro_payment_options_step-5}
   {#uc_intro_payment_options_step-5}

6. Under card brands, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to display the card brand logos in your button list.  
   Click the checkbox next to each card brand that you want to display in your checkout UI. Click the drag icon ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-drag-icon-15x25.svg/jcr:content/renditions/original) ) to rearrange the order of the card brands. {#uc_intro_payment_options_step-6}
   {#uc_intro_payment_options_step-6}

7. Click **Save and publish** to save your payment options configuration settings.{#uc_intro_payment_options_step-7}
   {#uc_intro_payment_options_step-7} {#uc_intro_payment_options_enable-uc}

Customize the `Unified Checkout` Look and Feel {#uc_intro_look_and_feel}
========================================================================

Follow these steps to customize the appearance of `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_look_and_feel_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_look_and_feel_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_look_and_feel_step-1}
   {#uc_intro_look_and_feel_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Look and Feel Merchant Experience ![Image that shows the Unified Checkout Look & feel
   merchant experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-look-800x875.png/jcr:content/renditions/original) {#uc_intro_look_and_feel_step-2}
   {#uc_intro_look_and_feel_step-2}

3. In the Look \& Feel section, click **Configure**. The Look and feel page appears.{#uc_intro_look_and_feel_step-3}
   {#uc_intro_look_and_feel_step-3}

4. If you want to use AI to determine the look and feel, under AI brand studio, click **Browse** the upload a screenshot of your website. These components are updated using the colors from the screenshot you provide:

   * Button list background color
   * Card checkout outline and text colors
   * Header and checkout font background colors  
     Proceed to the next steps to manually customize these and other components of the `Unified Checkout` appearance. {#uc_intro_look_and_feel_step-4}
     {#uc_intro_look_and_feel_step-4}
5. Under Button customizations, select the options for your button list. These customizations are available:

   **Universal Button Shape**
   :
   Use the Button shape drop-down menu to select if you want a sharp corner, rounded corner, or pill button:

       #### Figure: {#uc_intro_look_and_feel_fig_uc-buttons}

       `Unified Checkout` Button Shapes ![Diagram that shows the Unified Checkout button shapes.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-shape-650x150.svg/jcr:content/renditions/original)

   **Button List**
   :
   Use the color selector or enter a HEX code in the Button list background color text box to customize the background color of your button list. To review the button list preview, see [Button List](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-ui-config-examples/uc-ui-config-ex-button-list.md "").
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

   **Card Checkout and `Click to Pay` Button**
   :
   Use the card checkout button label drop-down menu to select the text that appears on the checkout button. These text options are available:
   * Pay with card
   * Card payment
   * Checkout with card (default)
   * Debit/Credit payment
   * Donate with card
   * Subscribe with card

   **Card Checkout Buttons**
   :
   Use the button style drop-down menu to select if you want an outlined or filled checkout button. Select the button fill and text colors using the color selector or HEX code:

       #### Figure: {#uc_intro_look_and_feel_fig_uc-button-fill}

       `Unified Checkout` Button Style ![Diagram that shows the Unified Checkout buttons as filled or unfilled.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-style-650x150.svg/jcr:content/renditions/original)

   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.
   {#uc_intro_look_and_feel_step-5}
   {#uc_intro_look_and_feel_step-5}

6. Under Checkout customizations, select the options for your checkout experience. These customizations are available:

   Font
   :
   Use the font drop-down menu to select the font you want to use. These fonts are available:
   * Inter
   * Monserrat
   * Open Sans
   * Raleway
   * Roboto Slab

       #### Figure: {#uc_intro_look_and_feel_fig_uc-button-example}

       `Unified Checkout` Fonts ![Diagram that shows the different Unified Checkout fonts.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-font-650x460.svg/jcr:content/renditions/original)

   :
   Select the background color using the color selector or HEX code.
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

   Header Customization
   :
   Select the color you want to use in your header using the color selector or HEX code.
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.
   {#uc_intro_look_and_feel_step-6}
   {#uc_intro_look_and_feel_step-6}

7. Click **Save and publish** to save your look and feel customization. The Ready to publish popup window appears.{#uc_intro_look_and_feel_step-7}
   {#uc_intro_look_and_feel_step-7}

8. If you are done editing, click **Publish now** to publish your changes. If you need to make more changes, click **Keep editing** to return to the Look and feel page. To review your changes, click through the example screens. For more information about the UI previews, see [Look and Feel UI Examples](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-ui-config-examples.md "").{#uc_intro_look_and_feel_step-8}
   {#uc_intro_look_and_feel_step-8} {#uc_intro_look_and_feel_enable-uc}

Look and Feel UI Examples {#uc_ui_config_examples}
==================================================

These examples show the different preview screens for each look and feel customization feature:

Button List {#uc_ui_config_ex_button_list}
==========================================

This example shows the button list:

#### Figure:

Screen 1: Button List ![Image that shows the Unified Checkout Look and Feel UI button list.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-button-list-548x632.svg/jcr:content/renditions/original)

Contact Details {#uc_ui_config_ex_contact}
==========================================

This example shows the contact details that appear during checkout:

#### Figure:

Screen 2: Contact Details ![Image that shows the Unified Checkout Look and Feel UI contact details.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-contact-details-548x632.svg/jcr:content/renditions/original)

Saved Cards {#uc_ui_config_ex_saved_cards}
==========================================

This example shows the saved card payment details that appear during checkout:

#### Figure:

Screen 3: Saved Cards ![Image that shows the Unified Checkout Look and Feel UI saved card details.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-saved-cards-548x632.svg/jcr:content/renditions/original)

Card Entry {#uc_ui_config_ex_card_entry}
========================================

This example shows the card entry payment details that appear during checkout:

#### Figure:

Screen 4: Card Entry ![Image that shows the Unified Checkout Look and Feel UI card entry checkout details.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-card-entry-548x632.svg/jcr:content/renditions/original)

Review Details {#uc_ui_config_ex_review}
========================================

This example shows the review contact details that appear at the end of checkout:

#### Figure:

Screen 5: Review ![Image that shows the Unified Checkout Look and Feel UI review checkout details.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-review-details-548x632.svg/jcr:content/renditions/original)

Configure Customer Data and Payment Flow {#uc_intro_customer_data}
==================================================================

Use the Customer data and payment flow section of the `Business Center` to configure the information that you want to collect during checkout. Follow these steps to customize the appearance of `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_customer_data_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_customer_data_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_customer_data_step-1}
   {#uc_intro_customer_data_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Data and Payment Flow Merchant Experience ![Image that shows the Unified Checkout customer data
   and payment flow merchant experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-custdata-800x875.png/jcr:content/renditions/original) {#uc_intro_customer_data_step-2}
   {#uc_intro_customer_data_step-2}

3. In the Customer data and payment flow section, click **Manage**. The Customer information and payment flow page appears.{#uc_intro_customer_data_step-3}
   {#uc_intro_customer_data_step-3}

4. Under Contact details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Email address and Mobile phone number to collect the customer email address and phone number during checkout.{#uc_intro_customer_data_step-4}
   {#uc_intro_customer_data_step-4}

5. Under Payment details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Billing address to collect the cardholder billing address.{#uc_intro_customer_data_step-5}
   {#uc_intro_customer_data_step-5}

6. Under Payment details, in the Billing address drop-down menu, select the billing address information for payment verification:

   #### ADDITIONAL INFORMATION {#uc_intro_customer_data_step-6}

   * **Full address**: Request the full cardholder billing address during checkout.
   * **Zip code only**: Request only the zip code of the cardholder billing address during checkout.
     {#uc_intro_customer_data_step-6}
7. Under Payment details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Shipping address to collect the cardholder shipping address.{#uc_intro_customer_data_step-7}
   {#uc_intro_customer_data_step-7}

8. Under Payment details, in the Shipping address drop-down menu, select the countries that you ship to.{#uc_intro_customer_data_step-8}
   {#uc_intro_customer_data_step-8}

9. Under Checkout review step, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to display a review page for the customer to confirm the payment and shipping address.{#uc_intro_customer_data_step-9}
   {#uc_intro_customer_data_step-9}

10. Under payment processing and \& service orchestration, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) in the Payment processing section to control how to process transactions:  
    You can turn payment processing on or off:

    * **Payment Processing ON** : `Unified Checkout` handles the complete payment for you automatically. When payment processing is on, you can select how transactions are processed:
      * **Preferred auth**: Choose this option to authorize the payment when possible.
      * **Sale**: Choose this option to capture the funds immediately.
    * **Payment Processing OFF**: You must complete the payment independently using CARD or another selected gateway.

    For information about enabling or disabling payment processing in `Unified Checkout`, see [Process Payments with Unified Checkout](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-pay-processing-intro.md ""). {#uc_intro_customer_data_step-10}
    {#uc_intro_customer_data_step-10}

11. Under save customer information in payment processing and \& service orchestration, slide the toggle to the right to prompt the user to save their payment information for future use.  
    Saving customer payment details can significantly improve the checkout experience for returning customers. There are two approaches that you can use:

    * **Ask for consent to save payment information for future use**: This option displays a checkbox during checkout that asks customers if they want their payment details saved. You can enable this option regardless of if payment processing is enabled at any time.
    * **Store payment details securely in your `TMS` vault** : This option saves payment information using secure encryption and links directly to your `TMS` vault. This enables faster checkout for returning customers by using tokens rather than raw card data.

    > IMPORTANT If you already have cardholder consent (for example, if it was obtained during account creation or through another verified process) or consent is not required for your flow, you should not display or request consent again in the UI.
    > {#uc_intro_customer_data_step-11}
    > {#uc_intro_customer_data_step-11}

12. Under Fraud detection in payment processing and \& service orchestration, use the drop-down menu to turn fraud detection with `Decision Manager` or `Fraud Management Essentials` **On** or **Skip**.{#uc_intro_customer_data_step-12}
    {#uc_intro_customer_data_step-12}

13. Under Localized payment settings, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to enable these features:

    #### ADDITIONAL INFORMATION {#uc_intro_customer_data_step-13}

    * **Combo cards**: Enable cardholders to decide how to process their payments.
    * **Brazil tax ID**: Collect a customer's CPF or CNPJ at checkout.

    > IMPORTANT Combo cards and tax IDs are only available in Brazil.
    > {#uc_intro_customer_data_step-13}

14. Click **Save and publish** to save your customer payment settings.{#uc_intro_customer_data_step-14}
    {#uc_intro_customer_data_step-14} {#uc_intro_customer_data_enable-uc}

Capture Context Fields in the `Business Center` {#uc_ebc_api_info}
==================================================================

There are some components of `Unified Checkout` that are available in the API, the `Business Center` or both. This section describes which components of the Sessions API capture context object can be configured using the `Business Center`. For a complete list of fields that are available, see the [API Reference](https://developer.cybersource.com/api-reference-assets/index.md#unified-checkout "") in the `Cybersource` Developer Center.

| Parameter                                             | `Business Center` | API      | Notes                                                                                                                                                                                                                                                                                                                                                                 |
|:------------------------------------------------------|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| allowedCardNetworks                                   | Yes               | Override | Optional. This is the override priority order: 1. API 2. Merchant experience profile 3. Portfolio profile                                                                                                                                                                                                                                                             |
| allowedPaymentTypes                                   | Yes               | Override | Optional. This is the priority order: 1. API (payment types that are not enabled are removed) 2. Merchant experience profile (payment types that are not enabled are removed) 3. Portfolio profile (all payment types are enabled at the profile level) > IMPORTANT > ` SRCCARD `, ` SRCMASTERCARD `, and ` SRCAMEX ` are not supported. You must use ` CLICKTOPAY `. |
| paymentConfigurations                                 | Partial           | Yes      | Allows per-transaction payment type configuration overrides. This is available only in clientVersion `1.0` or later.                                                                                                                                                                                                                                                  |
| paymentConfigurations.CLICKTOPAY                      | Yes               | Override | Default values can be set in the `Business Center`.                                                                                                                                                                                                                                                                                                                   |
| paymentConfigurations.CLICKTOPAY. autoCheckEnrollment | Yes               | Override | This payment configuration is part of the merchant experience.                                                                                                                                                                                                                                                                                                        |
| paymentConfigurations.GOOGLEPAY                       | Yes               | Override | Default values can be set in the `Business Center`.                                                                                                                                                                                                                                                                                                                   |
| paymentConfigurations.GOOGLEPAY. allowedAuthMethods   | Yes               | Override | This payment configuration is part of the merchant experience.                                                                                                                                                                                                                                                                                                        |
[API Parameters]

Capture Mandate
---------------

| Parameter                | `Business Center` | API      | Default Value |
|:-------------------------|:------------------|:---------|:--------------|
| showConfirmationStep     | Yes               | Override |               |
| billingType              | Yes               | Override |               |
| requestEmail             | Yes               | Override |               |
| requestPhone             | Yes               | Override |               |
| requestShipping          | Yes               | Override |               |
| shipToCountries          | Yes               | Override |               |
| showAcceptedNetworkIcons | Yes               | Override |               |
| comboCard                | Yes               | Override |               |
| requestSaveCredentials   | Yes               | Override |               |
| cpf                      | Yes               | Override |               |
| cpf.required             | Yes               | Override |               |
[Capture Mandate Parameters]

Complete Mandate
----------------

| Parameter              | `Business Center` | API      | Default Value |
|:-----------------------|:------------------|:---------|:--------------|
| type                   | Yes               | Override | `SALE`        |
| decisionManager        | Yes               | Override | `true`        |
| consumerAuthentication | Yes               | Override | `NONE`        |
| tms                    | Yes               | Optional |               |
| tms.tokenCreate        | Yes               | Override | `true`        |
[Complete Mandate Parameters]

Appearance Variables
--------------------

| Parameter / Variable       | `Business Center` | API      | Default Value | Example              |
|:---------------------------|:------------------|:---------|:--------------|:---------------------|
| buttonType                 | Yes               | Override | `CHECKOUT`    | "CHECKOUT"           |
| variables                  | Partial           | Override |               |                      |
| backgroundColor            | Yes               | Override |               | "#FFFFFF"            |
| textColor                  | Yes               | Override |               | "#000000"            |
| headerBackground           | Yes               | Override |               | "#1A237E"            |
| headerForeground           | Yes               | Override |               | "#FFFFFF"            |
| buttonBackground           | Yes               | Override |               | "#E0E0E0"            |
| buttonForeground           | Yes               | Override |               | "#333333"            |
| buttonBorderRadius         | Yes               | Override |               | "4px"                |
| fontFamily                 | Yes               | Override |               | "Roboto Slab, serif" |
| paymentSelectionBackground | Yes               | Override |               | "#F5F5F5"            |
[Top-Level Appearance Parameters and Variables]

Manage Permissions {#uc-manage-permissions-intro}
=================================================

Portfolio administrators can set permissions for new or existing `Business Center` user roles for `Unified Checkout`. Administrators retain full read and write permissions. They enable you to regulate access to specific pages and specify who can access, view, or amend digital products within `Unified Checkout`.  
Portfolio administrators must apply the appropriate user role permission for any existing or newly created `Business Center` user roles for `Unified Checkout`. For information on managing permissions as a portfolio administrator, see [Managing Permissions as a Portfolio Administrator](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-manage-permissions-intro/uc-manage-permissions-port.md "").  
If you are a transacting merchant, you might find that your permissions are restricted. If your permissions are restricted, a message appears indicating that you do not have access, or buttons might appear gray. To make changes to your digital products within `Unified Checkout` that have restricted permissions, contact your portfolio administrator's customer support representative. For more information, see [Managing Permissions as a Direct Merchant](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-manage-permissions-intro/uc-manage-permissions-merch.md "").

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

Process Payments with `Unified Checkout` {#uc_pay_processing_intro}
===================================================================

Payment processing is a payment completion option in your merchant configuration. Your configuration determines if your checkout system automatically handles and finalizes customer payments. When payment processing is enabled, `Unified Checkout` handles the complete payment for you automatically. When payment processing not enabled, you complete payments independently using your selected gateway.

Payment Processing Enabled
--------------------------

`Cybersource` recommends that you enable payment processing if you meet these requirements:

* Your integration is configured with the payment completion step. For more information about completeMandate() see [Complete Mandate](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features/uc-cc-complete-mandate.md "").

* You do not have a designated technical team to process payments.

* Your integration includes any of these features:

  * Fraud checks with `Decision Manager` or `Fraud Management Essentials`
  * `3-D Secure`/ `Payer Authentication`
  * Stored customer credentials with the `Token Management Service` (`TMS`)
* Multiple payment methods  
  When payment processing is enabled, you can choose how payments should be handled:

* **Preferred Authorization**: The payment is authorized first and captured at a later time. This method works well for businesses that ship products to their customers. For example, you authorize the payment when the customer places and order and capture the payment when you ship it.

* **Sale**: The payment is captured immediately. This method works well for service businesses, digital products, and immediate purchases.

> IMPORTANT
> Not all payment methods are compatible with all processing types. Different payment methods work with different payment processing types. You must configure your payment processing settings to be compatible with your integration and review which payment methods are compatible. For information about payment methods and their processing compatibility, see [Payment Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro.md "").

Payment Processing Disabled
---------------------------

`Cybersource` recommends that you disable payment processing if you meet these requirements:

* You want to process payments on `our platform` using your own API requests instead of relying on the automatic payment completion step.
* You want full control over your checkout and payment orchestration flow.
* You only use `Unified Checkout` to collect encrypted payment information and you handle the completion phase through `our platform` APIs or your custom back-end. The completion phase includes authorization, sale, fraud checks, `3-D Secure` and card storage.

When disable payment processing, the checkout system will collect payment information from your customers but you will need to process the actual payment on your end. When payment processing is disabled, you must consider the following:

* Customer payments are not completed automatically.
* Fraud checks and `3-D Secure` using automatic orchestration are disabled.
* Saved credentials and token management using automatic processing are disabled.
* You must handle payment completion yourself.

Webhooks Support {#uc-appendix-webhooks}
========================================

`Unified Checkout` supports webhooks. You can use webhooks to obtain the complete response from the completeMandate call. To receive a webhook notification, you must first subscribe to the webhook.

Prerequisite
------------

Webhook payloads are encrypted. In order to receive a `Unified Checkout` webhook notification, you must enabled message-level encryption (MLE). For information about enabling MLE, see [Enable Message-Level Encryption](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "") in the *Getting Started with REST Developer Guide*.

Integration {#uc-appendix-webhooks_section_zg3_yvq_ljc}
-------------------------------------------------------

Follow these steps to set up your system to support the Webhooks REST API. Some of these steps are dependent on your system's security policy.
1. Set up a server with a URL to receive webhook notifications.
2. Configure your server security to receive webhooks notifications. For more information, see *Set Up Your Security* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-server-security.md "").
3. Create a REST API security key that is compliant with your security policy. Security keys are used to authenticate the requests you send to `Cybersource`. You must create separate keys for the testing and production environments. For more information, see *Create REST API Keys* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro.md "").
4. Request a digital signature key from `Cybersource`. For more information, see *Create a Digital Signature Key* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro.md "").
5. Implement message-level encryption for those events. See *Message-Level Encryption* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").
6. If your system uses the *OAuth* or *OAuth with JWT* security policy, you must provide your OAuth credentials to `Cybersource`. OAuth is not required and Mutual Trust is the default. If you are not using OAuth, skip this step. For more information, see *(Optional) Provide Your OAuth Credentials* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-oauth-cred-intro.md "").
7. Request a list of the products for which your organization is enabled to receive webhook notifications. For more information, see *Retrieve a Lit of Products and Events* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-product-list-intro.md "").

   > IMPORTANT
   > You must enable message-level encryption (MLE) in order to access the webhook response. See *Message-Level Encryption* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

8. Create your webhook subscription event notifications. For more information, see *Create a Webhook Subscription* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro.md "").

Optional Set Up Tasks {#uc-appendix-webhooks_opt-tasks}
-------------------------------------------------------

You can complete these optional tasks after creating a webhook subscription.
* Include a health check URL to enable `Cybersource` to monitor your server's status for reliability. For more information, see *Webhook Health Check URL and Automatic Revalidation* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").
* Customize the retry policy for unresponsive webhook and health check URLs. For more information, see *Configure the Retry Policy* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").
* Validate your digital signature. For more information, see *Validating a Notification with the Digital Signature Key* in the [Webhooks Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro.md#wh-fg-optional-validate-intro "").
  {#uc-appendix-webhooks_ul_xlj_1yq_ljc}

Webhook Events
--------------

| Product ID        | Event Types                    | Description                                                                    |
|:------------------|:-------------------------------|:-------------------------------------------------------------------------------|
| `unifiedCheckout` | `uc.orders.transactionresults` | Full payload response from the payment service call made by `Unified Checkout` |
[`Unified Checkout` Webhook Events]

Set Up Webhook Subscriptions
----------------------------

For information on setting up a webhook for the `unifiedCheckout` product, see the [How to Set Up Webhook Subscriptions](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro.md "") section of the *Webhooks Implementation Guide*.

Example Webhook Payload
-----------------------

**Example: Webhooks Request for `Unified Checkout` Events**

```
{
  "organizationId": "your_merchant_id",
  "webhookId": "2d55e648-d96c-d727-e063-3cb8d30a938e",
  "productId": "unifiedCheckout",
  "eventType": "uc.orders.transactionresults",
  "eventDate": "2025-03-27T08:44:55",
  "payload": {
    "id": "7435188899356405003091",
    "status": "AUTHORIZED",
    "outcome": "AUTHORIZED",
    "details": {
      "processorInformation": {
        "transactionId": "2016011808153910011808153AUTH"
      },
      "paymentInformation": {
        "card": {
          "type": "001"
        }
      },
      "riskInformation": {
        "score": {
          "result": "42"
        }
      }
    }
  }
}
```

The `payload` field object contains the same fields as the response from a direct payment authorization request. Use the `id` field for capture requests or to look up a transaction.

Sessions API {#uc-setup-capture-context}
========================================

Use the Sessions API to generate a capture context. The capture context contains all of the merchant-specific parameters that tell the front-end JavaScript library what to do within your payment experience.

Capture Context {#uc-capture-context-features}
==============================================

The capture context is a signed JSON Web Token (JWT) containing this information:

* Merchant-specific parameters that dictate the customer payment experience for the current payment transaction.
* A one-time public key that secures the information flow during the current payment transaction.

There are some features of `Unified Checkout` that are available in the API, the `Business Center` or both. For information about how to configure `Unified Checkout` using the `Business Center`, see [Configure the Unified Checkout Merchant Experience](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc.md ""). For information about which fields are available using the API or the `Business Center`, and when one is overridden by the other, see [Capture Context Fields in the Business Center](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro-setup/uc-intro-setup-ebc/uc-ebc-api-info.md ""). For a full capture context with all possible fields, see [Example: Unified Checkout Complete Capture Context](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-appendix-complete-cc-ex.md "").
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
Include this field for values greater than or equal to `0.00`.

[targetOrigins](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/target-origins.md "")
:
The URL in this field value must contain `https`.
This example shows the minimum fields that must be included in the capture context:

```
{
  "targetOrigins": [
    "http://localhost:8080"
  ],
  "country": "US"
  "locale": "en_US"
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

For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").

> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Related Information {#uc-capture-context-features_section_ybj_nzz_sxb}
----------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#uc-capture-context-features_ul_zbj_nzz_sxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/uc/v1/sessions`  
**Test:** `POST ``https://apitest.cybersource.com``/uc/v1/sessions`  
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/uc/v1/sessions`  
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/uc/v1/sessions`

Allowed Card Networks {#uc_cc_allowed_card_networks}
====================================================

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
* Relay  
  To support dual-branded or co-badged cards, you must list your supported card type values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Relay and Cartes Bancaires, and Cartes Bancaires is listed first, the card type is set to Cartes Bancaires after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro/dual-co-brand-card-support.md "").

> IMPORTANT  
> Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). If you include only card types that do not have security codes in the allowedCardNetworks field, ` Unified Checkout ` does not display the security code field in the UI.  
> If you include card types that do not have security codes and cards types that do have security codes in the allowedCardNetworks field, ` Unified Checkout ` displays the security code field in the UI. The field is disabled in the UI when the cardholder enters a card number for a card type with no security code

Target Origins {#uc_cc_target_origin}
=====================================

The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain), and port number (if used).  
You must use the https:// protocol. Sub domains must also be included in the target origin.  
Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.  
For example, if you are launching `Unified Checkout` on example.com, the target origin could be any of the following:

* [https://example.com](https://example.com/ "")
* [https://subdomain.example.com](https://subdomain.example.com/ "")
* [https://example.com:8080](https://example.com:8080/ "")

When you use `Unified Checkout` in an iframe, you must include the domain for the URL that loads the iframe and the iframe URL in the targetOrigins field.

Allowed Payment Types {#uc_cc_allowed_pay_type}
===============================================

You can specify the type of `Unified Checkout` digital payment methods that you want to accept in the capture context.  
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
> ` Click to Pay ` accepts American Express, Mastercard, and Relay for saved cards. Relay and Mastercard tokenize payment credentials using network tokenization for all ` Click to Pay ` requests. ` Click to Pay ` uses ` Click to Pay ` Token Requester IDs (TRIDs) rather than your existing TRIDs to generate network tokens.  
> For more information on enabling and managing these digital payment methods, see these topics:

* [Enrolling in Apple Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay/uc-enable-digital-pay-applepay.md "")
* [Enabling Click to Pay in the Business Center](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-enable-digital-pay-ctp.md "")
* [Enrolling in Google Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay/uc-enable-digital-pay-google.md "")
* [Alternative Payment Methods](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-altpay-methods-intro.md "")

Client Version {#uc_cc_client_version}
======================================

This field is used to specify the `Unified Checkout`API version that your integration should use.  
`Cybersource` recommends that you do no include this field in your `uc/v1/sessions` API request. When you do not include this field, `Unified Checkout` automatically uses the latest available version. This ensures access to the most recent enhancements and updates without requiring integration changes.  
When you include this field, the value must be provided in `MAJOR.MINOR` format (for example, `1.1` or `1.2`). For information about semantic versioning, see [Versioning](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-getting-started-ss-setup/uc-versioning.md "").

> IMPORTANT
> This field cannot be configured through the merchant experience screens in the ` Business Center `.

Auto-check Enrollment {#uc_cc_ctp_enroll_precheck}
==================================================

You can have the `Click to Pay` box pre-checked when a user is manually entering their card details and `Click to Pay` is enabled. The customer can uncheck the box if necessary, which means the request is processed as a one-time manual PAN transaction. This is available when you set the billingType field to `PARTIAL` or `FULL` in the capture context. This ensures that the customer's billing country can be validated in the UI.  
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
"paymentConfigurations": {
    "CLICKTOPAY": {
      "autoCheckEnrollment": true
    }
  }
```

Button Type {#uc_cc_button_type}
================================

When `Unified Checkout` loads, the payment buttons displayed are based on what you include in the allowedPaymentTypes object in the capture context. `Unified Checkout` enables you to customize the text on the payment buttons. You can do this by setting the buttonType field object in the capture context to one of these values:

* `ADD_CARD`
* `CARD_PAYMENT`
* `CHECKOUT_AND_CONTINUE`
* `DEBIT_CREDIT`
* `DONATE`
* `PAY`
* `PAY_WITH_CARD`
* `SUBSCRIBE_WITH_CARD`  
  If you do not include the buttonType field in your request, the payment button text defaults to **Checkout with card**. For example:  
  ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-checkout-card-300x100.svg/jcr:content/renditions/original)

Customize Button Text {#uc-session-button-text}
===============================================

Use the buttonType field to customize the text on payment buttons:

| buttonType Value        | Button Display Text   |
|:------------------------|:----------------------|
| `ADD_CARD`              | Add card              |
| `CARD_PAYMENT`          | Card payment          |
| `CHECKOUT_AND_CONTINUE` | Checkout and continue |
| `DEBIT_CREDIT`          | Debit or credit       |
| `DONATE`                | Donate                |
| `PAY`                   | Pay                   |
| `PAY_WITH_CARD`         | Pay with card         |
| `SUBSCRIBE_WITH_CARD`   | Subscribe with card   |
[Button Text Options]

When you do not include this field in your request, the default button text is "Checkout with card."

Complete Mandate {#uc_cc_complete_mandate}
==========================================

The complete mandate feature provides service orchestration within `Unified Checkout` and simplifies your integration. Service orchestration enables `Unified Checkout` to orchestrate services on your behalf. The complete mandate feature provides instructions to the unifiedPayment.complete() method in the JavaScript. You must include both the unifiedPayment.complete() object in the Javascript and the completeMandate field object in your capture context to enable `Unified Checkout` to initiate services on your behalf from the browser.

> IMPORTANT
> If you are updating an existing ` Unified Checkout ` configuration to use the complete mandate, you must update your JavaScript to include the unifedPayment.complete() function.
> IMPORTANT
> When the billingType field is set to ` NONE ` you must include the required fields within the capture context request to ensure that the required fields are included for payment processing. For information about the fields that are required for payment services, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").

completeMandate.type {#uc_cc_complete_type}
===========================================

This field is required to run the complete mandate and is used to indicate how a payment should be processed.  
Possible values:

* `AUTH`: Authorize the payment and capture the funds at a later date.
* `CAPTURE`: Perform a sale. A sale is a combined authorization and capture in a single request.
* `PREFER_AUTH`: Perform an authorization if possible. If a payment method requires the funds to be captured immediately, then `Unified Checkout` captures the payment.

completeMandate.decisionManager {#uc_cc_complete_dm}
====================================================

This field determines whether `Decision Manager` is run. Set this field to `true` and include completeMandate.type in your request to run `Decision Manager` and device fingerprinting services. When `Decision Manager` runs, it uses the associated `Decision Manager` configuration based on the merchant ID that is included in the request.  
When this field is set to `false` or is not included in the request, `Decision Manager` and device fingerprinting services do not run.

completeMandate.consumerAuthentication {#uc_cc_complete_auth}
=============================================================

This field determines how a consumer is authenticated. You can authenticate a consumer using `3-D Secure`.  
You can set this field to one of these values:

* `NONE`: Consumer authentication does not run.
* `3DS`: `3-D Secure` authentication through `Payer Authentication` runs

{#uc_cc_complete_auth_ul_qhl_dth_njc} To initiate a passkey request for `Unified Checkout`, you must include these additional fields in your request:

* completeMandate.consumerAuthentication set to `PASSKEY`

* data.merchantInformation.merchantDescriptor.name

* data.acquirerInformation.country
  {#uc_cc_complete_auth_ul_wyp_s2r_vjc} When you use `Unified Checkout` with `Payer Authentication`, device data is collected through `Payer Authentication` setup and `Unified Checkout` completes all calls that are associated with `Payer Authentication`.  
  For information about challenge codes, see consumerAuthenticationInformation.challengeCode in the [REST API Field Reference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md ""). Unified Checkout supports `3-D Secure` data only when your payment processor supports it. For information see [Relay Data Only](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-data-only-intro/pa2-use-data-only-relay-intro.md "") in the *`Payer Authentication` Developer Guide*.
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

* Relay
  {#uc_cc_complete_auth_ul_sp5_52r_vjc}  
  Consumer authentication runs for these payment methods when they are supported in your `Unified Checkout` configuration:

* `PANENTRY`

* `CLICKTOPAY` when the transaction is not authenticated with `Click to Pay`.

* `GOOGLEPAY` when the transaction is not authenticated with Google Pay.
  {#uc_cc_complete_auth_ul_tp5_52r_vjc}  
  `Unified Checkout` does not attempt to authenticate for `Click to Pay` and Google Pay if the transaction has already been authenticated when it is received by `Unified Checkout`. For information about testing authentication, see [Test Authentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-authentication.md "").

completeMandate.tms {#uc_cc_complete_tms}
=========================================

completeMandate.tms.tokenCreate: This field determines if a `TMS` token is created for the customer's selected payment method. When this field is set to `true`, a token is created. When this field is set to `false` or not included in the request, a token is not created.

> IMPORTANT
> To make a new payment instrument or instrument identifier under an existing customer during the complete mandate, you must meet these requirements:
>
> * You must include the customer token ID in the paymentConfigurations field object.
>
> * ` TMS_TOKEN ` must be included in the allowedPaymentTypes field object.
>
> * tokenCreate must be set to ` true ` and ` paymentInstrument ` and ` instrumentIdentifier ` must be included as values in the tms.tokenTypes field array. For example:
>
>   ```
>         "tms": {
>         "tokenCreate": true,
>         "tokenTypes": [
>           "paymentInstrument",
>           "instrumentIdentifier",
>         ]
>       }
>
>   ```

When you meet these requirements, a new payment instrument or instrument identifier is created under the specified customer token.  
completeMandate.tms.tokenTypes: This is an optional field that you can use to indicate the token type for the token that is created. When this field is not included in the request, a token is created based on your `TMS` vault configuration. You can set this field to these values:

* `customer`
* `instrumentIdentifier`
* `paymentInstrument`
* `shippingAddress`  
  If you want `Unified Checkout` to capture the cardholder's consent to save the card before a request to create a token is completed, then you must set captureMandate.requestSaveCredentials to `true`. When this field is set to `true`, `Unified Checkout` presents a **Save card for future payments** checkbox within the UI and enables the cardholder to give consent. Do not include captureMandate.requestSaveCredentials in your request if you have already gained cardholder consent to create a `TMS` token or do not require consent.  
  This table indicates if a token is created given the requested payment method:

| Payment Method                  | Capture Context                                                                             | Result                                                                                                                                                                                                       |
|:--------------------------------|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAN Entry and `Click to Pay`    | completeMandate.tms.tokenCreate = `true`                                                    | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
| PAN Entry and `Click to Pay`    | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCredentials = `true` | Cardholder can check **Save Payment Information** in `Unified Checkout`. The request to create a token is made when the cardholder checks this field in the UI. When it is not checked, ni token is created. |
| Apple Pay, Google Pay, and Paze | completeMandate.tms.tokenCreate = `true`                                                    | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
| Apple Pay, Google Pay, and Paze | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCredentials = `true` | `Unified Checkout` cannot obtain consent to create a token and no token is created when the customer completes the payment.                                                                                  |
| Echeck                          | completeMandate.tms.tokenCreate = `true`                                                    | `TMS` token is created at the token level(s) specified in the request or based on the default for the token vault.                                                                                           |
| Echeck                          | completeMandate.tms.tokenCreate = `true` and captureMandate.requestSaveCredentials = `true` | `Unified Checkout` cannot obtain consent to create a token and no token is created when the customer completes the payment.                                                                                  |
[ ]

Capture Mandate {#uc_cc_capture_mandate}
========================================

The capture mandate enables you to define which fields are captured within `Unified Checkout`. You must include the fields and set the values in the capture context based on the information that you want `Unified Checkout` to collect. This enables the cardholder to review and edit their details where the UI includes these fields. When the UI is used to capture cardholder information, all captured information is available within the Payment Details API response. When you want the cardholder to review existing address data, you can include the known customer data in the capture context and this information is pre-filled in the `Unified Checkout` UI. For information about the Payment Details API, see [Payment Details API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md "").

captureMandate.comboCard {#uc_cc_combo_cards}
=============================================

A combo card is a single card in Brazil that functions as both a debit and a credit card. `Unified Checkout` enables the cardholder to choose whether to pay for a transaction using a debit or credit card. The cardholder can choose the card that they want to use when they enter their card details or when they choose a stored Relay card from their `Click to Pay` wallet during checkout. While in the card details section of the payment form, the cardholder is prompted for a debit or credit card. Credit is the default option.  
To enable combo cards during checkout, you must include the comboCard field in your capture context request and set the field value to `true`. When the comboCard field value is set to `true`, the option to use a debit or credit card appears for all Relay cards that are entered in Unified Checkout and for all cards that are already stored in `Click to Pay`. If you do not want to offer a combo card at checkout, do not include the comboCard field in your capture context request:

```
"captureMandate" : {
      "comboCard": true
}
```

IMPORTANT This feature is available only in Brazil.

captureMandate.CPF {#uc_cc_cpf}
===============================

The Cadastro de Pessoas Físicas (CPF) Brazilian tax ID feature is for customers in Brazil and provides your customers with a way to include their Consumer National Identifier when it is requested at checkout. Include this field in the capture context to display this field within the flow for manual card entry and `Click to Pay` transactions:

```
"captureMandate" : {
    "CPF": {
        "required": true
    }
}
```

IMPORTANT This feature is available only in Brazil.

captureMandate.requestSaveCredentials {#uc_cc_save_card}
========================================================

This feature enables you to display a consent option in the `Unified Checkout` UI for the cardholder to save their payment details for future use. If you use the complete mandate to create a token, see [Sessions API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context.md "").  
When you use this field without using the complete mandate, the transient token payload includes the consumerPreference.saveCard field with the value set to `true` when the cardholder has checked to save the payment information for future purchases:

```
"captureMandate" : {
      "requestSaveCredentials": true
}
```

captureMandate.showConfirmationStep {#uc_cc_rem_confirm_screen}
===============================================================

When showConfirmstionStep is set to `false`, you can remove the final summary confirmation screens from the checkout experience. When the UI displays cardholder data, the cardholder can review and, if necessary, edit their payment details before checkout is complete.

```
{
  "captureMandate": {
    "showConfirmationStep": false
  }
}
```

captureMandate.billingType {#uc_cc_capture_billing_type}
========================================================

`PARTIAL`: Only the billing postal code and billing country are collected in the UI. Set to this value when you use relaxed address verification services (AVS). This includes markets where postal code and billing country are enough for successful payment processing.  
`NONE`: No fields are shown in the UI to capture cardholder billing details. If you are using the Complete Mandate, you must provide billing details in the capture context. All information that is collected from these fields is tokenized in the transient token and sent for payment processing. For information about which fields are required for payment processing, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").  
`FULL`: These fields are shown in the UI to capture cardholder billing details. When you include the billing details in the capture context, these details are pre-filled in the `Unified Checkout` UI. All information that is collected from these fields are tokenized in the transient token and sent for payment processing where the Complete Mandate is used.

captureMandate.requestEmail {#uc_cc_capture_req_email}
======================================================

`false`: No email address is shown in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account and it appears in the UI when requestEmail is set to `false`.  
`true`: The email address is shown and captured in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account.

captureMandate.requestPhone {#uc_cc_capture_req_phone}
======================================================

`false`: No phone number is shown or captured in the UI.  
`true`: The phone number is shown and captured in the UI.

captureMandate.requestShipping {#uc_cc_capture_req_ship}
========================================================

`false`: No shipping information is captured in the UI. When shipping details are required for payment processing and are used for follow on services such as `Decision Manager`, you can include these fields in the capture context. These details are tokenized and passed through.  
`true`: Shipping fields are shown in the UI and are collected by `Unified Checkout`. When you include the shipping details in the capture context, the information appears prefilled in the UI.

captureMandate.shipToCountries {#uc_cc_capture_ship_to}
=======================================================

When the requestShipping field is set to `true`, only the countries that are included in this field can be selected by the cardholder for their shipping address.

Include Card Prefix {#uc_cc_include_prefix}
===========================================

You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

* Six digits
* Eight digits
* No prefix

To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.  
To receive a six-digit card number prefix in the response, follow this step:  
Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.  
This example shows how a six-digit card number prefix `411111` is returned in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111”,
                        "bin" : "411111"
```

To receive an eight-digit card number prefix in the response, follow this step:  
Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `true`. IMPORTANT

> This PCI DSS requirement applies only to card numbers longer than 15 digits and only for Discover, JCB, Mastercard, UnionPay, and Relay brands.
>
> * If the card type entered is not part of these brands, a six-digit card number prefix is returned instead.
> * If the card type entered is not part of these brands but is *co-branded* with these brands, an eight-digit card number prefix is returned.
>   This example shows how an eight-digit card prefix `41111102` is returned in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111”,
                        "prefix" : "41111102"
```

To not receive a card number prefix in the response, follow this step:  
Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `false`.  
This example shows how a card number is returned without a card number prefix in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111"
```

**Best practice:** If your application does not require card number prefix information for routing or identification, `Cybersource` recommends that you include the transientTokenResponseOptions.includeCardPrefix field in the capture context request and set its value to `false`. Doing so limits the exposure of payment data to only what is necessary for your processing needs.  
For more information about PCI DSS, see [Frequently Asked Questions](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers "") on the PCI Security Standards Council site.

Email Autolookup {#uc_cc_email_autolookup}
==========================================

When you include `Click to Pay` as an allowedPaymentType, an automatic email lookup occurs when an email address is included in the capture context request. If the user has a `Click to Pay` account but is not on a recognized device, a one-time password (OTP) screen appears and the user is prompted to enter their OTP. If the user does not have a `Click to Pay` account, the user must enter their card information manually. They will have the option to create a `Click to Pay` account.  
To enable email autolookup, you must include `CLICKTOPAY` as a value in the allowedPaymentTypes field and include an email address in the capture context.

> IMPORTANT
> When the captureMandate.requestEmail and captureMandate.requestPhone fields are set to ` false `, the contact details section is not displayed in the UI.

Mobile as Identity for `Click to Pay` {#uc_cc_mobile_identity}
==============================================================

`Click to Pay` supports mobile numbers as way to identify a user. This enables cardholders to use their mobile number instead of their email address in certain markets for Relay and Mastercard transactions.  
When the requestEmail field is set to `false` and the requestPhone field is set to `true`, the cardholder is identified using the provided mobile number. When the requestEmail field is set to `true` and the requestPhone field is set to `false`, the cardholder is identified using the provided email address. When the requestEmail field is set to `true` and the requestPhone field is also set to `true`, the cardholder is identified using the provided email address first and then the mobile number if there is no match.

Example: `Unified Checkout` Complete Capture Context {#uc-appendix-uc-auth-ex}
==============================================================================

Capture Context Request

```
{
  "country": "US",
  "locale": "en_GB",
  "targetOrigins": [
    "https://merchant.com",
    "https://reseller.com:8443"
  ],
  "clientVersion": "1.0",
  "allowedCardNetworks": [
    "CARD",
    "MASTERCARD",
    "AMEX",
    "JCB",
    "DISCOVER",
    "DINERSCLUB",
    "CARTESBANCAIRES",
    "EFTPOS",
    "JCREW",
    "MEEZA",
    "CUP",
    "CARNET",
    "MADA",
    "ELO",
    "MAESTRO",
    "PAYPAK",
    "JAYWAN",
    "KCP",
    "UATP"
  ],
  "allowedPaymentTypes": [
    "PANENTRY",
    "GOOGLEPAY",
    "CLICKTOPAY",
    "APPLEPAY",
    "PAZE",
    "CHECK",
    "AFTERPAY",
    "IDEAL",
    "MULTIBANCO",
    "PRZELEWY24",
    "MYBANK",
    "KONBINI",
    "DRAGONPAY",
    "BANCONTACT",
    "TINKPAYBYBANK"
  ],
  "appearance": {
    "theme": "LIGHT",
    "variables": {
      "primaryColor": "#007bff",
      "secondaryColor": "#6c757d",
      "fontFamily": "Arial, sans-serif",
      "fontSize": "14px",
      "borderRadius": "4px"
    }
  },
  "buttonType": "CHECKOUT",
  "captureMandate": {
    "showConfirmationStep": true,
    "billingType": "FULL",
    "requestEmail": true,
    "requestPhone": true,
    "requestShipping": true,
    "shipToCountries": [
      "US",
      "GB",
      "CA"
    ],
    "showAcceptedNetworkIcons": true,
    "comboCard": true,
    "requestSaveCredentials": true,
    "CPF": {
      "required": true
    }
  },
  "completeMandate": {
    "type": "CAPTURE",
    "decisionManager": true,
    "consumerAuthentication": "3DS",
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
  "paymentConfigurations": {
    "PANENTRY": {
      "customer": "existing_customer_token_123"
    },
    "GOOGLEPAY": {
      "allowedAuthMethods": [
        "PAN_ONLY",
        "CRYPTOGRAM_3DS"
      ]
    },
    "CLICKTOPAY": {
      "autoCheckEnrollment": true
    }
  },
  "transientTokenResponseOptions": {
    "includeCardPrefix": true
  },
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
        "taxAmount": "10.00",
        "taxDetails": [
          {
            "taxId": "1234",
            "type": "N"
          },
          {
            "taxId": "5678",
            "type": "S"
          }
        ]
      },
      "billTo": {
        "address1": "123 Main Street",
        "address2": "Apt 4B",
        "address3": "Building C",
        "address4": "Floor 3",
        "administrativeArea": "CA",
        "buildingNumber": "123",
        "country": "US",
        "district": "Downtown",
        "locality": "San Francisco",
        "postalCode": "94105",
        "email": "jane.doe@relay.com",
        "firstName": "John",
        "middleName": "Michael",
        "lastName": "Doe",
        "phoneNumber": "+1-123456789",
        "phoneType": "night",
        "nameSuffix": "Mr",
        "title": "Software Engineer",
        "company": {
          "name": "Relay Inc",
          "address1": "900 Metro Center Blvd",
          "address2": "Suite 200",
          "country": "US",
          "administrativeArea": "CA",
          "postalCode": "94404",
          "locality": "Foster City"
        }
      },
      "shipTo": {
        "address1": "456 Oak Avenue",
        "address2": "Suite 100",
        "address3": "Building A",
        "address4": "Level 2",
        "administrativeArea": "NY",
        "buildingNumber": "456",
        "country": "US",
        "district": "Midtown",
        "locality": "New York",
        "postalCode": "10001",
        "firstName": "Jane",
        "lastName": "Smith"
      },
      "lineItems": [
        {
          "productCode": "WIDGET-001",
          "productName": "Premium Widget",
          "productSku": "WID-PRE-001",
          "quantity": 2,
          "unitPrice": "45.50",
          "unitOfMeasure": "EA",
          "totalAmount": "91.00",
          "taxAmount": "7.28",
          "taxRate": "0.08",
          "taxAppliedAfterDiscount": "y",
          "taxStatusIndicator": "N",
          "taxTypeCode": "1234",
          "amountIncludesTax": true,
          "typeOfSupply": "12",
          "commodityCode": "COMM-001",
          "discountAmount": "5.00",
          "discountApplied": true,
          "discountRate": "0.05",
          "invoiceNumber": "INV-2024-001",
          "taxDetails": [
            {
              "type": "STATE",
              "amount": "3.64",
              "rate": "0.04",
              "code": "1234",
              "taxId": "TAX-001",
              "applied": true,
              "exemptionCode": "1"
            },
            {
              "type": "LOCAL",
              "amount": "3.64",
              "rate": "0.04",
              "code": "5678",
              "taxId": "TAX-002",
              "applied": true,
              "exemptionCode": "2"
            }
          ],
          "fulfillmentType": "SHIP",
          "weight": "500",
          "weightIdentifier": "N",
          "weightUnit": "mg",
          "referenceDataCode": "REF-001",
          "referenceDataNumber": "REF-NUM-001",
          "unitTaxAmount": "3.64",
          "productDescription": "High-quality premium widget with extended warranty",
          "giftCardCurrency": "USD",
          "shippingDestinationTypes": "residential",
          "gift": false,
          "passenger": {
            "type": "ADT",
            "status": "confirmed",
            "phone": "+1-123456789",
            "firstName": "Robert",
            "lastName": "Johnson",
            "id": "PASS-001",
            "email": "jane.doe@relay.com",
            "nationality": "US"
          }
        },
        {
          "productCode": "GADGET-002",
          "productName": "Digital Gadget",
          "productSku": "GAD-DIG-002",
          "quantity": 1,
          "unitPrice": "29.99",
          "unitOfMeasure": "EA",
          "totalAmount": "29.99",
          "taxAmount": "2.40",
          "taxRate": "0.08",
          "taxAppliedAfterDiscount": "n",
          "taxStatusIndicator": "Y",
          "taxTypeCode": "5678",
          "amountIncludesTax": false,
          "typeOfSupply": "11",
          "commodityCode": "COMM-002",
          "discountAmount": "3.00",
          "discountApplied": true,
          "discountRate": "0.10",
          "invoiceNumber": "INV-2024-002",
          "taxDetails": [
            {
              "type": "FEDERAL",
              "amount": "2.40",
              "rate": "0.08",
              "code": "9012",
              "taxId": "TAX-003",
              "applied": true,
              "exemptionCode": "0"
            }
          ],
          "fulfillmentType": "DIGITAL",
          "weight": "0",
          "weightIdentifier": "Y",
          "weightUnit": "g",
          "referenceDataCode": "REF-002",
          "referenceDataNumber": "REF-NUM-002",
          "unitTaxAmount": "2.40",
          "productDescription": "Advanced digital gadget with cloud sync",
          "giftCardCurrency": "EUR",
          "shippingDestinationTypes": "commercial",
          "gift": true,
          "passenger": {
            "type": "CHD",
            "status": "pending",
            "phone": "+1-123456789",
            "firstName": "Emily",
            "lastName": "Williams",
            "id": "PASS-002",
            "email": "jane.doe@relay.com",
            "nationality": "GB"
          }
        }
      ],
      "invoiceDetails": {
        "invoiceNumber": "INV-MAIN-2024-001",
        "productDescription": "Multiple items including widgets and gadgets"
      }
    },
    "buyerInformation": {
      "personalIdentification": [
        {
          "type": "CPF",
          "id": "01234567890"
        }
      ],
      "merchantCustomerId": "CUST-12345",
      "companyTaxId": "123456789",
      "dateOfBirth": "19901215",
      "language": "en"
    },
    "clientReferenceInformation": {
      "code": "TAGX001",
      "partner": {
        "developerId": "DEV-1234",
        "solutionId": "SOL-4567"
      }
    },
    "consumerAuthenticationInformation": {
      "challengeCode": "01",
      "messageCategory": "01",
      "acsWindowSize": "01"
    },
    "merchantInformation": {
      "merchantDescriptor": {
        "name": "Jane Sales",
        "alternateName": "BIG SALES INC",
        "locality": "New York",
        "phone": "+1-123456789",
        "country": "US",
        "postalCode": "170056",
        "administrativeArea": "NY",
        "address1": "123 47TH STREET"
      }
    },
    "processingInformation": {
      "reconciliationId": "01234567",
      "authorizationOptions": {
        "aftIndicator": true,
        "authIndicator": "Y",
        "ignoreCvResult": true,
        "ignoreAvsResult": true,
        "initiator": {
          "credentialStoredOnFile": true,
          "merchantInitiatedTransaction": {
            "reason": "1"
          }
        }
      },
      "businessApplicationId": "AA",
      "commerceIndicator": "recurring",
      "processingInstruction": "ORDER_SAVED_EXPLICITLY"
    },
    "recipientInformation": {
      "firstName": "John",
      "middleName": "A",
      "lastName": "Buyer",
      "country": "GB",
      "accountId": "acc0123567",
      "administrativeArea": "GB",
      "accountType": "01",
      "dateOfBirth": "19901215",
      "postalCode": "170056"
    },
    "merchantDefinedInformation": [
      {
        "key": "promo_code",
        "value": "DISCOUNT20"
      },
      {
        "key": "customer_tier",
        "value": "gold"
      }
    ],
    "deviceInformation": {
      "ipAddress": "192.168.1.100"
    },
    "paymentInformation": {
      "card": {
        "typeSelectionIndicator": "0"
      }
    }
  }
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
   * **Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/public-keys/{3g}`
   * **Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/public-keys/{3g}`  
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

Session Validation {#uc-session-validate}
=========================================

The session JWT is digitally signed using RS256. You must confirm that it was issued by `Cybersource` and has not been tampered with. Follow these steps to validate the signature:

1. Parse the session JWT header to extract the key ID (`kid`):

   ```
   {
     "kid": "3g",
     "alg": "RS256"
   }
   ```
2. Retrieve the public key by sending a request to the `/flex/v2/public-keys/{kid}` endpoint:

   * **Test** : GET `apitest.cybersource.com``flex/v2/public-keys/{kid}`
   * **Production** : GET `api.cybersource.com``flex/v2/public-keys/{kid}`
3. Use the returned RSA public key in JSON Web Key format to verify the JWT signature.  
   IMPORTANT Depending on the cryptographic library that tou use, you may need to convert the key to Privacy-Enhanced Mail (PEM) format.

Transient Tokens {#uc-tokens-intro}
===================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the checkout.mount() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.  
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.

Transient Token Format {#uc-tokens-format}
==========================================

The transient token is issued as a JSON Web Token (JWT) ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").  
The payload portion of the token is a Base64URL-encoded JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-jwts.md "").

Example: Transient Token Format {#uc-trans-tkn-ex}
==================================================

Transient Token Payload

> IMPORTANT The empty field values in the transient token indicate which fields were captured by the application without exposing you to personally identifiable information directly.

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
If you are using `Unified Checkout` with unifiedPayment.complete() and consumerAuthentication is set to `3DS` or `PASSKEY` in the complete mandate request, then `Payer Authentication` is called automatically if it is available for the selected payment method and card network. If you use a transient token to request follow-on services directly, the value of this field indicates if the transaction has been authenticated.

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
"allowedCardNetworks": ["CARD", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Relay.  
During the transaction, the card type is populated with the first network in the list, and the **detectedCardTypes** field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Relay and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option selected by the customer during checkout.

Authorizations with a Transient Token {#uc-auth-tokens}
=======================================================

This section provides the information required in order to perform a successful authorization with a `Unified Checkout` transient token. You can use this method to construct more complex payment scenarios that are not supported by the `unifiedPayments.complete()` payment method.

> IMPORTANT
> When you process payments through ` Unified Checkout ` using unifiedPayments.complete() , ` Unified Checkout ` invokes service orchestration directly. When you send an authorization request using a transient token, you must request the follow-on services that you want to use. For information about the required fields for the payment services that you request, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").  
> The transient token is a short-term token that expires after 15 minutes. Doing so eliminates the need to send sensitive payment data along with the request. For more information on transient tokens, see [Transient Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro.md "").  
> To send the transient token with a request, use the tokenInformation.transientTokenJwt field.  
> This example shows a transient token in the context of an authorization request:

```
"tokenInformation": { 
    "transientTokenJwt": "eyJraWQiOiIwOG4zUnVsRTJGQXJDRktycVRkZFlkWGZSWFhMNXFoNSIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzA3IiwiZXhwIjoxNTk3MDg0ODk3LCJ0eXBlIjoiZ2RhLTAuMS4xIiwiaWF0IjoxNTk3MDgzOTk3LCJqdGkiOiIxQzI2VlpSkVJUU1PTzVIMDUwNEtINDdJMEFNMklaRkM0M1Y1TDU0MUhCTE45Q09JM0w3NUYzMTk0RTE5NkExIn0.SNm1VZaZr3DkTqUg9CdV0F5arRe-uQU9oUWPKfWIpbIzIPZutRokv5DSDcM7asZIKNJyNIBx5DLsl_yQPrKgzhwQxZ8qbhto7cu3t-v8DHG2yO951plPQVQnj7x-vEDcXkLUL1F8sqY23R5HW-xSDAQ3AFLawCckn7Q2eudRGeuMhLWH742Gflf9Hz3KyKnmeNKA3o9yW2na16nmeVZaYGqbUSPVITdl5cMA0o9lEob8E3OQH0HHdmIsu5uMA4x7DeBjfTKD1rQxFP3JBNVcv30AIMLkNcw0pHbtHDVzKBWxUVxvnm3zFEdiBuSAco2uWhC9zFqHrrp64ZvzxZqoGA" 
}
```

To retrieve non-sensitive data from a `Unified Checkout` transient token, use the `payment-details` endpoint. This data includes cardholder name and billing and shipping details. For more information, see [Payment Details API](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md "").

> IMPORTANT Fields supplied directly in an API request supersede those that are also present in the transient token. For example, in the request below, the total amount might have been overridden because of a tax calculation.

Endpoint {#uc-auth-tokens_endpt-auth}
-------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#uc-auth-tokens_restauth}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#uc-auth-tokens_restauth-test}  
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/pts/v2/payments`  
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/pts/v2/payments`

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

Test Your Configuration {#uc-reference-test-cards}
==================================================

Use these test payment credentials to test your `Unified Checkout` configuration:

* [Unified Checkout Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-uc.md "")

* [Relay and Mastercard Click to Pay Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-relay-ctp.md "")

* [Test Cards for Authentication by Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-auth-ctp.md "")

* [Echeck Test Values](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-auth-echeck.md "")  
  You can handle errors and test your configuration using these topics:

* [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "")

* [Reason Codes](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-v1-reason-codes.md "")

`Unified Checkout` Test Cards {#uc-reference-test-cards-uc}
===========================================================

Use these test card numbers to test your `Unified Checkout` configuration.  
Combine the BIN with the card number when sending to `Unified Checkout`.
To test `Payer Authentication`, you must use `Payer Authentication` test cards. See [Test Cases for 3-D Secure 2.x](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "") in the *`Payer Authentication` Developer Guide*.

|    Card Brand    |  BIN   | Card Number  | Expiration Date | CVV  |
|------------------|--------|--------------|-----------------|------|
| Relay             | 411111 | 1111111111   | 12/2026         | 123  |
| Mastercard       | 555555 | 5555554444   | 02/2026         | 265  |
| American Express | 378282 | 246310005    | 03/2026         | 7890 |
| Cartes Bancaires | 436000 | 0001000005   | 04/2040         | 123  |
| Carnet           | 506221 | 0000000009   | 04/2026         | 123  |
| China UnionPay   | 627988 | 6248094966   | 04/2040         | 123  |
| Diners Club      | 305693 | 09025904     | 04/2040         | 123  |
| Discover         | 644564 | 4564456445   | 04/2040         | 123  |
| JCB              | 353011 | 13333 0000   | 04/2040         | 123  |
| Jaywan           | 679009 | 0000002009   | 04/2040         | 123  |
| Jaywan           | 669000 | 0000000000   | 04/2040         | 123  |
| KCP              | 949022 | 0011669217   | 04/2040         |      |
| Paypak           | 220543 | 0000003002   | 04/2040         | 123  |
| Maestro          | 675964 | 9826438453   | 04/2040         | 123  |
| mada             | 446404 | 0000000007   | 04/2040         | 123  |
| ELO              | 451416 | 0000000003   | 04/2040         | 123  |
| JCrew            | 515997 | 1500000005   | 04/2040         | 123  |
| EFTPOS           | 401795 | 000000000009 | 04/2040         | 123  |
| Meeza            | 507808 | 3000000002   | 04/2040         | 123  |
| UATP             | 148512 | 345678905    | 04/2040         |      |
[Test Card Numbers]

Test Cards for `Click to Pay` Authentication by `Unified Checkout`
------------------------------------------------------------------

se these test cards to test when you use a `Click to Pay` card with authentication performed outside `Click to Pay` and the consumerAuthentication field is set to `3DS` or `PASSKEY` in the capture context.  
Replace the X in the card number with 4.  
To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 46229431231X2X56 | 12/2026         | 432 |
| Relay       | 46229431231X232X | 12/2026         | 581 |
| Mastercard | 512X35X1XXX64578 | Any future date | Any |
| Mastercard | 512X35X1XXX64552 | Any future date | Any |
[Test Card Numbers for Authentication Outside `Click to Pay` Flow]

Relay and Mastercard `Click to Pay` Test Cards {#uc-reference-test-cards-relay-ctp}
=================================================================================

Relay Test Cards {#uc-reference-test-cards-relay-ctp_uc-reference-test-cards-relay-ctp}
------------------------------------------------------------------------------------

These Relay test cards can be added to your `Click to Pay` wallet.  
Replace the X in the card number with 4.  
You can manage your Relay `Click to Pay` test cards and account here:

* **Production:** [login](https://src.relay.com/login "")
* **Test:** [login](https://sandbox.src.relay.com/login "")

> IMPORTANT
> Relay ` Click to Pay ` may request additional verification details during testing, such as CVV confirmation.  
> To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| x6229x3123123755 | 12/2029         | 728 |
| x6229x3123123763 | 12/2029         | 605 |
| x6229x3123123771 | 12/2029         | 694 |
| x6229x3123123789 | 12/2029         | 881 |
| x6229x3123123797 | 12/2029         | 678 |
| x6229x3123123805 | 12/2029         | 084 |
| x6229x3123123813 | 12/2029         | 127 |
| x6229x3123123821 | 12/2029         | 218 |
| x6229x3123123839 | 12/2029         | 114 |
| x6229x31231238x7 | 12/2029         | 867 |
| x6229x312312385x | 12/2029         | 301 |
[Relay Test Card Numbers]

Mastercard Test Cards {#uc-reference-test-cards-relay-ctp_uc-reference-test-cards-relay-ctp-mc}
---------------------------------------------------------------------------------------------

Mastercard test cards can be added to your `Click to Pay` wallet. You must retrieve Mastercard test cards from their `Click to Pay` test page: [#test-cards](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "")  
For Mastercard `Click to Pay`, the user will see a loading Mastercard window where they will be prompted to enter additional information into this window  
Mastercard has different test cards for retrieving tokenized and non-tokenized data. `Cybersource` recommends that you use these test cards as follows:

* Test cards to retrieve PAN data: Use these cards when the customer is completing checkout as a one-time guest and does not have a `Click to Pay` account or want to create one.

* Test cards to retrieve token data: Use these cards for tokenized `Click to Pay` transactions.

* Tokenize eligible test cards for token authentication: Use these test cards to attempt `Click to Pay` authentication when `Click to Pay` authentication is enabled.  
  You can manage your Mastercard `Click to Pay` test cards and account here:

* **Live:** [enroll](https://src.mastercard.com/profile/enroll "")

* **SBX:** [enroll](https://sandbox.src.mastercard.com/profile/enroll "")  
  Mastercard authentication test cards are available on the *Mastercard Checkout Solutions* page in the [Mastercard Developer Center](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "").

Test Cards for Authentication by `Click to Pay` {#uc-reference-test-cards-auth-ctp}
===================================================================================

Use these cards when authentication is performed by `Click to Pay` within the `Click to Pay` flow.  
Replace the X in the card number with 4.  
To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 439584X300520271 | 12/2030         | 504 |
| Relay       | 439584X300600271 | 12/2030         | 184 |
| Relay       | 439584X300780271 | 12/2030         | 164 |
| Relay       | 439584X300860271 | 12/2030         | 668 |
| Relay       | 439584X300940271 | 12/2030         | 856 |
[`3-D Secure` Friction]

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | X3958X0000011019 | 12/2030         | 956 |
| Relay       | X3958X0000011027 | 12/2030         | 550 |
| Relay       | X3958X0000011035 | 12/2030         | 623 |
| Relay       | X3958X00000110X3 | 12/2030         | 997 |
| Relay       | X3958X0000011050 | 12/2030         | 790 |
| Relay       | X3958X0000011068 | 12/2030         | 888 |
| Relay       | X3958X0000011076 | 12/2030         | 924 |
| Relay       | X3958X000001108X | 12/2030         | 375 |
| Relay       | X3958X0000011092 | 12/2030         | 865 |
[`3-D Secure` Frictionless]

Mastercard authentication test cards are available on the *Mastercard Checkout Solutions* page in the [Mastercard Developer Center](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "").  
For information about testing authentication, see [Test Authentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-appendix-authentication.md ""). For information about enabling Relay customer authentication, see [Set Up Customer Authentication for Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-enable-digital-pay-ctp/uc-authentication-steps.md "").

Echeck Test Values {#uc-reference-test-cards-auth-echeck}
=========================================================

These eCheck test values can be used to process a test eCheck transactions:

* **Routing number:** Set to 071923284
* **Account number:** Set to any supported value. For example, 1234567890.

Test Authentication {#uc_appendix_authentication}
=================================================

Use this table to determine how to test your authentication method.

| Payment Method |                  Authentication                   |        Minimum Follow-On Actions         |                                                                                                       Prerequisites                                                                                                        |                                                                                                                                                                                                                                             Test Cards                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                               |
|----------------|---------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAN Entry      | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `3DS` or `PASSKEY`.                                                           | See [Testing `Payer Authentication`](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md "") in the *`Payer Authentication` Developer Guide.*                                                                                                                                                                                                                                                                                  | When the complete mandate is not used, `Unified Checkout` does not initiate authentication and you must perform authentication within your own environment.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `Click to Pay` | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `3DS` or `PASSKEY`. Authentication for `Click to Pay` must not be configured. | See [Unified Checkout Test Cards](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-uc.md "").                                                                                                                                                                                                                                                                                                | When authentication is not enabled for `Click to Pay` or `Click to Pay` is not able to perform authentication for `Click to Pay`, `Unified Checkout` performs authentication using `Payer Authentication` when the complete mandate is used with the consumerAuthentication field set to `3DS` or `PASSKEY`.                                                                                                                                                                                                                                                        |
| `Click to Pay` | Relay `Click to Pay`                               | Authorization and `Payer Authentication` | You must configure the authentication for `Click to Pay`. `Click to Pay` performs authentication only if it is a tokenized Relay or Mastercard card.                                                                        | See [Test Cards for Authentication by Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-reference-test-cards-auth-ctp.md ""). Mastercard authentication test cards are available on the *Mastercard Checkout Solutions* page in the [Mastercard Developer Center](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards ""). | When authentication is enabled for `Click to Pay`, authentication is attempted for all `Click to Pay` transactions for Relay and Mastercard cards that are stored in `Click to Pay`. For information about setting up authentication for Relay `Click to Pay`, see [Set Up Customer Authentication for Click to Pay](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-enable-digital-pay-ctp/uc-authentication-steps.md ""). |
| Google Pay     | Google Pay                                        | Authorization                            | A Google device must be used with biometric authentication for Google authentication.                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | A user authenticates themselves on a Google device with a tokenized Google Pay credential. The returned payload from Google is authenticated.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Google Pay     | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | You must use a device, such as a web browser, that does not authenticate the cardholder as part of the authorization process.                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Google returns an un-authenticated payload to `Unified Checkout`. `Unified Checkout` processes authentication via `Payer Authentication` when the complete mandate function is used with consumerAuthentication.                                                                                                                                                                                                                                                                                                                                                    |
[Authentication Testing by Product]

Handle Errors {#uc_appendix_handle_errors}
==========================================

The `Unified Checkout` SDK uses a structured error object for all error scenarios. Errors are returned as exceptions from asynchronous methods and are also returned as events for centralized handling.

UnifiedCheckoutError {#uc_handle_errors_uc_checkout}
====================================================

All SDK errors are instances of `UnifiedCheckoutError` with these properties:

| Property          | Type       | Description                                                                          |
|:------------------|:-----------|:-------------------------------------------------------------------------------------|
| `correlationId`   | `string?`  | The correlation ID from an underlying API call, when applicable.                     |
| `details`         | `unknown?` | Additional error-specific information. This is often an array of objects.            |
| `informationLink` | `string?`  | The URL linked to the online documentation for this error.                           |
| `message`         | `string`   | This property is a human-readable description of the error.                          |
| `name`            | `string`   | The value is always `"UnifiedCheckoutError"`.                                        |
| `reason`          | `string`   | This property is a machine-readable error code, such as `"CAPTURE_CONTEXT_INVALID"`. |
[`UnifiedCheckoutError` Properties]

Detect Errors {#uc_handle_errors_detect}
========================================

Errors may be serialized through `postMessage`. `Cybersource` recommends that you use the `name` property instead of `instanceof`:

```
try {
  const result = await checkout.mount('#buttons');
} catch (error) {
  if (error.name === 'UnifiedCheckoutError') {
    // Access error.reason, error.message, error.details
  }
}
```

You can also write a helper function that can be reused:

```
function isUnifiedCheckoutError(obj) {
  return (
    obj !== null &&
    typeof obj === 'object' &&
    obj.name === 'UnifiedCheckoutError' &&
    typeof obj.reason === 'string' &&
    typeof obj.message === 'string'
  );
}
```

Error Handling Patterns {#uc_handle_errors_pattern}
===================================================

Try/Catch
---------

```
try {
  const client = await VAS.UnifiedCheckout(sessionJWT);
  const checkout = await client.createCheckout();
  const result = await checkout.mount('#buttons');
} catch (error) {
  console.error(error.reason, error.message);
}
```

Promise .catch()
----------------

```
VAS.UnifiedCheckout(sessionJWT)
  .then(client =&gt; client.createCheckout())
  .then(checkout =&gt; checkout.mount('#buttons'))
  .catch(error =&gt; console.error(error.reason, error.message));
```

Centralized Error Logging via Events
------------------------------------

Errors from all integrations are applicable up to the client level. Use `client.on('error')` for centralized logging:

```
const client = await VAS.UnifiedCheckout(sessionJWT);

client.on('error', (err) =&gt; {
  errorReporter.send({
    source: err.source,   // "checkout", "trigger", "button", or "client"
    code: err.code,
    message: err.message
  });
});
```

`Cybersource` recommends that you do this as it catches errors from all checkouts, triggers, and buttons created from this client instance.

Error Codes {#uc_handle_errors_codes}
=====================================

Initialization Errors
---------------------

These errors are returned during `VAS.UnifiedCheckout(sessionJWT)`:

| Reason                    | Description                                                                                                                    |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| `CAPTURE_CONTEXT_EXPIRED` | The supplied JWT has expired. Generate a new session.                                                                          |
| `CAPTURE_CONTEXT_INVALID` | The session JWT is not valid. For example, it has a bad signature or is malformed.                                             |
| `UNUSED_TARGET_ORIGINS`   | One or more `targetOrigins` in the session do not match the current page origin. The `details` array lists the unused origins. |
[Initialization Reason Values]

Mount Errors
------------

These errors are returned during `checkout.mount()` or `trigger.mount()`:

| Reason                      | Description                                                                                                                                  |
|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| `CHECKOUT_ALREADY_MOUNTED`  | The checkout or trigger is already mounted. Call `unmount()` first, or create a new instance.                                                |
| `MOUNT_CONTAINER_SELECTOR`  | The CSS selector does not match any Document Object Model (DOM) element. Check that the container exists before calling `mount()`.           |
| `MOUNT_ERROR`               | A problem occurred loading the payment iframe.                                                                                               |
| `MOUNT_INVALID_CONTAINER`   | The supplied container parameter is not a valid CSS selector string or `HTMLElement`.                                                        |
| `MOUNT_PAYMENT_TIMEOUT`     | A payment method timed out during initialization.                                                                                            |
| `MOUNT_PAYMENT_UNAVAILABLE` | No payment types could be presented to the customer. This may be due to browser or device support, or errors during checkout initialization. |
| `MOUNT_SIDEBAR_OPTIONS`     | The supplied container parameter is invalid for sidebar mode.                                                                                |
| `MOUNT_TOKEN_TIMEOUT`       | Token creation timed out during mount. This may indicate a network issue.                                                                    |
| `MOUNT_TOKEN_XHR_ERROR`     | A network error occurred during token creation. Check the customer's connectivity.                                                           |
[Mount Reason Values]

Complete Errors
---------------

These errors are returned during `checkout.complete()` or `trigger.complete()`:

| Reason                             | Description                                                                                        |
|:-----------------------------------|:---------------------------------------------------------------------------------------------------|
| `COMPLETE_AUTHENTICATION_CANCELED` | The customer cancelled the `3-D Secure` authentication step-up.                                    |
| `COMPLETE_AUTHENTICATION_FAILED`   | The `3-D Secure` authentication step-up failed.                                                    |
| `COMPLETE_ERROR`                   | A general error occurred during transaction completion.                                            |
| `COMPLETE_IN_PROGRESS`             | complete() has already been called and has not yet finished. Wait for the current call to resolve. |
| `COMPLETE_NOT_ALLOWED`             | Complete is not allowed for this transaction, such as when `autoProcessing` is set to `true`.      |
| `COMPLETE_TRANSACTION_CANCELLED`   | The customer cancelled the transaction.                                                            |
| `COMPLETE_TRANSACTION_FAILED`      | The transaction failed during processing.                                                          |
| `COMPLETE_VALIDATION_ERROR`        | The parameters supplied to complete() have a validation error. Check the `details` for specifics   |
[Complete Reason Values]

Checkout Errors
---------------

| Reason                        | Description                                              |
|:------------------------------|:---------------------------------------------------------|
| `CHECKOUT_ERROR`              | A general checkout error occurred.                       |
| `CHECKOUT_PAYMENT_PARAMETERS` | One or more payment parameters have a validation error.  |
| `CHECKOUT_VALIDATION_PARAMS`  | One or more checkout parameters have a validation error. |
[Checkout Reason Values]

Trigger Errors
--------------

| Reason                               | Description                                                                                                      |
|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` | The specified payment type cannot be used with a trigger. Only `PANENTRY` and `CLICKTOPAY` values are supported. |
[Trigger Reason Values]

**Payment-Specific Errors**
---------------------------

| Reason                                 | Description                                           |
|:---------------------------------------|:------------------------------------------------------|
| `CLICK_TO_PAY_SDK_LOAD_ERROR`          | The `Click to Pay`SDK failed to load.                 |
| `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` | Card encryption for `Click to Pay` enrollment failed. |
| `GOOGLEPAY_CHECKOUT_ERROR`             | A Google Pay checkout error occurred.                 |
| `LAUNCH_SRC_CHECKOUT_ERROR`            | Launching the `Click to Pay` checkout failed.         |
| `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED`   | The payment type is not supported for triggers.       |
[Payment-Specific Reason Values]

General Errors
--------------

| Reason Code     | Description                    |
|:----------------|:-------------------------------|
| `UNKNOWN_ERROR` | An unknown error has occurred. |

Reason Codes {#uc_appendix_v1_reason_codes}
===========================================

This section describes the server-side HTTP status codes and reason values that are returned when you send requests to `Unified Checkout`. For information about client-side SDK error codes, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

HTTP Status Codes
-----------------

| Code  |                             Description                             |
|-------|---------------------------------------------------------------------|
| `200` | Request processed successfully                                      |
| `201` | Session created                                                     |
| `400` | Bad request. The response body contains a reason value with details |
| `404` | Resource not found                                                  |
| `500` | Unexpected server error                                             |

Reason Values (HTTP `400`)
--------------------------

When the API returns a status code value of `400`, the response body includes the reason field. This section lists all possible values for the reason field:

|          Reason           |                                    Description                                     |
|---------------------------|------------------------------------------------------------------------------------|
| `CAPTURE_CONTEXT_EXPIRED` | The session JWT is expired. Generate a new session.                                |
| `CAPTURE_CONTEXT_INVALID` | The session JWT is not valid. For example, it has a bad signature or is malformed. |
| `INVALID_APIKEY`          | The API key is not valid.                                                          |
[Initialization Reason Values]

|                Reason                 |                       Description                        |
|---------------------------------------|----------------------------------------------------------|
| `CHECKOUT_ERROR`                      | A general checkout error occurred.                       |
| `UNIFIED_PAYMENTS_ALREADY_SHOWN`      | The checkout is already displayed.                       |
| `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS` | One or more payment parameters have a validation error.  |
| `UNIFIED_PAYMENTS_VALIDATION_FIELDS`  | One or more fields have a validation error.              |
| `UNIFIED_PAYMENTS_VALIDATION_PARAMS`  | One or more checkout parameters have a validation error. |
[Checkout Reason Values]

|             Reason             |                      Description                       |
|--------------------------------|--------------------------------------------------------|
| `SHOW_LOAD_CONTAINER_SELECTOR` | The CSS selector does not match any element.           |
| `SHOW_LOAD_ERROR`              | A problem occurred loading the payment iframe.         |
| `SHOW_LOAD_INVALID_CONTAINER`  | The container parameter is not valid.                  |
| `SHOW_LOAD_SIDEBAR_OPTIONS`    | The container parameter is not valid for sidebar mode. |
| `SHOW_PAYMENT_TIMEOUT`         | A payment method timed out during initialization.      |
| `SHOW_PAYMENT_UNAVAILABLE`     | No payment types could be presented to the customer.   |
| `SHOW_TOKEN_TIMEOUT`           | Token creation timed out during mount.                 |
| `SHOW_TOKEN_XHR_ERROR`         | A network error occurred during token creation.        |
[Mount Reason Values]

|               Reason               |                            Description                            |
|------------------------------------|-------------------------------------------------------------------|
| `COMPLETE_AUTHENTICATION_CANCELED` | The customer cancelled `3-D Secure` authentication.               |
| `COMPLETE_AUTHENTICATION_FAILED`   | `3-D Secure` authentication failed.                               |
| `COMPLETE_ERROR`                   | A general error occurred during completion.                       |
| `COMPLETE_IN_PROGRESS`             | A complete call is already in progress.                           |
| `COMPLETE_NOT_ALLOWED`             | Complete is not allowed, such as when auto-processing is enabled. |
| `COMPLETE_TRANSACTION_CANCELLED`   | The customer cancelled the transaction.                           |
| `COMPLETE_TRANSACTION_FAILED`      | The transaction failed during processing.                         |
| `COMPLETE_VALIDATION_ERROR`        | Parameters supplied to complete have a validation error.          |
[Complete Reason Values]

|          Reason          |                   Description                   |
|--------------------------|-------------------------------------------------|
| `CREATE_TOKEN_TIMEOUT`   | Token creation request timed out.               |
| `CREATE_TOKEN_XHR_ERROR` | A network error occurred during token creation. |
| `SDK_XHR_ERROR`          | A general SDK network error occurred.           |
| `TOKENIZATION_ERROR`     | Tokenization of payment data failed.            |
[Tokenization Reason Values]

|                 Reason                 |                      Description                      |
|----------------------------------------|-------------------------------------------------------|
| `CLICK_TO_PAY_SDK_LOAD_ERROR`          | The `Click to Pay`SDK failed to load.                 |
| `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` | Card encryption for `Click to Pay` enrollment failed. |
| `GOOGLEPAY_CHECKOUT_ERROR`             | A Google Pay checkout error occurred.                 |
| `LAUNCH_SRC_CHECKOUT_ERROR`            | Launching the `Click to Pay` checkout failed.         |
| `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED`   | The payment type is not supported for triggers.       |
[Payment-Specific Reason Values]

Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the Payment Details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d8e1140}
----------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d8e1147}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d8e1159}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
The `{jti}` is the ID of the JWT within the transient token that is returned by `Unified Checkout`. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

REST Example: Retrieving Transient Token Payment Details {#uc-token-get-pymnt-details-ex-rest}
==============================================================================================

Request

```keyword
GET https://apitest.cybersource.com/flex/v2/payment-details/{jti}
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

JavaScript API Reference {#uc-appendix-js-reference-v1_api_reference}
=====================================================================

This reference provides details about the JavaScript API for creating the `Unified Checkout` v1 payment form.

VAS.UnifiedCheckout(sessionJWT) {#uc_appendix_js_initialize}
============================================================

This is a factory function that initializes the SDK. It returns a frozen, immutable client interface.

|     Name     |   Type   | Required? |                            Description                            |
|--------------|----------|-----------|-------------------------------------------------------------------|
| `sessionJWT` | `string` | Yes       | Signed JSON Web Token (JWT) from the server-side session endpoint |
[VAS.UnifiedCheckout(sessionJWT) Parameters]

**Returns**
:
`Promise&lt;UnifiedCheckoutInterface&gt;`

**Errors**
:
Returns `UnifiedCheckoutError` with reason `CAPTURE_CONTEXT_INVALID` if the JWT signature is invalid, or `UNUSED_TARGET_ORIGINS` if the current page origin is not in the JWT's `targetOrigins` list.

**Example**
:

    ```
    const client = await VAS.UnifiedCheckout(sessionJWT);
    ```

UnifiedCheckoutInterface {#uc_appendix_js_interface}
====================================================

The client object returned by `VAS.UnifiedCheckout()`. All methods throw an `Error` if called after `destroy()`.

client.createCheckout(options?)
-------------------------------

|   Name    |          Type           | Required? |          Description           |
|-----------|-------------------------|-----------|--------------------------------|
| `options` | `CreateCheckoutOptions` | No        | Configuration for the checkout |
[client.createCheckout(options?) Parameters]

|     Property     |   Type    |            Default             |                                                                                   Description                                                                                   |
|------------------|-----------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `autoProcessing` | `boolean` | Inferred from capture context. | * `true`: `mount()` returns completed payment result. Defaults to `true` when completeMandate is included in the capture context. * `false`: `mount()` returns transient token. |
[`CreateCheckoutOptions` Properties]

**Returns**
:
`Promise&lt;Checkout&gt;`

**Example**
:

    ```
    const checkout = await client.createCheckout({ autoProcessing: false });
    ```

client.createTrigger(paymentType, options?)
-------------------------------------------

|     Name      |          Type          | Required? |                   Description                   |
|---------------|------------------------|-----------|-------------------------------------------------|
| `paymentType` | `AllowedPaymentType`   | Yes       | Only `PANENTRY` and `CLICKTOPAY` are supported. |
| `options`     | `CreateTriggerOptions` | No        | The configuration for the trigger.              |
[client.createTrigger(paymentType, options?) Parameters]

|     Property     |   Type    |        Default        |            Description            |
|------------------|-----------|-----------------------|-----------------------------------|
| `autoProcessing` | `boolean` | Inferred from session | Same as checkout `autoProcessing` |
[`CreateTriggerOptions` Properties]

**Returns**
:
`Trigger`

**Errors**
:
Returns `UnifiedCheckoutError` with reason `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` when the payment type cannot be used with a trigger.

**Example**
:

    ```
    const trigger = client.createTrigger('PANENTRY');
    ```

client.createButton(paymentType, options?) (Experimental)
---------------------------------------------------------

Creates an individual payment method button.

|     Name      |         Type          | Required? |                              Description                              |
|---------------|-----------------------|-----------|-----------------------------------------------------------------------|
| `paymentType` | `AllowedPaymentType`  | Yes       | Payment type for the button. For example, `GOOGLEPAY` and `APPLEPAY`. |
| `options`     | `CreateButtonOptions` | No        | The configuration for the button.                                     |
[client.createButton(paymentType, options?) Parameters]

|     Property     |   Type    |        Default        |            Description            |
|------------------|-----------|-----------------------|-----------------------------------|
| `autoProcessing` | `boolean` | Inferred from session | Same as checkout `autoProcessing` |
[`CreateButtonOptions` Properties]

**Returns**
:
`PaymentButton`

**Example**
:

    ```
    const button = client.createButton('GOOGLEPAY');
    ```

client.on(event, callback)
--------------------------

Subscribes to a client-level event and returns an unsubscribe function.

|    Name    |    Type    | Required? |                              Description                               |
|------------|------------|-----------|------------------------------------------------------------------------|
| `event`    | `string`   | Yes       | Event name. Possible values: * `*` * `created` * `destroyed` * `error` |
| `callback` | `function` | Yes       | Handler function that receives event-specific payload.                 |
[client.on(event, callback) Parameters]

|     Property     |   Type    |        Default        |            Description            |
|------------------|-----------|-----------------------|-----------------------------------|
| `autoProcessing` | `boolean` | Inferred from session | Same as checkout `autoProcessing` |
[`CreateButtonOptions` Properties]

**Returns**
:
`Unsubscribe`: A function that removes the handler when called.

**Errors**
:
Returns `Error` when `event` is not a valid event name with reason `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` when the payment type cannot be used with a trigger.

**Example**
:

    ```
    const unsubscribe = client.on('error', (err) =&gt; {
      console.error(err.source, err.code, err.message);
    });

    // Later
    unsubscribe();
    ```

client.off(event, callback?)
----------------------------

Removes an event handler. This method is permissive --- calling it with an unknown event or callback does not throw.

|    Name    |    Type    | Required? |                                          Description                                           |
|------------|------------|-----------|------------------------------------------------------------------------------------------------|
| `event`    | `string`   | Yes       | Event name to unsubscribe from                                                                 |
| `callback` | `function` | No        | Specific handler to remove. When this is not included, all handlers for the event are removed. |
[client.off(event, callback?) Parameters]

client.destroy()
----------------

Permanently destroys the client. Returns a `destroyed` event, clears all event listeners, and marks the instance as destroyed.  
You can call `destroy()` multiple times.

client.isDestroyed()
--------------------

Returns a value of `true` if client.destroy() is called.

Checkout {#uc_appendix_js_checkout}
===================================

This field is returned by `client.createCheckout()` and manages the full checkout UI lifecycle.

checkout.mount(target)
----------------------

Subscribes to a client-level event and returns an unsubscribe function.

|   Name   |               Type               | Required? |                                                               Description                                                               |
|----------|----------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `target` | `string` or `CheckoutContainers` | No        | CSS selector string for sidebar mode, or an object with `paymentSelection` and `paymentScreen` for embedded mode. Omit for full sidebar |
[checkout.mount(target) Parameters]

|      Property      |   Type   | Default |                                           Description                                           |
|--------------------|----------|---------|-------------------------------------------------------------------------------------------------|
| `paymentSelection` | `string` | Yes     | CSS selector for the button list container                                                      |
| `paymentScreen`    | `string` | No      | CSS selector for the payment form container. If omitted, payment screens appear in sidebar mode |
[`CheckoutContainers` Properties]

**Returns**
:
`Promise&lt;string&gt;`: This is a transient token JWT when `autoProcessing: false` or completed payment result JWT when `autoProcessing: true`.

**Errors**
:
Returns `UnifiedCheckoutError`. For information about how to handle mount error codes, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

**Example**
:

    ```
    // Sidebar
    const result = await checkout.mount('#buttons');

    // Embedded
    const result = await checkout.mount({
      paymentSelection: '#buttons',
      paymentScreen: '#form'
    });
    ```

checkout.unmount()
------------------

Removes the payment UI from the page. The checkout is not destroyed --- you can call `mount()` again.

checkout.complete(transientToken)
---------------------------------

Manually completes the payment flow. This is only available when `autoProcessing` is set to `false`.

|       Name       |   Type   | Required? |                      Description                       |
|------------------|----------|-----------|--------------------------------------------------------|
| `transientToken` | `string` | Yes       | The transient token JWT that is returned by `mount()`. |
[checkout.complete(transientToken) Parameters]

|      Property      |   Type   | Default |                                           Description                                           |
|--------------------|----------|---------|-------------------------------------------------------------------------------------------------|
| `paymentSelection` | `string` | Yes     | CSS selector for the button list container                                                      |
| `paymentScreen`    | `string` | No      | CSS selector for the payment form container. If omitted, payment screens appear in sidebar mode |
[`CheckoutContainers` Properties]

**Returns**
:
`Promise&lt;string&gt;`: This is the completed payment result JWT.

**Errors**
:
Returns `UnifiedCheckoutError`. For information about how to handle mount error codes, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

**Example**
:

    ```
    const token = await checkout.mount('#buttons');
    const result = await checkout.complete(token);
    ```

checkout.isMounted()
--------------------

Returns `true` when the checkout UI is mounted.

checkout.isDestroyed()
----------------------

Returns `true` when `destroy()` is called.

checkout.on(event, handler)
---------------------------

Subscribes to a checkout-level event and returns an unsubscribe function.  
Valid events:

* `mounted`
* `ready`
* `unready`
* `unmounted`
* `destroyed`
* `paymentMethodSelected`
* `paymentMethodCancelled`
* `paymentMethodUpdate"`
* `error`
* `*`

checkout.off(event, handler?)
-----------------------------

Removes a checkout event handler.

checkout.destroy()
------------------

Permanently destroys the checkout. This field removes the payment UI, cleans up iframes, and emits a `destroyed` event.

Trigger {#uc_appendix_js_trigger}
=================================

The trigger is returned by `client.createTrigger()` and programmatically launches a specific payment method.

trigger.mount(target?)
----------------------

Launches the payment method UI.

|   Name   |   Type   | Required? |                      Description                       |
|----------|----------|-----------|--------------------------------------------------------|
| `target` | `string` | No        | CSS selector for embedded mode. Omit for sidebar mode. |
[trigger.mount(target?) Parameters]

**Returns**
:
`Promise&lt;string&gt;`: A transient token or completed payment result.

**Example**
:

    ```
    const result = await trigger.mount('#payment-screen');
    ```

trigger.unmount()
-----------------

Hides the payment method UI. The trigger is not destroyed.

trigger.complete(transientToken)
--------------------------------

Manually completes the payment. Same interface as `checkout.complete()`.

trigger.isMounted()
-------------------

Returns a boolean value.

trigger.isDestroyed()
---------------------

Returns a boolean value.

trigger.on(event, handler)
--------------------------

Subscribes to trigger events. Same event names and payloads as checkout events.

trigger.off(event, handler?)
----------------------------

Removes a trigger event handler.

trigger.destroy()
-----------------

Permanently destroys the trigger.

PaymentButton {#uc_appendix_js_pay_button}
==========================================

This is returned by `client.createButton()`. It renders an individual payment method button.

button.mount(container)
-----------------------

Mounts the button into a container.

|    Name     |           Type            | Required? |                                     Description                                     |
|-------------|---------------------------|-----------|-------------------------------------------------------------------------------------|
| `container` | `string` or `HTMLElement` | Yes       | CSS selector string or Document Object Model (DOM) element for the button container |
[button.mount(container) Parameters]

**Returns**
:
`Promise&lt;string&gt;`: A transient token or completed payment result.

button.unmount()
----------------

Removes the button from the page. The button is not destroyed.

button.isMounted()
------------------

Returns a boolean value if the button is mounted (`true`) or not mounted (`false`).

button.isDestroyed()
--------------------

Returns a boolean value if the button is destroyed (`true`) or not destroyed (`false`).

button.on(event, callback)
--------------------------

Subscribes to button events. Returns `void`. Use `button.off()` to remove handlers.

> IMPORTANT The button event system is under development. Event names and payloads may change in future releases.

button.off(event, callback?)
----------------------------

Removes a button event handler.

button.destroy()
----------------

Permanently destroys the button. Idempotent.

Events {#uc-appendix-js-events}
===============================

`Unified Checkout` provides a type-safe event system for monitoring the payment lifecycle. Events are emitted at the client and integration levels.

Subscribe to Events {#uc-appendix-js-events_uc-appendix-js-events-subscribe}
----------------------------------------------------------------------------

Use `on()` to subscribe to events. this returns an unsubscribe function:

```
const unsubscribe = checkout.on('ready', (data) =&gt; {
  console.log('Ready:', data.availablePaymentMethods);
});

// Later, remove the handler
unsubscribe();
```

You can use `off()` to remove a specific handler:

```
function onReady(data) { /* ... */ }

checkout.on('ready', onReady);
checkout.off('ready', onReady);
```

Update to `Unified Checkout` Version 1 {#uc_v1_migration_intro}
===============================================================

The version 1 (v1) SDK simplifies your integration with fewer lines of code, a streamlined API, and enhancements such as auto-processing and a full event system. The core flow is the same in v1, and migrating to v1 involves only straightforward method renames.

Summary of Changes
------------------

|                       Aspect                       |                            v0                            |                                                                                                                                                                                                    v1                                                                                                                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initialization                                     | `new Accept(session).unifiedPayments()`                  | `VAS.UnifiedCheckout(session)`                                                                                                                                                                                                                                                                                                                                                                           |
| Display the payment UI                             | `up.show(options)`                                       | `checkout.mount(target)`                                                                                                                                                                                                                                                                                                                                                                                 |
| Completing transactions                            | `up.complete(token)`                                     | `checkout.complete(token)` or automatic using `autoProcessing`                                                                                                                                                                                                                                                                                                                                           |
| Events                                             | None                                                     | Full event system on client and checkout                                                                                                                                                                                                                                                                                                                                                                 |
| Cleanup                                            | `up.dispose()`                                           | `checkout.destroy()` + `client.destroy()`                                                                                                                                                                                                                                                                                                                                                                |
| Hide UI                                            | `up.hide()`                                              | `checkout.unmount()`                                                                                                                                                                                                                                                                                                                                                                                     |
| Target Origin (Sessions API)                       | Multiple non-usable URLs can be included in the request. | If any origins are absent or mismatched, for example, they are not presented in `Unified Checkout`, the system prevents `Unified Checkout` from loading and displays a client-side error message.                                                                                                                                                                                                        |
| consumerAuthentication within the Complete Mandate | **Data type:** Boolean                                   | **Data type:** Enum Possible values: * `3DS` * `NONE` {#uc_v1_migration_intro_ul_bsk_khr_vjc} For information about consumerAuthentication, see [completeMandate.consumerAuthentication](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-setup-capture-context/uc-capture-context-features/uc-cc-complete-mandate/uc-cc-complete-auth.md ""). |
[Summary of Version 1 Changes]

{#uc_v1_migration_intro_rest-uc-cc-prod-code}

|                        Feature                        |                                                 Pre V1 Support                                                  |                                                   V1 Support                                                    |                        Description                        |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Status                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center`                                                                                               |                                                           |
| Capture context endpoint                              | `/up/v1/capture-contexts`                                                                                       | `/uc/v1/sessions`                                                                                               |                                                           |
| Capture context management                            | API only                                                                                                        | API only or API and `Business Center`                                                                           | `Business Center` configuration is at the merchant level. |
| `Unified Checkout` Look and Feel in `Business Center` | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center` configuration is at the merchant level. |
| `Unified Checkout` Look and Feel Using the API        | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Configure the look and feel in a Sessions API request.    |
| Payment methods                                       | API only                                                                                                        | API or API and `Business Center`                                                                                | `Business Center` configuration is at the merchant level. |
| Real-time preview in `Business Center`                | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center` configuration is at the merchant level. |
| Three-decimal currency support                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                           |
| SDK                                                   | Legacy Unified Payments SDK supported (link)                                                                    | New UC SDK (link)                                                                                               |                                                           |
| Payment Details API                                   | `/up/v1/payment-details/`*{id}*                                                                                 | JTI used in place of transient token                                                                            | JTI is located in the transient token                     |
| Future enhancements                                   | Manual opt-in is required.                                                                                      | Automatic when the clientVersion is not included in the Sessions API request.                                   | Legacy versions receive critical updates only.            |
[Summary of v0 and v1 Changes]

Initialization
--------------

Initialization with `Unified Checkout` v1 is done in a single asynchronous factory call. There is no intermediate `Accept` object: v0 Initialization

```
const accept = new Accept(sessionJWT);
const up = accept.unifiedPayments();
```

v1 Initialization

```
const client = await VAS.UnifiedCheckout(sessionJWT);
```

`Unified Checkout` v1 validates the JWT signature and target origins during initialization.

Display the Payment UI
----------------------

`Unified Checkout` v1 passes your UI payment selectors directly to `mount()`.  
When `autoProcessing` is enabled, `mount()` returns the completed payment result rather than a transient token. v0 Display Payment UI with `show()`

```
// Sidebar
const token = await up.show({
  containers: {
    paymentSelection: '#buttons'
  }
});

// Embedded
const token = await up.show({
  containers: {
    paymentSelection: '#buttons',
    paymentScreen: '#form'
  }
});
```

v1 Display Payment UI with `mount()`

```
// Sidebar
const result = await checkout.mount('#buttons');

// Embedded
const result = await checkout.mount({
  paymentSelection: '#buttons',
  paymentScreen: '#form'
});
```

Completing Transactions
-----------------------

When `autoProcessing` is enabled in `Unified Checkout` v1, `mount()` returns the completed payment result and you do not need to send a separate complete() request. When `autoProcessing` is disabled in `Unified Checkout` v1, you must complete transactions manually. v0 Complete Transactions Manually

```
const token = await up.show({
  containers: {
    paymentSelection: '#buttons'
  }
});
const result = await up.complete(token);
```

v1 Complete Transactions Manually or Automatically

```
// Automatic (default when completeMandate is in session)
const checkout = await client.createCheckout({ autoProcessing: true });
const result = await checkout.mount('#buttons');
// result is the completed transaction — no need to call complete()

// Manual - similar to v0
const checkout = await client.createCheckout({ autoProcessing: false });
const token = await checkout.mount('#buttons');
const result = await checkout.complete(token);
```

Events
------

`Unified Checkout` v0 does not include an event system, as the integration resolution or rejection from `show()` and complete(). v1 includes a full event system as the client and integration levels. v1 Full Event System

```
// Client-level — centralized error tracking
client.on('error', (err) =&gt; {
  console.error(`[${err.source}] ${err.code}: ${err.message}`);
});

// Checkout-level — granular lifecycle events
checkout.on('ready', (data) =&gt; {
  console.log('Available methods:', data.availablePaymentMethods);
});

checkout.on('paymentMethodSelected', (data) =&gt; {
  console.log('Selected:', data.type);
});

checkout.on('error', (err) =&gt; {
  console.error('Checkout error:', err.code);
});
```

Cleanup
-------

`Unified Checkout` v1 distinguishes between `unmount()`, which is reversible, and `destroy()`, which is permanent. Before a cleanup, `client.destroy()` sends a `destroyed` event. v0 Cleanup

```
up.hide();     // Hide UI
up.dispose();  // Clean up resources
```

v1 Cleanup

```
checkout.unmount();   // Remove UI from page (can remount later)
checkout.destroy();   // Permanent cleanup

client.destroy();     // Destroy client and clear all event listeners
```

Handle Errors
-------------

The `UnifiedCheckoutError` class and its reason codes are the same in v0 and v1: v0 Error Handling

```
try {
  const token = await up.show({
    containers: {
      paymentSelection: '#buttons'
    }
  });
} catch (err) {
  console.error(err.reason, err.message);
}
```

v1 Error Handling

```
// Same error class, same properties
try {
  const result = await checkout.mount('#buttons');
} catch (err) {
  console.error(err.reason, err.message);
}
```

Migrate Triggers
----------------

If your `Unified Checkout` v0 integration uses triggers, the migration is similar to checkout. In v1, triggers are created from the` client.createTrigger`, not from `UnifiedPayments` as in v0. In v1, `show()` is renamed to `mount()`. v0 Triggers

```
const trigger = up.createTrigger('CLICKTOPAY', {
  containers: { paymentScreen: '#screen' }
});
const token = await trigger.show();
```

v1 Triggers

```
const trigger = client.createTrigger('CLICKTOPAY');
const result = await trigger.mount('#screen');
```

Update Reason Codes {#uc_v1_migrate_reason_codes}
=================================================

Some reason codes were renamed in v1. This table shows the v0 reason code name and the corresponding name in the v1 client-side SDK:

|            v0 Reason Code             |        v1 Reason Code         |
|---------------------------------------|-------------------------------|
| `SHOW_LOAD_CONTAINER_SELECTOR`        | `MOUNT_CONTAINER_SELECTOR`    |
| `SHOW_LOAD_ERROR`                     | `MOUNT_ERROR`                 |
| `SHOW_LOAD_INVALID_CONTAINER`         | `MOUNT_INVALID_CONTAINER`     |
| `SHOW_LOAD_SIDEBAR_OPTIONS`           | `MOUNT_SIDEBAR_OPTIONS`       |
| `SHOW_PAYMENT_TIMEOUT`                | `MOUNT_PAYMENT_TIMEOUT`       |
| `SHOW_PAYMENT_UNAVAILABLE`            | `MOUNT_PAYMENT_UNAVAILABLE`   |
| `SHOW_TOKEN_TIMEOUT`                  | `MOUNT_TOKEN_TIMEOUT`         |
| `SHOW_TOKEN_XHR_ERROR`                | `MOUNT_TOKEN_XHR_ERROR`       |
| `UNIFIED_PAYMENTS_ALREADY_SHOWN`      | `CHECKOUT_ALREADY_MOUNTED`    |
| `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS` | `CHECKOUT_PAYMENT_PARAMETERS` |
| `UNIFIED_PAYMENTS_VALIDATION_PARAMS`  | `CHECKOUT_VALIDATION_PARAMS`  |

> IMPORTANT
> The server-side API continues to return these v0 reason codes. The v1 reason codes listed here are used only in the client-side SDK. For all v1 client-side error codes, see [Handle Errors](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-reference-test-cards/uc-handle-errors.md "").

Version 1 Update Checklist {#uc_v1_migration_checklist}
=======================================================

You must complete these tasks before you can complete your migration from `Unified Checkout` v0 to v1:

* Replace `new Accept(session).unifiedPayments()` with `await VAS.UnifiedCheckout(session)`.
* Replace `up.show(options)` with `checkout = await client.createCheckout(); checkout.mount(target)`.
* Update container options: `{ containers: { paymentSelection, paymentScreen } }` becomes direct arguments to `mount()`.
* Replace `up.complete(token)` with `checkout.complete(token)` or use `autoProcessing: true` to complete transactions automatically
* Replace `up.hide()` with `checkout.unmount()`.
* Replace `up.dispose()` with `checkout.destroy()` and `client.destroy()`.
* Add event listeners for observability. For example, `client.on('error')` and `checkout.on('ready')`.

Appendix {#uc-appendix}
=======================

This section contains supplementary information for `Unified Checkout`.

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

Supported Countries for Digital Payments {#uc-appendix-supp-countries}
======================================================================

Supported Countries for Digital Payments A-D {#uc-appendix-supp-countries-a-d}
==============================================================================

|             Country              |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                     eCheck                                                      |                                                   Google Pay                                                    |
|:--------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
|           Afghanistan            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Albania              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Algeria              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Andorra              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Angola              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|       Antigua and Barbuda        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Argentina             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Armenia              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Australia             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Austria              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Azerbaijan            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bahamas              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bahrain              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Bangladesh            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Barbados             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Belarus              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Belgium              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Brazil              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Belize              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Benin               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Bhutan              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Bolivia              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|      Bosnia and Herzegovina      |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Botswana             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|        Brunei Darussalam         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Bulgaria             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Burkina Faso           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Burundi              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Cambodia             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Cameroon             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Canada              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Cape Verde            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|     Central African Republic     |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|               Chad               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Chile               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              China               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Colombia             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Comoros              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|            Costa Rica            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|          Côte d'Ivoire           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Croatia              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|              Cyprus              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|          Czech Republic          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Democratic Republic of the Congo |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Denmark              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Djibouti             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Dominica             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|        Dominican Republic        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (A through D)]

Supported Countries for Digital Payments E-K {#uc-appendix-supp-countries-e-k}
==============================================================================

|      Country      |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                   Google Pay                                                    |
|-------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
| Ecuador           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Egypt             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| El Salvador       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Equatorial Guinea |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Eritrea           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Estonia           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Eswatini          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ethiopia          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Faroe Islands     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Fiji              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Finland           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| France            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gabon             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gambia            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Georgia           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Germany           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ghana             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Gibraltar         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Greece            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Greenland         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Guernsey          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Grenada           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guatemala         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guinea            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guinea-Bissau     |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Guyana            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Haiti             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Honduras          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Hong Kong         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Hungary           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Iceland           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Indonesia         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Iraq              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Ireland           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Isle of Man       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Israel            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Italy             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Jamaica           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Japan             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Jersey            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Jordan            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kazakhstan        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kenya             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kiribati          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kuwait            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Kyrgyzstan        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (E through K)]

Supported Countries for Digital Payments L-R {#uc-appendix-supp-countries-l-r}
==============================================================================

|             Country             |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                   Google Pay                                                    |
|---------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
| Laos                            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latvia                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lebanon                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lesotho                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Liberia                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Libya                           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Liechtenstein                   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Lithuania                       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Luxembourg                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Macau                           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Madagascar                      |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malawi                          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malaysia                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Maldives                        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mali                            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Malta                           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Marshall Islands                |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mauritania                      |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mauritius                       |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mexico                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Micronesia, Federated States of |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Moldova                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Monaco                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mongolia                        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Montenegro                      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Morocco                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Mozambique                      |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Myanmar                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Namibia                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nauru                           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nepal                           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Netherlands                     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| New Zealand                     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nicaragua                       |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Niger                           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Nigeria                         |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| North Macedonia                 |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Norway                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Oman                            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Pakistan                        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Palau                           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Palestinian Territories         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Panama                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Papua New Guinea                |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Paraguay                        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Peru                            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Philippines                     |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Poland                          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Portugal                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Qatar                           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Republic of the Congo           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Romania                         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Rwanda                          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Supported Countries (L through R)]

Supported Countries for Digital Payments S-Z {#uc-appendix-supp-countries-s-z}
==============================================================================

|             Country              |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                     eCheck                                                      |                                                   Google Pay                                                    |                                                      Paze                                                       |
|:--------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------:|
|      Saint Kitts and Nevis       |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Saint Lucia            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
| Saint Vincent and the Grenadines |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Samoa               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            San Marino            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|      Sao Tome and Principe       |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Saudi Arabia           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Senegal              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Serbia              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Seychelles            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Sierra Leone           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Singapore             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Slovakia             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Slovenia             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|         Solomon Islands          |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Somalia              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           South Africa           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|    Korea, Republic of (South)    | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           South Sudan            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Spain               | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Sri Lanka             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Sudan               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Suriname             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Sweden              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Switzerland            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       Switzerland -Italian       |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Taiwan              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Tajikistan            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Tanzania             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Thailand             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Timor-Leste            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|               Togo               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Tonga               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       Trinidad and Tobago        |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Tunisia              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Turkey              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|           Turkmenistan           |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Tuvalu              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Uganda              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Ukraine              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|       United Arab Emirates       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|          United Kingdom          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|          United States           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
|             Uruguay              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Uzbekistan            |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Vanuatu              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|     Vatican City (Holy See)      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|            Venezuela             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Vietnam              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Yemen               |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|              Zambia              |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
|             Zimbabwe             |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |   ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)   |
[Supported Countries (S through Z)]

Supported Locales {#uc-appendix-languages}
==========================================

The locale field within the capture context request consists of an ISO 639 language code, an underscore (_), and an ISO 3166 region code. Set the locale field in your session request to display the checkout UI in the customer's language.

> IMPORTANT
> When the chosen language is Arabic, ` Unified Checkout ` supports right-to-left languages in the UI for this locale.  
> `Unified Checkout` supports these locales:

| Locale  |   ISO Language   |      ISO Region      |
|---------|------------------|----------------------|
| `ar_AE` | Arabic           | United Arab Emirates |
| `ar_JO` | Arabic           | Jordan               |
| `ar_QA` | Arabic           | Qatar                |
| `bg_BG` | Bulgarian        | Bulgaria             |
| `ca_ES` | Catalan          | Spain                |
| `zh_CN` | Chinese          | China                |
| `zh_HK` | Chinese          | Hong Kong            |
| `zh_MO` | Chinese          | Macao                |
| `zh_SG` | Chinese          | Singapore            |
| `zh_TW` | Chinese          | Taiwan               |
| `hr_HR` | Croatian         | Croatia              |
| `cs_CZ` | Czech            | Czechia              |
| `da_DK` | Danish           | Denmark              |
| `nl_NL` | Dutch            | Netherlands          |
| `en_AE` | English          | United Arab Emirates |
| `en_AU` | English          | Australia            |
| `en_CA` | English          | Canada               |
| `en_GB` | English          | United Kingdom       |
| `en_IE` | English          | Ireland              |
| `en_NZ` | English          | New Zealand          |
| `en_PK` | English          | Pakistan             |
| `en_QA` | English          | Qatar                |
| `en_US` | English          | United States        |
| `en_LK` | English          | Sri Lanka            |
| `fi_FI` | Finnish          | Finland              |
| `fr_CA` | French           | Canada               |
| `fr_FR` | French           | France               |
| `de_AT` | German           | Austria              |
| `de_DE` | German           | Germany              |
| `el_GR` | Greek            | Greece               |
| `he_IL` | Hebrew           | Israel               |
| `hu_HU` | Hungarian        | Hungary              |
| `id_ID` | Indonesian       | Indonesia            |
| `it_IT` | Italian          | Italy                |
| `ja_JP` | Japanese         | Japan                |
| `km_KH` | Khmer            | Cambodia             |
| `ko_KR` | Korean           | South Korea          |
| `lo_LA` | Lao              | Laos                 |
| `ms_MY` | Malay            | Malaysia             |
| `nb_NO` | Norwegian Bokmål | Norway               |
| `pl_PL` | Polish           | Poland               |
| `pt_BR` | Portuguese       | Brazil               |
| `ro_RO` | Romanian         | Romania              |
| `ru_RU` | Russian          | Russia               |
| `si_LK` | Sinhala          | Sri Lanka            |
| `sk_SK` | Slovak           | Slovakia             |
| `sl_SI` | Slovenian        | Slovenia             |
| `es_AR` | Spanish          | Argentina            |
| `es_CL` | Spanish          | Chile                |
| `es_CO` | Spanish          | Colombia             |
| `es_ES` | Spanish          | Spain                |
| `es_MX` | Spanish          | Mexico               |
| `es_PE` | Spanish          | Peru                 |
| `es_US` | Spanish          | United States        |
| `sv_SE` | Swedish          | Sweden               |
| `tl_PH` | Tagalog          | Philippines          |
| `ta_LK` | Tamil            | Sri Lanka            |
| `th_TH` | Thai             | Thailand             |
| `tr_TR` | Turkish          | Türkiye              |
| `uk_UA` | Ukrainian        | Ukraine              |
| `ur_PK` | Urdu             | Pakistan             |
| `vi_VN` | Vietnamese       | Vietnam              |
[Supported Locales]

Security Recommendations {#uc_security_recs}
============================================

`Unified Checkout` is compliant with Payment Card Industry (PCI) Self-Assessment Questionnaire A (SAQ-A). `Cybersource` recommends that you consider these security policies so you can maintain a secure integration.

Content Security Policy
-----------------------

Implement a Content Security Policy (CSP) to mitigate cross-site scripting (XSS) attacks. Add these directives for `Unified Checkout`:

| Directive     | Test                              | Production                    |
|:--------------|:----------------------------------|:------------------------------|
| `connect-src` | `https://apitest.cybersource.com` | `https://api.cybersource.com` |
| `frame-src`   | `https://apitest.cybersource.com` | `https://api.cybersource.com` |
| `child-src`   | `https://apitest.cybersource.com` | `https://api.cybersource.com` |
| `script-src`  | `https://apitest.cybersource.com` | `https://api.cybersource.com` |
[CSP Directives]

These directives enable the SDK to load secure iframes and communicate with `Cybersource` services.

> IMPORTANT When you use additional payment methods such as Google Pay or PayPal, you must also add their respective domains to your CSP directives.

Iframe Isolation
----------------

`Unified Checkout` renders all payment UI inside cross-origin iframes hosted by `Cybersource`. This architecture provides several security benefits:

* **Data isolation**: Your page cannot access payment data within the iframe due to the browser's same-origin policy.
* **Reduced attack surface**: Attackers cannot extract card data from the isolated iframe if your merchant page is compromised.
* **Origin verification** : The SDK validates that the hosting page origin matches the `targetOrigins` that is declared in the session before displaying any UI.  
  Do not attempt to access or manipulate the contents of the payment iframes. The browser blocks cross-origin access by design.

Token Security
--------------

A session is a signed JWT with a short lifespan. `Cybersource` recommends that you follow these practices:

* Generate a new session for each checkout. Do not reuse sessions across checkouts or customers.

* Keep the session server-side until needed. Pass it to the client only when the customer is ready to pay.

* Set `targetOrigins` to only the domains that host the SDK. Do not use wildcard origins or include domains that do not need access.  
  The transient token returned by `mount()` or complete() expires after 15 minutes. `Cybersource` recommends that you follow these practices:

* Send the transient token to your server immediately after receiving it.

* Verify the token signature using the public key from the session before authorizing the payment. For verification details, see [Transient Tokens](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-tokens-intro.md "").

* Do not store transient tokens in browser storage (`localStorage`, `sessionStorage`, or cookies). Process them server-side and discard.

Immutable API
-------------

The client interface that is returned by `VAS.UnifiedCheckout()` is frozen with `Object.freeze()`. This prevents runtime tampering, which means that no properties can be added, removed, or modified on the client, checkout, trigger, or button objects. Do not attempt to modify or extend the SDK objects. If you need custom behavior, use the event system to react to SDK state changes.

Cleanup
-------

You must always call `destroy()` on the client when the payment flow is complete or the customer navigates away. This removes all iframes and clears internal state:

```
checkout.destroy();
client.destroy();
```

If you do not destroy the client, you could leave payment iframes in the page after they are no longer needed.

PCI Compliance {#uc_pci_compliance}
===================================

The least burdensome level of Payment Card Industry (PCI) compliance is [Self-Assessment Questionnaire A (SAQ-A)](https://www.pcisecuritystandards.org/documents/SAQ_A_v3.pdf ""). To be compliant with SAQ-A, you must securely capture sensitive payment data with a validated payment provider. `Unified Checkout` meets this requirement by rendering secure iframes hosted by `Cybersource`. Payment data is submitted directly to `Cybersource` and never touches your systems.

Security Architecture
---------------------

`Unified Checkout` uses many layers of protection to be compliant with PCI SAQ-A guidelines:
* **Iframe isolation** : All payment UI renders inside cross-origin iframes hosted by `Cybersource`. Your page cannot access payment data within the iframe due to the browser's same-origin policy.

* **Origin verification** : The SDK validates that the hosting page origin matches the `targetOrigins` declared in the session.

* **Immutable API** : The client interface returned by `VAS.UnifiedCheckout()` is frozen with `Object.freeze()`. This prevents runtime tampering.

* **Closure-based privacy**: The internal SDK state is not accessible from outside the SDK. There are no public properties that expose session data or credentials.

* **Short-lived tokens**: The session and transient tokens expire after a short period, limiting the window for misuse  
  Because `Unified Checkout` handles payment data capture within secure iframes, your page never receives, processes, or stores cardholder data. This means that you qualify for SAQ-A over the more burdensome SAQ A-EP or SAQ D and your PCI audit scope is significantly reduced compared to direct API integrations.  
  Even with all that `Unified Checkout` handles, you must still do the following to remain SAQ-A compliant:

* All pages that load the SDK must use Transport Layer Security (TLS).

* You must restrict which domains can load scripts and frames. For information about the required directives, see [Security Recommendations](/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-security-recs.md "").

* You must generate a new session for each checkout and restrict `targetOrigins` to only your domains.

* You must send transient tokens to your server over HTTPS and verify their signatures before authorizing payments.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.
