Introduction to the BIN Lookup Service {#bin-lookup-intro}
==========================================================

The BIN Lookup Service provides payment card account information based on a *bank identification number* (BIN) and account range information. The BIN represents the first six or eight digits on the payment card. The first digit of the BIN is the industry identifier for the network used by the card-issuing institution. The remaining five or seven digits of the BIN identify the card-issuing institution and some of the card attributes.  
You can request the BIN Lookup Service using a payment card number (PAN), BIN, network token, Token Management Service (TMS) token, or `Secure Acceptance` transient token.  
For more information about TMS, see the [Token Management Service API reference](https://developer.example.com/api-reference-assets/index.md?stage=pilot#token-management "") or the [Token Management Services Developer Guide](https://developer.example.com/docs/gateway/en-us/tms/developer/ctv/rest/tms/tms-about-guide.md "").  
For more information about `Secure Acceptance` transient tokens, see the [`Digital Accept` Secure Integration Developer Guide](https://developer.example.com/docs/gateway/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex/da-about-guide.md "").  
BIN lookup service returns BIN attribute information for the payment credential specified in the request, such as:

* Card type code
* Card brand, such as American Express, Mastercard, or Relay
* Card currency
* Account funding source, such as credit or debit
* Account prefix
* Payment credential type
* Issuer BIN length (network dependent)
* Issuer name
* Issuer country
* Issuer phone number
* Fast funds eligibility (if enabled)

