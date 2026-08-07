OAuth 2.0 Partner Implementation Guide {#cybs-extend-intro_id19818A009Y4}
=========================================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This document is for technology partners who want to register their OAuth application with `Cybersource`. Merchants can then delegate access to a technology partner to take actions on their behalf without sharing security keys. Actions can include accessing customer data and processing transactions.

Conventions
:
This special statement is used in this document:
> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional processor-specific versions of this guide and additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#oauth-doc-revisions}
========================================================

26.04.02
--------

Corrected the supported DigitCert CAs. The same CA can be used for both production and test environments. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

26.04.01
--------

Added list of supported DigiCert CAs for the test environment. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").  
Added additional information about the deprecated DigiCert CAs and how to know if you are affected by the no longer supported DigiCert CAs. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

25.11.01
--------

Added new section for how to set up OAuth 2.0. See [How to Set Up OAuth 2.0](/docs/cybs/en-us/oauth/developer/all/rest/oauth/implementation-overview.md "").  
Added support for new DigiCert CAs. Removed support for previous DigiCert CAs. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

25.05.02
--------

This revision contains only editorial changes and no technical updates.

25.05.01
--------

Updated the list of valid certificates for mutual authentication. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

25.01.02
--------

Updated the supported certificate authorities. See [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

25.01.01
--------

Updated the server-to-server certificate to include supported certificate authorities. See [How to Set Up OAuth 2.0](/docs/cybs/en-us/oauth/developer/all/rest/oauth/implementation-overview.md "") and [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to OAuth 2.0 Integration {#home}
=============================================

OAuth 2.0 enables your `Cybersource` merchants to securely grant your web-application permission to perform actions on their behalf, such as accessing their customer data and processing transactions. As a technology partner, you can integrate OAuth 2.0 into your web-application through `Cybersource`. When your integration is complete, `Cybersource` authenticates merchants for you, ensuring that your web-application only performs actions authorized by the merchants. This authentication method securely connects your web-application to the merchant account without the need to receive or store sensitive merchant credentials in your system.  
This guide explains how you, a technology partner, can set up and enable OAuth 2.0 for your web-application.

> IMPORTANT
> OAuth integration through ` Cybersource ` is in the pilot phase. To join the pilot program, and to know which API requests are OAuth-enabled, contact ` Cybersource ` support:  
> ` `[technology-partners.html](https://developer.cybersource.com/technology-partners.md "")` `

#### Figure:

OAuth 2.0 Overview ![](/content/dam/documentation/cybs/en-us/topics/platform/bam/oauth/images/oauth-overview-600x420.svg/jcr:content/renditions/original)

Additional Information about OAuth 2.0
--------------------------------------

OAuth is an industry-standard authorization protocol that enables an application to delegate limited access to another application. For more information about the OAuth open technical standard, see this OAuth 2.0 description from the official OAuth website:  
[`https://oauth.net/2/`](https://oauth.net/2/ "")

How to Set Up OAuth 2.0 {#implementation-overview}
==================================================

This overview describes the steps that you and the merchant must complete to implement OAuth.

#### Figure:

OAuth 2.0 Implementation ![](/content/dam/documentation/cybs/en-us/topics/platform/bam/oauth/images/oauth-implement-700x400.svg/jcr:content/renditions/original)

1. You enable mutual authentication by obtaining a Certificate Signing Request (CSR) from a supported certificate authority (CA). After obtaining a CSR, you provide your common name details to `Cybersource`. For more information, see [Enable Mutual Authentication](/docs/cybs/en-us/oauth/developer/all/rest/oauth/Supporting-Mutual-Authentication.md "").

2. You register your web-application in the `Business Center` and set a scope of permissions and a redirect URL to your web-application. For more information, see [Register Your Application](/docs/cybs/en-us/oauth/developer/all/rest/oauth/register-application.md "").

3. The merchant accesses your web-application, logs into their account using their credentials, and clicks a button or link to set up their `Cybersource` account.

4. Your application redirects the merchant to a `Cybersource`-hosted webpage. For more information, see [Redirect the Merchant](/docs/cybs/en-us/oauth/developer/all/rest/oauth/redirect-merchant-to-cybs.md "").

5. The merchant logs in to their `Cybersource` account and approves your request. This authorizes your web-application to perform specific actions on their behalf which are set by the permissions scope that the merchant approved. Notify the merchant that their account must have access to grant OAuth permissions to complete this requirement.

6. `Cybersource` redirects the merchant to your application using the redirect URL you registered. An authentication code is appended to the redirect URL. For more information, see [Interpreting the Redirect Response](/docs/cybs/en-us/oauth/developer/all/rest/oauth/redirect-merchant-to-cybs/response-parameters.md "").

7. Your application exchanges the authorization code with `Cybersource` for these two tokens:

   * **Access token** : A token to authenticate transactions using `Cybersource`. For more information about how to authenticate `Cybersource` transactions using this token, see [Submit API Requests Using OAuth](/docs/cybs/en-us/oauth/developer/all/rest/oauth/submitting-api-request-using-cybs-extend.md "").
   * **Refresh token**: A token that you can use to request additional access tokens.

   For more information about requesting tokens, see [Request the Access and Refresh Tokens](/docs/cybs/en-us/oauth/developer/all/rest/oauth/obtaining-access-refresh-tokens.md "").  
   For more information about refreshing your existing tokens, see [Refresh the Access Token](/docs/cybs/en-us/oauth/developer/all/rest/oauth/refreshing-access-token.md "") and [Refresh the Refresh Token](/docs/cybs/en-us/oauth/developer/all/rest/oauth/refreshing-the-refresh-token.md "").

To change the permissions the merchant grants you, you must repeat steps 2--7.  
You can view examples of these steps in the [demo application](https://oauthsample.test.cybersource.com/cybersource-oauth-app/ "").  
You must obtain test merchant credentials to emulate the access delegation. Your test account must contain at least one card-based transaction from within the past 7 days. To sign up for a sandbox test account to create your test credentials, see:  
[`https://developer.cybersource.com/hello-world/sandbox.html`](https://developer.cybersource.com/hello-world/sandbox.md "")

Enable Mutual Authentication {#Supporting-Mutual-Authentication_id2024I060BY4}
==============================================================================

OAuth uses *mutual authentication* to provide an additional layer of security. Mutual authentication occurs when a client and server verify each other's identities simultaneously. To enable mutual authentication, you must use a server-to-server certificate issued by a trusted Certificate Authority (CA). Before you can register your application with `Cybersource`, you must create one of these supported DigiCert CAs and enable mutual authentication:

Supported DigiCert CAs
:
* X9 Financial PKI -- ECC P-256 Root
* X9 Financial PKI -- RSA 2048 Root
* X9 Financial PKI -- RSA 4096 Root

:
Contact support to obtain a certificate from DigiCert: [`https://www.digicert.com/contact-us`](https://www.digicert.com/contact-us "")

Deprecated DigiCert CAs and Transition Guidance
-----------------------------------------------

These CAs are no longer supported:

* DigiCert Assured ID Root G2
* DigiCert Global G2 TLS RSA SHA256 2020 CA1
* DigiCert High Assurance EV Root CA
* DigiCert SHA2 Extended Validation Server CA

> IMPORTANT  
> If your current integration uses a deprecated DigiCert CA, obtain one of the supported certificates when your existing certificates expire or are due for renewal.  
> DigiCert has announced that the Client Authentication EKU will be removed from public TLS certificates to comply with industry requirements. Without this EKU, certificates cannot be used for client authentication in mTLS, which is essential for secure OAuth integrations. If your organization uses DigiCert certificates for mTLS, client authentication, or server-to-server authentication, review the DigiCert article [*"What should I do to prepare for the Client Authentication EKU removal from public TLS certificates?"*](https://knowledge.digicert.com/alerts/sunsetting-client-authentication-eku-from-digicert-public-tls-certificates#what-do-you-need-to-do ""). This article explains if your certificate usage is affected and describes DigiCert alternatives.  
> To download the supported X9 production root and intermediate certificates used for mTLS, see the DigiCert article [*X9 Production Certificates for mTLS*](https://knowledge.digicert.com/general-information/community-root-authority-certificates#X9Certificates "").

Set Up Tasks
------------

You must complete these tasks to enable mutual authentication:
1. Create a new key pair and Certificate Signing Request, using a server-to-server certificate from your CA.
2. Submit the Certificate Signing Request (CSR) to support for your CA and provide the required details.
3. Your CA verifies your request, and if they approve it, they issue the certificate in an email to the technical contact for your account.
4. Give the certificate's common name to your `Cybersource` technical contact. Your technical contact adds it to the `Cybersource` whitelist. IMPORTANT Your certificate's common name can only contain up to 40 characters.  
   To test your own application, you can use the certificate that is available with the `Cybersource` sample application code, hosted on [Github](https://github.com/CyberSource/cybersource-oauth-samples-node "").

Register Your Application {#register-application_id19818H0H0HT}
===============================================================

Before you can use OAuth credentials to connect to `Cybersource`, you must register your application in the `Business Center`. To obtain credentials, contact `Cybersource` support:  
[contact-us.html](https://developer.cybersource.com/support/contact-us.md "")

1. Log in to the `Business Center`:
   * Test: [`https://businesscentertest.cybersource.com`](https://businesscentertest.cybersource.com/ebc2/ "")
   * Production: [`https://businesscenter.cybersource.com`](https://businesscenter.cybersource.com/ebc2/ "")
2. Click Account Management in the left-navigation menu and choose Authorized Applications. The OAuth Authorized Applications page appears.{#register-application_step_2}
   {#register-application_step_2}
3. Click Add Application. You must use an administrator account to add or change an application.{#register-application_step_3}
   {#register-application_step_3}
4. Enter this information:
   * Name of the application that you are registering.
   * Description of the application.
   * URL to redirect the merchant to your system after they grant permissions. For more information about the redirect, see [Redirecting the Merchant to `Cybersource`](/docs/cybs/en-us/oauth/developer/all/rest/oauth/redirect-merchant-to-cybs.md#redirect-merchant-to-cybs "").
   * Choose permissions for individual APIs or for all listed APIs.
     {#register-application_step_4}
     {#register-application_step_4}
5. Click Save.  
   Your application is registered, and your application's client ID and client secret are shown. You will need them in order to redirect the merchant. Treat the client ID and client secret as confidential information and store them securely. You can regenerate your client secret if you misplace it or if its security is compromised. {#register-application_step_5}
   {#register-application_step_5}
6. Click Done to return to the previous page.{#register-application_step_6}
   {#register-application_step_6}

Redirect the Merchant {#redirect-merchant-to-cybs_id1981903J030}
================================================================

Your application must redirect the merchant to `Cybersource` so that the merchant can log in with their `Cybersource` credentials and provide permissions for your application.
IMPORTANT A merchant giving permissions to your application must log in as an Account Owner or Account Administrator.  
After the merchant provides or denies permissions for your application, `Cybersource` redirects the merchant to the redirect URL that you provided when you registered. If the merchant attempted to grant permissions using an account with insufficient privileges, the redirect response is the same as when a merchant denies permission.  
When you redirect the merchant to `Cybersource`, encode the URL with the following parameters as a query string:

| Parameter Name | Required | Notes                                                                                                                                                                                                                               |
|:---------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sub            | Yes      | Must be set to `oauth`.                                                                                                                                                                                                             |
| client_id      | Yes      | The client ID that you received when you registered your application in the `Business Center`.                                                                                                                                      |
| redirect_url   | Yes      | The page to which `Cybersource` redirects the merchant after the merchant grants your application permissions. The value of the `redirect_url` parameter must exactly match the redirect URL that you supplied during registration. |
| state          | No       | Value that is sent in the response to prevent malicious interception, such as a CSRF attack.                                                                                                                                        |
[URL-Encoded Query Parameters in Your Redirect]

{#redirect-merchant-to-cybs_URL_encoded_query_parameters} Sample Redirect for Testing

```keyword
https://businesscentertest.cybersource.com/ebc2/oauth/authorize?sub=oauth&redirect_url=
https://www.example.com&client_id=yourClientId&state=StateValue
```

Sample Redirect for Production

```keyword
https://businesscenter.cybersource.com/ebc2/oauth/authorize?sub=oauth&redirect_url=
https://www.example.com&client_id=yourClientId&state=StateValue
```

Interpreting the Redirect Response {#response-parameters_id198190C0FXW}
=======================================================================

After your application redirects the merchant to `Cybersource`, this sequence occurs.

1. Merchants not logged in to the `Business Center` at the time of the redirect are prompted to do so. Merchants with expired credentials are prompted to reset them, after which they must click the redirect link again.

2. The `Business Center` page opens, stating the partner's name along with the permissions that the partner is requesting from the merchant. If the merchant logged in using an account with sufficient privileges, the they are prompted to choose Allow or Deny. If the logged-in user does not have sufficient privileges, the Allow button is disabled.

3. If the merchant clicks Deny, `Cybersource` redirects the merchant to the URL that you defined in your `redirect_url` parameter with no parameters appended to it. This is not a failure but a denial of permission by the merchant's representative. The denial does not prohibit any future attempt for this or any merchant.

   4. When the merchant clicks Allow, `Cybersource` redirects the merchant to the URL that you defined in your `redirect_url` parameter.  
      The redirect URL in the `Cybersource` response is encoded with at least one of these parameters:

   | Parameter | Description                                                                                                                                                                                                                                                                                    |
   |:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `code`    | The authorization code that your application sends to `Cybersource` when requesting an access token (during the next step of the authentication process). For security reasons, the authorization code expires in ten minutes. If it expires, you must repeat the redirect to request another. |
   | `state`   | This parameter is returned only if it was submitted in the request. It is used to test for possible CSRF attacks. If the state values from the request and response do not match, you could be the victim of a CSRF attack, and you should display an HTTP 401 error code in response.         |

Request the Access and Refresh Tokens {#obtaining-access-refresh-tokens_id198190V0OX4}
======================================================================================

Use the authorization code from the redirect response to request an initial access token, as well as a refresh token, from the `/oauth/v3/token` endpoint. While a header is not required, we recommend including the header `v-c-client-correlation-id` with a unique value for every request to the `/oauth/v3/token` endpoint. For security, all parameters must be sent in the body and use the HTTPS protocol. Do not place any parameters in the URL.

* Test URL: [api-matest.cybersource.com](https://api-matest.cybersource.com "")
* Production URL: [api-ma.cybersource.com](https://api-ma.cybersource.com "")

Sample Token Request

```
POST https://api-ma.cybersource.com/oauth2/v3/token
Content-Type: application/x-www-form-urlencoded

client_id=8l57hYffFb&grant_type=refresh_token&code=eyJraK&client_secret=yourClientSecret
```

| Parameter Name | Value                                                        | Description                                                                                                                           |
|:---------------|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| grant_type     | Set to `authorization_code`.                                 | Required. Determines which type of flow the Authorization Server uses to acquire user authorization.                                  |
| code           | The authorization code received from the redirect response.  | Required. The value passed in this parameter must exactly match the value supplied by the OAuth server during the authorization step. |
| client_id      | The client ID obtained during client registration.           | Required. Indicates the client that is making the request.                                                                            |
| client_secret  | The client secret value obtained during client registration. | Required. You received this value when you registered your application with `Cybersource`.                                            |
[Access Token Request Parameters]

{#obtaining-access-refresh-tokens_access_token_request_params} Sample Response for Access Token Request

```
HTTP/1.1 200 OK 

Content-Type: application/json;charset=UTF-8 

Cache-Control: no-store 

Pragma: no-cache 

{ 

"access_token": "eyJraWQiOiIxMGM2MTYxNzg2MzE2ZWMzMGJjZmI5ZDcyZGU4MzFjOSIsImFsZyI6IlJTMjU2In0.
 eyJqdGkiOiI5YTM0MWVkZC0zY2ViLTRiMzYtYjQyMy05MDg4ZTliYWQ1YTAiLCJzY29wZXMiOlsiYWx0ZXJuYXRlX3B
 heW1lbnRzIiwiYmFua190cmFuc2ZlcnMiLCJib2FyZGluZyIsImNvbW1lcmNlX3NlcnZpY2VzIiwiZnJhdWRfbWFuYW
 dlbWVudCIsImludm9pY2luZyIsImtleXMiLCJtYW5hZ2Vfc2VjdXJlX2FjY2VwdGFuY2UiLCJwYXltZW50c193aXRoX
 3N0YW5kYWxvbmVfY3JlZGl0IiwicGF5bWVudHNfd2l0aG91dF9zdGFuZGFsb25lX2NyZWRpdCIsInBheW91dHMiLCJy
 ZXBvcnRpbmciLCJ0b2tlbml6YXRpb25fc2VydmljZXMiLCJ0cmFuc2FjdGlvbnMiLCJ1c2VycyJdLCJpYXQiOjE2MTk
 1MTg3MzY4OTUsImFzc29jaWF0ZWRfaWQiOiJzYW1wbGVwYXJ0bmVyIiwiY2xpZW50X2lkIjoidjZUSkgxSXFoTSIsIm1
 lcmNoYW50X2lkIjoicmFodWxyYW1hIiwiZXhwaXJlc19pbiI6MTYxOTUxOTYzNjg5NSwiZ3JhbnRfdHlwZSI6ImF1dGh
 vcml6YXRpb25fY29kZSIsImdyYW50X3RpbWUiOiIyMDIxMDQyNzAzMTgifQ.jhjH9_xxleoNKgidD9oduVuUqDGov2X6
 22gzh99_QeocFc-7KsndsdaaUqglRpfY8juCbtRIe8RhLa5_hIoKF3ZU3XJ4WnQeAXdbznjf0SfK2SHpih-Tl2u_Ufsl
 Q7WjJM3OVDRcV3udMKfe6ACX0_uH81vRobRK43kk1RjrKuQSWz6KRRmSGrHJWl2sbo0gdEQEZpnGQwVcJuGKYalOk6Xq
 vglu2nD7iNyZpaaXOJHVDqxNdQdz8vfkofBPFVcTMjx8cHge3gDOFWDce5-TIU2EGdD_nUUfh8OfXaMrvv6nBriKzG96
 j7SQm3BXfwfm6SzSIyBpiti3sgwGJs-vGA", 

"token_type": "bearer", 

"refresh_token": "eyJraWQiOiIxMGM2MTYxNzg2MzE2ZWMzMGJjZmI5ZDcyZGU4MzFjOSIsImFsZyI6IlJTMjU2In0.
 eyJqdGkiOiJmMTA2YjU1Yy00MjA1LTRjZDctOTkzNy04MzM3YTdjNmZmYWMiLCJzY29wZXMiOlsiYWx0ZXJuYXRlX3Bhe
 W1lbnRzIiwiYmFua190cmFuc2ZlcnMiLCJib2FyZGluZyIsImNvbW1lcmNlX3NlcnZpY2VzIiwiZnJhdWRfbWFuYWdlbW
 VudCIsImludm9pY2luZyIsImtleXMiLCJtYW5hZ2Vfc2VjdXJlX2FjY2VwdGFuY2UiLCJwYXltZW50c193aXRoX3N0YW5
 kYWxvbmVfY3JlZGl0IiwicGF5bWVudHNfd2l0aG91dF9zdGFuZGFsb25lX2NyZWRpdCIsInBheW91dHMiLCJyZXBvcnRp
 bmciLCJ0b2tlbml6YXRpb25fc2VydmljZXMiLCJ0cmFuc2FjdGlvbnMiLCJ1c2VycyJdLCJpYXQiOjE2MTk1MTg3MzY4O
 DksImFzc29jaWF0ZWRfaWQiOiJzYW1wbGVwYXJ0bmVyIiwiY2xpZW50X2lkIjoidjZUSkgxSXFoTSIsIm1lcmNoYW50X2
 lkIjoicmFodWxyYW1hIiwiZXhwaXJlc19pbiI6MTY1MTA1NDczNjg4OCwidG9rZW5fdHlwZSI6InJlZnJlc2hfdG9rZW4
 iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiZ3JhbnRfdGltZSI6IjIwMjEwNDI3MDMxOCJ9.Sj5y5ld
 pM4-ie5YT6_ARu6H0Ikd7jOhNvKsWgDB5NTxHvbyS5ciMidAIvxoxOXS_0vPpf1u865w8Qu8yT82iHHbNxyjjBXy03wbS
 utJBen_5roFUi6XE7KFgZPKL2hixmRVgivTrA8uAZ798Griv0PUOPnm6y6AzmK1ffmwdSNejKBdvz3_38TLLJk_0ylkRp
 D9akM8bSpDMSJJLNd3_eER5jdOQWRlqgaC030crrksS7o-vFJxXsK3MN0-_qnVqV5-l-8vhjJ0VUzg66eUgIyphIzU2c0
 M2J9d5tJVncHqOFz8N8HUZ800xKxMKH1MlB7F3L8alJJ04Jk6edT0KXA", 

"expires_in": 899, 

"scope": "transactions", 

"refresh_token_expires_in": 31535999, 

"client_status": "active" 

} 
```

| Error Code             | Description                                                                                                                                                                                                                                      |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `access_denied`        | The resource owner or authorization server denied the request.                                                                                                                                                                                   |
| `server_error`         | The authorization server encountered an unexpected condition that prevented it from fulfilling the request. This error code is needed because a 500 Internal Server Error HTTP status code cannot be returned to the client by an HTTP redirect. |
| `invalid_scope`        | The requested scope is invalid, unknown, or malformed.                                                                                                                                                                                           |
| `invalid_client`       | The requested client ID is invalid, unknown, or malformed.                                                                                                                                                                                       |
| `invalid_request`      | The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.                                                                                                |
| `unauthorized_client`  | The client is not authorized to request an authorization code.                                                                                                                                                                                   |
| `invalid_redirect_uri` | The requested redirect URI is invalid, unknown, or malformed.                                                                                                                                                                                    |
| `client_not_found`     | The requested client ID is not found in the system.                                                                                                                                                                                              |
| `invalid_client_type`  | The requested client ID is registered with an invalid client type (only confidential clients are supported).                                                                                                                                     |
| `merchant_not_active`  | The authorization could not be completed because the merchant's `Cybersource` account is inactive.                                                                                                                                               |
| `client_not_active`    | The authorization could not be completed because your `Cybersource` Partner Account is not currently listed as active. Contact customer support for assistance.                                                                                  |
[Error Responses for Token Request]

{#obtaining-access-refresh-tokens_token_request_error_responses}

Submit API Requests Using OAuth {#submitting-api-request-using-cybs-extend_id1981950047U}
=========================================================================================

You can submit API requests on behalf of the merchant using the access token. The access token expires after 15 minutes.  
Include the access token in the `Authorization` header as shown below.

> IMPORTANT
> Not all API endpoints are currently enabled for OAuth. For a list of OAuth-enabled endpoints, contact ` Cybersource ` support:  
> ` `[contact-us.html](https://developer.cybersource.com/support/contact-us.md "")` `
> Example: Authorization Header with Access Token

```
Authorization: Bearer eyJraWQiOiIyNmRjfjVkZTdlMmYwYTI0ODg0MjU1YjIwZWJjMGY0MSIsImFs

curl -X POST -H "Authorization: Bearer ACCESS_TOKEN""https://api-ma.cybersource.com/pts/v2/payments" 
```

Error Response {#error-response_id1981970102L}
==============================================

If the token is expired or the user is unauthorized, the API responds with a 401 HTTP status code. Expired Token

```
{
  "response": {
    "rmsg": {
      "error":"ACCESS_TOKEN_EXPIRED",
      "error_description":"ACCESS_TOKEN_EXPIRED
    }
  }
}
```

Unauthorized Partner

```
{
  "response": {
    "rmsg": {
      "error": "UNAUTHORIZED_PARTNER",
      "error_description": "UNAUTHORIZED_PARTNER"
    }
  }
}
```

Refresh the Access Token {#refreshing-access-token_id19819A0I0L7}
=================================================================

Access tokens expire after 15 minutes and refresh tokens expire after a year. To refresh the access token using the refresh token, follow the example below. We recommend including the header `v-c-client-correlation-id` with a unique value for every request to `/token`.  
Any token request failure results in an HTTP status code of `500 Server error`. Correct any errors and resend. Request to Refresh the Access Token

```
POST https://api-ma.cybersource.com/oauth2/v3/token 
Content-Type: application/x-www-form-urlencoded
 client_id=8l57hYffFb&client_secret=yourClientSecret&grant_type=refresh_token&refresh_token
  =eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCIsImFsZyI6IlJTMjU2In0.eyJqdGkiOiI0N2E4OGY0
   MS04ZTI5LTRhMTQtOWZlYi0wZjM0OTM2ZDk0M2QiLCJzY29wZXMiOlsicmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6
   MTQ3MTU3MDEyODQ5OCwiY2xpZW50X2lkIjoiOGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1MzY4IiwiZXhwaXJlc19p
   biI6MTQ3MTU5ODkyODQ5OH0.lDvGlZvjkgY5pcJEG5Y1d6o7mOiZA-up2MsGm6zVhZdZxiSDt7md7Ih4_Lkko63_-Fz6UXMg
   7SLt6ypVJqn3u2iqKRy8aiuSxhQCwAuenoqFFdsFEEqlqkEtDZeo6B3_YrrTeCdjyP_cpLf7vr9GKJS3k5snYGhL8sZrEQMx
   JaQsyz6F_IPrxajmMiLt4nJUJJgRTjF-krt8p-BBLGxOYCBXe8UPrpsmLnxlEPiwJcFYREimEMSkeD2uDShWXe-ociLWFtoX
   mYx50TDk_fx2hKRaOVHtnaQJdsgtnQrlc0UkFAOzp9fU45O2Vei7x8SPNA47NdoR1XmPK2ZnXm_TIA
```

Response from Refresh Request

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
"access_token": "eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCIsImFsZy
I6IlJTMjU2In0.eyJqdGkiOiI0Y2E5NGUyNy04NzkzLTRmOGQtYjY4YS01OWM0MjMwODlhZDAiLCJzY
29wZXMiOlsicmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6MTQ3MTU3MDE5NjM0MiwiY2xpZW50
X2lkIjoiOGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1MzY4IiwiZXhwaXJlc19pbiI6MTQ3MTU
5ODk5NjM0Mn0.cmYor7iW6lxRCiM3kWPKauMsiKNGwRrrRFKowcTdkRQewqbQ0Mn9As1RhZwDKL4dux
CzAzLw4e8aV8PUyd2-_eCUsqbPMWLWjGo75eU8GI9rrvSGTxEP-fr6jPAr-jBJekQTzMLgkKVtSGaJg
tz08dHqrJnrejR8rZs4h1GpPMk6i99cOVMHjuTV7ZzognvkLKj_OR01H4XK5M8TWH5uoAXWrII3K-JJ
V1YkzjpVkpS0tVXTIXJI-pk_eNeBaJ7Q6in9X3xQKXnIqA8I8zxZt3LNnxR-aui2yufzP5BDh2kfwU0
B1Uq8fEuqNmbj4HN1NrmnTHkRJTZ4ooYoqAQtnQ",

"token_type": "bearer",

"refresh_token": "eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCIsImFsZ
yI6IlJTMjU2In0.eyJqdGkiOiI4N2IxNDg2MC03YzI0LTQ0NmQtOWJlYS05Mzk2ZDI3MmNmOWQiLCJz
Y29wZXMiOlsicmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6MTQ3MTU3MDE5NjMyMywiY2xpZW5
0X2lkIjoiOGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1MzY4IiwiZXhwaXJlc19pbiI6MTQ3MT
U5ODk5NjMyM30.Fn8ZlXgvGBr-uvDi6e7-72g8tP-u42T5FNW5NW4YQ7GkrMqUEthexGc9NOcf6uWYf
SD4EiSbDVO8EIojZzIUgyXmG3tYDgSejFcDSPcMrF11m9WkOcapbIFTnFk2OyPVi48BVZ6vNb7j2184
pJ3KHKoq9E7qlaKrEbvBn2HRVdtvb1yj1Xv1tH38I6Qong8xMAEMCcIfzTinEOFIbENYzgxBsSNVrS1
5CYtDRFEDPGmAVPzd4I7HN_ed-pzOET3YbUBBQUbrAuZSrSrBcgfBCtT9C5szd7tYXmi-1AMVdFybnV
XArAXsDX0nZzm-PuCi_DGKMJET0sY2QNyesyKv8w",

"expires_in": 28798,

"scope": "payments_with_standalone_credit",

"refresh_token_expires_in": 28799,

"client_status": "active"
      
```

Refresh the Refresh Token {#refreshing-the-refresh-token}
=========================================================

Access tokens expire after 15 minutes and refresh tokens expire after a year. Merchants are not required to reapprove access after a year; the refresh token's expiration resets to one year after the last successful access token request. You are not required to use an authorization code to make this call.  
Below is an example of a request to obtain a new refresh token. We recommend including the header `v-c-client-correlation-id` with a unique value for every request to the `/token` endpoint.  
Any token request failure results in an HTTP status code of 500 - Server error. Correct any errors and resend.   
We provide a 6-month grace period to request a new refresh token. The new refresh token will expire one year from the last refresh token request. If the merchant has not had any activity within that grace period, they must be prompted to [grant authorization and delegate access](/docs/cybs/en-us/oauth/developer/all/rest/oauth/redirect-merchant-to-cybs.md ""). Request to Refresh the Refresh Token

```
POST https://api-ma.cybersource.com/oauth2/v3/token 

Content-Type: application/x-www-form-urlencoded 

client_id 
=8l57hYffFb& 

client_secret 
=yourClientSecret& 

grant_type 
=refresh_token& 

refresh_token 
=eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCIsImFsZyI6IlJTMjU2In0.
 eyJqdGkiOiI0N2E4OGY0MS04ZTI5LTRhMTQtOWZlYi0wZjM0OTM2ZDk0M2QiLCJzY29wZXMiOlsi
 cmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6MTQ3MTU3MDEyODQ5OCwiY2xpZW50X2lkIjoi
 OGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1MzY4IiwiZXhwaXJlc19pbiI6MTQ3MTU5ODky
 ODQ5OH0.lDvGlZvjkgY5pcJEG5Y1d6o7mOiZA-up2MsGm6zVhZdZxiSDt7md7Ih4_Lkko63_
 -Fz6UXMg7SLt6ypVJqn3u2iqKRy8aiuSxhQCwAuenoqFFdsFEEqlqkEtDZeo6B3_YrrTeCdjyP_
 cpLf7vr9GKJS3k5snYGhL8sZrEQMxJaQsyz6F_IPrxajmMiLt4nJUJJgRTjF-krt8p-BBLGxOYCB
 Xe8UPrpsmLnxlEPiwJcFYREimEMSkeD2uDShWXe-ociLWFtoXmYx50TDk_fx2hKRaOVHtnaQJdsg
 tnQrlc0UkFAOzp9fU45O2Vei7x8SPNA47NdoR1XmPK2ZnXm_TIA 
```

Response from Refreshing the Refresh Request

```
HTTP/1.1 200 OK 

Content-Type: application/json;charset=UTF-8 

Cache-Control: no-store 

Pragma: no-cache 

{ 

"access_token": "eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCI
 sImFsZyI6IlJTMjU2In0.eyJqdGkiOiI0Y2E5NGUyNy04NzkzLTRmOGQtYjY4YS01OWM0Mj
 MwODlhZDAiLCJzY29wZXMiOlsicmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6MTQ3M
 TU3MDE5NjM0MiwiY2xpZW50X2lkIjoiOGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1
 MzY4IiwiZXhwaXJlc19pbiI6MTQ3MTU5ODk5NjM0Mn0.cmYor7iW6lxRCiM3kWPKauMsiKN
 GwRrrRFKowcTdkRQewqbQ0Mn9As1RhZwDKL4duxCzAzLw4e8aV8PUyd2-_eCUsqbPMWLWjG
 o75eU8GI9rrvSGTxEP-fr6jPAr-jBJekQTzMLgkKVtSGaJgtz08dHqrJnrejR8rZs4h1GpP
 Mk6i99cOVMHjuTV7ZzognvkLKj_OR01H4XK5M8TWH5uoAXWrII3K-JJV1YkzjpVkpS0tVXTIXJI-pk_
 eNeBaJ7Q6in9X3xQKXnIqA8I8zxZt3LNnxR-aui2yufzP5BDh2kfwU0B1Uq8fEuqNmbj4HN1NrmnTHkRJTZ4ooYoqAQtnQ", 

"token_type": "bearer", 

"refresh_token": "eyJraWQiOiI4MGI2ZDJjM2NkZGRkMmY2NmY3MmRjYjIyMmZiNGM1MCI
 sImFsZyI6IlJTMjU2In0.eyJqdGkiOiI4N2IxNDg2MC03YzI0LTQ0NmQtOWJlYS05Mzk2ZDI
 3MmNmOWQiLCJzY29wZXMiOlsicmVhZCIsIndyaXRlIiwiZGVsZXRlIl0sImlhdCI6MTQ3MTU
 3MDE5NjMyMywiY2xpZW50X2lkIjoiOGw1N0lZZmZGYiIsIm1lcmNoYW50X2lkIjoiMzI1MzY
 4IiwiZXhwaXJlc19pbiI6MTQ3MTU5ODk5NjMyM30.Fn8ZlXgvGBr-uvDi6e7-72g8tP-u42T
 5FNW5NW4YQ7GkrMqUEthexGc9NOcf6uWYfSD4EiSbDVO8EIojZzIUgyXmG3tYDgSejFcDSPc
 MrF11m9WkOcapbIFTnFk2OyPVi48BVZ6vNb7j2184pJ3KHKoq9E7qlaKrEbvBn2HRVdtvb1y
 j1Xv1tH38I6Qong8xMAEMCcIfzTinEOFIbENYzgxBsSNVrS15CYtDRFEDPGmAVPzd4I7HN_
 ed-pzOET3YbUBBQUbrAuZSrSrBcgfBCtT9C5szd7tYXmi-1AMVdFybnVXArAXsDX0nZzm-PuCi_DGKMJET0sY2QNyesyKv8w", 

"expires_in": 899, 

"scope": "transactions", 

"refresh_token_expires_in": 31535999, 

"client_status": "active" 

}
```

Revoke Permissions {#revoking-permissions_id1981A080BL7}
========================================================

Merchants can revoke the permissions that they granted to your application. If a merchant revokes your application's permissions in the `Business Center`, any current access token is immediately invalidated, and no new access tokens can be generated. If the merchant decides to grant permissions to your application in the future, they must visit your web-application and begin the permissions process again.

Contact Support {#Contact_id2024I030E5Z}
========================================

If you have questions or are interested in becoming a pilot partner, contact `Cybersource` support:  
[contact-us.html](https://developer.cybersource.com/support/contact-us.md "")
