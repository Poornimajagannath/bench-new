Integrating Apple Pay into Your System {#applepay-cfg}
======================================================

This section describes how to integrate Apple Pay into your iOS app or website. The integration tasks are organized into three parts. The second part provides separate steps for the two different decryption models. The third part applies only if you will be supporting Apple Pay on the web.  
You will perform the integration tasks twice: First in your test environment and, after you validate your test integration, a second time in your production environment.

* **Part 1: Set Up Your Apple Developer Account** . You will enroll your organization in the Apple Developer Program, create an *Apple merchant ID*, and register it in your developer account.
* **Part 2: Create an Apple Pay Payment Processing Certificate** . This certificate is associated with your merchant ID, and it is used by Apple Pay servers to encrypt payment data.
  * You will generate a *certificate signing request* (CSR) at the system that will handle Apple Pay payload decryption. For `Cybersource` decryption, you will generate the CSR at the `Cybersource` `Business Center` user interface. For merchant decryption, you will generate the CSR at your Apple device.
  * You will upload the CSR with the public key to your Apple Developer account and use the CSR to create a *payments processing certificate* for your merchant ID and Apple Pay.
* **Part 3: Perform Additional Setup for Apple Pay on the Web** . If you offer your customers Apple Pay on the web, you will create an *Apple Pay merchant identity certificate* , associate the certificate with your merchant ID, and register *each merchant domain* that will process Apple Pay transactions.

> TIP
> If you are integrating **Apple Pay with ` Cybersource ` decryption** and you are experienced in creating Apple Pay payment processing certificates, you can use the [Quick Integration for the Cybersource Decryption Method](/docs/cybs/en-us/apple-pay/developer/all/rest/applepay/applepay-reference/applepay-ref-1-cybs-decrypt-quick.md "") instead of the detailed steps in this section.

