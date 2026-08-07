Processing Apple Pay Transactions {#applepay-txns-intro}
========================================================

`Payment Gateway` supports these payment services for Apple Pay: Authorization, Sale, Authorization Reversal, and Capture. This section of the guide contains tasks that show you how to use those services to process Apple Pay transactions:

* Authorize an Apple Pay payment with `Payment Gateway` decryption
* Authorize an Apple Pay payment with merchant decryption
* Process an Apple Pay sale with `Payment Gateway` decryption
* Process an Apple Pay sale with merchant decryption
* Reverse the authorization of an Apple Pay payment
* Capture an authorized Apple Pay payment  
  For each task in this section, the example request message includes the processingInformation. paymentSolution `REST` API field set to `001`. This value identifies Apple Pay as the digital payment solution.  
  IMPORTANT In response to your successful payment authorization request, Apple Pay returns an encrypted payload that contains sensitive payment information. The method you use to extract and decrypt the payment data depends on how you integrated Apple Pay into your system.  
  For high-level descriptions of the `Payment Gateway` decryption method and the merchant decryption method, see [Integration Options](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-intro-integration.md "").

