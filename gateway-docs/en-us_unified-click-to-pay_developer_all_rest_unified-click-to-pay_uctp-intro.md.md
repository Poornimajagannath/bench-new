pilot

Introduction to `Unified Click to Pay` {#uctp-intro}
====================================================

`Unified Click to Pay`, powered by `Unified Checkout`, provides a flexible integration that enables merchants to customize their checkout experience for accepting `Click to Pay` payments from Relay, Mastercard, and American Express. The `Unified Click to Pay` SDK has no UI and the UI must be configured by the integrator. This enables merchants and partners to fully control the UI and branding. `Unified Click to Pay` offers advanced security and compliance and is PCI 4.0 compliant.  
`Unified Click to Pay` consists of a server-side API and a client-side JavaScript SDK. The server-side component authenticates your identity as the merchant and instructs the system to act within your payment environment. The response contains a JWT that can be used for the initialization of the client-side SDK and sets up the backend configuration required to run the SDK.  
The client-side JavaScript SDK can be used to integrate with `Click to Pay` payments from Relay, Mastercard, and American Express cards.

> IMPORTANT
> Each request that you send to ` Payment Gateway ` requires header information. For information about constructing the headers for your request, see the [Getting Started with REST Developer Guide](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Prerequisites
-------------

Before you call the capture context and load the SDK, you must complete these tasks:

1. [Enable `Click to Pay`](/docs/gateway/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-intro/uc-enable-digital-pay-ctp.md "").
2. [Upload Your Encryption Key](/docs/gateway/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-intro/uctp-upload-encryption-key.md "").
3. [Set Up Customer Authentication for `Unified Click to Pay`](/docs/gateway/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-intro/uctp-authentication-steps.md "").

