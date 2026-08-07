Introduction to the `Token Management Service` {#tms-overview}
==============================================================

The `Token Management Service` (`TMS`) enables you to replace personally identifiable information (PII), such as the primary account numbers (PANs), with unique tokens. These tokens do not include the PII data, but act as a placeholder for the personal information that would otherwise need to be shared. By using tokens, businesses can provide a secure payment experience, reduce the risk of fraud, and comply with industry consumer security regulations such as PCI-DSS.  
`TMS` links tokens across service providers, payment types, and channels for sellers, acquirers, and technology partners. `TMS` tokenizes, securely stores, and manages the primary account number (PAN), the payment card expiration date, electronic check details, and customer data. `TMS` also enables you to create a network token of a customer's payment card.
IMPORTANT Due to mandates from the Reserve Bank of India, merchants based in India cannot store PANs. Use network tokens instead.  
You can manage sensitive data securely by creating, retrieving, updating, and deleting tokens through the [TMS API](https://developer.cybersource.com/api-reference-assets/index.md#token-management "").  
`TMS` simplifies your PCI DSS compliance. `TMS` passes tokens back to you that represent this data. You then store these tokens in your environment and databases instead of storing customer payment details.  
`TMS` protects sensitive payment information through tokenization and secures and manages customer data using these token types:

* Customer tokens
* Instrument identifier tokens
* Payment instrument tokens
* Shipping address tokens

These `TMS` tokens can be used individually, or they can be associated with one customer token:

#### Figure:

`TMS` Token Types  
![Diagram of the unified token identifier.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/tms/images/token-types-intro-600x400.svg/jcr:content/renditions/original)
