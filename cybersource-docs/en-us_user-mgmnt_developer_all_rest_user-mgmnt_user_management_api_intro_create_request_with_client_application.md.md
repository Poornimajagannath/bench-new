REST API

Create an API Request {#Id18ANJ0UK0HS_Id18ANJ100XHT}
====================================================

To call the User Management API:

1. You must already have a Business Center account. If you do not, you can create an [evaluation account](../../../../../../../api/developer-guides/dita-gettingstarted/registration.md "").
2. [Authenticate](../../../../../../../api/developer-guides/dita-gettingstarted/authentication.md "") to the API using either:
   1. [HTTP Signature Authentication](../../../../../../../api/developer-guides/dita-gettingstarted/authentication/createSharedKey.md "") - A Base-64 encoded Shared Secret Key passed in the [headers you generate for HTTP Signature authentication](../../../../../../../api/developer-guides/dita-gettingstarted/authentication/GenerateHeader/httpSignatureAuthentication.md "").
   2. [P12 Certificate](../../../../../../../api/developer-guides/dita-gettingstarted/authentication/createCert.md "") - Used for JSON Web Token (JWT) authentication and passed in the [headers you generate for JWT authentication.](/api/developer-guides/dita-gettingstarted/authentication/GenerateHeader/jwtTokenAuthentication.md "")
      {#Id18ANJ0UK0HS_ol_2}
3. Specify one of the following hosts in the URL:
   * **Sandbox:** `POST https://apitest.cybersource.com/`
   * **Live:** `POST https://api.cybersource.com/`
   * **Live in India:** `POST https://api.in.cybersource.com/`
     {#Id18ANJ0UK0HS_ol_3}
4. Append the resource `/ums/v1/users/search` to the host name.
5. Pass your request in a HTTP POST method. See [Retrieve a list of users](/docs/cybs/en-us/user-mgmnt/developer/all/rest/user-mgmnt/user_management_api_intro/retrieve_list_of_users.md "") for details.
   {#Id18ANJ0UK0HS_ol_1}

