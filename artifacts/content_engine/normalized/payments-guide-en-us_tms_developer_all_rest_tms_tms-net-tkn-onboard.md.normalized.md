Network Tokenization Overview {#tms-net-tkn-onboard}
====================================================

Network tokenization replaces a customer's primary account number (PAN) with a network token. A network token is a tokenized card number that is issued by card networks (for example, Visa, Mastercard, American Express, and Discover). Network tokens use the same format as a PAN but are domain-restricted and cryptographically secured. This reduces exposure to fraud and data breaches.
Unlike standard tokens that are converted back to the PAN during authorization, network tokens remove the PAN from the payment flow. Each network token is provisioned with its own expiration date and is paired with a dynamic cryptogram. Tokens can be restricted to a specific merchant, device, or transaction context.
Initially introduced for digital wallets, network tokens now support card-on-file (COF) use cases such as subscriptions, recurring payments, and one-click checkout, enabling secure storage and reuse of payment credentials.
`Token Management Service` (`TMS`) tokens can be linked to network tokens:

* Instrument identifier tokens represent the underlying account
* Payment instrument tokens represent a stored payment method
* Customer tokens represent a stored customer profile

{#tms-net-tkn-onboard_ul_dwq_54k_mjc}

Key Benefits and Features {#tms-net-tkn-onboard_section_ecn_4qk_mjc}
--------------------------------------------------------------------

Network tokenization helps improve payment security, performance, and customer experience:

* **Enhanced security**: Tokens are domain-restricted and tied to your Token Requestor ID (TRID), so they can only be used in your environment. Tokens cannot be reused outside that domain and can be deactivated without reissuing cards.
* **Higher authorization rates**: Each transaction includes a dynamic cryptogram. This provides additional assurance to issuers and helping improve authorization performance.
* **Automatic updates**: Card life-cycle changes, such as reissues or expirations, are updated automatically. You receive updates without handling new card numbers, reducing payment disruptions.
* **Reduced PCI scope**: By storing tokens instead of raw card data, you can lower PCI compliance requirements and the associated costs.
* **Simplified checkout**: Cardholders can complete transactions without re-entering CVV, reducing friction and improving conversion.
* **Enhanced checkout experiences**: Support for card art and push provisioning enables seamless onboarding and enhanced checkout or wallet interactions.
  {#tms-net-tkn-onboard_ul_j5w_4qk_mjc}

Integration Models {#tms-net-tkn-onboard_section_ypk_crk_mjc}
-------------------------------------------------------------

You can tokenize payment credentials using `TMS` or when you process payments:

* **`TMS` tokenization** : Use `TMS` as a standalone service for token provisioning, cryptogram generation, and lifecycle updates.
* **Tokenization with payments** : Extend existing payment flows with minimal changes, while `TMS` manages token life-cycle and transaction handling.
  {#tms-net-tkn-onboard_ul_ms5_2rk_mjc}
