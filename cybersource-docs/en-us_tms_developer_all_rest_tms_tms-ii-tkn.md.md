Instrument Identifier Tokens {#tms-ii-tkn}
==========================================

Instrument identifier tokens represent tokenized payment account numbers. Tokenized payment account information includes a primary account number (PAN) for card payments, or a US or Canadian bank account number and routing number for an ACH bank account. An instrument identifier token can exist independently, or it can be associated with a payment instrument.  
An instrument identifier token can also contain an associated network token.  
Instrument identifier tokens are associated with these features:

Card Art
:
`TMS` card art helps your customers select a card. See [Card Art](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-card-art.md "").

Enrollable Network Tokens
:
`TMS` can enroll certain *network tokens* in an instrument identifier token to be used for future payments. Future payments require only the instrument identifier token for the payment information. The types of network tokens you can enroll into an instrument identifier are tokens used for in-app payment methods such as:

    * Android Pay
    * Apple Pay
    * Chase Pay
    * Google Pay
    * Samsung Pay
    * `Relay Click to Pay`

    See [Create an Instrument Identifier for Enrollable Network Tokens](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-ii-tkn/tms-manage-ii-tkn/tms-ii-tkn-create-device-tkn-intro.md "").

Push Provisioning
:
Push provisioning connects you with participating issuers to quickly provide credentials to your customers. See [Provision a Network Token with Push Provisioning](/docs/cybs/en-us/tms/developer/all/rest/tms/tms-net-tkn-intro/tms-net-tkn-card-create-intro.md "").
