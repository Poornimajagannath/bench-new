Klarna Integration Developer Guide {#klarna-about-guide}
========================================================

This section describes how to use this developer guide and where to find further information.

Audience and Purpose
--------------------

This guide is written for merchants who want to offer Klarna payments services to customers. It describes tasks that a merchant must complete in order to make a payment, request the status of a payment, or refund a payment. It is intended to help the merchant provide a seamless customer payment experience.

Convention
----------

These statements appear in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> WARNING
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.visaacceptance.com>

Recent Revisions to This Document {#klarna-doc-revisions}
=========================================================

26.05.01
--------

This revision contains only editorial changes and no technical updates.

26.03.01
--------

Updated processing workflows see [Overview of Processing Klarna Transactions](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow.md "").

25.01
-----

Added support for Klarna chargeback notifications. See [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "").  
Add new status for chargebacks. See [Capture a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-capture-intro.md "") and [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").  
Updated and added new workflow graphics that describe how to process Klarna transactions. See [Overview of Processing Klarna Transactions](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow.md "").

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Visa Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Visa Platform Connect ACQUIRER.

Introduction to Klarna Integration {#klarna-intro}
==================================================

Klarna is a Buy Now Pay Later (BNPL) payment method that you can offer your customers through `Cybersource`. With Klarna, you can enable your customers to split their payments into multiple installments. You can display the Klarna payment method to your customers during checkout by either presenting a Klarna widget or redirecting your customers to a Klarna-hosted webpage.

Klarna API Requests
-------------------

These are the API requests you must integrate with to process a Klarna transaction:

* Session
* Authorization
* Capture
* Refund
* Authorization-reversal
* Check status

Requirements
------------

You must obtain a `Cybersource` merchant ID and a Klarna API key for each country in which you process transactions. Contact your `Cybersource` account manager for more information.

Supported Countries and Currencies
----------------------------------

Contact your account manager for the latest supported countries and currencies information.  
For information about the country codes, currency codes, and language codes, see these relevant guides:

* [*ISO Standard Country Codes*](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.md "")
* [*ISO Standard Currency Codes*](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "")
* [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "")

Klarna Review Process
---------------------

Before you can launch Klarna payments, Klarna reviews your integrations. For more information about Klarna's pre-launch review process, contact your `Cybersource` account manager.

Shipping Policies
-----------------

Always follow the shipping policies for each country as outlined by Klarna to ensure that Klarna assumes liability for fraudulent transactions. For Klarna's shipping policy, see:  
<https://www.klarna.com/international/shipping-policies/>

Disputes and Fraud
------------------

Klarna has a standard process for handling risky transactions and disputes between you and your customers. For more information, contact your technical account manager or customer support.

Chargeback Notifications
------------------------

Customers can file payment disputes directly to Klarna to receive a chargeback payment for the disputed amount.  
For information about setting up notifications for chargebacks, see [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "").

Getting Started with REST
-------------------------

To begin processing payments through `Cybersource`, you must first set up your payment processing system to be REST compliant. `Cybersource` uses the REST, or (REpresentational State Transfer), architecture for developing web services. REST enables communication between a client and server using HTTP protocols.  
For more information about how to set up secure communications between your client and server using either a **JSON Web Token** or **HTTP signature** , see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Merchant Account Types {#klarna-intro-acct}
===========================================

There are two types of `Cybersource` merchant accounts, *`Cybersource` settlement services account* and *processor direct contract account*.

`Cybersource` Settlement Services Account
-----------------------------------------

This merchant account has no direct contract with a payment provider partner. The `Cybersource` Financial Settlement Partner (FSP) collects funds on your behalf and settles them to your merchant account.

> IMPORTANT
> ` Cybersource ` requests the export compliance service for every transaction using the ` Cybersource ` settlement services account. The export compliance service compares customer information to export control lists maintained by government agencies. If a customer's name appears on any government list, the transaction is declined.  
> To facilitate compliance checks for `Cybersource` settlement services accounts, you must include these fields in your authorization service requests.  
> You must include these fields in the live environment to avoid receiving error messages.

Required Authorization Fields for a `Cybersource` Settlement Services Account
-----------------------------------------------------------------------------

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

Processor Direct Contract Account
---------------------------------

This merchant account must use the payment provider selected by `Cybersource`. If you have existing direct contracts, you must inform your sales representative.

Overview of Processing Klarna Transactions {#klarna-intro-flow}
===============================================================

This section provides an overview of the two methods for processing a payment using Klarna, as well as the order in which to send the Klarna API requests for these two methods.  
There are two methods for processing a payment that are determined by how the customer accesses their Klarna account to complete the checkout:

**Hosted Order Page**
:
The customer is redirected to a Klarna-hosted order page (HOP) to complete the checkout. For overview information about how to process a payment using the HOP method, see [HOP Session Workflow](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow/klarna-intro-flow-hop.md "").

**Inline**
:
The customer uses the Klarna widget that is installed into the merchant website to complete the checkout. For overview information about how to process a payment using the inline method, see [Inline Session Workflow](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow/klarna-intro-flow-inline.md "").
:
For information about how to install the Klarna widget into the merchant website, see [Widget Installation for Inline Workflow](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow/klarna-intro-flow-sdk.md "").

HOP Session Workflow {#klarna-intro-flow-hop}
=============================================

This workflow describes the sequence of events that comprises a successful payment using a Klarna hosted-page.

#### Figure:

Klarna HOP Workflow ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-hop-600x575.svg/jcr:content/renditions/original)

1. The customer begins to checkout on the merchant website and chooses the Klarna payment option.
   2. The merchant sends a HOP session API request to `Cybersource`. For more information, see [Creating a HOP Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-intro.md "").  
      If the customer changes their purchase selection after the merchant sends the session API request, the merchant must send an update session API request. For more information, see [Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro.md "").
2. `Cybersource` responds to the merchant with an `INITIATED` status and a Klarna redirect URL.
3. The merchant redirects the customer to the Klarna URL.
4. The customer completes checkout on the Klarna hosted-page and is redirected back to the merchant website. Klarna appends a unique authorization token to the merchant redirect URL.
5. The merchant sends an authorization API request to `Cybersource` and includes the authorization token Klarna appended to the merchant URL. For more information, see [Authorize a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-intro.md "").
6. `Cybersource` responds to the merchant with the `AUTHORIZED` status and a request ID.{#klarna-intro-flow-hop_step-7}
   {#klarna-intro-flow-hop_step-7}
7. The merchant sends a capture API request with the request ID. For more information, see [Capture a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-capture-intro.md "").{#klarna-intro-flow-hop_step-10}
   {#klarna-intro-flow-hop_step-10}
8. `Cybersource` responds to the merchant with the `SETTLED` status and a request ID.{#klarna-intro-flow-hop_step-11}
   {#klarna-intro-flow-hop_step-11}
9. The merchant displays a payment confirmation to the customer.{#klarna-intro-flow-hop_step-14}
   {#klarna-intro-flow-hop_step-14}

Inline Session Workflow {#klarna-intro-flow-inline}
===================================================

This workflow describes the sequence of events that comprises a successful payment using a Klarna widget.  
For information about how to install the Klarna widget, see [Widget Installation for Inline Workflow](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow/klarna-intro-flow-sdk.md "").

#### Figure:

Klarna Inline Workflow ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-inline-600x575.svg/jcr:content/renditions/original)

1. The customer begins to checkout on the merchant website using the displayed Klarna widget.
   2. The merchant sends an inline session API request to `Cybersource`. For more information, see [Creating an Inline Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-in-intro.md "").  
      If the customer changes their purchase selection after the merchant sends the session API request, the merchant must send an update session API request. For more information, see [Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro.md "").
2. `Cybersource` responds to the merchant with the `INITIATED` status and a pre-approval token.
3. The merchant sets the *Session Token ID* in the Klarna widget to the pre-approval token.
4. The customer completes checkout using the Klarna widget, and the Klarna widget generates a unique authorization token.
5. The merchant sends an authorization API to `Cybersource` request and includes the unique authorization token the Klarna widget displayed. For more information, see [Authorize a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-intro.md "").
6. `Cybersource` responds to the merchant with the `AUTHORIZED` status and a request ID.
7. The merchant sends a capture API request with the request ID. For more information, see [Capture a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-capture-intro.md "").
8. `Cybersource` responds to the merchant with the `SETTLED` status and a request ID.
9. The merchant displays a payment confirmation to the customer.

Widget Installation for Inline Workflow {#klarna-intro-flow-sdk}
================================================================

This workflow describes how to install the Klarna widget and complete a successful transaction. For a description of a successful transaction with the Klarna widget already installed, see [Inline Session Workflow](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-intro-flow/klarna-intro-flow-inline.md "").

#### Figure:

Widget Installation for Inline Workflow  
![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-flow-widget-600x440.svg/jcr:content/renditions/original)

1. Add the container for the Klarna widget to the HTML for your checkout page. This is a one-time operation and provides an iframe into which the Klarna widget will be dynamically loaded when the Klarna widget is initialized.

   ```
   &lt;div id=#klarna_container"&gt;&lt;/div&gt;
   ```
2. When the customer displays your checkout page, send a create session request to `Cybersource`. The sessions service creates a unique customer session and returns a pre-approval token. See [Creating a HOP Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-intro.md "") and [Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro.md "").

3. Present the available payment methods to the customer. When the customer chooses the Klarna payment method on your checkout page, install the Klarna software developer kit (SDK) and initialize it by calling **Klarna.Payments.init** . In the request, set the client token field to the value of the pre-approval token returned by `Cybersource`.  
   Initializing the Klarna SDK can take up to 10 seconds. `Cybersource` recommends that you try to initialize the SDK every three seconds, up to a maximum of three attempts.  
   For additional information about initializing the Klarna SDK, see:

   ```
   https://docs.klarna.com/klarna-payments/in-depth-knowledge/klarna-payments-sdk-reference/ 
   ```

   ```
   Klarna.Payments.init({client_token: '&lt;%=processorToken%&gt;'})
       if (count &lt; 3)
       {    
           setTimeout(initializeKlarna.bind(null, count), 3000);
       }
       else
       {
           showError()
       }
   ```
4. Load the Klarna widget into the Klarna container by calling **Klarna.Payments.load** and specifying the Klarna container.

   ```
   Klarna.Payments.load({
       container: "#klarna_container",
       (...)
   })
   ```
5. Display the Klarna payment options on your checkout page. The `show_form = true` statement dynamically updates the payment options in the Klarna widget.

   ```
   if (res["show_form"] == true)
   {
       logging("Klarna Available Payment Option");

       document.getElementById("auth_button").innerHTML =
       "&lt;br&gt;&lt;button type=\"button\" name=\"buy\"
       onclick=\"authorizeKlarnaOrder();\"&gt;Pay&lt;/button&gt;"
   }
   else
   {
       logging("Klarna Not Available As A Payment Option");
   }
   ```
6. When the customer chooses one of the Klarna payment options:

   * Send an update session request to `Cybersource` with available customer information. See [Creating a HOP Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-intro.md "") and [Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro.md "").

     * Call **Klarna.Payments.authorize** to authorize the order with Klarna. In the call, include an empty JSON object. For additional information about Klarna authorizations, see:

     ```
     https://docs.klarna.com/klarna-payments/api-call-descriptions/authorize-the-purchase/
     ```

   {#klarna-intro-flow-sdk_ul_sfm_nrg_crb}

   ```
   Klarna.Payments.authorize({}, function(res) {
       var auth_token = res["authorization_token"];
       var isApproved = res["approved"];
       var show_form = res["show_form"];
   })
   ```
7. Klarna validates the customer's information and determines whether to authorize the order. When Klarna authorizes the order, Klarna returns an authorization token.

8. Send an authorization request to `Cybersource`. Set the pre-approval token field to the value of the authorization token returned by Klarna. See [Authorize a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-intro.md "").

9. When `Cybersource` approves the authorization, send a capture request to complete the purchase. See [Capture a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-capture-intro.md "").  
   When the authorization response indicates that the purchase is pending, send a check status request every hour until the payment status changes. See [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").

Refunding a Payment Workflow {#concept}
=======================================

This workflow describes the sequence of events that comprises issuing a successful refund with Klarna.

#### Figure:

Refund Workflow  
![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-refund-600x275.svg/jcr:content/renditions/original)

1. The customer returns the purchase to the merchant.
2. The merchant sends a refund API request to `Cybersource` with the request ID from the successful capture. For more information, see [Refund a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-refund-intro.md "").
3. `Cybersource` responds to the merchant with the `REFUNDED` status and a refund request ID.
4. The merchant displays a refund confirmation to the customer.

Reversing an Authorized Payment Workflow {#concept}
===================================================

This workflow describes the sequence of events that comprises reversing an authorization, also known as cancelling a payment, with Klarna.

#### Figure:

Authorization Reversal Workflow  
![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-refund-600x635.svg/jcr:content/renditions/original)

1. The customer begins to checkout on the merchant website and either chooses the Klarna payment option or uses the Klarna widget.
2. The merchant sends either a HOP or inline session API request to `Cybersource`. For more information, see [Creating a HOP Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-intro.md "") and [Creating an Inline Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-in-intro.md "").
3. `Cybersource` responds with the initiated status and either a Klarna redirect URL or Klarna pre-approval token.
4. The merchant either redirects the customer to a Klarna URL or sets the Klarna widget to a unique token.
5. The customer completes the checkout using either the Klarna URL or widget. If the customer used the Klarna URL, the customer is redirected to the merchant website.
6. The merchant sends an authorization API request to `Cybersource`. For more information, see [Authorize a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-intro.md "").
7. `Cybersource` responds to the merchant with the `AUTHORIZED` status and an authorization request ID.
8. The customer or merchant decides to cancel the payment.
9. The merchant sends an authorization reversal API request to `Cybersource`. For more information, see [Reverse an Authorized Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-reversal-intro.md "").
10. `Cybersource` responds to the merchant with the `AUTH_REVERSED` status.
11. The merchant displays a payment cancellation confirmation to the customer.

Transaction Statuses Workflow {#concept}
========================================

This workflow describes the sequence of possible statuses you can receive when processing a Klarna transaction.

#### Figure:

Transaction Statuses Workflow  
![](/content/dam/documentation/cybs/en-us/topics/payments-processing/altpay/klarna/graphics/klarna-status-flow-600x1040.svg/jcr:content/renditions/original)

1. The merchant sends a session API request to `Cybersource` and receives one of these possible statuses:
   * `COMPLETED`: The customer completed the checkout process. You can now authorize the funds.
   * `FAILED`: The session request is not successful. Send a new session request.
   * `INITIATED`: The session is initiated and the customer may now checkout. Send periodic check status requests until the status updates to `COMPLETED`. For more information, see [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").
2. The merchant sends an authorization API request to `Cybersource` and receives one of these possible statuses:
   * `FAILED`: The authorization request is not successful. Send a new authorization request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
   * `AUTHORIZED`: The customer's funds are authorized. You can now capture the authorized amount.
   3. The merchant sends a check status API request to `Cybersource` and receives one of these possible statuses:
   * `ABANDONED`: The customer did not complete the payment using the redirect URL or widget.
   * `AUTHORIZED`: The customer's funds are authorized. You can now capture the authorized amount.
   * `FAILED`: The authorization request is not successful. Send a new authorization request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
3. If the customer or merchant decides to cancel the purchase, the merchant sends an authorization reversal API request to `Cybersource` and receives one of these possible statuses:
   * `FAILED`: The authorization reversal is not successful. Send a new request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
   * `AUTH_REVERSED`: The authorization is successfully reversed.
4. The merchant sends a capture API request to `Cybersource` and receives one of these possible statuses:
   * `FAILED`: The capture request is not successful. Send a new capture request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
   * `SETTLED`: The capture request is settled for the requested amount.
   6. The merchant sends a check status for the capture API request to `Cybersource` and receives one of these possible statuses:
   * `CHARGEBACK`: The customer submitted a payment dispute for the purchase, and Klarna reviewed and approved a chargeback to the customer. For more information about chargebacks, see [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "").
   * `FAILED`: The capture request is not successful. Send a new capture request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
   * `SETTLED`: The capture request is settled for the requested amount.
5. If the customer returns a purchase, the merchant sends a refund API request to `Cybersource` and receives one of these possible statuses:
   * `FAILED`: The refund request is not successful. Send a new refund request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
   * `REFUNDED`: The captured payment is successfully refunded.
   8. The merchant sends a check status for the refund API request to `Cybersource` and receives one of these possible statuses:
   * `FAILED`: The refund request is not successful. Send a new refund request. A failed request can be due to either Klarna rejecting the transaction or a technical error.

* `REFUNDED`: The captured payment is successfully refunded.

Klarna API Requests {#klarna-services}
======================================

This section describes how to send these Klarna requests using the `REST API`:

* [Creating a HOP Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-intro.md "")
* [Creating an Inline Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-cr-in-intro.md "")
* [Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro.md "")
* [Authorize a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-intro.md "")
* [Update an Authorized Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-auth-fo-intro.md "")
* [Reverse an Authorized Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-reversal-intro.md "")
* [Capture a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-capture-intro.md "")
* [Refund a Payment](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-refund-intro.md "")
* [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "")

Creating a HOP Session {#klarna-session-cr-intro}
=================================================

Create a new session whenever the customer displays your checkout page.

**HOP Specifications**
:
When you send a HOP session request, set the apSessionService_paymentFlowMode field value to `HOP`. `Cybersource` responds with a Klarna redirect URL in the processorInformation.paymentUrl field. Send the customer to the redirect URL to complete the checkout. When the customer completes the checkout, Klarna redirects the customer back to the merchant website and includes a token in the merchant URL. The token generated by Klarna can then be used in the authorization request to link it to the session.

Klarna Payment Methods {#klarna-session-cr-intro_method-name}
-------------------------------------------------------------

When you request the session service, you can determine the Klarna payment method you want to offer your customers. Set the optional paymentInformation.paymentType.method.type request field to a value listed in the Payment Method column.

| Payment Method Field Value |                    Description                     |                                       Klarna Products                                       |
|----------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| `pay_later`                | Customer pays total bill at a set date.            | * Klarna Invoice * Klarna Pay Later * Klarna Pay Later by Card (PLBC)                       |
| `pay_now`                  | Customer pays total bill at the time of checkout.  | * Klarna Direct Bank Transfer * Klarna Direct Debit                                         |
| `pay_over_time`            | Customer pays bill in equal multiple installments. | * Klarna Account * Klarna Financing * Klarna Fixed Installment Plans * Klarna Interest Free |
[Payment Methods]

Example: Payment Methods in Session Request
:

    ```
    {
      "paymentInformation": {
        "paymentType": {
          "method": {
            "type": "pay_later"
          }
        }
      }
    }
    ```

Calculating the Grand Total Amount {#klarna-session-cr-intro_grand-total-section}
---------------------------------------------------------------------------------

Klarna requires that the grand total amount of a purchase be included in the request using the orderInformation.amountDetails.totalAmount field. The country of the transaction and the use of coupons affect how to calculate the grand total amount.  
For more information about how to calculate the grand total amount, see [Calculating the Grand Total Amount](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-intro-total.md "") in the Reference Information section.

Language Specification
----------------------

To set the language for your Klarna checkout experience, include the buyerInformation.language field in your request. By not including this field, the Klarna checkout experience is set to English by default. For a list of all possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

Example: Language Specification
:

    ```
    {
      "buyerInformation": {
        "language": "es"
      }
    }
    ```

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payment-references`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payment-references`

Line Items {#klarna-session-cr-intro_line-items-section}
--------------------------------------------------------

Klarna uses line items when you send a create session and update session requests. [Line items](# "") are used to include information about the goods that your customers purchase, such as product name, quantity, and price.  
Line items are represented in a request as the lineItem\[\] array request fields.  
For more information about how to properly format line items in your request, see [Using Line Items](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-intro-items.md "") in the Reference Information section.

Response Status {#klarna-session-cr-intro_session-response}
-----------------------------------------------------------

The session service responds with one of these statuses as the status field value:

* `FAILED`: The session request is not successful. Send a new session request.{#klarna-session-cr-intro_status-2}
  {#klarna-session-cr-intro_status-2}

* `INITIATED`: The session is initiated and the customer may now checkout. Send periodic check status requests until the status updates to `COMPLETED`. For more information, see [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").{#klarna-session-cr-intro_status-4}
  {#klarna-session-cr-intro_status-4} {#klarna-session-cr-intro_session-cr-status}  
  When you send a check status request for an initiated session, you can receive one of these statuses when the session updates:

* `ABANDONED`: The customer did not complete the payment using the redirect URL or widget.{#klarna-session-cr-intro_status-abandoned}
  {#klarna-session-cr-intro_status-abandoned}

* `COMPLETED`: The customer completed the checkout process. You can now authorize the funds.{#klarna-session-cr-intro_status-completed}
  {#klarna-session-cr-intro_status-completed}

Requesting to Create a HOP Session {#klarna-session-cr-task-hop}
================================================================

Follow these steps to successfully create a HOP session.

1. Send a` POST` request to the `https://apitest.cybersource.com/pts/v2/payment-references` endpoint and include these required fields:

   > IMPORTANT Do not send any personally identifiable information (PII) data about the customer in the request to create a session.

   [merchantInformation.cancelUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-cancel-url.md "")
   :

   [merchantInformation.failureUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-failure-url.md "")
   :

   [merchantInformation.successUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-success-url.md "")
   :

   [orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
   :

   [orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
   :

   orderInformation.billTo.postalCode
   :

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   [paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
   :
   Set to `KLARNA`.

   [paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
   :
   Set to `INVOICE`.

   [processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
   :
   Set to `AP_SESSIONS`.

   processingInformation.paymentFlowMode
   :
   Set to `HOP` to display the Klarna widget on your checkout page.

   processingInformation.sessionType
   :
   Set to `N`.

   Non-US Countries
   :   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")

   US
   :
   [orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
   :
   [orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
   {#klarna-session-cr-task-hop_cntry-fields} {#klarna-session-cr-task-hop_request}

2. You can include these optional fields in the request:

   [buyerInformation.language](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-language.md "")
   :
   > IMPORTANT If this field is not included, the language is set to English by default.

   :
   For a list of possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :

   [orderInformation.amountDetails.discountAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
   :

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   [orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
   :

   [orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
   :

   [orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
   :

   [orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
   :

   [orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
   :

   orderInformation.lineItems\[\].productCode
   :

   orderInformation.lineItems\[\].productDescription
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   orderInformation.lineItems\[\].quantity
   :

   orderInformation.lineItems\[\].taxAmount
   :

   paymentInformation.paymentType.method.type
   :

   paymentInformation.type
   :

   processingInformation.sessionType
   :
   {#klarna-session-cr-task-hop_opt-fields}
   {#klarna-session-cr-task-hop_opt-fields}

3. To include an optional coupon in the request, include these fields:

   [orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
   :
   Set to `coupon`.

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
   :

   [orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :
   {#klarna-session-cr-task-hop_coupon-rest} {#klarna-session-cr-task-hop_coupon-fields}
   {#klarna-session-cr-task-hop_coupon-fields}

4. Redirect the customer to the URL in the processorInformation.paymentURL response field.

   ```
   "processorInformation": {
           "paymentUrl": "https://pay.playground.klarna.com/na/hpp/payments/2JUV3NC"
   }
   ```
5. When the customer completes the checkout using their Klarna credentials, Klarna redirects the customer to the URL you specified in the merchantInformation.successURL request field. Klarna appends the merchant's success URL with a unique Klarna generated token.

   ```
   https://www.test.com?auth-token=d9b4496b-f4b1-5ad5-bbe0-7f666682126
   ```
6. When you send the authorization request, set the processorInformation.preApprovalToken field to the unique token Klarna appended to the success URL.

   ```
   "processorInformation":{
       "preApprovalToken": "d9b4496b-f4b1-5ad5-bbe0-7f666682126"
   }
   ```

Example: Create a HOP Session {#klarna-session-cr-ex-rest}
==========================================================

Request

```
{
    "merchantInformation": {
    "cancelUrl": "https://www.merchant-cancel-redirect-url.com",
    "successUrl": "https://www.merchant-success-redirect-url.com",
    "failureUrl": "https://www.merchant-failure-redirect-url.com"
  },
    "orderInformation": {
        "billTo": {
            "administrativeArea": "VA",
            "postalCode": "22901",
            "country": "US"
        },
        "amountDetails": {
            "currency": "USD"
        },
        "lineItems": [
            {
                "productName": "Skirt on the sky",
                "unitPrice": "1.00",
                "totalAmount": "1.00"
            }
        ]
    },
    "paymentInformation": {
        "paymentType": {
            "name": "INVOICE",
            "method": {
                "name": "KLARNA"
            }
        }
    },
    "processingInformation": {
        "actionList": "AP_SESSIONS",
        "paymentFlowMode": "HOP",
        "sessionType": "N"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "POST",
            "href": "/pts/v2/payment-references"
        },
        "updateSession": {
            "method": "PATCH",
            "href": "/pts/v2/payment-references/7297155024486439603955"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7297155024486439603955"
        },
        "order": {
            "method": "POST",
            "href": "/pts/v2/payment-references/7297155024486439603955/intents"
        }
    },
    "clientReferenceInformation": {
        "code": "1729715502582"
    },
    "id": "7297155024486439603955",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00000",
        "paymentUrl": "https://pay.playground.klarna.com/na/hpp/payments/23NmehI",
        "responseCode": "00000",
        "token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyMzA1ZWJjLWI4MTEtMzYzNy1hYTRjLTY2ZWNhMTg3NGYzZCJ9.eyJzZXNzaW9uX2lkIjoiYmRiOGU5MGQtNzhiOS02ZWJkLTllZjMtOTNmNWYyN2Q3MmRhIiwiYmFzZV91cmwiOiJodHRwczovL2pzLnBsYXlncm91bmQua2xhcm5hLmNvbS9uYS9rcCIsImRlc2lnbiI6ImtsYXJuYSIsImxhbmd1YWdlIjoiZW4iLCJwdXJjaGFzZV9jb3VudHJ5IjoiVVMiLCJlbnZpcm9ubWVudCI6InBsYXlncm91bmQiLCJtZXJjaGFudF9uYW1lIjoiUGxheWdyb3VuZCBEZW1vIE1lcmNoYW50Iiwic2Vzc2lvbl90eXBlIjoiUEFZTUVOVFMiLCJjbGllbnRfZXZlbnRfYmFzZV91cmwiOiJodHRwczovL25hLnBsYXlncm91bmQua2xhcm5hZXZ0LmNvbSIsInNjaGVtZSI6dHJ1ZSwiZXhwZXJpbWVudHMiOlt7Im5hbWUiOiJrcGMtcHNlbC00NDI5IiwidmFyaWF0ZSI6ImEifSx7Im5hbWUiOiJrcC1jbGllbnQtb25lLXB1cmNoYXNlLWZsb3ciLCJ2YXJpYXRlIjoidmFyaWF0ZS0xIn0seyJuYW1lIjoia3BjLTFrLXNlcnZpY2UiLCJ2YXJpYXRlIjoidmFyaWF0ZS0xIn0seyJuYW1lIjoia3AtY2xpZW50LXV0b3BpYS1zdGF0aWMtd2lkZ2V0IiwidmFyaWF0ZSI6ImluZGV4IiwicGFyYW1ldGVycyI6eyJkeW5hbWljIjoidHJ1ZSJ9fSx7Im5hbWUiOiJrcC1jbGllbnQtdXRvcGlhLWZsb3ciLCJ2YXJpYXRlIjoidmFyaWF0ZS0xIn0seyJuYW1lIjoiaW4tYXBwLXNkay1uZXctaW50ZXJuYWwtYnJvd3NlciIsInBhcmFtZXRlcnMiOnsidmFyaWF0ZV9pZCI6Im5ldy1pbnRlcm5hbC1icm93c2VyLWVuYWJsZSJ9fSx7Im5hbWUiOiJrcC1jbGllbnQtdXRvcGlhLXNkay1mbG93IiwidmFyaWF0ZSI6InZhcmlhdGUtMSJ9LHsibmFtZSI6ImtwLWNsaWVudC11dG9waWEtd2Vidmlldy1mbG93IiwidmFyaWF0ZSI6InZhcmlhdGUtMSJ9LHsibmFtZSI6ImluLWFwcC1zZGstY2FyZC1zY2FubmluZyIsInBhcmFtZXRlcnMiOnsidmFyaWF0ZV9pZCI6ImNhcmQtc2Nhbm5pbmctZW5hYmxlIn19XSwicmVnaW9uIjoidXMiLCJvcmRlcl9hbW91bnQiOjEwMCwib2ZmZXJpbmdfb3B0cyI6Miwib28iOiIxOCIsInZlcnNpb24iOiJ2MS4xMC4wLTE1OTAtZzNlYmMzOTA3In0.Mx5JnoG7Te4IsB3yrxOEVOFnudHvOkd2XJ0EO6w6lBVI0wb2B5oYeh9pESt2EpqP0SYAXmXjNyA2gZ1whrByPhwnoxTVYW74EcdBYYMKlgYZ9JPiUlETYz5wOma_gCXWhQdFKUSopX5ZAL32v_6tDSYSCQt9CbLEyXwx4v-6utKbVH5mhCdaMxfcdzLIRNoZaFpk1CNgb-gu2hXtHm-e4dd8mIEf44xyexl_SZy7cCEUFS3QpmVt7VJtLNJgI6t3kFPSfmW4k2M189UiyDFnK26nE6loXIcGdzsO-pcHs3GhWteqPBvgg2XyQE9d2JFlo5BMHvVMieevI2Ox651t1g"
    },
    "reconciliationId": "XFZ402EJ8ZWO",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-10-23T203147Z"
}
```

Creating an Inline Session {#klarna-session-cr-in-intro}
========================================================

Create a new session whenever the customer displays your checkout page.

Inline Specifications
:
When you send a session request, set the apSessionService_paymentFlowMode field to `inline`. `Cybersource` responds with a pre-approval token in the processorInformation.token field. Set the Klarna widget installed in the merchant website to token. When the customer completes the checkout using the Klarna widget, the widget responds with an authorization token. Include the authorization token in the authorization request to link the authorization to the session.

Klarna Payment Methods
----------------------

When you request the session service, you can determine the Klarna payment method you want to offer your customers. Set the optional paymentInformation.paymentType.method.type request field to a value listed in the Payment Method column.

| Payment Method Field Value |                    Description                     |                                       Klarna Products                                       |
|----------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| `pay_later`                | Customer pays total bill at a set date.            | * Klarna Invoice * Klarna Pay Later * Klarna Pay Later by Card (PLBC)                       |
| `pay_now`                  | Customer pays total bill at the time of checkout.  | * Klarna Direct Bank Transfer * Klarna Direct Debit                                         |
| `pay_over_time`            | Customer pays bill in equal multiple installments. | * Klarna Account * Klarna Financing * Klarna Fixed Installment Plans * Klarna Interest Free |
[Payment Methods]

Example: Payment Methods in Session Request
:

    ```
    {
      "paymentInformation": {
        "paymentType": {
          "method": {
            "type": "pay_later"
          }
        }
      }
    }
    ```

Calculating the Grand Total Amount
----------------------------------

Klarna requires that the grand total amount of a purchase be included in the request using the orderInformation.amountDetails.totalAmount field. The country of the transaction and the use of coupons affect how to calculate the grand total amount.  
For more information about how to calculate the grand total amount, see [Calculating the Grand Total Amount](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-intro-total.md "") in the Reference Information section.

Language Specification {#klarna-session-cr-in-intro_language}
-------------------------------------------------------------

To set the language for your Klarna checkout experience, include the buyerInformation.language field in your request. By not including this field, the Klarna checkout experience is set to English by default. For a list of all possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

Example: Language Specification
:

    ```
    {
      "buyerInformation": {
        "language": "es"
      }
    }
    ```

Line Items
----------

Klarna uses line items when you send a create session and update session requests. [Line items](# "") are used to include information about the goods that your customers purchase, such as product name, quantity, and price.  
Line items are represented in a request as the lineItem\[\] array request fields.  
For more information about how to properly format line items in your request, see [Using Line Items](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-intro-items.md "") in the Reference Information section.

Endpoints
---------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payment-references`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payment-references`

Response Status
---------------

The session service responds with one of these statuses as the status field value:

* `FAILED`: The session request is not successful. Send a new session request.{#klarna-session-cr-in-intro_d11e234}
  {#klarna-session-cr-in-intro_d11e234}

* `INITIATED`: The session is initiated and the customer may now checkout. Send periodic check status requests until the status updates to `COMPLETED`. For more information, see [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").{#klarna-session-cr-in-intro_d11e239}
  {#klarna-session-cr-in-intro_d11e239} {#klarna-session-cr-in-intro_d11e232}  
  When you send a check status request for an initiated session, you can receive one of these statuses when the session updates:

* `ABANDONED`: The customer did not complete the payment using the redirect URL or widget.{#klarna-session-cr-in-intro_d11e255}
  {#klarna-session-cr-in-intro_d11e255}

* `COMPLETED`: The customer completed the checkout process. You can now authorize the funds.{#klarna-session-cr-in-intro_d11e260}
  {#klarna-session-cr-in-intro_d11e260}

Requesting to Create an Inline Session {#klarna-session-cr-task-inl}
====================================================================

Follow these steps to successfully create an inline session.

1. Send a` POST` request to the `https://apitest.cybersource.com/pts/v2/payment-references` endpoint and include these required fields:

   > IMPORTANT Do not send any personally identifiable information (PII) data about the customer in the request to create a session.

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :

   [merchantInformation.cancelUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-cancel-url.md "")
   :

   [merchantInformation.failureUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-failure-url.md "")
   :

   [merchantInformation.successUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-success-url.md "")
   :

   [orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
   :

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   [orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
   :

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
   :

   [orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   paymentInformation.paymentType.method.name
   :
   Set to `KLARNA`.

   paymentInformation.paymentType.method.type
   :

   [paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
   :
   Set to `INVOICE`.

   [processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
   :
   Set to `AP_SESSIONS`.

   processingInformation.paymentFlowMode
   :
   Set to `inline` to display the Klarna widget on your checkout page.

   Non-US Countries
   :   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")

   US
   :
   [orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
   :
   [orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")

2. You can include these optional fields in the request:

   [buyerInformation.language](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-language.md "")
   :
   > IMPORTANT If this field is not included, the language is set to English by default.

   :
   For a list of possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

   [clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
   :

   [orderInformation.amountDetails.discountAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
   :

   [orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
   :

   [orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
   :

   [orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
   :

   [orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
   :

   [orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
   :

   [orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
   :

   orderInformation.lineItems\[\].productCode
   :

   orderInformation.lineItems\[\].productDescription
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :

   orderInformation.lineItems\[\].quantity
   :

   orderInformation.lineItems\[\].taxAmount
   :

   paymentInformation.paymentType.method.type
   :

   paymentInformation.type
   :

   processingInformation.sessionType
   :

3. To include an optional coupon in the request, include these fields:

   [orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
   :
   Set to `coupon`.

   [orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
   :

   [orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
   :

   [orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
   :

   [orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
   :
   {#klarna-session-cr-task-inl_d8e441}

4. Set the Session Token ID in the Klarna widget to the processorInformation.token field value from the session response.

   ```
   IDeyJhbGciOiJSUzI1NiIsImtpZCI6IjgyMzA1ZWJjLWI4MTEtMzYzNy...
   ```
5. When the customer completes the payment using the Klarna widget, the Klarna widget creates a unique authorization token. Store the token for the authorization request.

   ```
   Authorizaiton Token: a6b2229c-665b-5660-a5fe-063bef3d9a1e
   ```
6. When you send the follow-on authorization request, set the processorInformation.preApprovalToken request field to the authorization token value created by the Klarna widget.

   ```
   {
     "processorInformation": {
       "preApprovalToken": "a6b2229c-665b-5660-a5fe-063bef3d9a1e"
     }
   }
   ```

Example: Create an Inline Session {#klarna-session-cr-in-ex-rest}
=================================================================

Request

```
{
    "merchantInformation": {
    "cancelUrl": "https://www.test0.com",
    "successUrl": "https://www.google.com",
    "failureUrl": "https://www.test1.com"
  },
    "orderInformation": {
        "billTo": {
            "firstName": "John",
            "lastName": "Smith",
            "address1": "123 Happy St",
            "locality": "Sunnyville",
            "administrativeArea": "CA",
            "postalCode": "55555",
            "country": "US",
            "email": "test email dot com"
        },
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        },
        "lineItems": [
            {
                "productCode": "A4890B5023",
                "productName": "Skirt on the sky",
                "productSku": "skirtonsky$bluegreen",
                "quantity": "1",
                "unitPrice": "1.00",
                "totalAmount": "1.00",
                "taxAmount": "0.00",
                "productDescription": "Amnesiac Shirt"
            }
        ]
    },
    "paymentInformation": {
        "paymentType": {
            "name": "INVOICE",
            "method": {
                "name": "KLARNA",
                "type": "pay_now"
            }
        }
    },
    "processingInformation": {
        "actionList": "AP_SESSIONS",
        "paymentFlowMode": "inline",
        "sessionType": "N"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "POST",
            "href": "/pts/v2/payment-references"
        },
        "updateSession": {
            "method": "PATCH",
            "href": "/pts/v2/payment-references/7322957972776014303955"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7322957972776014303955"
        },
        "order": {
            "method": "POST",
            "href": "/pts/v2/payment-references/7322957972776014303955/intents"
        }
    },
    "clientReferenceInformation": {
        "code": "1732295797319"
    },
    "id": "7322957972776014303955",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00000",
        "responseCode": "00000",
        "token": "inline_session_token_value"
    },
    "reconciliationId": "XEKSO3R50AFW",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-11-22T171638Z"
}
```

Updating a Session {#klarna-session-up-intro}
=============================================

You can update a session for 48 hours after creating it. The session update service enables you to update items in the cart and customer information, with or without sending customer billing details. However, when you send customer billing details in the session update request, send as many billing details as possible for the best customer checkout experience. For a list of all of the information you can update in a session, see the [Optional Fields for Updating a Session](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-session-up-intro/klarna-session-up-opt-fields.md "").  
Updating a session requires the request ID from the original session, which is in the id response field.  
Only update a session after the customer consents to sharing their data with Klarna.

> IMPORTANT PII data about a customer should be sent only after the customer chooses the Klarna payment option on your checkout page and consents to sharing their data with Klarna.

Klarna Payment Methods
----------------------

When you request the session service, you can determine the Klarna payment method you want to offer your customers. Set the optional paymentInformation.paymentType.method.type request field to a value listed in the Payment Method column.

| Payment Method Field Value |                    Description                     |                                       Klarna Products                                       |
|----------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| `pay_later`                | Customer pays total bill at a set date.            | * Klarna Invoice * Klarna Pay Later * Klarna Pay Later by Card (PLBC)                       |
| `pay_now`                  | Customer pays total bill at the time of checkout.  | * Klarna Direct Bank Transfer * Klarna Direct Debit                                         |
| `pay_over_time`            | Customer pays bill in equal multiple installments. | * Klarna Account * Klarna Financing * Klarna Fixed Installment Plans * Klarna Interest Free |
[Payment Methods]

Example: Payment Methods in Session Request
:

    ```
    {
      "paymentInformation": {
        "paymentType": {
          "method": {
            "type": "pay_later"
          }
        }
      }
    }
    ```

Language Specification
----------------------

To set the language for your Klarna checkout experience, include the buyerInformation.language field in your request. By not including this field, the Klarna checkout experience is set to English by default. For a list of all possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

Example: Language Specification
:

    ```
    {
      "buyerInformation": {
        "language": "es"
      }
    }
    ```

Endpoints
---------

Send a PATCH request to one of these endpoints:  
**Production:** `PATCH ``https://api.cybersource.com``/pts/v2/payment-references/`*{id}*  
**Test:** `PATCH ``https://apitest.cybersource.com``/pts/v2/payment-references/`*{id}*  
Set the *{id}* to the request ID contained in the original session response.

Response Status
---------------

The session service responds with one of these statuses as the field value:

* `INITIATED`: The session is initiated and the customer may now checkout.
* `COMPLETED`: The customer completed the checkout process.  
  The session service also responds with a reason code as the field value. For more information about reason codes, see the .

Response Statuses
-----------------

The session service responds with one of these statuses as the field value:

* `COMPLETED`: The customer completed the checkout process.
* `INITIATED`: The session is initiated and the customer may now checkout.
  {#klarna-session-up-intro_ul_gjc_lsn_jyb}  
  The session service also responds with a reason code as the field value. For more information about reason codes, see the .

Required Fields for Updating a Session {#klarna-session-up-req-fields}
======================================================================

[merchantInformation.cancelUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-cancel-url.md "")
:

[merchantInformation.failureUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-failure-url.md "")
:

[merchantInformation.successUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-success-url.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

orderInformation.billTo.postalCode
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_SESSIONS`.

processingInformation.paymentFlowMode
:
Set to one of these possible values:
:
* `HOP`
* `inline`

processingInformation.sessionType
:
Set to `U`.

Country-Specific Fields {#klarna-session-up-req-fields_country-fields}
----------------------------------------------------------------------

Non-US Countries
:   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")

US
:
[orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
:
[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")

Coupon Fields {#klarna-coupon-fields}
=====================================

To include a coupon in your request, include these fields.

[orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
:
Set to `coupon`.

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Optional Fields for Updating a Session {#klarna-session-up-opt-fields}
======================================================================

These are the optional fields you can include to update an existing session.

[buyerInformation.language](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-language.md "")
:
> IMPORTANT If this field is not included, the language is set to English by default.

:
For a list of possible values, see the [*ISO Standard Language Codes*](https://developer.cybersource.com/docs/cybs/en-us/language-codes/reference/all/na/language-codes/language-codes.md "") guide.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.amountDetails.discountAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-discount-amount.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.district](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-district.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

orderInformation.lineItems.productCode
:

orderInformation.lineItems.productDescription
:

orderInformation.lineItems.productSku
:

orderInformation.lineItems.quantity
:

orderInformation.lineItems.taxAmount
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street2.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.district](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-district.md "")
:

[orderInformation.shipTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-email.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

paymentInformation.type
:

Example: Update a Session {#klarna-session-up-ex-rest}
======================================================

Request

```
{
    "merchantInformation": {
    "cancelUrl": "https://www.test0.com",
    "successUrl": "https://www.google.com",
    "failureUrl": "https://www.test1.com"
  },
    "orderInformation": {
        "billTo": {
            "administrativeArea": "CA",
            "postalCode": "22901",
            "country": "US"
        },
        "amountDetails": {
            "currency": "USD"
        },
        "lineItems": [
            {
                "productName": "Skirt on the sky",
                "unitPrice": "2.00",
                "totalAmount": "2.00"
            }
        ]
    },
    "paymentInformation": {
        "paymentType": {
            "name": "INVOICE",
            "method": {
                "name": "KLARNA"
            }
        }
    },
    "processingInformation": {
        "actionList": "AP_SESSIONS",
        "paymentFlowMode": "HOP",
        "sessionType": "U"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "POST",
            "href": "/pts/v2/payment-references"
        },
        "updateSession": {
            "method": "PATCH",
            "href": "/pts/v2/payment-references/7303027715656351504951"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7303027715656351504951"
        },
        "order": {
            "method": "POST",
            "href": "/pts/v2/payment-references/7303027715656351504951/intents"
        }
    },
    "clientReferenceInformation": {
        "code": "1730302771619"
    },
    "id": "7303027715656351504951",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "2.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00000",
        "paymentUrl": "https://pay.playground.klarna.com/na/hpp/payments/2BUwyUw",
        "responseCode": "00000",
    },
    "reconciliationId": "XFZ3Y2N91JHR",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-10-30T153932Z"
}
```

Authorize a Payment {#klarna-auth-intro}
========================================

Authorizing a purchase requires the Klarna generated token from a completed session creation. Set the processorInformation.preApprovalToken request field value to the token value. Where you retrieve the token is dependent on whether you created a HOP session or inline session. If you created a HOP session, the token is appended to the success URL the customer is redirected to after completing the checkout using their Klarna account. If you created an inline session, the token is generated by the Klarna widget when the customer completes the checkout.  
After authorizing a payment, you can capture the authorization for up to 28 days.

Merchant-Defined Data {#klarna-auth-intro_merchant-defined-data}
----------------------------------------------------------------

Merchant-defined data is included in the merchantDefinedData_mddField_5 field.

> IMPORTANT
> This field has replaced the merchantDefinedData_field5 field. If you submit a request with the merchantDefinedData_field5 field, ` Cybersource ` automatically replaces the field with merchantDefinedData_mddField_5 .
> WARNING
> You are prohibited from including personally identifying information (PII) in the merchantDefinedData fields for the purposes of capturing, obtaining, and/or transmitting any PII. PII includes, but is not limited to, address, credit card number, social security number, driver's license, state-issued identification number, passport number, and card verification number (CVV, CVC2, CVV2, CID, CVN). In the event ` Cybersource ` discovers you are capturing and/or transmitting PII in the merchantDefinedData fields, whether or not intentionally, ` Cybersource ` immediately suspends your merchant account, which results in a rejection of any and all transaction requests submitted by the merchant account after the point of suspension.

Endpoints {#klarna-auth-intro_section_acs_kfm_lyb}
--------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`

Response Status
---------------

The authorization service responds with one of these statuses as the status field value:

* `FAILED`: The authorization request is not successful. Send a new authorization request. A failed request can be due to either Klarna rejecting the transaction or a technical error.{#klarna-auth-intro_status-failed}
  {#klarna-auth-intro_status-failed}
* `AUTHORIZED`: The customer's funds are authorized. You can now capture the authorized amount.{#klarna-auth-intro_status-pending}
  {#klarna-auth-intro_status-pending}

{#klarna-auth-intro_auth-statuses}  
When you send a check status request for a pending authorization, you can receive this status when the authorization updates:

* `AUTHORIZED`: The customer's funds are authorized. You can now capture the authorized amount.{#klarna-auth-intro_status-authorized}
  {#klarna-auth-intro_status-authorized}

Required Fields for an Authorization {#klarna-auth-req-fields}
==============================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_AUTH`.

[processorInformation.preApprovalToken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processor-info-aa/processor-info-pre-approval-token.md "")
:
Set to the token value created by Klarna.
:
If you created a HOP session, the token is appended to the merchant success URL.
:
If you created an inline session, the token is generated by the Klarna widget.

Country-Specific Fields
-----------------------

Non-US Countries
:   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")

US
:
[orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
:
[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")

Optional Fields for an Authorization {#klarna-auth-opt-fields}
==============================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[merchantDefinedInformation\[\].key](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-defined-info-aa/merch-defined-info-key.md "")
:

merchantDefinedInformation\[\].value
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

orderInformation.billTo.city
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
:
Set to `coupon`.

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

orderInformation.shipTo.city
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

Example: Authorizing a Payment {#klarna-auth-ex-rest}
=====================================================

Request

```
{
  "orderInformation": {
    "billTo": {
      "administrativeArea": "TX",
      "postalCode": "78757",
      "country": "US"
    },
    "amountDetails": {
      "totalAmount": "1.00",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "name": "INVOICE",
      "method": {
        "name": "KLARNA"
      }
    }
  },
  "processingInformation": {
    "actionList": "AP_AUTH"
  },
  "processorInformation":{
      "preApprovalToken": "87b09e60-4e34-69c6-9bea-906516cdec18"
  }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7297199754036380503955/reversals"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7297199754036380503955/captures"
        },
        "self": {
            "method": "POST",
            "href": "/pts/v2/payments/7297199754036380503955"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7297199754036380503955"
        }
    },
    "clientReferenceInformation": {
        "code": "1729717123388"
    },
    "id": "7297199754036380503955",
    "orderInformation": {
        "invoiceDetails": {
            "productId": "paylaterbycard"
        },
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00003",
        "transactionId": "dfcf1b24-311d-4e10-9be9-3b5f371bbe23",
        "responseCode": "00003"
    },
    "reconciliationId": "XFZ402EJ8ZWS",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-10-23T20:58:47Z"
}
```

Update an Authorized Payment {#klarna-auth-fo-intro}
====================================================

Successfully processed authorizations can be updated as follow-on authorizations before you capture or reverse the payment. Follow-on authorizations enable you to update the billing, shipping, itemization, and item break up information of already submitted orders. When updating an authorization, set the processingInformation.linkId field to the id field value from the original authorization response in order to link your request to the original authorization.

Endpoints {#klarna-auth-fo-intro_section_acs_kfm_lyb}
-----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`

Response Status
---------------

The authorization service responds with one of these statuses as the status field value:

* `AUTHORIZED`: The payment is successfully authorized.
* `FAILED`: The authorization request failed.
* `PENDING`: The authorization request is accepted but is not authorized. Request the check status service to retrieve status updates. For more information, see [Check Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").

{#klarna-auth-fo-intro_ul_gyh_p5y_byb}  
The authorization service also responds with a reason code as the field value. For more information about reason codes, see the .

Required Fields for Updating an Authorization {#klarna-auth-fo-req-fields}
==========================================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_AUTH`.

[processingInformation.linkId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-link-id.md "")
:
Set to the id field value from the initial authorization response.

[processorInformation.preApprovalToken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processor-info-aa/processor-info-pre-approval-token.md "")
:
Set to the token generated by Klarna.

Country-Specific Fields
-----------------------

Include these country-specific field in addition to the required fields listed above.

Non-US Countries
:   [orderInformation.lineItems\[\].taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-tax-amount-request.md "")

US
:
[orderInformation.amountDetails.taxAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-tax-amount.md "")
:
[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")

Optional Fields for Updating an Authorization {#klarna-auth-follow-optional-fields}
===================================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[merchantDefinedInformation\[\].key](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-defined-info-aa/merch-defined-info-key.md "")
:

merchantDefinedInformation\[\].value
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

orderInformation.billTo.city
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
:
Set to `coupon`.

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

orderInformation.shipTo.city
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

Example: Updating an Authorized Payment {#klarna-auth-fo-ex-rest}
=================================================================

Request

```
{
  "orderInformation": {
    "billTo": {
      "administrativeArea": "TX",
      "postalCode": "78757",
      "country": "US"
    },
    "amountDetails": {
      "totalAmount": "1.00",
      "currency": "USD"
    }
  },
  "paymentInformation": {
    "paymentType": {
      "name": "INVOICE",
      "method": {
        "name": "KLARNA"
      }
    }
  },
  "processingInformation": {
    "actionList": "AP_AUTH",
    "linkId": "7304002418446743104951"
  },
  "processorInformation":{
      "preApprovalToken": "abb1c505-6862-64f8-9bea-df68d3fbe397"
  }
}
```

Response to a Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7304003239726834704953/reversals"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7304003239726834704953/captures"
        },
        "self": {
            "method": "POST",
            "href": "/pts/v2/payments/7304003239726834704953"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7304003239726834704953"
        }
    },
    "clientReferenceInformation": {
        "code": "1730400324002"
    },
    "id": "7304003239726834704953",
    "orderInformation": {
        "invoiceDetails": {
            "productId": "paylaterbycard"
        },
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00003",
        "transactionId": "778a6b5f-48cb-43dc-b684-68d2540524c2",
        "responseCode": "00003"
    },
    "reconciliationId": "XFZ552N8J2WJ",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2024-10-31T18:45:25Z"
}
```

Reverse an Authorized Payment {#klarna-reversal-intro}
======================================================

The authorization reversal service enables you to reverse the amount that was authorized. To reverse an authorization, you must have the authorization request ID, which is the id field value from the authorization response. To reverse a follow-on authorization, use the request ID from the follow-on authorization response.

Endpoints {#klarna-reversal-intro_section_kcb_snm_lyb}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/reversals`  
Set the *`{id}`* to the request ID returned in the authorization request.

Response Status
---------------

The authorization reversal service responds with one of these statuses as the status field value:

* `PENDING`: The authorization reversal request is successful and is currently processing. Send periodic check status requests until you receive an updated status. For more information, see [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").{#klarna-reversal-intro_status-pending}
  {#klarna-reversal-intro_status-pending}
* `FAILED`: The authorization reversal is not successful. Send a new request. A failed request can be due to either Klarna rejecting the transaction or a technical error.{#klarna-reversal-intro_status-failed}
  {#klarna-reversal-intro_status-failed}

When you send a check status request for a pending authorization reversal, you can receive this status when the authorization reversal updates:

* `AUTH_REVERSED`: The authorization is successfully reversed.{#klarna-reversal-intro_status-reversed}
  {#klarna-reversal-intro_status-reversed}

Required Fields for Authorization Reversal {#klarna-reversal-req-fields}
========================================================================

Include these required fields to reverse an authorization.

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_AUTH_REVERSAL`

Optional Field for Authorization Reversal {#klarna-reversal-opt-fields}
=======================================================================

Example: Reversing an Authorization {#klarna-reversal-ex-rest}
==============================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "name": "INVOICE",
      "method": {
        "name": "KLARNA"
      }
    }
  },
  "processingInformation": {
    "actionList": "AP_AUTH_REVERSAL"
  }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "POST",
            "href": "/pts/v2/reversals/7297199754036380503955"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7297199754036380503955"
        }
    },
    "clientReferenceInformation": {
        "code": "refnum-1234"
    },
    "id": "7291980786556590303955",
    "processorInformation": {
        "responseDetails": "00007",
        "responseCode": "00007"
    },
    "reconciliationId": "XFZ3Z2EJC1OZ",
    "reversalAmountDetails": {
        "reversedAmount": "0"
    },
    "status": "AUTH_REVERSED",
    "submitTimeUtc": "2024-10-21T17:37:52Z"
}
```

Capture a Payment {#klarna-capture-intro}
=========================================

The capture service enables you to capture the entire authorized amount or part of the authorized amount. Klarna supports multiple capture requests when the total amount of all captures is less than the authorized amount.  
You can capture an authorization for up to 28 days after a payment is authorized.

Endpoints {#klarna-capture-intro_section_pg4_mfm_lyb}
-----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`  
Set the *`{id}`* to the request ID contained in the authorization response.

Response Statuses
-----------------

The capture service responds with one of these statuses as the status response field value:

* `FAILED`: The capture request is not successful. Send a new capture request. A failed request can be due to either Klarna rejecting the transaction or a technical error.{#klarna-capture-intro_status-failed}
  {#klarna-capture-intro_status-failed}

* `PENDING`: The capture request is accepted but is not captured. Request the check status service to retrieve status updates. For more information, see Check Status.{#klarna-capture-intro_status-pending}
  {#klarna-capture-intro_status-pending} {#klarna-capture-intro_ul_pv2_n2z_byb}  
  When you send a check status request for a pending capture, you can receive this status when the status updates:

* `CHARGEBACK`: The customer submitted a payment dispute for the purchase, and Klarna reviewed and approved a chargeback to the customer. For more information about chargebacks, see [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "").{#klarna-capture-intro_status-chargeback}
  {#klarna-capture-intro_status-chargeback}

* `SETTLED`: The capture request is settled for the requested amount.{#klarna-capture-intro_status-settled}
  {#klarna-capture-intro_status-settled}

Required Fields for a Capture {#klarna-capture-req-fields}
==========================================================

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_CAPTURE`.

Optional Fields for a Capture {#klarna-capture-opt-fields}
==========================================================

Choose from these optional fields to include additional information when capturing a payment.

clientReferenceInformation.code
:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

Example: Capture a Payment {#klarna-capture-ex-rest}
====================================================

Request

```
{
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "paymentInformation": {
        "paymentType": {
            "name": "INVOICE",
            "method": {
                "name": "KLARNA"
            }
        }
    },
    "processingInformation": {
        "actionList": "AP_CAPTURE"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "POST",
            "href": "/pts/v2/captures/7297199754036380503955"
        },
        "refund": {
            "method": "POST",
            "href": "/pts/v2/captures/7297199754036380503955/refunds"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7297199754036380503955"
        }
    },
    "clientReferenceInformation": {
        "code": "1729719300233"
    },
    "id": "7297199754036380503955",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "1.00",
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00004",
        "responseCode": "00004"
    },
    "reconciliationId": "XFZ3Y2EH1X26",
    "status": "SETTLED",
    "submitTimeUtc": "2024-10-23T21:35:04Z"
}
```

Refund a Payment {#klarna-refund-intro}
=======================================

Refunding a payment returns the entire captured amount or part of the captured amount to the customer's account. Klarna supports multiple refund requests when the total amount of all refunds is less than the captured amount.'  
`Cybersource` recommends using the optional fields for a refund to ensure the request is successful. For more information, see [Optional Fields for a Refund](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-refund-intro/klarna-refund-opt-fields.md "").

Endpoints {#klarna-refund-intro_section_tw1_4fm_lyb}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#klarna-refund-intro_d20e372}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/refunds`{#klarna-refund-intro_d20e385}  
The *{id}* is the request ID contained in the original transaction request.

Response Statuses {#klarna-refund-intro_section_uxl_fpm_lyb}
------------------------------------------------------------

The refund service responds with one of these statuses as the status field value:

* `FAILED`: The refund request is not successful. Send a new refund request. A failed request can be due to either Klarna rejecting the transaction or a technical error.{#klarna-refund-intro_status-failed}
  {#klarna-refund-intro_status-failed}
* `PENDING`: The refund request is accepted but is not refunded. Request the check status service to retrieve status updates. For more information, see [Check a Request Status](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-services/klarna-status-intro.md "").
* `REFUNDED`: The captured payment is successfully refunded.{#klarna-refund-intro_status-refunded}
  {#klarna-refund-intro_status-refunded}

{#klarna-refund-intro_ul_chy_fz1_cyb}  
The refund service also responds with a reason code as the field value. For more information about reason codes, see the .

Required Fields for a Refund {#klarna-refund-req-fields}
========================================================

Include these required fields to refund a payment.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_REFUND`.

Optional Fields for a Refund {#klarna-refund-opt-fields}
========================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[merchantDefinedInformation\[\].key](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-defined-info-aa/merch-defined-info-key.md "")
:

merchantDefinedInformation\[\].value
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

orderInformation.billTo.city
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderInformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.lineItems\[\].productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-code.md "")
:
Set to `coupon`.

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-street1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:

orderInformation.shipTo.city
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-last-name.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

Example: Issuing a Refund {#klarna-refund-ex-rest}
==================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "name": "INVOICE",
      "method": {
        "name": "KLARNA"
      }
    }
  },
  "processingInformation": {
    "actionList": "AP_REFUND"
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "1.00",
      "currency": "USD"
    }
  }
}
```

Response to a Successful Request

```
{
    "_links": {
        "self": {
            "method": "GET",
            "href": "/pts/v2/refunds/7297199754036380503955"
        },
        "status": {
            "method": "POST",
            "href": "/pts/v2/refresh-payment-status/7297199754036380503955"
        }
    },
    "clientReferenceInformation": {
        "code": "refnum-1234",
        "returnReconciliationId": "XZCJ2230ILKT"
    },
    "id": "7297199754036380503955",
    "orderInformation": {
        "amountDetails": {
            "currency": "USD"
        }
    },
    "processorInformation": {
        "responseDetails": "00006",
        "transactionId": "7ee251a9-6b9b-4f32-b486-30223db781cf",
        "responseCode": "00006"
    },
    "reconciliationId": "XFZ552EH3ISS",
    "refundAmountDetails": {
        "refundAmount": "1.00"
    },
    "status": "REFUNDED",
    "submitTimeUtc": "2024-10-21T17:06:50Z"
}
```

Check a Request Status {#klarna-status-intro}
=============================================

Request the check status service when the authorization response status is `PENDING`. A pending status occurs when Klarna reviews an authorization. `Cybersource` recommends that you request the check status service hourly until the payment status changes.

Endpoints {#klarna-status-intro_section_w15_rkm_lyb}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#klarna-status-intro_d20e193}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/refresh-payment-status/`*{id}*{#klarna-status-intro_d20e205}  
Set the *`{id}`* to the request ID of the API service you are retrieving.

Response Statuses {#klarna-status-intro_section_in3_2pm_lyb}
------------------------------------------------------------

The check status service responds with one of these statuses in the status field value:

Session
:
* `ABANDONED`: The customer did not complete the payment using the redirect URL or widget.
* `COMPLETED`: The customer completed the checkout process. You can now authorize the funds.
{#klarna-status-intro_status-session-list}

Authorization
:
* `AUTHORIZED`: The customer's funds are authorized. You can now capture the authorized amount.
* `FAILED`: The authorization request is not successful. Send a new authorization request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
{#klarna-status-intro_status-auth-list}

Authorization Reversal
:
* `AUTH_REVERSED`: The authorization is successfully reversed.
* `FAILED`: The authorization reversal is not successful. Send a new request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
{#klarna-status-intro_status-reversal-list}

Capture
:
* `CHARGEBACK`: The customer submitted a payment dispute for the purchase, and Klarna reviewed and approved a chargeback to the customer. For more information about chargebacks, see [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "").
* `FAILED`: The capture request is not successful. Send a new capture request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
* `SETTLED`: The capture request is settled for the requested amount.
{#klarna-status-intro_status-capture-list}

Refund
:
* `FAILED`: The refund request is not successful. Send a new refund request. A failed request can be due to either Klarna rejecting the transaction or a technical error.
* `REFUNDED`: The captured payment is successfully refunded.
{#klarna-status-intro_status-refund-list}

Required Fields for Check Status {#klarna-status-req-fields}
============================================================

[paymentInformation.paymentType.method.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-method-name.md "")
:
Set to `KLARNA`.

[paymentInformation.paymentType.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-payment-type-name.md "")
:
Set to `INVOICE`.

[processingInformation.actionList](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-action-list.md "")
:
Set to `AP_STATUS`.

Optional Field for Check Status {#klarna-status-optional-fields}
================================================================

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

`REST` Example: Request a Check Status {#klarna-status-ex-rest}
===============================================================

Request

```
{
  "paymentInformation": {
    "paymentType": {
      "name": "INVOICE",
      "method": {
        "name": "KLARNA"
      }
    }
  },
  "processingInformation": {
    "actionList": "AP_STATUS"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "1729719975533"
    },
    "id": "7297199754036380503955",
    "processorInformation": {
        "responseCode": "00003"
    },
    "reconciliationId": "XFZ3Y2EH1X28",
    "status": "AUTHORIZED"
}
```

Reference Information {#klarna-reference-info}
==============================================

This section contains reference information that is useful when integrating Klarna.

* [Klarna Chargebacks](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/klarna-reference-info-chargeback.md "")
* [Generating Reports In the Business Center](/docs/cybs/en-us/klarna/developer/all/rest/klarna/klarna-reference-info/conref-altpay-reporting.md "")

Calculating the Grand Total Amount {#klarna-intro-total}
========================================================

Klarna requires that the grand total amount of a purchase be included in the request using the orderInformation.amountDetails.totalAmount field. The country of the transaction and the use of coupons affect how to calculate the grand total amount.

US Grand Total with Coupons
---------------------------

To calculate the grand total amount for US transactions with coupons, use this formula:
sum of (unit price x quantity) for all items + item-level tax amount -- sum of (**coupon** amount x quantity) for all items -- item-level discount amount  
This is the same formula with the respective API fields:
sum of (orderInformation.lineItems\[\].unitPrice x orderInformation.lineItems\[\].quantity) for all items + orderInformation.amountDetails.taxAmount -- sum of coupons (orderInformation.lineItems\[\].unitPrice x orderInformation.lineItems\[\].quantity) -- orderInformation.amountDetails.discountAmount US Grand Total Amount with Coupons  
This example shows the proper syntax and calculation of a grand total amount within an API request.

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

US Grand Total without Coupons
------------------------------

To calculate the grand total amount for US transactions without coupons, use this formula:
sum of (unit price x quantity) for all items + item-level tax amount -- item-level discount amount  
This is the same formula with the respective API fields:
sum of (orderInformation.lineItems\[\].unitPrice x orderInformation.lineItems\[\].quantity) for all items + orderInformation.amountDetails.taxAmount -- orderInformation.amountDetails.discountAmount Grand Total Amount  
This example shows the proper syntax and calculation of a grand total amount within an API request.

```
{
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "135",
      "discountAmount": "30",
      "taxAmount": "15"
    },
    "lineItems": [
      {
        "quantity": "4",
        "unitPrice": "25",
        "totalAmount": "100"
      },
      {
        "quantity": "5",
        "unitPrice": "10",
        "totalAmount": "50"
      }
    ]
  }
}
```

Non-US Countries Grand Total with Coupons
-----------------------------------------

To calculate the grand total amount for non-US transactions with coupons, use this formula:
sum of (unit price x quantity) for all items + sum of (item-level tax amount) for all items -- sum of (coupon amount x quantity) for all items -- item-level discount amount  
This is the same formula with the respective API fields:
sum of (orderInformation.lineItems\[\].quantity) for all items + sum of (orderInformation.amountDetails.taxAmount) for all items -- sum of coupons (orderInformation.lineItems\[\].unitPrice x orderInformation.lineItems\[\].quantity) for all items -- orderInformation.amountDetails.discountAmount Grand Total Amount  
This example shows the proper syntax and calculation of a grand total amount within an API request.

```
{
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "135",
      "discountAmount": "30"
    },
    "lineItems": [
      {
        "quantity": "4",
        "unitPrice": "25",
        "totalAmount": "110",
        "taxAmount": "10"
      },
      {
        "quantity": "5",
        "unitPrice": "10",
        "totalAmount": "54",
        "taxAmount": "5"
      }
    ]
  }
}
```

Non-US Countries Grand Total without Coupons
--------------------------------------------

To calculate the grand total amount for non-US transactions without coupons, use this formula:
sum of (unit price x quantity) for all items + sum of (item-level tax amount) for all items -- item-level discount amount  
This is the same formula with the respective API fields:
sum of (orderInformation.lineItems\[\].quantity) for all items + sum of (orderInformation.amountDetails.taxAmount) for all items Grand Total Amount  
This example shows the proper syntax and calculation of a grand total amount within an API request.

```
{
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "165"
    },
    "lineItems": [
      {
        "quantity": "4",
        "unitPrice": "25",
        "totalAmount": "110",
        "taxAmount": "10"
      },
      {
        "quantity": "5",
        "unitPrice": "10",
        "totalAmount": "55",
        "taxAmount": "5"
      }
    ]
  }
}
```

Using Line Items {#klarna-intro-items}
======================================

Klarna uses line items when you send a create session and update session requests. [Line items](# "") are used to include information about the goods that your customers purchase, such as product name, quantity, and price.  
Line items are represented in a request as the lineItem\[\] array request fields.  
These fields are required for each line item that you use:

[orderInformation.lineItems\[\].productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems\[\].unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:
Including Line Items in a Service Request  
This example shows three valid line items.

```
{
  "orderInformation": {
    "lineItems": [
      {
        "productName": "Shirt",
        "unitPrice": "30.00",
        "totalAmount": "60.00"
      },
      {
        "productName": "Pants",
        "unitPrice": "19.99",
        "totalAmount": "19.99"
      },
      {
        "productName": "Dress",
        "unitPrice": "25.00",
        "totalAmount": "75.00"
      }
    ]
  }
}
```

Klarna Chargebacks {#klarna-reference-info-chargeback}
======================================================

Customers can file payment disputes directly to Klarna to receive a chargeback payment for the disputed amount.

Eligibility
:
Only captured payments that are in the settled status can be issued a chargeback.

Results
:
If Klarna approves the customer's payment dispute, you are charged for the disputed amount and a chargeback fee. These charges are deducted from your next settlement and the invoice will document the chargeback details. The disputed payment amount is issued to the customer by Klarna.

If Klarna does not approve the customer's payment dispute, you are charged for any fees associated with the dispute.

> IMPORTANT
> ` Cybersource ` is not involved with the payment dispute review process. All payment disputes are handled between the customer and Klarna.

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
