Transient Tokens {#uc-tokens-intro}
===================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the checkout.mount() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.  
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.
