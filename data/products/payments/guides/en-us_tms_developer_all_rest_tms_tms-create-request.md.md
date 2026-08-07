Requesting the `Token Management Service` API {#tms-create-request}
===================================================================

Before requesting the `Token Management Service` (`TMS`) API, you must already have a `Business Center` account. If you do not, you can create an evaluation account.  
Follow these steps to request the `TMS` API:

1. Authenticate to the API using either HTTP signature authentication or JSON Web Token (JWT) authentication.

   #### ADDITIONAL INFORMATION

   1. A Base64-encoded shared secret key is passed in the headers you generate for HTTP signature authentication.  
      See [Shared Secret Key Pair](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro.md "") in *Getting Started with the REST API* for instructions.
   2. A P12 Certificate is passed in the headers you generate for JWT authentication.  
      See [Create a P12 Certificate](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md "") in the *Getting Started with the REST API* for instructions.

   {#tms-create-request_ol_2} IMPORTANT

   > These keys are used to authenticate requests that are sent to the ` TMS ` API. You can create REST API keys at the portfolio or transacting organization level.  
   > Portfolio organizations that send requests to the ` TMS ` API on behalf of their transacting merchants can create Meta keys. Meta keys are used to transact on behalf of their multiple transacting MIDs with a single key. For more information on Meta keys, see [Meta Key Creation and Management](https://developer.cybersource.com/docs/cybs/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") in the *Creating and Using Security Keys* developer guide.

2. Specify one of the following hosts in the URL:

   #### ADDITIONAL INFORMATION

   1. **Sandbox:** `POST ``https://apitest.cybersource.com`
   2. **Production:** `POST ``https://api.cybersource.com`
   3. **Production in India:** `POST ``https://api.in.cybersource.com``/`
3. Append the resource, such as, `/tms/v2/customer` to the host URL. For example, `https://api.cybersource.com``/tms/v2/customer`.

4. Pass your request using a `HTTP` `GET`, `POST`, `PATCH` or `DELETE` method as specified in each API operation.

