# Source: https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started.md

Getting Started with REST Developer Guide {#product-about-guide}
================================================================

This section describes how to use this developer guide and where to find further information.  
Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional technical documentation.

Audience and Purpose
:
This guide provides information about how to sign up for a sandbox account and set up the `Payment Gateway` REST API.

Customer Support
:
For support information about any service, visit the Support Center:

[http://support.example.com](https://support.example.com/ "")

Recent Revisions to This Document {#restgs-doc-revisions}
=========================================================

26.06.01
--------

Added the request-host field to the required JWS Body Claims table. If you are using a P12 certificate, see Step 3C in [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md ""). If you are using a shared secret key pair, see Step 3C in [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-con-shared-secret-intro.md "").

26.05.01
--------

This revision contains only editorial changes and no technical updates.

26.04.01
--------

How to Set Up Your `Payment Gateway` Account
:
Updated the set up graphic to support the new SDK integration method. See [How to Set Up REST](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-setup-workflow.md "").

Construct Messages Using JSON Web Tokens
:
Updated the body claim field descriptions for the exp, iss, and request-resource-path fields.
:
Updated the JWS body claim field descriptions to include lowercase format requirements.

    For both updates, see Step 3C in [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "") using a P12 certificate and the [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-con-shared-secret-intro.md "") using a shared secret key pair.

Enable Message-Level Encryption
:
Updated the prerequisites list for enabling Messagel-Level Encryption (MLE). See the Prerequisites for MLE section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "") using P12 certificates and [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-mle-shared-secret-intro.md "") using shared secret key pairs.
:
Corrected the spelling for all mentions of the v-c-response-mle-kid body claim field throughout guide.

SDK Integration
:
Added new SDK integration section. See [Set Up a JSON Web Token Message Using the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro.md "").

26.02.01
--------

Added new section that explains how to migrate from HTTP signature messaging to JWT messaging using a shared secret key pair. See [Set Up a JSON Web Token Message Using Shared Secret Key Pairs](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro.md "").  
Added a warning note with the deprecation deadline for HTTP signature messaging. See [Set Up an HTTP Signature Message](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "").

26.01.01
--------

This revision contains only editorial changes and no technical updates.

Introduction to REST {#restgs-intro}
====================================

To get started using `Payment Gateway` APIs, you must first set up your system to be REST-compliant. `Payment Gateway` uses REST for developing web services. REST enables your system to exchange request and response messages with the `Payment Gateway` gateway using HTTP. This guide explains how to set up secure messaging using *JSON Web Tokens* or *HTTP Signature Security*.  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rest-api-overview-pgw-720x170.svg/jcr:content/renditions/original)

**JSON Web Token Messaging**
:
JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. Depending on your integration, you can sign your tokens with a certificate private key or a shared secret key. The signature is calculated from the JWS header and payload, which enables the receiver to verify that the content has not been tampered with.

    > WARNING  
    > As of **February 2026** , there are new requirements for constructing JWTs. This update also requires you to encrypt and decrypt messages using Message-Level Encryption (MLE). To remain compliant, you must update how your system constructs JWTs with MLE by **September 2026**. If you do not update your system before the September deadline, you risk transaction failure. Use this guide to update your system.

HTTP Signature Security Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original)
:
With HTTP Signature messaging, each request is digitally signed using a shared secret. This enables both the client and the server to validate the authenticity and integrity of the request. If a request is intercepted during transmission, an attacker cannot modify it or impersonate the sender without the shared secret key. HTTP Signature messaging can be used only with API requests and cannot be used in browser-based or mobile applications.

    > WARNING  
    > By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.

![](/content/dam/documentation/pgw/en-us/common/images/warning-red-24x24.svg/jcr:content/renditions/original) Fraud Prevention and Security Responsibilities
-------------------------------------------------------------------------------------------------------------------------------------------------------------

When setting up your connection to the `Payment Gateway` gateway, verify that you have implemented controls to prevent card testing and card enumeration attacks on your platform. For more information, see the [best practices guide](https://www.example.com/content/dam/documents/en/payment-card-testing-bot-attacks.pdf "").  
If `Payment Gateway` detects suspicious transaction activity associated with your merchant ID, including card testing or card enumeration attacks, `Payment Gateway` reserves the right to enable fraud management tools on your behalf to help mitigate the attack. The fraud team might also implement internal controls that block traffic perceived as fraudulent.  
If you are already using a `Payment Gateway` fraud tool and experience a significant attack, `Payment Gateway` internal teams might modify or add rules to your configuration to help reduce the threat to both your business and `Payment Gateway` infrastructure. However, these actions do not replace your responsibility to follow industry-standard best practices to protect your systems, servers, and platforms.

How to Set Up REST {#restgs-setup-workflow}
===========================================

This overview lists the tasks you must complete in order to set up your Payment Gateway account for sending and receiving REST API messages using JSON Web Token (JWT) messaging.  
You can choose from these set up methods:

* JWT messaging using a *P12 certificate*.
* JWT messaging using a *shared secret key pair*.
* JWT messaging using the *REST Client SDK*.
  {#restgs-setup-workflow_ul_gwz_r3x_s3c}

#### Figure:

Set Up Your Payment Gateway Account ![If you are using a custom integration, follow these steps. Step 1: Create a
test account. Step 2: Choose and create your security type using a P12
certificate or shared secret key pair. Step 3: Construct a message with JSON
Web Tokens. Step 4: Enable Message-Level Encryption (MLE). Step 5: Test your
setup. Step 6: Go live. If you are using an SDK integration, follow these
steps. Step 1: Create a test account. Step 2: Choose and create your
security type using a P12 certificate or shared secret key pair. Step 3:
Import an SDK that constructs messages using JSON Web Tokens and
Message-Level Encryption. Step 5: Test your setup. Step 6: Go live.](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-overview-750x635.svg/jcr:content/renditions/original)  
To set up JSON web token messaging using *P12 certificates* , see [Set Up a JSON Web Token Message Using P12 Certificates](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "").  
To set up JSON web token messaging using *shared secret key pairs* , see [Set Up a JSON Web Token Message Using Shared Secret Key Pairs](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro.md "").  
To set up JSON web token messaging using the *REST Client SDK* , see [Set Up a JSON Web Token Message Using the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro.md "").

HTTP Signature Security ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original) {#restgs-setup-workflow_section_wkh_3kx_s3c}
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You also have the option to set up your Payment Gateway account for sending and receiving messages using HTTP signature security.  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-http-deprecating-550x120.svg/jcr:content/renditions/original)

> WARNING  
> By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.  
> To set up HTTP signature messaging, see [Set Up an HTTP Signature Message](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "").

Set Up a JSON Web Token Message Using P12 Certificates {#restgs-jwt-message-intro}
==================================================================================

To set up JSON Web Token messaging using a *P12 certificate*, you must complete the tasks described in this section.

#### Figure:

Setting Up JSON Web Token a Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-all-750x175.svg/jcr:content/renditions/original)

1. Sign up for a test account. See [Sign Up for a Sandbox Account](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-register.md "").
2. Create a P12 certificate. See [Create or Submit a P12 Certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md "").
3. Construct a message using a JSON Web Token. See [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "").
4. Enable message-level encryption (MLE) to encrypt all messages. See [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "").
5. Go live by transitioning your sandbox account into a production account. See [Going Live](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-go-live-intro.md "").

Sign Up for a Sandbox Account {#restgs-register}
================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-1-750x175.svg/jcr:content/renditions/original)  
To begin setting up your account, you must first sign up for a sandbox account. A sandbox account enables you to obtain your security keys and test your implementation.

> IMPORTANT  
> A sandbox account cannot process live payments and is intended for only testing.  
> Follow these steps to sign up for a sandbox account:

1. Go to the `Payment Gateway` Developer Center sandbox account sign-up page:  
   [https://developer.example.com/hello-world/sandbox.html](https://developer.example.com/hello-world/sandbox.md "")

   2. Enter your information into the sandbox account form, and click **Create Account**.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-registration.png/jcr:content/renditions/original)
   3. Go to your email and find a message titled: *Merchant Registration Details* . Click **Set up your username and password now**.  
      Your browser opens the New User Sign Up wizard.
   4. Enter the organization ID and contact email you supplied when you created your account. Follow the wizard pages to add your name, a username, and a password. Your username and password must meet these requirements:

   |                                        **Username Requirements**                                        |                                                                                  **Password Requirements**                                                                                   |
   |---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | * Length must be 3-36 characters. * Can only contain letters, numbers, periods, dashes, or underscores. | * Length must be 12--50 characters. * Must contain one upper case letter. * Must contain one lower case letter. * Must contain one number. * Cannot contain the username or organization ID. |
   [Username and Password Requirements]

   5. Log in to the `Business Center`.  
      When you log in for the first time, you must verify your identity through a system-generated email sent to your email account.
2. Check your email for a message titled: *`Payment Gateway` Identification Code*. A passcode is included in the message.

   7. Enter the passcode on the *Verify your Identity* page.  
      You are directed to the `Business Center` home page.  
      You have successfully signed up for a sandbox account.

   > IMPORTANT  
   > A sandbox account cannot process live payments. After you verify that your system can send and receive REST messages, you can contact customer service to transition your sandbox account to a production account.

Create or Submit a P12 Certificate {#restgs-security-p12-intro}
===============================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-2-750x175.svg/jcr:content/renditions/original)  
This section describes how to create or submit a P12 certificate, extract the certificate's *private key*, and test the private key to verify that it works. A private key is necessary for you to construct JSON Web Tokens (JWTs).  
You can choose to create or submit a P12 certificate. *Create* a P12 certificate if you need a new certificate. *Submit* a P12 certificate if you want to use your own certificate.

(Optional) Meta Keys
:
If you are using a portfolio or merchant account, you have the option to create a *meta key* of a P12 certificate. Meta keys enable an organization administrator to assign a single P12 certificate to some or all transacting merchants in their organization. The purpose of a meta key is to reduce the time needed to manage an organization's keys. For example, by assigning the same meta key to all of your transacting merchants, you only need to update one key when it expires instead of having to update each transacting merchant's key.
:
For more information about meta keys, see the [Meta Key Creation and Management](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") section in the *Creating and Using Security Keys User Guide*.
{#restgs-security-p12-intro_metakeys-dl}

Step 2A: Create or Submit a P12 Certificate {#restgs-task-p12}
==============================================================

Follow these steps to create a P12 certificate file or submit your own certificate signing request (CSR):

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
   4. Under REST APIs, choose REST -- Certificate, and then click Generate key.  
      The Key Generation page appears.  
      If you are using a *portfolio* account, the Key options window appears, giving you the choice to create a meta key. For more information about how to create a meta key, see *[Creating and Using Security Keys](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "")*.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-select.png/jcr:content/renditions/original)
2. (Optional) You can set the Certificate Expiry Timeframe field to the number of months you want the key to remain active before it expires. Only whole numbers from 1--36 are accepted. By default, new keys expire after 12 months.
3. Choose from these two options:
   1. If you are a creating a new P12 Certificate, click Download key ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-blank.png/jcr:content/renditions/original)
   2. If you are submitting your own certificate, enter your public PEM-formatted certificate in the text box, then click Download key ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-fill.png/jcr:content/renditions/original)
      {#restgs-task-p12_step-5}
      {#restgs-task-p12_step-5}
   3. Create a password for the certificate by entering one into the New Password and Confirm Password fields. Click Generate key.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
      The *.p12* file downloads to your desktop.  
      If prompted by your system, approve the location to which the key downloads. {#restgs-task-p12_step-6}
      {#restgs-task-p12_step-6}

{#restgs-task-p12_steps}  
To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

> IMPORTANT  
> Securely store the *.p12* file and password in your system. These credentials are required in order to implement certain products, and you must be able to access them.

Step 2B: Extracting the Private Key from Your P12 Certificate {#restgs-security-extract-key}
============================================================================================

When you have your P12 certificate, extract the private key from the certificate. Use this key to sign your header when sending an API request.

> IMPORTANT  
> If you are using the SDK to establish communication, you do not need to extract the private key from the P12 certificate.

**Prerequisite**
:
You must have a tool such as OpenSSL installed on your system.

**Extract the Private Key**
:
Follow these steps to extract the private key using OpenSSL:

    1. Open the command-line tool and navigate to the directory that contains the P12 certificate.
       2. Enter this command:  
       `openssl pkcs12 -in [certificate name] -nodes -nocerts -out [private key name]`
       3. Enter the password for the certificate.  
       You set this password when you created the P12 certificate in the `Business Center`.

The new certificate is added to the directory with the private key name you supplied in Step 2.

Step 2C: Testing Your Private Key {#restgs_security_test}
=========================================================

After creating your key certificate, you must verify that it can successfully process API requests. This task explains how to test and validate your private key in the Developer Center and the `Business Center`.  
Follow these steps:

1. Go to the Developer Center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "") {#restgs_security_test_step-1}
   {#restgs_security_test_step-1}
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")** .{#restgs_security_test_step-2}
   {#restgs_security_test_step-2}
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **JSON Web Token**.{#restgs_security_test_step-3}
   {#restgs_security_test_step-3}
4. Enter your organization ID in the **Organization** field.{#restgs_security_test_step-4}
   {#restgs_security_test_step-4}
5. Enter your Password in the **Password** field.
6. Click **Browse** and upload your p12 certificate from your desktop.{#restgs_security_test_step-5}
   {#restgs_security_test_step-5}
7. Click **Update Credentials**.  
   A confirmation message states that your credentials are successfully updated.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-cert-test.png/jcr:content/renditions/original) {#restgs_security_test_step-6}
   {#restgs_security_test_step-6}
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.{#restgs_security_test_step-7}
   {#restgs_security_test_step-7}
9. Click **Send**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original) {#restgs_security_test_step-8}
   {#restgs_security_test_step-8}
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "") {#restgs_security_test_step-9}
    {#restgs_security_test_step-9}
11. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.{#restgs_security_test_step-10}
    {#restgs_security_test_step-10}
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original) {#restgs_security_test_step-11}
    {#restgs_security_test_step-11}

Construct Messages Using JSON Web Tokens {#restgs-jwt-const-intro}
==================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-3-750x175.svg/jcr:content/renditions/original) WARNING
As of **February 2026** , there are new requirements for constructing a JWT. This section explains how to update your system to remain in compliance. You must update how your system constructs JWTs by **September 2026** to remain compliant. You risk transaction failure if you do not update your system.  
To construct a message using JWTs, you must set the required HTTP headers, define the JWS header and body claims, calculate the token signature, and combine these elements into a request. This section describes how to create each element and construct the completed JWT message in the following subsections.

#### Figure:

JWT Construction Steps  
![Step 3A: Set the known HTTP header values. Step 3B: Set the JWS header claims.
Step 3C: Set the JWS body claims. Step 3D: Calculate the token signature. Step
3E: Combine the HTTP headers and HTTP message body.](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-jwt-mess-sec-800x500.svg/jcr:content/renditions/original)

JSON Web Token Message Elements {#restgs-jwt-const-elements}
============================================================

A JWT message consists of HTTP headers and an HTTP message body.

**HTTP Message Elements**
:
Your HTTP message header must include these elements:
:

    | HTTP Header Element |                                                                      Description                                                                       |
    |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **content-type**    | Also known as the Multipurpose Internet Mail Extension (MIME) type, this element identifies the media or file type of the resource (application/json). |
    | **host**            | The transaction endpoint. (`api.example.com`)                                                                                                      |
    | **authorization**   | JSON Web Signature (JWS) bearer token.                                                                                                                 |
    [HTTP Message Header Elements]

**HTTP Message Body**
:
Your API request.

Step 3A: Set Known HTTP Headers {#restgs-jwt-message-set-headers}
=================================================================

Set the values for these HTTP header elements. These header values do not require any calculation.

content-type
:
Set to the media or file type resource.

host
:
Set to the endpoint.

Step 3B: Set the JWS Header Claims {#restgs-jwt-message-set-jws-claims}
=======================================================================

You must construct a *JSON Web Signature* (JWS) token. To construct a JWS token, you must first set its header claim values.  
These header claim values do not require calculation.

| Header Field |                                                                                                                                                                                Description                                                                                                                                                                                 |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **alg**      | The asymmetric algorithm you use to sign the token header. These algorithms are supported: * RS256 (default) * RS384 * RS512 * PS256 * PS384 * PS512                                                                                                                                                                                                                       |
| **kid**      | The key ID you use to digitally sign the JWT. It must be registered with the authorizing server. It is the key ID from your P12 certificate. For more information, see [Create or Submit a P12 Certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md ""). |
| **typ**      | The token type. Set to `JWT`.                                                                                                                                                                                                                                                                                                                                              |
[HTTP Message Header Fields]

Step 3C: Set the JWS Body Claims {#restgs-jwt-message-set-jws-body}
===================================================================

After you set the JWS header values, set these JWS body claim values:

|   JWS Body Claim Field    |                                                                                                                                Description                                                                                                                                 | Data Type |               Format                |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------|
| **digest**                | A Base64-encoded hash of the message payload. Do not include the **digest** field if the request message is empty, such as during a GET or DELETE request.                                                                                                                 | String    | Lowercase                           |
| **digestAlgorithm**       | The algorithm used to hash the message payload. The message payload should be hashed using the SHA-256 algorithm. Do not include the **digestAlgorithm** field if the **digest** field is not included.                                                                    | String    | Lowercase                           |
| **exp**                   | The time at which the JWS token expires. > IMPORTANT > Field values cannot exceed two minutes after the message issue date, which is the **iat** field value. This field is an HTTP-date value as defined in RFC7231. For example, 01/01/2020 at 00:02:00 is `1577836920`. | String    | Numeric                             |
| **iat**                   | The date and time at which the message is issued. This field uses a *NumericDate* value as defined in RFC 7519, which is the number of seconds since `1970‑01‑01T00:00:00Z` (Unix epoch). For example, 01/01/2020 at 00:00:00 is `1577836800`.                             | String    | Numeric                             |
| **iss**                   | The issuer identifier for the JWS token. Set to the merchant ID that created the P12 certificate. This value is used to validate the issuer.                                                                                                                               | String    | Lowercase                           |
| **jti**                   | The unique token ID. This value is used for replay prevention. Format the value using UUID version 4. For example: `6643fb9a-8093-47c6-95d3-8d69785b5e62`                                                                                                                  | String    | Lowercase alphanumeric              |
| **request-host**          | The endpoint hostname for the HTTP request, excluding the protocol and path. For example, to send a message to the https://api.example.com`/pts/v2/payments` endpoint, set this field to `api.example.com`.                                                        | String    | Lowercase alphanumeric with periods |
| **request-method**        | The HTTP request method. For example, `post`, `get`, `put`, `patch`, or `delete`.                                                                                                                                                                                          | String    | Lowercase                           |
| **request-resource-path** | The endpoint path for the HTTP request, excluding the domain. For example, to send a message to the https://api.example.com`/pts/v2/payments` endpoint, set this field to `/pts/v2/payments`.                                                                          | String    | Lowercase alphanumeric              |
| **v-c-jwt-version**       | The Relay JWT scheme version number. Set to `2`.                                                                                                                                                                                                                            | String    | Numeric                             |
| **v-c-merchant-id**       | Your `Payment Gateway` transacting merchant ID (MID). If you are a portfolio or merchant account user, set this to the transacting merchant ID you send requests on behalf of.                                                                                                 | String    | Lowercase alphanumeric              |
| **v-c-response-mle-kid**  | The message-level encryption response key ID, also known as the *REST--API Response MLE* key.                                                                                                                                                                              | String    | Lowercase alphanumeric              |
[JWS Body Claims]

The value of the digest JWS claim is a hashed version of the HTTP message body that you must calculate. `Payment Gateway` uses this hash value to validate the integrity of your message body.  
Follow these steps to calculate the digest hash:

1. Generate the SHA-256 hash of the JSON payload (message body).
2. Encode the hashed string to Base64.
3. Add the message body hash to the **digest** JWS body claims.
4. Add the algorithm used to hash the digest in the **digestAlgorithm** JWS body claims.  
   Example: Creating a Message Hash Using the Command Line `shasum` Tool

```keyword
cat &lt;&lt;'EOF' | tr -d '\n' | shasum -a 256
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1MarketSt",
      "locality": "sanfrancisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@pgw.com",
      "phoneNumber": "4158880000"
    }
  }
}
EOF
```

Example: Creating a Message Hash Using the Command Line `base64` Tool

```
echo -n "6ae5459bc8a7d6a4b203e8a734d6a616725134088e13261f5bbcefc1424fc956" | base64
```

Example: Creating a Message Hash Using C#

```
public static string GenerateDigest()
{
    var digest = "";
    var bodyText = "{ your JSON payload }";

    using (var sha256hash = SHA256.Create())
    {
        byte[] payloadBytes = sha256hash.ComputeHash(Encoding.UTF8.GetBytes(bodyText));
        digest = Convert.ToBase64String(payloadBytes);
    }

    return digest;
}
```

Example: Creating a Message Using Java

```
public static String GenerateDigest() throws NoSuchAlgorithmException {
    String bodyText = "{ your JSON payload }";

    MessageDigest md = MessageDigest.getInstance("SHA-256");
    md.update(bodyText.getBytes(StandardCharsets.UTF_8));
    byte[] digest = md.digest();

    return Base64.getEncoder().encodeToString(digest);
}
```

Step 3D: Calculate the JWS Signature {#restgs-jwt-message-conf-token-sig}
=========================================================================

You can now calculate the JSON Web Signature (JWS). The JWS consists of the JWS header and claim set hashes in the following format. They are encrypted with the private key.  
`[JWS Header].[Claim Set]`  
Follow these steps to calculate the signature:

1. Concatenate the JWS header and claim set hash strings with a period character (`.`) between the hashes:  
   `[JWS Header].[Claim Set]` {#restgs-jwt-message-conf-token-sig_step1}
   {#restgs-jwt-message-conf-token-sig_step1}
2. Generate an encoded version of the text file using your private key from the *.p12* certificate. For more information, see [Create or Submit a P12 Certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md ""). {#restgs-jwt-message-conf-token-sig_step2}
   {#restgs-jwt-message-conf-token-sig_step2}
3. Base64-encode the signature output. {#restgs-jwt-message-conf-token-sig_step3}
   {#restgs-jwt-message-conf-token-sig_step3}
4. After calculating the signature, you can construct a complete JWS token by combining the JWS header claims, body claims, and signature.{#restgs-jwt-message-conf-token-sig_step4}
   {#restgs-jwt-message-conf-token-sig_step4}

**Example: Token Signature Hash**

```
YjgwNGIxOTMxMzQ2NzhlYjdiMDdhMWZmYjZiYzUzNzliMTk5NzFmNjAzNWRmMThlNzk0N2NhY2U0YTEwNzYyYQ
```

**Code Example: Encoding the Signature File Using OpenSSL**  
Encode the signature file using the `openssl` tool.

```
openssl rsautl -encrypt -inkey publickey.key -pubin -in [signature-text-file]
					&gt; [signature-encoded-file]
```

**Code Example: Base64 Encoding the Signature File Using the Command Line**  
Encode the signature file using the `openssl` tool and remove any padding.

```
base64 -i [signature-encoded-file]
```

Step 3E: Complete the Message with JWTs {#restgs-jwt-message-construct}
=======================================================================

Combine all of the HTTP headers with your HTTP message body to construct your HTTP signature message.  
If you have not already, you must construct the entire JWS token by combining the JWS header claims, body claims, and signature from Steps 2 -- 4.

Enable Message-Level Encryption {#restgs-mle-intro}
===================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-4-750x175.svg/jcr:content/renditions/original)  
IMPORTANT There are additional tasks you must complete before you can enable message-level encryption. See the Prerequisites for MLE section below.  
Message-Level Encryption (MLE) enables you to store information or communicate with other parties while helping to prevent uninvolved parties from understanding the stored information. Enabling MLE requires you to create or submit a *P12 Certificate* for encrypting your requests and a *REST -- API Response MLE* key for decrypting received responses. If your organization is using meta keys, the *P12 Certificate* and *REST -- API Response MLE* must be created by the same portfolio or merchant account.  
This section explains how to enable MLE with JWT messaging.

Prerequisites for MLE {#restgs_mle_prereq}
==========================================

Before you can set up message-level encryption (MLE), you must complete these requirements:

* Verify that your system is configured to read the public key and encrypt the API payload.
* Verify that you have a P12 certificate and extracted its private key. For more information, see [Create or Submit a P12 Certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-security-p12-intro.md "").
* Verify that your system can construct JWTs. For more information, see [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "").

  > WARNING  
  > As of **February 2026** , there are new requirements for constructing a JWT. By **September 2026**, merchants must update their system to support the new JWT construction. Merchants who do not update their system to support this requirement risk transaction failure.

Step 4A: Create or Submit a REST---API Response MLE Key {#restgs-security-mle-reply}
====================================================================================

Before you can enable your system to support MLE, you must create or upload a *REST---API response MLE* certificate. After creating or uploading the certificate, you can extract the certificate's key to begin enabling MLE. If your organization is using meta keys, the *P12 certificate* and *REST -- API response MLE* key must be created by the same portfolio or merchant account.  
Follow these steps to create or submit an API Response MLE certificate in the `Business Center`:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
2. Under REST APIs, choose **REST -- API Response MLE** , and then click **Generate key** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-4}
   {#restgs-security-mle-reply_step-4}

3. Choose one of these options to download your key:

   * To create a new API response MLE certificate, click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .
   * To upload your own certificate, enter your public PEM-formatted certificate in the text box, and then click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) . The *.pem* file downloads to your desktop. If prompted by your system, approve the location to which the file downloads.

   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply-submit.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-5}
   {#restgs-security-mle-reply_step-5}
   6. If you are creating a certificate, the Set a Password window appears. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
   The *.p12* file downloads to your desktop. If prompted by your system, approve the location to which the key downloads.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
   To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

   > IMPORTANT  
   > Securely store the *.p12* file and password in your system. These credentials are required in order to implement certain products, and you must be able to access them.
   > {#restgs-security-mle-reply_step-6}
   > {#restgs-security-mle-reply_step-6}

4. Click **Cancel** .  
   The Key Management page appears. {#restgs-security-mle-reply_step-7}
   {#restgs-security-mle-reply_step-7}

5. Click the **Key Type** filter and choose **REST-API Response MLE**.{#restgs-security-mle-reply_step-8}
   {#restgs-security-mle-reply_step-8}

6. Click the **Expires At** filter and choose **All Dates**.{#restgs-security-mle-reply_step-9}
   {#restgs-security-mle-reply_step-9}

7. Click **Search**.{#restgs-security-mle-reply_step-10}
   {#restgs-security-mle-reply_step-10}

8. Find the REST--API Response key that you created in the Search Results table and save its key ID.  
   The key ID is needed to test and configure your system to use MLE.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-key-mgmt.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-11}
   {#restgs-security-mle-reply_step-11}

{#restgs-security-mle-reply_list}

**Test Your REST--API Response MLE Key**
:
To test your REST--API Response key, see [Test Your REST---API Response MLE Key](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-message-test.md "").

Step 4B: Extract the SJC Certificate {#restgs-security-mle-extract}
===================================================================

The REST--API Response MLE Key contains an SJC certificate that you must extract in order to enable MLE.  
Follow these steps to extract the SJC certificate from your REST--API Response MLE Key:

1. Open and use a terminal window to navigate to the REST--API Response MLE Key *.p12* file in your system.

2. Run this command to open the *.p12* file:

   ```
   openssl pkcs12 -in {certificate_file_name}.p12
   ```

   You are prompted to enter the import password.

3. Enter the password you set when you created the REST--API Response MLE Key.

4. Locate the `Payment Gateway_SJC_US` certificate in the opened file. This is the SJC certificate.

5. Store the SJC certificate in your system to use when you enable MLE.

Step 4C: Set Up MLE {#restgs-mle-overview}
==========================================

Use the information in this section to configure your system with a custom MLE using JWTs.  
If you do not want to set up a custom MLE, you can use the REST Client SDK instead. For more information, see the REST Client SDKs in [GitHub](https://github.com/example/ "").

#### Figure:

Overview of MLE Set-Up Tasks  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-pgw-700x1200.svg/jcr:content/renditions/original)

1. Import the required programming libraries for your system.{#restgs-mle-overview_step1}
   {#restgs-mle-overview_step1}

2. Import these three certificates:

   * Signing certificate (P12 Certificate or REST -- Certificate).
   * MLE request certificate (SJC public certificate)
   * MLE response certificate (REST -- API Response MLE)
     {#restgs-mle-overview_step2}
     {#restgs-mle-overview_step2}
3. Encrypt the JSON request message using a JSON Web Encryption (JWE) that uses the SJC public certificate.{#restgs-mle-overview_step3}
   {#restgs-mle-overview_step3}

4. Create the HTTP body in this format: `{"encryptedRequest": "`*JWE-with-SJC*`"}`.{#restgs-mle-overview_step4}
   {#restgs-mle-overview_step4}

5. Create the JSON Web Signature (JWS) payload with these JWT payload fields and your signing certificate's private key. For descriptions of these fields, see the Headers table and Message Body Fields table in [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "").

   **Header Fields**
   :
   * alg
   * kid
   * type

   **Message Body Fields**
   :
   * digestAlgorithm
   * digest of the HTTP body
   * exp
   * iat
   * iss
   * jti
   * request-host
   * request-method
   * request-resource-path
   * v-c-jwt-version
   * v-c-merchant-id
   * v-c-response-mle-kid from the MLE response certificate.

   {#restgs-mle-overview_dl}{#restgs-mle-overview_step5}
   {#restgs-mle-overview_step5}

6. Sign the JWS with your P12 certificate and send it as `Authorization: Bearer`.{#restgs-mle-overview_step6}
   {#restgs-mle-overview_step6}

7. Receive an encrypted response and decrypt it with the MLE private key. You will receive the response in this format: `{"encryptedResponse": "`*JWE-with-ResponseMLECertificate*`"}`  
   The JWE contains a JOSE header containing these four default elements:

   ```
   "alg": "RSA-OAEP-256", // The algorithm used to encrypt the CEK.
   "enc": "A256GCM", // The algorithm used to encrypt the message.
   "iat": "1702493653", // The current timestamp in milliseconds.
   "kid": "keyId" // The serial number of the v-c-response-mle-kid from the authentication JWS in step 5.
   ```

   {#restgs-mle-overview_step7}
   {#restgs-mle-overview_step7}

Java Example: Enabling MLE Using JWTs {#rests-mle-jwt}
======================================================

This setup example describes the general requirements to configure your system to support MLE. How you enable MLE in your system can defer from the example code below due to your specific system environment. These example steps use the Java programming language.

1. Import your preferred libraries to support MLE. In this step, the configuration uses Java leveraging the open source Nimbus JOSE and Bouncy Castle libraries.

   ```
   // Nimbus JOSE + JWT
   import com.nimbusds.jose.JWEAlgorithm;
   import com.nimbusds.jose.JWEHeader;
   import com.nimbusds.jose.JWEObject;
   import com.nimbusds.jose.JWSAlgorithm;
   import com.nimbusds.jose.JWSHeader;
   import com.nimbusds.jose.JWSObject;
   import com.nimbusds.jose.JOSEObjectType;
   import com.nimbusds.jose.EncryptionMethod;
   import com.nimbusds.jose.Payload;
   import com.nimbusds.jose.crypto.RSADecrypter;
   import com.nimbusds.jose.crypto.RSAEncrypter;
   import com.nimbusds.jose.crypto.RSASSASigner;

   // BouncyCastle (PEM parsing + cert conversion)
   import org.bouncycastle.cert.X509CertificateHolder;
   import org.bouncycastle.cert.jcajce.JcaX509CertificateConverter;
   import org.bouncycastle.openssl.PEMKeyPair;
   import org.bouncycastle.openssl.PEMParser;
   import org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter;  
   ```
2. Import the signing, MLE, and SJC certificates. The P12 certificate as the signing certificate.

   ```
   public final class KeyPairMaterial {
       public final PrivateKey privateKey;
       public final X509Certificate cert;
       public KeyPairMaterial(PrivateKey k, X509Certificate c) {
           this.privateKey = k;
           this.cert = c;
       }
   }

   public final class CryptoMaterialDual {
       // Merchant: JWS (REST – Certificate)
       public final KeyPairMaterial signingCert;
       // Merchant: Response decryption (API Response MLE)
       public final KeyPairMaterial responseCert;
       // Platform encryption cert (SJC)
       public final X509Certificate sjcCert;

       public CryptoMaterialDual(KeyPairMaterial signingCert, KeyPairMaterial responseCert, X509Certificate sjcCert) {
           this.signingCert = signingCert;
           this.responseCert = responseCert;
           this.sjcCert = sjcCert;
       }
   }
   ```
3. Unpack your imported certificates into a usable format for your system.  
   Create this method for your system to read your *.p12* file, if you are using the P12 certificate.

   ```
   static KeyPairMaterial loadKeyPairFromP12(Path p12Path, char[] password, String keyAlias) throws Exception {
       KeyStore ks = KeyStore.getInstance("PKCS12");
       try (InputStream in = Files.newInputStream(p12Path)) {
           ks.load( in , password);
       }
       KeyStore.PrivateKeyEntry entry = (KeyStore.PrivateKeyEntry) ks.getEntry(
           keyAlias, new KeyStore.PasswordProtection(password));
       return new KeyPairMaterial(entry.getPrivateKey(), (X509Certificate) entry.getCertificate());
   }
   ```

   Create this method for your system to read the PEM chain and private key.

   ```
   static KeyPairMaterial loadKeyPairFromPem(Path certificateChainPem, String privateKeyPem) throws Exception {
       X509Certificate leaf = readPemCerts(certificateChainPem).get(0);
       PrivateKey key = readPkcs8PrivateKey(privateKeyPem);
       return new KeyPairMaterial(key, leaf);
   }
   ```

   Create this method for your system to read the SJC from the *.p12* file or PEM chain.

   ```
   static X509Certificate loadSjcFromP12(Path p12Path, char[] password, String sjcAlias) throws Exception {
       KeyStore ks = KeyStore.getInstance("PKCS12");
       try (InputStream in = Files.newInputStream(p12Path)) {
           ks.load( in , password);
       }
       return (X509Certificate) ks.getCertificate(sjcAlias);
   }

   static X509Certificate loadSjcFromPem(Path sjcCertPem) throws Exception {
       return readPemCerts(sjcCertPem).get(0);
   }
   ```

   Create this method to include PEM helper functions.

   ```
   static List &lt; X509Certificate &gt; readPemCerts(Path pemPath) throws Exception {
       try (Reader r = Files.newBufferedReader(pemPath); org.bouncycastle.openssl.PEMParser p = new org.bouncycastle.openssl.PEMParser(r)) {
           var xconv = new org.bouncycastle.cert.jcajce.JcaX509CertificateConverter().setProvider("BC");
           List &lt; X509Certificate &gt; certs = new ArrayList &lt; &gt; ();
           Object o;
           while ((o = p.readObject()) != null) {
               if (o instanceof org.bouncycastle.cert.X509CertificateHolder h) certs.add(xconv.getCertificate(h));
           }
           return certs;
       }
   }

   static PrivateKey readPkcs8PrivateKey(String pem) throws Exception {
       try (var parser = new org.bouncycastle.openssl.PEMParser(new StringReader(pem))) {
           Object o = parser.readObject();
           var conv = new org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter().setProvider("BC");
           if (o instanceof org.bouncycastle.asn1.pkcs.PrivateKeyInfo pki) return conv.getPrivateKey(pki);
           if (o instanceof org.bouncycastle.openssl.PEMKeyPair kp) return conv.getPrivateKey(kp.getPrivateKeyInfo());
           throw new IllegalArgumentException("Expect PKCS#8 private key PEM");
       }
   }
   ```
4. Create these methods as helpers for encrypting and signing.

   ```
   static String kidFromCert(X509Certificate cert) {
       String dn = cert.getSubjectDN().getName().toUpperCase();
       int i = dn.indexOf("SERIALNUMBER=");
       if (i &gt;= 0) {
           int j = dn.indexOf(",", i);
           if (j &lt; 0) j = dn.length();
           return dn.substring(i + "SERIALNUMBER=".length(), j).trim();
       }
       return cert.getSerialNumber().toString();
   }

   static String encryptToJwe(String json, X509Certificate sjcCert) throws Exception {
       var header = new com.nimbusds.jose.JWEHeader.Builder(
               com.nimbusds.jose.JWEAlgorithm.RSA_OAEP,
               com.nimbusds.jose.EncryptionMethod.A256GCM)
           .contentType("JWT")
           .keyID(kidFromCert(sjcCert))
           .build();
       var jwe = new com.nimbusds.jose.JWEObject(header, new com.nimbusds.jose.Payload(json));
       jwe.encrypt(new com.nimbusds.jose.crypto.RSAEncrypter((RSAPublicKey) sjcCert.getPublicKey()));
       return jwe.serialize();
   }

   static String sha256Base64(String body) throws Exception {
       MessageDigest md = MessageDigest.getInstance("SHA-256");
       return Base64.getEncoder().encodeToString(md.digest(body.getBytes(StandardCharsets.UTF_8)));
   }

   static String signAsJws(String payload, KeyPairMaterial signingCert) throws Exception {
       var header = new com.nimbusds.jose.JWSHeader.Builder(com.nimbusds.jose.JWSAlgorithm.RS256)
           .keyID(kidFromCert(signingCert.cert))
           .type(com.nimbusds.jose.JOSEObjectType.JWT) // typ=JWT
           .build();
       var jws = new com.nimbusds.jose.JWSObject(header, new com.nimbusds.jose.Payload(payload));
       jws.sign(new com.nimbusds.jose.crypto.RSASSASigner(signingCert.privateKey));
       return jws.serialize();
   }

   static String decryptJwe(String compactJwe, KeyPairMaterial responseCert) throws Exception {
       var jwe = com.nimbusds.jose.JWEObject.parse(compactJwe);
       jwe.decrypt(new com.nimbusds.jose.crypto.RSADecrypter((RSAPrivateKey) responseCert.privateKey));
       return jwe.getPayload().toString();
   }
   ```
5. Create a class that uses the methods described in the above steps to encrypt and decrypt your payloads with MLE using JWTs.

   ```
   // Example mix:
   // - REST – Certificate from PKCS#12
   // - API Response MLE from PEM
   // - SJC from PEM
   KeyPairMaterial signingCert = loadKeyPairFromP12(
   Paths.get("merchant.p12"), "password".toCharArray(), "merchant");
   KeyPairMaterial responseCert = loadKeyPairFromPem(
   Paths.get("api_response_mle_chain.pem"), Files.readString(Paths.get("api_response_mle_private_key.pem")));
   X509Certificate sjc = loadSjcFromPem(Paths.get("sjc_certificate.pem"));

   CryptoMaterialDual mat = new CryptoMaterialDual(signingCert, responseCert, sjc);

   // 1) Build your request JSON
   String requestJson = new org.json.JSONObject()
   .put("amount", "10.00")
   .put("currency", "USD")
   .put("reference", "ORDER-12345")
   .toString();

   // 2) Encrypt request body to JWE using SJC public cert
   String encryptedJwe = encryptToJwe(requestJson, mat.sjcCert);

   // 3) Build the HTTP body (this is what you’ll hash for the digest)
   String httpBody = new org.json.JSONObject()
   .put("encryptedRequest", encryptedJwe)
   .toString();

   // 4) Build JWS payload: include iat, response kid, digestAlgorithm, and digest of httpBody
   String digestB64 = sha256Base64(httpBody);
   String jwsPayload = new org.json.JSONObject()
   .put("iat", java.time.Instant.now().getEpochSecond())
   .put("v-c-response-mle-kid", kidFromCert(mat.responseCert.cert))  // instruct server to encrypt to your API Response MLE key
   .put("digestAlgorithm", "SHA-256")
   .put("digest", digestB64)
   .toString();

   // 5) Sign the JWS with the REST – Certificate private key
   String signedJws = signAsJws(jwsPayload, mat.signingCert);

   // 6) Send the HTTP request
   // POST /your/api
   // Content-Type: application/json
   // Authorization: Bearer &lt;signedJws&gt;
   /*
   Body:
   { "encryptedRequest": "&lt;encryptedJwe&gt;" }
   */

   // 7) Handle the response (decrypt if needed with API Response MLE private key)
   String apiResponse = /* http call result as string */;
   org.json.JSONObject resp = new org.json.JSONObject(apiResponse);
   String finalPayload = resp.has("encryptedResponse")
   ? decryptJwe(resp.getString("encryptedResponse"), mat.responseCert)
   : apiResponse;
   ```

Test Your Setup {#restgs-jwt-message-test}
==========================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-5-750x175.svg/jcr:content/renditions/original)  
`Payment Gateway` recommends that you test and verify that your payment system can securely send and receive REST API messages before transitioning to a production account. Use the test examples provided in this section to test your set up. You should also test any additional API requests that you will use in your live environment.

Troubleshooting Using the REST SDK {#restgs-jwt-message-test_section_xrs_b5q_s3c}
---------------------------------------------------------------------------------

You can also use the REST Client SDK to review how the SDK constructs, sends and receives JWT messages with MLE. If you are receiving unsuccessful responses from your custom integration, comparing how your system sends and receives messages to the REST SDK can be helpful. For more information about how to install the REST Client SDK into your system, see the [Install the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-install-intro.md "") section.

Test Your REST---API Response MLE Key {#restgs-jwt-message-mle-dev-center}
==========================================================================

Follow these steps to verify that your API response MLE key is working. If you have not already created or submitted an API response MLE certificate, see the Create or Submit a REST---API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "").

1. Go to the REST API Reference page in the `Payment Gateway` Developer Center:  
   [`https://developer.example.com/api-reference-assets/index.html#static-home-section`](https://developer.example.com/api-reference-assets/index.md#static-home-section "") {#restgs-jwt-message-mle-dev-center_step-1}
   {#restgs-jwt-message-mle-dev-center_step-1}

2. On the left navigation panel, choose an API that supports MLE. For testing purposes, you can choose **Intelligent Commerce \&gt; Intelligent Commerce Product \&gt; Enroll a Card** .  
   MLE support is indicated by **Request MLE** and **Response MLE** at the top of the screen.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-tags.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-2}
   {#restgs-jwt-message-mle-dev-center_step-2}

3. Choose the **MLE Configuration** tab.{#restgs-jwt-message-mle-dev-center_step-3}
   {#restgs-jwt-message-mle-dev-center_step-3}

4. In the Message Level Encryption Credentials section, enter your API response MLE key credentials:

   * **Response encryption:** Enter the key ID of your REST---API response MLE key.  
     You saved this key ID in Step 10 in the Create or Submit a REST---API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "").
   * **Response decryption:** Click **Browse** to submit your own private decryption key from your local system. Only *.p12* files are supported.

   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-upload.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-4}
   {#restgs-jwt-message-mle-dev-center_step-4}

5. Click **Update Credentials**.{#restgs-jwt-message-mle-dev-center_step-5}
   {#restgs-jwt-message-mle-dev-center_step-5}

6. From the **Send** drop-down menu, choose **Send Request with Message Level Encryption**.{#restgs-jwt-message-mle-dev-center_step-6}
   {#restgs-jwt-message-mle-dev-center_step-6}

7. Click **Send** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-send.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-7}
   {#restgs-jwt-message-mle-dev-center_step-7}

8. If a *Success: HTTP Status Code: 201* message displays in the Response section, your REST---API response MLE key is verified as properly configured.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-success.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-8}
   {#restgs-jwt-message-mle-dev-center_step-8} {#restgs-jwt-message-mle-dev-center_ol}

Completing a Test Transaction {#restgs-security-P12-test-transaction}
=====================================================================

After setting up your system to be REST compliant, you can send these test requests to verify that you can send and receive REST API messages.

> IMPORTANT  
> Depending on your payment processor, you may be required to send additional fields that are not shown in these examples.  
> Follow these steps to verify that you can complete a test transaction:

1. **Authorize a Payment**

2. You send this POST request to the `https://apitest.example.com``/pts/v2/payments` endpoint:

   ```keyword
   {
       "orderInformation": {
           "billTo": {
               "country": "US",
               "lastName": "Kim",
               "address1": "201 S. Division St.",
               "postalCode": "48104-2201",
               "locality": "Ann Arbor",
               "administrativeArea": "MI",
               "firstName": "Kyong-Jin",
               "email": "test@pgw.com"
           },
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       },
       "paymentInformation": {
           "card": {
               "expirationYear": "2031",
               "number": "4111111111111111",
               "expirationMonth": "12",
               "type": "001"
           }
       }
   }
   ```
3. You receive a successful response and store the authorization transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id" : "6461731521426399003473"
   ```
4. **Capture an Authorized Payment**

5. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/captures` endpoint and include the authorization transaction ID as the *`{id}`*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6461731521426399003473/captures
   ```

   ```
   {
       "clientReferenceInformation": {
           "code": "ABC123"
       },
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
       }
   }
   ```
6. You receive a successful response and store the capture transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id": "6772994431376681303954"
   ```
7. **Refund a Captured Payment**

8. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/refunds` endpoint and include the capture transaction ID as the *{id}*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6772994431376681303954/refunds
   ```

   ```
   {
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       }
   }
   ```
9. You receive a successful response, which verifies that your system can complete a transaction. A successful response is indicated by a 201 HTTP status code.

Going Live {#restgs-go-live-intro}
==================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-json-6-750x175.svg/jcr:content/renditions/original)  
When you are ready to process payments in a live environment, you must transition your account to the live status with a valid configuration for your chosen payment processor. When your account is live, your transaction data flows through the production `Payment Gateway` gateway, to your processor, and on to the appropriate payment network.  
To transition your account:

1. Sign up for a merchant account.
2. [Contact Sales](https://www.example.com/en-us/contact-us/sales.md "") to establish a contract with `Payment Gateway` that enables you to process real transactions and receive support.
3. Submit a merchant ID (MID) activation request.

{#restgs-go-live-intro_go-live-steps}  
It can take up to three business days for the MID to become active.

Step 6A: Create a Merchant ID {#restgs-go-live-mid}
===================================================

Your merchant ID (MID) identifies you and your transactions, which requires you to include it in each transaction request. When you signed up for a sandbox account, you received a merchant ID for testing purposes. If you choose, you can use that merchant ID as your production ID.  
Follow these steps to sign up for a merchant account in order to create a production MID:

1. Go to the `Business Center` [Sandbox Account Sign Up](https://developer.example.com/hello-world/sandbox.md "") page, enter the required information, and click **Create Account**.  
   Choose your merchant ID name. It cannot be changed. This name is not visible to your customers.
2. Review your information entered, especially your business email address. Your merchant ID registration information will be sent to the email entered on this form.
   3. Look for an email from customer support titled: *`Payment Gateway` Merchant Evaluation Account*.  
      This email contains your organization ID and contact email associated with your MID.
   4. Look for an email titled: *Merchant Registration Details* . Click the **Set up your username and password now** link.  
      Your browser opens the New User Sign Up wizard.
3. Enter the organization ID and contact email you supplied previously. Follow the wizard pages to add your name, a username, and password.
   6. Log in to the `Business Center`.  
      When you log in for the first time, you will be asked to identify yourself through a system-generated email that is sent to your email account.
4. Look for an email titled: *`Payment Gateway` Identification Code*. Save the passcode in the email.
5. Enter the passcode on the Verify your Identity page. You are directed to the `Business Center` home page.

{#restgs-go-live-mid_create-mid-steps}  
You have successfully created a merchant ID and merchant account.

Step 6B: Activate Your Merchant ID {#restgs-go-live-mid-activation}
===================================================================

The activation process, also known as *going live*, transitions your MID and account from test status to live status, enabling you to process real transactions. It can take up to three business days for your MID to become active.  
To transition your account, complete these steps:
1. Sign in to the [Support Center](https://support.example.com/ "") as an administrator.
   2. Enter your credentials and log in to your test environment. The organization ID is your MID.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-test-login.png/jcr:content/renditions/original)
2. In the `Business Center`, go to **Support Cases \&gt; MID Configuration Request**. The MID Configuration Request page should be open.
3. Click **MID Activation**.
4. In the **Description** field, enter the merchant ID that you want to take live.
   6. Choose a processor configuration, and enter the name of your processor.  
      If you are unsure of the processor name, contact your merchant service provider or your merchant acquiring bank.
5. Choose the environments to which this change applies (test or production).
6. Click **Service Enablement** and list the products and services that you intend to use.
7. Click **Submit**.
   {#restgs-go-live-mid-activation_activate-mid-steps}

Production Endpoints {#restgs-endpoints-live}
=============================================

Send API requests using your production account to the production server:  
`https://api.example.com`  
For example, send a live authorization request to this endpoint:  
`https://api.example.com``/pts/v2/payments`

Set Up a JSON Web Token Message Using Shared Secret Key Pairs {#restgs-jwt-shared-secret-intro}
===============================================================================================

> IMPORTANT  
> If you are using HTTP signature security for messaging, use this section to migrate your system to support JSON Web Token messaging. By **September 2026**, all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE).  
> To set up JSON Web Token messaging using a *shared secret key pair*, you must complete the tasks described in this section.

#### Figure:

Set Up JSON Web Token a Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-all-750x175.svg/jcr:content/renditions/original)

1. Sign up for a test account. See [Sign Up for a Sandbox Account](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-shared-secret-register.md "").
2. Create a shared secret key pair. See [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-shared-secret-create-intro.md "").
3. Construct a message using a JSON web token. See [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-con-shared-secret-intro.md "").
4. Enable message-level encryption (MLE) to encrypt all messages. See [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-mle-shared-secret-intro.md "").
5. Test your REST transaction messages. See [Test Your Setup](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-shared-secret-test.md "").
6. Go live by transitioning your sandbox account into a production account. See [Going Live](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-go-live-shared-secret-intro.md "").

Sign Up for a Sandbox Account {#restgs-shared-secret-register}
==============================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-1-750x175.svg/jcr:content/renditions/original)  
To begin setting up your account, you must first sign up for a sandbox account. A sandbox account enables you to obtain your security keys and test your implementation.

> IMPORTANT  
> A sandbox account cannot process live payments and is intended for only testing.  
> Follow these steps to sign up for a sandbox account:

1. Go to the `Payment Gateway` Developer Center sandbox account sign-up page:  
   [https://developer.example.com/hello-world/sandbox.html](https://developer.example.com/hello-world/sandbox.md "")

   2. Enter your information into the sandbox account form, and click **Create Account**.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-registration.png/jcr:content/renditions/original)
   3. Go to your email and find a message titled: *Merchant Registration Details* . Click **Set up your username and password now**.  
      Your browser opens the New User Sign Up wizard.
   4. Enter the organization ID and contact email you supplied when you created your account. Follow the wizard pages to add your name, a username, and a password. Your username and password must meet these requirements:

   |                                        **Username Requirements**                                        |                                                                                  **Password Requirements**                                                                                   |
   |---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | * Length must be 3-36 characters. * Can only contain letters, numbers, periods, dashes, or underscores. | * Length must be 12--50 characters. * Must contain one upper case letter. * Must contain one lower case letter. * Must contain one number. * Cannot contain the username or organization ID. |
   [Username and Password Requirements]

   5. Log in to the `Business Center`.  
      When you log in for the first time, you must verify your identity through a system-generated email sent to your email account.
2. Check your email for a message titled: *`Payment Gateway` Identification Code*. A passcode is included in the message.

   7. Enter the passcode on the *Verify your Identity* page.  
      You are directed to the `Business Center` home page.  
      You have successfully signed up for a sandbox account.

   > IMPORTANT  
   > A sandbox account cannot process live payments. After you verify that your system can send and receive REST messages, you can contact customer service to transition your sandbox account to a production account.

Create a Shared Secret Key Pair {#restgs-shared-secret-create-intro}
====================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-2-750x175.svg/jcr:content/renditions/original)  
This section describes how to create a shared secret key pair and test that it works. A shared secret key pair consists of a *key ID* and a *shared secret key*, which you must have in order to construct JWT messages and enable MLE.

(Optional) Meta Keys
:
If you are using a portfolio or merchant account, you have the option to create a *meta key* of a shared secret key pair. Meta keys enable an organization administrator to assign a single shared secret key pair to some or all transacting merchants in their organization. The purpose of a meta key is to reduce the time needed to manage an organization's keys. For example, by assigning the same meta key to all of your transacting merchants, you only need to update one key when it expires instead of having to update each transacting merchant's key.
:
For more information about meta keys, see the [Meta Key Creation and Management](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") section in the *Creating and Using Security Keys User Guide*.
{#restgs-shared-secret-create-intro_metakeys-dl}

Step 2A: Create a Shared Secret Key Pair {#restgs-shared-secret-create-task}
============================================================================

Follow these steps to create a shared secret key pair:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
     {#restgs-shared-secret-create-task_step-1}
     {#restgs-shared-secret-create-task_step-1}
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#restgs-shared-secret-create-task_step-2}
      {#restgs-shared-secret-create-task_step-2}
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#restgs-shared-secret-create-task_step-3}
      {#restgs-shared-secret-create-task_step-3}
   4. Under REST APIs, choose **REST -- Shared Secret** and then click **Generate key**.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-create-key.png/jcr:content/renditions/original)  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
      The REST API Shared Secret Key page appears. {#restgs-shared-secret-create-task_d17e26}
      {#restgs-shared-secret-create-task_d17e26}
   5. Click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      The *.pem* file downloads to your desktop.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/shared-secret-key-download.png/jcr:content/renditions/original)  
      The **Key** value is your *key ID* and the **Shared Secret** value is your *shared secret key*.

   > IMPORTANT
   > Securely store the key credentials and *.pem* file in your system. These credentials are required in order to implement certain products, and you must be able to access them.
   > {#restgs-shared-secret-create-task_d17e46}
   > {#restgs-shared-secret-create-task_d17e46}

{#restgs-shared-secret-create-task_d17e18}  
To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

**What to do next**
:
To test your shared secret key pair, see [Step 2B: Test Your Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro/restgs-security-key-pair-test-task.md "").

Step 2B: Test Your Shared Secret Key Pair {#restgs-shared-secret-test}
======================================================================

After creating your shared secret key pair, you must verify that your key pair can successfully process API requests. Follow these steps to validate your key pair in the Developer Center and the `Business Center`.

1. Go to the Developer Center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "")
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")** .
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **HTTP Signature**.
4. Enter your organization ID in the **Organization ID** field.
5. Enter your key ID in the **Key** field.
6. Enter your shared secret key in the **Shared Secret Key** field.
7. Click **Update Credentials**.  
   A confirmation message displays stating that your credentials are successfully updated.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-http.png/jcr:content/renditions/original)
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.
9. Click **Send**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original)
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
11. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original)

Construct Messages Using JSON Web Tokens {#restgs-jwt-con-shared-secret-intro}
==============================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-3-750x175.svg/jcr:content/renditions/original) WARNING
As of **February 2026** , there are new requirements for constructing a JWT. This section explains how to update your system to remain in compliance. You must update how your system constructs JWTs by **September 2026** to remain compliant. You risk transaction failure if you do not update your system.  
To construct a message using JWTs, you must set the required HTTP headers, define the JWS header and body claims, calculate the token signature, and combine these elements into a request. This section describes how to create each element and construct the completed JWT message in the following subsections.

#### Figure:

JWT Construction Steps  
![Step 3A: Set the known HTTP header values. Step 3B: Set the JWS header claims.
Step 3C: Set the JWS body claims. Step 3D: Calculate the token signature. Step
3E: Combine the HTTP headers and HTTP message body.](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-jwt-mess-sec-800x500.svg/jcr:content/renditions/original)

JSON Web Token Message Elements {#restgs-jwt-shared-secret-elements}
====================================================================

A JWT message consists of HTTP headers and an HTTP message body.

**HTTP Message Elements**
:
Your HTTP message header must include these elements:
:

    | HTTP Header Element |                                                                      Description                                                                       |
    |---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **content-type**    | Also known as the Multipurpose Internet Mail Extension (MIME) type, this element identifies the media or file type of the resource (application/json). |
    | **host**            | The transaction endpoint. (`api.example.com`)                                                                                                      |
    | **authorization**   | JSON Web Signature (JWS) bearer token.                                                                                                                 |
    [HTTP Message Header Elements]

**HTTP Message Body**
:
Your API request.

Step 3A: Set Known HTTP Headers {#restgs-jwt-shared-secret-set-headers}
=======================================================================

Set the values for these HTTP header elements. These header values do not require any calculation.

content-type
:
Set to the media or file type resource.

host
:
Set to the endpoint.

Step 3B: Set the JWS Header Claims {#restgs-jwt-shared-secret-set-jws-claims}
=============================================================================

You must construct a *JSON Web Signature* (JWS) token. To construct a JWS token, you must first set its header claim values.  
These header claim values do not require calculation.

| Header Field |                                                                                                                                                                                        Description                                                                                                                                                                                        |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **alg**      | The symmetric algorithm you use to sign the token header. These algorithms are supported: * HS256 * HS384 * HS512                                                                                                                                                                                                                                                                         |
| **kid**      | The key ID you use to digitally sign the JWT. It must be registered with the authorizing server. The key ID is from your shared secret key pair. For more information, see [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-shared-secret-create-intro.md ""). |
| **typ**      | The token type. Set to `JWT`.                                                                                                                                                                                                                                                                                                                                                             |
[HTTP Message Header Fields]

Step 3C: Set the JWS Body Claims {#restgs-jwt-shared-secret-set-jws-body}
=========================================================================

After you set the JWS header values, set these JWS body claim values:

|   JWS Body Claim Field    |                                                                                                                                Description                                                                                                                                 | Data Type |               Format                |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------|
| **digest**                | A Base64-encoded hash of the message payload. Do not include the **digest** field if the request message is empty, such as during a GET or DELETE request.                                                                                                                 | String    | Lowercase                           |
| **digestAlgorithm**       | The algorithm used to hash the message payload. The message payload should be hashed using the SHA-256 algorithm. Do not include the **digestAlgorithm** field if the **digest** field is not included.                                                                    | String    | Lowercase                           |
| **exp**                   | The time at which the JWS token expires. > IMPORTANT > Field values cannot exceed two minutes after the message issue date, which is the **iat** field value. This field is an HTTP-date value as defined in RFC7231. For example, 01/01/2020 at 00:02:00 is `1577836920`. | String    | Numeric                             |
| **iat**                   | The date and time at which the message is issued. This field uses a *NumericDate* value as defined in RFC 7519, which is the number of seconds since `1970‑01‑01T00:00:00Z` (Unix epoch). For example, 01/01/2020 at 00:00:00 is `1577836800`.                             | String    | Numeric                             |
| **iss**                   | The issuer identifier for the JWS token. Set to the merchant ID that created the shared secret key pair. This value is used to validate the issuer.                                                                                                                        | String    | Lowercase alphanumeric              |
| **jti**                   | The unique token ID. This value is used for replay prevention. Format the value using UUID version 4. For example: `6643fb9a-8093-47c6-95d3-8d69785b5e62`                                                                                                                  | String    | Lowercase alphanumeric              |
| **request-host**          | The endpoint hostname for the HTTP request, excluding the protocol and path. For example, to send a message to the https://api.example.com`/pts/v2/payments` endpoint, set this field to `api.example.com`.                                                        | String    | Lowercase alphanumeric with periods |
| **request-method**        | The HTTP request method. For example, `post`, `get`, `put`, `patch`, or `delete`.                                                                                                                                                                                          | String    | Lowercase                           |
| **request-resource-path** | The endpoint path for the HTTP request, excluding the domain. For example, to send a message to the https://api.example.com`/pts/v2/payments` endpoint, set this field to `/pts/v2/payments`.                                                                          | String    | Lowercase alphanumeric              |
| **v-c-jwt-version**       | The Relay JWT scheme version number. Set to `2`.                                                                                                                                                                                                                            | String    | Numeric                             |
| **v-c-merchant-id**       | Your `Payment Gateway` transacting merchant ID (MID). If you are a portfolio or merchant account user, set this to the transacting merchant ID you send requests on behalf of.                                                                                                 | String    | Lowercase alphanumeric              |
| **v-c-response-mle-kid**  | The message-level encryption response key ID, also known as the *REST--API Response MLE* key.                                                                                                                                                                              | String    | Lowercase alphanumeric              |
[JWS Body Claims]

The value of the digest JWS claim is a hashed version of the HTTP message body that you must calculate. `Payment Gateway` uses this hash value to validate the integrity of your message body.  
Follow these steps to calculate the digest hash:

1. Generate the SHA-256 hash of the JSON payload (message body).
2. Encode the hashed string to Base64.
3. Add the message body hash to the **digest** JWS body claims.
4. Add the algorithm used to hash the digest in the **digestAlgorithm** JWS body claims.  
   Example: Creating a Message Hash Using the Command Line `shasum` Tool

```keyword
cat &lt;&lt;'EOF' | tr -d '\n' | shasum -a 256
{
  "clientReferenceInformation": {
    "code": "TC50171_3"
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "102.21",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "John",
      "lastName": "Doe",
      "address1": "1MarketSt",
      "locality": "sanfrancisco",
      "administrativeArea": "CA",
      "postalCode": "94105",
      "country": "US",
      "email": "test@pgw.com",
      "phoneNumber": "4158880000"
    }
  }
}
EOF
```

Example: Creating a Message Hash Using the Command Line `base64` Tool

```
echo -n "6ae5459bc8a7d6a4b203e8a734d6a616725134088e13261f5bbcefc1424fc956" | base64
```

Example: Creating a Message Hash Using C#

```
public static string GenerateDigest()
{
    var digest = "";
    var bodyText = "{ your JSON payload }";

    using (var sha256hash = SHA256.Create())
    {
        byte[] payloadBytes = sha256hash.ComputeHash(Encoding.UTF8.GetBytes(bodyText));
        digest = Convert.ToBase64String(payloadBytes);
    }

    return digest;
}
```

Example: Creating a Message Using Java

```
public static String GenerateDigest() throws NoSuchAlgorithmException {
    String bodyText = "{ your JSON payload }";

    MessageDigest md = MessageDigest.getInstance("SHA-256");
    md.update(bodyText.getBytes(StandardCharsets.UTF_8));
    byte[] digest = md.digest();

    return Base64.getEncoder().encodeToString(digest);
}
```

Step 3D: Calculate the JWS Signature {#restgs-jwt-shared-secret-conf-token-sig}
===============================================================================

You can now calculate the JSON Web Signature (JWS). The JWS consists of the JWS header and claim set hashes in the following format. They are encrypted with the private key.  
`[JWS Header].[Claim Set]`  
Follow these steps to calculate the signature:

1. Concatenate the JWS header and claim set hash strings with a period character (`.`) between the hashes:  
   `[JWS Header].[Claim Set]`
2. Generate an encoded version of the text file using your shared secret key from the key pair. For more information, see [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-shared-secret-create-intro.md "").
3. Base64-encode the signature output.
4. After calculating the signature, you can construct a complete JWS token by combining the JWS header claims, body claims, and signature.

**Example: Encoding Headers and Body**

```
printf "%s.%s" \
  "$(echo -n '{"alg":"HS256","typ":"JWT","kid":"1234567890"}' | base64 | tr -d '\n' | tr '+/' '-_' | tr -d '=')" \
  "$(echo -n '{"digest":"Yjg0NGIxOTMxMzQ2NzhlYjdiMDdhMWZmYjZiYzUzNzlkMTk5NzFmNjAzNWRmMThlNzk0N2NhY2U0YTEwNzYyYQ==","digestAlgorithm":"SHA-256","iat":1709845200,"exp":1709845320,"request-method":"post",
"request-resource-path":"/pts/v2/payments","request-host":"api.example.com","iss":"merchantid","jti":"12345678-1234-1234-1234-123456789012","v-c-jwt-version":"2","v-c-merchant-id":"merchantid"}' | 
base64 | tr -d '\n' | tr '+/' '-_' | tr -d '=')" \
  &gt; signing_input.txt
```

**Code Example: Encoding the Signature File Using OpenSSL**  
Generate the HMAC signature using the openssl tool and the signing_input.txt generated above. The tr commands convert standard Base64 output to Base64URL encoding as required by JWT specification RFC 7515.

```
openssl dgst -sha256 -mac HMAC -macopt key:"$(echo 'YOUR_BASE64_ENCODED_SECRET' | base64 -d)" -binary signing_input.txt | base64 | tr -d '\n' | tr '+/' '-_' | tr -d '='
```

Step 3E: Complete the Message with JWTs {#restgs-jwt-shared-secret-construct}
=============================================================================

Combine all of the HTTP headers with your HTTP message body to construct your HTTP signature message.  
If you have not already, you must construct the entire JWS token by combining the JWS header claims, body claims, and signature from Steps 2 -- 4.

Enable Message-Level Encryption {#restgs-mle-shared-secret-intro}
=================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-4-750x175.svg/jcr:content/renditions/original)

> IMPORTANT  
> There are additional tasks you must complete before you can enable message-level encryption. See the Prerequisites for MLE section below.  
> Message-Level Encryption (MLE) enables you to store information or communicate with other parties while helping to prevent uninvolved parties from understanding the stored information. Enabling MLE requires you to create a *shared secret key pair* for encrypting your requests and a *REST -- API Response MLE* key for decrypting received responses. If your organization is using meta keys, the *shared secret key pair* and *REST -- API Response MLE* must be created by the same portfolio or merchant account.  
> This section explains how to enable MLE with JWT messaging.

Prerequisites for MLE {#restgs-mle-shared-secret-prereq}
========================================================

Before you can set up message-level encryption (MLE), you must complete these requirements:

* Verify that your system is configured to read the public key and encrypt the API payload.
* Verify that you have a shared secret key pair. For more information, see [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-shared-secret-create-intro.md "").
* Verify that your system can construct JWTs. For more information, see [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-con-shared-secret-intro.md "").

  > WARNING  
  > As of **February 2026** , there are new requirements for constructing a JWT. By **September 2026**, merchants must update their system to support the new JWT construction. Merchants who do not update their system to support this requirement risk transaction failure.
  > {#restgs-mle-shared-secret-prereq_ul_g3m_szx_s3c}

Step 4A: Create or Submit a REST---API Response MLE Key {#restgs-security-mle-shared-secret-reply}
==================================================================================================

Before you can enable your system to support MLE, you must create or upload a *REST---API response MLE* certificate. After creating or uploading the certificate, you can extract the certificate's key to begin enabling MLE. If your organization is using meta keys, the *shared secret key pair* and *REST -- API response MLE* key must be created by the same portfolio or merchant account.  
Follow these steps to create or submit an API Response MLE certificate in the `Business Center`:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
2. Under REST APIs, choose **REST -- API Response MLE** , and then click **Generate key** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply.png/jcr:content/renditions/original)

3. Choose one of these options to download your key:

   * To create a new API response MLE certificate, click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .
   * To upload your own certificate, enter your public PEM-formatted certificate in the text box, and then click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) . The *.pem* file downloads to your desktop. If prompted by your system, approve the location to which the file downloads.

   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply-submit.png/jcr:content/renditions/original)
   6. If you are creating a certificate, the Set a Password window appears. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
   The *.p12* file downloads to your desktop. If prompted by your system, approve the location to which the key downloads.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
   To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

   > IMPORTANT  
   > Securely store the *.p12* file and password in your system. These credentials are required in order to implement certain products, and you must be able to access them.

4. Click **Cancel** .  
   The Key Management page appears.

5. Click the **Key Type** filter and choose **REST-API Response MLE**.

6. Click the **Expires At** filter and choose **All Dates**.

7. Click **Search**.

8. Find the REST--API Response key that you created in the Search Results table and save its key ID.  
   The key ID is needed to test and configure your system to use MLE.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-key-mgmt.png/jcr:content/renditions/original)

**Test Your REST--API Response MLE Key**
:
To test your REST--API Response key, see [Test Your REST--API Response MLE Key](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-shared-secret-test/restgs-jwt-shared-secret-mle-dev-center.md "").
{#restgs-security-mle-shared-secret-reply_dl_ohx_wfx_s3c}

Step 4B: Extract the SJC Certificate {#restgs-jwt-shared-secret-mle-extract}
============================================================================

The REST--API Response MLE Key contains an SJC certificate that you must extract in order to enable MLE.  
Follow these steps to extract the SJC certificate from your REST--API Response MLE Key:

1. Open and use a terminal window to navigate to the REST--API Response MLE Key *.p12* file in your system.

2. Run this command to open the *.p12* file:

   ```
   openssl pkcs12 -in {certificate_file_name}.p12
   ```

   You are prompted to enter the import password.

3. Enter the password you set when you created the REST--API Response MLE Key.

4. Locate the `Payment Gateway_SJC_US` certificate in the opened file. This is the SJC certificate.

5. Store the SJC certificate in your system to use when you enable MLE.

Step 4C: Set Up MLE {#restgs-mle-shared-secret-overview}
========================================================

Use the information in this section to configure your system with a custom MLE using JWTs.  
If you do not want to set up a custom MLE, you can use the REST Client SDK instead. For more information, see the REST Client SDKs in [GitHub](https://github.com/example/ "").

#### Figure:

Overview of MLE Set-Up Tasks  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-overview-shared-secret-700x1200.svg/jcr:content/renditions/original)

1. Import the required programming libraries for your system.

2. Import these three credentials:

   * Shared secret key pair (REST API key)
   * MLE request certificate (SJC public certificate)
   * MLE response certificate (REST -- API Response MLE)
3. Encrypt the JSON request message using a JSON Web Encryption (JWE) that uses the SJC public certificate.

4. Create the HTTP body in this format: `{"encryptedRequest": "`*JWE-with-SJC*`"}`.

5. Create the JSON Web Signature (JWS) payload with these JWT payload fields and your shared secret key. For descriptions of these fields, see the Headers table and Message Body Fields table in [Construct Messages Using JSON Web Tokens](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-con-shared-secret-intro.md "").

   **Header Fields**
   :
   * alg
   * kid
   * type

   **Message Body Fields**
   :
   * digestAlgorithm
   * digest of the HTTP body
   * exp
   * iat
   * iss
   * jti
   * request-host
   * request-method
   * request-resource-path
   * v-c-jwt-version
   * v-c-merchant-id
   * v-c-response-mle-kid from the MLE response certificate.

   {#restgs-mle-shared-secret-overview_dl_dgm_p4q_s3c}

6. Sign the JWS with your private key from the shared secret key pair and send it as `Authorization: Bearer`.

7. Receive an encrypted response and decrypt it with the MLE private key. You will receive the response in this format: `{"encryptedResponse": "`*JWE-with-ResponseMLECertificate*`"}`  
   The JWE contains a JOSE header containing these four default elements:

   ```
   "alg": "RSA-OAEP-256", // The algorithm used to encrypt the CEK.
   "enc": "A256GCM", // The algorithm used to encrypt the message.
   "iat": "1702493653", // The current timestamp in milliseconds.
   "kid": "keyId" // The serial number of the v-c-response-mle-kid from the authentication JWS in step 5.
   ```

Java Example: Enabling MLE Using JWTs {#restgs-mle-shared-secret-jwt}
=====================================================================

This setup example describes the general requirements to configure your system to support MLE. How you enable MLE in your system can defer from the example code below due to your specific system environment. These example steps use the Java programming language.

1. Import your preferred libraries to support MLE. In this step, the configuration uses Java leveraging the open source Nimbus JOSE and Bouncy Castle libraries.

   ```
   // Nimbus JOSE + JWT
   import com.nimbusds.jose.JWEAlgorithm;
   import com.nimbusds.jose.JWEHeader;
   import com.nimbusds.jose.JWEObject;
   import com.nimbusds.jose.JWSAlgorithm;
   import com.nimbusds.jose.JWSHeader;
   import com.nimbusds.jose.JWSObject;
   import com.nimbusds.jose.JOSEObjectType;
   import com.nimbusds.jose.EncryptionMethod;
   import com.nimbusds.jose.Payload;
   import com.nimbusds.jose.crypto.RSADecrypter;
   import com.nimbusds.jose.crypto.RSAEncrypter;
   import com.nimbusds.jose.crypto.MACSigner;

   // BouncyCastle (PEM parsing + cert conversion)
   import org.bouncycastle.cert.X509CertificateHolder;
   import org.bouncycastle.cert.jcajce.JcaX509CertificateConverter;
   import org.bouncycastle.openssl.PEMKeyPair;
   import org.bouncycastle.openssl.PEMParser;
   import org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter;
   ```
2. Import the signing, MLE, and SJC certificates. The P12 certificate as the signing certificate.

   ```
   public final class CryptoMaterialHmac {
   public final byte[] sharedSecret;
   public final String keyId;
   public final KeyPairMaterial responseCert;
   public final X509Certificate sjcCert;

   public final class CryptoMaterialDual {
   // Merchant: JWS (REST – Certificate)
   public final KeyPairMaterial signingCert;
   // Merchant: Response decryption (API Response MLE)
   public final KeyPairMaterial responseCert;
   // Platform encryption cert (SJC)
   public final X509Certificate sjcCert;

   public CryptoMaterialHmac(byte[] sharedSecret, String keyId, KeyPairMaterial responseCert, X509Certificate sjcCert) {
   this.sharedSecret = sharedSecret;
   this.keyId = keyId;
   this.responseCert = responseCert;
   this.sjcCert = sjcCert;
   }
   }
   ```
3. Unpack your imported certificates into a usable format for your system.  
   Create this method for your system to read your *.p12* file, if you are using the P12 certificate.

   ```
   static KeyPairMaterial loadKeyPairFromP12(Path p12Path, char[] password, String keyAlias) throws Exception {
   KeyStore ks = KeyStore.getInstance("PKCS12");
   try (InputStream in = Files.newInputStream(p12Path)) {
   ks.load( in , password);
   }
   KeyStore.PrivateKeyEntry entry = (KeyStore.PrivateKeyEntry) ks.getEntry(
   keyAlias, new KeyStore.PasswordProtection(password));
   return new KeyPairMaterial(entry.getPrivateKey(), (X509Certificate) entry.getCertificate());
   }
   ```

   Create this method for your system to read the PEM chain and private key.

   ```
   static KeyPairMaterial loadKeyPairFromPem(Path certificateChainPem, String privateKeyPem) throws Exception {
   X509Certificate leaf = readPemCerts(certificateChainPem).get(0);
   PrivateKey key = readPkcs8PrivateKey(privateKeyPem);
   return new KeyPairMaterial(key, leaf);
   }
   ```

   Create this method for your system to read the SJC from the *.p12* file or PEM chain.

   ```
   static X509Certificate loadSjcFromP12(Path p12Path, char[] password, String sjcAlias) throws Exception {
   KeyStore ks = KeyStore.getInstance("PKCS12");
   try (InputStream in = Files.newInputStream(p12Path)) {
   ks.load( in , password);
   }
   return (X509Certificate) ks.getCertificate(sjcAlias);
   }

   static X509Certificate loadSjcFromPem(Path sjcCertPem) throws Exception {
   return readPemCerts(sjcCertPem).get(0);
   }
   ```

   Create this method to include PEM helper functions.

   ```
   static List &lt; X509Certificate &gt; readPemCerts(Path pemPath) throws Exception {
   try (Reader r = Files.newBufferedReader(pemPath); org.bouncycastle.openssl.PEMParser p = new org.bouncycastle.openssl.PEMParser(r)) {
   var xconv = new org.bouncycastle.cert.jcajce.JcaX509CertificateConverter().setProvider("BC");
   List &lt; X509Certificate &gt; certs = new ArrayList &lt; &gt; ();
   Object o;
   while ((o = p.readObject()) != null) {
   if (o instanceof org.bouncycastle.cert.X509CertificateHolder h) certs.add(xconv.getCertificate(h));
   }
   return certs;
   }
   }

   static PrivateKey readPkcs8PrivateKey(String pem) throws Exception {
   try (var parser = new org.bouncycastle.openssl.PEMParser(new StringReader(pem))) {
   Object o = parser.readObject();
   var conv = new org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter().setProvider("BC");
   if (o instanceof org.bouncycastle.asn1.pkcs.PrivateKeyInfo pki) return conv.getPrivateKey(pki);
   if (o instanceof org.bouncycastle.openssl.PEMKeyPair kp) return conv.getPrivateKey(kp.getPrivateKeyInfo());
   throw new IllegalArgumentException("Expect PKCS#8 private key PEM");
   }
   }
   ```
4. Create these methods as helpers for encrypting and signing.

   ```
   static String kidFromCert(X509Certificate cert) {
   String dn = cert.getSubjectDN().getName().toUpperCase();
   int i = dn.indexOf("SERIALNUMBER=");
   if (i &gt;= 0) {
   int j = dn.indexOf(",", i);
   if (j &lt; 0) j = dn.length();
   return dn.substring(i + "SERIALNUMBER=".length(), j).trim();
   }
   return cert.getSerialNumber().toString();
   }

   static String encryptToJwe(String json, X509Certificate sjcCert) throws Exception {
   var header = new com.nimbusds.jose.JWEHeader.Builder(
   com.nimbusds.jose.JWEAlgorithm.RSA_OAEP,
   com.nimbusds.jose.EncryptionMethod.A256GCM)
   .contentType("JWT")
   .keyID(kidFromCert(sjcCert))
   .build();
   var jwe = new com.nimbusds.jose.JWEObject(header, new com.nimbusds.jose.Payload(json));
   jwe.encrypt(new com.nimbusds.jose.crypto.RSAEncrypter((RSAPublicKey) sjcCert.getPublicKey()));
   return jwe.serialize();
   }

   static String sha256Base64(String body) throws Exception {
   MessageDigest md = MessageDigest.getInstance("SHA-256");
   return Base64.getEncoder().encodeToString(md.digest(body.getBytes(StandardCharsets.UTF_8)));
   }


   static String signAsJwsHmac(String payload, byte[] sharedSecret, String keyId) throws Exception {
   var headerBuilder = new com.nimbusds.jose.JWSHeader.Builder(com.nimbusds.jose.JWSAlgorithm.HS256)
   .type(com.nimbusds.jose.JOSEObjectType.JWT);

   // CHANGED: Add optional keyId (not extracted from certificate)
   if (keyId != null && !keyId.isEmpty()) {
   headerBuilder.keyID(keyId);
   }

   var header = headerBuilder.build();
   var jws = new com.nimbusds.jose.JWSObject(header, new com.nimbusds.jose.Payload(payload));
   jws.sign(new com.nimbusds.jose.crypto.MACSigner(sharedSecret));
   return jws.serialize();
   }

   static String decryptJwe(String compactJwe, KeyPairMaterial responseCert) throws Exception {
   var jwe = com.nimbusds.jose.JWEObject.parse(compactJwe);
   jwe.decrypt(new com.nimbusds.jose.crypto.RSADecrypter((RSAPrivateKey) responseCert.privateKey));
   return jwe.getPayload().toString();
   }
   ```
5. Create a class that uses the methods described in the above steps to encrypt and decrypt your payloads with MLE using JWTs.

   ```
   // - REST – Shared Secret (base64-encoded)
   // - API Response MLE from PEM
   // - SJC from PEM

   // Load and decode your base64-encoded shared secret
   String base64Secret = "YOUR_BASE64_ENCODED_SECRET";// Get from your secure configuration
   byte[] sharedSecret = java.util.Base64.getDecoder().decode(base64Secret);
   String keyId = "1234567890";// Optional: Your Key ID

   KeyPairMaterial responseCert = loadKeyPairFromPem(
   Paths.get("api_response_mle_chain.pem"), Files.readString(Paths.get("api_response_mle_private_key.pem")));
   X509Certificate sjc = loadSjcFromPem(Paths.get("sjc_certificate.pem"));

   CryptoMaterialHmac mat = new CryptoMaterialHmac(sharedSecret, keyId, responseCert, sjc);

   // 1) Build your request JSON
   String requestJson = new org.json.JSONObject()
   .put("amount", "10.00")
   .put("currency", "USD")
   .put("reference", "ORDER-12345")
   .toString();

   // 2) Encrypt request body to JWE using SJC public cert
   String encryptedJwe = encryptToJwe(requestJson, mat.sjcCert);

   // 3) Build the HTTP body (this is what you'll hash for the digest)
   String httpBody = new org.json.JSONObject()
   .put("encryptedRequest", encryptedJwe)
   .toString();

   // 4) Build JWS payload: include iat, response kid, digestAlgorithm, and digest of httpBody
   String digestB64 = sha256Base64(httpBody);
   String jwsPayload = new org.json.JSONObject()
   .put("iat", java.time.Instant.now().getEpochSecond())
   .put("v-c-response-mle-kid", kidFromCert(mat.responseCert.cert))// instruct server to encrypt to your API Response MLE key
   .put("digestAlgorithm", "SHA-256")
   .put("digest", digestB64)
   .toString();

   // 5) Sign the JWS with the shared secret using HMAC
   String signedJws = signAsJwsHmac(jwsPayload, mat.sharedSecret, mat.keyId);

   // 6) Send the HTTP request
   // POST /your/api
   // Content-Type: application/json
   // Authorization: Bearer &lt;signedJws&gt;
   /*
   Body:
   { "encryptedRequest": "&lt;encryptedJwe&gt;" }
   */

   // 7) Handle the response (decrypt if needed with API Response MLE private key)
   String apiResponse = /* http call result as string */;
   org.json.JSONObject resp = new org.json.JSONObject(apiResponse);
   String finalPayload = resp.has("encryptedResponse")
   ? decryptJwe(resp.getString("encryptedResponse"), mat.responseCert)
   : apiResponse;
   ```

Test Your Setup {#restgs-jwt-shared-secret-test}
================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-5-750x175.svg/jcr:content/renditions/original)  
`Payment Gateway` recommends that you test and verify that your payment system can securely send and receive REST API messages before transitioning to a production account. Use the test examples provided in this section to test your set up. You should also test any additional API requests that you will use in your live environment.

Troubleshooting Using the REST SDK {#restgs-jwt-shared-secret-test_d10e28}
--------------------------------------------------------------------------

You can also use the REST Client SDK to review how the SDK constructs, sends and receives JWT messages with MLE. If you are receiving unsuccessful responses from your custom integration, comparing how your system sends and receives messages to the REST SDK can be helpful. For more information about how to install the REST Client SDK into your system, see the [Install the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-install-intro.md "") section.

Test Your REST--API Response MLE Key {#restgs-jwt-shared-secret-mle-dev-center}
===============================================================================

Follow these steps to verify that your API response MLE key is working. If you have not already created or submitted an API response MLE certificate, see the Create or Submit a REST---API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-mle-shared-secret-intro.md "").

1. Go to the REST API Reference page in the `Payment Gateway` Developer Center:  
   [`https://developer.example.com/api-reference-assets/index.html#static-home-section`](https://developer.example.com/api-reference-assets/index.md#static-home-section "")

2. On the left navigation panel, choose an API that supports MLE. For testing purposes, you can choose **Intelligent Commerce \&gt; Intelligent Commerce Product \&gt; Enroll a Card** .  
   MLE support is indicated by **Request MLE** and **Response MLE** at the top of the screen.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-tags.png/jcr:content/renditions/original)

3. Choose the **MLE Configuration** tab.

4. In the Message Level Encryption Credentials section, enter your API response MLE key credentials:

   * **Response encryption:** Enter the key ID of your REST---API response MLE key.  
     You saved this key ID in Step 10 in the Create or Submit a REST---API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-mle-shared-secret-intro.md "").
   * **Response decryption:** Click **Browse** to submit your own private decryption key from your local system. Only *.p12* files are supported.

   {#restgs-jwt-shared-secret-mle-dev-center_ul_xhx_ncx_s3c}  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-upload.png/jcr:content/renditions/original) {#restgs-jwt-shared-secret-mle-dev-center_step-4}
   {#restgs-jwt-shared-secret-mle-dev-center_step-4}

5. Click **Update Credentials**.

6. From the **Send** drop-down menu, choose **Send Request with Message Level Encryption**.

7. Click **Send** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-send.png/jcr:content/renditions/original)

8. If a *Success: HTTP Status Code: 201* message displays in the Response section, your REST---API response MLE key is verified as properly configured.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-success.png/jcr:content/renditions/original)
   {#restgs-jwt-shared-secret-mle-dev-center_ol_cvb_jcx_s3c}

Completing a Test Transaction {#restgs-jwt-shared-secret-test-transaction}
==========================================================================

After setting up your system to be REST compliant, you can send these test requests to verify that you can send and receive REST API messages.

> IMPORTANT  
> Depending on your payment processor, you may be required to send additional fields that are not shown in these examples.  
> Follow these steps to verify that you can complete a test transaction:

1. **Authorize a Payment**

2. You send this POST request to the `https://apitest.example.com``/pts/v2/payments` endpoint:

   ```keyword
   {
       "orderInformation": {
           "billTo": {
               "country": "US",
               "lastName": "Kim",
               "address1": "201 S. Division St.",
               "postalCode": "48104-2201",
               "locality": "Ann Arbor",
               "administrativeArea": "MI",
               "firstName": "Kyong-Jin",
               "email": "test@pgw.com"
           },
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       },
       "paymentInformation": {
           "card": {
               "expirationYear": "2031",
               "number": "4111111111111111",
               "expirationMonth": "12",
               "type": "001"
           }
       }
   }
   ```
3. You receive a successful response and store the authorization transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id" : "6461731521426399003473"
   ```
4. **Capture an Authorized Payment**

5. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/captures` endpoint and include the authorization transaction ID as the *`{id}`*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6461731521426399003473/captures
   ```

   ```
   {
       "clientReferenceInformation": {
           "code": "ABC123"
       },
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
       }
   }
   ```
6. You receive a successful response and store the capture transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id": "6772994431376681303954"
   ```
7. **Refund a Captured Payment**

8. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/refunds` endpoint and include the capture transaction ID as the *{id}*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6772994431376681303954/refunds
   ```

   ```
   {
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       }
   }
   ```
9. You receive a successful response, which verifies that your system can complete a transaction. A successful response is indicated by a 201 HTTP status code.

Going Live {#restgs-go-live-shared-secret-intro}
================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-sharedsecret-6-750x175.svg/jcr:content/renditions/original)  
When you are ready to process payments in a live environment, you must transition your account to the live status with a valid configuration for your chosen payment processor. When your account is live, your transaction data flows through the production `Payment Gateway` gateway, to your processor, and on to the appropriate payment network.  
To transition your account:

1. Sign up for a merchant account.
2. [Contact Sales](https://www.example.com/en-us/contact-us/sales.md "") to establish a contract with `Payment Gateway` that enables you to process real transactions and receive support.
3. Submit a merchant ID (MID) activation request.

{#restgs-go-live-shared-secret-intro_d13e35}  
It can take up to three business days for the MID to become active.

Step 6A: Create a Merchant ID {#restgs-go-live-shared-secret-mid}
=================================================================

Your merchant ID (MID) identifies you and your transactions, which requires you to include it in each transaction request. When you signed up for a sandbox account, you received a merchant ID for testing purposes. If you choose, you can use that merchant ID as your production ID.  
Follow these steps to sign up for a merchant account in order to create a production MID:

1. Go to the `Business Center` [Sandbox Account Sign Up](https://developer.example.com/hello-world/sandbox.md "") page, enter the required information, and click **Create Account**.  
   Choose your merchant ID name. It cannot be changed. This name is not visible to your customers.
2. Review your information entered, especially your business email address. Your merchant ID registration information will be sent to the email entered on this form.
   3. Look for an email from customer support titled: *`Payment Gateway` Merchant Evaluation Account*.  
      This email contains your organization ID and contact email associated with your MID.
   4. Look for an email titled: *Merchant Registration Details* . Click the **Set up your username and password now** link.  
      Your browser opens the New User Sign Up wizard.
3. Enter the organization ID and contact email you supplied previously. Follow the wizard pages to add your name, a username, and password.
   6. Log in to the `Business Center`.  
      When you log in for the first time, you will be asked to identify yourself through a system-generated email that is sent to your email account.
4. Look for an email titled: *`Payment Gateway` Identification Code*. Save the passcode in the email.
5. Enter the passcode on the Verify your Identity page. You are directed to the `Business Center` home page.

{#restgs-go-live-shared-secret-mid_d9e21}  
You have successfully created a merchant ID and merchant account.

Step 6B: Activate Your Merchant ID {#restgs-go-live-mid-shared-secret-activation}
=================================================================================

The activation process, also known as *going live*, transitions your MID and account from test status to live status, enabling you to process real transactions. It can take up to three business days for your MID to become active.  
To transition your account, complete these steps:
1. Sign in to the [Support Center](https://support.example.com/ "") as an administrator.
   2. Enter your credentials and log in to your test environment. The organization ID is your MID.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-test-login.png/jcr:content/renditions/original)
2. In the `Business Center`, go to **Support Cases \&gt; MID Configuration Request**. The MID Configuration Request page should be open.
3. Click **MID Activation**.
4. In the **Description** field, enter the merchant ID that you want to take live.
   6. Choose a processor configuration, and enter the name of your processor.  
      If you are unsure of the processor name, contact your merchant service provider or your merchant acquiring bank.
5. Choose the environments to which this change applies (test or production).
6. Click **Service Enablement** and list the products and services that you intend to use.
7. Click **Submit**.
   {#restgs-go-live-mid-shared-secret-activation_d7e26}

Production Endpoints {#restgs-endpoints-shared-secret}
======================================================

Send API requests using your production account to the production server:  
`https://api.example.com`  
For example, send a live authorization request to this endpoint:  
`https://api.example.com``/pts/v2/payments`

Set Up a JSON Web Token Message Using the REST SDK {#restgs-sdk-intro}
======================================================================

To use the `Payment Gateway` REST Client SDK, you must complete the tasks described in this section.  
![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-all-750x200.svg/jcr:content/renditions/original)

1. Sign up for a test account. See [Sign Up for a Sandbox Account](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-register.md "").
2. Create an API security key, such as a P12 certificate or a shared secret key pair. See [Create a Security Key](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-key-intro.md "").
3. Create a REST--API Response Key in order to enable Message-Level Encryption. See [Create REST--API Response Key](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-mle-intro.md "").
4. Install the REST SDK. See [Install the REST SDK](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-install-intro.md "").
5. Test your REST transaction messages. See [Test Your Setup](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-test.md "").
6. Go live by transitioning your sandbox account into a production account. See [Going Live](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-go-live-shared-secret-intro.md "").

Sign Up for a Sandbox Account {#restgs-sdk-register}
====================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-1-750x200.svg/jcr:content/renditions/original)  
To begin setting up your account, you must first sign up for a sandbox account. A sandbox account enables you to obtain your security keys and test your implementation.

> IMPORTANT  
> A sandbox account cannot process live payments and is intended for only testing.  
> Follow these steps to sign up for a sandbox account:

1. Go to the `Payment Gateway` Developer Center sandbox account sign-up page:  
   [https://developer.example.com/hello-world/sandbox.html](https://developer.example.com/hello-world/sandbox.md "")

   2. Enter your information into the sandbox account form, and click **Create Account**.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-registration.png/jcr:content/renditions/original)
   3. Go to your email and find a message titled: *Merchant Registration Details* . Click **Set up your username and password now**.  
      Your browser opens the New User Sign Up wizard.
   4. Enter the organization ID and contact email you supplied when you created your account. Follow the wizard pages to add your name, a username, and a password. Your username and password must meet these requirements:

   |                                        **Username Requirements**                                        |                                                                                  **Password Requirements**                                                                                   |
   |---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | * Length must be 3-36 characters. * Can only contain letters, numbers, periods, dashes, or underscores. | * Length must be 12--50 characters. * Must contain one upper case letter. * Must contain one lower case letter. * Must contain one number. * Cannot contain the username or organization ID. |
   [Username and Password Requirements]

   5. Log in to the `Business Center`.  
      When you log in for the first time, you must verify your identity through a system-generated email sent to your email account.
2. Check your email for a message titled: *`Payment Gateway` Identification Code*. A passcode is included in the message.

   7. Enter the passcode on the *Verify your Identity* page.  
      You are directed to the `Business Center` home page.  
      You have successfully signed up for a sandbox account.

   > IMPORTANT  
   > A sandbox account cannot process live payments. After you verify that your system can send and receive REST messages, you can contact customer service to transition your sandbox account to a production account.

Create a Security Key {#restgs-sdk-key-intro}
=============================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-2-750x200.svg/jcr:content/renditions/original)  
This section describes how to create a security key and how to test that it works.  
Choose one of these REST security key types to create in order to use the REST Client SDK:

* P12 certificate. For more information, see [Create a P12 Certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-key-intro/restgs-sdk-key-p12-intro.md "").
* Shared secret key pair. For more information, see [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-sdk-intro/restgs-sdk-key-intro/restgs-sdk-key-shared-secret-intro.md "").

Create a P12 Certificate {#restgs-sdk-key-p12-intro}
====================================================

This section describes how to create or submit a P12 certificate, extract the certificate's *private key*, and test the private key to verify that it works. A private key is necessary for you to construct JSON Web Tokens (JWTs).  
You can choose to create or submit a P12 certificate. *Create* a P12 certificate if you need a new certificate. *Submit* a P12 certificate if you want to use your own certificate.

(Optional) Meta Keys
:
If you are using a portfolio or merchant account, you have the option to create a *meta key* of a P12 certificate. Meta keys enable an organization administrator to assign a single P12 certificate to some or all transacting merchants in their organization. The purpose of a meta key is to reduce the time needed to manage an organization's keys. For example, by assigning the same meta key to all of your transacting merchants, you only need to update one key when it expires instead of having to update each transacting merchant's key.
:
For more information about meta keys, see the [Meta Key Creation and Management](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") section in the *Creating and Using Security Keys User Guide*.
{#restgs-sdk-key-p12-intro_d82e43}

Step 2A: Creating or Submitting a P12 Certificate {#restgs-sdk-key-p12-create}
==============================================================================

Follow these steps to create a P12 certificate file or submit your own certificate signing request (CSR):

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
   4. Under REST APIs, choose REST -- Certificate, and then click Generate key.  
      The Key Generation page appears.  
      If you are using a *portfolio* account, the Key options window appears, giving you the choice to create a meta key. For more information about how to create a meta key, see *[Creating and Using Security Keys](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "")*.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-select.png/jcr:content/renditions/original)
2. (Optional) You can set the Certificate Expiry Timeframe field to the number of months you want the key to remain active before it expires. Only whole numbers from 1--36 are accepted. By default, new keys expire after 12 months.
3. Choose from these two options:
   1. If you are a creating a new P12 Certificate, click Download key ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-blank.png/jcr:content/renditions/original)
   2. If you are submitting your own certificate, enter your public PEM-formatted certificate in the text box, then click Download key ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-fill.png/jcr:content/renditions/original)
      {#restgs-sdk-key-p12-create_d62e31}
      {#restgs-sdk-key-p12-create_d62e31}
   3. Create a password for the certificate by entering one into the New Password and Confirm Password fields. Click Generate key.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
      The *.p12* file downloads to your desktop.  
      If prompted by your system, approve the location to which the key downloads. {#restgs-sdk-key-p12-create_d62e60}
      {#restgs-sdk-key-p12-create_d62e60}

{#restgs-sdk-key-p12-create_d62e18}  
To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

> IMPORTANT  
> Securely store the *.p12* file and password in your system. These credentials are required in order to implement certain products, and you must be able to access them.

Step 2B: Testing Your Private Key {#restgs-sdk-key-p12-test}
============================================================

After creating your key certificate, you must verify that it can successfully process API requests. This task explains how to test and validate your private key in the Developer Center and the `Business Center`.  
Follow these steps:

1. Go to the Developer Center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "") {#restgs-sdk-key-p12-test_d32e29}
   {#restgs-sdk-key-p12-test_d32e29}
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")** .{#restgs-sdk-key-p12-test_d32e42}
   {#restgs-sdk-key-p12-test_d32e42}
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **JSON Web Token**.{#restgs-sdk-key-p12-test_d32e52}
   {#restgs-sdk-key-p12-test_d32e52}
4. Enter your organization ID in the **Organization** field.{#restgs-sdk-key-p12-test_d32e61}
   {#restgs-sdk-key-p12-test_d32e61}
5. Enter your Password in the **Password** field.
6. Click **Browse** and upload your p12 certificate from your desktop.{#restgs-sdk-key-p12-test_d32e80}
   {#restgs-sdk-key-p12-test_d32e80}
7. Click **Update Credentials**.  
   A confirmation message states that your credentials are successfully updated.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-cert-test.png/jcr:content/renditions/original) {#restgs-sdk-key-p12-test_d32e89}
   {#restgs-sdk-key-p12-test_d32e89}
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.{#restgs-sdk-key-p12-test_d32e104}
   {#restgs-sdk-key-p12-test_d32e104}
9. Click **Send**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original) {#restgs-sdk-key-p12-test_d32e116}
   {#restgs-sdk-key-p12-test_d32e116}
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "") {#restgs-sdk-key-p12-test_d32e135}
    {#restgs-sdk-key-p12-test_d32e135}
11. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.{#restgs-sdk-key-p12-test_d32e150}
    {#restgs-sdk-key-p12-test_d32e150}
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original) {#restgs-sdk-key-p12-test_d32e162}
    {#restgs-sdk-key-p12-test_d32e162}

Create a Shared Secret Key Pair {#restgs-sdk-key-shared-secret-intro}
=====================================================================

This section describes how to create a shared secret key pair and test that it works. A shared secret key pair consists of a *key ID* and a *shared secret key*, which you must have in order to construct JWT messages and enable MLE.

(Optional) Meta Keys
:
If you are using a portfolio or merchant account, you have the option to create a *meta key* of a shared secret key pair. Meta keys enable an organization administrator to assign a single shared secret key pair to some or all transacting merchants in their organization. The purpose of a meta key is to reduce the time needed to manage an organization's keys. For example, by assigning the same meta key to all of your transacting merchants, you only need to update one key when it expires instead of having to update each transacting merchant's key.
:
For more information about meta keys, see the [Meta Key Creation and Management](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") section in the *Creating and Using Security Keys User Guide*.
{#restgs-sdk-key-shared-secret-intro_d74e35}

Step 2A: Create a Shared Secret Key Pair {#restgs-sdk-key-shared-secret-create}
===============================================================================

Follow these steps to create a shared secret key pair:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
     {#restgs-sdk-key-shared-secret-create_step-1}
     {#restgs-sdk-key-shared-secret-create_step-1}
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#restgs-sdk-key-shared-secret-create_step-2}
      {#restgs-sdk-key-shared-secret-create_step-2}
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#restgs-sdk-key-shared-secret-create_step-3}
      {#restgs-sdk-key-shared-secret-create_step-3}
   4. Under REST APIs, choose **REST -- Shared Secret** and then click **Generate key**.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-create-key.png/jcr:content/renditions/original)  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
      The REST API Shared Secret Key page appears. {#restgs-sdk-key-shared-secret-create_d17e26}
      {#restgs-sdk-key-shared-secret-create_d17e26}
   5. Click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      The *.pem* file downloads to your desktop.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/shared-secret-key-download.png/jcr:content/renditions/original)  
      The **Key** value is your *key ID* and the **Shared Secret** value is your *shared secret key*.

   > IMPORTANT
   > Securely store the key credentials and *.pem* file in your system. These credentials are required in order to implement certain products, and you must be able to access them.
   > {#restgs-sdk-key-shared-secret-create_d17e46}
   > {#restgs-sdk-key-shared-secret-create_d17e46}

{#restgs-sdk-key-shared-secret-create_d17e18}  
To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

**What to do next**
:
To test your shared secret key pair, see [Step 2B: Test Your Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro/restgs-security-key-pair-test-task.md "").

Step 2B: Test Your Shared Secret Key Pair {#restgs-sdk-key-shared-secret-test}
==============================================================================

After creating your shared secret key pair, you must verify that your key pair can successfully process API requests. Follow these steps to validate your key pair in the Developer Center and the `Business Center`.

1. Go to the Developer Center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "")
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")** .
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **HTTP Signature**.
4. Enter your organization ID in the **Organization ID** field.
5. Enter your key ID in the **Key** field.
6. Enter your shared secret key in the **Shared Secret Key** field.
7. Click **Update Credentials**.  
   A confirmation message displays stating that your credentials are successfully updated.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-http.png/jcr:content/renditions/original)
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.
9. Click **Send**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original)
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
11. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original)

Create REST--API Response Key {#restgs-sdk-mle-intro}
=====================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-3-750x200.svg/jcr:content/renditions/original)  
To enable message-level encryption (MLE) for your SDK integration, you must create a REST--API response key. This section describes how to create and test a REST--API response key.

Overview of MLE {#restgs-sdk-mle-intro_section_shd_zsp_s3c}
-----------------------------------------------------------

Message-Level Encryption (MLE) enables you to store information or communicate with other parties while helping to prevent uninvolved parties from understanding the stored information. Enabling MLE requires you to create a *P12 certificate* or *shared secret key pair* for encrypting your requests and a *REST -- API Response MLE* key for decrypting received responses. If your organization is using meta keys, your security keys must be created by the same portfolio or merchant account.

Step 3A: Create or Submit a REST---API Response MLE Key {#restgs-sdk-mle-create}
================================================================================

Before you can enable your system to support MLE, you must create or upload a *REST---API response MLE* certificate. After creating or uploading the certificate, you can extract the certificate's key to begin enabling MLE. If your organization is using meta keys, the *shared secret key pair* and *REST -- API response MLE* key must be created by the same portfolio or merchant account.  
Follow these steps to create or submit an API Response MLE certificate in the `Business Center`:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
2. Under REST APIs, choose **REST -- API Response MLE** , and then click **Generate key** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply.png/jcr:content/renditions/original)

3. Choose one of these options to download your key:

   * To create a new API response MLE certificate, click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .
   * To upload your own certificate, enter your public PEM-formatted certificate in the text box, and then click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) . The *.pem* file downloads to your desktop. If prompted by your system, approve the location to which the file downloads.

   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply-submit.png/jcr:content/renditions/original)
   6. If you are creating a certificate, the Set a Password window appears. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
   The *.p12* file downloads to your desktop. If prompted by your system, approve the location to which the key downloads.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
   To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

   > IMPORTANT  
   > Securely store the *.p12* file and password in your system. These credentials are required in order to implement certain products, and you must be able to access them.

4. Click **Cancel** .  
   The Key Management page appears.

5. Click the **Key Type** filter and choose **REST-API Response MLE**.

6. Click the **Expires At** filter and choose **All Dates**.

7. Click **Search**.

8. Find the REST--API Response key that you created in the Search Results table and save its key ID.  
   The key ID is needed to test and configure your system to use MLE.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-key-mgmt.png/jcr:content/renditions/original)

**Test Your REST--API Response MLE Key**
:
To test your REST--API Response key, see [Test Your REST--API Response MLE Key](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro/restgs-jwt-shared-secret-test/restgs-jwt-shared-secret-mle-dev-center.md "").
{#restgs-sdk-mle-create_d61e55}

Step 3B: Test Your REST-API Response Key {#restgs-sdk-mle-test}
===============================================================

Follow these steps to verify that your API response MLE key is working:
1. Go to the REST API Reference page in the `Payment Gateway` Developer Center:  
   [`https://developer.example.com/api-reference-assets/index.html#static-home-section`](https://developer.example.com/api-reference-assets/index.md#static-home-section "")

2. On the left navigation panel, choose an API that supports MLE. For testing purposes, you can choose **Intelligent Commerce \&gt; Intelligent Commerce Product \&gt; Enroll a Card** .  
   MLE support is indicated by **Request MLE** and **Response MLE** at the top of the screen.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-tags.png/jcr:content/renditions/original)

3. Choose the **MLE Configuration** tab.

4. In the Message Level Encryption Credentials section, enter your API response MLE key credentials:

   * **Response encryption:** Enter the key ID of your REST---API response MLE key.  
     You saved this key ID in Step 10 in the Create or Submit a REST---API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "").
   * **Response decryption:** Click **Browse** to submit your own private decryption key from your local system. Only *.p12* files are supported.

   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-upload.png/jcr:content/renditions/original)

5. Click **Update Credentials**.

6. From the **Send** drop-down menu, choose **Send Request with Message Level Encryption**.

7. Click **Send** .  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-send.png/jcr:content/renditions/original)

8. If a *Success: HTTP Status Code: 201* message displays in the Response section, your REST---API response MLE key is verified as properly configured.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-success.png/jcr:content/renditions/original)
   {#restgs-sdk-mle-test_ol_p54_5tp_s3c}

Install the REST SDK {#restgs-sdk-install-intro}
================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-4-750x200.svg/jcr:content/renditions/original)  
The *REST Client SDK* constructs JSON Web Token (JWT) messages for you to send to `Payment Gateway`. These messages are also encrypted using Message-Level Encryption (MLE) by the SDK. When you receive a response message from `Payment Gateway`, the SDK decrypts it using MLE.  
For more information about how to install the REST Client SDK into your system, see the *REST API related products* table in the `Payment Gateway` [GitHub](https://github.com/example/ "").

SDK Version
-----------

This table lists the minimum SDK versions that support the updated JWT message construction and MLE requirements. Find your system's processing language and install the corresponding SDK version or a later version.

|          Language          | Minimum SDK Version Required |                                                                                                        MLE Enablement Instructions                                                                                                        |
|----------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .NET Framework             | v0.0.1.60                    | [payment-gateway-rest-client-dotnet/MLE.md at master · Payment Gateway/payment-gateway-rest-client-dotnet](https://github.com/example/payment-gateway-rest-client-dotnet/blob/master/MLE.md "")                                                       |
| .NET Standard or .NET Core | v0.0.1.52                    | [payment-gateway-rest-client-dotnetstandard/payment-gateway-rest-client-netstandard/MLE.md at master · Cyber...](https://github.com/example/payment-gateway-rest-client-dotnetstandard/blob/master/payment-gateway-rest-client-netstandard/MLE.md "") |
| Java                       | v0.0.85                      | [payment-gateway-rest-client-java/MLE.md at master · Payment Gateway/payment-gateway-rest-client-java](https://github.com/example/payment-gateway-rest-client-java/blob/master/MLE.md "")                                                             |
| Node                       | v0.0.75                      | [payment-gateway-rest-client-node/MLE.md at master · Payment Gateway/payment-gateway-rest-client-node](https://github.com/example/payment-gateway-rest-client-node/blob/master/MLE.md "")                                                             |
| PHP                        | v0.0.69                      | [payment-gateway-rest-client-php/MLE.md at master · Payment Gateway/payment-gateway-rest-client-php](https://github.com/example/payment-gateway-rest-client-php/blob/master/MLE.md "")                                                                |
| Python                     | v0.0.73                      | [payment-gateway-rest-client-python/MLE.md at master · Payment Gateway/payment-gateway-rest-client-python](https://github.com/example/payment-gateway-rest-client-python/blob/master/MLE.md "")                                                       |
| Ruby                       | v0.0.81                      | [payment-gateway-rest-client-ruby/MLE.md at master · Payment Gateway/payment-gateway-rest-client-ruby](https://github.com/example/payment-gateway-rest-client-ruby/blob/master/MLE.md "")                                                             |
[**Minimum Required SDK Versions**]

Test Your Setup {#restgs-sdk-test}
==================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-5-750x200.svg/jcr:content/renditions/original)  
`Payment Gateway` recommends that you test and verify that your payment system can securely send and receive REST API messages before transitioning to a production account. Use the test examples provided in this section to test your set up. You should also test any additional API requests that you will use in your live environment.  
If you receive unsuccessful responses, verify that your security keys work and that the key information is correctly entered into the SDK.

Completing a Test Transaction {#restgs-sdk-test-transaction}
============================================================

After setting up your system to be REST compliant, you can send these test requests to verify that you can send and receive REST API messages.

> IMPORTANT  
> Depending on your payment processor, you may be required to send additional fields that are not shown in these examples.  
> Follow these steps to verify that you can complete a test transaction:

1. **Authorize a Payment**

2. You send this POST request to the `https://apitest.example.com``/pts/v2/payments` endpoint:

   ```keyword
   {
       "orderInformation": {
           "billTo": {
               "country": "US",
               "lastName": "Kim",
               "address1": "201 S. Division St.",
               "postalCode": "48104-2201",
               "locality": "Ann Arbor",
               "administrativeArea": "MI",
               "firstName": "Kyong-Jin",
               "email": "test@pgw.com"
           },
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       },
       "paymentInformation": {
           "card": {
               "expirationYear": "2031",
               "number": "4111111111111111",
               "expirationMonth": "12",
               "type": "001"
           }
       }
   }
   ```
3. You receive a successful response and store the authorization transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id" : "6461731521426399003473"
   ```
4. **Capture an Authorized Payment**

5. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/captures` endpoint and include the authorization transaction ID as the *`{id}`*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6461731521426399003473/captures
   ```

   ```
   {
       "clientReferenceInformation": {
           "code": "ABC123"
       },
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
       }
   }
   ```
6. You receive a successful response and store the capture transaction ID in the id field. A successful response is indicated by a 201 HTTP status code.

   ```
   "id": "6772994431376681303954"
   ```
7. **Refund a Captured Payment**

8. You send this POST request to the `https://apitest.example.com``/pts/v2/payments/`*{id}*`/refunds` endpoint and include the capture transaction ID as the *{id}*:

   ```keyword
   https://apitest.example.com/pts/v2/payments/6772994431376681303954/refunds
   ```

   ```
   {
       "orderInformation": {
           "amountDetails": {
               "totalAmount": "100.00",
               "currency": "USD"
           }
       }
   }
   ```
9. You receive a successful response, which verifies that your system can complete a transaction. A successful response is indicated by a 201 HTTP status code.

Going Live {#restgs-sdk-go-live-shared-secret-intro}
====================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-sdk-flow-6-750x200.svg/jcr:content/renditions/original)  
When you are ready to process payments in a live environment, you must transition your account to the live status with a valid configuration for your chosen payment processor. When your account is live, your transaction data flows through the production `Payment Gateway` gateway, to your processor, and on to the appropriate payment network.  
To transition your account:

1. Sign up for a merchant account.
2. [Contact Sales](https://www.example.com/en-us/contact-us/sales.md "") to establish a contract with `Payment Gateway` that enables you to process real transactions and receive support.
3. Submit a merchant ID (MID) activation request.

{#restgs-sdk-go-live-shared-secret-intro_d13e35}  
It can take up to three business days for the MID to become active.

Step 6A: Create a Merchant ID {#restgs-sdk-go-live-shared-secret-mid}
=====================================================================

Your merchant ID (MID) identifies you and your transactions, which requires you to include it in each transaction request. When you signed up for a sandbox account, you received a merchant ID for testing purposes. If you choose, you can use that merchant ID as your production ID.  
Follow these steps to sign up for a merchant account in order to create a production MID:

1. Go to the `Business Center` [Sandbox Account Sign Up](https://developer.example.com/hello-world/sandbox.md "") page, enter the required information, and click **Create Account**.  
   Choose your merchant ID name. It cannot be changed. This name is not visible to your customers.
2. Review your information entered, especially your business email address. Your merchant ID registration information will be sent to the email entered on this form.
   3. Look for an email from customer support titled: *`Payment Gateway` Merchant Evaluation Account*.  
      This email contains your organization ID and contact email associated with your MID.
   4. Look for an email titled: *Merchant Registration Details* . Click the **Set up your username and password now** link.  
      Your browser opens the New User Sign Up wizard.
3. Enter the organization ID and contact email you supplied previously. Follow the wizard pages to add your name, a username, and password.
   6. Log in to the `Business Center`.  
      When you log in for the first time, you will be asked to identify yourself through a system-generated email that is sent to your email account.
4. Look for an email titled: *`Payment Gateway` Identification Code*. Save the passcode in the email.
5. Enter the passcode on the Verify your Identity page. You are directed to the `Business Center` home page.

{#restgs-sdk-go-live-shared-secret-mid_d9e21}  
You have successfully created a merchant ID and merchant account.

Step 6B: Activate Your Merchant ID {#restgs-sdk-go-live-mid-shared-secret-activation}
=====================================================================================

The activation process, also known as *going live*, transitions your MID and account from test status to live status, enabling you to process real transactions. It can take up to three business days for your MID to become active.  
To transition your account, complete these steps:
1. Sign in to the [Support Center](https://support.example.com/ "") as an administrator.
   2. Enter your credentials and log in to your test environment. The organization ID is your MID.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-test-login.png/jcr:content/renditions/original)
2. In the `Business Center`, go to **Support Cases \&gt; MID Configuration Request**. The MID Configuration Request page should be open.
3. Click **MID Activation**.
4. In the **Description** field, enter the merchant ID that you want to take live.
   6. Choose a processor configuration, and enter the name of your processor.  
      If you are unsure of the processor name, contact your merchant service provider or your merchant acquiring bank.
5. Choose the environments to which this change applies (test or production).
6. Click **Service Enablement** and list the products and services that you intend to use.
7. Click **Submit**.
   {#restgs-sdk-go-live-mid-shared-secret-activation_d7e26}

Set Up an HTTP Signature Message ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-deprecating-100x20.svg/jcr:content/renditions/original) {#restgs-http-message-intro}
==================================================================================================================================================================================================================

To set up HTTP signature messaging, you must complete the tasks described in this section.

> WARNING  
> By **September 2026** , all merchants using HTTP signature messaging must migrate to JSON Web Token (JWT) messaging in order to support message-level encryption (MLE). You risk transaction failures if you do not implement this update. If you are setting up your system to be REST-compliant for the first time, ` Payment Gateway ` recommends using JWT messaging.  
> To update your system to support JWT messaging, use one of these methods:
>
> * [JWT messaging using a shared secret key pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-shared-secret-intro.md "")

* [JWT messaging using a P12 certificate](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")

#### Figure:

Set Up HTTP Signature Messaging ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-all-750x175.svg/jcr:content/renditions/original)

1. Sign up for a test account. See [Sign Up for a Sandbox Account](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-register.md "").
2. Create a shared secret key. See [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro.md "").
3. Construct a message using HTTP signature security. See [Construct Messages Using HTTP Signature Security](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-http-message-conf-intro.md "").
4. Test your REST transaction messages. See [Test Your Setup](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-test.md "").
5. Go live by transitioning your sandbox account into a production account. [Going Live](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-go-live-intro.md "").

Sign Up for a Sandbox Account {#restgs-register-http}
=====================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-1-750x175.svg/jcr:content/renditions/original)  
To begin setting up your account, you must first sign up for a sandbox account. A sandbox account enables you to obtain your security keys and test your implementation.

> IMPORTANT  
> A sandbox account cannot process live payments and is intended for only testing.  
> Follow these steps to sign up for a sandbox account:

1. Go to the `Payment Gateway` Developer Center sandbox account sign-up page:  
   [https://developer.example.com/hello-world/sandbox.html](https://developer.example.com/hello-world/sandbox.md "")

   2. Enter your information into the sandbox account form, and click **Create Account**.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-registration.png/jcr:content/renditions/original)
   3. Go to your email and find a message titled: *Merchant Registration Details* . Click **Set up your username and password now**.  
      Your browser opens the New User Sign Up wizard.
   4. Enter the organization ID and contact email you supplied when you created your account. Follow the wizard pages to add your name, a username, and a password. Your username and password must meet these requirements:

   |                                        **Username Requirements**                                        |                                                                                  **Password Requirements**                                                                                   |
   |---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | * Length must be 3-36 characters. * Can only contain letters, numbers, periods, dashes, or underscores. | * Length must be 12--50 characters. * Must contain one upper case letter. * Must contain one lower case letter. * Must contain one number. * Cannot contain the username or organization ID. |
   [Username and Password Requirements]

   5. Log in to the `Business Center`.  
      When you log in for the first time, you must verify your identity through a system-generated email sent to your email account.
2. Check your email for a message titled: *`Payment Gateway` Identification Code*. A passcode is included in the message.

   7. Enter the passcode on the *Verify your Identity* page.  
      You are directed to the `Business Center` home page.  
      You have successfully signed up for a sandbox account.

   > IMPORTANT  
   > A sandbox account cannot process live payments. After you verify that your system can send and receive REST messages, you can contact customer service to transition your sandbox account to a production account.

Create a Shared Secret Key Pair {#restgs-security-key-pair-intro}
=================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-2-750x175.svg/jcr:content/renditions/original)  
You must create a shared secret key pair to use HTTP signature message security.  
All account users can create their own unique shared secret key pair. In addition, portfolio and merchant account users can also create a *meta key* of a shared secret key pair. Meta keys enable an organization administrator to assign a single shared secret key pair to some or all transacting merchants in their organization. The purpose of a meta key is to reduce the time needed to manage an organization's keys. For example, by assigning the same meta key to all of your transacting merchants, you need to update only one key when it expires instead of having to update each transacting merchant's key when it expires.  
For more information about meta keys, see the [Meta Key Creation and Management](https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "") section in the *Creating and Using Security Keys User Guide*.

#### Figure: {#restgs-security-key-pair-intro_hierarchy}

Account Type Overview  
![](/content/dam/documentation/pgw/en-us/topics/platform/bam/partner/images/portfolio-one-merchant-account.svg/jcr:content/renditions/original)

Portfolio
:
A portfolio account represents the partner administrator user. This account type can create and manage merchant accounts in the test and production environments.

Merchant
:
A merchant account represents the merchant administrator user. This account type can create and manage multiple transacting merchant accounts in their organization.

Transacting Merchant
:
A transacting merchant represents the merchant user who is processing transactions. This account type is typically the account that sends API requests.
{#restgs-security-key-pair-intro_dl-hierarchy}

Step 2A: Creating a Shared Secret Key Pair {#restgs-security-key-pair-task}
===========================================================================

Follow these steps to create a shared secret key pair:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
     {#restgs-security-key-pair-task_step-1}
     {#restgs-security-key-pair-task_step-1}
   2. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#restgs-security-key-pair-task_step-2}
      {#restgs-security-key-pair-task_step-2}
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#restgs-security-key-pair-task_step-3}
      {#restgs-security-key-pair-task_step-3}
   4. Under REST APIs, choose **REST -- Shared Secret** and then click **Generate key**.  
      ![](/content/dam/documentation/pgw/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-create-key.png/jcr:content/renditions/original)  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
      The REST API Shared Secret Key page appears. {#restgs-security-key-pair-task_step-4-key-pair}
      {#restgs-security-key-pair-task_step-4-key-pair}
   5. Click **Download key** ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      The *.pem* file downloads to your desktop.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/shared-secret-key-download.png/jcr:content/renditions/original)  
      The **Key** value is your *key ID* and the **Shared Secret** value is your *shared secret key*.

   > IMPORTANT
   > Securely store the key credentials and *.pem* file in your system. These credentials are required in order to implement certain products, and you must be able to access them.
   > {#restgs-security-key-pair-task_step-5-key-pair}
   > {#restgs-security-key-pair-task_step-5-key-pair}

{#restgs-security-key-pair-task_steps}  
To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

**What to do next**
:
To test your shared secret key pair, see [Step 2B: Test Your Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro/restgs-security-key-pair-test-task.md "").

Step 2B: Test Your Shared Secret Key Pair {#restgs-security-key-pair-test-task}
===============================================================================

After creating your key certificate, you must verify that your key can successfully process API requests. Follow these steps to validate your key certificate in the Developer Center and the `Business Center`.

1. Go to the Developer Center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "")
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")** .
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **HTTP Signature**.
4. Enter your organization ID in the **Organization ID** field.
5. Enter your key, also known as your private key, in the **Key** field.
6. Enter your secret key, also known as your public key, in the **Shared Secret Key** field.
7. Click **Update Credentials**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-http.png/jcr:content/renditions/original)
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.
9. Click **Send**.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original)
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
11. On the left navigation panel, choose ![](/content/dam/documentation/pgw/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original)

Construct Messages Using HTTP Signature Security {#restgs-http-message-conf-intro}
==================================================================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-3-750x175.svg/jcr:content/renditions/original)  
HTTP signatures use a digital signature to enable the receiver to validate the sender's authenticity and ensure that the message was not tampered with during transit. For more information about HTTP signatures, see the [IETF Draft](https://httpwg.org/ "") that is maintained by the IETF HTTP Working Group.  
Follow these steps to create messages using HTTP signatures:  
![Step 3A: Set the known header values. Step 3B: Calculate the digest HTTP header hash value.
Step 3C: Calculate the signature hash value. Step 3D: Construct the signature HTTP
header value using all of the signature parameter values and signature hash. Step
3E: Combine the HTTP headers and HTTP message body.](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rest-gsg-http-mess-sec-800x525.svg/jcr:content/renditions/original)

HTTP Message Elements {#restgs-http-const-elements}
===================================================

An HTTP message is constructed using HTTP headers and an HTTP message body.

**HTTP Message Headers**
:
Your message header must include these HTTP header fields:

    |  HTTP Header Field  |                                                                                Description                                                                                 |
    |---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **content-type**    | Also known as the Multipurpose Internet Mail Extension (MIME) type, it is the identifier of the media or file type resource. You can set the value to: `application/json`  |
    | **host**            | The transaction endpoint (`api.example.com`).                                                                                                                          |
    | **v-c-date**        | The date of the transaction in the RFC1123 format. Example: `Thu, 18 Jul 2019 00:18:03 GMT`                                                                                |
    | **v-c-merchant-id** | Your `Payment Gateway` transacting merchant ID (MID). If you are a portfolio or merchant account user, set this to the transacting merchant ID you send requests on behalf of. |
    | **digest**          | A hash of the HTTP message body that contains your API request. The digest field does not apply to `GET` API requests.                                                     |
    | **signature**       | The digital signature, which is constructed using the values of the other headers and secured by your private key.                                                         |
    [HTTP Header Fields]

**HTTP Message Body**
:
Your API request.

Step 3A: Set Known HTTP Header Values {#restgs-message-set-known}
=================================================================

Set these HTTP header values, which do not require calculation:

content-type
:
Set to the media or file type resource.

host
:
Set to the transaction endpoint.

v-c-date
:
Set to the transaction date in RFC1123 format.

v-c-merchant-id
:
Set to a transacting merchant ID.

Step 3B: Digest Hash Calculation {#restgs-http-message-conf-payload-hash}
=========================================================================

The value of the digest HTTP header is a hashed version of the HTTP message body that you must calculate. This hash value validates the integrity of your message by the receiver.  
Follow these steps to calculate the digest hash:

1. Generate the SHA-256 hash of the JSON payload (message body).
2. Encode the hashed string to Base64.
3. Prepend **SHA-256=** to the front of the hash.
4. Add the message body hash to the digest HTTP header field.  
   Creating a Message Hash Using the Command Line `shasum` Tool

```keyword
echo -n "{"clientReferenceInformation":{"code":"TC50171_3"},"paymentInformation":{"card":{"number":
				"4111111111111111","expirationMonth":"12","expirationYear":"2031"}},"orderInformation":{"amountDetails":
				{"totalAmount":"102.21","currency":"USD"},"billTo”:{“firstName":"John","lastName":"Doe","address1":
				"1MarketSt","locality":"sanfrancisco","administrativeArea":"CA","postalCode":"94105","country":"US",
				"email":"test@pgw.com","phoneNumber":"4158880000"}}}" | shasum -a 256
```

```
echo -n "6ae5459bc8a7d6a4b203e8a734d6a616725134088e13261f5bbcefc1424fc956" | base64
```

Creating a Message Hash Using the Command Line `base64` Tool

```
echo -n "6ae5459bc8a7d6a4b203e8a734d6a616725134088e13261f5bbcefc1424fc956" | base64
```

Creating a Message Hash Using C#

```
public static string GenerateDigest() {
				var digest = "";
				var bodyText = "{ your JSON payload }";
				using (var sha256hash = SHA256.Create()) {
				byte[] payloadBytes = sha256hash
				.ComputeHash(Encoding.UTF8.GetBytes(bodyText));
				digest = Convert.ToBase64String(payloadBytes);
				digest = "SHA-256=" + digest;
				}
				return digest;
				}
```

Creating a Message Using Java

```
public static String GenerateDigest() throws NoSuchAlgorithmException {
				String bodyText = "{ your JSON payload }";
				MessageDigest md = MessageDigest.getInstance("SHA-256");
				md.update(bodyText.getBytes(StandardCharsets.UTF_8));
				byte[] digest = md.digest();
				return "SHA-256=" + Base64.getEncoder().encodeToString(digest);
				}
```

Step 3C: Signature Hash Calculation {#restgs-http-message-conf-signature}
=========================================================================

Before you can construct the signature HTTP header value, you must first generate the *signature hash*. To generate the signature hash value, you must use a Base64-encoded HMAC SHA-256 hash of the signature fields and their values.  
This table describes the signature field values that you must use to calculate the signature hash.

|   Signature Field   |                                                                                                                                                                                                                    Description                                                                                                                                                                                                                    |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **v-c-date**        | From the header, the date and time in the RFC1123 format. For example: `Date: Thu, 18 Jul 2023, 22:18:03.`                                                                                                                                                                                                                                                                                                                                        |
| **Digest**          | The Base64-encoded SHA-256 hash of the message body. For more information, see [Step 3B: Digest Hash Calculation](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-http-message-conf-intro/restgs-http-message-conf-payload-hash.md ""). Example: `Digest: SHA-256=gXWufV4Zc7VkN9Wkv9jh/JuAVclqDusx3vkyo3uJFWU=` Do not include the digest with GET requests. |
| **Host**            | From the header, the endpoint host. For example: `apitest.example.com`.                                                                                                                                                                                                                                                                                                                                                                       |
| **v-c-merchant-id** | From the header, the merchant ID associated with the request. For example: `v-c-merchant-id: mymerchantid`.                                                                                                                                                                                                                                                                                                                                       |
| **request-target**  | The HTTP method and endpoint resource path. For example: `request-target: post /pts/v2/payments`. > IMPORTANT > Verify that your request-target values match exactly the resource path. For example, ` /pts/v2/payments ` is not the same as ` /pts/v2/payments`**/**` `.                                                                                                                                                                         |
[Signature Fields]

Follow these steps to generate the signature hash value:

1. Generate a byte array of the secret key generated previously. For more information, see [Create a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro.md "").
2. Generate the HMAC SHA-256 key object using the byte array of the secret key.
3. Concatenate a string of the required information listed above.  
   For more information, see Creating the Validation String below.
4. Generate a byte array of the validation string.
5. Use the HMAC SHA-256 key object to create the HMAC SHA-256 hash of the validation string byte array.
6. Base64-encode the HMAC SHA-256 hash.

**Signature Hash**

```
signature=”OuKeDxj+Mg2Bh9cBnZ/25IXJs5n+qj93FvPKYpnqtTE=”
```

Creating the Validation String {#restgs-http-message-conf-signature_create-validation-string}
---------------------------------------------------------------------------------------------

To create the validation string, concatenate the required information in the same order as listed in the signature header field parameter. Each item must be on a separate line, and each line should be terminated with a new line character `\n`.  
**Validation String Example**

```keyword
host: apitest.example.com\n
date: Thu, 18 Jul 2019 00:18:03 GMT\n
request-target: post /pts/v2/payments/\n
digest: SHA-256=gXWufV4Zc7VkN9Wkv9jh/JuAVclqDusx3vkyo3uJFWU=\n
v-c-merchant-id: mymerchantid
```

**Generating a Signature Hash in C#**

```
private static string GenerateSignatureFromParams(string signatureParams, string secretKey) {
var sigBytes = Encoding.UTF8.GetBytes(signatureParams);
var decodedSecret = Convert.FromBase64String(secretKey);
var hmacSha256 = new HMACSHA256(decodedSecret);
var messageHash = hmacSha256.ComputeHash(sigBytes);
return Convert.ToBase64String(messageHash);
}
```

**Generating a Signature Hash in Java**

```
public static String GenerateSignatureFromParams(String keyString, 
String signatureParams) throws InvalidKeyException, NoSuchAlgorithmException {
byte[] decodedKey = Base64.getDecoder().decode(keyString);
SecretKey originalKey = new SecretKeySpec(decodedKey, 0, decodedKey.length, "HmacSHA256");
Mac hmacSha256 = Mac.getInstance("HmacSHA256");
hmacSha256.init(originalKey);
hmacSha256.update(signatureParams.getBytes());
byte[] HmachSha256DigestBytes = hmacSha256.doFinal();
return Base64.getEncoder().encodeToString(HmachSha256DigestBytes);}
```

Step 3D: Constructing the Signature Header {#restgs-http-message-headers}
=========================================================================

After you generate a signature hash, you can construct the signature HTTP header value.  
The signature HTTP header value is constructed using these parameters:

| Signature Parameter |                                                                                                                                                                                        Description                                                                                                                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **keyid**           | The serial number of the signing certificate/key pair. Obtain this in the `Business Center` Key Management area. For more information, see [Step 2A: Creating a Shared Secret Key Pair](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-security-key-pair-intro/restgs-security-key-pair-task.md ""). |
| **algorithm**       | The HMAC SHA256 algorithm used to encrypt the signature. It should be formatted: `HmacSHA256`.                                                                                                                                                                                                                                                                                             |
| **headers**         | The signed-header values calculated in the signature: * `digest` * `host` * `request-target` * `v-c-date` * `v-c-merchant-id` > IMPORTANT > If you are using a meta-key, set the v-c-merchant-id signature-parameter value to the meta-key creator's ID. Then set the v-c-merchant-id HTTP header value to the transacting merchant ID (MID) that you are sending a request on-behalf of.  |
| **signature**       | The signature hash.                                                                                                                                                                                                                                                                                                                                                                        |
[Signature Parameters]

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/rest-gsg-http-mess-sec-port-800x245.svg/jcr:content/renditions/original)

**Signature Field Format**
:
`Signature:"keyid:"[keyid]",algorithm="[encryption algoritm]",headers="field1" "field2" "field3" "etc.", signature="[signature hash]"`

**Signature Example**
:

    ```
    Signature:"keyid="123abcki-key1-key2-key3-keyid1234567", 
    algorithm="HmacSHA256", headers="host date request-target digest v-c-merchant-id", 
    signature="hrptKYTtn/VfwAdUqkrQ0HT7jqAbagAbFC6nRGXrNzE="
    ```

Step 3E: Complete Message with HTTP Signature {#restgs-http-message-complete}
=============================================================================

Combine all of the HTTP header values with your HTTP message body to construct your HTTP signature message.  
To test your message, you can send a test request to `Payment Gateway`. For more information, see [Test Your Setup](/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro/restgs-test.md "").

Test Your Setup {#restgs-test}
==============================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-4-750x175.svg/jcr:content/renditions/original)  
You can send a test API request to validate that your account, API key, HTTP headers, and HTTP message body are working as intended.  
`Payment Gateway` recommends that you test and verify that your payment system can securely send and receive REST API messages before transitioning to a production account. Use the test examples provided in this section to test your set up. You should also test any additional API requests that you will use in your live environment.

Going Live {#restgs-go-live-intro-http}
=======================================

![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/flow-keys-http-5-750x175.svg/jcr:content/renditions/original)  
When you are ready to process payments in a live environment, you must transition your account to the live status with a valid configuration for your chosen payment processor. When your account is live, your transaction data flows through the production `Payment Gateway` gateway, to your processor, and on to the appropriate payment network.  
To transition your account:

1. Sign up for a merchant account.
2. [Contact Sales](https://www.example.com/en-us/contact-us/sales.md "") to establish a contract with `Payment Gateway` that enables you to process real transactions and receive support.
3. Submit a merchant ID (MID) activation request.

{#restgs-go-live-intro-http_d13e35}  
It can take up to three business days for the MID to become active.

Step 5A: Create a Merchant ID {#restgs-go-live-mid-http}
========================================================

Your merchant ID (MID) identifies you and your transactions, which requires you to include it in each transaction request. When you signed up for a sandbox account, you received a merchant ID for testing purposes. If you choose, you can use that merchant ID as your production ID.  
Follow these steps to sign up for a merchant account in order to create a production MID:

1. Go to the `Business Center` [Sandbox Account Sign Up](https://developer.example.com/hello-world/sandbox.md "") page, enter the required information, and click **Create Account**.  
   Choose your merchant ID name. It cannot be changed. This name is not visible to your customers.
2. Review your information entered, especially your business email address. Your merchant ID registration information will be sent to the email entered on this form.
   3. Look for an email from customer support titled: *`Payment Gateway` Merchant Evaluation Account*.  
      This email contains your organization ID and contact email associated with your MID.
   4. Look for an email titled: *Merchant Registration Details* . Click the **Set up your username and password now** link.  
      Your browser opens the New User Sign Up wizard.
3. Enter the organization ID and contact email you supplied previously. Follow the wizard pages to add your name, a username, and password.
   6. Log in to the `Business Center`.  
      When you log in for the first time, you will be asked to identify yourself through a system-generated email that is sent to your email account.
4. Look for an email titled: *`Payment Gateway` Identification Code*. Save the passcode in the email.
5. Enter the passcode on the Verify your Identity page. You are directed to the `Business Center` home page.

{#restgs-go-live-mid-http_d9e21}  
You have successfully created a merchant ID and merchant account.

Step 5B: Activate Your Merchant ID {#restgs-go-live-mid-activation-http}
========================================================================

The activation process, also known as *going live*, transitions your MID and account from test status to live status, enabling you to process real transactions. It can take up to three business days for your MID to become active.  
To transition your account, complete these steps:
1. Sign in to the [Support Center](https://support.example.com/ "") as an administrator.
   2. Enter your credentials and log in to your test environment. The organization ID is your MID.  
      ![](/content/dam/documentation/pgw/en-us/topics/platform/rest/getting-started/images/restgs-test-login.png/jcr:content/renditions/original)
2. In the `Business Center`, go to **Support Cases \&gt; MID Configuration Request**. The MID Configuration Request page should be open.
3. Click **MID Activation**.
4. In the **Description** field, enter the merchant ID that you want to take live.
   6. Choose a processor configuration, and enter the name of your processor.  
      If you are unsure of the processor name, contact your merchant service provider or your merchant acquiring bank.
5. Choose the environments to which this change applies (test or production).
6. Click **Service Enablement** and list the products and services that you intend to use.
7. Click **Submit**.
   {#restgs-go-live-mid-activation-http_d7e26}

Production Endpoints {#restgs-endpoints-live-http}
==================================================

Send API requests using your production account to the production server:  
`https://api.example.com`  
For example, send a live authorization request to this endpoint:  
`https://api.example.com``/pts/v2/payments`

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.
