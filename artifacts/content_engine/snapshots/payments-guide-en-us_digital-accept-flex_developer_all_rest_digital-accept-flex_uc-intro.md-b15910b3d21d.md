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

