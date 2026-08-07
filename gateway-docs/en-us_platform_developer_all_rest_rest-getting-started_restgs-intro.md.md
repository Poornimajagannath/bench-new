Introduction to REST {#restgs-intro}
====================================

To get started using `Payment Gateway` APIs, you must first set up your system to be REST-compliant. `Payment Gateway` uses REST for developing web services. REST enables your system to exchange request and response messages with the `Payment Gateway` gateway using HTTP. This guide explains how to set up secure messaging using *JSON Web Tokens* or *HTTP Signature Security*.  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rest-api-overview-pgw-720x170.svg/jcr:content/renditions/original)

**JSON Web Token Messaging**
:
JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. Depending on your integration, you can sign your tokens with a certificate private key or a shared secret key. The signature is calculated from the JWS header and payload, which enables the receiver to verify that the content has not been tampered with.

    > WARNING  
    > As of **February 2026** , there are new requirements for constructing JWTs. This update also requires you to encrypt and decrypt messages using Message-Level Encryption (MLE). To remain compliant, you must update how your system constructs JWTs with MLE by **September 2026**. If you do not update your system before the September deadline, you risk transaction failure. Use this guide to update your system.

HTTP Signature Security Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original)
:
With HTTP Signature messaging, each request is digitally signed using a shared secret. This enables both the client and the server to validate the authenticity and integrity of the request. If a request is intercepted during transmission, an attacker cannot modify it or impersonate the sender without the shared secret key. HTTP Signature messaging can be used only with API requests and cannot be used in browser-based or mobile applications.

    > WARNING  
    > By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.

![](/content/dam/documentation/pgw/en-us/common/images/warning-red-24x24.svg/jcr:content/renditions/original) Fraud Prevention and Security Responsibilities
-------------------------------------------------------------------------------------------------------------------------------------------------------------

When setting up your connection to the `Payment Gateway` gateway, verify that you have implemented controls to prevent card testing and card enumeration attacks on your platform. For more information, see the [best practices guide](https://www.example.com/content/dam/documents/en/payment-card-testing-bot-attacks.pdf "").  
If `Payment Gateway` detects suspicious transaction activity associated with your merchant ID, including card testing or card enumeration attacks, `Payment Gateway` reserves the right to enable fraud management tools on your behalf to help mitigate the attack. The fraud team might also implement internal controls that block traffic perceived as fraudulent.  
If you are already using a `Payment Gateway` fraud tool and experience a significant attack, `Payment Gateway` internal teams might modify or add rules to your configuration to help reduce the threat to both your business and `Payment Gateway` infrastructure. However, these actions do not replace your responsibility to follow industry-standard best practices to protect your systems, servers, and platforms.
