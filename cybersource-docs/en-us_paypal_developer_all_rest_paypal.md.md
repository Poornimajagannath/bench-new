PayPal and Venmo Developer Guide {#paypal-about-guide}
======================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for application developers who want to integrate PayPal, Pay Later, and Venmo into their order management system.

Convention
:
This statement appears in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.visaacceptance.com>

Recent Revisions to This Document {#paypal-revisions}
=====================================================

25.11.01
--------

This is the first General Availability release of this guide.

25.05.01
--------

Add a new section for creating a Venmo order. See [Create a Venmo Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-create-order-venmo-intro.md "").  
Updated the payment workflows to distinguish the differences between PayPal and Venmo. See [Authorizing and Capturing a Payment Workflow](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-intro-overview/paypal-intro-flow-auth.md "") and [Processing a Sale Workflow](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-intro-overview/paypal-intro-flow-sale.md "").

25.01.01
--------

Pilot release.

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Visa Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Visa Platform Connect ACQUIRER.

Introduction to PayPal and Venmo {#paypal-intro}
================================================

PayPal and Venmo are two payment methods that you can offer your customers through Cybersource. When your customers check out on your website, they can choose to pay with PayPal or Venmo, and then use their PayPal or Venmo account to complete the purchase. PayPal also offers installant payments known as PayPal Pay Later.

Benefits
--------

Integrating PayPal or Venmo into your system gives you and your customers these payment options.

**PayPal**
:
PayPal is a secure and convenient payment service. Your customers can make payments without directly using their bank accounts or credit cards.

**Venmo (US only)**
:
Venmo is a mobile payment service owned by PayPal that enables your customers to make payments from their Venmo mobile app. Customers link their Venmo accounts to their bank accounts, debit cards, and credit cards to send and receive payments.

    > IMPORTANT  
    > Venmo requires that you integrate a JavaScript SDK into your checkout experience.  
    > For more information about how to integrate the SDK into your website, see the Pay with Venmo integration section and the JavaScript SDK reference section on the PayPal developer website:
    >
    > * **Pay with Venmo integration:** ` `<https://developer.paypal.com/docs/checkout/pay-with-venmo/integrate/#link-Pay%20with%20Venmo%20integration>` `
    > * **JavaScript SDK reference:** [` https://developer.paypal.com/sdk/js/reference/ `](https://developer.paypal.com/sdk/js/reference/ "")

**PayPal Pay Later**
:
With PayPal, customers can pay in installments, but merchants receive full payment immediately.

    * **Pay in 3:** Customer pays in three installments. Available in the UK.
    * **Pay in 4:** Customers pay in four installments. Available in the US.
    * **Pay Monthly:** Customers pay in monthly recurring installments.

Getting Started with REST
-------------------------

To begin processing payments through `Cybersource`, you must first set up your payment processing system to be REST compliant. `Cybersource` uses the REST architecture for developing web services. REST enables communication between a client and server using HTTP protocols.  
If you have not set up secure communications between your client and server using either a **JSON Web Token** or **HTTP signature** , see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Set Up Merchant Accounts {#paypal-intro-setup}
==============================================

Before you can process payments with PayPal, you must acquire PayPal merchant credentials. Complete these steps to obtain the credentials and to link your PayPal merchant account with your `Cybersource` merchant account:
1. Set up a PayPal business or premier account:  
   <https://www.paypal.com/us/business>
2. Set up a PayPal developer sandbox account.
   3. Create your PayPal credentials by creating a PayPal app as directed on the PayPal developer website:  
      <https://developer.paypal.com/api/rest/#get-credentials>
3. Save the sandbox account facilitator email address, the client ID, and the secret key for future reference.  
   For example:
   * Sandbox account facilitator email address:  
     `merchantuser-facilitator@merchant.com`
   * Client ID:  
     `AahnQzKLL2vvG_UI6YQy9xcyt5joMLVoPHW-1Bv8gCvPkTiNwQSRCvKIKXy8UZZguijbwJTTs_Cjhdz`
   * Secret key:  
     `EOE3eqqeIBy4q8LhsON0-wp2zPb_0SOqPH3sopx_uwuIMkCug7zw3aKDunstrXmcrGecmpeUJgsqTGO`
4. Contact `Cybersource` merchant support and provide your PayPal credentials:
   * Sandbox account facilitator email address
   * Client ID

* Secret key  
  When your account is set up, you can begin processing PayPal or Venmo payments.

Overview of Processing PayPal Transactions {#paypal-intro-overview}
===================================================================

PayPal requires you to create an order before processing a payment. After creating an order, you can process the payment using the authorization and capture API requests, or the sale API request. This section describes the steps required in order to create and manage orders and to process transactions.

Requests and Endpoints
----------------------

These are the requests you can send to `Cybersource` to process PayPal transactions and their corresponding endpoints.

|               Request                |                                                                                                                        Endpoint                                                                                                                         |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create an Order                      | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/intents`{#paypal-intro-overview_d7e559} * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/intents`                                                                            |
| Update an Order                      | * **Production:** `PATCH ``https://api.cybersource.com``/pts/v2/intents/`*{id}*{#paypal-intro-overview_d7e585} * **Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/intents/`*{id}*                                                            |
| Save an Order                        | * **Production:** `PATCH ``https://api.cybersource.com``/pts/v2/intents/`*{id}*{#paypal-intro-overview_d7e622} * **Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/intents/`*{id}*                                                            |
| Void an Order                        | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#paypal-intro-overview_d7e450} * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#paypal-intro-overview_d7e463}             |
| Authorize and Re-authorize a Payment | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/` * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`                                                                                                       |
| Reverse an Authorization             | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals` * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`                                                                   |
| Capture a Payment                    | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures` * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`                                                                     |
| Process a Sale                       | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#paypal-intro-overview_d7e345} * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#paypal-intro-overview_d7e355}                                           |
| Refund a Payment                     | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#paypal-intro-overview_d7e372} * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#paypal-intro-overview_d7e385}         |
| Check Status                         | * **Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-intro-overview_d7e193} * **Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-intro-overview_d7e205} |
[Requests and Endpoints]

Authorizing and Capturing a Payment Workflow {#paypal-intro-flow-auth}
======================================================================

This workflow illustrates a successful authorization and capture.

#### Figure:

Authorization and Capture Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-capture.svg/jcr:content/renditions/original)
1. The customer begins to check out on the merchant's website and chooses one of these payment methods:
   * PayPal
   * PayPal Pay Later
   * Venmo
2. You request a create order and sets the processingInformation.authorizationOptions.authType request field to `AUTHORIZE`. For more information, see [Create a PayPal Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-create-order-intro.md "").
3. `Cybersource` responds with this information in the response message:
   * `PAYER_ACTION_REQUIRED` status
   * PayPal checkout redirect URL or a Venmo checkout QR code
   * Order ID
   * Order request ID
4. You redirect the customer to the PayPal checkout URL or display the Venmo QR code. The Venmo QR code is generated by setting the transaction ID in the Venmo Java SDK.
5. The customer uses their PayPal or Venmo account to complete the payment and is redirected to the merchant's checkout page.
6. You request a check status with the order transaction ID. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").
7. `Cybersource` responds with an `APPROVED` status.
8. You display the order confirmation to the customer.
9. You request an authorization with the order ID. For more information, see [Authorize a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-auth-intro.md "").
10. `Cybersource` responds with the `COMPLETED` status and authorization request ID.  
    If you or the customer modify the purchase details before the authorized funds are captured, you must provide the updated payment information to Cybersource using one of these requests:
    * PayPal: You send a re-authorization request. For more information, see [Re-authorize a PayPal Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-reauth-intro.md "").
    * Venmo: You send an update order request. For more information, see [Update an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-update-order-intro.md "").
11. You request a capture with the authorization request ID. For more information, see [Capture a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-capture-intro.md "").
12. `Cybersource` responds with the `PENDING` status and a capture request ID.
13. You request a check status with the capture request ID. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").
14. `Cybersource` responds with a `COMPLETED` status.
15. You display the payment confirmation to the customer.

Processing a Sale Workflow {#paypal-intro-flow-sale}
====================================================

This workflow describes the sequence of events that comprises processing a successful payment using the sale request.

#### Figure:

Sale Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-sale.svg/jcr:content/renditions/original)

1. The customer begins to check out on the merchant's website and chooses one of these payment methods:
   * PayPal
   * PayPal Pay Later
   * Venmo
     {#paypal-intro-flow-sale_step-1}
     {#paypal-intro-flow-sale_step-1}
2. You send a create order API request to `Cybersource` and set the processingInformation.authorizationOptions.authType request field to `CAPTURE`. For more information, see [Create a PayPal Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-create-order-intro.md "").{#paypal-intro-flow-sale_step-2}
   {#paypal-intro-flow-sale_step-2}
3. `Cybersource` responds with this information in the response message:
   * `PAYER_ACTION_REQUIRED` status
   * PayPal checkout redirect URL or a Venmo checkout QR code
   * Order ID
   * Order request ID
     {#paypal-intro-flow-sale_step-3}
     {#paypal-intro-flow-sale_step-3}
4. You redirect the customer to the PayPal checkout URL or display the Venmo QR code. The Venmo QR code is generated by setting the transaction ID in the Venmo Java SDK.{#paypal-intro-flow-sale_step-4}
   {#paypal-intro-flow-sale_step-4}
5. The customer uses their PayPal or Venmo account to complete the payment and is redirected to the merchant's checkout page.{#paypal-intro-flow-sale_step-5}
   {#paypal-intro-flow-sale_step-5}
6. You request a check status with the order transaction ID. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").{#paypal-intro-flow-sale_step-6}
   {#paypal-intro-flow-sale_step-6}
7. `Cybersource` responds with an `APPROVED` status.{#paypal-intro-flow-sale_step-7}
   {#paypal-intro-flow-sale_step-7}
8. You display the order confirmation to the customer.{#paypal-intro-flow-sale_step-8}
   {#paypal-intro-flow-sale_step-8}
9. You request a sale with the order ID. For more information, see [Process a Sale](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-sale-intro.md "").
10. `Cybersource` responds with a `PENDING` status and a sale request ID.
11. You request a check status with the sale request ID. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").
12. `Cybersource` responds with a `COMPLETED` status.
13. You display a payment confirmation to the customer.

Refunding a Payment Workflow {#paypal-intro-flow-refund}
========================================================

This workflow illustrates the process of issuing a refund.

#### Figure:

Refund Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-refund.svg/jcr:content/renditions/original)

1. The customer returns a purchase to the merchant.
2. You request a refund and includes the capture request ID or sale request ID. For more information, see [Refund a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-refund-intro.md "").
3. `Cybersource` responds with a `PENDING` status and a refund request ID.
4. You request a check status with the refund request ID. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").
5. `Cybersource` responds with a `REFUNDED` status.
6. You display a refund confirmation to the customer.

Creating and Updating an Order Workflow {#paypal-intro-flow-order-update}
=========================================================================

This workflow illustrates the process of creating and updating an order.

#### Figure:

Creating and Updating an Order Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-order-update.svg/jcr:content/renditions/original)
1. The customer begins to check out on the merchant's website and chooses one of these payment methods:
   * PayPal
   * PayPal Pay Later
   * Venmo
2. You request a create order. For more information, see [Create a PayPal Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-create-order-intro.md "").
3. `Cybersource` responds with this information in the response message:
   * `PAYER_ACTION_REQUIRED` status
   * PayPal checkout redirect URL or a Venmo checkout QR code
   * Order ID
   * Order request ID
4. You redirect the customer to the PayPal checkout URL or display the Venmo QR code. The Venmo QR code is generated by setting the transaction ID in the Venmo Java SDK.
5. The customer uses their PayPal or Venmo account to complete the payment and is redirected to the merchant's checkout page.
   6. The customer or merchant decides to change order information, such as the payment amount.

   > IMPORTANT You cannot update an order after an authorization or sale is complete.

6. You request an update order. For more information, see [Update an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-update-order-intro.md "").
7. `Cybersource` responds with a `COMPLETED` status.
8. The merchant can send a follow-on request discussed in one of these topics:
   * [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "")
   * [Authorize a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-auth-intro.md "")

* [Process a Sale](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-sale-intro.md "")

Saving and Voiding an Order Workflow {#paypal-intro-flow-order-save}
====================================================================

This workflow illustrates the process of saving and then voiding an order. Voiding an order is optional.

#### Figure:

Save and Void an Order Workflow  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-order-save.svg/jcr:content/renditions/original)
1. The customer begins to check out on the merchant's website and chooses one of these payment methods:
   * PayPal
   * PayPal Pay Later
   * Venmo
2. You request a create order. For more information, see [Create a PayPal Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-create-order-intro.md "").
3. `Cybersource` responds with this information in the response message:
   * `PAYER_ACTION_REQUIRED` status
   * PayPal checkout redirect URL or a Venmo checkout QR code
   * Order ID
   * Order request ID
4. You redirect the customer to the PayPal checkout URL or display the Venmo QR code. The Venmo QR code is generated by setting the transaction ID in the Venmo Java SDK.
5. The customer uses their PayPal or Venmo account to complete the payment and is redirected to the merchant's checkout page.
6. The customer gives the merchant consent to save the customer's payment credentials in the order.
7. You send a save order API request with the order ID to Cybersource. For more information, see [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "").
8. `Cybersource` responds with a `COMPLETED` status.
9. You can now authorize the order as many times as needed until the payment is captured.
10. (Optional) The customer or merchant decides to delete the saved order with their payment credentials.
11. You send a void order API request to `Cybersource`. For more information, see [Void an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-void-order-intro.md "").
12. `Cybersource` responds with the `VOIDED` status.
13. You display a confirmation that the order and the customer's payment credentials are no longer saved on the merchant's website.

Order Management Statuses Workflow {#paypal-intro-flow-order-status}
====================================================================

This workflow shows the statuses that can occur at each stage of creating and managing an order.  
You can send a check status request after every request in this workflow to verify the status response.

#### Figure:

Order Management Statuses  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-status-order-650x625.svg/jcr:content/renditions/original)

1. You request a create order and receive one of these possible statuses:

* `PAYER_ACTION_REQUIRE`: The request was successful, and you must redirect the customer to the PayPal checkout URL in order for the customer to approve the payment.{#paypal-intro-flow-order-status_d10e29}
  {#paypal-intro-flow-order-status_d10e29}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-intro-flow-order-status_d10e34}
  {#paypal-intro-flow-order-status_d10e34}

2. If the customer changes their purchase, you request an update order and receive one of these possible statuses:

* `COMPLETED`: The request was successful and the order information is updated.{#paypal-intro-flow-order-status_d29e29}
  {#paypal-intro-flow-order-status_d29e29}
* `INVALID_REQUEST`: The request was not successful. Send a new update order request.{#paypal-intro-flow-order-status_d29e34}
  {#paypal-intro-flow-order-status_d29e34}

3. If the customer consents to future purchases on PayPal or Venmo checkout page, you request a save order and receive one of these possible statuses:

* `COMPLETED`: The request was successful and the customer's payment information from the order is saved for future transactions.{#paypal-intro-flow-order-status_d30e29}
  {#paypal-intro-flow-order-status_d30e29}
* `INVALID_REQUEST`: The request was not successful. Send a new save order request.{#paypal-intro-flow-order-status_d30e34}
  {#paypal-intro-flow-order-status_d30e34}

4. If the customer notifies you to delete the customer's saved payment credentials, you request a void order and receive one of these possible statuses:

* `VOIDED`: The request was successful and the customer's payment credentials are no longer saved.{#paypal-intro-flow-order-status_d31e29}
  {#paypal-intro-flow-order-status_d31e29}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-intro-flow-order-status_d31e34}
  {#paypal-intro-flow-order-status_d31e34}

Response Statuses for Authorizing a Payment Workflow {#paypal-intro-flow-auth-status}
=====================================================================================

This workflow shows the statuses that can occur at each stage of the payment process.

#### Figure:

Authorization Payment Statuses  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-status-auth.svg/jcr:content/renditions/original)

1. You request a create order and receive one of these possible statuses:

* `PAYER_ACTION_REQUIRE`: The request was successful, and you must redirect the customer to the PayPal checkout URL in order for the customer to approve the payment.{#paypal-intro-flow-auth-status_d10e29}
  {#paypal-intro-flow-auth-status_d10e29}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-intro-flow-auth-status_d10e34}
  {#paypal-intro-flow-auth-status_d10e34} {#paypal-intro-flow-auth-status_step-create-order}
  {#paypal-intro-flow-auth-status_step-create-order}

2. You request a check status for the created order and receive one of these possible statuses:
   * `COMPLETED`: The order was approved by the customer. This status can also occur when the order is successfully used for an authorization or sale.
   * `INVALID_REQUEST`: The request was not successful. Send a new request.
     {#paypal-intro-flow-auth-status_step-check-status-order}
     {#paypal-intro-flow-auth-status_step-check-status-order}
3. You request an authorization and receive one of these possible statuses:
   * `COMPLETED`: The authorized funds were successfully captured.
   * `INVALID_REQUEST`: The authorization request was not successful. Send a new authorization request.
   * `PENDING`: The authorization request was successful, and PayPal is reviewing the request. Use the check status request as often as necessary until the status updates.
   4. If you or the customer decide to cancel the payment, you request an authorization reversal and receive one of these possible statuses:
   * `REVERSED`: The reversal request was successful, and the authorized funds are released from hold.
   * `INVALID_REQUEST`: The reversal request was not successful. Send a new reversal request.
4. You request a capture and receive one of these possible statuses:
   * `COMPLETED`: The funds were successfully captured, and the payment is complete.
   * `DECLINED`: The funds were not captured because PayPal declined the request after a review.
   * `INVALID_REQUEST`: The capture request was not successful. Send a new capture request.
   * `PENDING`: The capture request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").
5. If the customer returns a purchase, you request a refund and receive one of these possible statuses:
   * `PENDING`: The refund request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.
   * `REFUNDED`: The captured funds were successfully refunded to the customer's account. This status can also occur during a customer dispute, such as a chargeback or reversal.
   * `INVALID_REQUEST`: The refund request was not successful. Send a new refund request.
     {#paypal-intro-flow-auth-status_step-refund}
     {#paypal-intro-flow-auth-status_step-refund}

Response Statuses for a Sale Workflow {#paypal-intro-flow-sale-status}
======================================================================

This workflow shows the statuses that can occur at each stage of the payment process.

#### Figure:

Sale Payment Statuses  
![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/altpay/paypal/images/paypal-flow-status-sale.svg/jcr:content/renditions/original)

1. You request a create order and receive one of these possible statuses:

* `PAYER_ACTION_REQUIRE`: The request was successful, and you must redirect the customer to the PayPal checkout URL in order for the customer to approve the payment.{#paypal-intro-flow-sale-status_d10e29}
  {#paypal-intro-flow-sale-status_d10e29}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-intro-flow-sale-status_d10e34}
  {#paypal-intro-flow-sale-status_d10e34}

2. You request a check status for the created order and receive one of these possible statuses:
   * `COMPLETED`: The order was approved by the customer. This status can also occur when the order is successfully used for an authorization or sale.
   * `INVALID_REQUEST`: The request was not successful. Send a new request.
3. You request a sale to `Cybersource` and receive one of these possible statuses:
   * `COMPLETED`: The sale successfully processed, and the payment is complete.
   * `DECLINED`: The sale request is declined. Send a new sale request.
   * `INVALID_REQUEST`: The sale request is not successful. Send a new sale request.
   * `PENDING`: The sale request is successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.
4. If the customer returns a purchase, you request a refund and receive one of these possible statuses:
   * `PENDING`: The refund request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.
   * `REFUNDED`: The captured funds were successfully refunded to the customer's account. This status can also occur during a customer dispute, such as a chargeback or reversal.

* `INVALID_REQUEST`: The refund request was not successful. Send a new refund request.

Order Management Requests {#paypal-services-order}
==================================================

This section describes how to manage orders using the `REST API`.

Create a PayPal Order {#paypal-create-order-intro}
==================================================

This section describes how to create a *PayPal* order.  
You must send a create order request to begin processing a new payment. Creating an order enables the customer to complete checkout using their PayPal account.

**Itemization**
:
Every unique item being purchased must be itemized in the request as a line item. For more information about how to format line items in a request, see [Including Line Items in Requests](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-ref-info/paypal-create-order-line-items.md "").

Payment Processing Type
:
You must also set the processingInformation.authorizationOptions.authType request field to `AUTHORIZE` or `CAPTURE` to indicate which follow-on requests you will send to process the payment. Set the field value to `AUTHORIZE` if you want to process the payment using the authorization and capture requests. Set the field value to `CAPTURE` if you want to process the payment using the sale request.

Payment Method
:
To specify that the customer is paying with PayPal, set the paymentInformation.paymentType.method.name request field to `payPal`.

Saving Payment Credentials
:
You can save a customer's payment credentials in order to make future transactions fast and simple for the customer. To save the customer's credentials, you must include the optional processingInformation.processingInstruction request field and set its value to `ORDER_SAVED_EXPLICITLY`. After you successfully create the order and the customer completes the checkout, you must send a follow-on save payment credentials request. For more information, see [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "").  
A successful request is indicated by a PayPal redirect URL in the processorInformation.paymentUrl response field and a request ID in the id response field. Redirect the customer to the PayPal URL where they can log in to their PayPal account to approve and complete the payment. Save the request ID in your system for the follow-on API requests.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/intents`{#paypal-create-order-intro_d7e559}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/intents`

Requesting to Create a PayPal Order {#paypal-create-order-task}
===============================================================

Follow these steps to successfully create an order.

1. Send a `POST `request to the `https://api.cybersource.com``/v2/intents` endpoint and include these required fields:

   [buyerInformation.dateOfBirth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-date-of-birth.md "")
   :

   [buyerInformation.language](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-language.md "")
   :

   [buyerInformation.personalIdentification\[\].id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-personal-id-id.md "")
   :

   [buyerInformation.personalIdentification\[\].type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-personal-id-type-a.md "")
   :

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :

   [merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
   :

   [merchantInformation.returnUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-return-url.md "")
   :

   [merchantInformation.successUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-success-url.md "")
   :

   [orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
   :

   [orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
   :

   orderInformation.amountDetails.taxDetails.taxId
   :

   orderInformation.amountDetails.taxDetails.type
   :

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   [orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
   :

   [orderInformation.billTo.company.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-name.md "")
   :

   [orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
   :

   [orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
   :

   [orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
   :

   [orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
   :

   [orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
   :

   orderInformation.invoiceDetails.invoiceNumber
   :

   orderInformation.invoiceDetails.productDescription
   :

   [orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
   :

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
   :

   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
   :

   [orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
   :

   [orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   [orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
   :

   [orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
   :

   [orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
   :

   [orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
   :

   [orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
   :

   [orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
   :

   [orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
   :

   paymentInformation.customer.customerid
   :

   [paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
   :
   Set to `payPal`.
   {#paypal-create-order-task_rest-method-name}
   {#paypal-create-order-task_rest-method-name}

   [paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
   :
   Set to `eWallet`.

   [processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
   :
   Set to `AP_ORDER`.

   processingInformation.authorizationOptions.authType
   :
   Set to one of these values:

       * `AUTHORIZE`: The created order can be processed with an authorization and capture.
       * `CAPTURE`: The created order can be processed for a sale.

2. Include any optional fields in the request:

   [merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
   :

   orderInformation.invoiceDetails.productDescription
   :

   [orderInformation.lineItems\[\].productSKU](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
   :

   [orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
   :

   processingInformation.processingInstruction
   :
   Set to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

3. Redirect the customer to the received URL in the processorInformation.paymentUrl response field.

   ```
   "processorInformation": {
           "transactionId": "1CE47930A46117822",
           "paymentUrl": "https://www.sandbox.paypal.com/checkoutnow?token=1CE47930A46117822"
       }
   ```
4. When the customer completes checking out using their PayPal account, the customer is redirected to the URL you included in the merchantInformation.successUrl request field.

Example: Creating a PayPal Order {#paypal-create-order-ex-rest}
===============================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "123456"
    },
    "buyerInformation": {
        "language": "en",
        "personalIdentification": [
            {
                "id": "123",
                "type": "BR_CNPJ"
            }
        ],
        "dateOfBirth": "20210101"
    },
    "orderInformation": {
        "shipTo": {
            "country": "PL",
            "postalCode": "CV-1012",
            "locality": "San"
        },
        "billTo": {
            "firstName": "ab",
            "lastName": "c",
            "address1": "ABC city, XYZ street",
            "phoneNumber": "1234",
            "email": "test@enets.com",
            "locality": "San",
            "company": {
                "name": "abc"
            }
        },
        "amountDetails": {
            "totalAmount": "150",
            "currency": "USD",
            "taxAmount": "50",
            "taxDetails": {
                "taxId": "123456",
                "type": "BR_CPF"
            }
        },
        "invoiceDetails": {
            "invoiceNumber": "123",
            "productDescription": "1bc"
        },
        "lineItems": [
            {
                "productName": "test-product",
                "quantity": 5,
                "productDescription": "description-123",
                "unitPrice": "20",
                "taxAmount": "10",
                "totalAmount": "100",
                "typeOfSupply": "01"
            }
        ]
    },
    "merchantInformation": {
        "successUrl": "https://developer.paypal.com/home",
        "merchantDescriptor": {
            "name": "Demo-Merchant"
        },
        "returnUrl": "https://developer.paypal.com/home"
    },
    "paymentInformation": {
        "customer": {
            "customerid": "12345"
        },
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    },
    "processingInformation": {
        "authorizationOptions": {
            "authType": "AUTHORIZE"
        },
        "actionList": [
            "AP_ORDER"
        ]
    }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "transactionId": "1CE47930A46117822",
        "paymentUrl": "https://www.sandbox.paypal.com/checkoutnow?token=1CE47930A46117822"
    },
    "message": "Successful",
    "status": "PAYER_ACTION_REQUIRE",
    "id": "7259726679396017501991",
    "submitTimeUtc": "2024-09-10T12:51:08Z"
}
```

Response Statuses for Creating a PayPal Order {#paypal-create-order-resp-fields}
================================================================================

`Cybersource` responds to your request with one of these statuses in the status field:
* `PAYER_ACTION_REQUIRE`: The request was successful, and you must redirect the customer to the PayPal checkout URL in order for the customer to approve the payment.{#paypal-create-order-resp-fields_payer-action-req}
  {#paypal-create-order-resp-fields_payer-action-req}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-create-order-resp-fields_status-failed}
  {#paypal-create-order-resp-fields_status-failed} {#paypal-create-order-resp-fields_statuses-create-order}  
  When you request a status update, `Cybersource` responds with one of these statuses in the status field:
* `COMPLETED`: The order was approved by the customer. This status can also occur when the order is successfully used for an authorization or sale.{#paypal-create-order-resp-fields_status-4}
  {#paypal-create-order-resp-fields_status-4}

Follow-On Requests {#paypal-create-order-resp-fields_follow-on-req}
-------------------------------------------------------------------

After you create an order, you can send these follow-on API requests using the order ID from the response message.

Update Order
:
To update the order information, such as the payment amount or line items, send an update order request. For more information, see [Update an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-update-order-intro.md "").

Save Order
:
To save the customer's payment credentials in the order to make future check out experiences faster for the customer, send a save order request. For more information, see [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "").

Authorization
:
To authorize funds for a payment, send an authorization request. For more information, see [Authorize a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-auth-intro.md "").

Sale
:
To authorize and capture funds for a payment in the same request, send a sale request. For more information, see [Process a Sale](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-sale-intro.md "").

Create a Venmo Order {#concept}
===============================

This section describes how to create a *Venmo* order.  
You must send a create order request to begin processing a new payment. Creating an order enables the customer to complete checkout using their Venmo account.

**Itemization**
:
Every unique item being purchased must be itemized in the request as a line item. For more information about how to format line items in a request, see [Including Line Items in Requests](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-ref-info/paypal-create-order-line-items.md "").

Payment Processing Type
:
You must also set the processingInformation.authorizationOptions.authType request field to `AUTHORIZE` or `CAPTURE` to indicate which follow-on requests you will send to process the payment. Set the field value to `AUTHORIZE` if you want to process the payment using the authorization and capture requests. Set the field value to `CAPTURE` if you want to process the payment using the sale request.

Payment Method
:
To specify that the customer is paying with Venmo, set the paymentInformation.paymentType.method.name request field to `Venmo`.

Saving Payment Credentials
:
You can save a customer's payment credentials in order to make future transactions fast and simple for the customer. To save the customer's credentials, you must include the optional processingInformation.processingInstruction request field and set its value to `ORDER_SAVED_EXPLICITLY`. After you successfully create the order and the customer completes the checkout, you must send a follow-on save payment credentials request. For more information, see [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "").  
A successful request is indicated by a Venmo transaction ID in the processorInformation.transactionId response field and a request ID in the id response field. Your system should set the transaction ID in the SDK to automatically create a Venmo checkout button on your checkout webpage. When the customer clicks the Venmo button, a QR displays to the customer. Your customer uses their Venmo mobile app to scan the QR code and complete the checkout using their Venmo mobile app. Save the request ID in your system for the follow-on API requests.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/intents`{#concept_d7e559}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/intents`

Requesting to Create a Venmo Order {#paypal-create-order-venmo-task}
====================================================================

Follow these steps to successfully create an order.

1. Send a `POST `request to the `https://api.cybersource.com``/v2/intents` endpoint and include these required fields:

   [buyerInformation.dateOfBirth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-date-of-birth.md "")
   :

   [buyerInformation.language](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-language.md "")
   :

   [buyerInformation.personalIdentification\[\].id](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-personal-id-id.md "")
   :

   [buyerInformation.personalIdentification\[\].type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-personal-id-type-a.md "")
   :

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :

   [merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
   :

   [merchantInformation.returnUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-return-url.md "")
   :

   [merchantInformation.successUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-success-url.md "")
   :

   [orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
   :

   [orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
   :

   orderInformation.amountDetails.taxDetails.taxId
   :

   orderInformation.amountDetails.taxDetails.type
   :

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   [orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
   :

   [orderInformation.billTo.company.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-company-name.md "")
   :

   [orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
   :

   [orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
   :

   [orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
   :

   [orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
   :

   [orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-phone-num.md "")
   :

   orderInformation.invoiceDetails.invoiceNumber
   :

   orderInformation.invoiceDetails.productDescription
   :

   [orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
   :

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
   :

   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
   :

   [orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
   :

   [orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   [orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
   :

   [orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
   :

   [orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
   :

   [orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
   :

   [orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
   :

   [orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
   :

   [orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
   :

   paymentInformation.customer.customerid
   :

   [paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
   :
   Set to `venmo`.
   {#paypal-create-order-venmo-task_rest-method-name}
   {#paypal-create-order-venmo-task_rest-method-name}

   [paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
   :
   Set to `eWallet`.

   [processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
   :
   Set to `AP_ORDER`.

   processingInformation.authorizationOptions.authType
   :
   Set to one of these values:

       * `AUTHORIZE`: The created order can be processed with an authorization and capture.
       * `CAPTURE`: The created order can be processed for a sale.

2. Include any optional fields in the request:

   [merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
   :

   orderInformation.invoiceDetails.productDescription
   :

   [orderInformation.lineItems\[\].productSKU](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
   :

   [orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
   :

   processingInformation.processingInstruction
   :
   Set to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

3. After sending your request, your system sets the processorInformation.transactionId response field value in the Venmo SDK. The SDK creates a Venmo checkout button that the customer clicks to display a Venmo QR code. Your customer scans the QR code using their Venmo mobile app. When your customer approves the payment on their Venmo mobile app, the payment is complete.

Example: Creating a Venmo Order {#paypal-create-order-venmo-ex-rest}
====================================================================

Request

```

```

Response to a Successful Request

```

```

Response Statuses for Creating a Venmo Order {#x-req-fields}
============================================================

`Cybersource` responds to your request with one of these statuses in the status field:
* `PAYER_ACTION_REQUIRE`: The request was successful, and your system must create a Venmo checkout button using the Venmo SDK in order for the customer to approve the payment.{#x-req-fields_payer-action-req}
  {#x-req-fields_payer-action-req}
* `INVALID_REQUEST`: The request was not successful. Send a new request.
  {#x-req-fields_statuses-create-order}  
  When you request a status update, `Cybersource` responds with one of these statuses in the status field:
* `COMPLETED`: The order was approved by the customer. This status can also occur when the order is successfully used for an authorization or sale.{#x-req-fields_d10e54}
  {#x-req-fields_d10e54}

Follow-On Requests
------------------

After you create an order, you can send these follow-on API requests using the order ID from the response message.

Update Order
:
To update the order information, such as the payment amount or line items, send an update order request. For more information, see [Update an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-update-order-intro.md "").

Save Order
:
To save the customer's payment credentials in the order to make future check out experiences faster for the customer, send a save order request. For more information, see [Save an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-save-order-intro.md "").

Authorization
:
To authorize funds for a payment, send an authorization request. For more information, see [Authorize a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-auth-intro.md "").

Sale
:
To authorize and capture funds for a payment in the same request, send a sale request. For more information, see [Process a Sale](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-sale-intro.md "").

Update an Order {#paypal-update-order-intro}
============================================

You can update the information in an order, such as the payment details and line items, by requesting an update order. Updating an order is necessary when a customer decides to change their purchase, billing, or shipping information, and when inventory adjustments occur.  
Include all of the customer's information sent in the create order request in the update order request to ensure the order's accuracy. Only exclude fields that relate to information you are intentionally removing from an order.

> IMPORTANT You cannot update an order after an authorization or sale is complete.

Endpoints
---------

**Production:** `PATCH ``https://api.cybersource.com``/pts/v2/intents/`*{id}*{#paypal-update-order-intro_d7e585}  
**Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/intents/`*{id}*  
Set the *`{id}`* to the order ID contained in the create order response.

Required Fields for Updating an Order {#paypal-update-order-req-fields}
=======================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.discountAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
:

[orderInformation.amountDetails.dutyAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-duty-amount.md "")
:

orderInformation.amountDetails.insuranceAmount
:

orderInformation.amountDetails.shippingAmount
:

orderInformation.amountDetails.shippingDiscountAmount
:

[orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
:

orderInformation.amountDetails.taxDetails.taxId
:

orderInformation.amountDetails.taxDetails.type
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_UPDATE_ORDER`.

Optional Fields for Updating an Order {#paypal-update-order-opt-fields}
=======================================================================

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:

orderInformation.invoiceDetails.productDescription
:

[orderInformation.lineItems\[\].productSKU](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

Example: Updating an Order {#paypal-update-order-ex-rest}
=========================================================

Request

```
{
  "orderInformation": {
    "shipTo": {
      "country": "PL",
      "address1": "I",
      "address2": "I",
      "locality": "I",
      "administrativeArea": "I",
      "postalCode": "I"
    },
    "amountDetails": {
      "totalAmount": "65",
      "currency": "USD",
      "taxAmount": "20",
      "shippingAmount": "15",
      "dutyAmount": "5",
      "insuranceAmount": "15",
      "shippingDiscountAmount": "5",
      "discountAmount": "5",
      "taxDetails": {
        "taxId": "123456",
        "type": "BR_CPF"
      }
    },
    "lineItems": [
      {
        "productName": "test-product",
        "quantity": 1,
        "productDescription": "description-123",
        "unitPrice": "20",
        "taxAmount": "20",
        "totalAmount": "20",
        "typeOfSupply": "01"
      }
    ]
  },
  "processingInformation": {
    "actionList": [
      "AP_UPDATE_ORDER"
    ]
  },
  "paymentInformation": {
    "paymentType": {
      "method": {
        "name": "payPal"
      },
      "name": "eWallet"
    }
  }
}
```

Response to a Successful Request

```
{
  "message": "Successful",
  "status": "COMPLETED",
  "id": "7259607420486012601991",
  "submitTimeUtc": "2024-09-10T09:32:22Z"
}
```

Response Statuses for Updating an Order {#paypal-update-order-resp-fields}
==========================================================================

`Cybersource` responds to your request with one of these statuses in the status field:
* `COMPLETED`: The request was successful and the order information is updated.{#paypal-update-order-resp-fields_status-1}
  {#paypal-update-order-resp-fields_status-1}
* `INVALID_REQUEST`: The request was not successful. Send a new update order request.{#paypal-update-order-resp-fields_status-2}
  {#paypal-update-order-resp-fields_status-2} {#paypal-update-order-resp-fields_update-order-statuses}

Save an Order {#paypal-save-order-intro}
========================================

After the customer completes the purchase using the Paypal or Venmo redirect URL from the create order response, you can save the customer's order by requesting a save order. Saving a customer's order enables you to retain an order even after you have authorized the payment. This is necessary for situations where you must reverse the authorization but plan to authorize the same order again. When the order is authorized and captured, you can longer authorize the saved order.  
If you decide that you no longer need to retain a saved order, you can cancel the saved order by sending a void order request. For more information, see [Void an Order](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services-order/paypal-void-order-intro.md "").  
IMPORTANT The customer must give you consent to saving their payment credentials in an order before you save their information.

Prerequisite
:
Before sending the save order request, you must ensure that the create order request included the processingInformation.processingInstruction field set to the `ORDER_SAVED_EXPLICITLY` value.

Endpoints
---------

**Production:** `PATCH ``https://api.cybersource.com``/pts/v2/intents/`*{id}*{#paypal-save-order-intro_d7e622}  
**Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/intents/`*{id}*  
Set the *`{id}`* to the order ID contained in the create order response.

Required Fields for Saving an Order {#paypal-save-order-req-fields}
===================================================================

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_EXTENDED_ORDER`.

Example: Saving an Order {#paypal-save-order-ex-rest}
=====================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "method": {
        "name": "payPal"
      },
      "name": "eWallet"
    }
  },
  "processingInformation": {
    "actionList": [
      "AP_EXTEND_ORDER"
    ]
  }
}
```

Response to a Successful Request

```
{
  "processorInformation": {
    "networkTransactionId": "O-0PJ044907K025064E",
    "transactionId": "15280613LP005810C"
  },
  "message": "Successful",
  "status": "COMPLETED",
  "id": "7259829628396022101991",
  "submitTimeUtc": "2024-09-10T15:42:42Z"
}
```

Response Statuses for Saving an Order {#paypal-save-order-resp-fields}
======================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `COMPLETED`: The request was successful and the customer's payment information from the order is saved for future transactions.{#paypal-save-order-resp-fields_status-1}
  {#paypal-save-order-resp-fields_status-1}
* `INVALID_REQUEST`: The request was not successful. Send a new save order request.{#paypal-save-order-resp-fields_status-2}
  {#paypal-save-order-resp-fields_status-2} {#paypal-save-order-resp-fields_statuses-save-order}

Void an Order {#paypal-void-order-intro}
========================================

You can cancel a saved order from your system by requesting a void order. Cancelling an order is necessary if you decide you no longer need to authorize a saved order.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#paypal-void-order-intro_d7e450}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/voids`{#paypal-void-order-intro_d7e463}  
Set the *{id}* to the request ID.

Required Fields for Voiding an Order {#paypal-void-order-req-fields}
====================================================================

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_CANCEL`.

Example: Voiding an Order {#paypal-void-order-ex-rest}
======================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "method": {
        "name": "payPal"
      },
      "name": "eWallet"
    }
  },
  "processingInformation": {
    "actionList": [
      "AP_CANCEL"
    ]
  }
}
```

Response to a Successful Request

```
{
  "message": "Successful",
  "status": "VOIDED",
  "id": "7259850570396024801991",
  "submitTimeUtc": "2024-09-10T16:17:37Z"
}
```

Response Statuses for Voiding an Order {#paypal-void-order-resp-fields}
=======================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `VOIDED`: The request was successful and the customer's payment credentials are no longer saved.{#paypal-void-order-resp-fields_status-2}
  {#paypal-void-order-resp-fields_status-2}
* `INVALID_REQUEST`: The request was not successful. Send a new request.{#paypal-void-order-resp-fields_status-1}
  {#paypal-void-order-resp-fields_status-1} {#paypal-void-order-resp-fields_statuses-void-order}

Check Status for an Order {#paypal-status-order-intro}
======================================================

You can retrieve the current status of any API request by requesting a check status. Use the check status request as often as necessary to obtain the information you need.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-status-order-intro_d7e193}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-status-order-intro_d7e205}  
Set the *`{id}`* to the request ID of the API service you are retrieving.

Required Fields for Checking Status {#paypal-status-order-req-fields}
=====================================================================

[agreementInformation.agreementId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agreement-info-aa/agreement-info-agreement-id.md "")
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[paymentInformation.customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_STATUS`.

Example: Checking Status {#paypal-status-order-ex-rest}
=======================================================

Request

```
{
    "agreementInformation": {
        "agreementId": "agreementId"
    },
    "clientReferenceInformation": {
        "code": "12"
    },
    "processingInformation": {
        "actionList": [
            "AP_STATUS"
        ]
    },
    "paymentInformation": {
        "customer": {
            "customerId": "201.1"
        },
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    }
}
```

Response to a Successful Request

```
{
    "submitTimeUtc": "2024-09-12T15:45:31Z",
    "orderInformation": {
        "referenceId": "default",
        "description": "1bc",
        "merchantDescriptor": "Demo-Merchant"
    },
    "processorInformation": {
        "transactionId": "2F930071T65206814",
        "paymentUrl": "https://www.sandbox.paypal.com/checkoutnow?token=2F930071T65206814"
    },
    "paypalgateway_mid": "J4QDR26LU6K4A",
    "message": "Successful",
    "reconciliationId": "7261559298496016901991",
    "paypalgateway_merchant_email": "sb-g66r631737562@business.example.com",
    "status": "PAYER_ACTION_REQUIRE",
    "id": "7261559585096017001991"
}
```

Response Statuses for Checking Status {#paypal-status-order-resp-status}
========================================================================

`Cybersource` responds to your request with one of these statuses in the status response field. The possible statuses are dependent on the API service you are retrieving a status for.

Create Order
:
* `COMPLETED`: The order was approved by the customer. This status can also occur when the order is successfully used for an authorization or sale.
* `PAYER_ACTION_REQUIRE`: The request was successful, and you must redirect the customer to the PayPal checkout URL in order for the customer to approve the payment.
* `INVALID_REQUEST`: The request was not successful. Send a new request.

Update Order
:
* `COMPLETED`: The request was successful and the order information is updated.
* `INVALID_REQUEST`: The request was not successful. Send a new update order request.

Save Order
:
* `COMPLETED`: The request was successful and the customer's payment information from the order is saved for future transactions.
* `INVALID_REQUEST`: The request was not successful. Send a new save order request.

Void Order
:
* `VOIDED`: The request was successful and the customer's payment credentials are no longer saved.
* `INVALID_REQUEST`: The request was not successful. Send a new request.

Payment Processing Requests {#paypal-services}
==============================================

This section describes how to process a payment using the `REST API`.

Authorize a Payment {#paypal-auth-intro}
========================================

You must request an authorization to secure funds for a payment. Include the request ID that you received in the create order response in the processingInformation.intentsId request field to link the authorization to the created order.  
Successfully authorized funds expire after 29 days. If the funds are not captured within 3 days of the authorization, you must request Re-authorization to maintain the honor period. The *honor period* is a 3-day period in which PayPal accepts the capture request that a merchant submits. If the 3-day honor period expires because you did not send a re-authorization request, PayPal contacts the card's issuer to re-authorize the payment. For more information, see [Re-authorize a PayPal Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-reauth-intro.md "").  
The `PENDING` status and a request ID in the id response field indicate a successful request. Save the request ID for follow-on requests.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`

Required Fields for Authorizing a Payment {#paypal-auth-req-fields}
===================================================================

agreementInformation.id
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_AUTH`.

processingInformation.intentsId
:
Set to the request ID in the create order response id field.

Example: Authorizing a Payment {#paypal-auth-ex-rest}
=====================================================

Request

```
{
    "agreementInformation": {
        "id": "agreementId-1"
    },
    "paymentInformation": {
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    },
    "processingInformation": {
        "actionList": [
            "AP_AUTH"
        ],
        "intentsId": "7261369946776012601991"
    }
}
```

Response to a Successful Request

```
{
    "submitTimeUtc": "2024-09-12T10:29:56Z",
    "processorInformation": {
        "sellerProtection": {
            "eligibility": "ELIGIBLE",
            "disputeCategories": [
                "ITEM_NOT_RECEIVED",
                "UNAUTHORIZED_TRANSACTION"
            ]
        },
        "transactionId": "4AA39743A21277452",
        "orderStatus": "COMPLETED",
        "orderId": "7LT08604AM018373M",
        "updateTimeUtc": "2024-09-12T10:31:10Z",
        "expirationTimeUtc": "2024-10-11T10:31:10Z"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "28.60",
            "currency": "USD"
        },
        "billTo": {
            "email": "jsmith@cybs.com",
            "lastName": "Smith",
            "firstName": "John"
        }
    },
    "updateTimeUtc": "2024-09-12T10:31:10Z",
    "buyerInformation": {
        "merchantCustomerId": "FDYJEFZ6G5YPG"
    },
    "message": "Successful",
    "createTimeUtc": "2024-09-12T10:31:10Z",
    "clientReferenceInformation": {
        "code": "default"
    },
    "reconciliationId": "7261369946776012601991",
    "status": "COMPLETED",
    "id": "7261370686446012701991"
}
```

Response Statuses for Authorizing a Payment {#paypal-auth-resp-status}
======================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:

* `INVALID_REQUEST`: The authorization request was not successful. Send a new authorization request.{#paypal-auth-resp-status_status-2}
  {#paypal-auth-resp-status_status-2}
* `PENDING`: The authorization request was successful, and PayPal is reviewing the request. Use the check status request as often as necessary until the status updates.{#paypal-auth-resp-status_status-1}
  {#paypal-auth-resp-status_status-1}

When you request a status update, `Cybersource` responds with one of these statuses in the status response field:

* `COMPLETED`: The authorized funds were successfully captured.{#paypal-auth-resp-status_status-3}
  {#paypal-auth-resp-status_status-3}
* `PENDING`: The authorization request was successful, and PayPal is reviewing the request. Continue to send periodic check status requests until the status updates.{#paypal-auth-resp-status_status-5}
  {#paypal-auth-resp-status_status-5}
* `REVERSED`: The authorized funds were released back to the customer and cannot be captured.{#paypal-auth-resp-status_status-reverse}
  {#paypal-auth-resp-status_status-reverse}

Follow-On Requests
------------------

After the payment is authorized, you can send these follow-on requests using the request ID from the authorization response message.

Authorization Reversal
:
To cancel the hold on the authorized funds, you must send an authorization reversal request. For more information, see [Reverse an Authorization](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-reversal-intro.md "").

Re-authorization
:
To update information in the authorization, such as the payment amount, you must send a re-authorization request. For more information, see [Re-authorize a PayPal Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-reauth-intro.md "").

Capture
:
To capture the authorized funds and complete the payment, you must send a capture request. For more information, see [Capture a Payment](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-capture-intro.md "").

Check Status
:
To know when the authorization status updates, you must periodically send a check status request. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Re-authorize a PayPal Payment {#paypal-reauth-intro}
====================================================

Re-authorizing an authorized PayPal payment maintains the 3-day honor period in which you can capture the payment. If the 3-day honor period expires because you did not send a re-authorization request, PayPal contacts the card's issuer to re-authorize the payment. When the issuer approves the re-authorization, PayPal accepts the capture request you submitted. Re-authorizing an authorization also enables you to change the payment amount. You can begin requesting a re-authorization 3 days after the original authorization was requested. If you reauthorize a payment on the 28th day of its authorization period, you only have 1 day to capture it. You can only re-authorize *PayPal* payments. Re-authorizing a payment using saved credentials is not supported.

> IMPORTANT If you need to reverse a re-authorized payment, use the initial authorization request ID in the reversal request.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`

Required Fields for Re-authorizing a PayPal Payment {#paypal-reauth-req-fields}
===============================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_REAUTH`.

[processingInformation.linkId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-link-id.md "")
:

Example: Re-authorizing a PayPal Payment {#paypal-reauth-ex-rest}
=================================================================

Request

```
{
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "31.00",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "method": {
        "name": "payPal"
      },
      "name": "eWallet"
    }
  },
  "processingInformation": {
    "actionList": [
      "AP_REAUTH"
    ],
    "linkId": "7261189513277014411040"
  }
}
```

Response to a Successful Request

```
{
  "submitTimeUtc": "2024-09-18T05:11:30Z",
  "processorInformation": {
    "transactionId": "8XL39452XB324090U",
    "expirationTimeUtc": "2024-10-11T05:29:13Z",
    "updateTimeUtc": "2024-09-18T05:11:30Z"
  },
  "message": "Successful",
  "status": "COMPLETED",
  "id": "7266362888326306001991"
}
```

Response Statuses for Re-authorizing a PayPal Payment {#paypal-reauth-resp-status}
==================================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `INVALID_REQUEST`: The request was not successful. Send a new authorization request.{#paypal-reauth-resp-status_status-1}
  {#paypal-reauth-resp-status_status-1}

* `PENDING`: The request was successful, and PayPal is reviewing the request. Use the check status request as often as necessary until the status updates.{#paypal-reauth-resp-status_status-2}
  {#paypal-reauth-resp-status_status-2} {#paypal-reauth-resp-status_statuses}  
  When you request a status update, `Cybersource` responds with this status in the status field:

* `COMPLETED`: The request was successful and the authorization is updated.{#paypal-reauth-resp-status_status-complete}
  {#paypal-reauth-resp-status_status-complete}

Reverse an Authorization {#paypal-reversal-intro}
=================================================

You can cancel an authorized payment by requesting an authorization reversal, which removes the hold on any authorized funds. An authorization reversal is typically requested when a customer cancels a payment or a merchant captures less than the total authorized amount. You cannot reverse a reauthorized transaction.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`  
Set the *`{id}`* to the request ID returned in the authorization request.

Required Fields for Reversing an Authorization {#paypal-reversal-req-fields}
============================================================================

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_AUTH_REVERSAL`.

Example: Reversing an Authorization {#paypal-reversal-ex-rest}
==============================================================

Request

```
{
    "paymentInformation": {
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    },
    "processingInformation": {
        "actionList": [
            "AP_AUTH_REVERSAL"
        ]
    }
}
```

Response to a Successful Request

```
{
    "message": "Successful",
    "status": "REVERSED",
    "id": "7259791326166018601991",
    "submitTimeUtc": "2024-09-10T14:38:52Z"
}
```

Response Statuses for Reversing an Authorization {#paypal-reversal-resp-status}
===============================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `REVERSED`: The reversal request was successful, and the authorized funds are released from hold.
* `INVALID_REQUEST`: The reversal request was not successful. Send a new reversal request.
  {#paypal-reversal-resp-status_statuses}

Capture a Payment {#paypal-capture-intro}
=========================================

You can capture an authorized payment by requesting a capture, which completes the payment.  
You can capture the full amount in a single request or capture partial amounts in multiple capture requests.  
The `PENDING` status and a new request ID indicate a successful capture. Send a follow-on check status request periodically to receive the current status of the capture. The payment is complete when the check status request responds with a `COMPLETED` status. For more information about sending a check status request, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`  
Set the *`{id}`* to the request ID contained in the authorization response.

Required Fields for Capturing a Payment {#paypal-capture-req-fields}
====================================================================

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_CAPTURE`.

[processingInformation.captureOptions.isFinal](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-capture-ops-is-final.md "")
:
Set to one of these values:

    * `true`: Release the authorization hold on the remaining funds.
    * `false`: Do not release the authorization hold on the remaining funds.

processingInformation.captureOptions.notes
:

Example: Capturing a Payment {#paypal-capture-ex-rest}
======================================================

Request

```
{
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "65"
        }
    },
    "merchantInformation": {
        "merchantDescriptor": {
            "name": "test-descriptor"
        }
    },
    "processingInformation": {
        "captureOptions": {
            "notes": "paypalV2",
            "isFinal": "true"
        },
        "actionList": [
            "AP_CAPTURE"
        ]
    },
    "paymentInformation": {
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "transactionId": "6EM63359FN838823Y"
    },
    "message": "Successful",
    "status": "COMPLETED",
    "id": "7265097759866005201991",
    "submitTimeUtc": "2024-09-16T18:02:56Z"
}
```

Response Statuses for Capturing a Payment {#paypal-capture-resp-status}
=======================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `INVALID_REQUEST`: The capture request was not successful. Send a new capture request.{#paypal-capture-resp-status_status-1}
  {#paypal-capture-resp-status_status-1}

* `PENDING`: The capture request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").{#paypal-capture-resp-status_status-2}
  {#paypal-capture-resp-status_status-2}  
  When you request a status update, `Cybersource` responds with one of these statuses in the status field:

* `COMPLETED`: The funds were successfully captured, and the payment is complete.{#paypal-capture-resp-status_status-3}
  {#paypal-capture-resp-status_status-3}

* `DECLINED`: The funds were not captured because PayPal declined the request after a review.{#paypal-capture-resp-status_status-4}
  {#paypal-capture-resp-status_status-4}

Process a Sale {#paypal-sale-intro}
===================================

You can process a payment by requesting a sale, which authorizes and captures funds for a payment in the same request. Include the request ID that you received in the create order response in the processingInformation.intentsId request field to link the sale to the created order.  
A `PENDING` status in the response indicates that the request is successful. After sending a sale request, send a follow-on check status request periodically. The payment is complete when you receive a response with a `COMPLETED` status. For more information about sending a check status request, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`{#paypal-sale-intro_d7e345}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`{#paypal-sale-intro_d7e355}

Required Fields for Processing a Sale {#paypal-sale-req-fields}
===============================================================

agreementInformation.id
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `payPal`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_SALE`.

processingInformation.intentsId
:
Set to the request ID in the create order response id field.

Example: Processing a Sale {#paypal-sale-ex-rest}
=================================================

Request

```
{
    "agreementInformation":{
        "id":"BillingAgreement1"
    },
    "paymentInformation": {
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    },
    "processingInformation": {
        "actionList": [
            "AP_SALE"
        ],
        "intentsId": "7266411151136307001991"
    }
}
```

Response to a Successful Request

```
{
    "submitTimeUtc": "2024-09-18T06:35:32Z",
    "processorInformation": {
        "sellerProtection": {
            "eligibility": "ELIGIBLE"
        },
        "transactionId": "58N37188U0725624T",
        "orderStatus": "COMPLETED",
        "orderId": "4P210796DA793354A",
        "updateTimeUtc": "2024-09-18T06:35:32Z"
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "65.00",
            "currency": "USD"
        },
        "billTo": {
            "email": "jsmith@cybs.com",
            "lastName": "Smith",
            "firstName": "John"
        }
    },
    "buyerInformation": {
        "merchantCustomerId": "FDYJEFZ6G5YPG"
    },
    "message": "Successful",
    "processingInformation": {
        "captureOptions": {
            "finalCapture": "true"
        }
    },
    "clientReferenceInformation": {
        "code": "default"
    },
    "reconciliationId": "7266411151136307001991",
    "status": "COMPLETED",
    "id": "7266413310926307101991"
}
```

Response Statuses for Processing a Sale {#paypal-sale-resp-status}
==================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `INVALID_REQUEST`: The sale request is not successful. Send a new sale request.{#paypal-sale-resp-status_status-1}
  {#paypal-sale-resp-status_status-1}

* `PENDING`: The sale request is successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.{#paypal-sale-resp-status_status-2}
  {#paypal-sale-resp-status_status-2}  
  When you request a status update, `Cybersource` responds with one of these statuses in the status field:

* `COMPLETED`: The sale successfully processed, and the payment is complete.{#paypal-sale-resp-status_status-3}
  {#paypal-sale-resp-status_status-3}

* `DECLINED`: The sale request is declined. Send a new sale request.{#paypal-sale-resp-status_status-4}
  {#paypal-sale-resp-status_status-4}

* `PENDING`: The sale request is successful and is being reviewed by PayPal. Continue to send the check status request until the status updates. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Refund a Payment {#paypal-refund-intro}
=======================================

When a customer returns a purchase, you can request a refund to return the entire or partial payment amount to the customer's account. Include the request ID from a completed capture or sale. A `PENDING` response status indicates that the refund was successful. Send a follow-on check status request periodically to receive the current status of the refund. The payment is refunded when the check status request responds with the `REFUNDED` status. For more information about sending a check status request, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#paypal-refund-intro_d7e372}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#paypal-refund-intro_d7e385}  
The *{id}* is the request ID contained in the original transaction request.

Required Fields for Refunding a Payment {#paypal-refund-req-fields}
===================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_REFUND`.

Example: Refunding a Payment {#paypal-refund-ex-rest}
=====================================================

Request

```
{
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "31",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    },
    "processingInformation": {
        "actionList": [
            "AP_REFUND"
        ]
    }
}
```

Response to a Successful Request

```
{
    "processorInformation": {
        "transactionId": "8EY55721B5181393M"
    },
    "message": "Successful",
    "status": "REFUNDED",
    "id": "7262018791236022601991",
    "submitTimeUtc": "2024-09-13T04:31:19Z"
}
```

Response Statuses for Refunding a Payment {#paypal-refund-resp-status}
======================================================================

`Cybersource` responds to your request with one of these statuses in the status response field:
* `PENDING`: The refund request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.{#paypal-refund-resp-status_status-1}
  {#paypal-refund-resp-status_status-1}

* `INVALID_REQUEST`: The refund request was not successful. Send a new refund request.{#paypal-refund-resp-status_status-2}
  {#paypal-refund-resp-status_status-2}  
  When you request the status of a refund, Cybersource responds with one of these statuses in the status response field:

* `REFUNDED`: The captured funds were successfully refunded to the customer's account. This status can also occur during a customer dispute, such as a chargeback or reversal.{#paypal-refund-resp-status_status-4}
  {#paypal-refund-resp-status_status-4}

Check Status for a Transaction {#paypal-status-intro}
=====================================================

You can retrieve the current status of any API request by requesting a check status. Use the check status request as often as necessary to obtain the information you need.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-status-intro_d7e193}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#paypal-status-intro_d7e205}  
Set the *`{id}`* to the request ID of the API service you are retrieving.

Required Fields for Checking Status {#paypal-status-req-fields}
===============================================================

[agreementInformation.agreementId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/agreement-info-aa/agreement-info-agreement-id.md "")
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[paymentInformation.customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to one of these values:

    * `payPal`: the PayPal payment method.
    * `venmo`: the Venmo payment method.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `eWallet`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_STATUS`.

Example: Checking Status {#paypal-status-ex-rest}
=================================================

Request

```
{
    "agreementInformation": {
        "agreementId": "agreementId"
    },
    "clientReferenceInformation": {
        "code": "12"
    },
    "processingInformation": {
        "actionList": [
            "AP_STATUS"
        ]
    },
    "paymentInformation": {
        "customer": {
            "customerId": "201.1"
        },
        "paymentType": {
            "method": {
                "name": "payPal"
            },
            "name": "eWallet"
        }
    }
}
```

Response to a Successful Request

```
{
    "submitTimeUtc": "2024-09-12T15:45:31Z",
    "orderInformation": {
        "referenceId": "default",
        "description": "1bc",
        "merchantDescriptor": "Demo-Merchant"
    },
    "processorInformation": {
        "transactionId": "2F930071T65206814",
        "paymentUrl": "https://www.sandbox.paypal.com/checkoutnow?token=2F930071T65206814"
    },
    "paypalgateway_mid": "J4QDR26LU6K4A",
    "message": "Successful",
    "reconciliationId": "7261559298496016901991",
    "paypalgateway_merchant_email": "sb-g66r631737562@business.example.com",
    "status": "PAYER_ACTION_REQUIRE",
    "id": "7261559585096017001991"
}
```

Response Statuses for Checking Status {#paypal-status-resp-status}
==================================================================

`Cybersource` responds to your request with one of these statuses in the status response field. The possible statuses are dependent on the API service you are retrieving a status for.

Authorization
:
* `COMPLETED`: The authorized funds were successfully captured.
* `INVALID_REQUEST`: The authorization request was not successful. Send a new authorization request.
* `PENDING`: The authorization request was successful, and PayPal is reviewing the request. Use the check status request as often as necessary until the status updates.
* `REVERSED`: The authorized funds were released back to the customer and cannot be captured.

Authorization Reversal
:
* `REVERSED`: The reversal request was successful, and the authorized funds are released from hold.
* `INVALID_REQUEST`: The reversal request was not successful. Send a new reversal request.

Capture
:
* `COMPLETED`: The funds were successfully captured, and the payment is complete.
* `DECLINED`: The funds were not captured because PayPal declined the request after a review.
* `INVALID_REQUEST`: The capture request was not successful. Send a new capture request.
* `PENDING`: The capture request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates. For more information, see [Check Status for a Transaction](/docs/cybs/en-us/paypal/developer/all/rest/paypal/paypal-services/paypal-status-intro.md "").

Re-authorization
:
* `COMPLETED`: The request was successful and the authorization is updated.
* `INVALID_REQUEST`: The request was not successful. Send a new authorization request.
* `PENDING`: The request was successful, and PayPal is reviewing the request. Use the check status request as often as necessary until the status updates.

Refund
:
* `REFUNDED`: The captured funds were successfully refunded to the customer's account. This status can also occur during a customer dispute, such as a chargeback or reversal.
* `INVALID_REQUEST`: The refund request was not successful. Send a new refund request.
* `PENDING`: The refund request was successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.

Sale
:
* `COMPLETED`: The sale successfully processed, and the payment is complete.
* `DECLINED`: The sale request is declined. Send a new sale request.
* `INVALID_REQUEST`: The sale request is not successful. Send a new sale request.
* `PENDING`: The sale request is successful and is being reviewed by PayPal. Use the check status request as often as necessary until the status updates.

Reference Information {#paypal-ref-info}
========================================

This section contains reference information that is useful when integrating PayPal and Venmo.

Including Line Items in Requests {#paypal-create-order-line-items}
==================================================================

PayPal requires that each unique item in your customers' purchases be itemized as line items when you create or manage an order.  
*Line items* are used to include information about each item, such as product name, quantity, and price.  
Line items are included in a request in the lineItem\[\] array request field.  
These fields are required for each line item in your request:

[orderInformation.lineItems\[\].productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].typeOfSupply](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-type-of-supply.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Including Line Items  
This example shows how to format line items in a request.

```
{
 "orderInformation": {
        "lineItems": [
            {
                "productName": "test-product-1",
                "quantity": 5,
                "productDescription": "description-123",
                "unitPrice": "20",
                "taxAmount": "10",
                "totalAmount": "100",
                "typeOfSupply": "01"
            },
            {
                "productName": "test-product-2",
                "quantity": 1,
                "productDescription": "description-456",
                "unitPrice": "5",
                "taxAmount": "1",
                "totalAmount": "6",
                "typeOfSupply": "01"
            },
            {
                "productName": "test-product-3",
                "quantity": 2,
                "productDescription": "description-789",
                "unitPrice": "4",
                "taxAmount": "2",
                "totalAmount": "10",
                "typeOfSupply": "01"
            }
        ]
    }
}
```

Generating Reports In the `Business Center` {#conref-altpay-reporting}
======================================================================

You can generate various types of reports for your financial and reconciliation data. For more information about how to automate your reports, see the [*Reporting Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/reporting/developer/all/rest/reporting/reporting_api.md ""). For more information about how to use your `Business Center` account to generate reports, see the [*Reporting User Guide*](https://developer.cybersource.com/library/documentation/dev_guides/reporting_and_reconciliation/Reporting_User.pdf "").  
The Reporting User Guide contains these relevant topics:

* How and When Reports Are Generated
* Downloading Available Reports
* Subscribing to Standard Reports

Additional Resources
--------------------

For additional information about how to use the `Business Center` and manage reports, see these helpful resources.

`Business Center` Navigation
:
For an overview of the various resources available in the `Business Center`, see this YouTube video:

    [watch?v=UDmAWGHPbWs](https://www.youtube.com/watch?v=UDmAWGHPbWs "")

Getting Started with the `Business Center`
:
For a step-by-step demonstration of how to navigate in the `Business Center`, see this YouTube video:

    [watch?v=2qi_g2DParI](https://www.youtube.com/watch?v=2qi_g2DParI "")

Managing Report Subscriptions
:
For an overview of how to manage report subscriptions in the Downloadable Reports section in the `Business Center`, see this YouTube video:

    [watch?v=tFlmkXtvxWE](https://www.youtube.com/watch?v=tFlmkXtvxWE "")

Downloading Reports
:
For an overview of how to download available reports in the Reports section of the `Business Center`, see this YouTube video:

[watch?v=E0slUYjJvmw](https://www.youtube.com/watch?v=E0slUYjJvmw "")

Configure Alternative Payments Methods in the `Business Center` {#manage-self-enable-altpay}
============================================================================================

Follow these steps to configure alternative payment methods in the `Business Center`:

1. In the left navigation panel, click the **Available Products** icon. The Available Products page appears.{#manage-self-enable-altpay_step-1}
   {#manage-self-enable-altpay_step-1}
2. In the Alternative Payment Methods section, click **Enable**.{#manage-self-enable-altpay_step-2}
   {#manage-self-enable-altpay_step-2}
3. Check the box next to each alternative payment method you want to enable and configure. You can choose alternative payment methods from these categories:
   * Bank Transfer
   * Buy Now Pay Later (BNPL)
   * Card Payment
   * Direct Debit
   * eWallet
   * Gift Card
   * Local Card
   * Post Pay Reference
   * QR
4. Click Continue. The Product Configuration page appears.
5. Enter the required details for each alternative payment method you want to configure.  
   Click Copy to other sections to populate the information to any other alternative payment methods that you selected.

   > IMPORTANT
   > You must select I have read and agree to the Terms and Conditions for each alternative payment method you want to enable.

6. Click **Continue** to return to the Available Products page.{#manage-self-enable-altpay_step-6}
   {#manage-self-enable-altpay_step-6}

Add Merchant Account Information {#boarding-merchants-v2-add-merch-acct-info}
=============================================================================

Follow these steps to add merchant account information:

1. In Basic Information, enter the merchant account name and the organization ID in the provided text fields.

   #### ADDITIONAL INFORMATION

   * The merchant account name is the name of the business.
   * The organization ID is the name or identifier of the account that you are creating. It must be unique, not just in the portfolio or account, but in the system.
2. Enter the merchant information in the provided text fields. Required fields are noted with an asterisk (\*).

3. Click **Save** . You are returned to the Add Merchant page. You can skip the optional hierarchy step by clicking **Skip**.

Configure the Transacting Organization and Products {#boarding-merchants-v2-add-trans-org-prod}
===============================================================================================

Follow these steps to modify the transacting organization details, or to enable and configure products for the transacting organization:

1. Click **Start** in the Transacting Organization and Products section. The Transacting Organization and Products page is displayed.
2. Optional: modify the name and ID of the organization by using the text fields in the Transacting Organization Details section. By default, the name is the merchant name with 001 added to the end of the name. If you accept this default, additional transacting organizations will have default names that iterate the numbers at the end of their names, beginning with 002.
3. Optional: to edit the organization information, Click **Edit** in the Transacting Organization Information section. After editing, click **Apply**.
4. To enable a product in the Product Enablement section, click the Enablement drop-down menu and select **Enabled**.
5. To modify the configuration, click the **Edit** or **configure** button (depending on the product). Some products are not configurable.
6. To confirm the configuration, click **Apply**.
7. To save all product configurations, click **Save**. You are returned to the Add Merchant page.
8. To continue working with this organization, click **Continue working with this merchant** . To finish and return to Merchant Management, click **Return to merchant management**.

Set Up the Transacting Organization and Products {#boarding-merchants-v2-add-merch-trans-org-prod}
==================================================================================================

The transacting organization is the entity that processes transactions. Follow these steps to create a transacting organization and configure products for it:

1. Click **Start** in the Transacting Organization and Products section. The Transacting Organization and Products page is displayed.

2. Optional: modify the name and ID of the organization by using the text fields in the Transacting Organization Details section. The ID must be unique, not just in the portfolio or account, but across the system. By default, the name is the merchant name with 001 added to the end of the name. If you accept this default, additional transacting organizations will have default names that iterate the numbers at the end of their names, beginning with 002.

3. Optional: By default, the organization information is inherited from the parent organization. To edit the organization information, click **Edit** in the Transacting Organization Information section. After editing, click **Apply**.

4. To enable a product in the Product Enablement section, click the Enablement drop-down menu and select **Enabled**.

5. To modify the configuration, click the **Edit** or **Configure** button (depending on the product). Some products are not configurable.

6. To confirm the configuration, click **Apply**.

7. To save all product configurations, click **Save**. You are returned to the Add Merchant page.

8. To continue working with this organization, click **Continue working with this merchant** . To finish and return to Merchant Management or to add another merchant, click **Return to merchant management**.

   #### ADDITIONAL INFORMATION

   The image below shows the Transacting Organization and Products page.

   #### Figure: {#boarding-merchants-v2-add-merch-trans-org-prod_transacting}

Transacting Organization and Products ![](/content/dam/new-documentation/documentation/en-us/topics/platform/bam/boarding-user/images/transacting_org.PNG/jcr:content/renditions/original)
