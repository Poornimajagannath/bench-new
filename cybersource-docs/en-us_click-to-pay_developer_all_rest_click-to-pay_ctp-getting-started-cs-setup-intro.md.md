Client-Side Set Up {#ctp-getting-started-cs-setup-intro}
========================================================

This section contains the information you need to set up the client side. You use the `Unified Checkout` JavaScript library to integrate with your e-commerce website. It has two primary components:

* The button widget, which presents `Click to Pay` to the customer. There are different options available to display this to your customers. See these topics: XXX
* The payment acceptance page, which captures payment information from the cardholder. You can embed the payment acceptance page within your webpage or add it as a sidebar.

The `Unified Checkout` JavaScript library supports `Click to Pay` and manual card entry payment methods.  
Follow these steps to set up the client:

1. Load the JavaScript library.
2. Initialize the accept object the capture context JWT. For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").
3. Initialize the unified payment object with optional parameters.
4. Show the button list or payment acceptance page or both.

{#ctp-getting-started-cs-setup-intro_ul_m5t_gwq_npb}  
The response to these interactions is a transient token that you use to retrieve the payment information captured by the UI.
