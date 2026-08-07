Introduction to Payer Authentication {#pa2-intro-intro}
=======================================================

`Cybersource` has a variety of products to manage and minimize the risk of fraud that merchants face in their daily transactions. While these risk management products can operate independently to address specific areas of risk, the best results are achieved when the entire suite of products works in concert to detect patterns of fraud in a business's online activity.

* Payer Authentication: Uses the `3-D Secure` protocol in online transactions to verify that payment is coming from the actual cardholder. Most transactions can be authenticated without the customer being aware of the process, but higher risk transactions might require an exchange of one-time passwords (OTPs) during authentication. This authentication of the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer. You can use Decision Manager with payer authentication services so that the risk level of an order determines when to invoke payer authentication. For example, low-risk orders can be set to skip payer authentication and proceed directly to authorization.
* Decision Manager: Uses AI to help large enterprises analyze the vast amount of data from their online transactions to detect known patterns of fraudulent behavior. Each potential transaction can be compared to past patterns and automatically assigned a risk score before authorizing a transaction. Behavior analysis of past transaction data enables you to recommend rules that identify risky transactions and to suggest how to handle them. Machine learning capabilities in Decision Manager enable you to create hypothetical environments to test strategies for dealing with risky scenarios so that you can either reject them or require payer authentication.
* Fraud Management Essentials: helps small-to-medium businesses monitor their online transactions using AI and preconfigured rules to spot and avoid fraudulent transactions. You can adjust the fraud detection settings to match your risk tolerance and manually review transactions flagged for risk review.
* Account Takeover Protection: monitors customer account activity to detect compromised accounts. You create account events and define rules to determine the types and levels of activity in a customer account that trigger a manual review for potential fraud. The activity data that happens within a customer account can be easily integrated into Decision Manager and used to assess risky payment behavior.

{#pa2-intro-intro_ul_l2t_bxn_n1c}
This guide documents the payer authentication aspect of fraud management and how payer authentication can be used to satisfy the Strong Customer Authentication (SCA) requirement of the Payment Services Directive (PSD2) that applies to the European Economic Area (EEA) and the United Kingdom. SCA requires banks to perform additional verification when customers make payments to confirm their identity. Access to the documentation for other aspects of the risk management portfolio requires a `Cybersource` support license for that product.
Transactions where the card is not present have a high risk of fraud, so authenticating a payer before processing a transaction greatly reduces the merchant risk for chargebacks. Payer authentication is a way of verifying that a customer making an e-commerce purchase is the owner of the payment card being used. The protocol that is followed to authenticate customers during online transactions is called [EMV 3-D Secure](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-glossary.md#reference_sjs_jmp_wpb_3-d-secure "").
This EMV `3-D Secure` protocol is used by all major payment cards to implement payer authentication, but payment companies usually brand it under a different name:

* Visa: Visa Secure
* Mastercard: Mastercard Identity Check
* American Express: American Express SafeKey
* JCB: J/Secure
* Discover/Diners: ProtectBuy
* Elo: Compra Segura (Secure Shopping)
* Cartes Bancaires: FAST'R
* China UnionPay: `3-D Secure`

{#pa2-intro-intro_ul_qf3_zhl_kxb}

Supported Card Networks
-----------------------

These card networks support using EMV `3-D Secure` during transactions:

* Amex
* Cartes Bancaires
* China UnionPay
* Discover/Diners
* eftpos
* Elo
* JCB
* Mada
* Mastercard
* Visa
  {#pa2-intro-intro_ul_yft_hdj_cfc}
