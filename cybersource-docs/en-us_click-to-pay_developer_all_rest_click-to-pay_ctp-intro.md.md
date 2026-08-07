Introduction to the `Click to Pay Drop-In UI` {#ctp-intro}
==========================================================

`Click to Pay Drop-In UI` powered by `Unified Checkout` provides an interface for easy acceptance of `Click to Pay` payments from Relay, Mastercard, and American Express cards. The `Click to Pay Drop-In UI` handles manual card entry for the non-`Click to Pay` payment schemes called out in this guide. Throughout this guide we refer to both *`Click to Pay Drop-In UI`* and *`Unified Checkout`.*  
`Click to Pay Drop-In UI` consists of a set of server-side APIs and a client-side JavaScript library.  
The server-side APIs authenticate your merchant identity, instruct the system to act within your payment environment, and provide a way to retrieve the payment data following a successful `Click to Pay Drop-In UI` interaction.  
The provided JavaScript library enables you to place a payment application within your e-commerce environment. This embedded component offers `Click to Pay` and card entry to your customers.  
Whether a customer uses a stored `Click to Pay` card or enters their payment information manually, the `Click to Pay Drop-In UI` handles all user interactions and provides a response to your e-commerce system. All UI / UX must follow the UI/UX guidelines. For information about configuring your UI/UX, see [Click to Pay UI Examples](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-ui-screens/ctp-appendix-ui-ux-ex.md "").  
The `Click to Pay Drop-In UI` enables a portfolio to receive an encrypted payload and send a request to the API to retrieve the payment details. The format of the decrypted payment details are determined by the transaction type. The details are either a network token and cryptogram or the PAN, expiration details, and card verification value (CVV).  
The figures below shows the `Click to Pay Drop-In UI` for a recognized user.

#### Figure: {#ctp-intro_fig1}

`Unified Checkout` UI with Card Payment Button  
![Example of the payment application with Click to Pay.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-mobile-ui-400x475.svg/jcr:content/renditions/original)

#### Figure: {#ctp-intro_fig_dwv_t41_3jc}

`Unified Checkout` UI without Card Payment Button ![Example of the trigger component of Click to Pay.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Firefox 121
* GoogleChrome/Chium‑based browsers 118
* MicrosoftEdge 118
* Safari16

