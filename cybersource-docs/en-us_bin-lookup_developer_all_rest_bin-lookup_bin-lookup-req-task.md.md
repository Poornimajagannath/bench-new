Requesting the BIN Lookup Service Using the REST API {#bin-lookup-req-task}
===========================================================================

`Cybersource` recommends that you send the full payment card number (PAN), a TMS token, or a network token when you request the BIN Lookup Service. This ensures that a single BIN record is identified during the request. Even though the service supports sending the six-digit or eight-digit card prefix in the request, this option can result in a `MULTIPLE` record match error if a single BIN record cannot be identified.

> IMPORTANT
> When you receive a ` MULTIPLE ` status record match error, we recommend you provide the full payment card number, a TMS token, or a network token to receive a ` SUCCESS ` status in the response.  
> Send one of these payment credentials to the BIN Lookup Service to get the payment card account information.  
> **Payment Card Numbers**

* Full payment card number (recommended best practice)

* Eight-digit card prefix (not recommended because it might result in a `MULTIPLE` status record match error)

* Six-digit card prefix (not recommended because this option can result in a `MULTIPLE` status record match error)  
  **Tokens**

* `TMS` customer ID token

* `TMS` payment instrument token

* `TMS` instrument identifier token

* `TMS` jti transient token

* `Flex API` JWT transient token

* Network tokens (Visa VTS, Mastercard MDES, and Discover)  
  Follow these steps to request the BIN Lookup Service:

1. Send the request to the BIN Lookup Service endpoint:

   #### ADDITIONAL INFORMATION

   `POST https://&lt;``url_prefix``&gt;/bin/v1/binlookup`

   #### ADDITIONAL INFORMATION

   Use one of these URL prefixes:

   * Test: `apitest.cybersource.com`
   * Production: `api.cybersource.com`
   * Production in India: `api.in.cybersource.com`
2. Include one of the prerequisite fields in the request:

   * paymentInformation.card.number (Full payment card number is recommended.)
   * paymentInformation.customer.id
   * paymentInformation.instrumentIdentifier.id
   * paymentInformation.paymentInstrument.id
   * tokenInformation.jti
   * tokenInformation.transientTokenJwt
     {#bin-lookup-req-task_choices_az2_s4v_f5b}
3. Include optional fields in the request as needed.

4. Check the response message to make sure that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [BIN Lookup Response Codes](/docs/cybs/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-reference-intro/bin-lookup-resp-codes.md "").

