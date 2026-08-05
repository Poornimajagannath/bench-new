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
