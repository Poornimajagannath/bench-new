Creating and Using Security Keys User Guide {#reference.dita_a3d5a5d5-8523-48e8-80d6-82dd712058cb}
==================================================================================================

This section describes how to use this user guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to use `Payment Gateway` services that require a security key, including API requests.

Related Documentation
:
Refer to the Technical Documentation Portal for more technical documentation:

    [https://developer.example.com/docs.html](https://developer.example.com/docs.md "")

    Visit the [`Payment Gateway` documentation hub](https://developer.example.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.example.com>

Recent Revisions to This Document {#keys-revisions}
===================================================

25.12.01
--------

Updated information about how to create, submit, and test the API Response MLE Certificate for the REST API. See [REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-rest-mle-intro.md "").  
Changed title of the *Message-Level Encryption Keys* section to Token Management MLE Keys. See [Token Management MLE Keys](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-mle-intro.md "").

25.10.01
--------

Added support for creating or submitting an API Response MLE Certificate for the REST API. See [Create or Submit a REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-security-mle-reply.md "").

25.08.01
--------

Added support for submitting a certificate signing request (CSR) as a REST API key. See [Submit a Certificate Signing Request](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-rest-intro/restgs-security-P12-upload.md "").

25.04.01
--------

Added information about `Payment Gateway` no longer supporting the SOAP toolkit key type. See the important note in [Introduction to Creating and Using Security Keys](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-intro.md "") and [SOAP Toolkit Keys](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-soap-intro.md "").

25.03.01
--------

Updated the available filters for searching for keys. See [Search for Keys Using Filters](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-managing/key_search.md "").  
Updated how to create a meta key for portfolio users and merchant account users. See [Create a Meta Key as a Portfolio User](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-create.md "") and [Create a Meta Key as a Merchant Account User](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-create-account.md "").  
Added information about removing a meta key from all merchants and select merchants. See [Remove a Meta Key from all Merchants](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-assign-all-revoke.md "") and [Remove a Meta Key from Select Merchants](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-assign-all-revoke-selection.md "").

24.08.01
--------

:
This revision contains only editorial changes and no technical updates.

24.06.01
--------

:
This revision contains only editorial changes and no technical updates.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Creating and Using Security Keys {#keys-intro}
==============================================================

`Payment Gateway` requires you to use security keys when sending and receiving API messages. This guide explains how to create and manage your security keys using the `Business Center`.  
A security key, also known as a *cryptographic key*, is a string of randomly or mathematically generated characters that are tied to a specific cryptographic algorithm. These keys are used to:

* Encrypt plain text to allow users to send text across the internet with confidence that the content is secure.
* Decrypt the encrypted message so that the text can be read by the intended recipient.
* Validate that the encrypted message has not been tampered with while in transit.

These are the available `Payment Gateway` security keys:

* Message-Level Encryption (MLE) Keys
* Meta Keys
* PGP Keys
* REST API Keys
* Secure Acceptance Keys
* Simple Order Keys
* SOAP Toolkit Keys

> WARNING
> Payment Gateway will no longer support SOAP toolkit keys by these dates:
>
> * **Test environment:** July 16, 2025
> * **Production environment:** August 13, 2025
>
> If you are integrating to the Simple Order API, you can use the compliant certificate-based *Simple Order key* . For more information, see [Simple Order API Keys](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-simple-order-intro.md "").  
> If your payment system currently uses the SOAP toolkit key, you can transition your payment system to use the certificate-based Simple Order API key. For more information about how to transition your payment system to use the compliant Simple Order API keys for authentication, see the [*P12 Authentication for SOAP Toolkit Key Users Migration Guide*](https://developer.example.com/docs/gateway/en-us/so-p12/migration/all/so/so-p12/so-p12-intro.md ""). Your API requests to ` Payment Gateway ` will be rejected if you do not implement P12 authentication by the above dates.

Additional Information
----------------------

For more information about cryptographic keys, see the *[Key (Cryptography)](https://en.wikipedia.org/wiki/Key_(cryptography) "")* article on Wikipedia.

Create a Security Key {#keys-manage}
====================================

This section describes how to create your security keys using the `Business Center`.  
In the `Business Center`, you can use the Dashboard or Key Management to create your keys. These keys can be downloaded for you to securely store in your system.

`Business Center` Dashboard
---------------------------

When you log in to the `Business Center`, the dashboard appears. You can use the Security Keys dashboard to:

* View any keys that will expire soon.
* Go directly to the Key Management page by clicking **View All Keys**.
* Create a new key by clicking **Generate new key**.

#### Figure: {#keys-manage_d28e63}

`Business Center` Dashboard ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/dashboard.PNG/jcr:content/renditions/original)

Key Management
--------------

When you log in to the `Business Center`, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management** to access the Key Management page.  
You can use the Key Management page to:

* Search for an existing key.
* Delete an existing key.
* Create a new key by clicking **Generate new key**.
* View any keys that will expire soon.

PGP Keys {#keys-pgp-intro}
==========================

`Payment Gateway` uses Pretty Good Privacy (PGP) encryption for Account Updater response files and Notice of Change (NOC) reports.  
For information about Account Updater, see the [*Account Updater User Guide*](http://apps.example.com/library/documentation/dev_guides/Account_Updater_UG/Account_Updater.pdf ""). For information about NOC reports, see [*Electronic Check Services Developer Guide*](https://docs.example.com/content/dam/new-documentation/documentation/en/e-checks/developer/all/so/e-checks-so.pdf "").  
A PGP public/private key pair enables you to use encryption to protect payment data. You exchange the public part of this key pair with `Payment Gateway`, which uses the public key to encrypt response files or NOC reports. You use the private part of the key pair to decrypt the response files or NOC reports. Only the private key can decrypt files that are encrypted with the public key.  
Key information:

* PGP keys expire after 3 years.
* Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.
* You must use separate keys for the test and production environments.

Creating PGP Keys {#keys-pgp-create}
====================================

You can use any OpenPGP-compliant software to generate Pretty Good Privacy (PGP) keys. The key that you generate must be an RSA key. These free OpenPGP solutions are available:

* [Bouncy Castle](http://www.bouncycastle.org/ "")
* [GPG4WIN](http://www.gpg4win.org "")

`Payment Gateway` recommends that you follow these guidelines:

* Make the key at least 2048 bits long.
* Store the private key in an encrypted format to protect it from unauthorized use.
* Back up the private key in case of disaster.

Place the backup of the private key on removable media, and lock it in secure storage.  
`Payment Gateway` does not receive a copy of your private key and cannot decrypt files that are encrypted with your public key. After you create a public/private key pair, add the public key to the `Business Center` as described in the next section.

Adding a PGP Key to Your Account {#keys-pgp-add}
================================================

Follow these steps to add a PGP key to your account:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-pgp-add_d10e35}
3. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
4. Select **PGP** and click **Generate key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)
5. Enter the ASCII string into the text field, and click **Create key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-pgp-create.png/jcr:content/renditions/original)

Granting User Permissions {#keys-pgp-permissions-create}
========================================================

A user account requires certain permissions in order to work with PGP keys and the Account Updater request files and reports. Follow these steps to grant user permissions:

1. Log in to the `Business Center`.
2. On the left navigation panel, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-accnt-mgmt.svg/jcr:content/renditions/original) **Account Management \&gt; Roles**.
3. Choose the role that needs to work with PGP keys and click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit User Role page appears.
4. Choose from these permissions:
   1. Under Credit Card Account Updater Permissions, choose **View Status**.  
      This option enables the user to view the status of uploaded Account Updater request files and NOC reports.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-pgp-cc.png/jcr:content/renditions/original)
   2. Under Merchant Settings Permissions, choose **PGP Security Settings**.  
      This option gives the user permission to upload, activate, and deactivate encryption keys.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-merch-set.png/jcr:content/renditions/original)
   3. Under Reporting Permissions, choose **Report Download**.  
      This option gives the user permission to download Account Updater response files and NOC reports.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-acctup.png/jcr:content/renditions/original)
5. Click **Save** when done.

REST API Keys {#keys-rest-intro}
================================

REST API keys are used to enable secure communication between you and `Payment Gateway` when using the REST API.  
The REST API supports these two types of security keys:

* **Certificates** for using JSON Web Token authentication.
* **Shared secret key pair** for using HTTP signature authentication.  
  You can create these keys using the `Business Center` or submit your own public PEM-formatted certificate to use as your security key.  
  IMPORTANT REST API keys expire after 3 years.  
  Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.  
  You must use separate keys for the test and production environments.  
  When you sign up for a [Sandbox account](https://developer.example.com/hello-world/sandbox.md ""), your confirmation email contains a shared secret key pair.

Create a P12 Certificate {#restgs-task-p12}
===========================================

Follow these steps to create a *.p12* file if you are using JSON Web Tokens to secure communication.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
     {#restgs-task-p12_step-1}
     {#restgs-task-p12_step-1}
   2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#restgs-task-p12_step-2}
      {#restgs-task-p12_step-2}
   3. Click + Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#restgs-task-p12_step-3}
      {#restgs-task-p12_step-3}
   4. Under REST APIs, choose REST -- Certificate, and then click Generate key.  
      If you are using a *portfolio* account, the Key options window appears, giving you the choice to create a meta key. For more information about how to create a meta key, see [Meta Key Creation and Management](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "").  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-select.png/jcr:content/renditions/original) {#restgs-task-p12_step-4}
      {#restgs-task-p12_step-4}
   5. Click Download key ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-generate.png/jcr:content/renditions/original) {#restgs-task-p12_step-5}
      {#restgs-task-p12_step-5}
   6. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
      The *.p12* file downloads to your desktop.  
      If prompted by your system, approve the location for where the key downloads. {#restgs-task-p12_step-6}
      {#restgs-task-p12_step-6}

{#restgs-task-p12_steps}  
You can create or upload another key by clicking **Generate another key**. To view all of your created keys, use the Key Management page.

> IMPORTANT
> Securely store the *.p12* file and password in your system. These credentials are required to implement certain products and you must be able to access them.

Submit a Certificate Signing Request {#restgs-security-P12-upload}
==================================================================

Follow these steps to submit your own public PEM-formatted certificate signing request (CSR) if you are using JSON Web Tokens to secure communication. You also have the option to create a P12 certificate from your CSR to use for testing purposes.

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
   4. Under REST APIs, choose REST -- Certificate, and then click Generate key.  
      If you are using a *portfolio* account, the Key options window appears, giving you the choice to create a meta key. For more information about how to create a meta key, see [Meta Key Creation and Management](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "").  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-select.png/jcr:content/renditions/original)
2. Enter your public PEM-formatted certificate in the text box, then click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
   If you need to generate your own CSR and private key, run this command. In this example, *merchant* is your organization or merchant ID (MID). You can extract the certificate value by opening the *example.csr* file using a text editor application.

   ```
   openssl req -new -newkey rsa:2048 -keyout private_key.pem -out example.csr -sha256 -nodes -subj "/CN=merchant"
   ```

   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-fill.png/jcr:content/renditions/original)

3. (Optional) To convert your submitted CSR into a *.p12* file, run this command. In this example, *merchant* is your organization or merchant ID (MID).  
   You can use the P12 certificate for testing using the [*REST API Reference*](https://developer.example.com/api-reference-assets/index.md#payments "") on the Developer Center.

   ```
   openssl pkcs12 -export -name "$(printf 'serialnumber=%s,cn=%s' "$(openssl x509 -in merchant_certChain.pem -noout -serial | cut -d= -f2 | xxd -r -p)" "$(openssl x509 -in merchant_certChain.pem -noout -subject | sed -n 's/.*CN=\([^/]*\).*/\1/p')" )" -out merchant.p12 -inkey private_key.pem -in merchant_certChain.pem
   ```
4. When prompted, set a password for the *.p12* file.

You can create or upload another key by clicking **Generate another key**. To view all of your created keys, use the Key Management page.
IMPORTANT Securely store your key's password in your system. These credentials are required to implement certain products and you must be able to access them.

Transacting Merchant User: Create a Shared Secret Key Pair {#restgs-security-key-pair-task}
===========================================================================================

Follow these steps to create a shared secret key pair. IMPORTANT Only transacting merchant account users can complete this task.

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
     {#restgs-security-key-pair-task_step-1}
     {#restgs-security-key-pair-task_step-1}
   2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#restgs-security-key-pair-task_step-2}
      {#restgs-security-key-pair-task_step-2}
   3. Click + Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#restgs-security-key-pair-task_step-3}
      {#restgs-security-key-pair-task_step-3}
   4. Under REST APIs, choose **REST -- Shared Secret** and then click **Generate key**.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-create-key.png/jcr:content/renditions/original)  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
      The REST API Shared Secret Key page appears. {#restgs-security-key-pair-task_step-4-key-pair}
      {#restgs-security-key-pair-task_step-4-key-pair}
   5. Click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      The *.pem* file is downloaded to your desktop.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/shared-secret-key-download.png/jcr:content/renditions/original) {#restgs-security-key-pair-task_step-5-key-pair}
      {#restgs-security-key-pair-task_step-5-key-pair}

{#restgs-security-key-pair-task_steps}  
You can create or upload another key by clicking **Generate another key**. To view all of your created keys, use the Key Management page.

> IMPORTANT
> Securely store the *.p12* file and password in your system. These credentials are required to implement certain products and you must be able to access them.

**What to do next**
:
To test your shared secret key pair, see [Test Your Shared Secret Key Pair](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-security-key-pair-test-task.md "").

REST---API Response MLE Key {#keys-rest-mle-intro}
==================================================

This section describes how to create, submit, and test a REST---API response MLE key.  
Message-Level Encryption (MLE) enables you to store information or communicate with other parties while helping to prevent uninvolved parties from understanding the stored information. MLE is required only for certain payments services. Enabling MLE requires you to create a *REST -- API Response MLE* key. If your organization is using a meta key, the portfolio account or merchant account that created the meta key must also create the REST -- API Response MLE key.  
MLE is required for APIs that primarily deal with sensitive transaction data, both financial and non-financial. These are the types of sensitive transaction data:

* Personal identification information (PII)
* Personal account number (PAN)
* Personal account information (PAI)
  {#keys-rest-mle-intro_d22e40}  
  MLE is supported when using JSON web tokens.

Additional Information
----------------------

For information about how to implement MLE in your system, see the [Enable Message-Level Encryption](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-mle-intro.md "") section in the *Getting Started with REST* Developer Guide.

Create or Submit a REST---API Response MLE Key {#concept}
=========================================================

Before you can enable your system to support MLE, you must create or upload an *REST---API response MLE* certificate. After creating or uploading the certificate, you can extract the certificate's key to begin enabling MLE.  
Follow these steps to create or submit an API Response MLE certificate using the `Business Center`:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
2. Under REST APIs, choose **REST -- API Response MLE** , and then click **Generate key** .  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply.png/jcr:content/renditions/original)

3. Choose one of these options to download your key:

   * To create a new API response MLE certificate, click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .
   * To upload your own certificate, enter your public PEM-formatted certificate in the text box, then click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) . The *.pem* file downloads to your desktop. If prompted by your system, approve the location for where the file downloads.

   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply-submit.png/jcr:content/renditions/original)
   6. If you are creating a certificate, the Set a Password window appears. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
   The *.p12* file downloads to your desktop. If prompted by your system, approve the location for where the key downloads.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
   You can create or upload another key by clicking **Generate another key**. To view all of your created keys, use the Key Management page.

   > IMPORTANT
   > Securely store the *.p12* file and password in your system. These credentials are required to implement certain products and you must be able to access them.

4. Click **Cancel** .  
   The Key Management page appears.

5. Click the Key Type filter and choose **REST-API Response MLE**.

6. Click the Expires At filter and choose **All Dates**.

7. Click **Search**.

8. Find the REST--API Response key that you created in the Search Results table and save its key ID.  
   The key ID is needed to test and configure your system to use MLE.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-key-mgmt.png/jcr:content/renditions/original)

**Test Your REST--API Response MLE Key**
:
To test your REST--API Response key, see [Test Your API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-rest-mle-intro/keys-rest-mle-test.md "").

Test Your API Response MLE Key {#keys-rest-mle-test}
====================================================

Follow these steps to verify that your API response MLE key is working using the API Reference in the Developer Center. If you have not already created or submitted an API response MLE certificate, see [Create or Submit a REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-security-mle-reply.md "").

1. Go to the API Reference in the `Payment Gateway` Developer Center:  
   [`https://developer.example.com/api-reference-assets/index.html#static-home-section`](https://developer.example.com/api-reference-assets/index.md#static-home-section "")

2. Choose an API that supports MLE on the left navigation panel.  
   MLE support is indicated by **Request MLE** and **Response MLE** at the top of the screen.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-tags.png/jcr:content/renditions/original)

3. Choose the **MLE Configuration** tab.

4. Enter your API response MLE key credentials in the Message Level Encryption Credentials section:

   * **Response encryption:** Enter the key ID of your API response MLE key.  
     This is the key ID that you saved in Step 10 in [Create or Submit a REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-security-mle-reply.md "").
   * **Response decryption:** Click **Browse** to submit your own decryption private key from your local system. Only *.p12* files are supported.

   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-upload.png/jcr:content/renditions/original) {#keys-rest-mle-test_step-4}
   {#keys-rest-mle-test_step-4}

5. Click **Update Credentials**.

6. Click the Send drop-down menu icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-arrow-up.svg/jcr:content/renditions/original) ) in the Request: Live Console section and choose **Send Request with Message Level Encryption**.

7. Click **Send** .  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-send.png/jcr:content/renditions/original)

8. If a *Success: HTTP Status Code: 201* message displays in the Response section, your API response key is properly configured.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-success.png/jcr:content/renditions/original)

Secure Acceptance Key {#keys-secure-acceptance-intro}
=====================================================

Secure Acceptance API keys are used to enable secure communication between you, the merchant, and `Payment Gateway` when using the Secure Acceptance features and APIs.  
Key information:

* Secure Acceptance keys expire after 2 years.
* Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.
* You must use separate keys for the test and production environments.

Creating a Secure Acceptance Key {#keys-secure-acceptance-create}
=================================================================

Follow these steps to create a Secure Acceptance key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-secure-acceptance-create_d10e35}
3. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
4. Select **Secure Acceptance** and click **Generate Key**.  
   The Key Generation page appears.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-sa-page.png/jcr:content/renditions/original)
5. Enter the required information in these fields:
   * Key Name: enter a name for this key.
   * Signature Version: select **1** from the drop-down menu.
   * Signature Method: select **HMAC-SHA256** from the drop-down menu.
   * Security Profile: select a security profile from the drop-down menu.
6. Click **Generate Key** when done.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
   The Key Generation page appears.
7. To obtain the access key and secret key, either:
   * Copy the keys to your clipboard by clicking the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-copy.svg/jcr:content/renditions/original) copy button.

* Download a text file containing both keys by clicking **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .

Simple Order API Keys {#keys-simple-order-intro}
================================================

Simple Order API keys are used to enable secure communication between the merchant and your `Payment Gateway` when using Simple Order APIs.  
Key information:

* Simple Order API keys expire after 3 years.
* Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.
* You must use separate keys for the test and production environments.

Creating a Simple Order API Key {#keys-simple-order-create}
===========================================================

Follow these steps to create a Simple Order API key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-simple-order-create_d10e35}
3. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
4. Select **Simple Order API** and click **Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-so-select.png/jcr:content/renditions/original)  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original) {#keys-simple-order-create_step-4}
   {#keys-simple-order-create_step-4}
5. Click **Download key** to download the .p12 file.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/so-generate-key.png/jcr:content/renditions/original)  
   The **Set Password** page appears. {#keys-simple-order-create_step-5}
   {#keys-simple-order-create_step-5}
6. Enter your new password and confirm it.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original) {#keys-simple-order-create_step-6}
   {#keys-simple-order-create_step-6}
7. Click **Generate Key** when done.{#keys-simple-order-create_step-7}
   {#keys-simple-order-create_step-7}
8. The .p12 file that contains your Simple Order API key downloads to your desktop.

   > IMPORTANT Store your .p12 file in a secure location with restricted access.
   > {#keys-simple-order-create_step-8}
   > {#keys-simple-order-create_step-8} {#keys-simple-order-create_steps}

SOAP Toolkit Keys {#keys-soap}
==============================

> WARNING
> Payment Gateway will no longer support SOAP toolkit keys by these dates:
>
> * **Test environment:** July 16, 2025
> * **Production environment:** August 13, 2025
>
> If you are integrating to the Simple Order API, you can use the compliant certificate-based *Simple Order key* . For more information, see [Simple Order API Keys](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-manage/keys-simple-order-intro.md "").  
> If your payment system currently uses the SOAP toolkit key, you can transition your payment system to use the certificate-based Simple Order API key. For more information about how to transition your payment system to use the compliant Simple Order API keys for authentication, see the [*P12 Authentication for SOAP Toolkit Key Users Migration Guide*](https://developer.example.com/docs/gateway/en-us/so-p12/migration/all/so/so-p12/so-p12-intro.md ""). Your API requests to ` Payment Gateway ` will be rejected if you do not implement P12 authentication by the above dates.  
> SOAP toolkit keys are used to enable secure communication between the merchant and `Payment Gateway` when using the SOAP toolkit.  
> Key information:

* SOAP Toolkit keys expire after 3 years.
* Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.
* You must use separate keys for the test and production environments.

Creating a SOAP Toolkit Key {#keys-soap-create}
===============================================

Follow these steps to create a SOAP Toolkit key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-soap-create_d10e35}
3. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
4. Select **SOAP Toolkit** and click **Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-soap-select.png/jcr:content/renditions/original)  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
   The Key Generation page appears.
5. To obtain the SOAP Toolkit Key, either:
   * Copy the generated key to your clipboard by clicking the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-copy.svg/jcr:content/renditions/original) clipboard button.
   * Download the generated key to your desktop by clicking **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
     ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/sotoolkit-generate-key.png/jcr:content/renditions/original)

Token Management MLE Keys {#keys-mle-intro}
===========================================

Token Management Message-Level Encryption (MLE) keys are required to send `Token Management Service` (`TMS`) related requests that use encryption. To create an Token Management MLE key, go to the `Business Center`.  
Key information:

* Message-level encryption keys expire after 3 years.
* Security keys can be used to make any request, including payments. Treat your security keys as you would any secure password.
* You must use separate keys for the test and production environments.

Creating a Token Management MLE Key {#keys-mle-create}
======================================================

Follow these steps to create a token management message-level encryption key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-mle-create_d10e35}
3. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
4. Select **Message-Level Encryption** and click **Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-mle.png/jcr:content/renditions/original)  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)
5. Enter the public key value into the text field, and click **Create Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-mle-value.png/jcr:content/renditions/original)

Manage a Security Key {#keys-managing}
======================================

This section describes how to manage your security keys using the `Business Center`, such as searching for keys and deleting keys.  
In the `Business Center`, you can use the `Business Center` dashboard or key management to manage your keys.

`Business Center` Dashboard
---------------------------

When you log in to the `Business Center`, the dashboard appears. You can use the Security Keys dashboard to:

* View any keys that will expire soon.
* Go directly to the Key Management page by clicking **View All Keys**.
* Create a new key by clicking **Generate new key**.

#### Figure: {#keys-managing_d28e63}

`Business Center` Dashboard ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/dashboard.PNG/jcr:content/renditions/original)

Key Management
--------------

When you log in to the `Business Center`, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management** to access the Key Management page.  
You can use the Key Management page to:

* Search for an existing key.
* Delete an existing key.
* Create a new key by clicking **Generate new key**.
* View any keys that will expire soon.

Deactivate a Key {#deactivate_key}
==================================

You can deactivate these key types when you no longer need to use them:

* PGP keys
* Message-level encryption (MLE) keys
* `Secure Acceptance` keys  
  Keys automatically deactivate when they reach the expiration date.  
  Follow these steps to deactivate security keys:

1. On the left navigation panel, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **`Payment Configuration` \&gt; Key Management**.  
   The Key Management page appears.
2. Find the key in the table of keys, or search for one using the search filters. Then click the link for that key in the Keys column.  
   The Key Information page appears.
3. Click the ![](/content/dam/new-documentation/documentation/en-us/olh/PaymentConfiguration/images/deactivate.PNG/jcr:content/renditions/original) **Deactivate** button.
4. Click **Yes**.

Delete a Key {#delete_key}
==========================

You can delete a key when you no longer need to use it for payment processing.  
Keys become inactive when they reach the expiration date.  
Follow these steps to delete a security key:

1. On the left navigation panel, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **`Payment Configuration` \&gt; Key Management**.  
   The Key Management page appears.
2. In the table of keys, find the key that you want to delete and click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-delete-row.svg/jcr:content/renditions/original) delete row button in the row for that key.  
   The Delete Confirmation window displays.  
   ![](/content/dam/new-documentation/documentation/en-us/olh/PaymentConfiguration/images/security-keys-delete-keys.png/jcr:content/renditions/original)
3. Click **Delete**.  
   The key is deleted.  
   ![](/content/dam/new-documentation/documentation/en-us/olh/PaymentConfiguration/images/security-keys-delete-keys-window.png/jcr:content/renditions/original)

Search for Keys Using Filters {#key_search}
===========================================

Key Management enables you to search for keys using filters, which set parameters that determine the keys in the search results. Follow these steps to search for keys using filters:

1. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **`Payment Configuration` \&gt; Key Management**.

2. Under Search Filters, use these drop-down menus to set the parameters of your search:

   |           Search Filters            |                                                                                                                                                                                                                                                                                                                                                                                                        Filter Descriptions                                                                                                                                                                                                                                                                                                                                                                                                        |
   |-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | **Created At**                      | Choose a date range to search for keys that were created within a certain date range. The default value is all dates. To search by a specific date, click **Custom Date** and then set these fields: * **Start Date** * **End Date**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | **Expires In**                      | Choose a date range to search for keys that are expiring within that date range. The default value displays keys expiring within the next 60 days. To search by a specific date, click **Custom Date** and then set these fields: * **Start Date** * **End Date**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Key ID**                          | Enter a key ID to search for a key by its ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | **Key Status**                      | Choose to search by the key status: * **Active:** Search for active keys. * **Inactive:** Search for inactive keys. * **All (default):** Search for both active or inactive keys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Key Type**                        | Choose a key type to search for keys based on its key type. > IMPORTANT > The default key type of **All** does not include these key types, which must be chosen individually to retrieve in a search: > * ISV Bridge > * Message Level Encryption (MLE) > * Mobile Points of Sale (MPOS) > * Pretty Good Privacy (PGP) > * ` Secure Acceptance `                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Merchant (portfolio users only)** | If you are logged into a portfolio-level account, choose a merchant. The default value is the organization ID that you are using to access the `Business Center`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Number of Records Per Page**      | Choose the amount of keys that will display in each results page from these options: * **25 (default)** * **50** * **100**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Sort Order**                      | Choose an order in which the key results will display from these options: * **Created Newest:** List keys in sequential order of when they were created, beginning with the most recent created key and ending with the oldest created key. * **Created Oldest:** List keys in sequential order of when they were created, beginning with the oldest created key and ending with the most recent created key. * **Expiring Last:** List keys in sequential order of their expiration dates, beginning with the key that has the soonest expiration date and ending with the key that has the last expiration date. * **Expiring Soon (default):** List keys in sequential order of their expiration dates, beginning with the key that has the last expiration date and ending with the key that has the soonest expiration date. |
   [Search Filters]

3. Click **Search** when done.  
   You can also reset the filters back to their default settings by clicking **Reset Search**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-search-filters.png/jcr:content/renditions/original)  
   The Search Results section displays a table with your key results based on the filter options you chose.

Meta Key Creation and Management {#keys-meta-intro}
===================================================

A meta key is a specialized API key that a portfolio or merchant account user can create for the purposes of processing transactions on behalf of multiple of their transacting MID accounts. Meta keys are useful for organizations whose transacting MID users do not manage or store their own individual API keys. Instead of having to create and assign a unique API key for each of your transacting MIDs, you can create and assign a single meta key to dozens or hundreds of your transacting MIDs simultaneously.  
IMPORTANT Transacting MIDs cannot generate meta keys. For security reasons, do not give a meta key to your transacting MID users.  
Meta keys are available for these APIs:

* REST
* Simple Order API
* SOAP
* SCMP
  {#keys-meta-intro_ul_pbd_hts_55b}  
  When you are logged in to a portfolio account or merchant account in the `Business Center`, you can assign a meta key to a static subset of transacting MIDs or to all current and future transacting MIDs. If you choose to assign a meta key to only a subset of transacting MIDs, you can reassign the key later to all current and future transacting MIDs.  
  When using a meta key, the portfolio account or merchant account user submits a transaction on behalf of the transacting MID. These processed transactions are recognized as belonging to the transacting MID. Searching for or reporting on the transactions are performed at the transacting MID level. All three account types can process follow-on transactions to the initial transaction, such as a capture or refund.  
  Access to creating and managing meta keys is automatically enabled for all organizations. You can disable the meta key feature to not allow portfolio or merchant account users to generate meta keys or process transactions using meta keys.

> WARNING When a meta key expires, it expires for all transacting MIDs to which it is assigned. All transactions using that meta key will fail. Careful monitoring is necessary to track meta key expiration dates. You must create and assign a new key before the previous key expires. The length of time after which a key expires depends on the API for which the key was created. Read the instructions for the API key you will use.

Hierarchy of Meta Keys
----------------------

In this diagram, if the portfolio user assigns a meta key to all of the transacting MIDs, every transacting MID in the diagram is assigned the key. If one of the merchant accounts assigns a meta key to all of the transacting MIDs, only the transacting MIDs belonging to that merchant account are assigned the key. The portfolio or merchant account user can also choose specific transacting MIDs to assign the meta key to.

#### Figure:

Portfolio Hierarchy Example ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/partner/images/portfolio-two-merchant-account-600x300.svg/jcr:content/renditions/original)

Create a Meta Key as a Portfolio User {#keys-meta-create}
=========================================================

This section describes how to create a meta key as a portfolio user in the `Business Center`.  
IMPORTANT If you would like to create meta keys using the API, contact your support team for more information.  
Follow these steps to create a meta key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-meta-create_d10e35}
3. In the **Merchant ID** field, choose your portfolio ID if it is not already chosen by default.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-merchant-id.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg) {#keys-meta-create_step-3}
   {#keys-meta-create_step-3}
4. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
5. Choose a key type and click **Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-create-key.png/jcr:content/renditions/original)  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-generate-key.png/jcr:content/renditions/original)  
   The Key options window appears. {#keys-meta-create_step-4}
   {#keys-meta-create_step-4}
6. Check the **Create as a Meta-Key** box and click **Continue**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta1.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg) {#keys-meta-create_step-5}
   {#keys-meta-create_step-5}
7. Choose one of these options to assign the key:
   * To assign this key to all accounts in the current portfolio, choose **All current and future Merchant IDs** , click **Create key**, and continue to the Create Key page. All future merchant IDs will be automatically assigned this key. You are done and do not need to proceed with the following steps.
   * To assign this key to a specific merchant or group of merchants, choose **Custom Merchant ID selection** and then click **Create key**. This key is not automatically assigned to any future merchants. Proceed to the following steps.  
     ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta2.PNG/jcr:content/renditions/original) {#keys-meta-create_step-6}
     {#keys-meta-create_step-6}
8. Click **+ Add custom merchant ids**. The Add Custom Merchant IDs page appears.  
   By default, all merchant IDs are shown in the Merchant IDs table. To limit the list to a subset of merchant IDs, click **+ Add filter** , select a search filter from the drop-down menu, and click **Search**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta3.PNG/jcr:content/renditions/original) {#keys-meta-create_step-7}
   {#keys-meta-create_step-7}
9. Use the check boxes to choose one or more transacting MID accounts, and click **Submit**.  
   The Key Generation page opens. {#keys-meta-create_step-8}
   {#keys-meta-create_step-8}
10. Click **Create key**.  
    Continue to the Create Key page to view your new key.  
    You can also generate a new key by clicking **+ Generate Key** again. {#keys-meta-create_step-9}
    {#keys-meta-create_step-9}

Create a Meta Key as a Merchant Account User {#keys-meta-create-account}
========================================================================

This section describes how to create a meta key as a merchant account user in the `Business Center`.  
IMPORTANT If you would like to create meta keys using the API, contact your support team for more information.  
Follow these steps to create a meta key:

1. Log in to the `Business Center`:  
   [`https://businesscentertest.example.com`](https://businesscentertest.example.com/ebc2/ "")
2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.  
   If you are using a portfolio account to create a meta key for one of your merchant accounts, you can switch to a merchant account by clicking **Switch merchant**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-switch-merchant.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg)  
   The Quick Merchant Switch window appears.  
   Choose the merchant account ID that you want to switch to. Click **Switch** when done.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-merchant-switch.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg) {#keys-meta-create-account_step-2}
   {#keys-meta-create-account_step-2}
3. In the **Merchant ID** search filter, choose your merchant account ID.  
   If you logged in from a portfolio user account or the account (*_acct* ) level, verify that the merchant ID you choose does not contain *_acct* in the ID name.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-merchant-field.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg) {#keys-meta-create-account_step-3}
   {#keys-meta-create-account_step-3}
4. Click **+ Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)  
   The Create Key page appears.
5. Choose a key type and click **Generate Key**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-create-key.png/jcr:content/renditions/original)  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-keymgmt-generate-key.png/jcr:content/renditions/original)  
   The Key options window appears.
6. Check the **Create as a Meta-Key** box and click **Continue**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta1.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg)
7. Choose one of these options to assign the key:
   * To assign this key to all accounts in the current portfolio, choose **All current and future Merchant IDs** , click **Create key**, and continue to the Create Key page. All future merchant IDs will be automatically assigned this key. You are done and do not need to proceed with the following steps.
   * To assign this key to a specific merchant or group of merchants, choose **Custom Merchant ID selection** and then click **Create key**. This key is not automatically assigned to any future merchants. Proceed to the following steps.  
     ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta2.PNG/jcr:content/renditions/original)
8. Click **+ Add custom merchant ids**. The Add Custom Merchant IDs page appears.  
   By default, all merchant IDs are shown in the Merchant IDs table. To limit the list to a subset of merchant IDs, click **+ Add filter** , select a search filter from the drop-down menu, and click **Search**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta3.PNG/jcr:content/renditions/original)
9. Use the check boxes to choose one or more transacting MID accounts, and click **Submit**.  
   The Key Generation page opens.
10. Click **Create key**.  
    Continue to the Create Key page to view your new key.  
    You can also generate a new key by clicking **+ Generate Key** again.

Assign a Meta Key to All Merchants {#keys-meta-assign-all}
==========================================================

Follow these steps to assign an existing meta key to all current MIDs and automatically assign it to all future MIDs.

1. On the left navigation panel of the `Business Center`, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-meta-assign-all_step-1}
   {#keys-meta-assign-all_step-1}
2. Find the key that you want to assign or revoke by searching and filtering.{#keys-meta-assign-all_step-2}
   {#keys-meta-assign-all_step-2}
3. In the Edit Key column, click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit Key page appears. {#keys-meta-assign-all_step-3}
   {#keys-meta-assign-all_step-3}
4. Check the **Meta Key** check box if it is not already.{#keys-meta-assign-all_step-4}
   {#keys-meta-assign-all_step-4}
5. Select **All current and future MIDs** if it is not already.{#keys-meta-assign-all_step-5}
   {#keys-meta-assign-all_step-5}
6. Click **Submit** when done.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-meta-edit.png/jcr:content/renditions/original) {#keys-meta-assign-all_step-6-cmd}
   {#keys-meta-assign-all_step-6}

Assign a Meta Key to Select Merchants {#keys-meta-assign-selection}
===================================================================

Follow these steps to assign an existing meta key to a custom selection of MIDs.

1. On the left navigation panel of the `Business Center`, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.{#keys-meta-assign-selection_step-1}
   {#keys-meta-assign-selection_step-1}
2. Find the key that you want to assign by searching and filtering.{#keys-meta-assign-selection_step-2}
   {#keys-meta-assign-selection_step-2}
3. In the Edit Key column, click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit Key page appears. {#keys-meta-assign-selection_step-3}
   {#keys-meta-assign-selection_step-3}
4. Check the **Meta Key** check box if it is not already.{#keys-meta-assign-selection_step-4}
   {#keys-meta-assign-selection_step-4}
5. Select **Custom MID selection** if it is not already.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-meta-merch-assign.png/jcr:content/renditions/original) {#keys-meta-assign-selection_step-5}
   {#keys-meta-assign-selection_step-5}
6. Click **+ Add custom merchant ids**. {#keys-meta-assign-selection_step-6}
   {#keys-meta-assign-selection_step-6}
7. Select the MIDs that you want to assign the meta key to.  
   To filter MIDs, click **+ Add filter** , select a filter, and click **Search** . Click **Save**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta3.PNG/jcr:content/renditions/original) {#keys-meta-assign-selection_step-7-cmd}
   {#keys-meta-assign-selection_step-7}
8. Click **Submit** when done.  
   The Key Generation page appears. {#keys-meta-assign-selection_step-8}
   {#keys-meta-assign-selection_step-8}
9. Click **Create key** to complete assigning the key.{#keys-meta-assign-selection_step-9}
   {#keys-meta-assign-selection_step-9}

Remove a Meta Key from all Merchants {#keys-meta-assign-all-revoke}
===================================================================

Follow these steps to remove a meta key from all of the transacting MIDs that it is assigned to. This action also changes the meta key into a regular API key.

> IMPORTANT
> Removing a meta key does not delete the key. To delete a meta key, see [Delete a Meta Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-delete.md "").

1. On the left navigation panel of the `Business Center`, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.
2. Find the key that you want to assign or revoke by searching and filtering.
3. In the Edit Key column, click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit Key page appears.
4. Uncheck the **Meta Key** checkbox.
5. Click **Submit** when done.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-key-meta-revoke-key.png/jcr:content/renditions/original)

Remove a Meta Key from Select Merchants {#keys-meta-assign-all-revoke-selection}
================================================================================

Follow these steps to remove a meta key from specific transacting MIDs that it is assigned to.

> IMPORTANT
> Removing a meta key does not delete the key. To delete a meta key, see [Delete a Meta Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro/keys-meta-delete.md "").

1. On the left navigation panel of the `Business Center`, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.
2. Find the key that you want to remove by searching and filtering.
3. In the Edit Key column, click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit Key page appears.
4. Verify that the **Meta Key** check box is checked.
5. Verify that **Custom MID selection** is selected.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-meta-merch-assign.png/jcr:content/renditions/original)
6. Click **+ Add custom merchant ids**.
7. Select the MIDs that you want to remove the meta key from.  
   To filter MIDs, click **+ Add filter** , select a filter, and click **Search** . Click **Save**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/meta3.PNG/jcr:content/renditions/original)
8. Click **Submit** when done.  
   The Key Generation page appears.

Convert a Meta Key or Non-Meta Key {#keys-meta-assign-convert}
==============================================================

Follow these steps to add or remove the meta key functionality to an existing API key.  
If you remove meta key functionality from an API key, all MIDs assigned to that key will no longer be able to process transactions using that meta key.

1. On the left navigation panel of the `Business Center`, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.
2. Find the key that you want to assign or revoke by searching and filtering.
3. In the Edit Key column, click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-edit.svg/jcr:content/renditions/original) edit button.  
   The Edit Key page appears.
4. Choose one of these options:
   * To *add* meta key functionality to the API key, check the **Meta Key** check box.
   * To *remove* meta key functionality from the API key, uncheck the **Meta Key** check box.
5. Click **Submit** when done.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-key-meta-edit.png/jcr:content/renditions/original)

Delete a Meta Key {#keys-meta-delete}
=====================================

You can delete a key when you no longer need to use it for payment processing.  
Keys become inactive when they reach the expiration date.  
Follow these steps to delete a security key:

1. On the left navigation panel, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **`Payment Configuration` \&gt; Key Management**.  
   The Key Management page appears.
2. In the table of keys, find the key that you want to delete and click the ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-delete-row.svg/jcr:content/renditions/original) delete row button in the row for that key.  
   The Delete Confirmation window displays.  
   ![](/content/dam/new-documentation/documentation/en-us/olh/PaymentConfiguration/images/security-keys-delete-keys.png/jcr:content/renditions/original)
3. Click **Delete**.  
   The key is deleted.  
   ![](/content/dam/new-documentation/documentation/en-us/olh/PaymentConfiguration/images/security-keys-delete-keys-window.png/jcr:content/renditions/original)

Regenerate a Meta Key {#keys-meta-regenerate}
=============================================

When any security key expires, it must be updated. If you update the meta key manually, you must reassign merchants to it, which can be time-consuming. Meta key regeneration enables you to update the meta key with all of its assignments intact, streamlining the process.

1. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) **Payment Configuration \&gt; Key Management**.  
   The Key Management page appears.
2. Use the Search Filters to find the key you want to regenerate.  
   Results appear in the Search Results table.
3. Click the **Regenerate meta key** button for the key you want to regenerate.  
   The Key Generation page opens. The new key appears on the screen. The original key remains active until its original expiration date.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-regnerate-active.png/jcr:content/renditions/original)
4. Provide the new key details to the merchants associated with the affected MIDs, and instruct them to update the information wherever it is used.

Meta Keys in API Requests {#keys-meta-edit}
===========================================

This section describes how to include meta keys in API requests.

REST API Payment Request with a Meta Key {#keys-meta-api-rest}
==============================================================

REST API meta keys can use either HTTP signature or JSON Web Token methods of authentication.  
If you use the SDK, see the sample code for how to configure your meta key in GitHub:  
[`https://github.com/example/payment-gateway-rest-samples-java/blob/master/README.md#setting-your-api-credentials`](https://github.com/example/payment-gateway-rest-samples-java/blob/master/README.md#setting-your-api-credentials "")  
If you do not use the SDK, see the following information.

HTTP Signature
--------------

When creating the signature, use the portfolio or account ID as the value for the `v-c_merchant-id` header. However, when sending the API request, use the transacting merchant ID (MID) as the value for the `v-c-merchant-id` header. Signature Headers

```
v-c-merchant-id : merchantId
Key id : 266438gb-2120-4q36-8da7-fbb9a196d452
Shared Key : mgWWJVV2aGQyEPwufdhhe/GiFUhsNIwYvWMih4FMCN9E=
Request Target : post /pts/v2/payments
Host : api.example.com
```

JSON Web Token
--------------

The portfolio or account ID is not required in the header or the body. Pass the P12 certificate along with the `v-c-merchant-id` header, using the transacting merchant account ID (MID) as the value. JSON Web Token

```
// JWT Header
{
"v-c-merchant-id":"MerchantID",
"alg":"RS256",
"x5c":["MIIB2jCCAUOgAwlBAgIWNDg...=="]
}
// JWT Claimset
{
"digest":"0qjow45/L/m6DIHd8K90rL+tBKufR1RuyE4QG7whZQ=",
"digestAlgorithm":"SHA-256",
"iat":"1594249865"
}
// JWT Signature
{
data=base64urlEncode(JWT header)+"."+base64urlEncode(Claimset) signature=RS256Hash(data,private_key);
```

Simple Order API Payment Request Using a Meta Key {#keys-meta-api-simple-order}
===============================================================================

In this Simple Order API payload, the merchantID field value is the transacting merchant ID (MID) on whose behalf this transaction is being sent from the portfolio or merchant account. The portfolio or merchant account user will use a Simple Order API meta-key certificate to digitally sign the request message before sending it to `Payment Gateway`. There is no need to declare the portfolio ID or merchant account ID.
Simple Order API Payment Request

```
&lt;requestMessage xmlns="urn:schemas-payment-gateway-com:transaction-data-1.135"&gt;
  &lt;merchantID&gt;merchant12378&lt;/merchantID&gt;
  &lt;merchantReferenceCode&gt;NGTS1500&lt;/merchantReferenceCode&gt;
  &lt;clientLibrary&gt;Java XML&lt;/clientLibrary&gt;
  &lt;clientLibraryVersion&gt;5.0.2&lt;/clientLibraryVersion&gt;
  &lt;clientEnvironment&gt;Mac OS X/10.14.5/Oracle Corporation/1.8.0_161&lt;/clientEnvironment&gt;
  &lt;invoiceHeader&gt;
    &lt;merchantDescriptor&gt;NGMerchants*MyProduct&lt;/merchantDescriptor&gt;
    &lt;merchantDescriptorContact&gt;444-444-4444&lt;/merchantDescriptorContact&gt;
  &lt;/invoiceHeader&gt;
  &lt;billTo&gt;
    &lt;firstName&gt;TSTester&lt;/firstName&gt;
    &lt;lastName&gt;NextGen&lt;/lastName&gt;
    &lt;street1&gt;201 S. Division St.&lt;/street1&gt;
    &lt;street2&gt;Suite 500&lt;/street2&gt;
    &lt;city&gt;Ann Arbor&lt;/city&gt;
    &lt;state&gt;MI&lt;/state&gt;
    &lt;postalCode&gt;48104-2201&lt;/postalCode&gt;
    &lt;country&gt;US&lt;/country&gt;
    &lt;phoneNumber&gt;999-999-9999&lt;/phoneNumber&gt;
    &lt;email&gt;rm@example.com&lt;/email&gt;
    &lt;ipAddress&gt;66.185.179.2&lt;/ipAddress&gt;
  &lt;/billTo&gt;
  &lt;shipTo&gt;
    &lt;firstName&gt;Olivia&lt;/firstName&gt;
    &lt;lastName&gt;White&lt;/lastName&gt;
    &lt;street1&gt;1295 Charleston Rd&lt;/street1&gt;
    &lt;street2&gt;Cube 2386&lt;/street2&gt;
    &lt;city&gt;Mountain View&lt;/city&gt;
    &lt;state&gt;CA&lt;/state&gt;
    &lt;postalCode&gt;94043&lt;/postalCode&gt;
    &lt;country&gt;US&lt;/country&gt;
    &lt;phoneNumber&gt;650-965-6000&lt;/phoneNumber&gt;
  &lt;/shipTo&gt;
  &lt;purchaseTotals&gt;
    &lt;currency&gt;usd&lt;/currency&gt;
    &lt;grandTotalAmount&gt;2202&lt;/grandTotalAmount&gt;
  &lt;/purchaseTotals&gt;
  &lt;card&gt;
    &lt;accountNumber&gt;4111111111111111&lt;/accountNumber&gt;
    &lt;expirationMonth&gt;12&lt;/expirationMonth&gt;
    &lt;expirationYear&gt;2021&lt;/expirationYear&gt;
    &lt;cvNumber&gt;111&lt;/cvNumber&gt;
    &lt;cardType&gt;001&lt;/cardType&gt;
  &lt;/card&gt;
  &lt;ccAuthService run="true"&gt;
    &lt;commerceIndicator&gt;internet&lt;/commerceIndicator&gt;
    &lt;billPayment&gt;true&lt;/billPayment&gt;
  &lt;/ccAuthService&gt;
  &lt;ccCaptureService run="true"/&gt;
  &lt;businessRules&gt;
    &lt;ignoreAVSResult&gt;true&lt;/ignoreAVSResult&gt;
    &lt;ignoreCVResult&gt;true&lt;/ignoreCVResult&gt;
  &lt;/businessRules&gt;
&lt;/requestMessage&gt;		
```

SOAP Payment Request Using a Meta Key {#keys-meta-api-soap}
===========================================================

The request envelope requires a SOAP API password generated for the meta key. The value of the wsse. Username field is the portfolio or merchant account ID. The value of the merchantID field is the transacting MID on whose behalf this transaction being sent from the portfolio or account.  
In this example, the request is being sent from a portfolio. The portfolio ID is `portfolioabc` and the transacting MID is `merchant12378`.
SOAP API Payment Request

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;
  &lt;SOAP-ENV:Header&gt;
    &lt;wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"&gt;
      &lt;wsse:UsernameToken&gt;
        &lt;wsse:Username&gt;portfolioabc&lt;/wsse:Username&gt;
        &lt;wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText"&gt;8SbCuVZ4FLYakM7Mm+g4jlXgV5kN/uPNfRmpTj8yKNrmvmZU25tFiTyA6Qbx4jakhKYGRDqnma/52WrOu4GQm9WbYp5xyjlE16+YQFJRXY9jQHAmikc18Na3YugZzuBbu1aRcr597pwmdxkoWb87l+6gkqJU04eHayfiMNWSkq8piBcK5fIKIah9eSQdH31DaaqAQHvJJKLL8Ki+7TYJHKc24fBLKY4QPKr0pdGNubqjJxl8YyJXozVv3F4BcmgaklqCVAiORTr/IKTczU6Y56BrPsixsoehBetzqwxnyUjRkS1172fsOFPqPwZSGhMoATyM+EYXTEZoni58q5zvvw==&lt;/wsse:Password&gt;
      &lt;/wsse:UsernameToken&gt;
    &lt;/wsse:Security&gt;
  &lt;/SOAP-ENV:Header&gt;
  &lt;SOAP-ENV:Body&gt;
    &lt;requestMessage xmlns="urn:schemas-payment-gateway-com:transaction-data-1.151"&gt;
      &lt;merchantID&gt;merchant12378&lt;/merchantID&gt;
      &lt;merchantReferenceCode&gt;BATSNTA1003&lt;/merchantReferenceCode&gt;
      &lt;billTo&gt;
        &lt;firstName&gt;James&lt;/firstName&gt;
        &lt;lastName&gt;Dough&lt;/lastName&gt;
        &lt;street1&gt;600 Morgan Falls Road&lt;/street1&gt;
        &lt;street2&gt;Room 2-2123&lt;/street2&gt;
        &lt;city&gt;Atlanta&lt;/city&gt;
        &lt;state&gt;GA&lt;/state&gt;
        &lt;postalCode&gt;30350&lt;/postalCode&gt;
        &lt;country&gt;US&lt;/country&gt;
        &lt;phoneNumber&gt;650-965-6111&lt;/phoneNumber&gt;
        &lt;email&gt;jdough@example.com&lt;/email&gt;
      &lt;/billTo&gt;
      &lt;item id="0"&gt;
        &lt;unitPrice&gt;1.00&lt;/unitPrice&gt;
      &lt;/item&gt;
      &lt;item id="1"&gt;
        &lt;unitPrice&gt;1.00&lt;/unitPrice&gt;
      &lt;/item&gt;
      &lt;purchaseTotals&gt;
        &lt;currency&gt;USD&lt;/currency&gt;
      &lt;/purchaseTotals&gt;
      &lt;card&gt;
        &lt;accountNumber&gt;4111111111111111&lt;/accountNumber&gt;
        &lt;expirationMonth&gt;04&lt;/expirationMonth&gt;
        &lt;expirationYear&gt;2025&lt;/expirationYear&gt;
        &lt;cvNumber&gt;111&lt;/cvNumber&gt;
        &lt;cardType&gt;001&lt;/cardType&gt;
      &lt;/card&gt;
      &lt;ccAuthService run="true"/&gt;
      &lt;ccCaptureService run="true"/&gt;
    &lt;/requestMessage&gt;
    &lt;urn:requestMessage xmlns:urn="urn:schemas-payment-gateway-com:transaction-data-1.151"/&gt;
  &lt;/SOAP-ENV:Body&gt;
&lt;/SOAP-ENV:Envelope&gt;
```

SCMP API Payment Request using a Meta Key {#keys-meta-api-scmp}
===============================================================

In an SCMP API payment request, the merchant_id field value is the transacting MID on whose behalf this transaction being sent from the portfolio or merchant account. The value of the sender_id field is the ID of the portfolio or merchant account. The portfolio or merchant account uses the SCMP API meta-key certificate to sign and encrypt the request before sending it to `Payment Gateway`. The SCMP API payment request below is sent from a portfolio account.
SCMP API Request

```
request_id=5580301042523113616883
sender_id=portfolioabc
merchant_id=merchant123
merchant_ref_number=MERCH_SCMP_123
ics_applications=ics_auth
currency=usd
return_auth_record=true
client_lib_version=Oracle Corporation/1.8.0_192/Windows Server 2008 R2/6.1/-/Java/5.2.1/Oracle Corporation/1.8.0_201/Mac OS X/10.14.3/-/Java/5.2.0
offer0=amount:2^offer_id:0^product_name:PName1^merchant_product_sku:testdl^quantity:1^product_code:clothing
ignore_avs=yes
tax_indicator=Y
user_po=LII Test
customer_email=jdoe@example.com
customer_cc_expmo=10
customer_firstname=Bob
customer_cc_expyr=2020
customer_cc_number=4111111111111111
customer_hostname=bob.bob.com
customer_ipaddress=120.1.1.1
customer_lastname=Dough
customer_phone=555-555-5555
bill_country=US
bill_city=Atlanta
bill_zip=30350
bill_address2=Room 2-2123
bill_address1=123 Test Road
bill_state=GA
ship_to_email=bob@example.com
ship_to_lastname=Jones
ship_to_country=US
ship_to_county=Monroe
ship_from_city=San Jose
ship_to_city=bloomington
ship_to_co_name=Bob's Excursion Emporium
ship_from_zip=94538
ship_from_state=CA
ship_to_zip=47404
ship_from_country=US
ship_from_county=Santa Clara
ship_to_state=indiana
ship_to_firstname=Cat
ship_to_address2=suite 2-5A
ship_to_address1=37 se main street
			
```

Enable Message-Level Encryption {#restgs-mle-intro}
===================================================

IMPORTANT There are additional tasks you must complete before you can enable message-level encryption. See the Prerequisites for MLE section below.  
Message-Level Encryption (MLE) enables you to store information or communicate with other parties while helping to prevent uninvolved parties from understanding the stored information. MLE is required only for certain payments services. Enabling MLE requires you to create a *REST -- API Response MLE* key. If your organization is using a meta key, the portfolio account or merchant account that created the meta key must also create the REST -- API Response MLE key.  
MLE provides enhanced security for message payload by using an asymmetric encryption technique (public-key cryptography). The message encryption is implemented with symmetric encryption using Advanced Encryption Standard (AES), Galois Counter Mode (GCM) with 256-bit key size. The encryption of keys is supported using RSA Optimal Asymmetric Encryption Padding (OAEP) with 2048-bit key size. The encryption service is based on JSON Web Encryption (JWE), works on top of SSL and requires separate key-pairs for request and response legs of the transaction.  
MLE is required for APIs that primarily deal with sensitive transaction data, both financial and non-financial. These are the types of sensitive transaction data:

* Personal identification information (PII)

* Personal account number (PAN)

* Personal account information (PAI)
  {#restgs-mle-intro_ul_a4g_m15_sxb}  
  MLE is supported when using JSON web tokens.  
  Each of these authentication schemes uses an encrypted payload, called the *JWE* . A JWE token has these five components, with each component separated by a period (.):

* JOSE header containing four elements:

  ```
  "alg": "RSA-OAEP-256", // The algorithm used to encrypt the CEK.
  "enc": "A256GCM", // The algorithm used to encrypt the message.
  "iat": "1702493653", // The current timestamp in milliseconds.
  "kid": "keyId" // The serial number of shared public cert for encryption of CEK.
  ```
* JWE encrypted key

* JWE initialization vector

* JWE additional authentication data (AAD)

* JWE ciphertext and authentication tag

Test Your REST---API Response MLE Key {#restgs-jwt-message-mle-dev-center}
==========================================================================

Follow these steps to verify that your API response MLE key is working using the API Reference in the Developer Center. If you have not already created or submitted an API response MLE certificate, see [Create or Submit a REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-security-mle-reply.md "").

1. Go to the API Reference in the `Payment Gateway` Developer Center:  
   [`https://developer.example.com/api-reference-assets/index.html#static-home-section`](https://developer.example.com/api-reference-assets/index.md#static-home-section "") {#restgs-jwt-message-mle-dev-center_step-1}
   {#restgs-jwt-message-mle-dev-center_step-1}

2. Choose an API that supports MLE on the left navigation panel.  
   MLE support is indicated by **Request MLE** and **Response MLE** at the top of the screen.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-tags.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-2}
   {#restgs-jwt-message-mle-dev-center_step-2}

3. Choose the **MLE Configuration** tab.{#restgs-jwt-message-mle-dev-center_step-3}
   {#restgs-jwt-message-mle-dev-center_step-3}

4. Enter your API response MLE key credentials in the Message Level Encryption Credentials section:

   * **Response encryption:** Enter the key ID of your API response MLE key.  
     This is the key ID that you saved in Step 10 in the Create or Submit an API Response MLE Key section in [Enable Message-Level Encryption](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-mle-intro.md "").
   * **Response decryption:** Click **Browse** to submit your own decryption private key from your local system. Only *.p12* files are supported.

   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-upload.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-4}
   {#restgs-jwt-message-mle-dev-center_step-4}

5. Click **Update Credentials**.{#restgs-jwt-message-mle-dev-center_step-5}
   {#restgs-jwt-message-mle-dev-center_step-5}

6. Click the Send drop-down menu icon ( ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-arrow-up.svg/jcr:content/renditions/original) ) in the Request: Live Console section and choose **Send Request with Message Level Encryption**.{#restgs-jwt-message-mle-dev-center_step-6}
   {#restgs-jwt-message-mle-dev-center_step-6}

7. Click **Send** .  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-dev-center-send.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-7}
   {#restgs-jwt-message-mle-dev-center_step-7}

8. If a *Success: HTTP Status Code: 201* message displays in the Response section, your API response key is properly configured.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-success.png/jcr:content/renditions/original) {#restgs-jwt-message-mle-dev-center_step-8}
   {#restgs-jwt-message-mle-dev-center_step-8}

Create or Submit a REST---API Response MLE Key {#restgs-security-mle-reply}
===========================================================================

Before you can enable your system to support MLE, you must create or upload an *REST---API response MLE* certificate. After creating or uploading the certificate, you can extract the certificate's key to begin enabling MLE.  
Follow these steps to create or submit an API Response MLE certificate using the `Business Center`:

1. Log in to the `Business Center`:

   * **Test:** [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
   * **Production:** [`https://businesscenter.example.com`](https://ebc2.example.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key.  
      ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
2. Under REST APIs, choose **REST -- API Response MLE** , and then click **Generate key** .  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-4}
   {#restgs-security-mle-reply_step-4}

3. Choose one of these options to download your key:

   * To create a new API response MLE certificate, click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .
   * To upload your own certificate, enter your public PEM-formatted certificate in the text box, then click **Download key** ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) . The *.pem* file downloads to your desktop. If prompted by your system, approve the location for where the file downloads.

   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-reply-submit.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-5}
   {#restgs-security-mle-reply_step-5}
   6. If you are creating a certificate, the Set a Password window appears. Create a password for the certificate by entering the password into the New Password and Confirm Password fields, and then click Generate key.  
   The *.p12* file downloads to your desktop. If prompted by your system, approve the location for where the key downloads.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
   You can create or upload another key by clicking **Generate another key**. To view all of your created keys, use the Key Management page.

   > IMPORTANT
   > Securely store the *.p12* file and password in your system. These credentials are required to implement certain products and you must be able to access them.
   > {#restgs-security-mle-reply_step-6}
   > {#restgs-security-mle-reply_step-6}

4. Click **Cancel** .  
   The Key Management page appears. {#restgs-security-mle-reply_step-7}
   {#restgs-security-mle-reply_step-7}

5. Click the Key Type filter and choose **REST-API Response MLE**.{#restgs-security-mle-reply_step-8}
   {#restgs-security-mle-reply_step-8}

6. Click the Expires At filter and choose **All Dates**.{#restgs-security-mle-reply_step-9}
   {#restgs-security-mle-reply_step-9}

7. Click **Search**.{#restgs-security-mle-reply_step-10}
   {#restgs-security-mle-reply_step-10}

8. Find the REST--API Response key that you created in the Search Results table and save its key ID.  
   The key ID is needed to test and configure your system to use MLE.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-mle-ebc-key-mgmt.png/jcr:content/renditions/original) {#restgs-security-mle-reply_step-11}
   {#restgs-security-mle-reply_step-11}

{#restgs-security-mle-reply_list}

**Test Your REST--API Response MLE Key**
:
To test your REST--API Response key, see [Test Your REST---API Response MLE Key](/docs/gateway/en-us/security-keys/user/all/ada/security-keys/restgs-jwt-message-mle-dev-center.md "").

Test Your Shared Secret Key Pair {#restgs-security-key-pair-test-task}
======================================================================

After creating your key certificate, you must test and verify that your key can successfully process API requests. These tasks explain how to test and validate your key certificate using the developer center and the `Business Center`.

1. Go to the developer center's API Reference page:  
   [https://developer.example.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.example.com/api-reference-assets/index.md#payments_payments_static-home-section "")
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.example.com/api-reference-assets/index.md#static-api-endpoints-section "")**.
3. Under Authentication and Sandbox Credentials, set the Authentication Type drop-down menu to HTTP Signature.
4. Enter your organization ID in the Organization ID field.
5. Enter your key, also known as your private key, in the Key field.
6. Enter your secret key, also known as your public key, in the Shared Secret Key field.
7. Click **Update Credentials**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-http.png/jcr:content/renditions/original)
8. On the developer center's left navigation panel, navigate to **Payments \&gt; `POST` Process a Payment**.
9. Under Request: Live Console, click **Send**.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original)
10. Log in to the `Business Center`:  
    [`https://businesscentertest.example.com`](https://ebc2test.example.com/ebc2/ "")
11. On the left navigation panel, navigate to ![](/content/dam/new-documentation/documentation/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/new-documentation/documentation/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original)

