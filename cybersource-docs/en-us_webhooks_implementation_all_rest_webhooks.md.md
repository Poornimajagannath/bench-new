Webhooks Implementation Guide {#webhooks-about-guide}
=====================================================

This guide provides information about Webhook features that you can include in your system:

* Multiple security options. For example, server security policy and digital signature verification.
* Multiple possible workflows based on the security policy you choose.
* The process for setting up and using the feature.
  {#webhooks-about-guide_ul_nvj_cyh_mxb}

Convention
:
This special statement is used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Related Documentation
:
Visit the [`Cybersource` documentation hub](https://developer.cybersource.com/docs.md "") to find additional technical documentation.

Customer Support
:
For support information about any service, visit the Support Center:

[support.example.com](http://support.example.com "")

Recent Revisions to This Document {#wh-fg-doc-revisions}
========================================================

26.7.01
-------

Add the section [URL Review and Approval Process](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro/wh-fg-url-validation.md "").

26.5.01
-------

Minor edits and clarifications in the section [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

26.3.01
-------

Added new section [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").  
Added Payment and Unified Checkout events to [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").  
Updated section [Example: Notification Payload](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-notification-payload-ex.md "") with a new example that includes headers.  
Reorganized sections and added clarifications and corrections throughout the guide.

26.1.01
-------

Created new section [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md ""). Message-level encryption is required for payment events.

25.1.01
-------

Added payment and Unified Checkout events to [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

25.10.01
--------

This revision contains only editorial changes and no technical updates.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Webhooks {#wh-fg-intro}
=======================================

Webhooks are automated notifications that are generated and sent to you when specific system events occur. By using the Webhooks REST API, you can subscribe to these notifications for events of your choice and designate a URL in your system to receive them. This is helpful for events that are not a part of an API request and response, or that are not available through the Reporting API. For example, you can receive webhook notifications when these events occur:

* Fraud alerts
* Invoice status updates
* Network token is provisioning
* Transaction monitoring
* Recurring billing

You can also configure your system to respond to the events in any way you choose.  
The Webhooks REST API enables you to:
* Create webhook subscriptions to receive automatic system notifications
* Update and delete existing webhook subscriptions
* Check the status of a webhook notification
* Retrieve webhook notification history and details  
  For more information about the products and event types for which you can receive notifications for, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

Benefits
--------

The Webhooks API provides these key benefits:

* Visibility into system events that are otherwise not visible.
* Ability to respond to events programmatically and to automate workflows.

`Business Center` Account
-------------------------

You must have an organization or merchant account (MID) in the `Business Center`.  
If you do not have an account, you can sign up for *test* account on the Developer Center:  
[`https://developer.cybersource.com/hello-world/sandbox.html`](https://developer.cybersource.com/hello-world/sandbox.md "")

Test Methods for Webhooks
-------------------------

You can test the Webhooks REST API using the Postman application or the `Cybersource` Developer Center's live console.

**Postman**
:
A Postman collection is available for you to test the Webhooks REST API. Contact your account manager to request the collection.

**Developer Center Live Console**
:
The `Cybersource` Developer Center offers the live console for you to test complete examples and view the API field descriptions. See the [Webhooks](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks "") section in the REST API Reference.

Webhooks Integration Overview {#wh-fg-workflow-options}
=======================================================

Follow these steps to set up your system to support the Webhooks REST API. Some of these steps are dependent on your system's security policy.

#### Figure:

Set Up Webhook Subscriptions Workflow ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/webhooks-setup-workflow-600x560.svg/jcr:content/renditions/original)
1. Set up a server with a URL to receive webhook notifications.
2. Configure your server security to receive webhooks notifications. For more information, see [Set Up Your Security](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-server-security.md "").
3. Create a REST API security key that is compliant with your security policy. Security keys are used to authenticate the requests you send to `Cybersource`. You must create separate keys for the testing and production environments. For more information, see [Create REST API Keys](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro.md "").
4. Request a digital signature key from `Cybersource`. For more information, see [Create a Digital Signature Key](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro.md "").
5. If your webhooks integration will include subscriptions to payment event notifications, implement message-level encryption for those events. See [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").
6. If your system uses the *OAuth* or *OAuth with JWT* security policy, you must provide your OAuth credentials to `Cybersource`. OAuth is not required and Mutual Trust is the default. If you are not using OAuth, skip this step. For more information, see [(Optional) Provide Your OAuth Credentials](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-oauth-cred-intro.md "").
7. Request a list of the products for which your organization is enabled to receive webhook notifications. For more information, see [Retrieve a List of Products and Events](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-product-list-intro.md "").

   > IMPORTANT
   > If your webhooks integration will include subscriptions to payment event notifications, implement message-level encryption for those events. See [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

8. Create your webhook subscription event notifications. For more information, see [Create a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro.md "").

Optional Set Up Tasks {#wh-fg-workflow-options_opt-tasks}
---------------------------------------------------------

You can complete these optional tasks after creating a webhook subscription.
* Include a health check URL to enable `Cybersource` to monitor your server's status for reliability. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").
* Customize the retry policy for unresponsive webhook and health check URLs. For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").
* Validate your digital signature. For more information, see [Validating a Notification with the Digital Signature Key](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro/wh-fg-optional-validate-intro.md "").

Supported Products and Event Types {#wh-fg-product-event-types}
===============================================================

When you create a webhook subscription, you must include a `Cybersource` *product* and one of its corresponding *event types* in your request. You can include multiple products and event types in the same request. Every time one of the events that you subscribe to occurs, you receive a notification. If you subscribe to a product that is not enabled for your account, you receive a notification when it is enabled. To retrieve a list of the enabled products that your organization can subscribe to, see [Retrieve a List of Products and Events](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-product-list-intro.md "").  
When you send a *create a webhook subscription* request, set the productId field to a value listed in the Product ID column. Set the eventTypes field array to a value listed in the Event Types column. If you are subscribing to multiple products and event types, separate each value with the comma character (`,`).  
These tables contain all of the supported products, event types, and their corresponding field values:

Alternative Payment Methods {#wh-fg-product-event-types_alt-pay}
----------------------------------------------------------------

|         Product ID          |         Event Types         |                                   Description                                   |
|-----------------------------|-----------------------------|---------------------------------------------------------------------------------|
| `alternativePaymentMethods` | `payments.payments.updated` | Notifies you that an alternative payment transaction's status was been updated. |

Decision Manager {#wh-fg-product-event-types_dm}
------------------------------------------------

|    Product ID     |              Event Types              |                         Description                         |
|-------------------|---------------------------------------|-------------------------------------------------------------|
| `decisionManager` | `risk.casemanagement.decision.accept` | Notifies you that a Decision Manager case was accepted.     |
| `decisionManager` | `risk.casemanagement.decision.reject` | Notifies you that a Decision Manager case was rejected.     |
| `decisionManager` | `risk.profile.decision.reject`        | Notifies you of a profile decision to reject a transaction. |

`eCheck` {#wh-fg-product-event-types_echeck}
--------------------------------------------

| Product ID |         Event Types          |                        Description                        |
|------------|------------------------------|-----------------------------------------------------------|
| `eCheck`   | `payments.credits.accepted`  | Notifies you of a successful `eCheck` credit transaction. |
| `eCheck`   | `payments.credits.failed`    | Notifies you of an `eCheck` credit transaction failure.   |
| `eCheck`   | `payments.payments.accepted` | Notifies you of a successful `eCheck` debit transaction.  |
| `eCheck`   | `payments.payments.failed`   | Notifies you of an `eCheck` debit transaction failure.    |
| `eCheck`   | `payments.voids.accepted`    | Notifies you of a successful `eCheck` void transaction.   |
| `eCheck`   | `payments.voids.failed`      | Notifies you of an `eCheck` void transaction failure.     |

`Fraud Management Essentials` {#wh-fg-product-event-types_fme}
--------------------------------------------------------------

|         Product ID          |              Event Types              |                                   Description                                    |
|-----------------------------|---------------------------------------|----------------------------------------------------------------------------------|
| `fraudManagementEssentials` | `risk.casemanagement.decision.accept` | Notifies you that a `Fraud Management Essentials` case was accepted.             |
| `fraudManagementEssentials` | `risk.casemanagement.addnote`         | Notifies you that a note has been added to a `Fraud Management Essentials` case. |
| `fraudManagementEssentials` | `risk.profile.decision.reject`        | Notifies you that a transaction was rejected.                                    |
| `fraudManagementEssentials` | `risk.casemanagement.decision.reject` | Notifies you that a `Fraud Management Essentials` case was rejected.             |
| `fraudManagementEssentials` | `risk.profile.decision.monitor`       | Notifies you of a profile decision to monitor a transaction.                     |
| `fraudManagementEssentials` | `risk.profile.decision.review`        | Notifies you of a profile decision to review a transaction.                      |

Invoicing {#wh-fg-product-event-types_invoicing}
------------------------------------------------

|     Product ID      |                  Event Types                  |                                                                  Description                                                                   |
|---------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `customerInvoicing` | `invoicing.customer.invoice.send`             | Notifies you that an invoice was sent.                                                                                                         |
| `customerInvoicing` | `invoicing.customer.invoice.cancel`           | Notifies you that an invoice was cancelled.                                                                                                    |
| `customerInvoicing` | `invoicing.customer.invoice.paid`             | Notifies you that an invoice was paid.                                                                                                         |
| `customerInvoicing` | `invoicing.customer.invoice.partial-payment`  | Notifies you that an invoice was partially paid.                                                                                               |
| `customerInvoicing` | `invoicing.customer.invoice.reminder`         | Notifies you 5 days before the invoice payment is due. This event is triggered if you have invoice reminders enabled in your invoice settings. |
| `customerInvoicing` | `invoicing.customer.invoice.overdue-reminder` | Notifies you 1 day after the invoice payment is due. This event is triggered if you have invoice reminders enabled in your invoice settings.   |

Pay By Link {#wh-fg-product-event-types_pbl}
--------------------------------------------

| Product ID  |         Event Types          |                                                                     Description                                                                      |
|-------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `payByLink` | `payByLink.customer.payment` | Merchants can subscribe to this event type to automate how their system is informed when a customer completes a payment.                             |
| `payByLink` | `payByLink.merchant.payment` | Partner resellers can subscribe to this event type to control the distribution of the payment confirmation email sent to their merchants' customers. |

Payments
--------

Payment events must be enabled for your account. Contact our support team to enable the events.  
Payment events require message-level encryption. See [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

| Product ID |                    Event Types                    |                                                                                                               Description                                                                                                                |
|------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `payments` | `payments.capture.status.accepted`                | Notifies you that a payment capture request was accepted. The transaction carries the status PENDING.                                                                                                                                    |
| `payments` | `payments.capture.status.updated`                 | Notifies you that a payment capture was updated and its status changed from PENDING to BATCHED.                                                                                                                                          |
| `payments` | `payments.refund.status.accepted`                 | Notifies you that a refund request was accepted. The transaction carries the status PENDING.                                                                                                                                             |
| `payments` | `payments.refund.status.updated`                  | Notifies you that a refund request was batched and its status has changed from PENDING to BATCHED.                                                                                                                                       |
| `payments` | `payments.credit.status.accepted`                 | Notifies you that a credit request was accepted. The transaction carries the status PENDING.                                                                                                                                             |
| `payments` | `payments.credit.status.updated`                  | Notifies you that a credit request was accepted. The transaction carries the status PENDING.                                                                                                                                             |
| `payments` | `payments.void.status.accepted`                   | Notifies you that a void request was accepted. The transaction carries the status VOIDED.                                                                                                                                                |
| `payments` | `payments.void.status.rejected`                   | Notifies you that a void request was rejected. The transaction carries the status NOT VOIDABLE.                                                                                                                                          |
| `payments` | `payments.authorization.status.accepted`          | Notifies you that an authorization request was authorized by the issuer. The transaction carries the status AUTHORIZED.                                                                                                                  |
| `payments` | `payments.authorization.status.reviewed`          | Notifies you that an authorization request was under review by Decision Manager. The transaction carries the status AUTHORIZED_PENDING_REVIEW.                                                                                           |
| `payments` | `payments.authorization.status.rejected`          | Notifies you that an authorization request was declined by the issuer or failed due to server error, timeout, or invalid request. Possible statuses include INVALID_REQUEST, SERVER_ERROR, DECLINED, SERVER_TIMEOUT, or SERVICE_TIMEOUT. |
| `payments` | `payments.authorization.status.partiallyApproved` | Notifies you that an authorization request was partially approved by the issuer. The transaction carries the status PARTIAL_AUTHORIZED.                                                                                                  |
| `payments` | `payments.reversal.status.accepted`               | Notifies you that a reversal request was approved successfully. The transaction carries the status REVERSED.                                                                                                                             |
| `payments` | `payments.reversal.status.rejected`               | Notifies you that a reversal request was declined due to issuer rejection, system error, invalid request, or timeout. Possible statuses include REVERSED, INVALID_REQUEST, SERVER_ERROR, DECLINED, SERVER_TIMEOUT, or SERVICE_TIMEOUT.   |

Recurring Billing {#wh-fg-product-event-types_rb}
-------------------------------------------------

|     Product ID     |               Event Types               |                  Description                   |
|--------------------|-----------------------------------------|------------------------------------------------|
| `recurringBilling` | `rbs.subscriptions.charge.failed`       | Notifies you of a recurring payment failure.   |
| `recurringBilling` | `rbs.subscriptions.charge.pre-notified` | Notifies you of an upcoming recurring payment. |
| `recurringBilling` | `rbs.subscriptions.charge.created`      | Notifies you of successful recurring payment.  |

`Token Management Service` {#wh-fg-product-event-types_tms}
-----------------------------------------------------------

|    Product ID     |          Event Types           |                                               Description                                               |
|-------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| `tokenManagement` | `tms.networktoken.updated`     | Notifies you of a network token's change in expiration date or status (suspend, resume, or deactivate). |
| `tokenManagement` | `tms.networktoken.provisioned` | Notifies you when a network token provision for an instrument identifier token has been successful.     |
| `tokenManagement` | `tms.networktoken.binding`     | Notifies you of the binding status of a network token with a device.                                    |

Unified Checkout {#wh-fg-product-event-types_uc}
------------------------------------------------

Unified Checkout events require message-level encryption. See [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

|    Product ID     |          Event Types           |                                               Description                                               |
|-------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| `unifiedCheckout` | `uc.orders.transactionresults` | Notifies you of the payment outcome, including the full payload response from the payment service call. |

Set Up Your Security {#wh-fg-server-security}
=============================================

There are a variety of security options for Webhooks. This section provides an overview of the security options, with links to the instructions for using them.

Mutual Trust
------------

All Webhooks integrations must use mutual trust by adding `Cybersource` to your allowlist and by trusting the root certificate.  
**Allowlist**  
Add these IP addresses to your allowlist to permit `Cybersource` to deliver your webhook notifications:

* 198.241.206.21
* 198.241.207.21

**Trusting the Root Certificate**  
Download the *Relay Corporate Root CA - G2* certificate from the Relay Public Key Infrastructure webpage, and add it to your Java keystore: [`https://enroll.relayca.com`](https://enroll.relayca.com "").

API Keys {#wh-fg-server-security_section_ykc_y1p_33c}
-----------------------------------------------------

REST API requests must use API Keys. All Webhooks requests require a shared secret key pair. Requests to create a subscription using OAuth with JWT **also** require a P12 Certificate. For instructions, see [Create REST APIs](https://developer.cybersource.com/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro.md "").

Digital Signature Key {#wh-fg-server-security_section_v2j_z1p_33c}
------------------------------------------------------------------

You must create a digital signature key in order for `Cybersource` to send notifications to your servers. For instructions, see [Create a Digital Signature Key](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro.md "").

OAuth and OAuth with JWT {#wh-fg-server-security_section_cm4_sqp_33c}
---------------------------------------------------------------------

In addition to mutual trust, you can also use the OAuth or OAuth with Java Web Token (JWT). You must provide your OAuth credentials and use the appropriate request fields for your security policy. See [(Optional) Provide Your OAuth Credentials](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-oauth-cred-intro.md "") and [Create a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro.md "").

Message-Level Encryption {#wh-fg-server-security_section_yyq_xbp_33c}
---------------------------------------------------------------------

Message-level encryption is required for some products and events. For instructions, see [Message-Level Encryption](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro.md "").

Create REST API Keys {#webhooks-keys-intro}
===========================================

The Webhooks REST API requires you to create a *shared secret key pair* . You might have already completed this requirement if your system is currently REST compliant. If you are using the OAuth with JWT security policy, you must also create a *P12 certificate* . The shared secret key pair and P12 certificate are also known as REST API keys. REST API keys are used to enable secure communication between you and `Cybersource` when using the REST API.
* **Shared secret key pair:** A key pair used for HTTP signature authentication. It is consists of a key and a shared secret key. See [Create a Shared Secret Key Pair](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro/webhooks-keys-shared-secret.md "").
* **P12 certificate:** A key used for JSON Web Token authentication. It consists of *.p12* file and a password that you must set to use the file. See [Create a P12 Certificate](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro/webhooks-keys-p12.md "").  
  When using the test and production environments, you must create separate keys for each environment.  
  Securely store your created keys in your system. You must be able to access your key credentials while implementing and managing webhook subscriptions.  
  REST API keys expire after 3 years.

Create a Shared Secret Key Pair {#webhooks-keys-shared-secret}
==============================================================

The Webhook REST API requires you to create a shared secret key pair. You may have already completed this requirement if your system is currently REST compliant.  
Follow these steps to create a shared secret key pair:

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://ebc2test.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://ebc2.cybersource.com/ebc2/ "")
     {#webhooks-keys-shared-secret_step-1}
     {#webhooks-keys-shared-secret_step-1}
   2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original) {#webhooks-keys-shared-secret_step-2}
      {#webhooks-keys-shared-secret_step-2}
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original) {#webhooks-keys-shared-secret_step-3}
      {#webhooks-keys-shared-secret_step-3}
   4. Under REST APIs, choose **REST -- Shared Secret** and then click **Generate key**.  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/security-keys-create-key.png/jcr:content/renditions/original)  
      ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/generate-key-bttn.png/jcr:content/renditions/original)  
      The REST API Shared Secret Key page appears. {#webhooks-keys-shared-secret_d10e26}
      {#webhooks-keys-shared-secret_d10e26}
   5. Click **Download key** ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      The *.pem* file downloads to your desktop.  
      ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/shared-secret-key-download.png/jcr:content/renditions/original)  
      The **Key** value is your *key ID* and the **Shared Secret** value is your *shared secret key*.

   > IMPORTANT
   > Securely store the key credentials and *.pem* file in your system. These credentials are required in order to implement certain products, and you must be able to access them.
   > {#webhooks-keys-shared-secret_d10e46}
   > {#webhooks-keys-shared-secret_d10e46}

To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.
IMPORTANT Securely store the shared secret key pair in your system. You must be able to retrieve these credentials to implement the Webhooks REST API.

Create a P12 Certificate {#webhooks-keys-p12}
=============================================

If you are using the OAuth with JWT security policy, you must create a P12 certificate in addition to a shared secret key pair. You might have already completed this requirement if your system is currently REST compliant.  
Follow these steps to create a P12 certificate file or submit your own certificate signing request (CSR):

1. Log in to the `Business Center`:
   * **Test:** [`https://businesscentertest.cybersource.com`](https://ebc2test.cybersource.com/ebc2/ "")
   * **Production:** [`https://businesscenter.cybersource.com`](https://ebc2.cybersource.com/ebc2/ "")
   2. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-pymt-config.svg/jcr:content/renditions/original) Payment Configuration \&gt; Key Management.  
      ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/left-navigation.png/jcr:content/renditions/original)
   3. Click + Generate key on the Key Management page.  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/generate-key.png/jcr:content/renditions/original)
   4. Under REST APIs, choose REST -- Certificate, and then click Generate key.  
      The Key Generation page appears.  
      If you are using a *portfolio* account, the Key options window appears, giving you the choice to create a meta key. For more information about how to create a meta key, see *[Creating and Using Security Keys](https://developer.cybersource.com/docs/cybs/en-us/security-keys/user/all/ada/security-keys/keys-meta-intro.md "")*.  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/p12-key-select.png/jcr:content/renditions/original)
2. (Optional) You can set the Certificate Expiry Timeframe field to the number of months you want the key to remain active before it expires. Only whole numbers from 1--36 are accepted. By default, new keys expire after 12 months.
3. Choose from these two options:
   1. If you are a creating a new P12 Certificate, click Download key ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-blank.png/jcr:content/renditions/original)
   2. If you are submitting your own certificate, enter your public PEM-formatted certificate in the text box, then click Download key ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-bttn-download.svg/jcr:content/renditions/original) .  
      ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/sec-keys/images/submit-key-fill.png/jcr:content/renditions/original)
      {#webhooks-keys-p12_d12e31}
      {#webhooks-keys-p12_d12e31}
   3. Create a password for the certificate by entering one into the New Password and Confirm Password fields. Click Generate key.  
      ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/restgs-set-pass.png/jcr:content/renditions/original)  
      The *.p12* file downloads to your desktop.  
      If prompted by your system, approve the location to which the key downloads. {#webhooks-keys-p12_d12e60}
      {#webhooks-keys-p12_d12e60}

To create or submit another key, click **Generate another key**. To view all of your created keys, go to the Key Management page.

> IMPORTANT
> Securely store the *.p12* file and password in your system.

Create a Digital Signature Key {#wh-fg-key-dig-sig-intro}
=========================================================

Use the information in this section to create a *digital signature key*. The Digital Signature Key request uses Relay's key management service to store your credentials. The Webhooks platform retrieves your credentials from key management to digitally authenticate your notifications.  
You must create a digital signature key to enable `Cybersource` to send notifications to your servers. Replace the digital signature key every year. When you generate a new digital signature key, it overrides the old key and new transactions must use the new key.  
Notifications that use message-level encryption must also the digital signature key.

> IMPORTANT Store the created digital signature key in a secure location in your system.

Optional Notification Validation
--------------------------------

After you set up a webhook subscription, you can validate each notification you receive using your digital signature key. For more information, see [Validating a Notification with the Digital Signature Key](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro/wh-fg-optional-validate-intro.md "").

Endpoints
---------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/kms/egress/v2/keys-sym`
* **Production:** `POST ``https://api.cybersource.com``/kms/egress/v2/keys-sym`
* **India Production:** `POST https://api.in.cybersource.com/kms/egress/v2/keys-sym`

Required Fields for Creating a Digital Signature Key {#wh-fg-key-dig-sig-req-fields}
====================================================================================

clientRequestAction
:
Set the value to `CREATE`.

keyInformation.expiryDuration
:
Set to a number of days. We recommend `365`.

keyInformation.keyType
:
Set the value to `sharedSecret`.

keyInformation.organizationId
:
Set the value to the organization ID of the organization requesting the key.

keyInformation.provider
:
Set the value to `nrtd`.

keyInformation.tenant
:
Set the value to the organization ID of the organization requesting the key.

Example: Creating a Digital Signature Key {#wh-fg-key-dig-sig-ex}
=================================================================

Digital Signature Key Request

```
{
  "clientRequestAction": "CREATE",
  "keyInformation": {
    "provider": "nrtd",
    "tenant": "merchantName",
    "keyType": "sharedSecret",
    "organizationId": "merchantName"
  }
}
```

Digital Signature Key Response

```
{
"submitTimeUtc": "2021-03-17T06:53:06+0000",
"status": "SUCCESS",
"keyInformation": {
"provider": "NRTD",
"tenant": "merchantName",
"organizationId": "merchantName",
"keyId": "bdc0fe52-091e-b0d6-e053-34b8d30a0504", //ID associated with the key in the key field
"key": "u3qgvoaJ73rLJdPLTU3moxrXyNZA4eo5dklKtIXhsAE=", //Base64 encoded key
"keyType": "sharedSecret",
"status": "Active",
"expirationDate": "2022-03-17T06:53:06+0000"
}
```

REST Interactive Example: Creating a Digital Signature Key {#wh-fg-key-dig-sig-dev-ex}
======================================================================================

Click this image to access the interactive code example for creating a digital signature key. The Live Console refers to this request as *Create Webhook Symmetric Key*.

#### Figure:

Creating a Digital Signature Key [![Image and link to the interactive code example for creating a digital signature key.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-create-digi-sig-key.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md#webhooks_create-new-webhooks_create-webhook-security-keys_samplerequests-dropdown_create-webhook-symmetric-key_liveconsole-tab-request-body "")

Validating a Notification with the Digital Signature Key {#wh-fg-optional-validate-intro}
=========================================================================================

You can use the digital signature key to verify that the webhook notifications you receive are from `Cybersource`. Verifying your webhook notifications validates their integrity and helps prevent replay attacks.  
When you receive a webhook notification from `Cybersource`, it contains a digital signature key. You can configure your system to compare the notification's digital signature to the digital signature you created. If the digital signatures match, the notification is validated.  
Complete these tasks to validate the webhook notifications that you receive:
1. Create a digital signature key by sending a *create a digital signature key* request to `Cybersource`. You may have already completed this requirement while setting up your first webhook subscription. For more information, see [Create a Digital Signature Key](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-key-dig-sig-intro.md "").
2. Extract the digital signature from the digital signature key that you created.
3. Configure your system to compare your digital signature to the digital signatures in the notifications that you receive. A webhook notification is valid if the notification's digital signature matches your digital signature.

Digital Signature Format {#wh-fg-optional-validate-sig-format}
==============================================================

When you receive a webhook notification from `Cybersource`, it contains a `v-c-signature` header in this format:

```
v-c-signature: t=1617830804768;keyId=bf44c857-b182-bb05-e053-34b8d30a7a72;sig=CzHY47nzJgCSD/BREtSIb+9l/vfkaaL4qf9n8MNJ4CY=";
```

The header contains these three parameters concatenated with semicolons:

* t: The timestamp at which the digital signature key was created.
* keyId: The digital signature key ID.
* sig: The digital signature. It is encrypted using the HMAC-SHA256 algorithm.

Validating a Notification {#wh-fg-optional-validate}
====================================================

Follow these steps to validate the integrity of your webhook notifications.

1. Separate the signature parameters with a semicolon (;) and extract the t, keyId, and sig values.
2. Use the keyId value to fetch the digital signature key.
3. Generate the payload by concatenating the timestamp and the payload from the body of the notification, using a period (.) to join them.
4. Use the SHA-256 algorithm to encrypt the generated payload from Step 3 using the key from Step 2.
5. Verify that the encrypted value matches the value in sig parameter.

Example: Validating a Notification {#wh-fg-optional-validate-ex}
================================================================

This example shows a system script that validates webhook notifications by comparing the merchant's digital signature with the webhook notification's signature. Use this example as a reference for how to configure your system.

```
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Base64;

public class Validator {
    public static void main(String[] args) {

        // Sample signature header
        String signatureHeader = "v-c-signature: t=1617830804768;keyId=bf44c857-b182-bb05-e053-34b8d30a7a72;sig=CzHY47nzJgCSD/BREtSIb+9l/vfkaaL4qf9n8MNJ4CY=";
        String payload = "this is a decrypted payload";
        // Convert the received signatureHeader into timestamp, keyId, and signature.
        DigitalSignature companySignature = new DigitalSignature(signatureHeader);
        // Check if the timestamp is within tolerance.
        if (companySignature.isValidTimestamp()) {
            // Client regenerates their signature using the timestamp from header and received payload.
            byte[] signature = regenerateSignature(companySignature.getTimestamp(), payload);
            // Check if the generated signature is same as signature received in header.
            if (isValidSignature(signature, companySignature.getSignature())) {
                System.out.println("Success - Signature is valid");
            } else {
                System.out.println("Error - Signatures do not match");
            }
        } else {
            System.out.println("Error - timestamp is outside of tolerance level");
        }
    }
    /**
     * Compute HMAC with the SHA256 hash function.
     * key is your private key.
     * message is timestamp.payload.
     * @return
     */
    public static byte[] regenerateSignature(long timestamp, String message) {
        String timestampedMessage = timestamp + "." + message;
        String key = getSecurityKey();
        // Generate the hash using key and message.
        return calcHmacSHA256(Base64.getDecoder().decode(key), timestampedMessage.getBytes(StandardCharsets.UTF_8));
    }
    /**
    * A mechanism to fetch the security key using keyId from a source. We're using Base64encoded version of
    (test_key).
    * @return
    */
    private static String getSecurityKey() {
        return "dGVzdF9rZXk="; //test_key
    }
    /**
     * Generate SHA256 using secretKey and a message.
     * Sample Hmacgenerator to test: https://8gwifi.org/hmacgen.jsp
     * @param secretKey
     * @param message
     * @return
     */
    private static byte[] calcHmacSHA256(byte[] secretKey, byte[] message) {
        byte[] hmacSha256 = null;
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            SecretKeySpec secretKeySpec = new SecretKeySpec(secretKey, "HmacSHA256");
            mac.init(secretKeySpec);
            hmacSha256 = mac.doFinal(message);
        } catch (Exception e) {
            throw new RuntimeException("Failed to calculate hmac-sha256", e);
        }
        return hmacSha256;
    }
    /**
     * Compare the Base64 decoding of the signature with the signature received in the header.
     * Sample encoder/decoder to test:
     * https://www.base64encode.org/
     * https://www.base64decode.org/
     * @param bankSignature
     * @param companySignature
     * @return
     */
    private static boolean isValidSignature(byte[] bankSignature, String companySignature) {
        return Arrays.equals(bankSignature, Base64.getDecoder().decode(companySignature));
    }
}

import java.time.Clock;

public class DigitalSignature {
    private long timestamp;
    private String keyId;
    private String signature;

    public DigitalSignature(String digitalSignature) {
        try {
            //split the header by space. first part is the key "v-c-signature" second part is the actual signature
              String signature = digitalSignature.split(" ")[1];

            //separate the actual signature by semicolon. this creates 3 parts (timestamp, keyId, sig)
            String[] signatureParts = signature.split(";");

            //timestamp section is the first block. split timestamp section by = sign and actual timestamp is in the second block
            this.timestamp = Long.parseLong(signatureParts[0].split("=")[1]);

            //keyId section is the second block. split keyId section by = sign and actual keyId is in the second block
            this.keyId = signatureParts[1].split("=")[1];

            //digital signature is the third block. split digital signature by = sign and actual signature is in the second block. This is Base64 encoded
            this.signature = signatureParts[2].split("=")[1];

            if unable to format exactly like the above then would recommend the following edit:
            /* split the header by space. first part is the key "v-c-signature" second part is the actual signature */
              String signature = digitalSignature.split(" ")[1];

            /* separate the actual signature by semicolon. this creates 3 parts (timestamp, keyId, sig) */
            String[] signatureParts = signature.split(";");

            /* timestamp section is the first block. split timestamp section by = sign and actual timestamp is in the second block */
            this.timestamp = Long.parseLong(signatureParts[0].split("=")[1]);

            /* keyId section is the second block. split keyId section by = sign and actual keyId is in the second block */
            this.keyId = signatureParts[1].split("=")[1];

            /* digital signature is the third block. split digital signature by = sign and actual signature is in the second block. This is Base64 encoded */
            this.signature = signatureParts[2].split("=")[1];
        } catch (Exception e) {
            System.out.println("Invalid digital signature format");
        }
    }
    public long getTimestamp() {
        return timestamp;
    }
    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }
    public String getKeyId() {
        return keyId;
    }
    public void setKeyId(String keyId) {
        this.keyId = keyId;
    }
    public String getSignature() {
        return signature;
    }
    public void setSignature(String signature) {
        this.signature = signature;
    }
    /**
     * Using a tolerance of 60 mins
     * Compute the current time in UTC and make sure the timestamp was generated within the tolerance period.
     * UTC millis generator to test: https://currentmillis.com/
     *
     * @return
     */
    public boolean isValidTimestamp() {
        long tolerance = 60 * 60 * 1000L; //60 mins
        // return Clock.systemUTC().millis() - timestamp  &lt; tolerance; // Enable this if you want timestamp
        validation.
        return true;
    }
}
```

(Optional) Provide Your OAuth Credentials {#wh-fg-oauth-cred-intro}
===================================================================

If your system uses the *OAuth* or *OAuth with JWT* security policy, you must provide your OAuth credentials to `Cybersource`. The OAuth credentials request uses Relay's key management service to store your credentials. When `Cybersource` sends you webhook notifications in the future, `Cybersource` will use your OAuth credentials to access your server and deliver the notification message.  
For more information about using OAuth, see *[OAuth 2.0 Partner Implementation Guide](https://developer.cybersource.com/docs/cybs/en-us/oauth/developer/all/rest/oauth/cybs-extend-intro.md "")*.

> IMPORTANT
> If you are using only the default *mutual trust* security policy, you do not need to provide OAuth credentials to ` Cybersource `.

**OAuth**
:
The OAuth security policy with client credentials is an authentication method that is designed for applications that communicate with each other. Basic authentication is the most common mechanism for authenticating a client with the client credentials. This authentication method enables `Cybersource` services to obtain only the relevant user data without exposing the user's credentials.

**OAuth with JWT**
:
The OAuth with JWT security policy is an authentication method in which your system sends a JSON Web Token. This method bypasses domain headers and minimizes the need for server-side authentication checks.

Endpoints
---------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/kms/egress/v2/keys-sym`
* **Production:** `POST ``https://api.cybersource.com``/kms/egress/v2/keys-sym`
* **India Production:** `POST https://api.in.cybersource.com/kms/egress/v2/keys-sym`
  {#wh-fg-oauth-cred-intro_ul_kmx_mcl_b1c}

Headers
-------

Each API request should use headers that provide your client credentials, which are the username and password of your webhooks server. Here is an example:

```
curl --location 'Client's OAauth URL' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode ‘client_id=webhooks-server-username' \
--data-urlencode ‘client_secret=webhooks-server-password'
```

Required Fields for Providing Your OAuth Credentials {#wh-fg-oauth-cred-req-fields}
===================================================================================

clientRequestAction
:
Set to `STORE`.

keyInformation.clientKeyId
:
Set to the webhook server's username.

keyInformation.expiryDuration
:
Set to `365`.

keyInformation.key
:
Set to the webhooks server's secret key.

keyInformation.keyType
:
Set to `oAuthClientCredentials`.

keyInformation.organizationId
:
Set to the organization ID or merchant ID of the organization requesting the key.

keyInformation.provider
:
Set to `nrtd`.

keyInformation.tenant
:
Set to the organization ID that the requesting organization belongs to.

Example: Providing Your OAuth Credentials {#wh-fg-oauth-cred-ex}
================================================================

```
{
  "clientRequestAction": "STORE",
  "keyInformation": {
    "provider": "nrtd",
    "tenant": "merchantName",
    "keyType": "oAuthClientCredentials",
    "organizationId": "merchantName",
    "clientKeyId": "Webhook server's username",
    "key": "Webhook server's secret key",
    "expiryDuration": "365"
  }
}
```

```
{
    "submitTimeUtc": "2022-02-18T19:49:52Z",
    "status": "SUCCESS",
    "keyInformation": {
        "provider": "nrtd",
        "tenant": "org1",
        "organizationId": "org1",
        "clientKeyId": "ef400ac1-edfe-406e-94b3-0d73be09a1a0",
        "keyId": "d8512fb5-1d8c-4f2d-e053-3cb8d30a764c",
        "key": "KTTY1LLGYR6A2LL4XZTT9W9RGCVJ5Z4XZAP6AFTRUFWLSXX0NX4N88N9EJED3BMM",
        "keyType": "oAuthClientCredentials",
        "status": "active",
        "expirationDate": "2023-02-18T19:49:52Z"
    }
}
			
```

REST Interactive Example: Providing Your OAuth Credentials {#wh-fg-oauth-cred-dev-ex}
=====================================================================================

Click this image to access the interactive code example for providing your OAuth credentials to `Cybersource`. The Live Console refers to this request as *Store oAuth Credentials*.

#### Figure:

Providing Your OAuth Credentials [![Image and link to the interactive code example for providing your
OAuth credentials.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-oauth-cred.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md#webhooks_create-new-webhooks_create-webhook-security-keys_samplerequests-dropdown_store-oauth-credentials_liveconsole-tab-request-body "")

Retrieve a List of Products and Events {#wh-fg-product-list-intro}
==================================================================

This section describes how to retrieve a list of the products and event types that are enabled for your organization. Use this list to know which products and events that you can subscribe to. A successful response lists the enabled products and events in the productId and eventTypes.eventName fields. You can use these same field values when you send a *create a webhook subscription* request.  
If the list you retrieve does not contain an expected product or event type, the product might not be enabled for your organization. Contact your account manager for more information.  
For a list of all the products and event types that are supported by the Webhooks `REST API`, see the [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

Endpoints
---------

Send a GET request to one of these endpoints. The *{organizationId}* is your organization ID.

* **Test:** `GET ``https://apitest.cybersource.com``/notification-subscriptions/v2/products/`*{organizationId}*
* **Production:** `GET ``https://api.cybersource.com``/webhooks/notification-subscriptions/v2/products/`*{organizationId}*
* **India Production:** `GET https://api.in.cybersource.com/notification-subscriptions/v2/products/`*{organizationId}*

Example: Retrieving a List Products and Event {#wh-fg-product-list-ex}
======================================================================

```keyword
GET https://api.cybersource.com/notification-subscriptions/v2/products/{organizationId}
```

```
[
  {
    "productId": "terminalManagement",
    "eventTypes": [
      {
        "eventName": "terminalManagement.status.update",
        "payloadEncryption": false
      },
      {
        "eventName": "terminalManagement.assignment.update",
        "payloadEncryption": false
      },
      {
        "eventName": "terminalManagement.reAssignment.update",
        "payloadEncryption": false
      }
    ]
  }
]
```

REST Interactive Example: Retrieving Product and Event Types {#wh-fg-product-events-dev-ex}
===========================================================================================

Click this image to access the interactive code example for retrieving the product and event types enabled for your organization.

#### Figure:

Retrieve Product and Event Types [![Image and link to the interactive code example for retrieving the
product and event types enabled for your organization.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/retrieve-product-list-dev.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_create-new-webhooks_find-products-you-can-subscribe-to "")

Message-Level Encryption {#wh-fg-mle-intro}
===========================================

> IMPORTANT
> Payment and Unified Checkout events require message-level encryption. To see the event types and product IDs for Payment and Unified Checkout events, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").  
> Message-level encryption (MLE) encrypts the payload of a message to prevent tampering. This section explains how to create the key that is necessary to decrypt encrypted payloads.  
> The webhook notification service requires X.509 certificates instead of raw public keys for MLE. The service uses:

* **Symmetric Encryption**: AES-GCM with 256-bit keys
* **Asymmetric Encryption**: RSA-OAEP with 2048-bit keys
* **Format**: JSON Web Encryption
* Separate key pairs for request and response transactions

Prerequisite
------------

* OpenSSL must be installed on your system.
* You must have access to terminal/command line.
* You must have appropriate permissions to create the asymmetric key in the `Cybersource` system.

Preparing Your Workspace {#wh-fg-mle-prepare}
=============================================

Open a terminal and navigate to a secure location for storing your key pairs:

```
mkdir -p ~/webhooks-keys 
cd ~/webhoooks-keys
```

**Generate Certificate and Key Pair** {#wh-fg-mle-generate}
===========================================================

Run the following command with no line breaks, but change these values:

* Replace `RequestKey` with the API key that you created in [Create REST API Keys](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/webhooks-keys-intro.md "").
* Replace `YourOrg` with your account's organization ID.

{#wh-fg-mle-generate_ul_dpr_4gw_djc}

```
openssl req -x509 -newkey rsa:2048 -keyout request_private.pem -out request_certificate.pem -days 365 -nodes -subj "/CN=RequestKey/O=YourOrg/C=US" && cat request_certificate.pem | grep -v "BEGIN CERTIFICATE" | grep -v "END CERTIFICATE" | tr -d '\n' && echo
```

Result
------

* A 2048-bit RSA key pair is generated.
* A self-signed X.509 certificate valid for 365 days is created. Use the text of the certificate in the keyInformation.pub field during registration, in one line, and without the BEGIN and END lines. See [Required Fields for Registering Your Message-Level Encryption Keys](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro/wh-fg-mle-register/wh-fg-mle-req-fields.md "") and [Example: Registering Your Certificate](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro/wh-fg-mle-register/wh-fg-mle-ex.md "").
* The private key in `request_private.pem` is stored.
* The certificate in `request_certificate.pem` is stored.
* Separate keys for each organization ID or account that uses message-level encryption are created.
  {#wh-fg-mle-generate_ul_r4y_bbm_13c}

Register the Certificate {#wh-fg-mle-register}
==============================================

Use the REST API to register and store your certificate. Each webhook subscription requires its own unique asymmetric certificate.

Endpoints
---------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/kms/egress/v2/keys-asym`
* **Production:** `POST ``https://api.cybersource.com``/kms/egress/v2/keys-asym`
* **India Production:** `POST https://api.in.cybersource.com/kms/egress/v2/keys-asym`

Required Fields for Registering Your Message-Level Encryption Keys {#wh-fg-key-mle-req-fields}
==============================================================================================

clientRequestAction
:
Set the value to `STORE`.

keyInformation.provider
:
Set the value to `nrtd`.

keyInformation.tenant
:
Set the value to the name of the organization ID of the account.

keyInformation.keyType
:
Set the value to `publickey`.

keyInformation.organizationId
:
Set the value to the name of the organization ID of the account.

keyInformation.pub
:
Set the value to the X.509 certificate that you generated in [Generate Certificate and Key Pair](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro/wh-fg-mle-generate.md "").
:
IMPORTANT: The certificate is generated with line breaks. You must remove the line breaks before adding it to this field. Do not include the *--BEGIN--* and *--END--* lines. See [Example: Registering Your Certificate](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-mle-intro/wh-fg-mle-register/wh-fg-mle-ex.md "")

keyInformation.expiryDuration
:
Set the value to `365`.

Example: Registering Your Certificate {#wh-fg-mle-ex}
=====================================================

```
{
"clientRequestAction": "STORE",
"keyInformation": {
	"provider": "nrtd",
	"tenant": "&lt;set this to your organization ID&gt;",
	"keyType": "publickey",
	"organizationId": "&lt;set this to your organization ID&gt;",
	"pub":  "//this must be one line with no breaks
	MIIDbDCCAlQCCQD4lcSlmasmCTANBgkqhkiG9w0BAQsFADB4MQswCQYDVQQGEwJVUzELMAkGA1UECAwCVFgxDzANBgNVBAcMBkF1c3RpbjENMAsGA1UECgwEVGVzdDEOMAwGA1UECwwFVGVzdDIxDjAMBgNVBAMMBVRlc3QzMRwwGgYJKoZIhvcNAQkBFg10ZXN0QHRlc3QuY29tMB4XDTIxMDgwOTE0MTcxNFoXDTIyMDgwOTE0MTcxNFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAlRYMQ8wDQYDVQQHDAZBdXN0aW4xDTALBgNVBAoMBFRlc3QxDjAMBgNVBAsMBVRlc3QyMQ4wDAYDVQQDDAVUZXN0MzEcMBoGCSqGSIb3DQEJARYNdGVzdEB0ZXN0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMcHQWZRETqim3XzUQlAiujFEvsHIi1uJZKj+1lvPH36Ucqo3ORcoh/MM/zxVdahjhSyyp7MHuKBWnzft6bFeDEul6qKWGPAAzaxG/2xZSV3FggA9SyAZEDUpJ6mblwqm/EY4KmZi1FrNBUHfW2wwaqDexHPRDesRG6aI7Wuu4GdQUUqoTa2+Nv7kVgEDmGcfIjoWkGKHe+Yan95EITrq4jEFCE5Tg/vERnMvHfK2SovENZ13/pnwFYbeh1kfJSBzWW7yq8AyQAgAE9iqJXbJ/MAasir2vjUQ2+Hcl7WbkpoVjLqDt3rzV1T0Bsd4T9SC3wij9qjJSxa6vAgV4xn6bECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEADuMrtYW1Sf0IsZ4ZD9ipjUrFuTxqh+0M5Jk8h0QqAXEHA/MawedlU3JmE3NB/UR82/XUwdmtObGnFANuUQQ+8WMFpcNo/Sq2kg7juneHZroRh72o73UUMtHWHzo8s0fXElNal8h3SaAAnjMblCiN+gM1RvWMvhGrMTXp2XAcdIezXf8/FOZLlzOF9QylbSk1U4ayWBag6MydkxgHjkPKdShZROEm0oz/O7J/gNp/r7J8F42Rw9MmJh9qH3SFre13nQa8V7Kg+dJHZ/jpGtSlDHAxO0SSTrPXkwB+iBJ6hSkiL/J2Ep+lYHqVe3p5NXMOlTtJdbU4enHeLkD6PazKTw",
	"expiryDuration": "365"
		}
	}
```

```
{
"submitTimeUtc": "2026-01-22T14:36:31Z",
"status": "SUCCESS",
"keyInformation": {
	"provider": "nrtd",
	"tenant": "384259",
	"organizationId": "384259",
	"keyId": "937dfa75-acff-4f5b-9aab-66a49455ae04",
	"pub": "MIIDbDCCAlQCCQD4lcSlmasmCTANBgkqhkiG9w0BAQsFADB4MQswCQYDVQQGEwJVUzELMAkGA1UECAwCVFgxDzANBgNVBAcMBkF1c3RpbjENMAsGA1UECgwEVGVzdDEOMAwGA1UECwwFVGVzdDIxDjAMBgNVBAMMBVRlc3QzMRwwGgYJKoZIhvcNAQkBFg10ZXN0QHRlc3QuY29tMB4XDTIxMDgwOTE0MTcxNFoXDTIyMDgwOTE0MTcxNFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAlRYMQ8wDQYDVQQHDAZBdXN0aW4xDTALBgNVBAoMBFRlc3QxDjAMBgNVBAsMBVRlc3QyMQ4wDAYDVQQDDAVUZXN0MzEcMBoGCSqGSIb3DQEJARYNdGVzdEB0ZXN0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMcHQWZRETqim3XzUQlAiujFEvsHIi1uJZKj+1lvPH36Ucqo3ORcoh/MM/zxVdahjhSyyp7MHuKBWnzft6bFeDEul6qKWGPAAzaxG/2xZSV3FggA9SyAZEDUpJ6mblwqm/EY4KmZi1FrNBUHfW2wwaqDexHPRDesRG6aI7Wuu4GdQUUqoTa2+Nv7kVgEDmGcfIjoWkGKHe+Yan95EITrq4jEFCE5Tg/vERnMvHfK2SovENZ13/pnwFYbeh1kfJSBzWW7yq8AyQAgAE9iqJXbJ/MAasir2vjUQ2+Hcl7WbkpoVjLqDt3rzV1T0Bsd4T9SC3wij9qjJSxa6vAgV4xn6bECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEADuMrtYW1Sf0IsZ4ZD9ipjUrFuTxqh+0M5Jk8h0QqAXEHA/MawedlU3JmE3NB/UR82/XUwdmtObGnFANuUQQ+8WMFpcNo/Sq2kg7juneHZroRh72o73UUMtHWHzo8s0fXElNal8h3SaAAnjMblCiN+gM1RvWMvhGrMTXp2XAcdIezXf8/FOZLlzOF9QylbSk1U4ayWBag6MydkxgHjkPKdShZROEm0oz/O7J/gNp/r7J8F42Rw9MmJh9qH3SFre13nQa8V7Kg+dJHZ/jpGtSlDHAxO0SSTrPXkwB+iBJ6hSkiL/J2Ep+lYHqVe3p5NXMOlTtJdbU4enHeLkD6PazKTw",
	"keyType": "publickey",
	"status": "active",
	"expirationDate": "2022-08-09T14:17:14Z"
		}
	}
```

REST Interactive Example: Registering Your Certificate {#wh-fg-mle-dev-ex}
==========================================================================

Click this image to access the interactive code example for registering your certificate. The Live Console refers to this request as *Message-Level Encryption*.

#### Figure:

Registering Your Certificate [![Image and link to the interactive code example for creating a digital signature key.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/mle.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md#webhooks_manage-webhooks_message-level-encryption "")

Security Best Practices {#wh-fg-mle-secure}
===========================================

Here are some tips to ensure that your keys remain secure.
* Store private keys in a secure location with restricted permissions.
* Never commit private keys to version control.
* Rotate certificates before expiration.
* Use environment variables or secure vaults for production deployments.
* Keep back-up copies of your private keys in a secure location.
  {#wh-fg-mle-secure_ul_zv4_pg5_13c}

Securing Your Private Key
-------------------------

Keep your *request_private.pem* file secure. This private key is required to decrypt incoming webhook notifications. To modify the permissions so that only the file owner can read and write to the files, use this command:

```
chmod 600 request_private.pem
```

Troubleshooting {#wh-fg-mle-troubleshooting}
============================================

If you receive the *Key invalid or validity too long* error, try generating a certificate with shorter validity:

```
# 90-day validity
openssl req -x509 -newkey rsa:2048 -keyout request_private.pem
 -out request_certificate.pem -days 90 -nodes -subj 
"/CN=RequestKey/O=YourOrg/C=US" && cat request_certificate.pem
 | grep -v "BEGIN CERTIFICATE" | grep -v "END CERTIFICATE" | 
tr -d '\n' && echo				
```

Viewing Certificate Details {#wh-fg-mle-view}
=============================================

To verify your certificate details, use this command.

```
openssl x509 -in request_certificate.pem -text -noout
```

Create a Webhook Subscription {#wh-fg-subscribe-intro}
======================================================

This section describes how to create a webhook subscription using a REST API request. The request you send is dependent on your system's security policy:

* Mutual trust (default)
* Mutual trust and *OAuth* (optional)
* Mutual trust and *OAuth with JWT* (optional)

The Webhooks REST API uses the mutual trust security policy by default. In addition to mutual trust, you can also use the OAuth or OAuth JWT security policy. If you are not using OAuth security to authenticate your webhook notifications, use the default mutual trust request.

Create a Webhook Subscription {#wh-fg-subscription-mutual-api-intro}
====================================================================

This section describes how to create webhook subscription using mutual trust. Mutual trust is the default security policy. For more information, see [Set Up Your Security](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-server-security.md "").  
You can subscribe to multiple webhook products and event types in the same request.

Health Check URL {#wh-fg-subscription-mutual-api-intro_healthcheck-url}
-----------------------------------------------------------------------

`Cybersource` recommends that you include a health check URL in the subscription request. A health check URL ensures that you do not miss any notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

URL Validation {#wh-fg-subscription-mutual-api-intro_url-validation}
--------------------------------------------------------------------

When a webhook subscription is created or updated, the URLs associated with that subscription are evaluated through a validation and approval process that can take 1-2 business days. See [URL Review and Approval Process](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro/wh-fg-url-validation.md "")

Retry Policy {#wh-fg-subscription-mutual-api-intro_retry-policy}
----------------------------------------------------------------

If your webhook URL or health check URL are unresponsive when sent a notification, `Cybersource` resends the notification according to the subscription's *retry policy* . By default, `Cybersource` sends you 3 notification attempts, beginning 1 minute after the initial failed attempt. Retry attempts occur in 1 minute intervals if your URL remains unresponsive. You can configure the default retry policy when you create or update a subscription. For more information about how to configure the retry policy, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Subscription ID {#wh-fg-subscription-mutual-api-intro_subscribe}
----------------------------------------------------------------

> IMPORTANT
> After sending this request, you receive a response with a subscription ID in the webhookId field. Save this ID in your system to send follow-on requests that enable you to update and manage the subscription. For more information about the follow-on requests, see [Manage Webhook Subscriptions Requests](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro.md "").

Endpoints {#wh-fg-subscription-mutual-api-intro_endpoint-create-sub}
--------------------------------------------------------------------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/notification-subscriptions/v2/webhooks`
* **Production:** `POST ``https://api.cybersource.com``/notification-subscriptions/v2/webhooks`
* **India Production:** `POST https://api.in.cybersource.com/notification-subscriptions/v2/webhooks`

Required Fields for Subscribing to Webhooks {#wh-fg-subscription-mutual-req-fields}
===================================================================================

description
:
Description of the webhook subscription.

name
:
Name of the webhook subscription.

organizationId
:
Set to your organization ID or merchant ID.

products.eventTypes
:
For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

products.productId
:
For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

securityPolicy.securityType
:
Set to `KEY`.

webhookUrl
:
The URL in your system to which webhooks notifications will be sent.

Optional Fields for Subscribing to Webhooks {#wh-fg-subscription-mutual-opt-fields}
===================================================================================

deactivateflag
:
Required when the healthCheckUrl field is present.
:
Set to `true` to automatically activate the subscription.

healthCheckUrl
:
Set to the health check URL. Required to auto-activate the subscription. If you do not include this field, the created subscription is inactive. An inactive subscription does not send notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

notificationScope.scopeData
:
Set to the organization IDs that you want to have receive notifications when events occur in those organizations. Concatenate each organization ID with the comma character (`,`).

retryPolicy.deactivateFlag
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.firstRetry
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.interval
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.numberOfRetries
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceCount
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceWaitTime
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Example: Creating a Webhook Subscription {#wh-fg-subscription-mutual-ex}
========================================================================

```
{
  "name": "My Custom Webhook",
  "description": "Sample Webhook from Developer Center",
  "organizationId": "&lt;SET TO YOUR ORGANIZATION ID OR MERCHANT ID&gt;",
  "products": [
    {
      "productId": "product1.name",
      "eventTypes": [
        "product.name.event.type"
        "product.name.event.type"
        "product.name.event.type"
      ]
    }
    {
      "productId": "product2.name",
      "eventTypes": [
        "product.name.event.type"
        "product.name.event.type"
        "product.name.event.type"
        "product.name.event.type"
        "product.name.event.type"
        "product.name.event.type"
      ]
    }
  ],
  "webhookUrl": "https://MyWebhookServer.com:8443/simulateClient",
  "securityPolicy": {
    "securityType": "KEY"
  }
}
```

Response to a Successful Request

```
{
  "organizationId": "organizationId",
  "productId": "terminalManagement",
  "eventTypes": [
    "terminalManagement.assignment.update"
  ],
  "webhookId": "ddb9bced-c3e3-1b1d-e053-9c588e0a3c42",
  "name": "My Custom Webhook",
  "webhookUrl": "https://MyWebhookServer.com:443/simulateClient",
  "healthCheckUrl": "https://MyWebhookServer.com:443/simulateClientHealthCheck",
  "createdOn": "2022-04-28T15:39:56.928Z",
  "status": "ACTIVE",
  "description": "Sample Webhook from Developer Center",
  "retryPolicy": {
    "algorithm": "ARITHMETIC",
    "firstRetry": "1",
    "interval": "1",
    "numberOfRetries": "3",
    "deactivateFlag": "false",
    "repeatSequenceCount": '0",
    "repeatSequenceWaitTime": "0"
  },
  "securityPolicy": {
    "securityType": "KEY",
    "digitalSignatureEnabled": "yes"
  },
  "version": "3",
  "notificationScope": "SELF"
}
```

**Response Codes** {#wh-fg-subscription-mutual-reply-status}
============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

**Notification Scope Response Indicators** {#wh-fg-subscription-notification-scope-mutual}
==========================================================================================

The notificationScope response field indicates which organizations receive the webhook notification. By default, notifications use the `DESCENDANTS` setting. To modify this setting, include the notificationScope.scopeData field in your request.  
These are all possible field values:

`SELF`
:
Only the organization creating the webhook subscription receives notifications when a subscribed event occurs.

`DESCENDANTS` (default)
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any of their children/descendant accounts in their portfolio hierarchy. This is the default notification setting.

`CUSTOM`
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any organization listed in the notificationScope.scopeData request field.

**Subscription Statuses** {#wh-fg-status-mutual}
================================================

When you create a subscription, its status is indicated in the status response field. If you did not include a health check URL in your request, the subscription is set to `INACTIVE`. If you included a health check URL and `Cybersource` receives a response from the health check URL, the subscription status is set to `ACTIVE`.  
These are the five possible statuses a subscription can be set to:

`PENDING_REVIEW`
:
One or more submitted URLs are being validated or awaiting required security approval.

`BLOCKED`
:
One or more URLs were rejected or identified as unsafe or non-compliant. The subscription cannot proceed until the URL(s) are updated.

`ACTIVE`
:
The subscription is ready to send notifications or is actively sending notifications.

`INACTIVE`
:
The subscription has not been activated. Add a health check URL to activate it. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

`SUSPENDED`
:
The subscription was active, but the webhook URL or the health check URL became unreachable. When the URL becomes reachable, the status changes to `ACTIVE` and notifications resume.

**REST Interactive Example: Create a Webhook Subscription** {#wh-fg-subscription-mutual-ex-dev}
===============================================================================================

Click this image to access the interactive code example for creating a webhook subscription.

#### Figure:

Create a Webhook Subscription [![Image and link to the interactive code example for creating a webhook
subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/create-webhook-dev.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_create-new-webhooks_create-a-new-webhook-subscription_samplerequests-dropdown_create-webhook-using-oauth-with-client-credentials_liveconsole-tab-request-body "")

Create a Webhook Subscription Using OAuth {#wh-fg-subscription-oauth-api-intro}
===============================================================================

This section describes how to create a webhook subscription using the OAuth security policy, in addition to mutual trust. You can subscribe to multiple webhook products and event types in the same request. After creating a subscription, you receive a notification every time your subscribed events occur.  
The *OAuth* security policy with client credentials is an authentication method that is designed for applications to communicate with each other. Basic authentication is the most common mechanism for authenticating a client with the client credentials. This authentication method enables `Cybersource` services to obtain only the relevant user data without exposing the user's credentials.

Health Check URL
----------------

`Cybersource` recommends that you include a health check URL in the subscription request. A health check URL ensures that you do not miss any notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

URL Validation
--------------

When a webhook subscription is created or updated, the URLs associated with that subscription are evaluated through a validation and approval process that can take 1-2 business days. See [URL Review and Approval Process](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro/wh-fg-url-validation.md "")

Retry Policy
------------

If your webhook URL or health check URL are unresponsive when sent a notification, `Cybersource` resends the notification according to the subscription's *retry policy* . By default, `Cybersource` sends you 3 notification attempts, beginning 1 minute after the initial failed attempt. Retry attempts occur in 1 minute intervals if your URL remains unresponsive. You can configure the default retry policy when you create or update a subscription. For more information about how to configure the retry policy, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Subscription ID
---------------

> IMPORTANT
> After sending this request, you receive a response with a subscription ID in the webhookId field. Save this ID in your system to send follow-on requests that enable you to update and manage the subscription. For more information about the follow-on requests, see [Manage Webhook Subscriptions Requests](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro.md "").

Endpoints
---------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/notification-subscriptions/v2/webhooks`
* **Production:** `POST ``https://api.cybersource.com``/notification-subscriptions/v2/webhooks`
* **India Production:** `POST https://api.in.cybersource.com/notification-subscriptions/v2/webhooks`

Required Fields for Subscribing to Webhooks Using OAuth {#wh-fg-subscription-oauth-req-fields}
==============================================================================================

description
:
Description of the webhook subscription.

name
:
Name of the webhook subscription.

organizationId
:
Set to your organization ID or merchant ID.

products.eventTypes
:
For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

products.productId
:
For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

securityPolicy.config.oAuthTokenExpiry
:

securityPolicy.config.oAuthTokenType
:
Set to `Bearer`.

securityPolicy.config.oAuthURL
:
This is the URL of your OAuth server.

securityPolicy.securityType
:
Set to `oAuth`.

webhookUrl
:
The URL in your system to which webhooks notifications will be sent.

Optional Fields for Subscribing to Webhooks Using OAuth {#wh-fg-subscription-oauth-opt-fields}
==============================================================================================

deactivateflag
:
Required if healthCheckUrl field is present.
:
Set to `true` to automatically activate the subscription.

healthCheckUrl
:
Set to the health check URL. Required to auto-activate the subscription. If you do not include this field, the created subscription is inactive. An inactive subscription does not send notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

notificationScope.scopeData
:
Set to the organization IDs that you want to receive notifications for when subscribed events occur in those organizations. Concatenate each organization ID with the comma character (`,`).

retryPolicy.deactivateFlag
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.firstRetry
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.interval
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.numberOfRetries
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceCount
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceWaitTime
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Example: Creating a Webhook Subscription Using OAuth {#wh-fg-subscription-oauth-ex}
===================================================================================

```
{
  "name": "My Custom Webhook",
  "description": "",
  "organizationId": "&lt;INSERT ORGANIZATION ID HERE&gt;",
  "products": [
    {
      "productId": "product.name",
      "eventTypes": [
        "product.name.event.type"
      ]
    }
  ],
  "webhookUrl": "https://MyWebhookServer.com:8443/simulateClient",
  "securityPolicy": {
    "securityType": "oAuth",
    "config": {
      "oAuthTokenExpiry": 365,
      "oAuthURL": "https://MyWebhookServer.com:8443/oAuthToken",
      "oAuthTokenType": "Bearer"
    }
  }
}
```

```
{
  "organizationId" : "org1",
  "productId" : "terminalManagement",
  "eventTypes" : [ 
	"terminalManagement.assignment.update" 
],
  "webhookId" : "d7399cb6-ff9f-72d9-e053-3cb8d30a62ee",
  "webhookUrl" : "https://mywebhookserver.com/simulateclient",
  "healthCheckUrl" : "https://mywebhookserver.com/simulateclient/healthcheck",
  "createdOn" : "2022-02-04T22:17:43.045Z",
  "status" : "INACTIVE",
  "retryPolicy" : {
    "algorithm" : "ARITHMETIC",
    "firstRetry" : "1",
    "interval" : "1",
    "numberOfRetries" : "3",
    "deactivateFlag" : "false",
    "repeatSequenceCount" : "0",
    "repeatSequenceWaitTime" : "0"
  },
  "securityPolicy" : {
    "securityType" : "oAuth",
    "proxyType" : "internal",
    "digitalSignatureEnabled" : "yes",
    "config" : {
      "oAuthTokenExpiry" : "300,
      "oAuthURL" : "https://myoauthserver.com/simulator/v1/token",
      "oAuthTokenType" : "Bearer"
    }
  },
  "version" : "3",
  "notificationScope" : "SELF"
}
```

**Response Codes** {#wh-fg-subscription-oath-reply-status}
==========================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

**Notification Scope Response Indicators** {#wh-fg-subscription-notification-scope-oauth}
=========================================================================================

The notificationScope response field indicates which organizations receive the webhook notification. By default, notifications use the `DESCENDANTS` setting. To modify this setting, include the notificationScope.scopeData field in your request.  
These are all possible field values:

`SELF`
:
Only the organization creating the webhook subscription receives notifications when a subscribed event occurs.

`DESCENDANTS` (default)
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any of their children/descendant accounts in their portfolio hierarchy. This is the default notification setting.

`CUSTOM`
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any organization listed in the notificationScope.scopeData request field.

**Subscription Statuses** {#wh-fg-status-oauth}
===============================================

When you create a subscription, its status is indicated in the status response field. If you did not include a health check URL in your request, the subscription is set to `INACTIVE`. If you included a health check URL and `Cybersource` receives a response from the health check URL, the subscription status is set to `ACTIVE`.  
These are the five possible statuses a subscription can be set to:

`PENDING_REVIEW`
:
One or more submitted URLs are being validated or awaiting required security approval.

`BLOCKED`
:
One or more URLs were rejected or identified as unsafe or non-compliant. The subscription cannot proceed until the URL(s) are updated.

`ACTIVE`
:
The subscription is ready to send notifications or is actively sending notifications.

`INACTIVE`
:
The subscription has not been activated. Add a health check URL to activate it. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

`SUSPENDED`
:
The subscription was active, but the webhook URL or the health check URL became unreachable. When the URL becomes reachable, the status changes to `ACTIVE` and notifications resume.

**REST Interactive Example: Create a Webhook Subscription Using OAuth** {#wh-fg-subscription-oauth-dev-ex}
==========================================================================================================

Click this image to access the interactive code example for creating a webhook subscription using OAuth.

#### Figure:

Create a Webhook Subscription Using OAuth [![Image and link to the interactive code example for creating a
webhook subscription using OAuth.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/create-webhook-dev.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_create-new-webhooks_create-a-new-webhook-subscription_samplerequests-dropdown_create-webhook-using-oauth-with-client-credentials_liveconsole-tab-request-body "")

Create a Webhook Subscription Using OAuth with JWT {#wh-fg-subscription-oauth-jwt-api-intro}
============================================================================================

This section describes how to create a webhook subscription using OAuth with a JSON Web Token (JWT), in addition to mutual trust. You can subscribe to multiple webhook products and event types in the same request. After creating a subscription, you receive a notification every time your subscribed events occur.  
The *OAuth with JWT* security policy is an authentication method in which your system sends a JSON Web Token. This method bypasses domain headers and minimizes the need for server-side authentication checks.

Health Check URL
----------------

`Cybersource` recommends that you include a health check URL in the subscription request. A health check URL ensures that you do not miss any notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

URL Validation
--------------

When a webhook subscription is created or updated, the URLs associated with that subscription are evaluated through a validation and approval process that can take 1-2 business days. See [URL Review and Approval Process](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscribe-intro/wh-fg-url-validation.md "")

Retry Policy
------------

If your webhook URL or health check URL are unresponsive when sent a notification, `Cybersource` resends the notification according to the subscription's *retry policy* . By default, `Cybersource` sends you 3 notification attempts, beginning 1 minute after the initial failed attempt. Retry attempts occur in 1 minute intervals if your URL remains unresponsive. You can configure the default retry policy when you create or update a subscription. For more information about how to configure the retry policy, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Subscription ID
---------------

> IMPORTANT
> After sending this request, you receive a response with a subscription ID in the webhookId field. Save this ID in your system to send follow-on requests that enable you to update and manage the subscription. For more information about the follow-on requests, see [Manage Webhook Subscriptions Requests](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro.md "").

Endpoints
---------

Send a POST request to one of these endpoints:

* **Test:** `POST ``https://apitest.cybersource.com``/notification-subscriptions/v2/webhooks`
* **Production:** `POST ``https://api.cybersource.com``/notification-subscriptions/v2/webhooks`
* **India Production:** `POST https://api.in.cybersource.com/notification-subscriptions/v2/webhooks`

Required Fields for Subscribing to Webhooks Using OAuth with JWT {#wh-fg-subscription-oauth-jwt-req-fields}
===========================================================================================================

description
:
Description of the webhook subscription.

name
:
Name of the webhook subscription.

organizationId
:
Set to your organization ID or merchant ID.

products.eventTypes
:
For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

products.productId
:
For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

securityPolicy.config.additionalConfig.aud
:

securityPolicy.config.additionalConfig.client_id
:

securityPolicy.config.additionalConfig.keyId
:

securityPolicy.config.additionalConfig.scope
:

securityPolicy.config.oAuthTokenExpiry
:
Set to `365`.

securityPolicy.config.oAuthTokenType
:
Set to `Bearer`.

securityPolicy.config.oAuthUrl
:
This is the URL of your OAuth server.

securityPolicy.securityType
:
Set to `oAuth_JWT`.

webhookUrl
:
The URL in your system to which webhooks notifications will be sent.

Optional Fields for Subscribing to Webhooks Using OAuth with JWT {#wh-fg-subscription-oauth-jwt-opt-fields}
===========================================================================================================

deactivateflag
:
Required if the healthCheckUrl field is present.
:
Set to `true` to automatically activate the subscription.

healthCheckUrl
:
Set to the health check URL. Required to auto-activate the subscription. If you do not include this field, the created subscription is inactive. An inactive subscription does not send notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

notificationScope.scopeData
:
Set to the organization IDs that you want to receive notifications for when events occur in those organizations. Concatenate each organization ID with the comma character (`,`).

retryPolicy.deactivateFlag
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.firstRetry
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.interval
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.numberOfRetries
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceCount
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceWaitTime
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

Example: Creating a Webhook Subscription Using OAuth with JWT {#wh-fg-subscription-oauth-jwt-ex}
================================================================================================

```
{
  "name": "My Custom Webhook",
  "description": "Sample Webhook from Developer Center",
  "organizationId": "&lt;INSERT ORGANIZATION ID HERE&gt;",
  "products": [
    {
      "productId": "product.id",
      "eventTypes": [
        "product.id.event.type"
      ]
    }
  ],
  "webhookUrl": "https://MyWebhookServer.com:8443/simulateClient",
  "securityPolicy": {
    "securityType": "oAuth_JWT",
    "config": {
      "oAuthTokenExpiry": "365",
      "oAuthURL": "https://MyWebhookServer.com:443/oAuthToken",
      "oAuthTokenType": "Bearer",
      "additionalConfig": {
        "aud": "idp.api.myServer.com",
        "client_id": "650538A1-0000-0000-0000-932ABC57AD70",
        "keyId": "y-00000000000000-eAZ34pR9Ts",
        "scope": "merchantacq:rte:write"
      }
    }
  }
}
```

```
{
  "organizationId": "organizationId",
  "productId": "product.id",
  "eventTypes": [
    "product.id.event.type"
  ],
  "webhookId": "fe46bf08-3918-21ba-e053-a1588d0aeefa",
  "name": "My Custom Webhook",
  "webhookUrl": "https://MyWebhookServer.com:443/simulateClient",
  "healthCheckUrl": "https://MyWebhookServer.com:443/simulateClientHealthCheck",
  "createdOn": "2023-06-16T21:19:54.667Z",
  "status": "INACTIVE",
  "description": "Sample Webhook from Developer Center",
  "retryPolicy": {
    "algorithm": "ARITHMETIC",
    "firstRetry": 1,
    "interval": 1,
    "numberOfRetries": 3,
    "deactivateFlag": false,
    "repeatSequenceCount": 0,
    "repeatSequenceWaitTime": 0
  },
  "securityPolicy": {
    "securityType": "oAuth_JWT",
    "proxyType": "external",
    "digitalSignatureEnabled": "yes",
    "config": {
      "oAuthTokenExpiry": 365,
      "oAuthURL": "https://MyWebhookServer.com:443/oAuthToken",
      "oAuthTokenType": "Bearer",
      "additionalConfig": {
        "aud": "idp.api.myServer.com",
        "client_id": "650538A1-0000-0000-0000-932ABC57AD70",
        "keyId": "y-00000000000000-eAZ34pR9Ts",
        "scope": "merchantacq:rte:write"
      }
    }
  },
  "version": "3",
  "deliveryType": "nrtdCentral",
  "notificationScope": "SELF"
}
```

**Response Codes** {#wh-fg-subscription-oauth-jwt-reply-status}
===============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

**Notification Scope Response Indicators** {#wh-fg-subscription-notification-scope-oauth-jwt}
=============================================================================================

The notificationScope response field indicates which organizations receive the webhook notification. By default, notifications use the `DESCENDANTS` setting. To modify this setting, include the notificationScope.scopeData field in your request.  
These are all possible field values:

`SELF`
:
Only the organization creating the webhook subscription receives notifications when a subscribed event occurs.

`DESCENDANTS` (default)
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any of their children/descendant accounts in their portfolio hierarchy. This is the default notification setting.

`CUSTOM`
:
The organization creating the webhook subscription receives notifications when a subscribed event occurs in their organization and in any organization listed in the notificationScope.scopeData request field.

**Subscription Statuses** {#wh-fg-status-oauth-jwt}
===================================================

When you create a subscription, its status is indicated in the status response field. If you did not include a health check URL in your request, the subscription is set to `INACTIVE`. If you included a health check URL and `Cybersource` receives a response from the health check URL, the subscription status is set to `ACTIVE`.  
These are the five possible statuses a subscription can be set to:

`PENDING_REVIEW`
:
One or more submitted URLs are being validated or awaiting required security approval.

`BLOCKED`
:
One or more URLs were rejected or identified as unsafe or non-compliant. The subscription cannot proceed until the URL(s) are updated.

`ACTIVE`
:
The subscription is ready to send notifications or is actively sending notifications.

`INACTIVE`
:
The subscription has not been activated. Add a health check URL to activate it. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

`SUSPENDED`
:
The subscription was active, but the webhook URL or the health check URL became unreachable. When the URL becomes reachable, the status changes to `ACTIVE` and notifications resume.

**REST Interactive Example: Create a Webhook Subscription Using OAuth with JWT** {#wh-fg-subscription-oauth-jwt-dev-ex}
=======================================================================================================================

Click this image to access the interactive code example for creating a webhook subscription using OAuth with JWT.

#### Figure:

Create a Webhook Subscription Using OAuth with JWT [![Image and link to the interactive code example for creating a
webhook subscription using OAuth with JWT.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/create-webhook-dev.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_create-new-webhooks_create-a-new-webhook-subscription_samplerequests-dropdown_create-webhook-using-oauth-with-jwt_liveconsole-tab-request-body "")

URL Review and Approval Process {#wh-fg-url-validation}
=======================================================

When a webhook subscription is created or updated, the URLs associated with that subscription are evaluated through a validation and approval process.  
URL validation is designed to:

* **Reduce security risk** by preventing outbound calls to unapproved endpoints.

* **Improve compliance** through stronger review and approval controls.

* **Increase transparency** with clearer client-visible statuses.

* **Support scale** through a standardized and repeatable validation process.
  {#wh-fg-url-validation_ul_qnx_jdt_1jc}  
  URL validation applies to:

* **Webhook URL** (required)

* **OAuth URL** (if applicable)

* **Health Check URL** (if applicable)
  {#wh-fg-url-validation_ul_enx_jdt_1jc}

**Overview** {#wh-fg-url-validation_section_hnx_jdt_1jc}
--------------------------------------------------------

1. A webhook subscription is created or updated.
2. Submitted URLs are checked against existing approval records.
3. New or unknown URLs are evaluated through manual validation.
4. If additional review is required, the subscription status changes to **PENDING_REVIEW**.
5. If any URL is rejected or blocked, the subscription status changes to **BLOCKED**.
6. If all required URLs are approved, the subscription status changes to **INACTIVE**.
   {#wh-fg-url-validation_ol_inx_jdt_1jc}

Status Descriptions
-------------------

|     **Status**     |                                                            **Description**                                                             |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **PENDING_REVIEW** | One or more submitted URLs are being validated or awaiting required security approval. Review can take 1-2 business days.              |
| **BLOCKED**        | One or more URLs were rejected or identified as unsafe or non-compliant. The subscription cannot proceed until the URL(s) are updated. |
| **INACTIVE**       | All required approvals are complete, and the subscription is ready under the existing activation flow.                                 |

**If Your Subscription Is Marked BLOCKED** {#wh-fg-url-validation_section_onx_jdt_1jc}
--------------------------------------------------------------------------------------

This means one or more URLs associated with the subscription cannot be used in their current form. To continue, the client must update the affected URL(s) and resubmit.

Create a Sample Webhook Subscription {#wh-fg-trig-tms-webhook}
==============================================================

Follow these steps to create a sample webhook subscription and then trigger a test webhook notification. This sample subscription uses the `Token Management Service` (`TMS`). IMPORTANT

> You must first confirm that your account or organization ID is enabled for ` TMS ` and that a ` TMS ` vault is set up. For assistance, contact ` Cybersource ` Customer Support.

1. Create a `TMS` webhook subscription for your organization ID using this endpoint:  
   ` POST ``https://apitest.cybersource.com``/notification-subscriptions/v2/webhooks`  
   Set the productId field to `tokenManagement` and the eventTypes field to `tms.networktoken.provisioned`. The following example creates a webhook subscription using Mutual Trust, which is the default security policy.

   ```
   {
     "name": "TMS Webhook",
     "description": "Sample TMS Webhook from Developer Center",
     "organizationId": "organizationId",
     "productId": "tokenManagement",
     "eventTypes": [
       "tms.networktoken.provisioned"
     ],
     "webhookUrl": "https://MyWebhookServer.com:8443/simulateClient",
     "healthCheckUrl": "https://MyWebhookServer.com:8443/simulateClientHealthCheck",
     "notificationScope": "SELF",
     "retryPolicy": {
       "algorithm": "ARITHMETIC",
       "firstRetry": 1,
       "interval": 1,
       "numberOfRetries": 3,
       "deactivateFlag": "false",
       "repeatSequenceCount": 0,
       "repeatSequenceWaitTime": 0
     },
     "securityPolicy": {
       "securityType": "KEY",
       "proxyType": "external"
     }
   }
   ```

   {#wh-fg-trig-tms-webhook_codeblock_fpt_lv2_syb}

2. Go to the [Create an Instrument Identifier](https://developer.cybersource.com/api-reference-assets/index.md#token-management_instrument-identifier_create-an-instrument-identifier "") section in the API Reference.

3. Click the **Configuration** tab.

4. In the Sample Request drop-down menu, choose Create Instrument Identifier using a Card and Create Network Token:  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/wh-fg-tms-create-ii.png/jcr:content/renditions/original)

5. Set the card.number field to a test PAN. (If you need a test PAN, contact `Cybersource` customer support). Send the request to this endpoint:  
   `POST ``https://apitest.cybersource.com``/tms/v1/instrumentidentifiers`{#wh-fg-trig-tms-webhook_codeblock_fkq_ykl_5yb}

   ```
   {
     "type": "enrollable card",
     "card": {
       "number": "411111111111XXXX",  // Replace the ‘X’s with 1
       "expirationMonth": "12",
       "expirationYear": "2031"
     }
   }
   ```

   {#wh-fg-trig-tms-webhook_codeblock_rbx_fhf_syb} IMPORTANT

   > A test PAN can have only one associated instrument identifier. If you need to test multiple webhook notifications, delete the instrument identifier created for that PAN before using the *Delete an Instrument Identifier API*.

6. Click Send. After you receive a successful response, your system should receive a webhook event notification.  
   For an example of a complete webhook notification, including the header and payload information, see [Example: Webhook Notification](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-notification-format.md "").

Optional Set-Up Tasks {#wh-fg-optional-intro}
=============================================

You can complete optional set-up tasks during or after creating a webhook subscription. These tasks are optional and are not required in order to successfully set-up webhook subscriptions.

* Include a health check URL to enable `Cybersource` to monitor your server's status for reliability.
* Validate the integrity of a webhook notification.
* Set up a retry policy for how to receive notifications when your server URL is initially unresponsive.

Webhook Health Check URL and Automatic Revalidation {#wh-fg-subscription-health-check-url}
==========================================================================================

When you create a webhook subscription, `Cybersource` recommends that you include a health check URL in the request. Including a health check URL enables `Cybersource` to monitor your server's status for reliability. When `Cybersource` detects that your health check URL is unresponsive, notification deliveries are withheld until your health check URL becomes responsive again. A health check URL ensures that you do not miss any notifications.  
To add a health check URL to your *create a subscription* request, include the healthCheckurl field and set it to your health check URL. You must also include the deactivateflag field and set it to `true` to enable `Cybersource` to withhold notifications for periods when your server becomes unresponsive.

Automatic Activation
--------------------

After you successfully create or update a subscription, `Cybersource` pings your health check URL within five to ten minutes. If `Cybersource` receives a response, the subscription status automatically becomes `ACTIVE` and notifications are delivered. When `Cybersource` does not receive a response, your subscription status remains `SUSPENDED` until `Cybersource` receives a response. If you did not include a health check URL when you created the subscription, `Cybersource` pings your webhook URL for automatic activation instead. You can also activate a subscription that is not automatically activated by sending a PUT request. For more information, see [Activate a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro/wh-fg-subscription-manage-activate-intro.md "").

#### Figure:

Webhook Automatic Activation ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/webhooks-subscription-cybs-600x400.svg/jcr:content/renditions/original)

Automatic Revalidation
----------------------

After the subscription's initial activation, `Cybersource` continues to monitor your server status. If `Cybersource` detects that your server is unavailable, your subscription status automatically updates to `SUSPENDED`, and notifications are withheld. When `Cybersource` detects that your server is available again, your subscription status automatically updates to `ACTIVE`, and all withheld notifications are delivered.

Configure the Retry Policy {#wh-fg-optional-retry}
==================================================

If your webhook URL or health check URL are unresponsive, `Cybersource` resends the webhook notifications according to the subscription's *retry policy*. All subscriptions have a default retry policy (see the default values in the field descriptions below). You can change the retry policy when you create a subscription or update the webhook subscription by modifying the retry field values described below.  
To configure a subscription's retry policy, include these required fields in the *create a subscription* request or an *update a subscription* request:

retryPolicy.deactivateFlag
:
Set to one of these values:
:
* `false`: Notifications are *not* withheld when your webhook URL or health check URL are unresponsive. **This value is the default.**
* `true`: Notifications are withheld when your webhook URL or health check URL are unresponsive, and the subscription status updates to `SUSPENDED`. When the URLs become responsive again, the withheld notifications are sent and the subscription status updates to `ACTIVE`.

retryPolicy.firstRetry
:
The number of minutes before the notification is resent. **The default value is `1`.**

retryPolicy.interval
:
The number of minutes between each retry attempt. **The default value is `1`.**

retryPolicy.numberOfRetries
:
The number of retry attempts. **The default value is `3`.**

retryPolicy.repeatSequenceCount
:
The number of times to repeat the retry sequence. **The default value is `0`.**

retryPolicy.repeatSequenceWaitTime
:
The number of minutes between each repeat sequence. **The default value is `0`.**

Example: Retry Policy in a Subscription Request {#wh-fg-optional-retry-example}
===============================================================================

This example shows how to format a retry policy in a request.

```
"retryPolicy": {
  "firstRetry": "1",
  "interval": "1",
  "numberOfRetries": "3",
  "deactivateFlag": "false",
  "repeatSequenceCount": "0",
  "repeatSequenceWaitTime": "0"
}
```

Webhook Notification Field Descriptions {#wh-fg-notification-format}
====================================================================

Each webhook notification that you receive contains a message body with fields. This section describes the possible fields and values you can receive in a notification. The default version of the Webhooks API is version 3, and the information in this section describes version 3.

Notification Message Body
-------------------------

The message body contains fields associated with the notification and the payload of the event that generated the notification.

webhookId
:
The identifier of the webhook subscription that generated the notification.

transactionTraceId
:
The identifier of the notification attempt. Every retry attempt has a unique transaction trace ID.

productId
:
The identifier of the product that generated the event.

organizationId
:
The identifier of the organization that is subscribed to the notification.

eventType
:
The type of event that generated the notification.

eventDate
:
The timestamp of when the event occurred.

payload
:
The data generated by the event.

requestType
:
The indicator of whether the notification is new or a retry attempt.

Example: Notification Payload {#wh-fg-notification-payload-ex}
==============================================================

TMS Webhook Notification

```
Headers
POST /test HTTP/1.1Host: test.test.comContent-Length: 537 Content-Type: 
application/jsonv-c-event-type: product.event.typev-c-organization-id: 
orgidv-c-product-name: productv-c-request-type: NEWv-c-retry-count: 0
v-c-signature "t=timestamp;keyId=key-UUID;sig=calculatedDigitalSignature"
v-c-transaction-trace-id: "7ac2ad9f-6a89-d3e9-e053-34b8d30aaf40"
v-c-webhook-id: "e339e8b1-d540-4efd-e053-8d588e0a2de5"

Body Payload
{
    "eventType": "tms.networktoken.provisioned",
    "webhookId": "e339e8b1-d540-4efd-e053-8d588e0a2de5",
    "productId": "tokenManagement",
    "organizationId": "sampleSubscriptionHolder",
    "eventDate": "2022-07-20T11:38:45",
    "transactionTraceId": "7ac2ad9f-6a89-d3e9-e053-34b8d30aaf40",
    "retryNumber": 0,
    "payload": {
      "data": {
        "_links": {
          "paymentInstruments": [
             {
               "href": "/tms/v1/paymentinstruments/...................."
             }
           ],
           "instrumentIdentifiers": [
             {
               "href": "/tms/v1/instrumentidentifiers/...................."
                 }
            ]
          },
            "id": "...................",
            "type": "tokenizedCardEnrollments",
            "version": "1.0"
        },
        "organizationId": "sampleSelfOrChildOrg"
    },
    "requestType": "NEW"
}
```

Manage Webhook Subscriptions Requests {#wh-fg-subscription-manage-intro}
========================================================================

This section describes how to manage your webhook subscriptions using the REST API. These follow-on requests require the webhook subscription ID.  
After you set up a webhook subscription, you can manage your subscription using these requests:

* Retrieve the details of a subscription
* Retrieve a list of subscriptions by product and event
* Update a subscription
* Delete a subscription
* Verify a subscription's configuration
* Activate a subscription
* Deactivate a subscription

Retrieve the Details of a Webhook Subscription {#wh-fg-subscription-manage-get-intro}
=====================================================================================

This section describes how to retrieve the details of a webhook subscription, such as the subscription status, which organizations are receiving the notifications, and other useful details.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints
---------

Send a GET request to this endpoint. The *`{webhookId}`* is the webhook subscription ID.

* **Test:** `GET ``apitest.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **Production:** `GET ``api.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **India Production:** `GET https://api.in.cybersource.com/notification-subscriptions/v2/webhooks/`*{webhookId}*

Example: Retrieving the Details of a Webhook Subscription {#wh-fg-subscription-manage-get-ex}
=============================================================================================

```keyword
GET https://apitest.cybersource.com/notification-subscriptions/v1/webhooks/ddb9bced-c3e3-1b1d-e053-9c588e0a3c42
```

```
{
  "organizationId": "organizationId",
  "productId": "terminalManagement",
  "eventTypes": [
    "terminalManagement.assignment.update"
  ],
  "webhookId": "ddb9bced-c3e3-1b1d-e053-9c588e0a3c42",
  "webhookUrl": "https://MyWebhookServer.com:443/simulateClient",
  "healthCheckUrl": "https://MyWebhookServer.com:443/simulateClientHealthCheck",
  "createdOn": "2022-04-28 15:39:56.931",
  "status": "SUSPENDED",
  "retryPolicy": {
    "algorithm": "ARITHMETIC",
    "firstRetry": 1,
    "interval": 1,
    "numberOfRetries": 3,
    "deactivateFlag": false,
    "repeatSequenceCount": 0,
    "repeatSequenceWaitTime": 0
  },
  "securityPolicy": {
    "securityType": "KEY",
    "digitalSignatureEnabled": "yes"
  },
  "version": "3",
  "deliveryType": "nrtdCentral",
  "notificationScope": "DESCENDANTS"
}
```

Response Codes {#wh-fg-subscription-manage-get-reply-status}
============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Interactive Example: Retrieve the Details of a Webhook Subscription {#wh-fg-subscription-manage-get-dev-ex}
================================================================================================================

Click this image to access the interactive code example for retrieving the details of a webhook subscription.

#### Figure:

Retrieve the Details of a Webhook Subscription [![Image and link to the interactive code example for retrieving the
details of a webhook subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-get-details.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_get-details-on-a-single-webhook "")

Retrieve All of an Organization's Subscriptions {#wh-fg-subscription-manage-get-list-intro}
===========================================================================================

This section describes how to retrieve a list of the webhook subscriptions to which an organization subscribes. This request requires you to include the organization ID in the endpoint as a query parameter. You have the option to include a product ID and event type as additional query parameters. If you include any of the optional query parameters, you must concatenate them by separating each parameter with the ampersand character (`&`).

Endpoints
---------

Send a GET request to one of these endpoints. The *`{organization.id}`* is the organization ID or merchant ID.

* **Test:** `GET ``https://apitest.cybersource.com``/notification-subscriptions/v2/webhooks?organizationId=`*{organization.id}*
* **Production:** `GET ``https://api.cybersource.com``/notification-subscriptions/v2/webhooks?organizationId=`*{organization.id}*
* **India Production:** `GET https://api.in.cybersource.com/notification-subscriptions/v2/webhooks?organizationId=`*{organization.id}*

Required Query Parameters for Retrieving All of an Organization's Subscriptions {#wh-fg-subscription-manage-get-list-req-fields}
================================================================================================================================

eventType
:
Set to an event type. For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

organizationId
:
Set to your organization ID or merchant ID.

productId
:
Set to a product ID. For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

Optional Query Parameters for Retrieving All of an Organization's Subscriptions {#wh-fg-subscription-manage-get-list-opt-fields}
================================================================================================================================

eventType
:
Set to an event type that corresponds to the chosen product ID. For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

productId
:
Set to a product ID. For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

Example: Retrieving All of an Organization's Subscriptions {#wh-fg-subscription-manage-get-list-ex}
===================================================================================================

```keyword
GET https://apitest.cybersource.com/notification-subscriptions/v2/webhooks?organizationId=organization123&productId=tokenManagement&eventType=tms.networktoken.provisioned
```

Response Codes {#wh-fg-subscription-manage-get-list-reply-status}
=================================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

**REST Interactive Example: Retrieving all of an Organization's Subscriptions** {#wh-fg-subscription-manage-get-list-dev-ex}
============================================================================================================================

Click this image to access the interactive code example for retrieving an organization's subscription using the product and event.

#### Figure:

Retrieve an Organization's Subscriptions Using the Product and Event [![Image and link to the interactive code example for retrieving an
organization's subscription using the product and event.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-get-list.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_get-details-on-all-created-webhooks "")

Update a Webhook Subscription {#wh-fg-subscription-manage-patch-intro}
======================================================================

This section describes how to update a webhook subscription, such as updating the notification scope, health check URL, or retry policy. Include only the fields that you want to update in your request.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints
---------

Send a PATCH request to one of these endpoints. The *`{webhookId}`* is the webhook subscription ID.

* **Test:** `PATCH ``apitest.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **Production:** `PATCH ``api.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **India Production:** `PATCH https://api.in.cybersource.com/notification-subscriptions/v2/webhooks/`*{webhookId}*

Optional Fields for Updating a Webhook Subscription {#wh-fg-subscription-manage-patch-opt-fields}
=================================================================================================

deactivateflag
:
Required if the healthCheckUrl field is present.
:
Set to `true` to automatically activate the subscription.

description
:

healthCheckUrl
:
Set to the health check URL. Required in order to auto-activate the subscription. If you do not include this field, the created subscription is inactive. An inactive subscription does not send notifications. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

name
:

organizationId
:
Set to your organization ID or merchant ID.

products.eventTypes
:
For a list of event types, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

products.productId
:
For a list of product IDs, see [Supported Products and Event Types](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-intro/wh-fg-product-event-types.md "").

retryPolicy.deactivateFlag
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.firstRetry
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.interval
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.numberOfRetries
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceCount
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

retryPolicy.repeatSequenceWaitTime
:
For more information, see [Configure the Retry Policy](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-optional-retry.md "").

securityPolicy.config.additionalConfig.aud
:

securityPolicy.config.additionalConfig.client_id
:

securityPolicy.config.additionalConfig.keyId
:

securityPolicy.config.additionalConfig.scope
:

securityPolicy.config.oAuthUrl
:

webhookUrl
:

Example: Updating a Webhook Subscription {#wh-fg-subscription-manage-patch-ex}
==============================================================================

```
{
  "name": "My Sample Webhook",
  "description": "Sample decision manager webhook reject event.",
  "products": [
    {
      "productId": "decisionManager",
      "eventTypes": [
        "risk.profile.decision.reject"
      ]
    }
  ],
  "webhookUrl": "https://MyWebhookServer.com:8443:/simulateClient",
  "healthCheckUrl": "https://MyWebhookServer.com:8443:/simulateClientHealthCheck",
  "notificationScope": {
    "scope": "CUSTOM"
  }
}
```

Response Codes {#wh-fg-subscription-manage-patch-reply-status}
==============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

**REST Interactive Example: Updating a Webhook Subscription** {#wh-fg-subscription-manage-patch-dev-ex}
=======================================================================================================

Click this image to access the interactive code example for updating a webhook subscription.

#### Figure:

Updating a Webhook Subscription [![Image and link to the interactive code example for updating a
webhook subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-patch.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_update-a-webhook-subscription "")

Delete a Webhook Subscription {#wh-fg-subscription-manage-delete-intro}
=======================================================================

This section describes how to delete a webhook subscription. Deleting a webhook subscription does not delete the history of webhook notifications.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints
---------

Send a DELETE request to one of these endpoints. The *`{webhookId}`* is the webhook subscription ID.

* **Test:** `DELETE ``apitest.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **Production:** `DELETE ``api.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*
* **India Production:** `DELETE https://api.in.cybersource.com/notification-subscriptions/v2/webhooks/`*{webhookId}*

Example: Deleting a Webhook Subscription {#wh-fg-subscription-manage-delete-ex}
===============================================================================

```keyword
DELETE https://apitest.cybersource.com/notification-subscriptions/v2/webhooks/b555a545-58a9-47c7-aef9-10a8e17f201a
```

```
{
    "status": "successfully deleted"
}
```

Response Codes {#wh-fg-subscription-manage-delete-reply-status}
===============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Interactive Example: Deleting a Webhook Subscription {#wh-fg-subscription-manage-delete-dev-ex}
====================================================================================================

Click this image to access the interactive code example for deleting a webhook subscription.

#### Figure:

Deleting a Webhook Subscription [![Image and link to the interactive code example for deleting a
webhook subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-delete.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_delete-a-webhook-subscription "")

Verify a Webhook Subscription's Configuration {#wh-fg-subscription-manage-test-intro}
=====================================================================================

This section describes how to test if a webhook subscription is configured correctly. Use this request to verify that the details you are expecting in the webhook notification are included, such as the notification message and the product and event types.  
A successful response includes the expected notification message and the product and event type. Only the first event type in your subscription is listed in the eventType response field.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints
---------

Send a POST request to one of these endpoints. The *`{webhookId}`* is the webhook subscription ID.

> IMPORTANT
> This endpoint uses the ` /v1/ ` path segment.

* **Test:** `POST ``apitest.cybersource.com``/notification-subscriptions/v1/webhooks/`*{webhookId}*
* **Production:** `POST ``api.cybersource.com``/notification-subscriptions/v1/webhooks/`*{webhookId}*
* **India Production:** `POST https://api.in.cybersource.com/notification-subscriptions/v1/webhooks/`*{webhookId}*

Example: Verifying a Webhook Subscription's Configuration {#wh-fg-subscription-manage-test-ex}
==============================================================================================

Request

```keyword
POST https://apitest.cybersource.com/notification-subscriptions/v1/webhooks/17915c64-73d9-5475-e063-7cb8d30a8089
```

Response to a Successful Request

```
{
   "eventDate": "2024-05-08T16:15:23",
    "eventType": "tms.networktoken.updated",
    "organizationId": "npr_gpn",
    "payloads": {
        "testPayload": {
            "message": "Yay! Your webhook integration worked! This is only a test and an example of what a webhook message payload looks like. Thank you for using our test feature."
        }
    },
    "productId": "tokenManagement",
    "requestType": "NEW",
    "retryNumber": "0",
    "transactionTraceId": "ddd8883c-f14d-48af-bd35-ff9b4a51ca35",
    "webhookId": "17915c64-73d9-5475-e063-7cb8d30a8089"
}
```

Response Codes {#wh-fg-subscription-manage-test-reply-status}
=============================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Interactive Example: Verifying a Webhook Subscription's Configuration {#wh-fg-subscription-manage-test-dev-ex}
===================================================================================================================

Click this image to access the interactive code example for testing a webhook subscription configuration.

#### Figure:

Testing a Webhook Subscription Configuration [![Image and link to the interactive code example for testing a
webhook subscription configuration.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-test.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_test-a-webhook-configuration "")

Activate a Webhook Subscription {#wh-fg-subscription-manage-activate-intro}
===========================================================================

This section describes how to activate a webhook subscription.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints {#wh-fg-subscription-manage-activate-intro_endpoint-status}
---------------------------------------------------------------------

Send a PUT request to one of these endpoints. The *`{webhookId}`* is the webhook subscription ID.

* **Test:** `PUT ``apitest.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`
* **Production:** `PUT ``api.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`
* **India Production:** `PUT https://api.in.cybersource.com/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`

Example: Activate a Webhook Subscription {#wh-fg-subscription-manage-activate-ex}
=================================================================================

Request

```keyword
PUT https://apitest.cybersource.com/notification-subscriptions/v2/webhooks/ddb9bced-c3e3-1b1d-e053-9c588e0a3c42
```

Response to a Successful Request

```
{
  "status": "ACTIVE"
}
```

Response Codes {#wh-fg-subscription-manage-activate-reply-status}
=================================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Interactive Example: Activating a Webhook Subscription {#wh-fg-subscription-manage-activate-dev-ex}
========================================================================================================

Click this image to access the interactive code example for activating a webhook subscription.

#### Figure:

Activating a Webhook Subscription [![Image and link to the interactive code example for activating a
webhook subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-status.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_update-a-webhook-status "")

Deactivate a Webhook Subscription {#wh-fg-subscription-manage-deactivate-intro}
===============================================================================

This section describes how to deactivate a webhook subscription.  
This request requires the webhook subscription ID. The subscription ID is in the webhookId response field from the *create a webhook subscription* request.

Endpoints
---------

Send a PUT request to one of these endpoints. The *`{webhookId}`* is the webhook subscription ID.

* **Test:** `PUT ``apitest.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`
* **Production:** `PUT ``api.cybersource.com``/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`
* **India Production:** `PUT https://api.in.cybersource.com/notification-subscriptions/v2/webhooks/`*{webhookId}*`/status`

Example: Deactivate a Webhook Subscription {#wh-fg-subscription-manage-deactivate-ex}
=====================================================================================

Request

```keyword
PUT https://apitest.cybersource.com/notification-subscriptions/v2/webhooks/ddb9bced-c3e3-1b1d-e053-9c588e0a3c42
```

Response to a Successful Request

```
{
  "status": "INACTIVE"
}
```

Response Codes {#wh-fg-subscription-manage-deactivate-reply-status}
===================================================================

A successful request is indicated by the 200-level response code. For more information about all of the possible response codes you can receive, see [Transaction Response Codes](https://developer.cybersource.com/api/reference/response-codes.md "").

REST Interactive Example: Deactivating a Webhook Subscription {#wh-fg-subscription-manage-deactivate-dev-ex}
============================================================================================================

Click this image to access the interactive code example for deactivating a webhook subscription.

#### Figure:

Deactivating a Webhook Subscription [![Image and link to the interactive code example for deactivating a
webhook subscription.](/content/dam/documentation/cybs/en-us/topics/payments-processing/payment-services/webhooks/images/dev-ex-status.png/jcr:content/renditions/original)](https://developer.cybersource.com/api-reference-assets/index.md?stage=pilot#webhooks_manage-webhooks_update-a-webhook-status "")

Troubleshooting Webhook Subscriptions {#wh-fg-subscription-troubleshooting}
===========================================================================

If you created a webhook subscription but are not receiving notifications, consider the following:

* Verify that the digital signature key you created includes the correct organization ID. You can verify the organization ID by locating it in the response for creating the digital signature key. If the key is configured with the wrong organization ID, send a request for a new digital signature key using the correct organization ID.
* Verify that your server and the endpoint URL for the webhook are working and are configured correctly.
* Verify that the notification scope of the subscription is configured to send notifications to the correct organization. You can retrieve the webhook details to verify that the organization is listed in the organizationId response field. For more information, see [Retrieve the Details of a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro/wh-fg-subscription-manage-get-intro.md ""). If the organization is not in the notification scope, you must update the webhook subscription. For more information, see [Update a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro/wh-fg-subscription-manage-patch-intro.md "").
* Verify that the subscription status is `ACTIVE`. You can do this by retrieving the webhook details. For more information, see [Retrieve the Details of a Webhook Subscription](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-subscription-manage-intro/wh-fg-subscription-manage-get-intro.md ""). If the webhook is not set to the `ACTIVE` status:
  * Verify that your subscription is configured with a health check URL. If it is not, update the subscription with a correct URL. You must also verify that the URL is working and is configured to accept GET and POST requests. For more information, see [Webhook Health Check URL and Automatic Revalidation](/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks/wh-fg-optional-intro/wh-fg-subscription-health-check-url.md "").

  * Verify that the webhook URL and health check URL contain hypertext transfer protocol secure (HTTPS). For example:

    ```
    "webhookUrl": "https://MyWebhookServer.com:443/simulateClient"
    "healthCheckUrl": "https://MyWebhookServer.com:443/simulateClientHealthCheck"
    ```

Step 2B: Test Your Shared Secret Key Pair {#restgs-security-key-pair-test-task}
===============================================================================

After creating your key certificate, you must verify that your key can successfully process API requests. Follow these steps to validate your key certificate in the Developer Center and the `Business Center`.

1. Go to the Developer Center's API Reference page:  
   [https://developer.cybersource.com/api-reference-assets/index.html#payments_payments_static-home-section](https://developer.cybersource.com/api-reference-assets/index.md#payments_payments_static-home-section "")
2. On the left navigation panel, click **[API Endpoints \& Authentication](https://developer.cybersource.com/api-reference-assets/index.md#static-api-endpoints-section "")** .
3. Under Authentication and Sandbox Credentials, go to the Authentication Type drop-down menu and choose **HTTP Signature**.
4. Enter your organization ID in the **Organization ID** field.
5. Enter your key, also known as your private key, in the **Key** field.
6. Enter your secret key, also known as your public key, in the **Shared Secret Key** field.
7. Click **Update Credentials**.  
   ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-http.png/jcr:content/renditions/original)
8. Go to the Developer Center's API Reference and navigate to **Payments \&gt; `POST` Process a Payment**.
9. Click **Send**.  
   ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/restgs-dev-center-ex.png/jcr:content/renditions/original)  
   A message confirms that your request was successful with the status code 201.  
   ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/rstgs-success-201.png/jcr:content/renditions/original)
10. Log in to the `Business Center`:  
    [`https://businesscentertest.cybersource.com`](https://ebc2test.cybersource.com/ebc2/ "")
11. On the left navigation panel, choose ![](/content/dam/documentation/cybs/en-us/common/images/ebc/ebc-icon-trxn-mgmt.svg/jcr:content/renditions/original) **Transaction Management \&gt; Transactions**.
12. Under Search Results, verify that the request ID from the test authorization response is listed in the Request ID column.  
    If the test authorization was successful, a success message is present in the corresponding Applications column.  
    ![](/content/dam/documentation/cybs/en-us/topics/platform/rest/getting-started/images/restgs-verify-key-pair.png/jcr:content/renditions/original)

