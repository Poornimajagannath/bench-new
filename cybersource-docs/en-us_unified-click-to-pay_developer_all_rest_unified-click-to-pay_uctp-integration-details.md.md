pilot

`Unified Click to Pay` Integration {#uctp-integration-details}
==============================================================

This section describes how to integrate and launch `Unified Click to Pay` on your website and process a transaction for you. For information about the detailed specifications of the APIs described in this section see [API Specifications](/docs/cybs/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-api-specifications.md ""). To integrate `Unified Click to Pay` into your platform, you must follow these integration steps:

1. You send a server-to-server API request for a capture context. This request is fully authenticated and returns a JSON Web Token (JWT) that is necessary to invoke the frontend JavaScript library. For information on setting up the server side, see [Server-Side Set Up](/docs/cybs/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-integration-details/uctp-ss-setup.md "").
2. You invoke the `Unified Click to Pay` JavaScript library using the JWT response from the capture context request. For information on setting up the client side, see [Client-Side Set Up](/docs/cybs/en-us/unified-click-to-pay/developer/all/rest/unified-click-to-pay/uctp-integration-details/uctp-cs-setup.md "").

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

