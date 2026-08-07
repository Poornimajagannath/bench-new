`Token Management Service` {#boarding-pecs-tms}
===============================================

The `Token Management Service` (`TMS`) links tokens across service providers, payment types, and channels for sellers, acquirers, and technology partners. `TMS` tokenizes, securely stores, and manages the primary account number (PAN), the payment card expiration date, electronic check details, and customer data. `TMS` also enables merchants to create a network token of a customer's payment card.

> IMPORTANT
> When you board a merchant and enable ` TMS ` and network tokenization, the token requestor ID is enrolled at the merchant account organization level where the token vault is configured. You must include the merchant business information during token requestor ID enrollment and when you create the ` TMS ` token vault. This ensures that the network tokens that are provisioned are assigned to the merchant that owns the tokens.  
> For more information on `TMS` and network tokenization, see [Token Vault Management](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-products-intro/boarding-tms/tms-vault-hierarchy.md "").

