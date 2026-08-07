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
options.](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/unified-checkout/images/button-widget-flow-865x475.svg/jcr:content/renditions/original)  
For examples of different payment method UIs through `Unified Checkout`, see these topics:

* [Click to Pay UI](/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-ctp/uc-ui-ctp.md "")
* [Google Pay UI](/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-googlepay/uc-ui-googlepay.md "")
* [Pay with eCheck/ACH Service UI](/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-echeck/uc-ui-echeck.md "")
* [Paze UI](/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-paze/uc-ui-paze.md "")
* [Apple Pay UI](/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-pay-methods-intro/uc-pay-methods-dig-wallets/uc-pay-methods-dig-wallets-applepay/uc-ui-applepay.md "")
  .

> IMPORTANT
> Each request that you send to ` Payment Gateway ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Key Features
------------

![](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-intro-600x100.svg/jcr:content/renditions/original)
* **Low-code integration**: You can use as few as three lines of JavaScript to accept payments, as well as add or remove payment methods through portal configuration without changing your integration code.
* **PCI SAQ-A compliant**: Payment data never touches your systems.
* **Fully customizable**: You can match the payment experience to your brand with theming, fonts, and layout options. Embed inline or display as a sidebar overlay.
* **Service orchestration** : You can use `Decision Manager`, `Payer Authentication` (`3-D Secure`), and `Token Management Service` (`TMS`) throughout the session.

