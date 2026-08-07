Requesting the BIN Lookup Service with Fast Funds Eligibility Using the REST API {#bin-lookup-payouts-req-task}
===============================================================================================================

Send one of these payment credentials to the BIN Lookup Service to retrieve BIN information and fast funds eligibility.  
**Payment Card Numbers**

* Full payment card number  
  **Tokens**

* `TMS` customer ID token

* `TMS` payment instrument token

* `TMS` instrument identifier token

* `TMS` jti transient token

* `Flex API` JWT transient token  
  Follow these steps to request the BIN Lookup Service with Fast Funds:

1. Send the request to the BIN Lookup Service endpoint:

   #### ADDITIONAL INFORMATION

   `POST https://&lt;``url_prefix``&gt;/bin/v1/binlookup `

   #### ADDITIONAL INFORMATION

   Use one of these URL prefixes:

   * Test: `apitest.example.com`
   * Production: `api.example.com`
   * Production in India: `api.in.example.com`
2. Include one of the prerequisite fields in the request:

   * paymentInformation.card.number (Full payment card number is recommended.)
   * paymentInformation.customer.id
   * paymentInformation.instrumentIdentifier.id
   * paymentInformation.paymentInstrument.id
   * tokenInformation.jti
   * tokenInformation.transientTokenJwt
     {#bin-lookup-payouts-req-task_choices_az2_s4v_f5b}
3. Request the service. Set processingInformation.payoutOptions.payoutInquiry to true.

4. Include optional fields in the request as needed.

5. Check the response message to make sure that the request was successful. A 200-level HTTP response code indicates success. For information about response codes, see [BIN Lookup Response Codes](/docs/gateway/en-us/bin-lookup/developer/all/rest/bin-lookup/bin-lookup-reference-intro/bin-lookup-resp-codes.md ""). {#bin-lookup-payouts-req-task_response-rest}

