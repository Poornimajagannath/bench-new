Implementing Direct API for Payer Authentication {#concept_hdl_g1x_wpb}
=======================================================================

The Direct API integrates EMV `3-D Secure` 2.x into your business's website. This integration uses an iframe to complete the device profiling and EMV `3-D Secure` authentication requirements without including third-party JavaScript directly on your site.
This implementation requires the use of JavaScript to leverage the authentication. The JavaScript is hosted and contained inside the iframe and does not directly access your web page.

> IMPORTANT
> Payer Authentication uses Cardinal Centinel as the technology platform to manage all EMV ` 3-D Secure ` authentication processes. Any references to Cardinal in this document refer to the underlying services that are provided by Cardinal technology.
> A website that provides a demo tool to help users understand how payer authentication works is available:
> [https://developer.cybersource.com/demo/index.html](https://developer.cybersource.com/demo/index.md "").
> You can complete the steps required to implement payer authentication on their website and examine the code underlying the process. Use test card numbers to walk through the process and enter `123` as the security code.

Prerequisites {#concept_q1d_j1x_wpb}
====================================

Notify your account representative that you want to implement payer authentication (3-D Secure) using the Direct API integration. Provide the merchant ID that you will use for testing. For more information, see [Required Merchant Information](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-intro-intro/pa2-intro-process-overview.md "").
Before you can implement payer authentication services, your business team must contact your acquirer and `Cybersource` to establish the service. Your software development team should become familiar with the API fields and technical details of this service.

After Implementation and Before Go Live {#concept_nzg_z3x_wpb}
==============================================================

Use the test cases to test your preliminary code and make appropriate changes. See [Testing Payer Authentication](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md ""). Testing ensures that your account is configured for production and that your transactions are processed quickly and correctly.
