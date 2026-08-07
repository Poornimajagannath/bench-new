Introduction to Apple Pay {#applepay-intro}
===========================================

Apple Pay is a digital payment solution that enables your customers to make secure and convenient purchases without requiring them to enter their card details or shipping information. You can use the `Payment Gateway` platform to process and manage Apple Pay transactions.  
When you offer your customers *device apps* enabled for Apple Pay, you can collect payments for purchases made on iPhone and Apple Watch apps. When you offer your customers *Apple Pay on the web* , Apple Pay cardholders can purchase goods and services from within your web app. You can try an Apple Pay test transaction on the Apple Developer site by using the *Apple Pay on the Web Interactive Demo*:  
<https://applepaydemo.apple.com/>  
Using Apple Pay on the `Payment Gateway` platform can reduce the exposure of sensitive payment data to your system. When a cardholder initiates a purchase from within your Apple Pay enabled app or web page, Apple Pay receives the encrypted transaction. An Apple Pay server returns the transaction payment information re-encrypted with a developer-specific key. The key helps to ensure that only the app or the web page can access the encrypted information.  
Customers experience reduced payment friction because their information is tokenized and stored for future use. Customers who configure auto-fill options for their Apple Pay accounts can have payment and card data pre-populate after they sign in to their accounts and authenticate.

Apple Pay Digital Wallets (with the Elavon Processor)
-----------------------------------------------------

**With the `Elavon` processor,** `Payment Gateway` supports Apple Pay as a digital wallet, which is a mobile app that enables users to link their credit cards, debit cards, loyalty card to their mobile phones. The mobile wallet enables fast online checkouts and contactless in-store payments. `Payment Gateway` digital wallets integrate through `Unified Checkout`, ensuring secure transactions.  
`Elavon` supports 3-D Secure 2.2 with Diners Club, Mastercard, and Relay card transactions. The section [Authorizing Apple Pay Digital Wallet Payments (with Elavon)](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-auth-digital-wallet.md "") covers authorizations of Apple Pay digital wallet payments without 3-D Secure and with 3-D Secure.

Processors and Cards Supported
------------------------------

Support for card types and optional features varies by partner and processor. For a list of processors and cards supported with Apple Pay, see [Processors and Cards Supported with Apple Pay](/docs/gateway/en-us/apple-pay/developer/all/rest/applepay/applepay-intro/applepay-ref-6-supported-processors-all.md "").
