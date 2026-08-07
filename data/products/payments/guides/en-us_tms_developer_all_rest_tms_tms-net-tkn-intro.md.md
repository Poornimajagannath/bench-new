Manage Network Tokens {#tms_net_tkn_intro}
==========================================

This section contains information about how to manage network tokens using `TMS`.  
You can manage network tokens using the Instrument Identifiers, Tokenized Cards, and Payment Credentials APIs.

Tokenized Cards API {#tms_net_tkn_intro_section_idv_fwf_3jc}
------------------------------------------------------------

The Tokenized Cards API enables you to create, retrieve, and manage network tokens:

* [Create a Network Token](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-partner-card-intro.md "")

* [Retrieve a Network Token](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-card-retrieve-tkn-consumer-intro.md "")

* [Delete a Network Token](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-card-delete-tkn-consumer-intro.md "")
  {#tms_net_tkn_intro_ul_jtr_ffy_hjc}  
  The Tokenized Cards API also supports these value-added capabilities for network tokenization:

* [Provision a Network Token for a Consumer](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-card-create-cof-intro.md "")

* [Provision a Network Token with Push Provisioning](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-card-create-intro.md "")

* [Payment Passkey](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-passkey-intro.md "")
  {#tms_net_tkn_intro_ul_utp_kfy_hjc}  
  For information about network tokenization, see [Network Tokenization Overview](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-onboard.md "").  
  To retrieve payment credentials, including a cryptogram for a network token, see [Generate Payment Credentials](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-pay-cred-intro.md "").  
  Use this endpoint to access the Tokenized Cards API: `POST ``https://apitest.cybersource.com``/tms/v2/tokenized-cards`

Payment Credentials API {#tms_net_tkn_intro_section_t22_gwf_3jc}
----------------------------------------------------------------

The Payment Credentials API enables you to generate and retrieve network token payment credentials such as:

* Network token value

* Cryptogram (Visa and Mastercard only)

* Dynamic card verification value (CVV) (American Express only)
  {#tms_net_tkn_intro_ul_s5x_txf_3jc}  
  Use this endpoint to access the Payment Credentials API: `POST ``https://apitest.cybersource.com``/tms/v2/tokens/`*{tokenId}/*`payment-credentials`  
  You can also provision a network token while creating an instrument identifier token or when you process a payment:

* `POST ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers`

* `POST ``https://apitest.cybersource.com``/pts/v2/payments`
  {#tms_net_tkn_intro_ul_t1k_342_mjc}  
  For information about provisioning a network token when you create an instrument identifier, see *Create Instrument Identifier Using Card and Create Network Token* in the [`Cybersource` Developer Center API Reference](https://developer.cybersource.com/api-reference-assets/index.md#token-management_instrument-identifier_create-an-instrument-identifier_samplerequests-dropdown_create-instrument-identifier-using-card-and-create-network-token_liveconsole-tab-request-body "").  
  For information about provisioning a network token when you process a payment, see *Authorization with a Customer Token* in the [`Cybersource` Developer Center API Reference](https://developer.cybersource.com/api-reference-assets/index.md#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body "").

