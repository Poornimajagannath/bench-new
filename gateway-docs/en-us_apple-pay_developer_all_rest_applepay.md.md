Apple Pay Developer Guide {#applepay-DEV-about-guide}
=====================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is for merchants who want to offer Apple Pay in an iOS mobile app or web page and use information from Apple to process payments through `Payment Gateway`. The guide describes how to integrate Apple Pay with your system and how to process and search for Apple Pay transactions. Processing is described for Apple Pay payment authorizations, sale (authorization with capture) transactions, authorization reversals, and payment captures. The method you use to extract and decrypt Apple Pay payment data depends on how you integrated Apple Pay into your iOS app or website.
:
**With the `Elavon` processor,** `Payment Gateway` supports Apple Pay as a digital wallet, and this guide shows how to authorize an Apple Pay digital wallet payment with and without 3-D Secure authentication.

Conventions
:
These statements appear in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

    > TIP
    > A *Tip* contains information that can help you to complete a tasks or learn a concept.

Related Documentation
:
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional technical documentation.
:
When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information:

    * Apple ID: <https://appleid.apple.com>
    * Apple Support: <https://support.apple.com/>
    * Apple Developer Support: <https://developer.apple.com/support/>
    * Apple Developer Programs: <https://developer.apple.com/programs/>
    * Apple Developer Help: <https://developer.apple.com/help/>
    * Apple Developer Documentation: <https://developer.apple.com/documentation/>

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#applepay-doc-revisions}
===========================================================

26.03.01
--------

`Elavon` support for Apple Pay digital wallets
:
Introduced support for Apple Pay Digital Wallets with the *`Elavon` processor* . See these sections:

    * [Authorizing an Apple Pay Digital Wallet Payment without 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-no-3ds.md "")
    * [Authorizing an Apple Pay Digital Wallet Payment with 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-with-3ds.md "")

    `Elavon` supports 3-D Secure 2.2 with Diners Club, Mastercard, and Relay card transactions.

List of processors and cards
:
Added a list of processors and card types supported with Apple Pay. See [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").

25.09.01
--------

Single guide for the REST API covers all processors supported for Apple Pay
:
This guide combines information for all processors supported for Apple Pay.
:

Information for Authorizing an Apple Pay Payment with Merchant Decryption
:
Updated the topic [Fields Required to Authorize a Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-fields.md "") to include these fields for authorizing Mastercard payments:

    * consumerAuthenticationInformation.ucafAuthenticationData
    * consumerAuthenticationInformation.ucafCollectionIndicator

:
Added REST API code examples for payment card types in addition to Relay card. See these topics:

    * [REST Example: Authorize an American Express Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-amex.md "")
    * [REST Example: Authorize a Discover Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-discover.md "")
    * [REST Example: Authorize a JCB Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-jcb.md "")
    * [REST Example: Authorize a mada Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-mada.md "")
    * [REST Example: Authorize a Mastercard Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-mc.md "")

Information for Processing an Apple Pay Sale with Merchant Decryption
:
Updated the topic [Fields Required to Process a Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-fields.md "") to include these fields for authorizing Mastercard payments:

    * consumerAuthenticationInformation.ucafAuthenticationData
    * consumerAuthenticationInformation.ucafCollectionIndicator

:
Added REST API code examples for payment card types in addition to Relay card. See these topics:

    * [REST Example: Process an American Express Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-amex.md "")
    * [REST Example: Process a Discover Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-discover.md "")
    * [REST Example: Process a JCB Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-jcb.md "")
    * [REST Example: Process a mada Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-mada.md "")
    * [REST Example: Process a Mastercard Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-mc.md "")

25.04.01
--------

:
This revision contains only editorial changes and no technical updates.

25.01.01
--------

Use of the eCommerce Indicator
:
Removed the processingInformation.commerceIndicator REST API field from request messages for transactions that entail authorization with `Payment Gateway` decryption. Added the field to request messages for transactions that entail authorization with merchant decryption. See these tasks:

    * [Authorize an Apple Pay Payment with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-pgw-ex.md "")
    * [Authorize an Apple Pay Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex.md "")
    * [Process an Apple Pay Sale with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-pgw-ex.md "")
    * [Process an Apple Pay Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex.md "")

Specifying the Card Type and the Cryptogram Value with Merchant Decryption
:
Added the paymentInformation.tokenizedCard.type field and removed the paymentInformation.tokenizedCard.cryptogram field. See these tasks:

    * [Authorize an Apple Pay Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex.md "")
    * [Process an Apple Pay Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex.md "")

Introduction to Apple Pay {#applepay-intro}
===========================================

Apple Pay is a digital payment solution that enables your customers to make secure and convenient purchases without requiring them to enter their card details or shipping information. You can use the `Payment Gateway` platform to process and manage Apple Pay transactions.  
When you offer your customers *device apps* enabled for Apple Pay, you can collect payments for purchases made on iPhone and Apple Watch apps. When you offer your customers *Apple Pay on the web* , Apple Pay cardholders can purchase goods and services from within your web app. You can try an Apple Pay test transaction on the Apple Developer site by using the *Apple Pay on the Web Interactive Demo*:  
<https://applepaydemo.apple.com/>  
Using Apple Pay on the `Payment Gateway` platform can reduce the exposure of sensitive payment data to your system. When a cardholder initiates a purchase from within your Apple Pay enabled app or web page, Apple Pay receives the encrypted transaction. An Apple Pay server returns the transaction payment information re-encrypted with a developer-specific key. The key helps to ensure that only the app or the web page can access the encrypted information.  
Customers experience reduced payment friction because their information is tokenized and stored for future use. Customers who configure auto-fill options for their Apple Pay accounts can have payment and card data pre-populate after they sign in to their accounts and authenticate.

Apple Pay Digital Wallets (with the Elavon Processor)
-----------------------------------------------------

**With the `Elavon` processor,** `Payment Gateway` supports Apple Pay as a digital wallet, which is a mobile app that enables users to link their credit cards, debit cards, loyalty card to their mobile phones. The mobile wallet enables fast online checkouts and contactless in-store payments. `Payment Gateway` digital wallets integrate through `Unified Checkout`, ensuring secure transactions.  
`Elavon` supports 3-D Secure 2.2 with Diners Club, Mastercard, and Relay card transactions. The section [Authorizing Apple Pay Digital Wallet Payments (with Elavon)](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet.md "") covers authorizations of Apple Pay digital wallet payments without 3-D Secure and with 3-D Secure.

Processors and Cards Supported
------------------------------

Support for card types and optional features varies by partner and processor. For a list of processors and cards supported with Apple Pay, see [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").

Two Apple Pay Decryption Methods {#applepay-intro-built-in-hooks}
=================================================================

Integration hooks for two Apple Pay decryption methods are built into the `Payment Gateway` payment management platform. The two decryption methods---`Payment Gateway` decryption and merchant decryption---handle Apple Pay encrypted payment data differently. You will integrate the decryption method that best suits your technical development environment in terms of desired degree of exposure to, or control over, sensitive payment information.
IMPORTANT The Apple Pay decryption method that you integrate determines how you will format your API request messages when you authorize a payment or process a sale.  
To integrate Apple Pay into your system, you simply register with both Apple and `Payment Gateway`, generate keys and certificates (or `Payment Gateway` creates and manages them on your behalf), and place the Apple Pay mark on your app or web page. This guide includes instructions for integrating Apple Pay on `Payment Gateway` into your system. The instructions cover both of the Apple Pay decryption methods.

Integration Options {#applepay-intro-integration}
=================================================

`Payment Gateway` supports Apple Pay in multiple integration options. Three of the most widely used options are `Payment Gateway` decryption, merchant decryption, and `Checkout API`. Each option presents specific tradeoffs and advantages, and you can select the integration model that best fits your business.  
Apple Pay integration is built into the `Payment Gateway` payment management platform. `Payment Gateway` offers two integration methods for handling the payment data returned by the Apple Pay service for processing payments. In response to an authorization request, Apple Pay returns payment data in an encrypted payload. The encrypted payment data is handled and processed differently, depending on which integration method is used. Both decryption methods support Apple Pay in-app and Apple Pay on the web.

`Payment Gateway` Decryption {#applepay-intro-integration-pgw}
===========================================================

For `Payment Gateway` decryption, you implement Apple Pay directly on your checkout page. You send `Payment Gateway` all encrypted payment information that you receive from Apple Pay. `Payment Gateway` creates and manages the Apple Pay decryption keys, extracts and decrypts payment information, and maps the information to the appropriate fields for authorization and other payment services on your behalf. Having `Payment Gateway` process your Apple Pay transactions reduces your exposure to sensitive payment information.

Merchant Decryption {#applepay-intro-integration-merch}
=======================================================

For merchant decryption, you (the merchant or the integrator) manage all aspects of the Apple Pay implementation, from generation of the payment encryption keys to decryption of the payment response payload from Apple Pay. As a merchant, you submit the Apple Pay payment token and other payment information to `Payment Gateway` for processing. With merchant decryption, payment instrument details remain visible to you, and you control the technical development that decrypts this information.

`Unified Checkout` {#applepay-intro-integration-unified}
========================================================

`Unified Checkout` is a consolidated digital acceptance product. `Unified Checkout` offers a single implementation for multiple payment options. This integration type is designed for merchants looking for a single solution for integrating multiple digital payment options.

> IMPORTANT
> ` Unified Checkout ` is not covered in this guide. It is mentioned here for the sake of completeness. For information about Unified Checkout, see the [Unified Checkout Integration Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "") .

Payment Services Supported for Apple Pay {#applepay-intro-supported-services}
=============================================================================

Apple Pay is supported for the authorization, sale, authorization reversal, and capture services. The credit and void services are also supported for Apple Pay.

Authorization
-------------

An authorization confirms that a payment card account holds sufficient funds to pay for a purchase. A successful authorization places a hold on the funds in the account, reducing the cardholder's available limits by the authorized amount. The authorization service is supported with both types of Apple Pay decryption. For more information, see these topics:

* [Authorize an Apple Pay Payment with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-pgw-ex.md "")
* [Authorize an Apple Pay Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex.md "")

Sale (Authorization and Capture)
--------------------------------

A sale bundles an authorization and capture into a single transaction. Request the authorization and capture at the same time. Upon a successful transaction, funds are immediately transferred from the cardholder account to the merchant account. The authorization and capture amounts must be the same. The sale service is supported with both types of Apple Pay decryption. For more information, see these topics:

* [Process an Apple Pay Sale with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-pgw-ex.md "")
* [Process an Apple Pay Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex.md "")

Authorization Reversal
----------------------

Initiate an authorization reversal to reverse an unnecessary or undesired authorization. A successful authorization reversal releases the hold that the authorization placed on the cardholder's credit card funds. Include in the request message the request ID returned from the previous authorization because the request ID links the reversal to the authorization.  
For more information, see [Reverse an Apple Pay Payment Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-reversal-ex.md "").

Capture
-------

A capture, also known as settlement, transfers funds from the cardholder's account to your bank, typically in 2 to 4 days, and it releases the hold that the authorization placed on the cardholder's credit card funds. Include in the capture request message the request ID returned from the previous authorization because the request ID links the capture to the authorization.  
For more information, see [Capture an Apple Pay Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-capture-ex.md "").

Credit
------

A **refund** (also known as a follow-on credit) is a payment refund from your bank to the cardholder for a payment that has already been captured. To initiate a refund, send a request message to the **credit service** and include the request ID that was returned in the response to the capture request. Because the request ID links to the cardholder's billing and account information, you are not required to include those fields in the credit request. Unless otherwise specified, you must request a refund within 180 days of a settlement.  
For more information about credit requests and credit authorization results, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Void
----

You can void an Apple Pay capture or credit that was submitted but is not yet processed by the processor. You send a request for a capture void and a credit void to different endpoints. A void is linked to a capture or credit transaction through the request ID of the transaction you want to void. As a best practice, also include an order reference number or a tracking number. This number can help you to perform meaningful searches for the transaction.  
For more information about void requests and responses, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Summary of Requirements for Using Apple Pay {#applepay-intro-requirments}
=========================================================================

This topic lists the key requirements for using Apple Pay. More detailed information is provided in [Getting Started with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-getting-started.md "").

A `Payment Gateway` merchant account.
:
If you do not have a merchant account, contact your `Payment Gateway` sales representative.
:

Apple Pay enabled for your `Payment Gateway` account.
:
If Apple Pay is not enabled, contact your `Payment Gateway` representative.
:

A `Payment Gateway` `Business Center` sandbox account.
:
To create a test account, visit the [`Business Center` Sandbox Account Sign-Up](https://developer.example.com/hello-world/sandbox.md "") page.
:
Test account login page: ` `<https://businesscentertest.example.com/ebc2>` `
:

A `Payment Gateway` `Business Center` production account with a supported processor.
:
If you do not have a production account, contact your `Payment Gateway` sales representative.
:
Production account login page: ` `<https://businesscenter.example.com>` `
:
Production account login in India: [https://businesscenter.in.payment-gateway.in.com](https://businesscenter.in.example.com "")
:

> IMPORTANT
> Apple Pay relies on authorizations with payment network tokens. Your environment must meet these requirements in order to support payment network tokenization:
>
> * Your processor supports payment network tokens.
> * ` Payment Gateway ` supports payment network tokens with your processor.
>
> If your environment does not meet both requirements, you have these options:
>
> <!-- -->
> * Obtain a new merchant account with a processor that supports payment network tokens.

* Wait until your processor supports payment network tokens.

Processors and Cards Supported with Apple Pay {#applepay-ref-6-supported-processors-all}
========================================================================================

This table lists processors and card types supported with Apple Pay.

|                     Processor Name                      |                                                                                                                                                                                                                                                       Card Types                                                                                                                                                                                                                                                       |                                               Optional Features                                                |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `American Express Direct`                               | * American Express                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | * Multiple partial captures * Recurring payments                                                               |
| `Banque de France et Tresor Public`                     | * Cartes Bancaires * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | * Recurring payments                                                                                           |
| `Barclays`                                              | * Diners Club * Discover * Maestro (International) * Maestro (UK Domestic) * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                         | * Multiple partial captures * Recurring payments                                                               |
| `BNP Paribas France`                                    | * Cartes Bancaires * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | * Recurring payments                                                                                           |
| `Chase Paymentech Solutions`                            | * American Express * Discover * Maestro (International) * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                            | * Merchant-initiated transactions * Multiple partial captures * Recurring payments                             |
| `Cielo`3 `Cielo`3 is a Brazilian payment gateway.       | * American Express * Aura * Diners Club * Discover * Elo * Hipercard * JCB * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                         | * Merchant-initiated transactions * Multiple partial captures * Recurring payments * Subsequent authorizations |
| `Credit Mutuel-CIC`                                     | * Cartes Bancaires * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | * Recurring payments                                                                                           |
| `Elavon`                                                | * Diners * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                |
| `Elavon Americas`                                       | * American Express * Discover * JCB * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                | * Merchant-initiated transactions * Multiple partial captures * Recurring payments                             |
| `FDC Compass`                                           | * American Express * Discover * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | * Multiple partial captures * Recurring payments                                                               |
| `FDC Nashville Global`                                  | * American Express * Diners Club * Discover * JCB * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Multiple partial captures * Recurring payments * Subsequent authorizations                                   |
| `GPN`                                                   | * American Express * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ---                                                                                                            |
| `HSBC` `HSBC` is the `Payment Gateway` name for `HSBC` U.K. | * Maestro (International) * Maestro (UK Domestic) * Mastercard * Relay * Relay Electron                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Merchant-Initiated transactions * Multiple partial captures * Recurring payments                             |
| `JCN Gateway`                                           | * American Express * JCB * Mastercard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Multiple partial captures * Subsequent authorizations                                                        |
| `Moneris`                                               | * American Express * China UnionPay * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                | * Merchant-initiated captures * Recurring payments                                                             |
| `OmniPay Direct`                                        | * Maestro (International) * Maestro (UK Domestic) * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Multiple partial captures * Recurring payments                                                               |
| `SIX` Supports only card-present transactions.          | * Maestro (International) * Maestro (UK Domestic) * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Recurring payments                                                                                           |
| `Streamline`                                            | * Maestro (International) * Maestro (UK Domestic) * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                  | * Multiple partial captures * Recurring payments * Subsequent authorizations                                   |
| `TSYS Acquiring Solutions`                              | * American Express * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | * Multiple partial captures                                                                                    |
| `Vero`                                                  | * Elo * Mastercard * Relay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | * Merchant-Initiated transactions * Recurring payments * Subsequent authorizations                             |
| `Platform Connect`                                 | * JCB * mada Debit cards and prepaid cards issued in the Kingdom of Saudi Arabia. * Mastercard Including mada co-badged cards issued in the Kingdom of Saudi Arabia. * Relay Including mada co-badged cards issued in the Kingdom of Saudi Arabia.                                                                                                                                                                                                                                                                      | * Merchant-Initiated transactions * Multiple partial captures * Recurring payments                             |
| `Worldpay Relay`                                          | * American Express * Diners Club * Discover * JCB * Mastercard * Relay `Worldpay Relay` supports network tokens and digital payments with Mastercard transactions. `Worldpay Relay` also supports 3-D Secure 2.0 with Mastercard transactions. However, `Worldpay Relay` does not support the 3-D Secure 2.0 protocol when it is used with network tokens or digital payment. `Payment Gateway` declines any transaction processed by `Worldpay Relay` that uses both 3-D Secure 2.0 and either network tokens or digital payments. | * Recurring payments                                                                                           |
[Processors, Card Types, and Optional Features Supported with Apple Pay]

Getting Started with Apple Pay {#applepay-getting-started}
==========================================================

This section describes requirements for integrating Apple Pay into your system:

* Requirements for payment network token support
* Requirements for enrolling in the Apple Developer Program
* Requirements for end-to-end testing

Some of the requirements will be met as you complete the steps described in [Integrating Apple Pay into Your System](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg.md "").

Requirements for Payment Network Token Support {#applepay-getting-started-reqts-pnt-support}
============================================================================================

Apple Pay relies on authorizations being processed with *payment network tokens* . Make sure your processor and your `Payment Gateway` test accounts and production accounts meet these requirements.

Your processor supports payment network tokens and `Payment Gateway` supports payment network tokens with your processor.
:
If your processor does not support payment network tokens, or if `Payment Gateway` does not support payment network tokens with your processor, you must obtain a new `Payment Gateway` merchant account with a processor that supports payment network tokens.

Your `Payment Gateway` test account supports payment network tokens with your payment processor.
:
In order to configure and validate a test integration of Apple Pay, your `Payment Gateway` merchant test account supports payment network tokens with your processor.
:
If you do not have a merchant test account that meets this criteria, contact your `Payment Gateway` sales representative.

Your `Payment Gateway` production account supports payment network tokens with your payment processor.
:
In order to use your Apple Pay implementation in a production environment, your `Payment Gateway` merchant production account supports network tokens with your processor.
:
If you do not have a production account that meets these criteria, contact your `Payment Gateway` sales representative.

Requirements for Enrolling in the Apple Developer Program {#applepay-getting-started-reqts-apple-dev-pgm}
=========================================================================================================

The Apple Pay integration process requires you to enroll your organization in the Apple Developer Program. The exact requirements can vary depending on the specifics of your app and business. Always refer to official Apple documentation for the most up-to-date information. IMPORTANT

> If you are enabling Apple Pay digital payments on ` Unified Checkout `, see the [Unified Checkout Integration Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "") . The requirements described in this topic apply only if you are integrating *standalone Apple Pay* for ` Payment Gateway ` decryption or merchant decryption.

Your Apple device runs the latest Apple Developer app.
:
The machine that you use for **enrollment** must be an Apple device that run the latest version of the Apple Developer app. You can download the app from the Apple App Store.

You have an Apple ID with two-factor authentication and a valid payment method.
:
An Apple ID grants access to Apple Developer resources, including documentation, sample code, forums, and technical support. This Apple ID can be different from the Apple ID that you used to sign in to your enrollment device.
:
Two-factor authentication is required in order to sign in to your Apple Developer account and manage your account in the Certificates, Identifiers \& Profiles page. The payment method associated with your Apple ID is used to pay the annual subscription fee.

You will be the Account Holder or Admin for your organization.
:
As the person enrolling your organization in the Apple Developer Program, you automatically become the Account Holder for your project. Either of these roles enables you to generate an Apple Pay encryption key to encrypt payment data during the payment flow.
:
Each developer in your organization must be assigned to your project as an Account Holder or an Admin. Only an Account Holder or an Admin can create developer accounts for their team.

You have the information about your organizations that is required for enrollment.
:
You must provide basic business details and a D-U-N-S Number. Apple verifies that the information you provide is accurate and current before approving your enrollment.

You have the authorization to pay the annual membership fee.
:
The annual membership fee that you pay to Apple enables you to distribute your apps on the Apple App Store and to access beta software, beta testing tools, advanced app capabilities, and app analytics.

You must accept the terms of the license agreement.
:
You must agree to the Apple Developer Program License Agreement.

Requirements for End-to-End Testing {#applepay-getting-started-reqts-end-to-end-test}
=====================================================================================

This topic lists the requirements for supporting end-to-end testing of Apple Pay transaction processing in a testing environment. End-to-end testing requires that test payment cards have been loaded to your Apple Developer sandbox tester account wallet. IMPORTANT If these requirements are not met, Apple Pay servers will not return a valid payload in your test environment.

You have an Apple sandbox tester account.
:
For sandbox setup instructions, see the *Sandbox Testing* page in the Apple Developer portal: <https://developer.apple.com/apple-pay/sandbox-testing/>
:
Follow the steps described in the section *Create a Sandbox Tester Account*.

If you are integrating the merchant decryption model, you have an Apple test device.
:
You must register the device with Apple using your Apple Developer account. You will use test device to create the certificate signing request (CSR) that you will use to associate your Apple sandbox tester account with your test environment.
:
If you are integrating the merchant decryption model, you will use the Apple device in one of the tasks described in [Part 2: Create an Apple Pay Payment Processing Certificate](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert.md "").

You have a test environment that you can access by logging in to your Apple sandbox tester account.
:
To create this access, you will use the sandbox tester account to create an Apple test merchant ID. You will use the test ID to create a CSR and use the CSR to create an Apple Pay payment processing certificate. Apple Pay servers use this certificate to encrypt payment data using a key known to your test environment.
:
The steps for associating a sandbox tester account with your test environment (as well as for associating an Apple production account with your production environment) are included in [Part 2: Create an Apple Pay Payment Processing Certificate](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert.md "").

You have test payment cards in the wallet of your Apple sandbox tester account.
:
You will be instructed to add test cards to your sandbox tester account in [Validating Your Test Integration](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-4-validate-on-test.md "").

Integrating Apple Pay into Your System {#applepay-cfg}
======================================================

This section describes how to integrate Apple Pay into your iOS app or website. The integration tasks are organized into three parts. The second part provides separate steps for the two different decryption models. The third part applies only if you will be supporting Apple Pay on the web.  
You will perform the integration tasks twice: First in your test environment and, after you validate your test integration, a second time in your production environment.

* **Part 1: Set Up Your Apple Developer Account** . You will enroll your organization in the Apple Developer Program, create an *Apple merchant ID*, and register it in your developer account.
* **Part 2: Create an Apple Pay Payment Processing Certificate** . This certificate is associated with your merchant ID, and it is used by Apple Pay servers to encrypt payment data.
  * You will generate a *certificate signing request* (CSR) at the system that will handle Apple Pay payload decryption. For `Payment Gateway` decryption, you will generate the CSR at the `Payment Gateway` `Business Center` user interface. For merchant decryption, you will generate the CSR at your Apple device.
  * You will upload the CSR with the public key to your Apple Developer account and use the CSR to create a *payments processing certificate* for your merchant ID and Apple Pay.
* **Part 3: Perform Additional Setup for Apple Pay on the Web** . If you offer your customers Apple Pay on the web, you will create an *Apple Pay merchant identity certificate* , associate the certificate with your merchant ID, and register *each merchant domain* that will process Apple Pay transactions.

> TIP
> If you are integrating **Apple Pay with ` Payment Gateway ` decryption** and you are experienced in creating Apple Pay payment processing certificates, you can use the [Quick Integration for the Payment Gateway Decryption Method](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-reference/applepay-ref-1-pgw-decrypt-quick.md "") instead of the detailed steps in this section.

Part 1: Set Up Your Apple Developer Account {#applepay-cfg-1-dev-pgm}
=====================================================================

Complete the tasks in this section to enroll your organization in the Apple Developer program and register a new Apple merchant ID.

Starting Enrollment in the Apple Developer Program {#applepay-cfg-1a-dev-pgm-enroll-start}
==========================================================================================

Enrolling in the Apple Developer program as an organization enables you to associate multiple developer accounts with your Apple Developer account. Multiple developer accounts can be beneficial if you have a large project with a team of developers.  
For the first phase of the enrollment process, you log in to your Apple Developer account and submit information about your organization to Apple. IMPORTANT

> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to start the enrollment process:
2. Launch the Apple Developer app on your device.
3. Click Account, and sign in with your Apple ID.
4. If prompted, review the Apple Developer Agreement and click Agree.
5. Click Enroll Now, review the program benefits and requirements, and then click Continue.
6. At the prompts, enter your information as the Account Holder.
7. At the prompts, enter information about your organization.

#### RESULT

After Apple verifies your information and approves your enrollment, it sends you an email that describes the next steps.

Completing Enrollment in the Apple Developer Program {#applepay-cfg-1b-dev-pgm-enroll-complete}
===============================================================================================

When you receive your approval email from Apple, you will log in to your Apple Developer account again and complete the enrollment process. IMPORTANT

> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to complete the enrollment process:
2. Launch the Apple Developer app on the device you used to start the enrollment process.
3. Click Account and sign in with the Apple ID you used to start the enrollment process.
4. Click Continue Your Enrollment, review the terms of the Apple Developer Program License Agreement, and then click Agree.
5. Review the annual membership subscription details and click Subscribe.

Registering a New Merchant ID in Your Apple Developer Account {#applepay-cfg-1c-merch-id-create}
================================================================================================

Finish setting up your Apple Developer account by creating and registering a merchant ID for each environment. A registered merchant ID uniquely identifies you to Apple Pay as a valid entity that can accept payments.  
In order to support multiple environments, such as sandbox and production, you can create multiple merchant IDs in your Apple Developer account. IMPORTANT

> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to create a merchant ID and to register it in your Apple Developer account:
2. Log in to your Apple Developer account.
3. In the left navigation panel, select Certificates, Identifiers \& Profiles.
4. Click Identifiers.
5. Click the plus sign (+) on the top left.
6. Select Merchant IDs and click Continue.
7. Enter a merchant description and identifier name.
8. Click Continue.
9. Verify that you entered the merchant information correctly.
10. Click Register.

Part 2: Create an Apple Pay Payment Processing Certificate {#applepay-cfg-2-pay-proc-cert}
==========================================================================================

Complete the tasks in this section to create an Apple Pay payment processing certificate. Apple Pay servers use this certificate to encrypt payment data. Creation of an Apple Pay payment processing certificate consists of two tasks:

* Generating a certificate signing request (CSR).
* Using the CSR to create an Apple Pay payment processing certificate.

> IMPORTANT
> When you generate a CSR, the sequence of steps you will perform depends on whether you are integrating ` Payment Gateway ` decryption and merchant decryption.
>
> * If you are integrating ` Payment Gateway ` decryption, you will generate a CSR at the ` Payment Gateway ` ` Business Center `. See [Generating a CSR for Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2a-pay-proc-cert-ebc-gen-csr.md "").

* If you are integrating merchant decryption, you will generate a CSR at your Apple device. See [Generating a CSR for Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2b-pay-proc-cert-own-gen-csr.md "").

Generating a CSR for `Payment Gateway` Decryption {#applepay-cfg-2a-pay-proc-cert-ebc-gen-csr}
==========================================================================================

> IMPORTANT
> These steps apply to setting up ` Payment Gateway ` decryption only. If you are integrating the merchant decryption model of Apple Pay into your system, follow the steps in [Generating a CSR for Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2b-pay-proc-cert-own-gen-csr.md "") instead.  
> For `Payment Gateway` decryption, you will use your `Payment Gateway` account in the `Business Center` to generate a certificate signing request (CSR). You will use the Apple Pay Registration page within the `Business Center`.  
> If you do not have an Admin account or an account with write access, contact your Account Admin, `Payment Gateway` sales engineer, alliance partner, or technical account manager.

1. Follow these steps at the `Payment Gateway` `Business Center` to generate a CSR:

2. Log in to your `Payment Gateway` merchant account in the `Business Center`.

   #### ADDITIONAL INFORMATION

   Production: ` `<https://businesscenter.example.com>` `

   #### ADDITIONAL INFORMATION

   Production in India: [https://businesscenter.in.payment-gateway.in.com](https://businesscenter.in.example.com "")

   #### ADDITIONAL INFORMATION

   Test: ` `<https://businesscentertest.example.com/ebc2>` `

3. In the left navigation panel, select Payment Configuration.

4. Choose Digital Payment Solutions.

   #### ADDITIONAL INFORMATION

   The Digital Payment Solutions page appears.

5. Click Configure for Apple Pay.

   #### ADDITIONAL INFORMATION

   The Apple Pay Registration page appears.

   #### ADDITIONAL INFORMATION

   This image shows the Apple Pay Registration page in the `Payment Gateway` `Business Center`.

   #### Figure:

   Apple Pay Registration Page in the `Payment Gateway` `Business Center` Interface ![Business Center UI : Payment Configuration : Digital Payment Solutions : Apple Pay Registration (aem pdf)](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/applepay-dev/images/ebc-generate-new-csr.png/jcr:content/renditions/original)

6. Enter the Apple merchant ID that you created and registered in your Apple Developer account.

   #### ADDITIONAL INFORMATION

   These steps are described in [Registering a New Merchant ID in Your Apple Developer Account](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-1-dev-pgm/applepay-cfg-1c-dev-pgm-merch-id-create.md ""). This value should match the id you set up with Apple including the "merchant" prefix.

7. Click Generate new certificate signing request.

8. Click the download icon next to the key.

9. Download the certificate request file (a file with a *.certSigningRequest* file extension) to your local machine.

10. Use your browser controls to save the file to your local machine.

    #### ADDITIONAL INFORMATION

    In the next task, you will upload the CSR file to your Apple Developer account.

11. Proceed to [Creating a Payment Processing Certificate for Your Merchant ID](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2c-pay-proc-cert-apple-cre-cert.md "").

Generating a CSR for Merchant Decryption {#applepay-cfg-2b-pay-proc-cert-own-gen-csr}
=====================================================================================

> IMPORTANT
> These steps apply to setting up merchant decryption only. If you are integrating the ` Payment Gateway ` decryption model of Apple Pay into your system, follow the steps in [Generating a CSR for Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2a-pay-proc-cert-ebc-gen-csr.md "") instead.  
> For merchant decryption, you will use your Apple device to generate a certificate signing request (CSR). IMPORTANT
> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps at your Apple device to generate a CSR:
2. Sign in to your Apple Developer account as the Account Holder or as an Admin and select **Certificates, Identifiers \& Profiles**.
3. Click Identifiers in the sidebar.
4. Select Merchant IDs and click Continue.
5. Under Identifiers, select Merchant IDs using the filter on the top right.
6. On the right, select your merchant identifier.
7. Under Apple Pay Payment Processing Certificate, click Create Certificate.
8. Proceed to [Creating a Payment Processing Certificate for Your Merchant ID](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2c-pay-proc-cert-apple-cre-cert.md "").

Creating a Payment Processing Certificate for Your Merchant ID {#applepay-cfg-2c-pay-proc-apple-cre-cert}
=========================================================================================================

Using the certificate signing request that you just created, you will create an Apple payment processing certificate and associate the certificate with your Apple merchant ID that you created before that. Those earlier tasks are described in these topics:

* [Registering a New Merchant ID in Your Apple Developer Account](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-1-dev-pgm/applepay-cfg-1c-dev-pgm-merch-id-create.md "")
* [Creating a Payment Processing Certificate for Your Merchant ID](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert/applepay-cfg-2c-pay-proc-cert-apple-cre-cert.md "")  
  Apple Pay uses the payment processing certificate to encrypt the customer's payment information. This certificate expires every 25 months. If the certificate expires or is revoked, you can recreate it.

> IMPORTANT
> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to create a payment processing certificate for your Apple Pay merchant ID:

2. Sign in to your Apple Developer account as the Account Holder or as an Admin and select **Certificates, Identifiers \& Profiles**.

3. Upload the CSR file and associate the CSR with your merchant ID.

   #### ADDITIONAL INFORMATION

   The CSR contains your Apple merchant ID and a public key that Apple Pay uses to encrypt sensitive payment data.

   1. Click Identifiers in the sidebar.

   2. Select Merchant IDs using the filter on the top right.

   3. On the right, select your merchant ID.

      #### Step Result

      If a banner at the top of the page prompts you, you need to accept an agreement. Click Review Agreement and follow the instructions that appear.

   4. Under Apple Pay Payment Processing Certificate, click Create Certificate.

4. Create a payment processing certificate and download the certificate to your local machine.

   1. Click Choose File and select the CSR file that you uploaded.

      #### ADDITIONAL INFORMATION

      The CSR file has the filename extension *.certSigningRequest*.

   2. Click Choose.

   3. Click Continue.

   4. Click Download.

      #### Step Result

      The payment processing certificate (a file with the filename extension *.cert*) appears in your Downloads folder.

5. Go to the next task.

   * If you offer your customers Apple Pay in a web page, go to [Part 3: Perform Additional Setup for Apple Pay on the Web](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-3-opt-on-web.md "").

* Otherwise, proceed to [Validating Your Test Integration](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-4-validate-on-test.md "").

Part 3: Perform Additional Setup for Apple Pay on the Web {#applepay-cfg-3-opt-on-web}
======================================================================================

If you develop web pages that support Apple Pay on the Web, your customers can use Apple Pay to purchase goods and services from within your web page. You can use the same Apple Pay merchant ID and Apple Pay payment processing certificate as required for Apple Pay in-app implementations. However, Apple Pay on the Web requires additional set-up tasks that you perform in your Apple Developer account:

* Creating an Apple Pay merchant identity certificate
* Registering your merchant domains with Apple

If you created multiple merchant ID and payment processing certificate pairs to support multiple environments, such as sandbox and production, you must associate each ID-and-certificate pair with a unique merchant identify certificate.

Creating an Apple Pay Merchant Identity Certificate {#applepay-cfg-3a-opt-on-web-merch-id-cert}
===============================================================================================

If you offer your customers Apple Pay in a web page, you must create an Apple Pay merchant identity certificate and associate it with your merchant ID. You need this Transport Layer Security (TLS) certificate in order to authenticate your sessions with the Apple Pay servers. IMPORTANT

> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to create an Apple Pay merchant identity certificate:
2. Log in to your Apple Developer merchant account as an Account Holder or Admin.
3. In the left navigation panel, select Certificates, Identifiers \& Profiles.
4. Perform these steps for each merchant identity certificate you need to create:
   1. Click Identifiers, and click the plus sign (+) on the top left.
   2. Select Merchant IDs and click Continue.
   3. Enter the merchant description and identifier name, and then click Continue.
5. Click Register.

Registering Your Merchant Domains with Apple {#applepay-cfg-3b-opt-on-web-reg-merch-domains}
============================================================================================

Each merchant domain in your organization that will process Apple Pay transactions must be registered with Apple. IMPORTANT

> When you perform tasks at the Apple Developer portal, always refer to official Apple documentation for the most up-to-date information .

1. Follow these steps to register your merchant domains with Apple:
2. Log in to your Apple Developer merchant account as an Account Holder or Admin.
3. In the left navigation panel, select Certificates, Identifiers \& Profiles.
4. Perform these steps for each merchant domain that you registered with Apple:
   1. Click Identifiers, and select Merchant IDs in the pop-up menu on the top right.
   2. On the right, select your merchant identifier.
   3. Under Merchant Domains, click Add Domain. Enter the fully qualified name of the domain and click Save.
   4. Click Download, place the downloaded file in the specified locations, and click Verify.
5. After you add all merchant domains that will process Apple Pay transactions, click Done.

Verifying the Merchant Domains That You Registered with Apple {#applepay-cfg-3c-opt-on-web-vfy-merch-domains}
=============================================================================================================

1. Follow these steps to verify the merchant domains you registered with Apple:
2. Log in to your Apple Developer merchant account as an Account Holder or Admin.
3. In the left navigation panel, select Certificates, Identifiers \& Profiles.
4. Perform these steps for each merchant domain that you registered with Apple:
   1. Click Identifiers, and select Merchant IDs in the pop-up menu on the top right.
   2. On the right, select your merchant identifier.
   3. Under Merchant Domains, click Verify next to the domain name.
   4. Follow the instructions that appear on the screen.

#### RESULT

You can now proceed to [Validating Your Test Integration](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-4-validate-on-test.md "").

Validating Your Test Integration {#applepay-cfg-4-validate-on-test}
===================================================================

Before you integrate Apple Pay into your production environment, validate your test integration of Apple Pay.

1. Follow these steps to validate the integration in your test environment:

2. Make sure your system is prepared for end-to-end testing.

   #### ADDITIONAL INFORMATION

   See [Requirements for End-to-End Testing](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-getting-started/applepay-getting-started-reqts-end-to-end-test.md "").

3. Add test payment cards to the wallet of your Apple sandbox tester account.

   #### ADDITIONAL INFORMATION

   Instructions are provided in the *Sandbox Testing* page on the Apple Developer portal:  
   <https://developer.apple.com/apple-pay/sandbox-testing/>

   1. Follow the steps in the *Create a Sandbox Tester Account* section.

      #### ADDITIONAL INFORMATION

      Make sure the user account has permissions to use Apple Pay. You will use this account to log in to devices and services.

   2. Follow the steps in the *Adding a Test Card Number* section.

4. Using the `REST` API, send Apple Pay transaction requests to the test endpoints.

   #### ADDITIONAL INFORMATION

   Refer to the tasks in [Processing Apple Pay Transactions](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro.md "").

5. Adjust your integration settings as needed until your test transactions complete successfully.

#### RESULT

You can now proceed to [Integrating Apple Pay into Your Production Environment](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-5-integrate-on-prod.md "").

Integrating Apple Pay into Your Production Environment {#applepay-cfg-5-integrate-on-prod}
==========================================================================================

After you validate Apple Pay in your test environment, you can integrate Apple Pay into your production environment.

1. Follow these steps to integrate Apple Pay into your production environment:

2. Use your Apple merchant ID to generate a certificate signing request (CSR) and create a *production* Apple Pay payment processing certificate.

   #### ADDITIONAL INFORMATION

   See [Part 2: Create an Apple Pay Payment Processing Certificate](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-2-pay-proc-cert.md "").

3. If you offer your customers Apple Pay on the Web, perform the additional setup steps for your production environment.

   #### ADDITIONAL INFORMATION

   See [Part 3: Perform Additional Setup for Apple Pay on the Web](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg/applepay-cfg-3-opt-on-web.md "").

#### RESULT

You can now proceed to [Processing Apple Pay Transactions](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro.md "").

Processing Apple Pay Transactions {#applepay-txns-intro}
========================================================

`Payment Gateway` supports these payment services for Apple Pay: Authorization, Sale, Authorization Reversal, and Capture. This section of the guide contains tasks that show you how to use those services to process Apple Pay transactions:

* Authorize an Apple Pay payment with `Payment Gateway` decryption
* Authorize an Apple Pay payment with merchant decryption
* Process an Apple Pay sale with `Payment Gateway` decryption
* Process an Apple Pay sale with merchant decryption
* Reverse the authorization of an Apple Pay payment
* Capture an authorized Apple Pay payment  
  For each task in this section, the example request message includes the processingInformation. paymentSolution `REST` API field set to `001`. This value identifies Apple Pay as the digital payment solution.  
  IMPORTANT In response to your successful payment authorization request, Apple Pay returns an encrypted payload that contains sensitive payment information. The method you use to extract and decrypt the payment data depends on how you integrated Apple Pay into your system.  
  For high-level descriptions of the `Payment Gateway` decryption method and the merchant decryption method, see [Integration Options](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-intro-integration.md "").

Endpoints for Services Supported with Apple Pay {#applepay-ref-2-endpoints-applepay-services}
=============================================================================================

This topic lists the `REST` API endpoints that you use to request the services supported with Apple Pay.

Authorizing a Payment
---------------------

Production: `POST ``https://api.example.com``/pts/v2/payments`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments`  
Test: `POST ``https://apitest.example.com``/pts/v2/payments`

Processing a Sale
-----------------

Production: `POST ``https://api.example.com``/pts/v2/payments`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments`  
Test: `POST ``https://apitest.example.com``/pts/v2/payments`  
Make sure to set the processingInformation.capture field to `true`.

Reversing an Authorization
--------------------------

Production: `POST ``https://api.example.com``/pts/v2/payments/{id}/reversals`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments/{id}/reversals`  
Test: `POST ``https://apitest.example.com``/pts/v2/payments/{id}/reversals`  
Replace the `{id}` portion of the URL with the transaction ID of the payment that you want to reverse. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the authorization request. Example value: 7359642011156554503954

Capturing a Payment
-------------------

Production: `POST ``https://api.example.com``/pts/v2/payments/{id}/captures`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments/{id}/captures`  
Test: `POST ``https://apitest.example.com``/pts/v2/payments/{id}/captures`  
Replace the `{id}` portion of the URL with the transaction ID of the payment that you want to capture. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the authorization request. Example value: 7359642011156554503954

Processing a Refund
-------------------

Production: `POST ``https://api.example.com``/pts/v2/payments/{id}/refunds`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments/{id}/refunds`  
Test: `POST ``https://apitest.example.com``/pts/v2/payments/{id}/refunds`  
Replace the `{id}` portion of the URL with the transaction ID of the capture request for the payment you are refunding. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the capture request. Example value: 7359642011156554503954

Voiding a Capture
-----------------

Production: `POST ``https://api.example.com``/v2/captures/{id}/voids`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/payments/v2/captures/{id}/voids`  
Test: `POST ``https://apitest.example.com``/v2/captures/{id}/voids`  
Replace the `{id}` portion of the URL with the transaction ID of the capture that you want to void. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the capture request. Example value: 7359642011156554503954

Voiding a Credit
----------------

Production: `POST ``https://api.example.com``/pts/v2/credits/{id}/voids`  
Production in India: `POST ``https://api.in.example.com``/pts/v2/credits/{id}/voids`  
Test: `POST ``https://apitest.example.com``/pts/v2/credits/{id}/voids`  
Replace the `{id}` portion of the URL with the transaction ID of the credit you want to void. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the credit request. Example value: 7359642011156554503954

Authorize an Apple Pay Payment with `Payment Gateway` Decryption {#applepay-txn-auth-pgw-ex}
=========================================================================================

The topics in this section show to how to authorize an Apple Pay payment transaction with the *`Payment Gateway` decryption* implementation of Apple Pay:

* Basic Steps: Authorizing a Payment with `Payment Gateway` Decryption
* Fields Required to Authorize a Payment with `Payment Gateway` Decryption
* REST Example: Authorize a Payment with `Payment Gateway` Decryption
  For general information about basic authorizations, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Authorizing a Payment with `Payment Gateway` Decryption {#applepay-txn-auth-pgw-ex-rest-steps}
========================================================================================================

Follow these steps to request an Apple Pay payment authorization with `Payment Gateway` decryption:

1. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Authorize a Payment with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-pgw-ex/applepay-txn-auth-pgw-ex-rest-fields.md "").
   * Refer to the example in [REST Example: Authorize a Payment with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-pgw-ex/applepay-txn-auth-pgw-ex-rest-code.md "").
2. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
3. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Authorize a Payment with `Payment Gateway` Decryption {#applepay-txn-auth-pgw-ex-rest-fields}
=============================================================================================================

As a best practice, include these REST API fields in your request for an authorization transaction with the `Payment Gateway` decryption implementation of Apple Pay.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.fluidData.descriptor](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-descriptor.md "")
:
Format of the encrypted payment data.
:
Set the value to `RklEPUNPTU1PTi5BUFBMRS5JTkFQUC5QQVlNRU5U` for Apple Pay.

[paymentInformation.fluidData.encoding](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-encoding.md "")
:
Encoding method used to encrypt the payment data.
:
Set the value to `Base64` for Apple Pay.

[paymentInformation.fluidData.value](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-value.md "")
:
Set the value to the encrypted payment data value returned by the Full Wallet request.

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

REST Example: Authorize a Payment with `Payment Gateway` Decryption {#applepay-txn-auth-pgw-ex-rest-code}
======================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@example.com"
    }
  },
  "paymentInformation": {
    "fluidData": {
      "value": "eyJkYXRhIjoiXC9NK2VQQ0JlMmtod1pMQkFzRWhneHFqYXF2MmtZNDJSNnd1VDdnT3JlelBwRE9hR2dmc1AzZUNHZUplSjFSc3JpSERGSnJIK0FJVHp6RFdjVXNHUlNuSER3QlBcL2JHakU0dUhYcTFDOXFjWDBLWmYzaTFZNkV2b1wvaXExOFhkcG5obTI1U2kwSGpkWUJGRmVBUmZlVENpMEtDSGtRN04wZTAyeElRbm84Qmt1TVwvSUQ5bHdoNXBFVnVYM08ybjc4bHVyU0tlRmpXVHMyWG9Pc1pmWXBpbFQ4ZFFtK2RaYmh6VHgyZ2hMXC9FcFBReUVvdW5QTFZjTlwvaTR0blFnakxWRWJiNUFDNHJ4ZjBwK2M0VGtYSzcycGZGY05NSnlxd0RlQWZ2cHB6cnFQZVdoaWlpdzUwTmljT3duR29tcXA0bWU2anV4S2N5ZFh3cGpJR3BhQlBuXC9NY3o2d2ZDSFAzMWY1NHdkRmZ4bEZadjl5XC85aGw5YlY1d08yN2R5bFwvYUVxN2FYbU5JZHBQNTFsOXlSQlUzNDNYcjR3XC9MSXN2ZmZTTE91WDlsRU5QUGtocE1LUXo4VWpYNG0xXC9xazdcL256aGFSekFaZGh6VGZsNkZ3PT0iLCJ2ZXJzaW9uIjoiRUNfdjEiLCJoZWFkZXIiOnsiYXBwbGljYXRpb25EYXRhIjoiNDE3MDcwNkM2OTYzNjE3NDY5NkY2RTQ0NjE3NDYxIiwidHJhbnNhY3Rpb25JZCI6IjU0NzI2MTZFNzM2MTYzNzQ2OTZGNkU0OTQ0IiwiZXBoZW1lcmFsUHVibGljS2V5IjoiTUlJQlN6Q0NBUU1HQnlxR1NNNDlBZ0V3Z2ZjQ0FRRXdMQVlIS29aSXpqMEJBUUloQVBcL1wvXC9cLzhBQUFBQkFBQUFBQUFBQUFBQUFBQUFcL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL01Gc0VJUFwvXC9cL1wvOEFBQUFCQUFBQUFBQUFBQUFBQUFBQVwvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cLzhCQ0JheGpYWXFqcVQ1N1BydlZWMm1JYThaUjBHc014VHNQWTd6ancrSjlKZ1N3TVZBTVNkTmdpRzV3U1RhbVo0NFJPZEpyZUJuMzZRQkVFRWF4ZlI4dUVzUWtmNHZPYmxZNlJBOG5jRGZZRXQ2ek9nOUtFNVJkaVl3cFpQNDBMaVwvaHBcL200N242MHA4RDU0V0s4NHpWMnN4WHM3THRrQm9ONzlSOVFJaEFQXC9cL1wvXC84QUFBQUFcL1wvXC9cL1wvXC9cL1wvXC9cLys4NXZxdHB4ZWVoUE81eXNMOFl5VlJBZ0VCQTBJQUJPSnZpNkxGa0JpUTJINDR6K05VK0I3N1hZV2p4UHJQaXRDMFRWZytJYnNGeXIrNjFsemFkQjFrU25hUHpFTmVMMEVrbzhWTExzVjRhU1hTalwvZXlJRmc9IiwicHVibGljS2V5SGFzaCI6IlwvNkxQT3BoS0tydWFvdjBET3VOTDk1YXFCcFVcLzArNElXNXFhV3FxME5qRT0ifSwic2lnbmF0dXJlIjoiTUlJRFFnWUpLb1pJaHZjTkFRY0NvSUlETXpDQ0F5OENBUUV4Q3pBSkJnVXJEZ01DR2dVQU1Bc0dDU3FHU0liM0RRRUhBYUNDQWlzd2dnSW5NSUlCbEtBREFnRUNBaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUF3SnpFbE1DTUdBMVVFQXg0Y0FHTUFhQUJ0QUdFQWFRQkFBSFlBYVFCekFHRUFMZ0JqQUc4QWJUQWVGdzB4TkRBeE1ERXdOakF3TURCYUZ3MHlOREF4TURFd05qQXdNREJhTUNjeEpUQWpCZ05WQkFNZUhBQmpBR2dBYlFCaEFHa0FRQUIyQUdrQWN3QmhBQzRBWXdCdkFHMHdnWjh3RFFZSktvWklodmNOQVFFQkJRQURnWTBBTUlHSkFvR0JBTkM4K2tndGdtdldGMU96amdETnJqVEVCUnVvXC81TUt2bE0xNDZwQWY3R3g0MWJsRTl3NGZJWEpBRDdGZk83UUtqSVhZTnQzOXJMeXk3eER3YlwvNUlrWk02MFRaMmlJMXBqNTVVYzhmZDRmek9wazNmdFphUUdYTkxZcHRHMWQ5VjdJUzgyT3VwOU1NbzFCUFZyWFRQSE5jc005OUVQVW5QcWRiZUdjODdtMHJBZ01CQUFHalhEQmFNRmdHQTFVZEFRUlJNRStBRUhaV1ByV3RKZDdZWjQzMWhDZzdZRlNoS1RBbk1TVXdJd1lEVlFRREhod0FZd0JvQUcwQVlRQnBBRUFBZGdCcEFITUFZUUF1QUdNQWJ3QnRnaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUFEZ1lFQWJVS1lDa3VJS1M5UVEybUZjTVlSRUltMmwrWGc4XC9KWHYrR0JWUUprT0tvc2NZNGlOREZBXC9iUWxvZ2Y5TExVODRUSHdOUm5zdlYzUHJ2N1JUWTgxZ3EwZHRDOHpZY0FhQWtDSElJM3lxTW5KNEFPdTZFT1c5a0prMjMyZ1NFN1dsQ3RIYmZMU0tmdVNnUVg4S1hRWXVaTGsyUnI2M044QXBYc1h3QkwzY0oweGdlQXdnZDBDQVFFd096QW5NU1V3SXdZRFZRUURIaHdBWXdCb0FHMEFZUUJwQUVBQWRnQnBBSE1BWVFBdUFHTUFid0J0QWhCY2wrUGYzK1U0cGsxM25WRDlud1FRTUFrR0JTc09Bd0lhQlFBd0RRWUpLb1pJaHZjTkFRRUJCUUFFZ1lDZ2RvN2lrTzdERTNCXC9pY0lycmRjc1ZIanJyQmNPdXNndXhlcGs1QW41ZEExV01rajBlVjRsMVM0RnR5NktwdlR0T0xcL3VSdDhuTHZpVnR0TVVSZHBYTjNWXC9NVmZnVkxlXC9YUm5cLzRzbUJnMVgweE5OTXlTZXBQalVxV1ZkWFg1K0RWYnp2U0ZKSVJGdmt1MHJPaGg3REZmODVpbXNkaGRZRUhCaUg0TzdpK1E9PSJ9",
      "descriptor": "RklEPUNPTU1PTi5BUFBMRS5JTkFQUC5QQVlNRU5U",
      "encoding": "Base64"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359642011156554503954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359642011156554503954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359642011156554503954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "consumerAuthenticationInformation": {
    "token": "Axj/7wSTjveM2Bej4NcSABsY1aQodZpGb2Y8uGnvx4dJq4Cnvx4dJq+kCvoTi4ZNJMvRiuIkVgTk473jNgXo+DXEgAAAkQmH"
  },
  "id": "7359642011156554503954",
  "issuerInformation": {
    "responseRaw": "0110322000000E1000020000000000000010000104041641840132353442435634463759474B433833313030303030000159008000223134573031363135303730333830323039344730363400103232415050524F56414C00065649435243200034544B54523031313132313231323132313231544C3030323636504E30303431313131"
  },
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
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
      "expirationYear": "2025",
      "requestorId": "12121212121",
      "prefix": "411111",
      "assuranceLevel": "66",
      "expirationMonth": "07",
      "suffix": "1111",
      "type": "001"
    },
    "card": {
      "suffix": "1111",
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "02495701"
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "merchantNumber": "000372839590885",
    "approvalCode": "831000",
    "networkTransactionId": "016150703802094",
    "transactionId": "016150703802094",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "54BCV4F7YGKC",
  "riskInformation": {
    "earlyVelocity": {
      "counts": [
        {
          "count": "1",
          "informationCode": "MVEL-R1"
        }
      ]
    }
  },
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T04:16:42Z"
}
```

Authorize an Apple Pay Payment with Merchant Decryption {#applepay-txn-auth-merch-ex}
=====================================================================================

The topics in this section show to how to authorize an Apple Pay payment transaction with the *merchant decryption* implementation of Apple Pay

* Basic Steps: Authorizing a Payment with Merchant Decryption
* Fields Required to Authorize a Payment with Merchant Decryption
* REST Example: Authorize an American Express Payment
* REST Example: Authorize a Discover Payment
* REST Example: Authorize a JCB Payment
* REST Example: Authorize a mada Payment
* REST Example: Authorize a Mastercard Payment
* REST Example: Authorize a Relay Payment

> IMPORTANT
> Support for cards varies by partner and processor. For a list of processors and cards supported with Apple Pay, see [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").
> For general information about basic authorizations, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Authorizing a Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-steps}
====================================================================================================

1. Follow these steps to request an Apple Pay payment authorization with merchant decryption:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Authorize a Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-fields.md "").

   * Refer to the example for your payment card type:

     * [REST Example: Authorize an American Express Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-amex.md "")
     * [REST Example: Authorize a Discover Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-discover.md "")
     * [REST Example: Authorize a JCB Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-jcb.md "")
     * [REST Example: Authorize a mada Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-mada.md "")
     * [REST Example: Authorize a Mastercard Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-mc.md "")
     * [REST Example: Authorize a Relay Payment with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-auth-merch-ex/applepay-txn-auth-merch-ex-rest-code-relay.md "")

     > IMPORTANT In these code examples, any test card numbers that contain zeroes are formatted with Xs replacing the zeroes. When you test using one of these reformatted card numbers, replace each X with a 0 (zero).

3. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Authorize a Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-fields}
=========================================================================================================

As a best practice, include these REST API fields in your request for an authorization transaction with the `Payment Gateway` decryption implementation of Apple Pay.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.ucafAuthenticationData](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-ucaf-auth-data.md "")
:
Universal cardholder authentication field (UCAF) data. For Apple Pay, this field is available (but optional) only for merchant decryption of Mastercard transactions on `FDC Compass` and `Platform Connect` processors.

[consumerAuthenticationInformation.ucafCollectionIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-ucaf-collect-indicator.md "")

consumerAuthenticationInformation.ucafCollectionIndicator
:
Universal cardholder authentication field (UCAF) collection indicator used for Mastercard Identity Check. For Apple Pay, this field is available and required only for merchant decryption of Mastercard transactions on the `Platform Connect` processor.
:
Set the value to `2`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.tokenizedCard.cryptogram](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:
Token authentication verification value cryptogram.
:
The value for this field must be a 28-character, Base64-encoded string (the encoding method for Apple Pay transactions).

[paymentInformation.tokenizedCard.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:
Set the value to month in which the token expires. Format: `MM`  
Possible values: `01` through `12`.

[paymentInformation.tokenizedCard.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:
Set the value to the year in which the token expires. Format: `yyyy`.

[paymentInformation.tokenizedCard.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:
Set the value to customer's payment network token value that contains the customer's credit card number.

[paymentInformation.tokenizedCard.transactionType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:
For `Elavon Americas`, `FDC Compass`, `Platform Connect`, and `GPX` processors, set this field to the value that indicates the type of transaction that provided the payment network token data. Possible values:

    * `1`: In-app transaction.
    * `2`: Near-field communication (NFC) transaction. The customer's mobile device provided the token data for a contactless EMV transaction.
    * `3`: A transaction using stored customer credentials on `Platform Connect`, whether for merchant-initiated transactions (MITs) or customer-initiated transactions (CITs).

:
> IMPORTANT This value does not specify the token service provider. It specifies the entity that provided you with information about the token.

[paymentInformation.tokenizedCard.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:
Three-digit value that indicates the card type. Possible values:

    * `001`: Relay (excluding mada co-badged cards issued in the Kingdom of Saudi Arabia.)
    * `002`: Mastercard (excluding mada co-badged cards issued in the Kingdom of Saudi Arabia)
    * `003`: American Express
    * `004`: Discover
    * `007`: JCB
    * `060`: mada debit cards and prepaid cards issued in the Kingdom of Saudi Arabia (including mada co-badged Mastercard and Relay cards)

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Type of transaction. Some payment card companies use this information when determining discount rates. Possible values:

    * `aesk`: American Express SafeKey authentication.
    * `dipb`: Discover card type.
    * `internet`: Default value for authorizations. E-commerce order placed from a website.
    * `js`: JCB J/Secure authentication.
    * `mada`: mada authentication.
    * `spa`: Mastercard Identity Check authentication. When the transaction type field is set to this value, you must also include the consumerAuthenticationInformation. ucafCollectionIndicator field with the value set to `2`.
    * `vbv`: Relay Secure authentication

:
For a transaction on a mada co-badged Mastercard, set the value to `mada` or `spa`.
:
For a transaction on a mada co-badged Relay card, set the value to `mada` or `vbv`

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

REST Example: Authorize an American Express Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-amex}
=========================================================================================================================

American Express Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "aesk",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "37828224631XXX5",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "003"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "003"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "003"
    },
    "card": {
      "type": "003"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

REST Example: Authorize a Discover Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-discover}
====================================================================================================================

Discover Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "dipb",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "6X11111111111117",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "004"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "004"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "004"
    },
    "card": {
      "type": "004"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

REST Example: Authorize a JCB Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-jcb}
==========================================================================================================

JCB Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "js",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "3566xxxxxxxxxxx3",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "007"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "007"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "007"
    },
    "card": {
      "type": "007"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

REST Example: Authorize a mada Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-mada}
============================================================================================================

Apple Pay supports mada Pay mobile app transactions with `Platform Connect` only and only for these payment cards issued in the Kingdom of Saudi Arabia:

* mada
* Mastercard co-badged with mada
* Relay co-badged with mada  
  To authorize an Apple Pay payment with the mada Pay mobile app---whether for a mada card or for a mada co-badged Mastercard or Relay card---specify the mada card type (value `060`) in the paymentInformation.tokenizedCard.type REST API field. For more information, see Co-Badged Cards in the Payments Developer Guide for `Platform Connect`.  
  mada Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "mada",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "5X696819161XX419",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "060"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "SAR"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "Al Dariyah Dist",
      "locality": "Riyadh",
      "administrativeArea": "01",
      "postalCode": "22028",
      "country": "SA",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
      "currency": "SAR"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "060"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "060"
    },
    "card": {
      "type": "060"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

REST Example: Authorize a Mastercard Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-mc}
================================================================================================================

Mastercard Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "spa",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "5555555555554444",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "002"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  },
  "consumerAuthenticationInformation": {
    "ucafAuthenticationData": "ABCDEFabcdefABCDEFabcdef0987654321234567",
    "ucafCollectionIndicator": "2"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "002"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "002"
    },
    "card": {
      "type": "002"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

REST Example: Authorize a Relay Payment with Merchant Decryption {#applepay-txn-auth-merch-ex-rest-code-relay}
============================================================================================================

Relay Auth Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "vbv",
    "paymentSolution": "001"
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "authReversal": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/reversals"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359621903916966603954"
    },
    "capture": {
      "method": "POST",
      "href": "/pts/v2/payments/7359621903916966603954/captures"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359621903916966603954",
  "orderInformation": {
    "amountDetails": {
      "authorizedAmount": "10.00",
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
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "918032",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303918032",
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
  "reconciliationId": "7359621903916966603954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:43:10Z"
}
```

Process an Apple Pay Sale with `Payment Gateway` Decryption {#applepay-txn-sale-pgw-ex}
====================================================================================

A sale bundles an authorization and capture in a single transaction. Request the authorization and capture at the same time. The authorization and capture amounts must be the same. The `REST` API message for a sale request is the same as the message for an authorization request, except that the sale request message must set the processingInformation.capture field to `true`.  
The topics in this section show to how to process an Apple Pay sale with the *`Payment Gateway` decryption* implementation of Apple Pay:

* Basic Steps: Processing a Sale with `Payment Gateway` Decryption
* Fields Required to Process a Sale with `Payment Gateway` Decryption
* REST Example: Process a Sale with `Payment Gateway` Decryption
  For general information about sale transactions, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Processing a Sale with `Payment Gateway` Decryption {#applepay-txn-sale-pgw-ex-rest-steps}
====================================================================================================

1. Follow these steps to process an Apple Pay sale transaction with `Payment Gateway` decryption:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Process a Sale with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-pgw-ex/applepay-txn-sale-pgw-ex-rest-fields.md "").
   * Refer to the example in [REST Example: Process a Sale with Payment Gateway Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-pgw-ex/applepay-txn-sale-pgw-ex-rest-code.md "").
3. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Process a Sale with `Payment Gateway` Decryption {#applepay-txn-sale-pgw-ex-rest-fields}
========================================================================================================

As a best practice, include these REST API fields in your request for a combined authorization and capture (sale) transaction with the `Payment Gateway` decryption implementation of Apple Pay.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.fluidData.descriptor](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-descriptor.md "")
:
Format of the encrypted payment data.
:
Set the value to `RklEPUNPTU1PTi5BUFBMRS5JTkFQUC5QQVlNRU5U` for Apple Pay.

[paymentInformation.fluidData.encoding](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-encoding.md "")
:
Encoding method used to encrypt the payment data.
:
Set the value to `Base64` for Apple Pay.

[paymentInformation.fluidData.value](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-value.md "")
:
Set the value to the encrypted payment data value returned by the Full Wallet request.

[processingInformation.capture](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true` for a sale transaction (to include a capture with the authorization).

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

REST Example: Process a Sale with `Payment Gateway` Decryption {#applepay-txn-sale-pgw-ex-rest-code}
=================================================================================================

Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "paymentSolution": "001",
    "capture": true
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  },
  "paymentInformation": {
    "fluidData": {
      "value": "eyJkYXRhIjoiXC9NK2VQQ0JlMmtod1pMQkFzRWhneHFqYXF2MmtZNDJSNnd1VDdnT3JlelBwRE9hR2dmc1AzZUNHZUplSjFSc3JpSERGSnJIK0FJVHp6RFdjVXNHUlNuSER3QlBcL2JHakU0dUhYcTFDOXFjWDBLWmYzaTFZNkV2b1wvaXExOFhkcG5obTI1U2kwSGpkWUJGRmVBUmZlVENpMEtDSGtRN04wZTAyeElRbm84Qmt1TVwvSUQ5bHdoNXBFVnVYM08ybjc4bHVyU0tlRmpXVHMyWG9Pc1pmWXBpbFQ4ZFFtK2RaYmh6VHgyZ2hMXC9FcFBReUVvdW5QTFZjTlwvaTR0blFnakxWRWJiNUFDNHJ4ZjBwK2M0VGtYSzcycGZGY05NSnlxd0RlQWZ2cHB6cnFQZVdoaWlpdzUwTmljT3duR29tcXA0bWU2anV4S2N5ZFh3cGpJR3BhQlBuXC9NY3o2d2ZDSFAzMWY1NHdkRmZ4bEZadjl5XC85aGw5YlY1d08yN2R5bFwvYUVxN2FYbU5JZHBQNTFsOXlSQlUzNDNYcjR3XC9MSXN2ZmZTTE91WDlsRU5QUGtocE1LUXo4VWpYNG0xXC9xazdcL256aGFSekFaZGh6VGZsNkZ3PT0iLCJ2ZXJzaW9uIjoiRUNfdjEiLCJoZWFkZXIiOnsiYXBwbGljYXRpb25EYXRhIjoiNDE3MDcwNkM2OTYzNjE3NDY5NkY2RTQ0NjE3NDYxIiwidHJhbnNhY3Rpb25JZCI6IjU0NzI2MTZFNzM2MTYzNzQ2OTZGNkU0OTQ0IiwiZXBoZW1lcmFsUHVibGljS2V5IjoiTUlJQlN6Q0NBUU1HQnlxR1NNNDlBZ0V3Z2ZjQ0FRRXdMQVlIS29aSXpqMEJBUUloQVBcL1wvXC9cLzhBQUFBQkFBQUFBQUFBQUFBQUFBQUFcL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL01Gc0VJUFwvXC9cL1wvOEFBQUFCQUFBQUFBQUFBQUFBQUFBQVwvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cLzhCQ0JheGpYWXFqcVQ1N1BydlZWMm1JYThaUjBHc014VHNQWTd6ancrSjlKZ1N3TVZBTVNkTmdpRzV3U1RhbVo0NFJPZEpyZUJuMzZRQkVFRWF4ZlI4dUVzUWtmNHZPYmxZNlJBOG5jRGZZRXQ2ek9nOUtFNVJkaVl3cFpQNDBMaVwvaHBcL200N242MHA4RDU0V0s4NHpWMnN4WHM3THRrQm9ONzlSOVFJaEFQXC9cL1wvXC84QUFBQUFcL1wvXC9cL1wvXC9cL1wvXC9cLys4NXZxdHB4ZWVoUE81eXNMOFl5VlJBZ0VCQTBJQUJPSnZpNkxGa0JpUTJINDR6K05VK0I3N1hZV2p4UHJQaXRDMFRWZytJYnNGeXIrNjFsemFkQjFrU25hUHpFTmVMMEVrbzhWTExzVjRhU1hTalwvZXlJRmc9IiwicHVibGljS2V5SGFzaCI6IlwvNkxQT3BoS0tydWFvdjBET3VOTDk1YXFCcFVcLzArNElXNXFhV3FxME5qRT0ifSwic2lnbmF0dXJlIjoiTUlJRFFnWUpLb1pJaHZjTkFRY0NvSUlETXpDQ0F5OENBUUV4Q3pBSkJnVXJEZ01DR2dVQU1Bc0dDU3FHU0liM0RRRUhBYUNDQWlzd2dnSW5NSUlCbEtBREFnRUNBaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUF3SnpFbE1DTUdBMVVFQXg0Y0FHTUFhQUJ0QUdFQWFRQkFBSFlBYVFCekFHRUFMZ0JqQUc4QWJUQWVGdzB4TkRBeE1ERXdOakF3TURCYUZ3MHlOREF4TURFd05qQXdNREJhTUNjeEpUQWpCZ05WQkFNZUhBQmpBR2dBYlFCaEFHa0FRQUIyQUdrQWN3QmhBQzRBWXdCdkFHMHdnWjh3RFFZSktvWklodmNOQVFFQkJRQURnWTBBTUlHSkFvR0JBTkM4K2tndGdtdldGMU96amdETnJqVEVCUnVvXC81TUt2bE0xNDZwQWY3R3g0MWJsRTl3NGZJWEpBRDdGZk83UUtqSVhZTnQzOXJMeXk3eER3YlwvNUlrWk02MFRaMmlJMXBqNTVVYzhmZDRmek9wazNmdFphUUdYTkxZcHRHMWQ5VjdJUzgyT3VwOU1NbzFCUFZyWFRQSE5jc005OUVQVW5QcWRiZUdjODdtMHJBZ01CQUFHalhEQmFNRmdHQTFVZEFRUlJNRStBRUhaV1ByV3RKZDdZWjQzMWhDZzdZRlNoS1RBbk1TVXdJd1lEVlFRREhod0FZd0JvQUcwQVlRQnBBRUFBZGdCcEFITUFZUUF1QUdNQWJ3QnRnaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUFEZ1lFQWJVS1lDa3VJS1M5UVEybUZjTVlSRUltMmwrWGc4XC9KWHYrR0JWUUprT0tvc2NZNGlOREZBXC9iUWxvZ2Y5TExVODRUSHdOUm5zdlYzUHJ2N1JUWTgxZ3EwZHRDOHpZY0FhQWtDSElJM3lxTW5KNEFPdTZFT1c5a0prMjMyZ1NFN1dsQ3RIYmZMU0tmdVNnUVg4S1hRWXVaTGsyUnI2M044QXBYc1h3QkwzY0oweGdlQXdnZDBDQVFFd096QW5NU1V3SXdZRFZRUURIaHdBWXdCb0FHMEFZUUJwQUVBQWRnQnBBSE1BWVFBdUFHTUFid0J0QWhCY2wrUGYzK1U0cGsxM25WRDlud1FRTUFrR0JTc09Bd0lhQlFBd0RRWUpLb1pJaHZjTkFRRUJCUUFFZ1lDZ2RvN2lrTzdERTNCXC9pY0lycmRjc1ZIanJyQmNPdXNndXhlcGs1QW41ZEExV01rajBlVjRsMVM0RnR5NktwdlR0T0xcL3VSdDhuTHZpVnR0TVVSZHBYTjNWXC9NVmZnVkxlXC9YUm5cLzRzbUJnMVgweE5OTXlTZXBQalVxV1ZkWFg1K0RWYnp2U0ZKSVJGdmt1MHJPaGg3REZmODVpbXNkaGRZRUhCaUg0TzdpK1E9PSJ9",
      "descriptor": "RklEPUNPTU1PTi5BUFBMRS5JTkFQUC5QQVlNRU5U",
      "encoding": "Base64"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359641336126184303955/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359641336126184303955"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "consumerAuthenticationInformation": {
    "token": "Axj//wSTjveKcificy1TABsQ3ZtGThq1Zp78eHSPSAp78eHSPTpAr6E4uGTSTL0YriJFQwJycd7xTkT8TmWqYAAAtQlD"
  },
  "id": "7359641336126184303955",
  "issuerInformation": {
    "responseRaw": "0110322000000E1000020000000000000010000104041534840127353442435634463759474B373833313030303030000159008000223134573031363135303730333830323039344730363400103232415050524F56414C00065649435243200034544B54523031313132313231323132313231544C3030323636504E30303431313131"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
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
      "expirationYear": "2025",
      "requestorId": "12121212121",
      "prefix": "411111",
      "assuranceLevel": "66",
      "expirationMonth": "07",
      "suffix": "1111",
      "type": "001"
    },
    "card": {
      "suffix": "1111",
      "type": "001"
    }
  },
  "pointOfSaleInformation": {
    "terminalId": "02495701"
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "merchantNumber": "000372839590885",
    "approvalCode": "831000",
    "networkTransactionId": "016150703802094",
    "transactionId": "016150703802094",
    "responseCode": "00",
    "avs": {
      "code": "Y",
      "codeRaw": "Y"
    }
  },
  "reconciliationId": "73428553",
  "riskInformation": {
    "earlyVelocity": {
      "counts": [
        {
          "count": "1",
          "informationCode": "MVEL-R1"
        }
      ]
    }
  },
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T04:15:34Z"
}
```

Process an Apple Pay Sale with Merchant Decryption {#applepay-txn-sale-merch-ex}
================================================================================

A sale bundles an authorization and capture in a single transaction. Request the authorization and capture at the same time. The authorization and capture amounts must be the same. The `REST` API message for a sale request is the same as the message for an authorization request, except that the sale request message must set the processingInformation.capture field to `true`.  
The topics in this section show to how to process an Apple Pay sale with the *merchant decryption* implementation of Apple Pay:

* Basic Steps: Processing a Sale with Merchant Decryption
* Fields Required to Process a Sale with Merchant Decryption
* REST Example: Process an American Express Sale
* REST Example: Process a Discover Sale
* REST Example: Process a JCB Sale
* REST Example: Processe a mada Sale
* REST Example: Process a Mastercard Sale
* REST Example: Process a Relay Sale

> IMPORTANT
> Support for cards varies by partner and processor. For a list of processors and cards supported with Apple Pay, see [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").
> For general information about sale transactions, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Processing a Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-steps}
================================================================================================

1. Follow these steps to process an Apple Pay sale transaction with merchant decryption:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Process a Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-fields.md "").

   * Refer to the example for your payment card type:

     * [REST Example: Process an American Express Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-amex.md "")
     * [REST Example: Process a Discover Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-discover.md "")
     * [REST Example: Process a JCB Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-jcb.md "")
     * [REST Example: Process a mada Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-mada.md "")
     * [REST Example: Process a Mastercard Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-mc.md "")
     * [REST Example: Process a Relay Sale with Merchant Decryption](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-sale-merch-ex/applepay-txn-sale-merch-ex-rest-code-relay.md "")

     > IMPORTANT In these code examples, any test card numbers that contain zeroes are formatted with Xs replacing the zeroes. When you test using one of these reformatted card numbers, replace each X with a 0 (zero).

3. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Process a Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-fields}
====================================================================================================

As a best practice, include these REST API fields in your request for a combined authorization and capture (sale) transaction with the `Payment Gateway` decryption implementation of Apple Pay.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.ucafAuthenticationData](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-ucaf-auth-data.md "")
:
Universal cardholder authentication field (UCAF) data. For Apple Pay, this field is available (but optional) only for merchant decryption of Mastercard transactions on `FDC Compass` and `Platform Connect` processors.

[consumerAuthenticationInformation.ucafCollectionIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-ucaf-collect-indicator.md "")

consumerAuthenticationInformation.ucafCollectionIndicator
:
Universal cardholder authentication field (UCAF) collection indicator used for Mastercard Identity Check. For Apple Pay, this field is available and required only for merchant decryption of Mastercard transactions on the `Platform Connect` processor.
:
Set the value to `2`.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.tokenizedCard.cryptogram](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:
Token authentication verification value cryptogram.
:
The value for this field must be a 28-character, Base64-encoded string (the encoding method for Apple Pay transactions).

[paymentInformation.tokenizedCard.expirationMonth](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:
Set the value to month in which the token expires. Format: `MM`  
Possible values: `01` through `12`.

[paymentInformation.tokenizedCard.expirationYear](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:
Set the value to the year in which the token expires. Format: `yyyy`.

[paymentInformation.tokenizedCard.number](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:
Set the value to customer's payment network token value that contains the customer's credit card number.

[paymentInformation.tokenizedCard.transactionType](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:
For `Elavon Americas`, `FDC Compass`, `Platform Connect`, and `GPX` processors, set this field to the value that indicates the type of transaction that provided the payment network token data. Possible values:

    * `1`: In-app transaction.
    * `2`: Near-field communication (NFC) transaction. The customer's mobile device provided the token data for a contactless EMV transaction.
    * `3`: A transaction using stored customer credentials on `Platform Connect`, whether for merchant-initiated transactions (MITs) or customer-initiated transactions (CITs).

:
> IMPORTANT This value does not specify the token service provider. It specifies the entity that provided you with information about the token.

[paymentInformation.tokenizedCard.type](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:
Three-digit value that indicates the card type. Possible values:

    * `001`: Relay (excluding mada co-badged cards issued in the Kingdom of Saudi Arabia)
    * `002`: Mastercard (excluding mada co-badged cards issued in the Kingdom of Saudi Arabia)
    * `003`: American Express
    * `004`: Discover
    * `007`: JCB
    * `060`: mada debit cards and prepaid cards issued in the Kingdom of Saudi Arabia (including mada co-badged Mastercard and Relay cards)

[processingInformation.capture](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-a.md "")
:
Set the value to `true` to include a capture with the authorization.

[processingInformation.commerceIndicator](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Type of transaction. Some payment card companies use this information when determining discount rates. Possible values:

    * `aesk`: American Express SafeKey authentication.
    * `dipb`: Discover card type.
    * `internet`: Default value for authorizations. E-commerce order placed from a website.
    * `js`: JCB J/Secure authentication.
    * `mada`: mada authentication.
    * `spa`: Mastercard Identity Check authentication. When the transaction type field is set to this value, you must also include the consumerAuthenticationInformation. ucafCollectionIndicator field with the value set to `2`.
    * `vbv`: Relay Secure authentication

:
For a transaction on a mada co-badged Mastercard, set the value to `mada` or `spa`.
:
For a transaction on a mada co-badged Relay card, set the value to `mada` or `vbv`

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

REST Example: Process an American Express Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-amex}
====================================================================================================================

American Express Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "aesk",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "37828224631XXX5",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "003"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "003"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "003"
    },
    "card": {
      "type": "003"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

REST Example: Process a Discover Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-discover}
===============================================================================================================

Discover Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "dipb",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "6X11111111111117",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "004"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "004"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "004"
    },
    "card": {
      "type": "004"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

REST Example: Process a JCB Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-jcb}
=====================================================================================================

JCB Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "js",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "3566xxxxxxxxxxx3",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "007"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "007"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "007"
    },
    "card": {
      "type": "007"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

REST Example: Process a mada Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-mada}
=======================================================================================================

Apple Pay supports mada Pay mobile app transactions with `Platform Connect` only and only for these payment cards issued in the Kingdom of Saudi Arabia:

* mada
* Mastercard co-badged with mada
* Relay co-badged with mada  
  To process an Apple Pay sale on the mada Pay mobile app---whether for a mada card or for a mada co-badged Mastercard or Relay card---specify the mada card type (value `060`) in the paymentInformation.tokenizedCard.type REST API field. For more information, see Co-Badged Cards in the Payments Developer Guide for `Platform Connect`.  
  mada Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "mada",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "5X696819161XX419",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "060"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "SAR"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "Al Dariyah Dist",
      "locality": "Riyadh",
      "administrativeArea": "01",
      "postalCode": "22028",
      "country": "SA",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
      "currency": "SAR"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "060"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "060"
    },
    "card": {
      "type": "060"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

REST Example: Process a Mastercard Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-mc}
===========================================================================================================

Mastercard Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "spa",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "5555555555554444",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "002"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  },
  "consumerAuthenticationInformation": {
    "ucafAuthenticationData": "ABCDEFabcdefABCDEFabcdef0987654321234567",
    "ucafCollectionIndicator": "2"
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
      "currency": "USD"
    }
  },
  "paymentAccountInformation": {
    "card": {
      "type": "002"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "002"
    },
    "card": {
      "type": "002"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

REST Example: Process a Relay Sale with Merchant Decryption {#applepay-txn-sale-merch-ex-rest-code-relay}
=======================================================================================================

Relay Sale Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "commerceIndicator": "vbv",
    "paymentSolution": "001",
    "capture": true
  },
  "paymentInformation": {
    "tokenizedCard": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cryptogram": "AceY+igABPs3jdwNaDg3MAACAAA=",
      "transactionType": "1",
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "901 Metro Center Blvd",
      "locality": "Foster City",
      "administrativeArea": "CA",
      "postalCode": "94404",
      "country": "US",
      "email": "test@pgw.com"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/payments/7359627932726161403954/voids"
    },
    "self": {
      "method": "GET",
      "href": "/pts/v2/payments/7359627932726161403954"
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "7359627932726161403954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "authorizedAmount": "10.00",
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
      "expirationYear": "2031",
      "prefix": "411111",
      "expirationMonth": "12",
      "suffix": "1111",
      "type": "001"
    },
    "card": {
      "type": "001"
    }
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "processorInformation": {
    "systemTraceAuditNumber": "417802",
    "approvalCode": "831000",
    "merchantAdvice": {
      "code": "01",
      "codeRaw": "M001"
    },
    "responseDetails": "ABC",
    "networkTransactionId": "016153570198200",
    "retrievalReferenceNumber": "500303417802",
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
  "reconciliationId": "7359627932726161403954",
  "status": "AUTHORIZED",
  "submitTimeUtc": "2025-01-04T03:53:13Z"
}
```

Reverse an Apple Pay Payment Authorization {#applepay-txn-reversal-ex}
======================================================================

The topics in this section show to how to reverse an Apple Pay payment authorization:

* Basic Steps: Reversing a Payment Authorization
* Fields Required to Reverse a Payment Authorization
* REST Example: Reverse a Payment Authorization
  For general information about authorization reversals, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Reversing a Payment Authorization {#applepay-txn-reversal-ex-rest-steps}
=====================================================================================

1. Follow these steps to reverse an Apple Pay payment authorization:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Reverse a Payment Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-reversal-ex/applepay-txn-reversal-ex-rest-fields.md "").
   * Refer to the example in [REST Example: Reverse a Payment Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-reversal-ex/applepay-txn-reversal-ex-rest-code.md "").
3. Send the request to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments/{id}/reversals`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments/{id}/reversals`

   #### ADDITIONAL INFORMATION

   Replace the `{id}` portion of the URL with the transaction ID of the payment that you want to reverse. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the authorization request. Example value: 7359642011156554503954

4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Reverse a Payment Authorization {#applepay-txn-reversal-ex-rest-fields}
==========================================================================================

As a best practice, include these REST API fields in your request to reverse the authorization of an Apple Pay transaction.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set this field to the value returned in the response to the original authorization.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

[reversalInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/reversal-info-aa/reversal-info-amount-details-total-amount.md "")
:

REST Example: Reverse a Payment Authorization {#applepay-txn-reversal-ex-rest-code}
===================================================================================

Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    }
  },
  "reversalInformation": {
    "amountDetails": {
      "totalAmount": "10"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/captures/6662994431376681303954/voids"
    },
    "self": {
      "method": "GET",
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "6662994431376681303954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "currency": "USD"
    }
  },
  "reconciliationId": "66535942B9CGT52U",
  "status": "PENDING",
  "submitTimeUtc": "2025-01-04T23:56:13Z"
}
```

Capture an Apple Pay Authorization {#applepay-txn-capture-ex}
=============================================================

The topics in this section show to how to capture an authorized Apple Pay payment transaction:

* Basic Steps: Capturing an Authorization
* Fields Required to Capture an Authorization
* REST Example: Capturing an Authorization
  For general information about capture transactions, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps: Capturing an Authorization {#applepay-txn-capture-ex-rest-steps}
=============================================================================

1. Follow these steps to capture an authorized Apple Pay payment transaction:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Fields Required to Capture an Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-capture-ex/applepay-txn-capture-ex-rest-fields.md "").
   * Refer to the example in [REST Example: Capturing an Authorization](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-txn-capture-ex/applepay-txn-capture-ex-rest-code.md "").
3. Send the request to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments/{id}/captures`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments/{id}/captures`

   #### ADDITIONAL INFORMATION

   Replace the `{id}` portion of the URL with the transaction ID of the payment that you want to capture. The transaction ID is returned in the [id](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/id.md "") field of the response to the authorization request. Example value: 7359642011156554503954

4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Fields Required to Capture an Authorization {#applepay-txn-capture-ex-rest-fields}
==================================================================================

As a best practice, include these REST API fields in your request to capture an authorized Apple Pay payment transaction.  
Depending on your processor, your geographic location, and whether the relaxed address verification system (RAVS) is enabled for your account, some of these fields might not be required. It is your responsibility to determine whether an API field can be omitted from the transaction you are requesting. For information about the relaxed requirements for address data and expiration dates in payment transactions, see the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

[clientReferenceInformation.code](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:
Set this field to the value returned in the response to the original authorization.

[orderInformation.amountDetails.currency](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[processingInformation.paymentSolution](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-payment-solution.md "")
:
Set the value to `001` to identify Apple Pay as the digital payment solution.

REST Example: Capturing an Authorization {#applepay-txn-capture-ex-rest-code}
=============================================================================

Request

```
{ 
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "processingInformation": {
    "paymentSolution": "001"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10",
      "currency": "USD"
    }
  }
}
```

Response to a Successful Request

```
{
  "_links": {
    "void": {
      "method": "POST",
      "href": "/pts/v2/captures/6662994431376681303954/voids"
    },
    "self": {
      "method": "GET",
    }
  },
  "clientReferenceInformation": {
    "code": "TC_1231223"
  },
  "id": "6662994431376681303954",
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "10.00",
      "currency": "USD"
    }
  },
  "reconciliationId": "66535942B9CGT52U",
  "status": "PENDING",
  "submitTimeUtc": "2024-11-21T04:17:20Z"
}
```

Authorizing Apple Pay Digital Wallet Payments (with `Elavon`) {#applepay-payment-auth-digital-wallet}
=====================================================================================================

`Elavon` supports Apple Pay digital wallet transactions. An Apple Pay digital wallet uses *tokenization* to prevent sensitive card data from being exposed or intercepted during transactions. A token is generated when a user adds a supported card to their Apple Pay digital wallet.  
`Elavon` supports 3-D Secure 2.2 with Diners Club, Mastercard, and Relay card transactions.

> IMPORTANT
> ` Elavon ` does not support the 3-D Secure 2.2 protocol if it is used with *network tokens* or *digital payment* . ` Payment Gateway ` will decline any transaction processed by ` Elavon ` that uses both 3-D Secure 2.2 and either network tokens or digital payments.  
> This section shows you how to request authorization of a Apple Pay digital wallet payment:

* [Authorizing an Apple Pay Digital Wallet Payment without 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-no-3ds.md "")
* [Authorizing an Apple Pay Digital Wallet Payment with 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-with-3ds.md "")

Authorizing an Apple Pay Digital Wallet Payment without 3-D Secure {#applepay-auth-dw-no-3ds}
=============================================================================================

The topics in this section show to how to authorize an Apple Pay digital wallet payment without 3-D Secure authentication:

* Basic steps
* Required fields
* Mastercard example
* Common error responses and resolutions  
  When 3-D Secure is not used, the transaction ID is automatically populated with the cryptogram value
  For general information about basic authorizations, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps to Authorize an Apple Pay Digital Wallet Payment without 3-D Secure {#applepay-auth-dw-no-3ds-rest-steps}
=====================================================================================================================

1. Follow these steps to request an Apple Pay payment on a supported card without 3-D Secure authentication:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Required Fields to Authorize an Apple Pay Digital Wallet Payment without 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-no-3ds/applepay-auth-dw-no-3ds-rest-fields.md "").  
     These REST API fields are specific to this request payload:
     * merchantInformation.merchantDomain
     * paymentInformation.tokenizedCard.cryptogram
     * paymentInformation.tokenizedCard.transactionType
     * processingInformation.commerceIndicator
     * processingInformation.paymentSolution
   * Refer to the example [Diners Club Example: Authorize an Apple Pay Digital Wallet Payment without 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-no-3ds/applepay-auth-dw-no-3ds-rest-code-diners.md ""). IMPORTANT

     > The example is based on a Diners Club transaction. For a Mastercard or a Relay card transaction, set the card-specific value for the paymentInformation.tokenizedCard.type field.

3. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

   A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

5. If the response message contain errors, see [Common Error Responses for Transactions without 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-no-3ds/applepay-auth-dw-no-3ds-errors.md "").

Required Fields to Authorize an Apple Pay Digital Wallet Payment without 3-D Secure {#applepay-auth-dw-no-3ds-rest-fields}
==========================================================================================================================

These REST API fields are required to request authorization of an Apple Pay Digital Wallet payment without 3-D Secure authentication.

clientReferenceInformation.code
:

merchantInformation.merchantId
:

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.totalAmount
:

orderInformation.billTo.address1
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.country
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

paymentInformation.tokenizedCard.cryptogram
:
Set the value to the network token cryptogram from Apple Pay.

paymentInformation.tokenizedCard.expirationMonth
:

paymentInformation.tokenizedCard.expirationYear
:

paymentInformation.tokenizedCard.transactionType
:
Set the value to `1` for network tokens.

paymentInformation.tokenizedCard.type
:
Set the value to the card type code. Possible values:

    * `001` for Relay
    * `002` for Mastercard
    * `005` for Diners Club

processingInformation.commerceIndicator
:
Set the value to `internet` for a Diners Club, Discover, and Relay card for an authorization request without 3-D Secure authentication.

processingInformation.paymentSolution
:
Set the value to `001` for Apple Pay in-app and web transactions.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")

Diners Club Example: Authorize an Apple Pay Digital Wallet Payment without 3-D Secure {#applepay-auth-dw-no-3ds-relay}
=====================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "DINERS-NO3DS-APPLEPAY-002"
  }, 
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "89.99",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "Maria",
      "lastName": "Garcia",
      "address1": "123 Main Street",
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "maria.garcia@example.com",
      "phoneNumber": "415-555-0123"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "cryptogram": "BgAAAAAABk4DWZ4C28yUQAAAAAA=",
      "transactionType": "1",
      "expirationMonth": "11",
      "expirationYear": "2026",
      "type": "005"
    }
  },
  "processingInformation": {
    "paymentSolution": "001",
    "commerceIndicator": "internet"
  },
  "merchantInformation": {
    "merchantId": "demo_merchant_12345"
  }
}
```

Common Error Responses for Transactions without 3-D Secure {#applepay-auth-dw-no-3ds-errors}
============================================================================================

This topic lists common error responses to transaction requests without 3-D Secure authentication.

3DS ECI provided for non-3DS transaction
:
Cause: Invalid e-commerce indicator for a transaction that does not use 3-D Secure.
:
Resolution: Make sure the processingInformation.commerceIndicator field is set to `internet` to indicate a transaction without 3-D Secure authentication. You could also omit the field from your request and let the gateway assign the value.

Authentication data present in non-3DS transaction
:
Cause: Conflicting authentication data.
:
Resolution: Remove the cardholder authentication data, which is used for transactions with 3-D Secure:

    * Remove the consumerAuthenticationInformation. cavv field (for Diners Club or Relay cards).
    * Remove the consumerAuthenticationInformation. ucafAuthenticationData field (for Mastercard only).

Digital wallet transaction missing required cryptogram
:
Cause: Missing or invalid cryptogram.
:
Resolution: Make sure the paymentInformation.tokenizedCard.cryptogram field is populated with the correct value.

Authorizing an Apple Pay Digital Wallet Payment with 3-D Secure {#applepay-auth-dw-with-3ds}
============================================================================================

The topics in this section show to how to authorize an Apple Pay digital wallet payment with 3-D Secure authentication:

* Basic steps
* Required fields
* Diners Club example
  For general information about basic authorizations, see the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Basic Steps to Authorize an Apple Pay Digital Wallet Payments with 3-D Secure {#applepay-auth-ex-with-3ds-rest-steps}
=====================================================================================================================

1. Follow these steps to authorize an Apple Pay payment on Mastercard with 3-D Secure authentication:

2. Create the request message with the required `REST` API fields.

   * Use the API fields listed in [Required Fields to Authorize an Apple Pay Digital Wallet Payment with 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-with-3ds/applepay-auth-dw-with-3ds-rest-fields.md "").  
     These REST API fields are specific to this payload:
     * merchantInformation.merchantDomain
     * consumerAuthenticationInformation.cavv---Diners Club and Relay only
     * consumerAuthenticationInformation.ucafAuthenticationData---Mastercard only
     * consumerAuthenticationInformation.ucafCollectionIndicator---Mastercard only
     * paymentInformation.tokenizedCard.cryptogram
     * paymentInformation.tokenizedCard.transactionType
     * paymentInformation.tokenizedCard.type
     * processingInformation.commerceIndicator
     * processingInformation.paymentSolution
     * processingInformation.paymentNetworkTokenTransactionType
   * Refer to the example [Relay Card Example: Authorize an Apple Pay Digital Wallet Payment with 3-D Secure](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet/applepay-auth-dw-with-3ds/applepay-auth-dw-with-3ds-rest-code-relay.md ""). IMPORTANT

     > The example is based on a Relay card transaction. Set these fields to the appropriate values based on the card type:
     > * paymentInformation.tokenizedCard.type
     > * processingInformation.commerceIndicator

3. Send the message to one of these endpoints:

   * Production: `POST ``https://api.example.com``/pts/v2/payments`
   * Test: `POST ``https://apitest.example.com``/pts/v2/payments`
4. Verify the response messages to make sure that the request was successful.

   #### ADDITIONAL INFORMATION

A 200-level HTTP response code indicates success. See the [Transaction Response Codes](https://developer.example.com/api/reference/response-codes.md "").

Required Fields to Authorize an Apple Pay Digital Wallet Payment with 3-D Secure {#applepay-auth-dw-with-3ds-rest-fields}
=========================================================================================================================

These REST API fields are required to request authorization of an Apple Pay digital wallet payment with 3-D Secure authentication.

clientReferenceInformation.code
:

consumerAuthenticationInformation.cavv
:
For Diners Club and Relay cards only---Set this value to the universal cardholder authentication number to indicate 3-D Secure authentication.

consumerAuthenticationInformation.directoryServerTransactionId
:

consumerAuthenticationInformation.paSpecificationVersion
:

consumerAuthenticationInformation.ucafAuthenticationData
:
For Mastercard transactions only---Set this value to the universal cardholder authentication field (UCAF) data to indicate 3-D Secure authentication.

consumerAuthenticationInformation.ucafCollectionIndicator
:
For Mastercard transactions only---Set the value of this field to `2`. UCAF collection is supported on your website and the UCAF was populated. This value indicates a successful Mastercard Identity Check transaction.

merchantInformation.merchantId
:

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.totalAmount
:

orderInformation.billTo.address1
:

orderInformation.billTo.country
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

paymentInformation.tokenizedCard.cryptogram
:
Set the value to the network token cryptogram from Apple Pay.

paymentInformation.tokenizedCard.expirationMonth
:

paymentInformation.tokenizedCard.expirationYear
:

paymentInformation.tokenizedCard.transactionType
:
Set the value to `1`.

paymentInformation.tokenizedCard.type
:
Set the value to the card type code. Possible values:

    * `001` for Relay
    * `002` for Mastercard
    * `005` for Diners Club

processingInformation.commerceIndicator
:
Set the value to the code for the 3-D Secure authentication service. Possible values:

    * `pb` for 3-D Secure authentication by Diners Club ProtectBuy
    * `spa` for 3-D Secure authentication by Mastercard Identity Check
    * `vbv` for 3-D Secure authentication by Relay Secure

processingInformation.paymentSolution
:
Set the value to `001` for Apple Pay in-app and web transactions.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/acq-info.md "")

Relay Card Example: Authorize an Apple Pay Digital Wallet Payment with 3-D Secure {#applepay-auth-dw-with-3ds-rest-code-mc}
==========================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "CARD-3DS-APPLEPAY-006"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "199.00",
      "currency": "EUR"
    },
    "billTo": {
      "firstName": "Pierre",
      "lastName": "Dubois",
      "address1": "15 Rue de la Paix",
      "locality": "Paris",
      "postalCode": "75001",
      "country": "FR",
      "email": "pierre.dubois@example.fr",
      "phoneNumber": "+33-1-42-96-12-34"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "cryptogram": "BwABBJQ0AgAAAAAgJDUCAAAAAAA=",
      "transactionType": "1",
      "expirationMonth": "08",
      "expirationYear": "2027",
      "type": "001"
    }
  },
  "consumerAuthenticationInformation": {
    "cavv": "BgABBJQ0AgAAAAAgJDUCAAAAAA=",
    "directoryServerTransactionId": "8a2+89r+vs8fsc8w+v+79y==",
    "paSpecificationVersion": "2.2.0"
  },
  "processingInformation": {
    "paymentSolution": "001",
    "commerceIndicator": "vbv"
  },
  "merchantInformation": {
    "merchantId": "demo_merchant_12345"
  }
}
```

Searching for Transactions {#applepay-search-for-txns}
======================================================

Use the Transaction page in the `Business Center` to search transactions that have been (successfully or unsuccessfully) processed on your account or for one or more of your merchants. The page consists of a Search pane and a Search Results pane.  
This section describes how to search *Apple Pay transactions* using the Search pane in the Transactions page. IMPORTANT

> For complete information about searching *all transactions* , see the Search for Transactions topics in the ` Business Center ` using the ` Payment Gateway ` Transaction Management module You must have login credentials to view the online help.

Related Information
-------------------

[Getting Started with Business Center Reports](https://developer.example.com/docs/gateway/en-us/reporting/user/all/ebc/reporting-ug/Get_Started_with_Business_Center_Reporting.md "")

Searching for Apple Pay Transactions {#billing-history-search}
==============================================================

Use the Transactions page in the `Business Center` to search for Apple Pay transactions.  
Follow these steps to search for Apple Pay transactions:

1. In the left navigation panel, click the Transaction Management icon and Transactions.
2. In the Transactions page, click Add Filter.
   1. In the New Filter drop-down box, select Payment Solution.

   2. In the Payment Solution drop-down box, select Digital Payment Method and then select Apple Pay.

      #### ADDITIONAL INFORMATION

      The Transactions page appears.

      #### Figure: {#billing-history-search_fig-search-txns}

      Transactions Page in the `Payment Gateway` `Business Center` ![Searching transactions using a saved search (AEM)](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/applepay-dev/images/ebc-applepay-search-criteria.png/jcr:content/renditions/original)

3. Click Search.
   1. Enter values into the search filters you want to apply to the list.
   2. To specify additional filters, click Add filter, select a filter in the list, and enter a value.
4. To download an invoice to a file, click the download icon for that invoice.
5. Click Search.

Reference Information {#applepay-reference}
===========================================

This section contains helpful information for integrating Apple Pay and for processing Apple Pay authorization transactions.

* [Quick Integration for the Payment Gateway Decryption Method](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-reference/applepay-ref-1-pgw-decrypt-quick.md "")
* [Endpoints for Services Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro/applepay-ref-2-endpoints-applepay-services.md "")
* [Optional Features Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-reference/applepay-ref-3-optional-features.md "")
* [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "")

Quick Integration for the `Payment Gateway` Decryption Method {#applepay-ref-1-pgw-decrypt-quick}
==============================================================================================

If you are integrating the **`Payment Gateway` decryption method** of Apple Pay and you are experienced in creating Apple Pay payment processing certificates, you can use these abbreviated instructions instead of the more detailed steps in [Integrating Apple Pay into Your System](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-cfg.md "").

1. Follow these steps to integrate the `Payment Gateway` decryption method of Apple Pay:

2. Enroll your organization in the Apple Developer Program and register a merchant ID for each environment, such as sandbox and production.

3. Log in to your `Payment Gateway` merchant account at the `Business Center`.

   #### ADDITIONAL INFORMATION

   Production: ` `<https://businesscenter.example.com>` `

   #### ADDITIONAL INFORMATION

   Production in India: [https://businesscenter.in.payment-gateway.in.com](https://businesscenter.in.example.com "")

   #### ADDITIONAL INFORMATION

   Test: ` `<https://businesscentertest.example.com/ebc2>` `

4. In the left navigation panel, select Payment Configuration and click Digital Payment Solution.

   #### ADDITIONAL INFORMATION

   The Digital Payments page appears. If you do not have the correct permissions enabled on your account, the Digital Payment Solution option does not appear on the left navigation panel.

5. Click Configure. The Apple Pay Registration page appears.

6. Enter your Apple merchant ID, and then click Generate New Certificate Signing Request.

7. To download the newly generated certificate signing request (CSR), click the Download icon next to the key and follow your browser's instructions to save and open the file.

8. Log into your Apple Developer account and use your CSR to create an Apple payment processing certificate that is associated with your merchant ID.

9. If you are validating your integration in your test environment, perform these tasks:

   1. Add test cards to your Apple sandbox tester account. For details, see [Requirements for End-to-End Testing](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-getting-started/applepay-getting-started-reqts-end-to-end-test.md "").
   2. Submit Apple Pay test transactions. For examples of Apple Pay transactions, see [Processing Apple Pay Transactions](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-txns-intro.md "").
   3. Adjust your integration settings as needed until your test transactions complete successfully.
10. If you are ready to integrate Apple Pay into your production environment, repeat Steps 2 through 7 with your `Payment Gateway` and Apple production accounts.

Optional Features Supported with Apple Pay {#applepay-ref-3-optional-features}
==============================================================================

These optional features are supported with Apple Pay. IMPORTANT

> Support for card types and optional features varies by partner and processor. For a list, see [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").

Merchant-Initiated Transactions
-------------------------------

Merchants can initiate a payment on the behalf of a customer. This type of transaction is called a merchant-initiated transaction (MIT). When initiating a MIT, the customer is not present. Customers must authorize the storage of their credentials and the use of these credentials for future payments.  
Merchant-initiated transactions are covered in the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Multiple Partial Captures
-------------------------

This feature enables you to request multiple partial captures for one authorization. A multiple partial capture allows you to incrementally settle authorizations over time. The total amount of all the captures must not exceed the authorized amount.  
Multiple partial captures are covered in the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Recurring Payments
------------------

A recurring payment is a credentials-on-file (COF) transaction in a series of payments that you bill to a customer for a fixed amount at regular intervals that do not exceed one year between transactions. The series of recurring payments is the result of an agreement between you and the customer for the purchase of goods or services that are provided at regular intervals. Recurring payments are also known as subscriptions.  
Recurring payments are covered in the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

Subsequent Authorizations
-------------------------

This feature enables you to manage recurring transactions. After a successful initial authorization, you can request subsequent authorizations and request one capture for both authorizations.  
Subsequent authorizations are covered in the "Standard Payments Processing" section of the [Payments Developer Guide](https://developer.example.com/docs.md#PaymentServices "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.
