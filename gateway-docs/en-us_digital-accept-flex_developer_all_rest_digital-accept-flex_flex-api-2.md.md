`Flex API` v2 {#flex-api-2_FlexAPI}
===================================

The `Flex API` v2 suite enables a merchant to ensure secure transmission of payment information captured from client-side code. Integrate your system with `Flex API` v2 to enable `Payment Gateway` to protect your customer's primary account number (PAN), card verification number (CVN), and other payment information when payment processing activity crosses the Web.

> IMPORTANT
> ` Flex API ` is not designed to be used from the browser. For securing payment information from the browser, please see the ` Microform Integration ` product.  
> Use the APIs in this suite to secure your customer's payment information, and exchange this sensitive data for a *transient token* . A transient token is a temporary reference to sensitive data that `Payment Gateway` has securely stored on your behalf. A transient token can be transported and stored safely without adding risk to your PCI DSS burden.  
> IMPORTANT The transient token response can be cryptographically validated to ensure that payload injection attacks can be mitigated.  
> Before you capture the payment data from the client application, generate the context in which the data is to be captured and tokenized. The *capture context* can help you to limit PCI exposure to the context in which it is captured.  
> After you capture the payment data from the client application, the `Flex API` v2 can secure and tokenize the data:

* `Payment Gateway` secures your customer's card data at the device using one-time public encryption keys.
* `Payment Gateway` then replaces the card data in the client application form with a transient token. A transient token can only be accessed by the merchant.
  {#flex-api-2_ul_zdk_1tn_qqb}  
  After you tokenize the payment information, you can initiate `Payment Gateway` services that use transient tokens in place of your customer's payment information.

