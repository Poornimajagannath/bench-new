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

