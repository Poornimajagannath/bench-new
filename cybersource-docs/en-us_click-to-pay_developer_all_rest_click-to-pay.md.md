`Click to Pay Drop-In UI` Developer Guide {#ctp-about-guide}
============================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This document is written for merchants who want to enable the `Click to Pay Drop-In UI` so that they can accept and manual card entry payments on their e-commerce page.

Conventions
:
This statement is used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

Customer Support
:
For support information about any service, visit the Support Center:

<http://support.cybersource.com>

Recent Revisions to This Document {#cp-doc-revisions}
=====================================================

26.05.01 {#cp-doc-revisions_section_x5n_whk_cjc}
------------------------------------------------

Added global support for clientVersion `1.0`.  
Updated Relay `Click to Pay` test cards. See [Test Payment Details](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-testing-intro/ctp-reference-test-cards.md "").  
Added information about handling errors. See [Handle Errors](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-testing-intro/ctp-handle-errors.md "").  
Added information about enabling `Click to Pay Drop-In UI` using the API. See [Enabling Click to Pay Drop-In UI Using the API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-getting-started-integration-flow/ctp-enable-digital-pay-intro/boarding-click-to-pay-enable-intro.md "") and [Enable Click to Pay Customer Authentication Using the API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication/boarding-click-to-pay-auth-enable-intro.md "").  
Added information about adding `Click to Pay` to a merchant account. See [Add Click to Pay to a Merchant Account](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-getting-started-integration-flow/boarding-config-ctp-boarding.md "").  
Updated the `Click to Pay` workflow. See [Click to Pay Customer Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication.md "").

26.01.01
--------

Added endpoints for Kingdom of Saudi Arabia. See these topics:

* [Requesting the Capture Context Using the Sessions API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context/ctp-setup-capture-context-intro.md "")
* [Validating the Capture Context](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context/uc-validate-capture-context-intro.md "")
* [Payment Details API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-details.md "")
* [Payment Credentials API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-credentials.md "")

25.12.01
--------

Introduction to the `Click to Pay Drop-In UI`
:
Added information about supported browsers. See [Introduction to the Click to Pay Drop-In UI](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-intro.md "").

Client-Side Setup
:
Removed reference to the complete mandate from JavaScript Examples. See [JavaScript Example: Setting Up with Full Sidebar](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-button-widget-intro/ctp-getting-started-button-widget-sidebar.md "") and [JavaScript Example: Setting Up with the Embedded Component](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-button-widget-intro/ctp-getting-started-button-widget-embedded.md "").

Capture Context
:
Added support for the removal of the confirm and continue screen and mobile as identity for `Click to Pay`. See [Features](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context/ctp-capture-context-features.md "").
:
Added support for up to clientVersion `0.34`. See [Client Version History](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-capture-context-versions.md "").

Transient Tokens
:
Updated the transient token payload and added an EPC token. See [Example: Transient Token Format](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-tokens-intro/ctp-tokens-format/ctp-trans-tkn-ex.md "").
:
Added a decrypted EPC token example for retrieving payment credentials. See [Payment Credentials API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-credentials.md "").

JavaScript API Reference
:
Added the JavaScript API reference. See [JavaScript API Reference](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-appendix-js-reference.md "").

`Unified Checkout` Configuration
:
Updated the steps for configuring customer authentication for Relay `Click to Pay`. See [Click to Pay Customer Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication.md "").

Test Your `Click to Pay` Configuration
:
Updated the test cards for testing authentication. See [Test Payment Details](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-testing-intro/ctp-reference-test-cards.md "").

25.10.02
--------

Capture Context
:
Added support for clientVersion `0.30`. See [Client Version History](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-capture-context-versions.md "").

25.10.01
--------

Capture Context
:
Updated the clientVersion field value to `0.30` in examples.

`Click to Pay` Appendix
:
Added missing reason codes. See [Reason Codes](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-reason-codes.md "").

25.09.01
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

Introduction to the `Click to Pay Drop-In UI` {#ctp-intro}
==========================================================

`Click to Pay Drop-In UI` powered by `Unified Checkout` provides an interface for easy acceptance of `Click to Pay` payments from Relay, Mastercard, and American Express cards. The `Click to Pay Drop-In UI` handles manual card entry for the non-`Click to Pay` payment schemes called out in this guide. Throughout this guide we refer to both *`Click to Pay Drop-In UI`* and *`Unified Checkout`.*  
`Click to Pay Drop-In UI` consists of a set of server-side APIs and a client-side JavaScript library.  
The server-side APIs authenticate your merchant identity, instruct the system to act within your payment environment, and provide a way to retrieve the payment data following a successful `Click to Pay Drop-In UI` interaction.  
The provided JavaScript library enables you to place a payment application within your e-commerce environment. This embedded component offers `Click to Pay` and card entry to your customers.  
Whether a customer uses a stored `Click to Pay` card or enters their payment information manually, the `Click to Pay Drop-In UI` handles all user interactions and provides a response to your e-commerce system. All UI / UX must follow the UI/UX guidelines. For information about configuring your UI/UX, see [Click to Pay UI Examples](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-ui-screens/ctp-appendix-ui-ux-ex.md "").  
The `Click to Pay Drop-In UI` enables a portfolio to receive an encrypted payload and send a request to the API to retrieve the payment details. The format of the decrypted payment details are determined by the transaction type. The details are either a network token and cryptogram or the PAN, expiration details, and card verification value (CVV).  
The figures below shows the `Click to Pay Drop-In UI` for a recognized user.

#### Figure: {#ctp-intro_fig1}

`Unified Checkout` UI with Card Payment Button  
![Example of the payment application with Click to Pay.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-mobile-ui-400x475.svg/jcr:content/renditions/original)

#### Figure: {#ctp-intro_fig_dwv_t41_3jc}

`Unified Checkout` UI without Card Payment Button ![Example of the trigger component of Click to Pay.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

> IMPORTANT
> Each request that you send to ` Cybersource ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Firefox 121
* GoogleChrome/Chium‑based browsers 118
* MicrosoftEdge 118
* Safari16

`Click to Pay` Customer Workflows {#ctp-walkthrough-intro}
==========================================================

This section provides an overview of the `Click to Pay Drop-In UI` user experience. The `Click to Pay Drop-In UI` is designed to provide customers with a friction-free payment experience across many payment experiences. The user experience has been optimized for mobile use and performs equally well on mobile and desktop devices. `Click to Pay` recognizes customers as follows:
* The customer is a recognized `Click to Pay` customer.

* The customer is not recognized but is a `Click to Pay` customer.

* The customer is a guest at checkout.  
  These workflows show you the pages a customer encounters based on their status:

* [Recognized Click to Pay Customer](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-recognized.md "")

* [Unrecognized Click to Pay Customer](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-unrecognized.md "")

* [Guest Customer](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-intro/ctp-walkthrough-intro/ctp-walkthrough-guest.md "")

Recognized `Click to Pay` Customer {#ctp-walkthrough-recognized}
================================================================

This section provides an overview of the `Click to Pay Drop-In UI` recognized experience. This interaction occurs when a customer's device is recognized by the `Click to Pay Drop-In UI`.  
A customer's device is recognized under these conditions:

* When the customer has used `Click to Pay` on their device through any `Click to Pay` channel.
* If the customer chose to have their device remembered during a previous transaction or when they enter their one-time password (OTP).
  The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#ctp-walkthrough-recognized_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer {#ctp-walkthrough-unrecognized}
====================================================================

This section provides an overview of the `Click to Pay Drop-In UI` unrecognized experience. This interaction occurs when a customer's device is not recognized by the `Click to Pay Drop-In UI`. This condition occurs when the customer has a `Click to Pay` account but has not opted to have their details stored on the device. In this flow, the customer receives an OTP on their registered mobile device or their email address. The OTP can be received from any of the supported card networks, but will return cards that are stored in `Click to Pay` across all of the user's supported card networks. A Relay cardholder will receive an OTP to their registered email address and phone number to authenticate their identity. A Mastercard cardholder will receive an OTP on their registered phone number. After the user's identity is authenticated, their stored `Click to Pay` credentials are shown:

#### Figure: {#ctp-walkthrough-unrecognized_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

Guest Customer {#ctp-walkthrough-guest}
=======================================

This section provides an overview of the `Click to Pay Drop-In UI` guest experience. This interaction occurs when the customer has not previously created a `Click to Pay` account, or their issuer has not provisioned their card into `Click to Pay`.  
In the guest experience, `Click to Pay Drop-In UI` captures the PAN details and the cardholder chooses to create a `Click to Pay` account or to check out as a guest. In both cases, the payment credentials are available for processing transactions using your payment gateway.  
The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use using their chosen email address and phone number combination. A user can select Switch ID or Edit within the contact details tab in order to look up new payment details:

#### Figure: {#ctp-walkthrough-guest_fig-ctp-no-account}

Guest UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

`Click to Pay Drop-In UI` Flow {#ctp_uc_getting_started_integration_flow}
=========================================================================

To integrate `Click to Pay Drop-In UI` into your platform, you must follow several integration steps. This section gives a high-level overview of how to integrate and launch `Click to Pay Drop-In UI` on your webpage and process a transaction. You can find the detailed specifications of the APIs later in this document.

1. You send a server-to-server API request for a capture context. This request is fully authenticated and returns a JSON Web Token (JWT) that is necessary to invoke the frontend JavaScript library. For information on setting up the server side, see [Server-Side Set Up](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-ss-setup.md "").
2. You invoke the `Unified Checkout` JavaScript library using the JWT response from the capture context request. For information on setting up the client side, see [Client-Side Set Up](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro.md "").
3. You use the response from the `Click to Pay Drop-In UI` to retrieve payment credentials for payment processing or other steps.
   This figure illustrates the system's payment flow.

#### Figure: {#ctp_uc_getting_started_integration_flow_fig_uc-payment-flow}

`Click to Pay` Payment Flow  
![Diagram that shows the sequence and flow of a Click to Pay payment.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/ctp-srvorch-authdm-gateway-600x680.svg/jcr:content/renditions/original)  
For more information on the specific APIs referenced, see these topics:

* [Sessions API - Capture Context](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context.md "")
* [Payment Details API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-details.md "")
* [Payment Credentials API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-credentials.md "")

Enabling `Click to Pay` in the `Business Center` {#ctp-uc-enabling-ebc}
=======================================================================

To begin using the `Click to Pay Drop-In UI` powered by `Unified Checkout`, you must first ensure that your merchant ID (MID) is configured to use the service and that `Click to Pay` is properly set up.

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure: {#ctp-uc-enabling-ebc_fig_nh2_q31_2jc}

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original)

3. Under Payment Options, click Manage. The Payment Options page appears.

4. Click the checkbox next to each payment method that you want to display in your checkout UI. Click the drag icon ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-drag-icon-15x25.svg/jcr:content/renditions/original) ) to rearrange the order of the payment options. The `Click to Pay Drop-In UI` supports Relay, Mastercard, and American express. Other card types are routed through the guest checkout journey.

5. Next to `Click to Pay`, click **Manage** and follow the instructions to enroll your business in `Click to Pay`. When `Click to Pay` is enabled, it appears on the payment configuration page.  
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original)

6. Click **Manage** to alter your `Click to Pay` enrollment details. For more information on registering for `Click to Pay`, see [Enable Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-enable-digital-pay-intro.md "").  
   After you enable `Click to Pay`, you can enable authentication. For information about enabling authentication for `Click to Pay` in the `Business Center`, see [Set Up Customer Authentication for Relay Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication/ctp-authentication-steps.md "").

Add `Click to Pay` to a Merchant Account {#boarding-config-ctp-boarding}
========================================================================

Follow these steps to add `Click to Pay` to an organization:

1. In the left navigation panel, click **Portfolio Management**.

2. Under Merchants, click **Manage Merchants**. The Manage Merchants page appears.

3. Click **+ Add Merchant**.

4. Select where you want to board your merchant:

   * Select Board a new merchant account to create a new merchant account.
   * Select Add to an existing account to add a transacting merchant to an existing merchant organization.

   {#boarding-config-ctp-boarding_ul_kkx_fxp_2jc}  
   Click Next.

5. If you are adding a transacting organization to an existing merchant account, search for the merchant account in the Boarding Presets section.

6. If you have more than one boarding package, choose a boarding package from the drop-down menu, or enter text in the search field to find one. Click **Next**. If you have only one boarding package, the Boarding Package section does not display.

7. Click **Start** in the Merchant Account Information section to enter account information. For more information, see [Add Merchant Account Information](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/merchants-v2-add-merch-acct-info.md "").

8. Optional: click **Skip** in the Hierarchy Details section to skip the hierarchy step.

9. Click Start in the Transacting Organization and Products section to set up a transacting organization and configure products for it. The Transacting Organization and Products page appears.

10. Under Transacting Organization Details, enter the transacting organization name and the organization ID.

11. Under Product Enablement, find `Unified Checkout` and select Enabled under the Enablement drop-down menu.

12. Click Configure to configure `Unified Checkout`.

13. Under Payment methods, select `Click to Pay`.{#boarding-config-ctp-boarding_step-pay-method}
    {#boarding-config-ctp-boarding_step-pay-method}

14. Under Card Brands, select the card brands you want to enable in `Unified Checkout`. These card brands are supported by `Click to Pay`:

    * American Express
    * Mastercard
    * Relay
      {#boarding-config-ctp-boarding_ul_l2l_fzs_fjc}  
      You can select **Allow All** to enable all card brands for your merchants. When you select **Allow All** , future additions to supported card brands are automatically available. IMPORTANT You must select at least one card brand to support.
      {#boarding-config-ctp-boarding_step-card-brands}
      {#boarding-config-ctp-boarding_step-card-brands}
15. Under Integrated services, select **Retrieve Sensitive Information at Portfolio Level**.{#boarding-config-ctp-boarding_step-integrated-services}
    {#boarding-config-ctp-boarding_step-integrated-services}

16. Click Apply to save your configuration.{#boarding-config-ctp-boarding_step-apply}
    {#boarding-config-ctp-boarding_step-apply} {#boarding-config-ctp-boarding_steps_jkx_fxp_2jc}

Enable `Click to Pay` {#ctp_enable_digital_pay_intro}
=====================================================

To enable `Click to Pay` on `Unified Checkout`, you must first register `Click to Pay`. This process sends the appropriate information to the digital payment systems and registers your page with each system.  
Follow these steps to enable `Click to Pay` for `Unified Checkout` using the API or in the `Business Center`. You must follow these steps for each transacting merchant for which you want to enable `Click to Pay`.

Enabling `Click to Pay Drop-In UI` Using the API {#boarding-click-to-pay-enable-intro}
======================================================================================

This section shows you how to enable `Click to Pay Drop-In UI` using the Boarding Registration Service (BRS) API.  
To enable `Click to Pay` 3DS authentication, you must include these fields in your request:

* productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerBIN
* productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerName

{#boarding-click-to-pay-enable-intro_ul_cll_v4m_3jc}For information about enabling `Click to Pay` authentication, see [Enable Click to Pay Customer Authentication Using the API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication/boarding-click-to-pay-auth-enable-intro.md "").

Endpoint {#boarding-click-to-pay-enable-intro_d11e752}
------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-click-to-pay-enable-intro_d11e759}  
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-click-to-pay-enable-intro_d11e769}

Required Fields for Enabling `Click to Pay Drop-In UI` {#boarding-click-to-pay-enable-reqfields}
================================================================================================

organizationInformation.businessInformation.merchantCategoryCode
:

organizationInformation.businessInformation.name
:

organizationInformation.businessInformation.websiteUrl
:

organizationInformation.organizationId
:

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.clickToPay.enrollmentData.merchantName
:
Required if the enrollmentData object is included in the request.

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.clickToPay.enrollmentData.merchantURL
:
Required if the enrollmentData object is included in the request.

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.portfolioAccessofSensitiveData.merchantAccessofSensitiveData
:
Set to `false`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation.enabled
:
Required to enable `Unified Checkout`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation. features.clickToPay.enabled
:
Set to `true`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation. features.portfolioAccessofSensitiveData.enabled
:
Set to `true`.
{#boarding-click-to-pay-enable-reqfields_dl_fsr_5c1_3jc}

Related Information {#boarding-click-to-pay-enable-reqfields_section_dgl_c11_3jc}
---------------------------------------------------------------------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-click-to-pay-enable-reqfields_ul_kpc_xzz_sxb}

Optional Fields for Enabling `Click to Pay Drop-In UI` {#boarding-click-to-pay-enable-optfields}
================================================================================================

organizationInformation.businessInformation.address
:

organizationInformation.businessInformation.address.address1
:

organizationInformation.businessInformation.address.administrativeArea
:

organizationInformation.businessInformation.address.country
:

organizationInformation.businessInformation.address.locality
:

organizationInformation.businessInformation.address.postalCode
:

organizationInformation.configurable
:

organizationInformation.parentOrganizationId
:
This value is dependent on your organization hierarchy rules.

organizationInformation.status
:

organizationInformation.type
:

productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerBIN
:
Required when you want to enroll in `3-D Secure`.

productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerName
:
Required when you want to enroll in `3-D Secure`.

registrationInformation.boardingFlow
:

registrationInformation.boardingPackageId
:

registrationInformation.mode
:
{#boarding-click-to-pay-enable-optfields_dl_f3k_zb1_3jc}

Related Information {#boarding-click-to-pay-enable-optfields_section_dgl_c11_3jc}
---------------------------------------------------------------------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-click-to-pay-enable-optfields_ul_kpc_xzz_sxb}

REST Example: Enabling `Click to Pay Drop-In UI` {#boarding-click-to-pay-enable-ex-rest}
========================================================================================

Enable `Click to Pay Drop-In UI`

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE",
    "mode": "COMPLETE",
    "boardingPackageId": "74921204027"
  },
  "organizationInformation": {
    "organizationId": "testucctp001",
    "status": "TEST",
    "businessInformation": {
      "name": "testucctp",
      "websiteUrl": "https://www.test.com",
      "merchantCategoryCode": "0742",
      "address": {
        "country": "US",
        "address1": "Test Dr",
        "postalCode": "78641",
        "administrativeArea": "TX",
        "locality": "Austin"
      }
    },
    "parentOrganizationId": "testucctp",
    "type": "TRANSACTING",
    "configurable": false
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "unifiedCheckout": {
          "subscriptionInformation": {
            "enabled": true,
            "features": {
              "clickToPay": {
                "enabled": true
              },
              "portfolioAccessofSensitiveData ": {
                "enabled": true
              }
            }
          },
          "configurationInformation": {
            "configurations": {
              "features": {
                "clickToPay": {
                  "enrollmentData": {
                    "merchantName": "testucctp",
                    "merchantURL": "https://www.test.com",
                    "acquirerBIN": "123456",
                    "acquirerName": "ExampleAcquirer"
                  }
                },
                "portfolioAccessofSensitiveData ": {
                  " merchantAccessofSensitiveData ": false
                }
              }
            }
          }
        }
      }
    }
  }
}
```

{#boarding-click-to-pay-enable-ex-rest_codeblock_zmy_c11_3jc}

Enabling `Click to Pay` in the `Business Center` {#uc-enable-digital-pay-ctp}
=============================================================================

To begin your integration, you must first enable `Click to Pay`. `Click to Pay` is a digital payment solution that allows customers to pay with their preferred card network and issuer without entering their card details on every website. Customers can use Relay, Mastercard, and American Express cards to streamline their purchase experience. `Click to Pay` provides a fast, secure, and consistent checkout experience across devices and browsers.  
Follow these steps to enable in `Click to Pay` on `Unified Checkout`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-enable-digital-pay-ctp_step-1}
   {#uc-enable-digital-pay-ctp_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original) {#uc-enable-digital-pay-ctp_step-2}
   {#uc-enable-digital-pay-ctp_step-2}

3. In the Payment Options section, click **Manage**. The Payment Options page appears.

4. Click **Manage** next to `Click to Pay`. The `Click to Pay` configuration page appears.

5. Enter your business name and website URL.

6. Click Submit.

   > IMPORTANT
   > ` Click to Pay ` uses network tokenization for transactions. These network tokens are stored in the vault of the token requestor ID (TRID) for the card scheme.

Server-Side Set Up {#ctp-getting-started-ss-setup}
==================================================

This section contains the information you need to set up your server. Initializing `Click to Pay Drop-In UI` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how the `Click to Pay Drop-In UI` performs.  
The server-side component provides this information:

* A transaction-specific public key that is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and interaction methods.

{#ctp-getting-started-ss-setup_ul_atq_bwq_npb}  
The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context* . For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Capture Context Using the Sessions API {#ctp-capture-context-intro}
===================================================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the Sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The Sessions API request contains parameters that define how `Unified Checkout` performs.  
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.  
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types. The capture context request includes these elements:
* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigin
  Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context.  
  When you configure the merchant settings using the Merchant Experience section of the `Business Center`, your request to the `sessions` API must include these required fields. All other values are determined from the settings that are configured in the `Business Center`:

```
{
  "targetOrigins": ["https://merchant.com", "https://reseller.com:8443"],
  "locale": "en_US",
  "country": "US",
    "data": {
        "orderInformation": {
          "amountDetails": {
            "totalAmount": "21.00",
            "currency": "USD"
      }
    }
  }
}
```

{#ctp-capture-context-intro_codeblock_kxt_pcj_2jc}  
When you use only the sessions API to generate the capture context, your request must include these required fields:

```
{
  "targetOrigins": [
    "https://yourCheckoutPage.com"
  ],
  "allowedCardNetworks": [
    "CARD",
    "MASTERCARD",
    "AMEX"
  ],
  "allowedPaymentTypes": [
    "CLICKTOPAY"
  ],
  "country": "US",
  "locale": "en_US",
  "captureMandate": {
    "billingType": "FULL",
    "requestEmail": true,
    "requestPhone": true,
    "requestShipping": true,
    "shipToCountries": [
      "US",
      "GB"
    ],
    "showAcceptedNetworkIcons": true
  },
  "data": {
    "orderInformation": {
      "amountDetails": {
        "totalAmount": "21.00",
        "currency": "USD"
      }
    }
  }
}
```

{#ctp-capture-context-intro_codeblock_nfk_rcj_2jc}  
For information about requesting the capture context using the `sessions` API, see the [API Reference](https://developer.cybersource.com/api-reference-assets/index.md#unified-checkout "") in the `Cybersource` Developer Center. For more information on requesting the capture context, see [Sessions API - Capture Context](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context.md "").

Client-Side Set Up {#ctp-getting-started-cs-setup-intro}
========================================================

This section contains the information you need to set up the client side. You use the `Unified Checkout` JavaScript library to integrate with your e-commerce website. It has two primary components:

* The button widget, which presents `Click to Pay` to the customer. There are different options available to display this to your customers. See these topics: XXX
* The payment acceptance page, which captures payment information from the cardholder. You can embed the payment acceptance page within your webpage or add it as a sidebar.

The `Unified Checkout` JavaScript library supports `Click to Pay` and manual card entry payment methods.  
Follow these steps to set up the client:

1. Load the JavaScript library.
2. Initialize the accept object the capture context JWT. For information JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").
3. Initialize the unified payment object with optional parameters.
4. Show the button list or payment acceptance page or both.

{#ctp-getting-started-cs-setup-intro_ul_m5t_gwq_npb}  
The response to these interactions is a transient token that you use to retrieve the payment information captured by the UI.

Loading the JavaScript Library and Invoking the Accept Function {#ctp-getting-started-cs-js-library-intro}
==========================================================================================================

Use the client library asset path and client library integrity value that is returned by the capture context response to invoke `Unified Checkout` on your page.  
You can retrieve these values from the clientLibrary and clientLibraryIntegrity fields that are returned in the JWT from POST `https://api.cybersource.com``/uc/v1/sessions`. You can use these values to create your script tags.  
You must perform this process for each transaction, as these values may be unique for each transaction. You must avoid hard-coding values for the clientLibrary and clientLibraryIntegrity fields to prevent client-side errors.  
For example, a response from `https://apitest.cybersource.com``/uc/v1/sessions` would include:

```
"data": {
    "clientLibrary":"[EXTRACT clientLibrary VALUE from here]",
    "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]"
}
```

Below is an example script tag:

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" 
    integrity=”[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous”&gt;&lt;/script&gt;
```

> IMPORTANT
> Use the clientLibrary and clientLibraryIntegrity parameter values in the capture context response to obtain the ` Unified Checkout ` JavaScript library URL and the integrity value. This ensures that you are always using the most up-to-date library and protects against fraud. Do not hard-code the ` Unified Checkout ` JavaScript library URL or integrity value.  
> When you load the library, the capture context from your initial server-side request is used to invoke the accept function.

JavaScript Example: Initializing the SDK {#ctp-getting-started-cs-js-library-example}
=====================================================================================

```
async function launchCheckout() {
  try {
	const client = await VAS.UnifiedCheckout(sessionJWT);
	const checkout = await client.createCheckout({ autoProcessing: false }); 
	const token = await checkout.mount('#buttons');
    // result contains the Transient Token
    // Send result to your server for retrieval of payment information
    sendToServer(token);
  } catch (error) {
    if (error.name === 'UnifiedCheckoutError') {
      handleError(error.reason, error.message);
    }
  } finally {
    checkout.destroy();
    client.destroy();
  }
}

launchCheckout();
```

{#ctp-getting-started-cs-js-library-example_codeblock_qsv_chn_djc}  
In this example, `sessionJWT` refers to the capture context JWT.

JavaScript Example: Displaying the Button List {#ctp-getting-started-cs-js-button-example}
==========================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the embedded `Unified Checkout` tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named components that are replaced with `Unified Checkout`'s iframes.

```
// Sidebar
const result = await checkout.mount('#buttons');

// Embedded
const result = await checkout.mount({
  paymentSelection: '#buttons',
  paymentScreen: '#form'
});
```

{#ctp-getting-started-cs-js-button-example_codeblock_fpp_pb1_2jc}

JavaScript Example: Client-Defined Trigger for `Click to Pay` or PAN Entry {#ctp-getting-started-cs-js-trigger-ctp-pan-example}
===============================================================================================================================

When you display `CLICKTOPAY` or `PANENTRY` as allowed payment types, you can load the UI without displaying the `Unified Checkout` checkout button. You can do this by creating a trigger that defines what event loads the UI.  
You can create a trigger only for `CLICKTOPAY` or `PANENTRY` payment methods:

```
//PAN Entry

const trigger = client.createTrigger('PANENTRY');

//Click to Pay

const trigger = client.createTrigger('CLICKTOPAY');
```

{#ctp-getting-started-cs-js-trigger-ctp-pan-example_codeblock_ffr_qb1_2jc} IMPORTANT
When you use the ` client.createTrigger() ` method for ` Click to Pay `, you must create a custom UI to trigger ` Click to Pay `. See [Click to Pay UI Examples](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-ui-screens/ctp-appendix-ui-ux-ex.md "").

Adding the Payment Application and Payment Acceptance {#ctp-getting-started-button-widget-intro}
================================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the `Unified Checkout` embedded tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named `&lt;div&gt;` components that are replaced with `Click to Pay Drop-In UI` `iframes`.
IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the sidebar.

JavaScript Example: Setting Up with Full Sidebar {#ctp-getting-started-button-widget-sidebar}
=============================================================================================

```
&lt;html&gt;
&lt;head&gt;
  &lt;script
    src="[INSERT clientLibrary VALUE HERE]"
    integrity="[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Unified Checkout Integration&lt;/h1&gt;
  &lt;input
    type="hidden"
    name="sessionJWT"
    value="[INSERT sessionJWT HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sessionJWT = document.getElementById("sessionJWT").value;
    
    async function launchCheckout() {
      try {
        const client = await VAS.UnifiedCheckout(sessionJWT);
        const checkout = await client.createCheckout();
        const result = await checkout.mount('#payment-buttons');

        // result contains the completed payment result JWT
        // Send result to your server for verification
        sendToServer(result);
      } catch (error) {
        if (error.name === 'UnifiedCheckoutError') {
          handleError(error.reason, error.message);
        }
      } finally {
        checkout.destroy();
        client.destroy();
      }
    }

    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

JavaScript Example: Setting Up with the Embedded Component {#ctp-getting-started-button-widget-embedded}
========================================================================================================

The main difference between using an embedded component and the sidebar is that the `VAS.UnifiedCheckout(sessionJWT)` object is set to `false`, and the location of the payment screen is passed in the containers argument.

> IMPORTANT If you do not specify a location for the payment acceptance page, it is placed in the side bar.

```
&lt;html&gt;
&lt;head&gt;
  &lt;script
    src="[INSERT clientLibrary VALUE HERE]"
    integrity="[INSERT clientLibraryIntegrity VALUE HERE]"
    crossorigin="anonymous"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Unified Checkout Integration&lt;/h1&gt;
  &lt;input
    type="hidden"
    id="sessionJWT"
    name="sessionJWT"
    value="[INSERT sessionJWT HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sessionJWT = document.getElementById("sessionJWT").value;

    async function launchCheckout() {
      let client;
      let checkout;

      try {
        client = await VAS.UnifiedCheckout(sessionJWT);
        checkout = await client.createCheckout();
        const result = await checkout.mount('#payment-buttons');

        // result contains the completed payment result JWT
        // Send result to your server for verification
        sendToServer(result);
      } catch (error) {
        if (error.name === 'UnifiedCheckoutError') {
          handleError(error.reason, error.message);
        }
      } finally {
        if (checkout) {
          checkout.destroy();
        }

        if (client) {
          client.destroy();
        }
      }
    }

    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

{#ctp-getting-started-button-widget-embedded_codeblock_ugy_tb1_2jc}

Sessions API - Capture Context {#ctp-setup-capture-context}
===========================================================

This section contains the information you need to request the capture context using the `sessions` API. The capture context request contains all of the merchant-specific parameters that tell the frontend JavaScript library how to behave within your payment experience.  
The capture context is a signed JSON Web Token (JWT) containing this information:

* Merchant-specific parameters that dictate the customer payment experience for the current payment transaction.
* A one-time public key that secures the information flow during the current payment transaction.

The capture context request includes these elements:

* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigins  
  For information on JSON Web Tokens, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Target Origin
:
The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain) and port number (if used).

    You must use the https:// protocol. Sub domains must also be included in the target origin.

    Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.

    For example, if you are launching `Click to Pay` on example.com, the target origin could be any of the following:

    * [https://example.com](https://example.com/ "")
    * [https://subdomain.example.com](https://subdomain.example.com/ "")
    * [https://example.com:8080](https://example.com:8080/ "")

:
You can supply up to seven origins within the targetOrigins field for nested iframes. To do this, you must do the following:

    * Compare the list of origins in the `v1/sessions` targetOrigins field against the location.ancestorOrigins of the browser.
    * Ensure that the count of origins and their content matches in the targetOrigins field against the location.ancestorOrigins of the browser. If any origins are missing or mismatched, the system prevents `Unified Checkout` from loading and displays a client-side error message.
    {#ctp-setup-capture-context_ul_ijc_2tj_2jc}

    You must::

Allowed Card Networks
:
Use the allowedCardNetworks field to define the card types. `Click to Pay` supports American Express, Mastercard, and Relay. The `Click to Pay Drop-In UI` manually captures the other card types that are listed in the capture context request. This enables you to process the payment through the chosen gateway but the cardholder is not able to enroll these cards in `Click to Pay`.

    These card networks are available for card entry:

    * American Express
    * Carnet
    * Cartes Bancaires
    * China UnionPay
    * Diners Club
    * Discover
    * EFTPOS
    * ELO
    * Jaywan
    * JCB
    * KCP
    * mada
    * Maestro
    * Mastercard
    * Meeza
    * PayPak
    * UATP
    * Relay

    To support dual-branded or co-badged cards, you must list your supported card types values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Relay and EFTPOS and EFTPOS is listed first, the card type is set to EFTPOS after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-tokens-intro/ctp-dual-co-brand-card-support.md "").

    When a Cartes Bancaires dual-branded card is entered in the `Click to Pay Drop-In UI`, the `Click to Pay Drop-In UI` provides a radio selector button to enable the cardholder to select which scheme they want to use to process the payment. The radio selector defaults to the card scheme that appears first in the allowedCardNetworks field.

    Cartes Bancaires is not supported for `Click to Pay`. If a cardholder selects to process a payment with Cartes Bancaires it is processed as a one-time guest checkout and the user is not enrolled in `Click to Pay`. If a cardholder chooses to process with Relay or Mastercard instead of Cartest Bancaires, they are given the option to enroll their card in `Click to Pay`.

:
> IMPORTANT
> Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). If you include only card types that do not have security codes in the allowedCardNetworks field, ` Unified Checkout ` does not display the security code field in the UI.  
> If you include card types that do not have security codes and cards types that do have security codes in the allowedCardNetworks field, ` Unified Checkout ` displays the security code field in the UI. The field is disabled in the UI when the cardholder enters a card number for a card type with no security code.

Include Card Prefix
:
You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

    * 6 digits
    * 8 digits
    * no prefix at all


    > IMPORTANT
    > When you request the card number prefix for a ` Click to Pay ` tokenized credential, 6 digits are returned. ` Click to Pay ` does not return 8 digits.
    To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.

:
**If you want to receive a 6-digit card number prefix in the response**

    * Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.
    * This example shows how a 6-digit card number prefix `411111` is returned in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111”,
                          "bin" : "411111"
      ```

:
**If you want to receive an 8-digit card number prefix in the response**

    * Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `true`. IMPORTANT
      > Per PCI DSS requirements, this requirement applies only to card numbers longer than 15 digits and for Discover, JCB, Mastercard, UnionPay, and Relay brands.
      > * If the card type entered is not part of these brands, a 6-digit card number prefix is returned instead.
      > * If the card type entered is not part of these brands but is *co-branded* with these brands, an 8-digit card number prefix is returned.
    * This example shows how an 8-digit card prefix `41111102` is returned in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111”,
                          "prefix" : "41111102"
      ```

:
**If you do not want to receive a card number prefix in the response**

    * Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `false`.
    * This example shows how a card number is returned without a card number prefix in the transient token response:

      ```
      "maskedValue" : "XXXXXXXXXXXX1111"
      ```

:
**Best practice:** If your application does not require card number prefix information for routing or identification purposes, `Cybersource` recommends that you include the transientTokenResponseOptions.includeCardPrefix field in the capture context request and set its value to `false`. Doing so limits the exposure of payment data to only what is necessary for your processing needs.  
For more information about PCI DSS, see [Frequently Asked Questions](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers "") on the PCI Security Standards Council site.

Allowed Payment Types
:
You can specify the type of `Unified Checkout` digital payment methods that you want to accept in the capture context.
:
Use the allowedPaymentTypes field to define the payment type. The `Click to Pay Drop-In UI` accepts these payment types:

    * `CLICKTOPAY`
    * `PANENTRY`


    > IMPORTANT
    > When you include ` CLICKTOPAY `, it supports both ` Click to Pay ` and ` PANENTRY ` in the UI.

> IMPORTANT
> When integrating with ` Cybersource ` APIs, ` Cybersource ` insists that you dynamically parse the response for the fields that you are looking for. Additional fields may be added in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. While the underlying data structures will not change, you must also ensure that your integration can handle changes to the order in which the data is returned.

Features {#ctp-capture-context-features}
========================================

This section includes information on the features that are supported in `Click to Pay`.

Allowed Card Networks {#ctp-cc-allowed-card-networks}
=====================================================

Use the allowedCardNetworks field to define the card types.  
These card networks are available for card entry:

* American Express (supported on `Click to Pay`)
* Cartes Bancaires
* Carnet
* China UnionPay
* Diners Club
* Discover
* EFTPOS
* ELO
* Jaywan
* JCB
* JCrew
* KCP
* mada
* Maestro
* Mastercard (supported on `Click to Pay`)
* Meeza
* PayPak
* UATP
* Relay (supported on `Click to Pay`)
  {#ctp-cc-allowed-card-networks_ul_cz5_tt1_3jc}  
  To support dual-branded or co-badged cards, you must list your supported card type values for the allowedCardNetworks field based on your preference for processing card numbers. For example, if a card is dual-branded as Relay and Cartes Bancaires, and Cartes Bancaires is listed first, the card type is set to Cartes Bancaires after the card number is entered in your `Unified Checkout` card collection form. For information on dual-branded or co-badged cards, see [Dual-Branded Cards](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-tokens-intro/ctp-dual-co-brand-card-support.md "").

> IMPORTANT  
> Some card types, such as KCP and UATP, do not have security codes (CVV or CVN). If you include only card types that do not have security codes in the allowedCardNetworks field, ` Unified Checkout ` does not display the security code field in the UI.  
> If you include card types that do not have security codes and cards types that do have security codes in the allowedCardNetworks field, ` Unified Checkout ` displays the security code field in the UI. The field is disabled in the UI when the cardholder enters a card number for a card type with no security code

Target Origins {#ctp-cc-target-origin}
======================================

The [target origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "") is defined by the scheme (protocol), hostname (domain), and port number (if used).  
You must use the https:// protocol. Sub domains must also be included in the target origin.  
Any valid top-level domains, such as .com, .co.uk, and .gov.br, are supported. Wildcards are not supported.  
For example, if you are launching `Unified Checkout` on example.com, the target origin could be any of the following:

* [https://example.com](https://example.com/ "")
* [https://subdomain.example.com](https://subdomain.example.com/ "")
* [https://example.com:8080](https://example.com:8080/ "")

{#ctp-cc-target-origin_ul_plq_qt1_3jc}  
When you use `Unified Checkout` in an iframe, you must include the domain for the URL that loads the iframe and the iframe URL in the targetOrigins field.

Allowed Payment Types {#ctp-cc-allowed-pay-type}
================================================

You can specify the type of `Unified Checkout` digital payment methods that you want to accept in the capture context.  
Use the allowedPaymentTypes field to define the payment type:

* `CLICKTOPAY`
* `PANENTRY`

{#ctp-cc-allowed-pay-type_ul_s5z_4t1_3jc} IMPORTANT
` Click to Pay ` accepts American Express, Mastercard, and Relay for saved cards. Relay and Mastercard tokenize payment credentials using network tokenization for all ` Click to Pay ` requests. ` Click to Pay ` uses ` Click to Pay ` Token Requester IDs (TRIDs) rather than your existing TRIDs to generate network tokens.  
For more information on enabling and managing `Click to Pay`, see [Enabling Click to Pay in the Business Center](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-getting-started-integration-flow/ctp-enable-digital-pay-intro/uc-enable-digital-pay-ctp.md "").

Auto-check Enrollment {#ctp-cc-ctp-enroll-precheck}
===================================================

You can have the `Click to Pay` box pre-checked when a user is manually entering their card details and `Click to Pay` is enabled. The customer can uncheck the box if necessary, which means the request is processed as a one-time manual PAN transaction. This is available when you set the billingType field to `PARTIAL` or `FULL` in the capture context. This ensures that the customer's billing country can be validated in the UI.  
`Click to Pay` enrollment pre-check is available in these countries:

* Argentina
* Brazil
* Chile
* Colombia
* Kuwait
* Mexico
* Peru
* Qatar
* Saudi Arabia
* South Africa
* Ukraine
* United Arab Emirates
  {#ctp-cc-ctp-enroll-precheck_ul_znq_st1_3jc}

```
"paymentConfigurations": {
    "CLICKTOPAY": {
      "autoCheckEnrollment": true
    }
  }
```

{#ctp-cc-ctp-enroll-precheck_codeblock_a4q_st1_3jc}

Button Type {#ctp-cc-button-type}
=================================

When `Unified Checkout` loads, the payment buttons displayed are based on what you include in the allowedPaymentTypes object in the capture context. `Unified Checkout` enables you to customize the text on the payment buttons. You can do this by setting the buttonType field object in the capture context to one of these values:

* `ADD_CARD`
* `CARD_PAYMENT`
* `CHECKOUT_AND_CONTINUE`
* `DEBIT_CREDIT`
* `DONATE`
* `PAY`
* `PAY_WITH_CARD`
* `SUBSCRIBE_WITH_CARD`
  {#ctp-cc-button-type_ul_flz_5t1_3jc}  
  If you do not include the buttonType field in your request, the payment button text defaults to **Checkout with card**. For example:  
  ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-checkout-card-300x100.svg/jcr:content/renditions/original)

Customize Button Text {#ctp-session-button-text}
================================================

Use the buttonType field to customize the text on payment buttons:

|    buttonType Value     |  Button Display Text  |
|-------------------------|-----------------------|
| `ADD_CARD`              | Add card              |
| `CARD_PAYMENT`          | Card payment          |
| `CHECKOUT_AND_CONTINUE` | Checkout and continue |
| `DEBIT_CREDIT`          | Debit or credit       |
| `DONATE`                | Donate                |
| `PAY`                   | Pay                   |
| `PAY_WITH_CARD`         | Pay with card         |
| `SUBSCRIBE_WITH_CARD`   | Subscribe with card   |
[Button Text Options]

When you do not include this field in your request, the default button text is "Checkout with card."

Capture Mandate {#ctp-cc-capture-mandate}
=========================================

The capture mandate enables you to define which fields are captured within `Unified Checkout`. You must include the fields and set the values in the capture context based on the information that you want `Unified Checkout` to collect. This enables the cardholder to review and edit their details where the UI includes these fields. When the UI is used to capture cardholder information, all captured information is available within the payment details API response. When you want the cardholder to review existing address data, you can include the known customer data in the capture context and this information is pre-filled in the `Unified Checkout` UI. For information about the payment details API, see [Payment Details API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-token-get-pymnt-details.md "").

captureMandate.comboCard {#ctp-cc-capture-combo-cards}
======================================================

A combo card is a single card in Brazil that functions as both a debit and a credit card. `Unified Checkout` enables the cardholder to choose whether to pay for a transaction using a debit or credit card. The cardholder can choose the card that they want to use when they enter their card details or when they choose a stored Relay card from their `Click to Pay` wallet during checkout. While in the card details section of the payment form, the cardholder is prompted for a debit or credit card. Credit is the default option.  
To enable combo cards during checkout, you must include the comboCard field in your capture context request and set the field value to `true`. When the comboCard field value is set to `true`, the option to use a debit or credit card appears for all Relay cards that are entered in Unified Checkout and for all cards that are already stored in `Click to Pay`. If you do not want to offer a combo card at checkout, do not include the comboCard field in your capture context request:

```
"captureMandate" : {
      "comboCard": true
}
```

{#ctp-cc-capture-combo-cards_codeblock_dmg_4r1_3jc} IMPORTANT This feature is available only in Brazil.

captureMandate.CPF {#ctp-cc-capture-cpf}
========================================

The Cadastro de Pessoas Físicas (CPF) Brazilian tax ID feature is for customers in Brazil and provides your customers with a way to include their Consumer National Identifier when it is requested at checkout. Include this field in the capture context to display this field within the flow for manual card entry and `Click to Pay` transactions:

```
"captureMandate" : {
    "CPF": {
        "required": true
    }
}
```

{#ctp-cc-capture-cpf_codeblock_g2p_lr1_3jc}
IMPORTANT This feature is available only in Brazil.

captureMandate.requestSaveCredentials {#ctp-cc-capture-save-card}
=================================================================

This feature enables you to display a consent option in the `Unified Checkout` UI for the cardholder to save their payment details for future use.  
When you use this field without using the complete mandate, the transient token payload includes the consumerPreference.saveCard field with the value set to `true` when the cardholder has checked to save the payment information for future purchases:

```
"captureMandate" : {
      "requestSaveCredentials": true
}
```

{#ctp-cc-capture-save-card_codeblock_y3r_ht1_3jc}

captureMandate.showConfirmationStep {#ctp-cc-capture-rem-confirm-screen}
========================================================================

When showConfirmstionStep is set to `false`, you can remove the final summary confirmation screens from the checkout experience. When the UI displays cardholder data, the cardholder can review and, if necessary, edit their payment details before checkout is complete.

```
{
  "captureMandate": {
    "showConfirmationStep": false
  }
}
```

{#ctp-cc-capture-rem-confirm-screen_codeblock_fj1_151_3jc}

captureMandate.billingType {#ctp-cc-capture-billing-type}
=========================================================

`PARTIAL`: Only the billing postal code and billing country are collected in the UI. Set to this value when you use relaxed address verification services (AVS). This includes markets where postal code and billing country are enough for successful payment processing.  
`NONE`: No fields are shown in the UI to capture cardholder billing details. If you are using the Complete Mandate, you must provide billing details in the capture context. All information that is collected from these fields is tokenized in the transient token and sent for payment processing. For information about which fields are required for payment processing, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").  
`FULL`: These fields are shown in the UI to capture cardholder billing details. When you include the billing details in the capture context, these details are pre-filled in the `Unified Checkout` UI. All information that is collected from these fields are tokenized in the transient token and sent for payment processing where the Complete Mandate is used.

captureMandate.requestEmail {#ctp-cc-capture-req-email}
=======================================================

`false`: No email address is shown in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account and it appears in the UI when requestEmail is set to `false`.  
`true`: The email address is shown and captured in the UI. If you are using `Click to Pay`, this email address is used to find the cardholder's `Click to Pay` account.

captureMandate.requestPhone {#ctp-cc-capture-req-phone}
=======================================================

`false`: No phone number is shown or captured in the UI.  
`true`: The phone number is shown and captured in the UI.

captureMandate.requestShipping {#ctp-cc-capture-req-ship}
=========================================================

`false`: No shipping information is captured in the UI. When shipping details are required for payment processing and are used for follow on services such as `Decision Manager`, you can include these fields in the capture context. These details are tokenized and passed through.  
`true`: Shipping fields are shown in the UI and are collected by `Unified Checkout`. When you include the shipping details in the capture context, the information appears prefilled in the UI.

captureMandate.shipToCountries {#ctp-cc-capture-ship-to}
========================================================

When the requestShipping field is set to `true`, only the countries that are included in this field can be selected by the cardholder for their shipping address.

Include Card Prefix {#ctp-cc-include-prefix}
============================================

You can control the length of the card number prefix to be received in the response to the capture context `/sessions` request:

* Six digits
* Eight digits
* No prefix

{#ctp-cc-include-prefix_ul_cjr_xt1_3jc}To specify your preferred card number prefix length, include or exclude the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.  
To receive a six-digit card number prefix in the response, follow this step:  
Do not include the transientTokenResponseOptions.includeCardPrefix field in the capture context `/sessions` request.  
This example shows how a six-digit card number prefix `411111` is returned in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111”,
                        "bin" : "411111"
```

{#ctp-cc-include-prefix_codeblock_djr_xt1_3jc}  
To receive an eight-digit card number prefix in the response, follow this step:  
Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `true`. IMPORTANT

> This PCI DSS requirement applies only to card numbers longer than 15 digits and only for Discover, JCB, Mastercard, UnionPay, and Relay brands.
>
> * If the card type entered is not part of these brands, a six-digit card number prefix is returned instead.
> * If the card type entered is not part of these brands but is *co-branded* with these brands, an eight-digit card number prefix is returned.
>   {#ctp-cc-include-prefix_ul_fjr_xt1_3jc}
>   This example shows how an eight-digit card prefix `41111102` is returned in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111”,
                        "prefix" : "41111102"
```

{#ctp-cc-include-prefix_codeblock_gjr_xt1_3jc}  
To not receive a card number prefix in the response, follow this step:  
Include the transientTokenResponseOptions.includeCardPrefix field in the capture context request, and set the value to `false`.  
This example shows how a card number is returned without a card number prefix in the transient token response:

```
"maskedValue" : "XXXXXXXXXXXX1111"
```

{#ctp-cc-include-prefix_codeblock_hjr_xt1_3jc}
**Best practice:** If your application does not require card number prefix information for routing or identification, `Cybersource` recommends that you include the transientTokenResponseOptions.includeCardPrefix field in the capture context request and set its value to `false`. Doing so limits the exposure of payment data to only what is necessary for your processing needs.  
For more information about PCI DSS, see [Frequently Asked Questions](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-are-acceptable-formats-for-truncation-of-primary-account-numbers "") on the PCI Security Standards Council site.

Email Autolookup {#ctp-cc-email-autolookup}
===========================================

When you include `Click to Pay` as an allowedPaymentType, an automatic email lookup occurs when an email address is included in the capture context request in the data.billTo.email field.. If the user has a `Click to Pay` account but is not on a recognized device, a one-time password (OTP) screen appears and the user is prompted to enter their OTP. If the user does not have a `Click to Pay` account, the user must enter their card information manually. They will have the option to create a `Click to Pay` account.

Mobile as Identity for `Click to Pay` {#ctp-cc-mobile-identity}
===============================================================

`Click to Pay` supports mobile numbers as way to identify a user. This enables cardholders to use their mobile number instead of their email address in certain markets for Relay and Mastercard transactions.  
When the requestEmail field is set to `false` and the requestPhone field is set to `true`, the cardholder is identified using the provided mobile number. When the requestEmail field is set to `true` and the requestPhone field is set to `false`, the cardholder is identified using the provided email address. When the requestEmail field is set to `true` and the requestPhone field is also set to `true`, the cardholder is identified using the provided email address first and then the mobile number if there is no match.

UI/UX Customization Look and Feel {#ctp-cc-ui-ux-look-feel}
===========================================================

UI/UX Customization Look and Feel
`Click to Pay Drop-In UI` supports appearance customization using the appearance field object. You can customize the theme, button configuration, color styling, input states, and typography. All customization fields are optional and can be configured in the API in the appearance.variables field object. For a complete list of customizable fields, see [Customization Matrix](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-cust-matrix.md "").  
This is an example JSON configuration:

```
{ 
  "appearance": { 
    "theme": "LIGHT", 
    "buttonType": "CHECKOUT", 
    "variables": { 
      "backgroundColor": "#FFFFFF", 
      "textColor": "#000000", 
      "headerBackground": "#1A237E", 
      "headerForeground": "#FFFFFF", 
      "inputBackground": "#FAFAFA", 
      "buttonBackground": "#E0E0E0", 
      "buttonForeground": "#333333", 
      "fontFamily": "Roboto Slab, serif" 
    } 
  } 
} 
```

{#ctp-cc-ui-ux-look-feel_codeblock_y5l_ndz_hjc}  
This is an example sessions capture context request with UI/UX customization:

```
{
  "targetOrigins": [
    "https://yourCheckoutPage.com"
  ],
  "allowedCardNetworks": [
    "CARD",
    "MASTERCARD",
    "AMEX"
  ],
  "allowedPaymentTypes": [
    "CLICKTOPAY"
  ],
  "appearance": {
    "variables": {
      "backgroundColor": "#FFFFFF",
      "textColor": "#1A1A1A",
      "headerBackground": "#0A3450",
      "headerForeground": "#FFFFFF",
      "headerAvatarBackgroundColor": "#E6EEF8",
      "headerAvatarForegroundColor": "#0A2540",
      "inputBackground": "#FFFFFF",
      "inputColor": "#1A1A1A",
      "inputPlaceholderColor": "#6B7280",
      "inputBorderColor": "#D1D5DB",
      "inputBorderStyle": "solid",
      "inputBorderRadius": "6px",
      "inputHoverBackground": "#FFFFFF",
      "inputHoverColor": "#111827",
      "inputHoverPlaceholderColor": "#6B7280",
      "inputHoverBorderColor": "#9CA3AF",
      "inputHoverBorderStyle": "solid",
      "inputFocusedBackground": "#FFFFFF",
      "inputFocusedColor": "#111827",
      "inputFocusedPlaceholderColor": "#6B7280",
      "inputFocusedBorderColor": "#2563EB",
      "inputFocusedBorderStyle": "solid",
      "inputActiveBackground": "#FFFFFF",
      "inputActiveColor": "#111827",
      "inputActivePlaceholderColor": "#6B7280",
      "inputActiveBorderColor": "#2563EB",
      "inputActiveBorderStyle": "solid",
      "inputPressedBackground": "#F9FAFB",
      "inputPressedColor": "#111827",
      "inputPressedPlaceholderColor": "#9CA3AF",
      "inputPressedBorderColor": "#2563EB",
      "inputPressedBorderStyle": "solid",
      "inputErrorBackground": "#FEF2F2",
      "inputErrorColor": "#991B1B",
      "inputErrorPlaceholderColor": "#B91C1C",
      "inputErrorBorderColor": "#DC2626",
      "inputErrorBorderStyle": "solid",
      "inputValidBackground": "#F0FDF4",
      "inputValidColor": "#065F46",
      "inputValidPlaceholderColor": "#047857",
      "inputValidBorderColor": "#16A34A",
      "inputValidBorderStyle": "solid",
      "buttonBackground": "#2563EB",
      "buttonForeground": "#FFFFFF",
      "buttonShape": "rect",
      "buttonBorderColor": "#2563EB",
      "buttonBorderStyle": "solid",
      "buttonBorderRadius": "8px",
      "buttonHoverBackground": "#1D4ED8",
      "buttonHoverForeground": "#FFFFFF",
      "buttonHoverBorderColor": "#1D4ED8",
      "buttonHoverBorderStyle": "solid",
      "buttonFocusBackground": "#1E40AF",
      "buttonFocusForeground": "#FFFFFF",
      "buttonFocusBorderColor": "#1E40AF",
      "buttonActiveBackground": "#1E3A8A",
      "buttonActiveForeground": "#FFFFFF",
      "buttonActiveBorderColor": "#1E3A8A",
      "buttonActiveBorderStyle": "solid",
      "buttonDisabledBackground": "#E5E7EB",
      "buttonDisabledForeground": "#9CA3AF",
      "buttonDisabledBorderColor": "#E5E7EB",
      "fontFamily": "Inter, Arial, sans-serif",
      "borderRadius": "8px",
      "paymentSelectionBackground": "#F9FAFB"
    }
  },
  "country": "US",
  "locale": "en_US",
  "captureMandate": {
    "billingType": "FULL",
    "requestEmail": true,
    "requestPhone": true,
    "requestShipping": true,
    "shipToCountries": [
      "US",
      "GB"
    ],
    "showAcceptedNetworkIcons": true
  },
  "data": {
    "orderInformation": {
      "amountDetails": {
        "totalAmount": "21.00",
        "currency": "USD"
      }
    }
  }
}
```

{#ctp-cc-ui-ux-look-feel_codeblock_hw4_q51_3jc}

Client Version History {#uc-capture-context-versions}
=====================================================

Below is a list of client versions and the features that are included in each version.

> IMPORTANT
> ` Cybersource ` recommends that you use the most recent client version in your integration.

0.23
:
Accepts these card networks in the allowedCardNetworks field for manual card entry:

    * Carnet
    * Cartes Bancaires
    * China UnionPay with card verification value (CVV)
    * EFTPOS
    * ELO
    * JCrew PLCC
    * mada
    * Meeza

:
Ordering controls for the allowedPaymentTypes button.
:
De-coupling of PANENTRY from other payment types in the allowedPaymentTypes field.

0.24
:
Support for enabling combo cards in the capture context.
:
Support for eight-digit BINs.
:
Support for enabling card save in the capture context.

0.25
:
Addition of **Skip Verification next time** in the `Click to Pay` payment flow.
:
Support for CPF in the capture context.

0.26
:
Support for auto-lookup in `Click to Pay` when an email is included in the capture context.
:
Inclusion of the cardDetails field object in the transient token response.

0.28
:
Support for PayPak as an allowedCardNetwork.
:
Auto-enrollment for `Click to Pay` in supported markets.
:
Removal of the confirm or continue screen for specific use cases.
:
Static button for `Click to Pay` flows.

0.30
:
Support for Pakistan locales (en_PK and ur_PK).
:
New look and feel of `Unified Checkout` in line with EMVCO best practices.

0.31
:
Addition of the data object of the orderInformation field object and pass-through fields.
:
Support for Jaywan as an allowedCardNetwork.
:
Updated the payment details response to return detected card types. Multiple card types are shown when more than one card type is detected.

0.32
:
Support for KCP and UATP in the allowedCardNetwork field.
:
A radio button in the UI for Cartes Bancaires dual-branded cards.

0.33
:
Support for Mobile as Identity `Click to Pay` lookup.

0.34
:
Additional BIN range for Jaywan card types.

Requesting the Capture Context Using the Sessions API {#ctp-setup-capture-context-intro}
========================================================================================

This section shows you how to request the capture context.

Endpoint {#ctp-setup-capture-context-intro_d14e1021}
----------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/uc/v1/sessions`{#ctp-setup-capture-context-intro_d14e1028}  
**Test:** `POST ``https://apitest.cybersource.com``/uc/v1/sessions`{#ctp-setup-capture-context-intro_d14e1038}  
**Production in Saudi Arabia:** `POST ``https://api.sa.cybersource.com``/uc/v1/sessions`{#ctp-setup-capture-context-intro_d14e1048}  
**Test in Saudi Arabia:** `POST ``https://apitest.sa.cybersource.com``/uc/v1/sessions`{#ctp-setup-capture-context-intro_d14e1058}

Required Fields for Requesting the Capture Context {#ctp-setup-capture-context-req-fields}
==========================================================================================

Use these required fields to request the capture context:

Required Fields for Requesting the Capture Context {#ctp-setup-capture-context-req-fields_req-fields-uc-capture-ctx}
--------------------------------------------------------------------------------------------------------------------

Your capture context request must include these fields:

[allowedPaymentTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/allowed-payment-types.md "")
:
Set to `CLICKTOPAY`.

[country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/country.md "")
:

[data.orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[data.orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[locale](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/locale.md "")
:

[targetOrigins](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/target-origins.md "")
:
The URL in this field value must contain `https`.

Related Information {#ctp-setup-capture-context-req-fields_section_ybj_nzz_sxb}
-------------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#ctp-setup-capture-context-req-fields_ul_zbj_nzz_sxb}

REST Example: Requesting the Capture Context {#ctp-setup-capture-context-example}
=================================================================================

Request

```
{
    "targetOrigins": [
      "https://unified-payments.appspot.com"
    ],
    "allowedCardNetworks": [
      "CARD",
      "MASTERCARD",
      "AMEX"
    ],
    "allowedPaymentTypes": [
      "CLICKTOPAY"
    ],
    "country": "US",
    "locale": "en_US",
    "captureMandate": {
      "billingType": "FULL",
      "requestEmail": true,
      "requestPhone": true,
      "requestShipping": true,
      "shipToCountries": [
        "US",
        "UK"
      ],
      "showAcceptedNetworkIcons": true
    },
    "data": {
      "orderInformation": {
        "amountDetails": {
          "totalAmount": "21.00",
          "currency": "USD"
        },
        "billTo": {
          "address1": "1111 Park Street",
          "address2": "Apartment 24B",
          "administrativeArea": "NY",
          "country": "US",
          "district": "district",
          "locality": "New York",
          "postalCode": "00000",
          "company": {
            "name": "Relay Inc",
            "address1": "900 Metro Center Blvd",
            "administrativeArea": "CA",
            "buildingNumber": "1",
            "country": "US",
            "district": "district",
            "locality": "Foster City",
            "postalCode": "94404"
          },
          "email": "maya.tran@company.com",
          "firstName": "Maya",
          "lastName": "Tran",
          "middleName": "S",
          "title": "Ms",
          "phoneNumber": "1234567890",
          "phoneType": "phoneType"
        },
        "shipTo": {
          "address1": "Relay",
          "address2": "123 Main Street",
          "address3": "Apartment 102",
          "administrativeArea": "CA",
          "buildingNumber": "string",
          "country": "US",
          "locality": "Springfield",
          "postalCode": "99999",
          "firstName": "Joe",
          "lastName": "Soap"
        }
      }
    }
  }
```

Successful Encrypted JWT Response to Request  
eyJraWQiOiJ6dSIsImFsZyI6IlJTMjU2In0.eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImNvbXBsZXRlUGF0aCI6Ii9mbGV4L3YyL2NvbXBsZXRlIiwiZGF0YSI6Im4xWnFrVXFNaTJSTjVjVXJBTmp1aUJBQUVLVTY0blNKSjFDRDdBaDFvbW9nVFFTWk4zVE1uLzVpc201WEN6TTlzMitVcUdkaERCSCtEMmNPY3A2TmgyZmNRa0NnUUUzT3dicXJFdUpxdHBCZ2ZSU1h0aXI0Z0RUY0dEMHhCcndGNmdDN1plbk8zS2s3NUw3ZG1hZ2VkNm9hQ09mVkVwSThhYnZRWTRBcDdvTGdKdEpOYnViNFU2M3hzZ3B3NWdHbXhEY1ZyanlmN0FqeitvdFRLUU1UcHpnT1ByTVhxaitPbHV6VERZSTltbFdEQi9pRjlaNUF6SGZoOHdtWm9vVHBIb1ZxT1hZY1NJa1JIRWNqemZBQ2c5WFUrZ1lrTlE1MjlaOWhEemtvZ2RvMmxkNFx1MDAzZCIsIm9yaWdpbiI6Imh0dHBzOi8vdGVzdGZsZXguY3liZXJzb3VyY2UuY29tIiwidHJhbnNpZW50VG9rZW5PcGVyYXRpb25zIjpbeyJzdWIiOiIwNDA0X3Rlc3RjdHBkaXVpMDAxIiwiYXVkIjoibmFfcGFydG5lcl9jdHAyIiwia2lkIjoiMTE3ZjY5ZWMtYTA1ZS00MDM0LThhNzAtYWNjMWViOGM5ZThiIiwidHlwZSI6IlNUT1JFIn1dLCJjb21wbGV0ZVVybCI6Imh0dHBzOi8vdGVzdGZsZXguY3liZXJzb3VyY2UuY29tL2ZsZXgvdjIvY29tcGxldGUiLCJhdXRoZW50aWNhdGlvblNldHVwUGF0aCI6Ii9mbGV4L3YyL2V4dGVybmFsLXNlc3Npb25zL3NjYSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJwbFc2THMxa2oyXzdJM096Y3l6YXZoblpJUUhrUDFhMU10Um1nYUswSm1yaUlRUkFBdzhRMUlQV2xTQTI0Y2s0VGxBY2JVeW5nRzJTeWJmc3o4NDZfWlVMb19PZzBwaVlvazhOVl9uMEVPNHFtMDhtblNFMzZJRGdweldSa3E0QkFHMmpqY3cyclNzbHAwY05TQmxLb1B1ZDZSYUsxSUJHNGVMN3hFTmVvR0VZTzByZ0NyZFUtWHlTTGZxYlZaNkNiODNLZFFxeXI3VUZFa0FWc0xETkpKSU1yTnB0SGtmZ0xFejlIV1FmRkNHZUYzWVRBNGc1Ri1DLXNraHJNNkRSMDZKdENiOUFsZzljRVlpNklhTHJPYmNMXzlvLU95bG5xclBSeld6WHA3RnI4WGNUVmgyNkx0S3BzRDZGQUliUVdBaGNkYklwTGJoMktzRy03VjBBcXciLCJraWQiOiIwODM2TExkMnZFRDNWWE5jNlFWUmJXNVk5TlM3a2RPayJ9fSwiY3R4IjpbeyJkYXRhIjp7ImFsbG93ZWRQYXltZW50VHlwZXMiOlsiQ0xJQ0tUT1BBWSIsIlBBTkVOVFJZIl0sInBheW1lbnRDb25maWd1cmF0aW9ucyI6eyJTUkNWSVNBIjp7Im9yaWdpbiI6Imh0dHBzOi8vc2FuZGJveC1hc3NldHMuc2VjdXJlLmNoZWNrb3V0LnZpc2EuY29tIiwicGF0aCI6Ii9jaGVja291dC13aWRnZXQvcmVzb3VyY2VzL2pzL3NyYy1pLWFkYXB0ZXIvdmlzYVNkay5qcz92MiIsInBhbkVuY3J5cHRpb25LZXkiOnsia3R5IjoiUlNBIiwiZSI6IkFRQUIiLCJ1c2UiOiJlbmMiLCJraWQiOiJXMFBaOFZYVVZFQlU5NUpPNlpEWTEzc3E1Si1keFRuNTZmSWJEWDZObWMzWmo5V3FjIiwibiI6InNaUEl1c0RmN3lRbm5oQmtVOW11MTRWT08zQ3J1aTNiN3JBZjJLWWVvYlVSbVhBMTdiMUpYOWpnMENkLXZncG11eVRyeEJVU2MtNGIwLVVQZ1N3R0ZxUFdVcHgwOEV4cXJ3UERPdkZvakJvdTJ3bHlxOGJjeTBVcy1CZmVDelNFNWxNVmRTWFRYWFhjTnF1LXFiMjJqQ0NDSkFMcHhzQXJzYm9NT1hzTGVkaDNNNFhOUTVYR0F0UmY3Yi0tdVRZNURyOUtMWXlVdlpLQW5ZMDRNS0pQRU81NFlpSUZNNURUQWhOT21zMDg5amRNZHgtVVJJS0pqUFUyLVJwSEcxdThMQ0cwMjhSVElwUHNOYlJhbnVTNVRBWV96bHhEZ2IxaEtKMzZZYlpFTkhMZzlQWFRCaGRPTWxVOTBEVExsZmNiTFRhLUQ3RGdsakFhV0N1dnpMUGFHdyJ9LCJwYXJhbWV0ZXJzIjp7InNyY0luaXRpYXRvcklkIjoiSkZDWjhRVk9KQTc2TlhaNjhGWkQyMVJZSXhqM3lQWmRpVXhrZE51aWJCbHhnd2FQNCIsInNyY2lEcGFJZCI6Ijc3NWIyMWYyLTRkMDMtNGM1MC1iY2JiLWIyNjQ0ZGFhZWY2NSIsInNyY2lUcmFuc2FjdGlvbklkIjoiMDRlYTNhMjctZmI3OS00YjBiLWFiOTUtZmVhNzdkMDY3MDZmIiwiZHBhVHJhbnNhY3Rpb25PcHRpb25zIjp7ImRwYUxvY2FsZSI6ImVuX1VTIiwicGF5bG9hZFR5cGVJbmRpY2F0b3IiOiJGVUxMIiwicmV2aWV3QWN0aW9uIjoiY29udGludWUiLCJkcGFBY2NlcHRlZEJpbGxpbmdDb3VudHJpZXMiOltdLCJkcGFBY2NlcHRlZFNoaXBwaW5nQ291bnRyaWVzIjpbIlVTIiwiR0IiXSwiZHBhQmlsbGluZ1ByZWZlcmVuY2UiOiJBTEwiLCJkcGFTaGlwcGluZ1ByZWZlcmVuY2UiOiJBTEwiLCJjb25zdW1lck5hbWVSZXF1ZXN0ZWQiOnRydWUsImNvbnN1bWVyRW1haWxBZGRyZXNzUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lclBob25lTnVtYmVyUmVxdWVzdGVkIjp0cnVlLCJtZXJjaGFudENvdW50cnlDb2RlIjoiVVMiLCJjdXN0b21JbnB1dERhdGEiOnsiY2hlY2tvdXRPcmNoZXN0cmF0b3IiOiJtZXJjaGFudCJ9LCJ0cmFuc2FjdGlvbkFtb3VudCI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6IjIxLjAwIiwidHJhbnNhY3Rpb25DdXJyZW5jeUNvZGUiOiJVU0QifSwicGF5bWVudE9wdGlvbnMiOnsiZHBhRHluYW1pY0RhdGFUdGxNaW51dGVzIjoxNSwiZHBhUGFuUmVxdWVzdGVkIjpmYWxzZSwiZHluYW1pY0RhdGFUeXBlIjoiQ0FSRF9BUFBMSUNBVElPTl9DUllQVE9HUkFNX0xPTkdfRk9STSJ9fX0sImNoZWNrb3V0UGFyYW1ldGVycyI6eyJkcGFUcmFuc2FjdGlvbk9wdGlvbnMiOnsidHJhbnNhY3Rpb25BbW91bnQiOnsidHJhbnNhY3Rpb25BbW91bnQiOiIyMS4wMCIsInRyYW5zYWN0aW9uQ3VycmVuY3lDb2RlIjoiVVNEIn0sImFjcXVpcmVyTWVyY2hhbnRJZCI6IjEyMzQ1Njc4IiwiYWNxdWlyZXJCSU4iOiIxMjM0NTYiLCJtZXJjaGFudE5hbWUiOiJUZXN0IE1lcmNoYW50IiwiYXV0aGVudGljYXRpb25QcmVmZXJlbmNlcyI6eyJhdXRoZW50aWNhdGlvbk1ldGhvZHMiOlt7ImF1dGhlbnRpY2F0aW9uTWV0aG9kVHlwZSI6IjNEUyIsImF1dGhlbnRpY2F0aW9uU3ViamVjdCI6IkNBUkRIT0xERVIiLCJtZXRob2RBdHRyaWJ1dGVzIjp7ImNoYWxsZW5nZUluZGljYXRvciI6IjAxIn19XSwicGF5bG9hZFJlcXVlc3RlZCI6IkFVVEhFTlRJQ0FURUQifX19fSwiU1JDTUFTVEVSQ0FSRCI6eyJvcmlnaW4iOiJodHRwczovL3NhbmRib3guc3JjLm1hc3RlcmNhcmQuY29tIiwicGF0aCI6Ii9zZGsvc3Jjc2RrLm1hc3RlcmNhcmQuanMiLCJwYW5FbmNyeXB0aW9uS2V5Ijp7Imt0eSI6IlJTQSIsImUiOiJBUUFCIiwidXNlIjoiZW5jIiwia2lkIjoiMjAyMzAyMDcyMjM1MjEtc2FuZGJveC1mcGFuLWVuY3J5cHRpb24tc3JjLW1hc3RlcmNhcmQtaW50Iiwia2V5X29wcyI6WyJlbmNyeXB0Iiwid3JhcEtleSJdLCJhbGciOiJSU0EtT0FFUC0yNTYiLCJuIjoidDA2SThzamxTLXJyczd1Q2FnSDhldm9ldW1hUm92S3ppWlNJOVMyTjlJRFE5dFcyUGFwZlJhOUxjMUt2ZUVCRFZzMjdQa2hrVTVPeUhnUDBpRWpUdUtWcHZoNTlUNGxhLW1CU0lsczdVZWNVUUxMYTBXa21idEw3ak5kbHRBNWZxN0FoY0FyNXFjYTk4OHFyTGQ3SXlyOUUwQzNUeGJUOXRvMWlRY3B6OG9jWk9EUlhvaWRGQW5PVkw1WUdGbWxzcmVEYko0VmhzaTBwQWRjY1FjaWwteWRTZ3VyS0ItcnFLcHBiOWVwb211NFFVaDMzODJDdjhOb2JZbUYzb3M4bkdHZ0dQLWN5WG8wbnNLY1BBZ2ZybFF6b3M3cUh4VU9yRmUyeF9sWjFHMUFFLVhya3J4akJ5czlxNTNHTVJTTkNROGMtX21jRjlwYnE0SFlCcy12RDVRIn0sInBhcmFtZXRlcnMiOnsic3JjaVRyYW5zYWN0aW9uSWQiOiIwNGVhM2EyNy1mYjc5LTRiMGItYWI5NS1mZWE3N2QwNjcwNmYiLCJzcmNpRHBhSWQiOiI3NzViMjFmMi00ZDAzLTRjNTAtYmNiYi1iMjY0NGRhYWVmNjUiLCJzcmNJbml0aWF0b3JJZCI6Ijg0NGY3ZTNkLTA3ZjAtNDRiMS1hMjM3LWU2NDI0NDRlMDUxMiIsImRwYVRyYW5zYWN0aW9uT3B0aW9ucyI6eyJ0cmFuc2FjdGlvblR5cGUiOiJQVVJDSEFTRSIsImRwYUxvY2FsZSI6ImVuX1VTIiwiZHBhQWNjZXB0ZWRTaGlwcGluZ0NvdW50cmllcyI6WyJVUyIsIkdCIl0sImNvbnN1bWVyRW1haWxBZGRyZXNzUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lclBob25lTnVtYmVyUmVxdWVzdGVkIjp0cnVlLCJ0cmFuc2FjdGlvbkFtb3VudCI6eyJ0cmFuc2FjdGlvbkFtb3VudCI6IjIxLjAwIiwidHJhbnNhY3Rpb25DdXJyZW5jeUNvZGUiOiJVU0QifSwiZHBhQWNjZXB0ZWRCaWxsaW5nQ291bnRyaWVzIjpbXSwiZHBhQmlsbGluZ1ByZWZlcmVuY2UiOiJGVUxMIiwiZHBhU2hpcHBpbmdQcmVmZXJlbmNlIjoiRlVMTCIsImNvbnN1bWVyTmFtZVJlcXVlc3RlZCI6dHJ1ZSwicGF5bG9hZFR5cGVJbmRpY2F0b3IiOiJGVUxMIiwicGF5bWVudE9wdGlvbnMiOnsiZHluYW1pY0RhdGFUeXBlIjoiQ0FSRF9BUFBMSUNBVElPTl9DUllQVE9HUkFNX1NIT1JUX0ZPUk0ifX19fSwiU1JDQU1FWCI6eyJvcmlnaW4iOiJodHRwczovL3F3d3cuYWV4cC1zdGF0aWMuY29tIiwicGF0aCI6Ii9ha2FtYWkvcmVtb3RlY29tbWVyY2Uvc2NyaXB0cy9hbWV4U0RLLTEuMC4wLmpzIiwicGFuRW5jcnlwdGlvbktleSI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsImtpZCI6InNyYy1hbWV4LWNhcmQtZW5jLTIwMjYiLCJhbGciOiJSU0EtT0FFUC0yNTYiLCJuIjoicFpNa2VwaUY5TnM4QTBnQlhDWGkwV1dzZnZZOXJSNUVJdHpGbXV0RkVkNlFHMHItVkYtSUJhRFNkM091RHdUVGRzeURySVh4cUR5eUs0Wm1neTI3QzdpT2dYZi1OZmZELU9UOWxuVUxOMV8xa3NrR0ROZEhLUWVFd2FsS0JrNkhPcTFCZGZQak9mTkg5WmJ6TS1HbnZMdWpzWkJLMHpveWhCcGdpZmh5R043SGdNRmFCZXJTeld5T0Q4aVAyZENERzNkMTIxRklnbm9waXVLZmdQaWIyZkZqQjBIeWJEOXVHZ0NocWRrYmxiOENja2pwZWJpYzZFbmdjc2lOYlR3UHAtT2tpMmlDN1FaRUljOWZ1eko1SGllb0JWX3Fha3lfUF9qUkJRSkRmSThhMnVlaDBUaG9rbllORFB6ZXlGV1dCZTZmYndLblZjT0lpaDc3WXF3YTR5bHczTVJWblJnVzMxU0JDX0owWVh5UzJnTFdMY3dUMU1hSGQ0WXdVbW43bjVZWWZYak5rTDg5X2ZycDcyc3ItSmlQbmZMUHBvQ204UHJiZTJWcTJ3VnhkMjc0bUd5X3I3S2pfWnIwY3UwaGlTem1jTnFZbWdITG8xUTc4UnhaaXlKMWNnWU5pXy1EQWR6cnE3dGxnRkR6eHVZTHRBVUhYZ1prdUxlVS13Q0wifSwicGFyYW1ldGVycyI6eyJzcmNpVHJhbnNhY3Rpb25JZCI6IjA0ZWEzYTI3LWZiNzktNGIwYi1hYjk1LWZlYTc3ZDA2NzA2ZiIsInNyY0luaXRpYXRvcklkIjoiOGVjMmM4ODgtNjRjYy00ZWZjLTkxNzUtYjMzNzQ1MmIyOGM4IiwiZHBhRGF0YSI6eyJkcGFOYW1lIjoiMDQwNCBUZXN0IENUUERJVUkgIiwiZHBhTG9nb1VyaSI6Imh0dHBzOi8vd3d3LnRlc3QuY29tLyIsImRwYVByZXNlbnRhdGlvbk5hbWUiOiIwNDA0IFRlc3QgQ1RQRElVSSAiLCJkcGFVcmkiOiJodHRwczovL3d3dy50ZXN0LmNvbS8ifSwiZHBhVHJhbnNhY3Rpb25PcHRpb25zIjp7ImRwYUxvY2FsZSI6ImVuX1VTIiwiZHBhQWNjZXB0ZWRCaWxsaW5nQ291bnRyaWVzIjpbXSwiZHBhQWNjZXB0ZWRTaGlwcGluZ0NvdW50cmllcyI6WyJVUyIsIkdCIl0sImRwYUJpbGxpbmdQcmVmZXJlbmNlIjoiQUxMIiwiZHBhU2hpcHBpbmdQcmVmZXJlbmNlIjoiQUxMIiwiY29uc3VtZXJOYW1lUmVxdWVzdGVkIjp0cnVlLCJjb25zdW1lckVtYWlsQWRkcmVzc1JlcXVlc3RlZCI6dHJ1ZSwiY29uc3VtZXJQaG9uZU51bWJlclJlcXVlc3RlZCI6dHJ1ZSwicmV2aWV3QWN0aW9uIjoiY29udGludWUiLCJ0aHJlZURzUHJlZmVyZW5jZSI6Ik5PTkUifX19fSwiY2FwdHVyZU1hbmRhdGUiOnsic2hvd0NvbmZpcm1hdGlvblN0ZXAiOnRydWUsImJpbGxpbmdUeXBlIjoiRlVMTCIsInJlcXVlc3RFbWFpbCI6dHJ1ZSwicmVxdWVzdFBob25lIjp0cnVlLCJyZXF1ZXN0U2hpcHBpbmciOnRydWUsInNoaXBUb0NvdW50cmllcyI6WyJVUyIsIkdCIl0sInNob3dBY2NlcHRlZE5ldHdvcmtJY29ucyI6dHJ1ZSwiY29tYm9DYXJkIjpmYWxzZSwicmVxdWVzdFNhdmVDYXJkIjpmYWxzZSwiZGV2aWNlRmluZ2VycHJpbnRpbmciOnsiVE0iOnsidXJsIjoiaHR0cHM6Ly90bS5jeWJlcnNvdXJjZS5jb20vZnAvdGFncy5qcz9vcmdfaWRcdTAwM2Qxc25uNW45d1x1MDAyNnNlc3Npb25faWRcdTAwM2QwNDA0X3Rlc3RjdHBkaXVpMDAxMjNlYTc4ZDctNDJlMi00MTZhLTkwYjAtNTAzOTI1OGQ4MTkwIiwic2Vzc2lvbklkIjoiMjNlYTc4ZDctNDJlMi00MTZhLTkwYjAtNTAzOTI1OGQ4MTkwIn19fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJhbW91bnREZXRhaWxzIjp7InRvdGFsQW1vdW50IjoiMjEuMDAiLCJjdXJyZW5jeSI6IlVTRCJ9LCJiaWxsVG8iOnsiYWRkcmVzczEiOiIxMjMgQ29vbCBTdHJlZXQiLCJhZG1pbmlzdHJhdGl2ZUFyZWEiOiJOWSIsImJ1aWxkaW5nTnVtYmVyIjoiMTIiLCJjb3VudHJ5IjoiVVMiLCJkaXN0cmljdCI6ImRpc3RyaWN0IiwibG9jYWxpdHkiOiJOZXcgWW9yayIsInBvc3RhbENvZGUiOiIxMDE3MiIsImVtYWlsIjoiYm9sdG9uakB2aXNhLmNvbSIsImZpcnN0TmFtZSI6IlZpa3RvciIsImxhc3ROYW1lIjoiVmF1Z2huIiwibWlkZGxlTmFtZSI6IkYiLCJuYW1lU3VmZml4IjoiSnIiLCJ0aXRsZSI6Ik1yIiwicGhvbmVOdW1iZXIiOiIrMTEyMzQ1Njc4OTAiLCJwaG9uZVR5cGUiOiJtb2JpbGUifSwic2hpcFRvIjp7ImFkZHJlc3MxIjoiNDU2IE5pY2UgQXZlbnVlIiwiYWRtaW5pc3RyYXRpdmVBcmVhIjoiQ0EiLCJidWlsZGluZ051bWJlciI6IjQwOSIsImNvdW50cnkiOiJVUyIsImRpc3RyaWN0IjoiVXB0b3duIiwibG9jYWxpdHkiOiJMb3MgQW5nZWxlcyIsInBvc3RhbENvZGUiOiI5MDAxMCIsImZpcnN0TmFtZSI6IkFsYW4iLCJsYXN0TmFtZSI6IlR1cmluZyJ9fSwidGFyZ2V0T3JpZ2lucyI6WyJodHRwczovL3Zhc2RlbW9zLnZpc2EuY29tIl0sImlmcmFtZXMiOnsibWNlIjoiL21jZS9tY2UuaHRtbCIsImJ1dHRvbnMiOiIvYnV0dG9ubGlzdC9idXR0b25saXN0Lmh0bWwiLCJzcmMiOiIvc2VjdXJlLXJlbW90ZS1jb21tZXJjZS9zcmMuaHRtbCIsImN0cCI6Ii9jdHAvY3RwLmh0bWwiLCJnb29nbGVwYXkiOiIvZ29vZ2xlcGF5L2dvb2dsZXBheS5odG1sIiwiYXBwbGVwYXkiOiIvYXBwbGVwYXkvYXBwbGVwYXkuaHRtbCIsInBhemUiOiIvcGF6ZS9wYXplLmh0bWwiLCJjaGVjayI6Ii9jaGVjay9jaGVjay5odG1sIiwiZ2EiOiIvZ2EvZ2EuaHRtbCIsIm9yYyI6Ii9vcmMvb3JjLmh0bWwiLCJ0bSI6Ii90bS90bS5odG1sIiwiYXBtIjoiL2FwbS9hcG0uaHRtbCIsImFwbS1zdGVwcGVyIjoiL2FwbS1zdGVwcGVyL2FwbS1zdGVwcGVyLmh0bWwifSwiY2xpZW50VmVyc2lvbiI6IjAuMzMiLCJjb3VudHJ5IjoiVVMiLCJsb2NhbGUiOiJlbl9VUyIsImFsbG93ZWRDYXJkTmV0d29ya3MiOlsiVklTQSIsIk1BU1RFUkNBUkQiLCJBTUVYIl0sImNvbXBsZXRlTWFuZGF0ZSI6eyJ0eXBlIjoiUFJFRkVSX0FVVEgiLCJ0cmFuc2FjdGlvbklkIjoiNWZqT2s0MEhFSTV5czRISFBWRFphR2NlMHYwWiIsImNvbnN1bWVyQXV0aGVudGljYXRpb24iOnsiYWxsb3dlZENhcmROZXR3b3JrcyI6WyJWSVNBIiwiQU1FWCIsIk1BU1RFUkNBUkQiXSwiYWxsb3dlZFBheW1lbnRUeXBlcyI6WyJDTElDS1RPUEFZIiwiUEFORU5UUlkiXX19LCJhbmFseXRpY3MiOnsiZ29vZ2xlIjp7InNjcmlwdCI6Imh0dHBzOi8vd3d3Lmdvb2dsZXRhZ21hbmFnZXIuY29tL2d0YWcvanMiLCJpZCI6IkctVEY4MDRETlY5OSJ9LCJldmVudEdyb3VwSWQiOiIxWUdTbGE0TTdmS3pqTV9pdlBMV2ZaeXVaT2ZFOV85S0FNZ3JZVjAweF96SWFhcEtPbU9SbnZ4LVVKdU1KU080In0sImNyIjoiNUYxZ3ZCeWJmTmZBcThIaEx5V1hlQmJVNFUtd2ZVSERkMDc1RThBMTRxdlpLWmdZQlJoQ0ltSkI0YklsbE95UFlWMzdvNVdSaURZYVpsaGJidXhZR1V5MVZvd1ZibUZOZjkxTk84MVVoRGhUc3NVN3pkbElUQkc1dFVwdmljMVVXb0dROXBWaDZ4eTZTLXZWNHFNIiwic2VydmljZU9yaWdpbiI6Imh0dHBzOi8vdGVzdHVwLmN5YmVyc291cmNlLmNvbSIsImNsaWVudExpYnJhcnkiOiJodHRwczovL3Rlc3R1cC5jeWJlcnNvdXJjZS5jb20vdWMvdjEvYXNzZXRzL2FwdzFIMHVjVThUbDl2MHBYX055MjJPRUcwR0RLcG9pQ01aTFNvd1ZUZXZCQUVBbml6Y2ptd25aNjZwaWdLcnl4TE45QzZ4alRwbUUybkxrY21ySzk1VlZDM0E1VWp6V0htbG4zaERyNFF0ZWYtQVM3eWNOTDN5ZXd2aGliTzR1ekJhdlpTSnc5VG1wd2FybkF6c1pSNnQ0L1NlY3VyZUFjY2VwdGFuY2UuanMiLCJsb2dnaW5nUGF0aCI6Ii91Yy92MS9sb2ctZXZlbnRzIiwiYXNzZXRzUGF0aCI6Ii91Yy92MS9hc3NldHMvYXB3MUgwdWNVOFRsOXYwcFhfTnkyMk9FRzBHREtwb2lDTVpMU293VlRldkJBRUFuaXpjam13blo2NnBpZ0tyeXhMTjlDNnhqVHBtRTJuTGtjbXJLOTVWVkMzQTVVanpXSG1sbjNoRHI0UXRlZi1BUzd5Y05MM3lld3ZoaWJPNHV6QmF2WlNKdzlUbXB3YXJuQXpzWlI2dDQiLCJjbGllbnRMaWJyYXJ5SW50ZWdyaXR5Ijoic2hhMjU2LWNRMXQ2R1FjTjVFbDRtbDFIMTBlYVNWK1R1Uy9oRnJ5YmxMTGw5cy94allcdTAwM2QifSwidHlwZSI6ImdkYS0wLjEwLjAifV0sImlzcyI6IkZsZXggQVBJIiwiZXhwIjoxNzY1ODI3MTQ0LCJpYXQiOjE3NjU4MjYyNDQsImp0aSI6Ims3b3kzcmh5S25McjQ0cGYifQ.Xa1Rw64mKGk9lr-25KWbbARmCTIF1wEabTxrRGU3tE_Pk1g0bPZP67T5vau81BNOn2pd2aaSKSQvywyuOMvgObkmg-vVKrasZtxHFGQUz-3F16j8y85p2fNElUwzl1s12dbPaA6IgsvZ47k2QGBmYcVq7aBAb9ia4zhORqHPb8B_gWuZoaMtBeH59DyLg1184XUiZ7-vEOaepZTJUcjH4g8DXlaOlwO0h8bHQTpLnjvHGyBU0ltNdePR-FoPUn0ZjnE22H-Mg0vncpE1V2qymtBMEXiESZjrz1SbYx3Wp1oYhCOvnikyxs4yH1eJPqrlRUw7eyPyRGjjecTe1S3aoA  
Decrypted Capture Context Header

```
{
          "kid": "zu", 
          "alg": "RS256"
          } 
```

Decrypted Capture Context Body with Selected Fields

```
{
  "flx": {
    // filled with token metadata 
  },
  "ctx": [
    {
      // filled with data related to your capture context request parameters 
      "data": {
        "clientLibrary": // taken dynamically from response ,
        "clientLibraryIntegrity": //taken dynamically from response: "sha256-cQ1t6GQcN5El4ml1H10eaSV+TuS/hFryblLLl9s/xjY="
      },
      "type": "gda-0.10.0"
    }
  ],
  "iss": "Flex API",
  "exp": 1765827144,
  "iat": 1765826244,
  "jti": "k7oy3rhyKnLr44pf"
}
```

Validating the Capture Context {#uc-validate-capture-context-intro}
===================================================================

The capture context that you generate is a JSON Web Token (JWT) data object. The JWT is digitally signed using a public key and confirms the validity of the JWT and that it comes from `Cybersource`. When you do not have a key in the JWT header, `Cybersource` recommends that you follow cryptography best practices and validate the capture context signature.  
To validate a JWT, you must obtain its public key. This public RSA key is in JSON Web Key (JWK) format. The public key is associated with the capture context on the `Cybersource` domain.  
To get the public key of a capture context from the header of the capture context itself, you must retrieve the key ID associated with the public key and then pass the key ID to the `/flex/v2/public-keys` endpoint:

1. From the header of the capture context, get the key ID (kid):

   ```
   {
       "kid": "3g",
       "alg": "RS256"
   }
   ```
2. Send a GET request to the `/flex/v2/public-keys` endpoint and include the key ID. For example:

   * **Test:** `GET ``https://apitest.cybersource.com``/flex/v2/public-keys/{3g}`
   * **Production:** `GET ``https://api.cybersource.com``/flex/v2/public-keys/{3g}`
   * **Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/public-keys/{3g}`
   * **Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/public-keys/{3g}`  
     Depending on the cryptographic method you use to validate the public key, you might need to convert the key to privacy-enhanced mail (PEM) format.
3. The resource returns the public key:

   ```
   eyJmbHgiOnsicGF0aCI6Ii9mbGV4L3YyL3Rva2VucyIsImRhdGEiOiI2bUFLNTNPNVpGTUk5Y3RobWZmd2doQUFFRGNqNU5QYzcxelErbm8reDN6WStLOTVWQ2c5bThmQWs4czlTRXBtT21zMmVhbEx5NkhHZ29oQ0JEWjVlN3ZUSGQ5YTR5a2tNRDlNVHhqK3ZoWXVDUmRDaDhVY1dwVUNZWlZnbTE1UXVFMkEiLCJvcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsInVzZSI6ImVuYyIsIm4iOiJyQmZwdDRjeGlkcVZwT0pmVTlJQXcwU1JCNUZqN0xMZjA4U0R0VmNyUjlaajA2bEYwTVc1aUpZb3F6R3ROdnBIMnFZbFN6LVRsSDdybVNTUEZIeTFJQ3BfZ0I3eURjQnJ0RWNEanpLeVNZSTVCVjNsNHh6Qk5CNzRJdnB2Smtqcnd3QVZvVU4wM1RaT3FVc0pfSy1jT0xpYzVXV0ZhQTEyOUthWFZrZFd3N3c3LVBLdnMwNmpjeGwyV05STUIzTS1ZQ0xOb3FCdkdCSk5oYy1uM1lBNU5hazB2NDdiYUswYWdHQXRfWEZ0ZGItZkphVUVUTW5WdW9fQmRhVm90d1NqUFNaOHFMOGkzWUdmemp2MURDTUM2WURZRzlmX0tqNzJjTi1OaG9BRURWUlZyTUtiZ3QyRDlwWkJ1d2gzZlNfS3VRclFWTVdPelRnT3AzT2s3UVFGZ1EiLCJraWQiOiIwOEJhWXMxbjdKTUhjSDh1bkcxc1NDUVdxN2VveWQ1ZyJ9fSwiY3R4IjpbeyJkYXRhIjp7InRhcmdldE9yaWdpbnMiOlsiaHR0cHM6Ly93d3cudGVzdC5jb20iXSwibWZPcmlnaW4iOiJodHRwczovL3Rlc3RmbGV4LmN5YmVyc291cmNlLmNvbSJ9LCJ0eXBlIjoibWYtMC4xMS4wIn1dLCJpc3MiOiJGbGV4IEFQSSIsImV4cCI6MTYxNjc3OTA5MSwiaWF0IjoxNjE2Nzc4MTkxLCJqdGkiOiJ6SG1tZ25uaTVoN3ptdGY0In0.GvBzyw6JKl3b2PztHb9rZXawx2T817nYqu6goxpe4PsjqBY1qeTo19R-CP_DkJXov9hdJZgdlzlNmRY6yoiziSZnGJdpnZ-pCqIlC06qrpJVEDob3O_efR9L03Gz7F5JlLOiTXSj6nVwC5mRlcP032ytPDEx5TMI9Y0hmBadJYnhEMwQnn_paMm3wLh2v6rfTkaBqd8n6rPvCNrWMOwoMdoTeFxku-
   ```

   Use this public RSA key to validate the capture context.

4. Parse the JWT capture context to get the kid from its header:

   ```
   {
       "kid": "3g",
       "alg": "RS256"
   }
   ```
5. Send a GET request to retrieve the public key from `/flex/v2/public-keys/3g`:

   ```
   {
       "kty":"RSA",    
       "use":"enc",
       "kid":"3g",
       "n":"ir7Nl1Bj8G9rxr3co5v_JLkP3o9UxXZRX1LIZFZeckguEf7Gdt5kGFFfTsymKBesm3Pe
        8o1hwfkq7KmJZEZSuDbiJSZvFBZycK2pEeBjycahw9CqOweM7aKG2F_bhwVHrY4YdKsp
        _cSJe_ZMXFUqYmjk7D0p7clX6CmR1QgMl41Ajb7NHI23uOWL7PyfJQwP1X8HdunE6ZwK
        DNcavqxOW5VuW6nfsGvtygKQxjeHrI-gpyMXF0e_PeVpUIG0KVjmb5-em_Vd2SbyPNme
        nADGJGCmECYMgL5hEvnTuyAybwgVwuM9amyfFqIbRcrAIzclT4jQBeZFwkzZfQF7MgA6QQ",
        "e":"AQAB"
   }
   ```

Session Validation {#uc-session-validate}
=========================================

The session JWT is digitally signed using RS256. You must confirm that it was issued by `Cybersource` and has not been tampered with. Follow these steps to validate the signature:

1. Parse the session JWT header to extract the key ID (`kid`):

   ```
   {
     "kid": "3g",
     "alg": "RS256"
   }
   ```
2. Retrieve the public key by sending a request to the `/flex/v2/public-keys/{kid}` endpoint:

   * **Test** : GET `apitest.cybersource.com``flex/v2/public-keys/{kid}`
   * **Production** : GET `api.cybersource.com``flex/v2/public-keys/{kid}`
3. Use the returned RSA public key in JSON Web Key format to verify the JWT signature.  
   IMPORTANT Depending on the cryptographic library that tou use, you may need to convert the key to Privacy-Enhanced Mail (PEM) format.

Transient Tokens {#ctp-tokens-intro}
====================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the checkout.mount() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.  
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.

Transient Token Format {#ctp-tokens-format}
===========================================

The transient token is issued as a JSON Web Token (JWT) ([RFC 7519](https://tools.ietf.org/html/rfc7519 "")). The payload portion of the token is a Base64URL-encoded JSON string and contains various claims. For more information, see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/ctp-appendix-jwts.md "").

Example: Transient Token Format {#uc-trans-tkn-ex}
==================================================

Encrypted Transient Token JWT

```
eyJraWQiOiIwMEl1NWJDT2NINVpPWjFNYldsQktodzFZeFFjSkVlZSIsImFsZyI6IlJTMjU2In0.eyJtZXRhZGF0YSI6eyJzZXF1ZW5jZU51bWJlciI6IjEiLCJjYXJkaG9sZGVyQXV0aGVudGljYXRpb25TdGF0dXMiOmZhbHNlLCJwYXltZW50VHlwZSI6IlNSQ01BU1RFUkNBUkQifSwiaXNzIjoiRmxleC8wMCIsInBheW1lbnRDcmVkZW50aWFsc1JlZmVyZW5jZSI6eyJ1Y19hZ25vc3RpY19wb3J0Zm9saW9fdmFsaWQiOiJXaWUyM2NBS3RGblFlSXpqeDRFUXgifSwiZXhwIjoxNzY1ODg1MDcyLCJ0eXBlIjoiZ2RhLTAuMTAuMCIsImlhdCI6MTc2NTg4NDE3MywianRpIjoiMUQwMlk4Q09FQURYS1k5VjRHTjRNUDJOSVNMVjNQM1dSUUNEV0VZNDJHUjNBRzIzTUI3WjY5NDE0NDkwQkI1MSIsImNvbnRlbnQiOnsiZGV2aWNlSW5mb3JtYXRpb24iOnsiZmluZ2VycHJpbnRTZXNzaW9uSWQiOnt9fSwicHJvY2Vzc2luZ0luZm9ybWF0aW9uIjp7InBheW1lbnRTb2x1dGlvbiI6eyJ2YWx1ZSI6IjAyNyJ9fSwib3JkZXJJbmZvcm1hdGlvbiI6eyJiaWxsVG8iOnsiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiZmlyc3ROYW1lIjp7fSwicGhvbmVOdW1iZXIiOnt9LCJhZGRyZXNzMSI6e30sInBvc3RhbENvZGUiOnt9LCJsb2NhbGl0eSI6e30sImFkbWluaXN0cmF0aXZlQXJlYSI6e30sImVtYWlsIjp7fX0sImFtb3VudERldGFpbHMiOnsidG90YWxBbW91bnQiOnt9LCJjdXJyZW5jeSI6e319LCJzaGlwVG8iOnsiZmlyc3ROYW1lIjp7fSwiY291bnRyeSI6e30sImxhc3ROYW1lIjp7fSwiYWRkcmVzczEiOnt9LCJwb3N0YWxDb2RlIjp7fSwibG9jYWxpdHkiOnt9LCJhZG1pbmlzdHJhdGl2ZUFyZWEiOnt9fX0sInBheW1lbnRJbmZvcm1hdGlvbiI6eyJjYXJkIjp7ImV4cGlyYXRpb25ZZWFyIjp7InZhbHVlIjoiMjAyNyJ9LCJudW1iZXIiOnsibWFza2VkVmFsdWUiOiJYWFhYWFhYWFhYWFg5OTA4IiwiYmluIjoiNTE4NjAwIn0sImV4cGlyYXRpb25Nb250aCI6eyJ2YWx1ZSI6IjAzIn0sInR5cGUiOnsidmFsdWUiOiIwMDIifSwidHlwZVNlbGVjdGlvbkluZGljYXRvciI6eyJ2YWx1ZSI6IjEifX19fSwiXyI6IkwrYnlQL2FIRnhEUDRPc0NGNFI5RkhjbElkZkFXR0g4VkF3NGdta0NubGRyZzQ3WDdnR1hseUZRTWM4aU5KWjBzSlNhTlFOTzM5RHVCVWdWaW1SeC9zRUJJS2VQYXFvRVRoWDZpRjFrWWs1ZkxjWDRqU1gvTmtzb1U0bGQzU0RNTnJHcS8ybDRoM0laTjd1WEVON1g5azA5K3FaRFNaWVk3S1dzaVJXeXNwcHpFZE5uQy9ORGYxY1ZqNUJHZTZnN3Jjckt0THYyT1VzYUIyb3hicVkwL2VuUFY4N0JHakMrUk9lSmFYa3VGeml0RDVrQ0paZHdoYnorRStRVmtnejdBVTZnNG5pa0dsWDFNUklkeXVVNnY4QlJsWG42ZEF3c252TW5pZ3Yvc05NUE4zV0hSaUhZWHZubTdramVOd2k2YW1EbkdTSzVqY3RFMmJPWDZUU0RmWG5RSE01eVhWcFdMRHZxa0VQOVZzM2NBNmhTbTlZcHFaaXRSSjZ5OWtMSGFNemsydm9TWlhUV1JQU210UkZ2TWdcdTAwM2RcdTAwM2QifQ.M1ttoaMyKz9NjQ7nYfhGqrt7Gga1YvUph8FH4-0aV98tNbZilEqF4ANQHKFjNQavJ5_EKB_4cDayuwa7xyZzrz2WNXSlRS97EJYfvFAYza8cq2SpvHlR1DvJdMuYsyui-fZafdkxqTudsAUUYJErWezliWOvCw2gi18hb3bS3V_evt8zznRdgbwd7Q1BgSmQwgnIDI-H4wdZMByMbpG1zC8UjbvyPB5OUQxOTCljmbsiAquSI_8LFJoasRUK9txVjezO49E_DX1ClETbnzuiUlJ6MzBlTNAtdbxGB5ELjuf8-SSj4ojlZZTMWARllskZsx_DUtqLBUdNXKpPKEJtzg
```

{#uc-trans-tkn-ex_codeblock_bagt_cfz_hjc}  
Decoded Transient Token JWT - Relay PAN

```
{
  "metadata": {
    "sequenceNumber": "1",
    "ccJti": "onNpuEB7TmCjcga2",
    "cardholderAuthenticationStatus": false,
    "paymentType": "PANENTRY"
  },
  "iss": "Flex/08",
  "paymentCredentialsReference": {
    "na_partner_ctp2": "P6RXHH8Lc79oT1DKS1_Rs"
  },
  "exp": 1778665181,
  "type": "uc-1.0.0",
  "iat": 1778664281,
  "jti": "1E3QZQ85MKIWE5EU8QUT4AVC2Y4J0Z8ZEQ4C7QDKZ28171QG12DD6A0446DD7118",
  "content": {
    "clientReferenceInformation": {
      "applicationVersion": {},
      "applicationUser": {},
      "code": {},
      "applicationName": {}
    },
    "deviceInformation": {
      "fingerprintSessionId": {}
    },
    "orderInformation": {
      "billTo": {
        "country": {},
        "lastName": {},
        "firstName": {},
        "phoneNumber": {},
        "address2": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {},
        "email": {}
      },
      "amountDetails": {
        "totalAmount": {},
        "currency": {}
      },
      "shipTo": {
        "firstName": {},
        "lastName": {},
        "country": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {}
      }
    },
    "paymentInformation": {
      "card": {
        "expirationYear": {
          "value": "2029"
        },
        "number": {
          "maskedValue": "XXXXXXXXXXXX1111",
          "bin": "411111"
        },
        "securityCode": {},
        "expirationMonth": {
          "value": "12"
        },
        "typeSelectionIndicator": {
          "value": "1"
        },
        "type": {
          "value": "001"
        }
      }
    }
  }
}
```

{#uc-trans-tkn-ex_codeblock_bgt_cfz_hjc}  
Decoded Transient Token JWT - Relay Network Token

```
{
  "metadata": {
    "sequenceNumber": "1",
    "tokenizedCard": {
      "card": {
        "expirationYear": "2033",
        "maskedValue": "XXXXXXXXXXXX2700",
        "prefix": "462294",
        "expirationMonth": "08"
      }
    },
    "ccJti": "9M2EooZC767DNhvC",
    "cardholderAuthenticationStatus": false,
    "paymentType": "SRCCARD"
  },
  "iss": "Flex/08",
  "paymentCredentialsReference": {
    "na_partner_ctp2": "U3lO1Flys1fcQmAWLzchn"
  },
  "exp": 1778665930,
  "type": "uc-1.0.0",
  "iat": 1778665030,
  "jti": "1E0T0CPF4S96D8P30Y89ID69U51WRHRWCTW896BX7K75ROSI6TMV6A0449CA2D1B",
  "content": {
    "clientReferenceInformation": {
      "applicationVersion": {},
      "applicationUser": {},
      "code": {},
      "applicationName": {}
    },
    "deviceInformation": {
      "fingerprintSessionId": {}
    },
    "processingInformation": {
      "paymentSolution": {
        "value": "027"
      }
    },
    "orderInformation": {
      "billTo": {
        "lastName": {},
        "country": {},
        "firstName": {},
        "phoneNumber": {},
        "address2": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {},
        "email": {}
      },
      "amountDetails": {
        "totalAmount": {},
        "currency": {}
      },
      "shipTo": {
        "country": {},
        "firstName": {},
        "lastName": {},
        "address1": {},
        "postalCode": {},
        "locality": {},
        "buildingNumber": {},
        "administrativeArea": {}
      }
    },
    "paymentInformation": {
      "tokenizedCard": {
        "expirationYear": {
          "value": "2033"
        },
        "transactionType": {},
        "number": {
          "maskedValue": "XXXXXXXXXXXX3278",
          "bin": "432312"
        },
        "expirationMonth": {
          "value": "08"
        },
        "type": {
          "value": "001"
        },
        "cryptogram": {}
      },
      "card": {
        "typeSelectionIndicator": {
          "value": "1"
        },
        "useAs": {
          "value": "D"
        }
      }
    }
  }
}
```

{#uc-trans-tkn-ex_codeblock_bgat_cfz_hjc}  
Authentication Status in metadata Object  
The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

{#uc-trans-tkn-ex_codeblock_fgt_cfz_hjc}

Token Verification {#ctp-tokens-verification}
=============================================

When you receive the transient token, you should cryptographically verify its integrity using the public key embedded within the capture context. Doing so verifies that `Cybersource` issued the token and that the data has not been tampered with in transit. Verifying the transient token JWT involves verifying the signature and various claims within the token. Programming languages each have their own specific libraries to assist. For an example in Java, see: [Java Example in Github](https://github.com/CyberSource/cybersource-unified-checkout-sample-java/blob/main/src/main/java/com/cybersource/example/service/JwtProcessorService.java "").

PAN BIN in metadata Object
--------------------------

The `cardDetails` object, including the PAN BIN, is included in the transient token `metadata` when a `Click to Pay` network token is used as a payment method. This allows you to display information about the card on invoices and see the BIN details that are linked to the underlying card.

```
"metadata": {
  "cardDetails": {
    "suffix": "9876",
    "prefix": "123456",
    "expirationMonth": "MM",
    "expirationYear": "YYYY"
  }
}
```

The `cardholderAuthenticationStatus` object is included in the `metadata` and enables you to determine if the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `true`, the payload is fully authenticated. When `cardholderAuthenticationStatus` is set to `false`, the transaction is not authenticated.

```
"metadata": {
  "cardholderAuthenticationStatus": "true"
  }
}
```

Dual-Branded Cards {#dual-co-brand-card-support}
================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["CARD", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Relay.  
During the transaction, the card type is populated with the first network in the list, and the detectedCardTypes field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Relay and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option that the customer selects during checkout.

Dual-Branded Cards {#ctp-dual-co-brand-card-support}
====================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["CARD", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Relay.  
During the transaction, the card type is populated with the first network in the list, and the detectedCardTypes field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Relay and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option that the customer selects during checkout.

Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the payment details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")
  {#uc-token-get-pymnt-details_ul_ogl_bgz_hjc}

> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d14e1140}
-----------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1147}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1159}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
The `{jti}` is the ID of the JWT within the transient token that is returned by `Unified Checkout`. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

Required Field for Retrieving Transient Token Payment Details {#ctp-token-get-pymnt-details-required}
=====================================================================================================

Your payment details request must include this field:

id
:
The `{id}` is the full JWT received from `Unified Checkout` as the result of capturing payment information.

REST Example: Retrieving Transient Token Payment Details {#uc-token-get-pymnt-details-ex-rest}
==============================================================================================

Request

```keyword
GET https://apitest.cybersource.com/flex/v2/payment-details/{jti}
```

{#uc-token-get-pymnt-details-ex-rest_codeblock_c51_vmt_gwb}  
Response to Successful Request

```
{
  "paymentInformation": {
    "card": {
      "expirationYear": "2026",
      "number": "XXXXXXXXXXXX1111",
      "expirationMonth": "05",
      "type": "001"
    }
  },
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "21.00",
      "currency": "USD"
    },
    "billTo": {
      "lastName": "Lee",
      "country": "US",
      "firstName": "Tanya",
      "email": "tanyalee@example.com"
    },
    "shipTo": {
      "locality": "Small Town",
      "country": "US",
      "administrativeArea": "CA",
      "address1": "123 Main Street",
      "postalCode": "98765"
    }
  }
}
```

{#uc-token-get-pymnt-details-ex-rest_codeblock_jpq_zfz_hjc}

Payment Credentials API {#ctp-token-get-pymnt-credentials}
==========================================================

This section contains the information you need to retrieve the full payment credentials collected by `Click to Pay Drop-In UI` using the payment credentials API. The payment information is returned in a redundantly signed and encrypted payment object. It uses the JSON Web Tokens (JWTs) as the data standard for communicating this sensitive data.

> IMPORTANT
> Payment information returned by the ` payment-credentials ` endpoint will contain Personal Identifiable Information (PII). Retrieving this sensitive information requires your system to comply with PCI security standards. For more information on PCI security standards, see: <https://www.pcisecuritystandards.org/>  
> The response is returned using a JWE data object that is encrypted with your public key created during the `Unified Checkout` tool's integration. For more information, see [Upload Your Encryption Key](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-upload-encrypt-key-intro.md "").  
> To decrypt the JWE response, use your private key created during the `Unified Checkout` tool's integration. The decrypted content is a JWS data object containing a JSON payload. This payload can be validated with the `Unified Checkout` public signature key.
> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned.

Returned Credentials
--------------------

A payment account number (PAN) or network token is returned on your request depending on your payment method and `Click to Pay` account status:

|     `Click to Pay` Account Status      | American Express |  Mastercard   |     Relay      |
|----------------------------------------|------------------|---------------|---------------|
| New card not saved in `Click to Pay`   | PAN              | PAN           | PAN           |
| New card saved in `Click to Pay`       | PAN              | Network Token | Network Token |
| Existing card stored in `Click to Pay` | PAN              | Network Token | Network Token |
[Payment Credentials Returned by Card Type and `Click to Pay` Account Status]

When you retrieve PAN information from the Payment Credentials API, the response includes the PAN, card expiration date, and the card verification value (CVV). When you retrieve network token information, the response includes the network token and network token cryptogram.

> IMPORTANT
> Relay and Mastercard always attempt to provision a network token. A PAN is returned when a network token is not provisioned before checkout or when the cardholder did not request to enroll the card in ` Click to Pay `.
> Network tokens are generated in the wallet of the `Click to Pay` token requestor ID (TRID). When tokenization is successful, Relay and Mastercard can also complete authentication during the `Click to Pay` experience to acquire a fully authenticated response. For information on authentication, see [Click to Pay Customer Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication.md "").

Endpoint {#ctp-token-get-pymnt-credentials_d14e634}
---------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-credentials/`*{paymentCredentialsReference}*{#ctp-token-get-pymnt-credentials_d14e641}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-credentials/`*{paymentCredentialsReference}*{#ctp-token-get-pymnt-credentials_d14e653}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-credentials/`*{paymentCredentialsReference}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-credentials/`*{paymentCredentialsReference}*  
The *{paymentCredentialsReference}* is the reference ID returned in the `id` field when you created the payment credentials.

Required Field for Retrieving Payment Credentials {#ctp-token-get-payment-credentials-required}
===============================================================================================

Your payment credentials request must include this field:

ReferenceID
:
The reference ID that is returned in the `paymentCredentialsReference.[organizationID]` field of the transient token data object after a successful `Click to Pay` interaction. This is an example `paymentCredentialsReference.[organizationID]` field in the transient token response payload:

    ```
    "paymentCredentialsReference": {
        "na_partner_ctp2": "qlXufLdFrU_TIIye497LN"
      },...
    ```

{#ctp-token-get-payment-credentials-required_codeblock_in4_3k1_2jc}

REST Example: Retrieving Payment Credentials {#ctp-token-get-payment-credentials-example-rest}
==============================================================================================

Request

```keyword
https://api.cybersource.com/flex/v2/payment-credentials/E-firqlLk7GiziQwXxAsq
```

Encrypted Response to Successful Request

```
eyJhdWQiOiJwc3AiLCJzdWIiOiJwc19ocGEiLCJraWQiOiIyMDIzMDUxNC1kcmFmdC1wc3AtZW5jcnlwdCIsI
mN0eSI6IkpXVCIsImVuYyI6IkEyNTZHQ00iLCJleHAiOjE2ODQxNDk2NjQsImFsZyI6IlJTQS1PQUVQLTI1Ni
IsImp0aSI6IjA0NDUwNWNiLTM1ZDYtNDU2ZS05OTBlLWRkZjQwYzI5NzlhNCJ9.enhUfZJOjbMX-wZPIOb1zj
8sFZiix6JSJyNw2i9QJ4k_hd7Iy_UMYvOmS-X1FJwjH0IQxMIblSV8XqMegIOm5dYBYdqouUfC8zq4Zm_dsMo
Tp3m9T6z-A_eJ8MGaxqTHSf2vWiXB-EMrww2eCXPyVTBkI1OdmYIX-s85vsqYpW-s0ThlCKaGI7B4_rJKNa7m
ou9VMBtBnfzhHLtnHDW8vsX8rLmTT76Ct2jMdIoQnlQRgEOi-zYu0Jm0gHERavUtq_7lDw9Ta73_TFw3KA2fs
G13CURyR7ZXoZy9_nRifwHjwNVbaFRceAzXoVtvM8H8F-ZzIC8AdA1FRye7RqcK9Q.OlrMxOMDkVDU6goS.TP
fBhm1eBfRjCSSvuT6SxFeZ3SGwOC6qX2Z4rlAEY9lOor2Q2E1CMqB6o-q6DNkGtASFONBzKtoB0yAgXBpx3S7
2FltR8bd40qmRnPyTOAscXa3eWbP45EqZqHW58lwUtMwcBORcfSjxPnWUo-OGmKCtIgiUO4MTlBsl9HdCLx7R
Wpwslo0pKQAuFrURHJyhdE1JUArgjNQMdQwPvCjoZ2RxTzECEqE1l0KmBGM-w8suowrnTNZl8cwVUZKzHQEJV
-twAGykQIIRCI3ydHfCupyUuA-5-Wvlk6nhcL3qND4JF-E3EIRpzm7WH8pCV5nzByUue-grHejg774c7fi1eh
fTBUZ8v6X7rTZUBLL0V5343X3zQQy_G-vq5qcaJZ8AS2XWSi17r8UEHoU5emYu5QAuXy1AhL32nDRZuXzOzQ1
9JsrTN2CD8qxU7tDpkUCEmY2GEMp4sd-rfu_2qBZDdr74tjYNgMsTIXSpgGDiwjLMJu4r460YencO6-JweGCT
8woIySjBRYpX1_axxcO6I9RUTSopPbslZwq_zpy3UuDa9InlSexM--fatYfAehY857F7bFVXlnXeqr7X0_Lri
bJsx6CWJU1ihjMVtnF-SxeE3IdpJxyFYBb7D1iL3ywFooxcGqarXU-3_CBuDHvnJFDC_iQPaeH7csb-EMeNqF
TmFf8dWNQYG7IJDfEnrnRW_XtnczH-ZS67iVuGzGwJZDQfJZ-KLhnWr6FE1EnT1VLyXPM78WeocT7cnLXmr9B
gevNmU3q_SV5nxlDLPuCqF0PmFNxaTjqfF2Qw_zOCvazwFWuBdUDdHilPqhj3gfsOesAJVA7VoTDw2U3zte3V
09KcJLaHygwPomopWOODinKzcZeWfJ39984pQa5cOMSEToGegkRZyvSxpf5PTht30uB3F3qC4cVLOu4qukYsr
jXqOtxg3icde7lXywfAtEZgf54jAP2Cl8JFmGWL5YnIY44-zj-GVz2C8iCN1CCUP3U4eVxz2GtxNNSXuwY8OR
Udino4rF-OpqqdjX5F0Uw6J2D3uR9cWB4Ee3v8TIA3-tRkG4ScAcclEwjkwsILPgVLU57HOm0AnaEsznyHrd9
-Qfz_p-UjbsaD3e-_sr56-x2UZVVL6TAMmJqmS2C55CHgkkhtHBCu-vb0KOmssopIvaQA5jK6ZoCftewE8-98
816ZmoU8Sty05PSeK0yBlxFwTIeJxt-moszRawFuBrLAbOu72y_eeUtk1tHpHV2Db7T6XvaRD4NvOFZg8ianY
Y6uHidoTl1ApjCp8VG9oTJ-uKWAEp9TU6qEHUswZZUIBeGTKjzBkRAQ20cZs5POb-qtjteoWo9QdnczipZ8de
my-FSZwNRFPkeedl3oHLepeTgwVnmij9ovk0e5Wqq2GVUMe8sLa-4eEnjliIjAVUQ9YNJBeqLf6_wo3HF8o2k
4ZgSJTuPHAuP41-D6sYrOcM6WvkCfKRTXw7ue5unri3M0Rpd2TEnzyw.TaLt6G8QyRykbrxb0iV9Jg
```

Decrypted Response Payment Credentials JWE - Relay PAN

```
{
  "aud": "na_partner_ctp2",
  "sub": "0404_testctpdiui001",
  "clientReferenceInformation": {
    "applicationVersion": "1.4.0",
    "applicationUser": "UC",
    "code": "1778664244584",
    "applicationName": "unifiedCheckout"
  },
  "deviceInformation": {
    "fingerprintSessionId": "ea5f708f-0a77-4623-bdf8-62bb656c4a1f"
  },
  "orderInformation": {
    "billTo": {
      "firstName": "firstName",
      "lastName": "lastName",
      "country": "GB",
      "phoneNumber": "07514573636",a
      "address2": "test address1",
      "address1": "test address1",
      "postalCode": "W26TT",
      "locality": "London",
      "buildingNumber": "",
      "administrativeArea": "",
      "email": "malachieuk@gmail.com"
    },
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "GBP"
    },
    "shipTo": {
      "country": "GB",
      "lastName": "lastName",
      "firstName": "firstName",
      "address1": "test address1",
      "postalCode": "W26TT",
      "locality": "London",
      "buildingNumber": "",
      "administrativeArea": ""
    }
  },
  "paymentInformation": {
    "card": {
      "expirationYear": "2029",
      "number": "FOURONE11111111111111",
      "securityCode": "123",
      "expirationMonth": "12",
      "type": "001",
      "typeSelectionIndicator": "1"
    }
  },
  "exp": 1778664881,
  "jti": "P6RXHH8Lc79oT1DKS1_Rs"
}
```

{#ctp-token-get-payment-credentials-example-rest_codeblock_bgt_cfzz_hjc}  
Decrypted Response Payment Credentials JWE - Relay Network Token

```
{
  "aud": "na_partner_ctp2",
  "sub": "0404_testctpdiui001",
  "clientReferenceInformation": {
    "applicationVersion": "1.4.0",
    "applicationUser": "UC",
    "code": "1778664940677",
    "applicationName": "unifiedCheckout"
  },
  "deviceInformation": {
    "fingerprintSessionId": "e8cc0b02-7eb3-476b-8253-055b39cdcb62"
  },
  "processingInformation": {
    "paymentSolution": "027"
  },
  "orderInformation": {
    "billTo": {
      "firstName": "David",
      "country": "GB",
      "lastName": "Pentland",
      "phoneNumber": "44 7514573636",
      "address2": "test address1",
      "address1": "17 Marius Avenue",
      "postalCode": "NE15 0EB",
      "locality": "Newcastle Upon Tyne",
      "buildingNumber": "",
      "administrativeArea": "",
      "email": "malachieuk@gmail.com"
    },
    "amountDetails": {
      "totalAmount": "100.00",
      "currency": "GBP"
    },
    "shipTo": {
      "lastName": "lastName",
      "firstName": "firstName",
      "country": "GB",
      "address1": "test address1",
      "postalCode": "W26TT",
      "locality": "London",
      "buildingNumber": "",
      "administrativeArea": ""
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "transactionType": "1",
      "expirationYear": "2033",
      "number": "FOURTHREE23126880583278",
      "expirationMonth": "08",
      "type": "001",
      "cryptogram": "Ax0AAGQfGv6nK5QDMx6WgIUxYeg="
    },
    "card": {
      "typeSelectionIndicator": "1",
      "useAs": "D"
    }
  },
  "exp": 1778665630,
  "jti": "U3lO1Flys1fcQmAWLzchn"
}
```

{#ctp-token-get-payment-credentials-example-rest_codeblock_bgt_cfz_hajc}

JavaScript API Reference {#ctp-appendix-js-reference_api_reference}
===================================================================

This reference provides details about the JavaScript API for creating the `Click to Pay Drop-In UI` payment form.

Class: Accept {#ctp-appendix-js-class-accept}
=============================================

Accept
------

**Returns**  
Type: Promise.\&lt;Accept\&gt;  
**Example**  
*Basic Setup*

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" integrity=”[INSERT clientLibraryIntegrity VALUE HERE]” crossorigin=”anonymous”&gt;&lt;/script&gt;
//Note: Script location and integrity value should be sourced from the capture context response clientLibrary and clientLibraryIntegrity values.
&lt;script&gt; Accept('header.payload.signature').then(function(accept) {
// use accept object
});
&lt;/script&gt;
```

Methods
-------

**dispose()**` → {void}`  
Dispose of this Accept instance.  
**Returns**  
Type: void
**unifiedPayments(sidebar)**` → `**{Promise.&lt;UnifiedPayments&gt;}**  
Create a Unified Payments integration.

| Name    | Type    | Attributes         | Description                                                                                                                                                                                                                                                                                      |
|:--------|:--------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sidebar | Boolean | \&lt;optional\&gt; | Set the option to `false` to enable embedded functionality of Unified Checkout. This will configure Unified Checkout to place the Payment Entry form inline. If this value is not set, the default is `true` and Unified Checkout will open the Payment Entry form in the sidebar configuration. |
[Parameters]

**Throws:** AcceptError  
**Returns:**  
Type: Promise.\&lt;UnifiedPayments\&gt;  
**Examples**  
*Minimal Setup - sidebar*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
```

*Embedded Payment Entry*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments(false))
```

*Error Handling*

```
const captureContext = document.getElementById('captureContext').value;

Accept(captureContext)
    .then(accept =&gt; accept.unifiedPayments())
    .then(up =&gt; up.show(showArgs))
    .then(tt =&gt; {
        document.getElementById('transientToken').value = tt;
        document.getElementById("authForm").submit();
    })
    .catch(error =&gt; {
                console.error(error);
                document.getElementById('logo').text = `Checkout error: ${JSON.stringify(error)}. Try again.`;
            });
```

Class: AcceptError {#ctp-appendix-js-class-accept-error}
========================================================

AcceptError
-----------

This class defines how errors are returned by the Unified Checkout JavaScript.

Members
-------

`(static, readonly) Reason Codes - Accept object creation`  
Possible errors that can occur during the creation of an Accept object.

| Name                    | Type   | Description                                                                  |
|:------------------------|:-------|:-----------------------------------------------------------------------------|
| CAPTURE_CONTEXT_INVALID | string | Occurs when you pass an invalid JWT.                                         |
| CAPTURE_CONTEXT_EXPIRED | string | Occurs when the JWT you pass has expired.                                    |
| SDK_XHR_ERROR           | string | Occurs when a network error is encountered while attempting to load the SDK. |
[Properties:]

`(static, readonly) Reason Codes - Show Errors`  
Possible errors that can occur during the rendering of payment selection list.

| Name                                 | Type   | Description                                                                         |
|:-------------------------------------|:-------|:------------------------------------------------------------------------------------|
| CHECKOUT_ERROR                       | string | Occurs when checkout failed to load.                                                |
| CLICK_TO_PAY_SDK_LOAD_ERROR          | string | Occurs when the `Click to Pay` SDK fails to load.                                   |
| ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR | string | Occurs when the card encryption for SRC enrollment fails to load.                   |
| LAUNCH_SRC_CHECKOUT_ERROR            | string | Occurs when the SRC checkout fails to load.                                         |
| SHOW_LOAD_CONTAINER_SELECTOR         | string | Occurs when a DOM element cannot be located using the supplied CSS Selector string. |
| SHOW_LOAD_ERROR                      | string | Occurs when there is an issue loading the payment iframe.                           |
| SHOW_LOAD_INVALID_CONTAINER          | string | Occurs when an invalid container parameter is supplied.                             |
| SHOW_LOAD_SIDEBAR_OPTIONS            | string | Occurs when an invalid container parameter is supplied when sidebar is selected.    |
| SHOW_PAYMENT_TIMEOUT                 | string | Occurs when an error is encountered during the handling of a payment option.        |
| SHOW_PAYMENT_UNAVAILABLE             | string | Occurs when no payment types can be presented to the customer.                      |
| SHOW_TOKEN_TIMEOUT                   | string | Occurs when the createToken call is unable to proceed.                              |
| SHOW_TOKEN_XHR_ERROR                 | string | Occurs when a network error is encountered while attempting to create a token.      |
| UNIFIED_PAYMENTS_ALREADY_SHOWN       | string | Occurs when you attempt to show a Unified Payments instance multiple times.         |
| UNKNOWN_ERROR                        | string | Occurs when an unknown error has occurred.                                          |
[Properties:]

`(static, readonly) Reason Codes - Unified Payments Errors`  
Possible errors that can occur during the creation of a Unified Payments object.

| Name                                | Type   | Description                                                                               |
|:------------------------------------|:-------|:------------------------------------------------------------------------------------------|
| CREATE_TOKEN_TIMEOUT                | string | Occurs when the createToken call times out.                                               |
| CREATE_TOKEN_XHR_ERROR              | string | Occurs when a network error is encountered while attempting to create a token.            |
| UNIFIED_PAYMENTS_PAYMENT_PARAMETERS | string | Occurs when no valid payment parameters exist while initializing button.                  |
| UNIFIED_PAYMENTS_VALIDATION_PARAMS  | string | Occurs when there's an issue with the parameters supplied to UnifiedPayments constructor. |
[Properties:]

`(nullable) correlationId :string`  
The correlationId of any underlying API call that resulted in this error.  
**Type:** string
`(nullable) details :array`  
Additional error-specific information.  
**Type:** array
`(nullable) informationLink :string`  
A URL link to online documentation for this error.  
**Type:** string
`message :string`  
A human-readable explanation of the error that has occurred.  
**Type:** string
`reason :string`  
A reason corresponding to the specific error that has occurred.

Class: UnifiedPayments {#ctp-appendix-js-class-unified-payments}
================================================================

UnifiedPayments
---------------

An instance of this class is returned upon the creation of a Unified Payments integration using accept.unifiedPayments(). Using this object you can add the payment options list to your checkout.

Methods {#ctp-appendix-js-class-unified-payments_section_n1t_k5v_ncc}
---------------------------------------------------------------------

`hide() → {Promise}`  
Hide button list.  
**Returns:** Type Promise  
**Example**  
Basic Usage

```
up.hide()
  .then(() =&gt; console.log('Hidden'))
  .catch(err =&gt; console.error(err));
```

`show(optionsopt) → {Promise.&lt;UnifiedPayments~TransientToken}`  
Show button list.

| Name             | Type   | Attributes         | Description                                                                                                                  |
|:-----------------|:-------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| options          | object | \&lt;optional\&gt; |                                                                                                                              |
| containers       | object | \&lt;optional\&gt; | CSS selectors to locate containers in which to place various UI elements. If not specified, these will operate in a sidebar. |
| paymentSelection | string | \&lt;optional\&gt; | For showing payment buttons.                                                                                                 |
| paymentScreen    | string | \&lt;optional\&gt; | For the main payment flows.                                                                                                  |
[Parameters]

**Returns:** Type Promise  
**Examples**  
Basic Usage With Full Sidebar Experience

```
const showArgs = {
            containers: {
                paymentSelection: #buttonPaymentListContainer'
            }
        };

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

All Screens Embedded in Containers

```
const showArgs = {
  containers: {
    paymentSelection: '#buttonPaymentListContainer',
    paymentScreen:  '#embeddedPaymentContainer'
  }
};

up.show(showArgs).then(transientToken =&gt; console.log(transientToken));
```

Type Definitions
----------------

**TransientToken**  
The response to a successful customer interaction with Unified Checkout is a transient token. The transient token is a reference to the payment data collected on your behalf. Tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that lasts 15 minutes. This reduces your PCI burden and responsibility and ensures that sensitive information is not exposed to your backend systems.  
It is in a JSON Web Token format. The payload of the transient token may contain useful metadata in relation to the stored sensitive info. However , all of this info is safe to use and store on your systems.  
The transient token can be used to complete a payment or other services, after which the transient data will be evicted from the token store.  
**Type:** string  
**Examples**  
How to Split the Transient Token

```
const transientToken = 'hhhhhhhhhh.pppppppppp.sssssssssss';

const segments = transientToken.split('.');
const urlBase64Decode = (s) =&gt; atob(s.replace(/_/g, '/').replace(/-/g, '+'));

const header = JSON.parse(urlBase64Decode(segments[0]));
const payload = JSON.parse(urlBase64Decode(segments[1]));
const signature = segments[2];
```

Decoded Body

```
{
  "iss" : "Flex/00",
  "exp" : 1706910242,
  "type" : "gda-0.9.0",
  "iat" : 1706909347,
  "jti" : "1D1I2O2CSTMW3UIXOKEQFI4OQX1L7CMSKDE3LJ8B5DVZ6WBJGKLQ65BD6222D426",
  "content" : {
    "orderInformation" : {
      "billTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "amountDetails" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      },
      "shipTo" : {
        // Empty fields present within this node indicate which fields were captured by
        // the application without exposing you to personally identifiable information
        // directly.
      }
    },
    "paymentInformation" : {
      "card" : {
        "expirationYear" : {
          "value" : "2028"
        },
        "number" : {
          "maskedValue" : "XXXXXXXXXXXX1111",
          "bin" : "411111"
        },
        "securityCode" : { },
        "expirationMonth" : {
          "value" : "06"
        },
        "type" : {
          "value" : "001"
        }
      }
    }
  }
}
```

VAS.UnifiedCheckout(sessionJWT) {#ctp_appendix_js_initialize}
=============================================================

This is a factory function that initializes the SDK. It returns a frozen, immutable client interface.

|     Name     |   Type   | Required? |                            Description                            |
|--------------|----------|-----------|-------------------------------------------------------------------|
| `sessionJWT` | `string` | Yes       | Signed JSON Web Token (JWT) from the server-side session endpoint |
[VAS.UnifiedCheckout(sessionJWT) Parameters]

**Returns**
:
`Promise&lt;UnifiedCheckoutInterface&gt;`

**Errors**
:
Returns `UnifiedCheckoutError` with reason `CAPTURE_CONTEXT_INVALID` if the JWT signature is invalid, or `UNUSED_TARGET_ORIGINS` if the current page origin is not in the JWT's `targetOrigins` list.

**Example**
:

    ```
    const client = await VAS.UnifiedCheckout(sessionJWT);
    ```

UnifiedCheckoutInterface {#ctp-appendix-js-interface}
=====================================================

The client object returned by `VAS.UnifiedCheckout()`. All methods throw an `Error` if called after `destroy()`.

client.createCheckout(options?) {#ctp-appendix-js-interface_section_zcx_g1s_hjc}
--------------------------------------------------------------------------------

|   Name    |          Type           | Required? |          Description           |
|-----------|-------------------------|-----------|--------------------------------|
| `options` | `CreateCheckoutOptions` | No        | Configuration for the checkout |
[client.createCheckout(options?) Parameters]

|     Property     |   Type    |            Default             |                 Description                 |
|------------------|-----------|--------------------------------|---------------------------------------------|
| `autoProcessing` | `boolean` | Inferred from capture context. | `false`: `mount()` returns transient token. |
[`CreateCheckoutOptions` Properties]

**Returns**
:
`Promise&lt;Checkout&gt;`

**Example**
:

    ```
    const checkout = await client.createCheckout({ autoProcessing: false });
    ```

    {#ctp-appendix-js-interface_codeblock_edx_g1s_hjc}

{#ctp-appendix-js-interface_dl_ddx_g1s_hjc}

client.createTrigger(paymentType, options?) {#ctp-appendix-js-interface_section_fdx_g1s_hjc}
--------------------------------------------------------------------------------------------

|     Name      |          Type          | Required? |                      Description                      |
|---------------|------------------------|-----------|-------------------------------------------------------|
| `paymentType` | `AllowedPaymentType`   | Yes       | Support trigger of the UI from client- driven button. |
| `options`     | `CreateTriggerOptions` | No        | The configuration for the trigger.                    |
[client.createTrigger(paymentType, options?) Parameters]

**Returns**
:
`Trigger`

**Example**
:

    ```
    const trigger = client.createTrigger(CLICKTOPAY);
    ```

    {#ctp-appendix-js-interface_codeblock_jdx_g1s_hjc}

{#ctp-appendix-js-interface_dl_idx_g1s_hjc}

client.on(event, callback) {#ctp-appendix-js-interface_section_qdx_g1s_hjc}
---------------------------------------------------------------------------

Subscribes to a client-level event and returns an unsubscribe function.

|    Name    |    Type    | Required? |                                                    Description                                                     |
|------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------|
| `event`    | `string`   | Yes       | Event name. Possible values: * `*` * `created` * `destroyed` * `error` {#ctp-appendix-js-interface_ul_sdx_g1s_hjc} |
| `callback` | `function` | Yes       | Handler function that receives event-specific payload.                                                             |
[client.on(event, callback) Parameters]

**Returns**
:
`Unsubscribe`: A function that removes the handler when called.

**Errors**
:
Returns `Error` when `event` is not a valid event name with reason `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` when the payment type cannot be used with a trigger.

**Example**
:

    ```
    const unsubscribe = client.on('error', (err) =&gt; {
      console.error(err.source, err.code, err.message);
    });

    // Later
    unsubscribe();
    ```

    {#ctp-appendix-js-interface_codeblock_vdx_g1s_hjc}

{#ctp-appendix-js-interface_dl_udx_g1s_hjc}

client.off(event, callback?) {#ctp-appendix-js-interface_section_wdx_g1s_hjc}
-----------------------------------------------------------------------------

Removes an event handler. This method is permissive --- calling it with an unknown event or callback does not throw.

|    Name    |    Type    | Required? |                                          Description                                           |
|------------|------------|-----------|------------------------------------------------------------------------------------------------|
| `event`    | `string`   | Yes       | Event name to unsubscribe from                                                                 |
| `callback` | `function` | No        | Specific handler to remove. When this is not included, all handlers for the event are removed. |
[client.off(event, callback?) Parameters]

client.destroy() {#ctp-appendix-js-interface_section_ydx_g1s_hjc}
-----------------------------------------------------------------

Permanently destroys the client. Returns a `destroyed` event, clears all event listeners, and marks the instance as destroyed.  
You can call `destroy()` multiple times.

client.isDestroyed() {#ctp-appendix-js-interface_section_zdx_g1s_hjc}
---------------------------------------------------------------------

Returns a value of `true` if client.destroy() is called.

Checkout {#ctp-appendix-js-checkout}
====================================

This field is returned by `client.createCheckout()` and manages the full checkout UI lifecycle.

checkout.mount(target) {#ctp-appendix-js-checkout_section_c32_hbs_hjc}
----------------------------------------------------------------------

Subscribes to a client-level event and returns an unsubscribe function.

|   Name   |               Type               | Required? |                                                               Description                                                               |
|----------|----------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `target` | `string` or `CheckoutContainers` | No        | CSS selector string for sidebar mode, or an object with `paymentSelection` and `paymentScreen` for embedded mode. Omit for full sidebar |
[checkout.mount(target) Parameters]

|      Property      |   Type   | Default |                                           Description                                           |
|--------------------|----------|---------|-------------------------------------------------------------------------------------------------|
| `paymentSelection` | `string` | Yes     | CSS selector for the button list container                                                      |
| `paymentScreen`    | `string` | No      | CSS selector for the payment form container. If omitted, payment screens appear in sidebar mode |
[`CheckoutContainers` Properties]

**Returns**
:
`Promise&lt;string&gt;`: This is a transient token JWT when `autoProcessing: false`.

**Errors**
:
Returns `UnifiedCheckoutError`. For information about how to handle mount error codes, see [Handle Errors](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-testing-intro/ctp-handle-errors.md "").

**Example**
:

    ```
    // Sidebar
    const result = await checkout.mount('#buttons');

    // Embedded
    const result = await checkout.mount({
      paymentSelection: '#buttons',
      paymentScreen: '#form'
    });
    ```

    {#ctp-appendix-js-checkout_codeblock_g32_hbs_hjc}

{#ctp-appendix-js-checkout_dl_f32_hbs_hjc}

checkout.unmount() {#ctp-appendix-js-checkout_section_h32_hbs_hjc}
------------------------------------------------------------------

Removes the payment UI from the page. The checkout is not destroyed --- you can call `mount()` again.

checkout.isMounted() {#ctp-appendix-js-checkout_section_n32_hbs_hjc}
--------------------------------------------------------------------

Returns `true` when the checkout UI is mounted.

checkout.isDestroyed() {#ctp-appendix-js-checkout_section_o32_hbs_hjc}
----------------------------------------------------------------------

Returns `true` when `destroy()` is called.

checkout.on(event, handler) {#ctp-appendix-js-checkout_section_p32_hbs_hjc}
---------------------------------------------------------------------------

Subscribes to a checkout-level event and returns an unsubscribe function.  
Valid events:

* `mounted`
* `ready`
* `unready`
* `unmounted`
* `destroyed`
* `paymentMethodSelected`
* `paymentMethodCancelled`
* `paymentMethodUpdate"`
* `error`
* `*`
  {#ctp-appendix-js-checkout_ul_q32_hbs_hjc}

checkout.off(event, handler?) {#ctp-appendix-js-checkout_section_r32_hbs_hjc}
-----------------------------------------------------------------------------

Removes a checkout event handler.

checkout.destroy() {#ctp-appendix-js-checkout_section_s32_hbs_hjc}
------------------------------------------------------------------

Permanently destroys the checkout. This field removes the payment UI, cleans up iframes, and emits a `destroyed` event.

Trigger {#ctp-appendix-js-trigger}
==================================

The trigger is returned by `client.createTrigger()` and programmatically launches a specific payment method.

trigger.mount(target?) {#ctp-appendix-js-trigger_section_nmc_sbs_hjc}
---------------------------------------------------------------------

Launches the payment method UI.

|   Name   |   Type   | Required? |                      Description                       |
|----------|----------|-----------|--------------------------------------------------------|
| `target` | `string` | No        | CSS selector for embedded mode. Omit for sidebar mode. |
[trigger.mount(target?) Parameters]

**Returns**
:
`Promise&lt;string&gt;`: A transient token or completed payment result.
{#ctp-appendix-js-trigger_dl_pmc_sbs_hjc}

**Example**
:

    ```
    const result = await trigger.mount('#payment-screen');
    ```

    {#ctp-appendix-js-trigger_codeblock_smc_sbs_hjc}

{#ctp-appendix-js-trigger_dl_rmc_sbs_hjc}

trigger.unmount() {#ctp-appendix-js-trigger_section_tmc_sbs_hjc}
----------------------------------------------------------------

Hides the payment method UI. The trigger is not destroyed.

trigger.isMounted() {#ctp-appendix-js-trigger_section_vmc_sbs_hjc}
------------------------------------------------------------------

Returns a boolean value.

trigger.isDestroyed() {#ctp-appendix-js-trigger_section_wmc_sbs_hjc}
--------------------------------------------------------------------

Returns a boolean value.

trigger.on(event, handler) {#ctp-appendix-js-trigger_section_xmc_sbs_hjc}
-------------------------------------------------------------------------

Subscribes to trigger events. Same event names and payloads as checkout events.

trigger.off(event, handler?) {#ctp-appendix-js-trigger_section_ymc_sbs_hjc}
---------------------------------------------------------------------------

Removes a trigger event handler.

trigger.destroy() {#ctp-appendix-js-trigger_section_zmc_sbs_hjc}
----------------------------------------------------------------

Permanently destroys the trigger.

Events {#ctp_appendix_js_events}
================================

`Click to Pay` provides a type-safe event system for monitoring the payment lifecycle. Events are emitted at the client and integration levels.

Subscribe to Events {#ctp_appendix_js_events_section_r13_l2n_djc}
-----------------------------------------------------------------

Use `on()` to subscribe to events. this returns an unsubscribe function:

```
const unsubscribe = checkout.on('ready', (data) =&gt; {
  console.log('Ready:', data.availablePaymentMethods);
});

// Later, remove the handler
unsubscribe();
```

You can use `off()` to remove a specific handler:

```
function onReady(data) { /* ... */ }

checkout.on('ready', onReady);
checkout.off('ready', onReady);
```

`Unified Checkout` Configuration {#ctp-configuration-intro}
===========================================================

This section contains information necessary to configure `Unified Checkout` in the `Business Center`:

* [Upload Your Encryption Key](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-upload-encrypt-key-intro.md "")
* [Enable Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-getting-started-integration-flow/ctp-enable-digital-pay-intro.md "")
* [Manage Permissions](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-manage-permissions-intro.md "")

Upload Your Encryption Key {#uc-upload-encrypt-key-intro}
=========================================================

Payment information can be retrieved from the `Unified Checkout` platform by invoking the Payment Credentials API. This API retrieves all of the data captured by `Unified Checkout`. This information is transmitted in an encrypted format to ensure the security of the payment information while in transit.  
You must generate an encryption key pair to retrieve this encrypted payment information, and the public encryption key must uploaded to the `Unified Checkout` system.

Generate a Public Private Key Pair {#uc-generate-keypair}
=========================================================

You must generate a public-private key pair to upload to the `Unified Checkout` system. The public key is uploaded to the `Unified Checkout` platform and is used to encrypt sensitive information in transit. The private key is used to decrypt the sensitive payment information on your server. Only the private key can properly decrypt the payment information.
IMPORTANT You must secure your private decryption key. This key must never be exposed to any external systems or it will risk the integrity of the secure channel.  
`Unified Checkout` accepts only keys that meet these requirements:
* Only RSA keys are supported. Elliptical curves are not supported.
* The minimum accepted RSA key size is 2048 bits.
  * RSA keys must be in JWK format. More information on JWK format is available here:  
    [rfc7517](https://datatracker.ietf.org/doc/html/rfc7517 "").
* The key ID must be a valid UUID.

Uploading Your Key Pair {#uc-upload-key}
========================================

When you have generated your encryption key pairs, you can upload your key to the `Unified Checkout` platform. Keys can be loaded at any hierarchy that is enabled for them and are used for all child entities that do not have keys loaded. You can upload a key at parent and child levels, but child keys override parent keys.  
Follow these steps to upload your key pair:

1. Navigate to Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` configuration page opens.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-decrypt-pay-details.png/jcr:content/renditions/original)
2. Click Enabled. You can upload your key in the appropriate section.
3. Upload the public encryption key in JWK format, and click Save.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-upload-pub-key.png/jcr:content/renditions/original)

Enable `Click to Pay` {#ctp_enable_digital_pay_intro}
=====================================================

To enable `Click to Pay` on `Unified Checkout`, you must first register `Click to Pay`. This process sends the appropriate information to the digital payment systems and registers your page with each system.  
Enable `Click to Pay` for `Unified Checkout` in the `Business Center`. `Click to Pay` is listed as an available digital payment method offered by `Unified Checkout`.

Enabling `Click to Pay` {#uc-enable-digital-pay-ctp}
====================================================

To begin your integration, you must first enable `Click to Pay`. `Click to Pay` is a digital payment solution that allows customers to pay with their preferred card network and issuer without entering their card details on every website. Customers can use Relay, Mastercard, and American Express cards to streamline their purchase experience. `Click to Pay` provides a fast, secure, and consistent checkout experience across devices and browsers.  
Follow these steps to enable in `Click to Pay` on `Unified Checkout`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-enable-digital-pay-ctp_step-1}
   {#uc-enable-digital-pay-ctp_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
   Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original) {#uc-enable-digital-pay-ctp_step-2}
   {#uc-enable-digital-pay-ctp_step-2}

3. In the Payment Options section, click **Manage**. The Payment Options page appears.

4. Click **Manage** next to `Click to Pay`. The `Click to Pay` configuration page appears.

5. Enter your business name and website URL.

6. Click Submit.

7. Contact your implementation contact or technical account manager to request that you be enabled for tokenization within `Click to Pay`. Your implementation contact or technical account manager will confirm that you were configured successfully and that you can now accept digital payments with `Click to Pay`.

   > IMPORTANT
   > ` Click to Pay ` uses network tokenization for transactions. These network tokens are stored in the vault of the token requestor ID (TRID) for the card scheme.

Manage Permissions {#uc-manage-permissions-intro}
=================================================

Portfolio administrators can set permissions for new or existing `Business Center` user roles for `Unified Checkout`. Administrators retain full read and write permissions. They enable you to regulate access to specific pages and specify who can access, view, or amend digital products within `Unified Checkout`.  
Portfolio administrators must apply the appropriate user role permission for any existing or newly created `Business Center` user roles for `Unified Checkout`. For information on managing permissions as a portfolio administrator, see [Managing Permissions as a Portfolio Administrator](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-manage-permissions-intro/uc-manage-permissions-port.md "").  
If you are a transacting merchant, you might find that your permissions are restricted. If your permissions are restricted, a message appears indicating that you do not have access, or buttons might appear gray. To make changes to your digital products within `Unified Checkout` that have restricted permissions, contact your portfolio administrator's customer support representative. For more information, see [Managing Permissions as a Direct Merchant](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-manage-permissions-intro/uc-manage-permissions-merch.md "").

Managing Permissions as a Direct Merchant {#uc-manage-permissions-merch}
========================================================================

Follow these steps to configure and manage user permissions in the `Business Center` for `Unified Checkout` as a direct merchant:

1. On the left navigation panel, navigate to Account Management.

2. Click Roles to display a list of your user roles.

3. Click the pencil icon next to the user role that you want to update.

4. Click Payment Configuration Permission.

5. Select the relevant permission for the specific user role you are editing. You can select from these `Unified Checkout` permissions:

   * Unified Checkout View
   * Unified Checkout Manage

   > IMPORTANT  
   > If you are a transacting merchant without view permissions, ` Unified Checkout ` will still appear on the navigation bar, however, a *no access* message appears when you access ` Unified Checkout `.  
   > If you are a transacting merchant with view permissions but not management permissions, you can access the ` Unified Checkout ` screens and view the different payment methods configurations, however, you cannot edit or enroll new products.

Managing Permissions as a Portfolio Administrator {#uc-manage-permissions-port}
===============================================================================

Follow these steps to configure and manage user permissions in the `Business Center` for `Unified Checkout` as a portfolio administrator:

1. On the left navigation panel, navigate to Account Management.{#uc-manage-permissions-port_step-1}
   {#uc-manage-permissions-port_step-1}

2. Click Roles to see a list of your user roles.{#uc-manage-permissions-port_step-2}
   {#uc-manage-permissions-port_step-2}

3. Click the pencil icon next to the user role that you want to update.{#uc-manage-permissions-port_step-3}
   {#uc-manage-permissions-port_step-3}

4. Click Payment Configuration Permission. {#uc-manage-permissions-port_step-4}
   {#uc-manage-permissions-port_step-4}

5. Select the relevant permission for the specific user role you are editing. You can choose from these `Unified Checkout` permissions:

   * Unified Checkout View
   * Unified Checkout Manage
   * Unified Checkout Portfolio View (available for portfolio users only)
   * Unified Checkout Portfolio Manage (available for portfolio users only)

   > IMPORTANT  
   > If all permissions are left unselected, the user has restricted permission. A *no access* message appears when the user tries to access the ` Unified Checkout ` digital product enablement pages. The user is advised to contact a customer representative.  
   > If a portfolio user has view permissions and does not have a management role, they can access the ` Unified Checkout ` pages, but they cannot modify toggles for different digital payments.
   > {#uc-manage-permissions-port_step-5}
   > {#uc-manage-permissions-port_step-5}

Click to Pay Customer Authentication {#ctp-authentication}
==========================================================

When you enable customer authentication through Click to Pay, you give `Cybersource` permission to request that Relay and Mastercard provide an authenticated payload for each transaction. Authentication takes place within the authentication service of each card type. You must inspect the payload that is returned to you to determine if the transaction is authenticated.  
For information about enabling customer authentication through Click to Pay, see these topics:

* [Enable Click to Pay Customer Authentication Using the API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication/boarding-click-to-pay-auth-enable-intro.md "")
* [Enable Click to Pay Customer Authentication Using the Business Center](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/ctp-authentication/ctp-authentication-config-ebc.md "")
  {#ctp-authentication_ul_iyg_v1b_3jc}  
  When the customer completes a transaction using a Relay or Mastercard Click to Pay credentials, authentication is managed within Click to Pay. When the customer checks out using manual card entry and does not save their card to Click to Pay, the transaction is not processed through Click to Pay and you must complete authentication based on your existing authentication method.

> IMPORTANT
> American Express cards cannot be authenticated through Click to Pay customer authentication. You must use another authentication method for this card type.

Authentication Flow {#ctp-authentication_section_rkj_xcs_hjc}
-------------------------------------------------------------

This image shows the Click to Pay authentication flow:  
![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/uc-ctp-auth-flow-vas-740x475.svg/jcr:content/renditions/original)

Set Up Customer Authentication for Click to Pay {#uc-authentication-steps}
==========================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. These authentication methods are available:

* `3-D Secure`
* Payment Passkey
* Card verification value (CVV)
* One-time password (OTP)

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-authentication-steps_step-1}
   {#uc-authentication-steps_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.  
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.  
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)  
   If Click to Pay is not enabled, click **On** next to Click to Pay.  
   ![Manage Available Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#uc-authentication-steps_step-2}
   {#uc-authentication-steps_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.  
   ![Value Added Solutions Page](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Relay the information that is required for authentication. IMPORTANT
   Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.

Authentication Methods {#uc-authentication-methods}
===================================================

`Cybersource` recommends that you review the response in the transient token and compare it with the information below in order to determine the authentication status. For more information about transient tokens, see [Transient Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-tokens-intro.md ""). This table describes the possible authentication results and the associated processingInformation.commerceIndicator.value field values in the transient token.

|   Authentication Result   |                          `Unified Checkout` Commerce Indicator Value                           |
|---------------------------|------------------------------------------------------------------------------------------------|
| Successful authentication | processingInformation.commerceIndicator.value field value set to `VBV` in the transient token. |
| No authentication         | No commerce indicator in transient token.                                                      |
[Responses for Relay `Click to Pay` Transactions for `Unified Checkout`]

For more information about the authentication methods that are supported for Relay, see this page: <https://developer.relay.com/capabilities/relay-secure-remote-commerce/docs-use-cases>

Authentication Test Cards
-------------------------

Use these test cards to test these authentication methods. Replace the X with a 0.

|     Authentication Method      |   Card Number    | CVV | Expiration Date |
|--------------------------------|------------------|-----|-----------------|
| `3-D Secure`/Passkey Challenge | 43958XXX0449X11X | 509 | 12/25           |
| `3-D Secure`/Passkey Challenge | 439584XXX282X11X | 693 | 12/25           |
| Frictionless                   | 439584XX91X1XX11 | 676 | 12/25           |
| Frictionless                   | 439584XX9119XX11 | 789 | 12/25           |
[Authentication Test Cards]

Enable `Click to Pay` Customer Authentication Using the API {#boarding-click-to-pay-auth-enable-intro}
======================================================================================================

This section shows you how to enable `Click to Pay` Authentication using the Boarding Registration Service (BRS) API.

Endpoint {#boarding-click-to-pay-auth-enable-intro_d11e752}
-----------------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/boarding/v1/registrations`{#boarding-click-to-pay-auth-enable-intro_d11e759}  
**Test:** `POST ``https://apitest.cybersource.com``/boarding/v1/registrations`{#boarding-click-to-pay-auth-enable-intro_d11e769}

Required Fields for Enabling `Click to Pay` Authentication {#boarding-click-to-pay-auth-enable-reqfields}
=========================================================================================================

organizationInformation.businessInformation.merchantCategoryCode
:

organizationInformation.businessInformation.name
:

organizationInformation.businessInformation.websiteUrl
:

organizationInformation.organizationId
:

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.clickToPay.enrollmentData.merchantName
:
Required if the enrollmentData object is included in the request.

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.clickToPay.enrollmentData.merchantURL
:
Required if the enrollmentData object is included in the request.

productInformation.selectedProducts.payments.unifiedCheckout.configurationInformation. configurations.features.portfolioAccessofSensitiveData.merchantAccessofSensitiveData
:
Set to `false`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation.enabled
:
Required to enable `Unified Checkout`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation. features.clickToPay.enabled
:
Set to `true`.

productInformation.selectedProducts.payments.unifiedCheckout.subscriptionInformation. features.portfolioAccessofSensitiveData.enabled
:
Set to `true`.

productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerBIN
:
Required for authentication with `Click to Pay` 3DS authentication.

productInformation.selectedProducts.payments.unifiedCheckout. configurationInformation.configurations.features.clickToPay.enrollmentData.acquirerName
:
Required for authentication with `Click to Pay` 3DS authentication.
{#boarding-click-to-pay-auth-enable-reqfields_dl_fsr_5c1_3jc}

Related Information {#boarding-click-to-pay-auth-enable-reqfields_section_dgl_c11_3jc}
--------------------------------------------------------------------------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-click-to-pay-auth-enable-reqfields_ul_kpc_xzz_sxb}

Optional Fields for Enabling `Click to Pay` Authentication {#boarding-click-to-pay-auth-enable-optfields}
=========================================================================================================

organizationInformation.businessInformation.address
:

organizationInformation.businessInformation.address.address1
:

organizationInformation.businessInformation.address.administrativeArea
:

organizationInformation.businessInformation.address.country
:

organizationInformation.businessInformation.address.locality
:

organizationInformation.businessInformation.address.postalCode
:

organizationInformation.configurable
:

organizationInformation.parentOrganizationId
:
This value is dependent on your organization hierarchy rules.

organizationInformation.status
:

organizationInformation.type
:

registrationInformation.boardingFlow
:

registrationInformation.boardingPackageId
:

registrationInformation.mode
:
{#boarding-click-to-pay-auth-enable-optfields_dl_f3k_zb1_3jc}

Related Information {#boarding-click-to-pay-auth-enable-optfields_section_dgl_c11_3jc}
--------------------------------------------------------------------------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-click-to-pay-auth-enable-optfields_ul_kpc_xzz_sxb}

REST Example: Enabling `Click to Pay` Authentication {#boarding-click-to-pay-auth-enable-ex-rest}
=================================================================================================

Enable `Click to Pay Drop-In UI`

```
{
  "registrationInformation": {
    "boardingFlow": "ENTERPRISE",
    "mode": "COMPLETE",
    "boardingPackageId": "74921204027"
  },
  "organizationInformation": {
    "organizationId": "testucctp001",
    "status": "TEST",
    "businessInformation": {
      "name": "testucctp",
      "websiteUrl": "https://www.test.com",
      "merchantCategoryCode": "0742",
      "address": {
        "country": "US",
        "address1": "Test Dr",
        "postalCode": "78641",
        "administrativeArea": "TX",
        "locality": "Austin"
      }
    },
    "parentOrganizationId": "testucctp",
    "type": "TRANSACTING",
    "configurable": false
  },
  "productInformation": {
    "selectedProducts": {
      "payments": {
        "unifiedCheckout": {
          "subscriptionInformation": {
            "enabled": true,
            "features": {
              "clickToPay": {
                "enabled": true
              },
              "portfolioAccessofSensitiveData ": {
                "enabled": true
              }
            }
          },
          "configurationInformation": {
            "configurations": {
              "features": {
                "clickToPay": {
                  "enrollmentData": {
                    "merchantName": "testucctp",
                    "merchantURL": "https://www.test.com",
                    "acquirerBIN": "123456",
                    "acquirerName": "ExampleAcquirer"
                  }
                },
                "portfolioAccessofSensitiveData ": {
                  " merchantAccessofSensitiveData ": false
                }
              }
            }
          }
        }
      }
    }
  }
}
```

{#boarding-click-to-pay-auth-enable-ex-rest_codeblock_zmy_c11_3jc}

Enable Click to Pay Customer Authentication Using the `Business Center` {#ctp-authentication-config-ebc}
========================================================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. These authentication methods are available:

* `3-D Secure`
* Payment Passkey
* Card verification value (CVV)
* One-time password (OTP)
  {#ctp-authentication-config-ebc_ul_ey3_1zs_hjc}

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#ctp-authentication-config-ebc_step-1}
   {#ctp-authentication-config-ebc_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.  
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.  
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)  
   If Click to Pay is not enabled, click **On** next to Click to Pay.  
   ![Manage Available Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/click-to-pay/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#ctp-authentication-config-ebc_step-2}
   {#ctp-authentication-config-ebc_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.  
   ![Value Added Solutions Page](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Relay and Mastercard the information that is required for authentication. IMPORTANT

   > Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.
   > {#ctp-authentication-config-ebc_steps_fy3_1zs_hjc}

Upload Your Encryption Key {#uc-upload-encrypt-key-intro}
=========================================================

Payment information can be retrieved from the `Unified Checkout` platform by invoking the Payment Credentials API. This API retrieves all of the data captured by `Unified Checkout`. This information is transmitted in an encrypted format to ensure the security of the payment information while in transit.  
You can retrieve payment information from the `Click to Pay Drop-In UI` platform from the checkout response payloads. This information is transmitted in an encrypted format to ensure that sensitive data is secure. To retrieve and decrypt this information, you must set up message-level encryption. For information about enabling MLE, see *How to Set up REST* in the [Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-setup-workflow.md "") and follow the steps based on your integration method.  
You must generate an encryption key pair to retrieve this encrypted payment information, and the public encryption key must uploaded to the `Unified Checkout` system.

Generate a Public Private Key Pair {#uc-generate-keypair}
=========================================================

You must generate a public-private key pair to upload to the `Unified Checkout` system. The public key is uploaded to the `Unified Checkout` platform and is used to encrypt sensitive information in transit. The private key is used to decrypt the sensitive payment information on your server. Only the private key can properly decrypt the payment information.
IMPORTANT You must secure your private decryption key. This key must never be exposed to any external systems or it will risk the integrity of the secure channel.  
`Unified Checkout` accepts only keys that meet these requirements:
* Only RSA keys are supported. Elliptical curves are not supported.
* The minimum accepted RSA key size is 2048 bits.
  * RSA keys must be in JWK format. More information on JWK format is available here:  
    [rfc7517](https://datatracker.ietf.org/doc/html/rfc7517 "").
* The key ID must be a valid UUID.
  {#uc-generate-keypair_ul_hgf_qht_hjc}

Uploading Your Key Pair {#uc-upload-key}
========================================

When you have generated your encryption key pairs, you can upload your key to the `Unified Checkout` platform. Keys can be loaded at any hierarchy that is enabled for them and are used for all child entities that do not have keys loaded. You can upload a key at parent and child levels, but child keys override parent keys.  
Follow these steps to upload your key pair:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc-upload-key_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc-upload-key_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc-upload-key_step-1}
   {#uc-upload-key_step-1}
2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Key Management. The Key Management page appears.{#uc-upload-key_step-2}
   {#uc-upload-key_step-2}
3. Click +Generate key. The Create Key page appears.
4. On the Create Key page, select Token Management MLE.
5. Click Generate key.
6. Enter your MLE public key value in JWK format.
7. Click Create key.
8. On the Key Management page, search for your key and select it.
9. Click Activate. Your key is now active.
   {#uc-upload-key_steps_nf4_qht_hjc}

Test Your `Click to Pay` Configuration {#ctp-testing-intro}
===========================================================

This section contains information about testing your `Click to Pay` configuration.

Test Payment Details {#ctp_reference_test_cards}
================================================

Use these test card numbers to test your `Click to Pay` configuration.  
Combine the BIN with the card number when sending to `Click to Pay`.

Relay `Click to Pay` Test Cards
------------------------------

These Relay test cards can be added to your `Click to Pay` wallet.  
Replace the X in the card number with 4.  
You can manage your Relay `Click to Pay` test cards and account here:

* **Production:** [login](https://src.relay.com/login "")
* **Test:** [login](https://sandbox.src.relay.com/login "")  
  To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| x6229x3123123755 | 12/2029         | 728 |
| x6229x3123123763 | 12/2029         | 605 |
| x6229x3123123771 | 12/2029         | 694 |
| x6229x3123123789 | 12/2029         | 881 |
| x6229x3123123797 | 12/2029         | 678 |
| x6229x3123123805 | 12/2029         | 084 |
| x6229x3123123813 | 12/2029         | 127 |
| x6229x3123123821 | 12/2029         | 218 |
| x6229x3123123839 | 12/2029         | 114 |
| x6229x31231238x7 | 12/2029         | 867 |
| x6229x312312385x | 12/2029         | 301 |
[Relay Test Card Numbers]

To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.  
These Relay test card numbers can be used to test ECI05 frictionless authentication. Replace the X in the card number with 4.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| X6229X3123113723 | 12/2027         | 929 |
| X6229X3123113731 | 12/2027         | 217 |
[ECI05 Authentication Test Card Numbers]

These Relay test card numbers can be used to enroll in Passkey Service. Replace the X in the card number with 4.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| X3958X0327800110 | 12/2027         | 832 |
| X3958X0328300110 | 12/2027         | 474 |
[Passkey Enrollment Test Card Numbers]

Mastercard Test Cards
---------------------

Mastercard test cards can be added to your `Click to Pay` wallet. You must retrieve Mastercard test cards from their `Click to Pay` test page: [#test-cards](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "")  
Mastercard has different test cards for retrieving tokenized and non-tokenized data. `Cybersource` recommends that you use these test cards as follows:

* Test cards to retrieve PAN data: Use these cards when the customer is completing checkout as a one-time guest and does not have a `Click to Pay` account or want to create one.

* Test cards to retrieve token data: Use these cards for tokenized `Click to Pay` transactions.  
  You can manage your Mastercard `Click to Pay` test cards and account here:

* **Live:** [enroll](https://src.mastercard.com/profile/enroll "")

* **SBX:** [enroll](https://sandbox.src.mastercard.com/profile/enroll "")  
  Mastercard authentication test cards are available on the *Mastercard Checkout Solutions* page in the [Mastercard Developer Center](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "").

Handle Errors {#uc_appendix_handle_errors}
==========================================

The `Unified Checkout` SDK uses a structured error object for all error scenarios. Errors are returned as exceptions from asynchronous methods and are also returned as events for centralized handling.

UnifiedCheckoutError {#uc_handle_errors_uc_checkout}
====================================================

All SDK errors are instances of `UnifiedCheckoutError` with these properties:

|     Property      |    Type    |                                     Description                                      |
|-------------------|------------|--------------------------------------------------------------------------------------|
| `correlationId`   | `string?`  | The correlation ID from an underlying API call, when applicable.                     |
| `details`         | `unknown?` | Additional error-specific information. This is often an array of objects.            |
| `informationLink` | `string?`  | The URL linked to the online documentation for this error.                           |
| `message`         | `string`   | This property is a human-readable description of the error.                          |
| `name`            | `string`   | The value is always `"UnifiedCheckoutError"`.                                        |
| `reason`          | `string`   | This property is a machine-readable error code, such as `"CAPTURE_CONTEXT_INVALID"`. |
[`UnifiedCheckoutError` Properties]

Detect Errors {#uc_handle_errors_detect}
========================================

Errors may be serialized through `postMessage`. `Cybersource` recommends that you use the `name` property instead of `instanceof`:

```
try {
  const result = await checkout.mount('#buttons');
} catch (error) {
  if (error.name === 'UnifiedCheckoutError') {
    // Access error.reason, error.message, error.details
  }
}
```

You can also write a helper function that can be reused:

```
function isUnifiedCheckoutError(obj) {
  return (
    obj !== null &&
    typeof obj === 'object' &&
    obj.name === 'UnifiedCheckoutError' &&
    typeof obj.reason === 'string' &&
    typeof obj.message === 'string'
  );
}
```

Error Handling Patterns {#uc_handle_errors_pattern}
===================================================

Try/Catch
---------

```
try {
  const client = await VAS.UnifiedCheckout(sessionJWT);
  const checkout = await client.createCheckout();
  const result = await checkout.mount('#buttons');
} catch (error) {
  console.error(error.reason, error.message);
}
```

Promise .catch()
----------------

```
VAS.UnifiedCheckout(sessionJWT)
  .then(client =&gt; client.createCheckout())
  .then(checkout =&gt; checkout.mount('#buttons'))
  .catch(error =&gt; console.error(error.reason, error.message));
```

Centralized Error Logging via Events
------------------------------------

Errors from all integrations are applicable up to the client level. Use `client.on('error')` for centralized logging:

```
const client = await VAS.UnifiedCheckout(sessionJWT);

client.on('error', (err) =&gt; {
  errorReporter.send({
    source: err.source,   // "checkout", "trigger", "button", or "client"
    code: err.code,
    message: err.message
  });
});
```

`Cybersource` recommends that you do this as it catches errors from all checkouts, triggers, and buttons created from this client instance.

Error Codes {#ctp-handle-errors-codes}
======================================

Initialization Errors {#ctp-handle-errors-codes_section_kw4_czg_3jc}
--------------------------------------------------------------------

These errors are returned during `VAS.UnifiedCheckout(sessionJWT)`:

|          Reason           |                                                          Description                                                           |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `CAPTURE_CONTEXT_EXPIRED` | The supplied JWT has expired. Generate a new session.                                                                          |
| `CAPTURE_CONTEXT_INVALID` | The session JWT is not valid. For example, it has a bad signature or is malformed.                                             |
| `UNUSED_TARGET_ORIGINS`   | One or more `targetOrigins` in the session do not match the current page origin. The `details` array lists the unused origins. |
[Initialization Reason Values]

Mount Errors {#ctp-handle-errors-codes_section_ow4_czg_3jc}
-----------------------------------------------------------

These errors are returned during `checkout.mount()` or `trigger.mount()`:

|           Reason            |                                                                 Description                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `CHECKOUT_ALREADY_MOUNTED`  | The checkout or trigger is already mounted. Call `unmount()` first, or create a new instance.                                                |
| `MOUNT_CONTAINER_SELECTOR`  | The CSS selector does not match any Document Object Model (DOM) element. Check that the container exists before calling `mount()`.           |
| `MOUNT_ERROR`               | A problem occurred loading the payment iframe.                                                                                               |
| `MOUNT_INVALID_CONTAINER`   | The supplied container parameter is not a valid CSS selector string or `HTMLElement`.                                                        |
| `MOUNT_PAYMENT_TIMEOUT`     | A payment method timed out during initialization.                                                                                            |
| `MOUNT_PAYMENT_UNAVAILABLE` | No payment types could be presented to the customer. This may be due to browser or device support, or errors during checkout initialization. |
| `MOUNT_SIDEBAR_OPTIONS`     | The supplied container parameter is invalid for sidebar mode.                                                                                |
| `MOUNT_TOKEN_TIMEOUT`       | Token creation timed out during mount. This may indicate a network issue.                                                                    |
| `MOUNT_TOKEN_XHR_ERROR`     | A network error occurred during token creation. Check the customer's connectivity.                                                           |
[Mount Reason Values]

Checkout Errors {#ctp-handle-errors-codes_section_sw4_czg_3jc}
--------------------------------------------------------------

|            Reason             |                       Description                        |
|-------------------------------|----------------------------------------------------------|
| `CHECKOUT_ERROR`              | A general checkout error occurred.                       |
| `CHECKOUT_PAYMENT_PARAMETERS` | One or more payment parameters have a validation error.  |
| `CHECKOUT_VALIDATION_PARAMS`  | One or more checkout parameters have a validation error. |
[Checkout Reason Values]

Trigger Errors {#ctp-handle-errors-codes_section_vw4_czg_3jc}
-------------------------------------------------------------

|                Reason                |                                                   Description                                                    |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED` | The specified payment type cannot be used with a trigger. Only `PANENTRY` and `CLICKTOPAY` values are supported. |
[Trigger Reason Values]

**Payment-Specific Errors** {#ctp-handle-errors-codes_section_xw4_czg_3jc}
--------------------------------------------------------------------------

|                 Reason                 |                      Description                      |
|----------------------------------------|-------------------------------------------------------|
| `CLICK_TO_PAY_SDK_LOAD_ERROR`          | The `Click to Pay`SDK failed to load.                 |
| `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` | Card encryption for `Click to Pay` enrollment failed. |
| `GOOGLEPAY_CHECKOUT_ERROR`             | A Google Pay checkout error occurred.                 |
| `LAUNCH_SRC_CHECKOUT_ERROR`            | Launching the `Click to Pay` checkout failed.         |
| `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED`   | The payment type is not supported for triggers.       |
[Payment-Specific Reason Values]

General Errors {#ctp-handle-errors-codes_section_zw4_czg_3jc}
-------------------------------------------------------------

|   Reason Code   |          Description           |
|-----------------|--------------------------------|
| `UNKNOWN_ERROR` | An unknown error has occurred. |

JSON Web Tokens {#uc-appendix-jwts}
===================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.  
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```
* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```
* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#uc-appendix-jwts_ul_ozy_ysn_4pb}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.  
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

Reason Codes {#uc-appendix-reason-codes}
========================================

A `Unified Checkout` request response returns one of the following reason codes:

| Reason Code                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|:----------------------------|:---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `200`                       | Successful response.                                                                                                                                                                                                                                                                                                                                                                                                                                                      ||
| `201`                       | Capture context created.                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
| `400` - Capture Context API | Bad request. Possible reason values:   |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `400` - Capture Context API | `CAPTURE_CONTEXT_EXPIRED`              | This reason is returned when the capture context JWT has passed its expiration time of 900 seconds (15 minutes). Example decrypted JWT fields include `"exp": "1762894371"` and `"iat": "1762893471"`.                                                                                                                                                                                                                            |
| `400` - Capture Context API | `CAPTURE_CONTEXT_INVALID`              | The `Unified Checkout` configuration rejected the request due to invalid values. This reason is returned when the minimum required fields are missing or invalid or the capture context contradicts which products are enabled.                                                                                                                                                                                                   |
| `400` - Capture Context API | `CHECKOUT_ERROR`                       | Checkout failed. This reason is returned when a general, non‑payment‑method‑specific error occurs during the UnifiedPayments checkout flow. When the checkout failure is specifically related to tokenization, `Click to Pay` SDK, SRC launch, Google Pay, etc., the SDK returns a more specific error                                                                                                                            |
| `400` - Capture Context API | `CLICK_TO_PAY_SDK_LOAD_ERROR`          | This reason is returned when the UI cannot be successfully rendered. For example: * Network failures (CDN unavailable, blocked, or timed out) * Browser or device restrictions are preventing the SDK from loading. * Incorrect or missing configuration causes `Unified Checkout` not to request the SDK asset. * The merchant site CSP is blocking the SDK. * Any runtime error that prevents `Click to Pay` JS initialization. |
| `400` - Capture Context API | `CREATE_TOKEN_TIMEOUT`                 | The token creation timed out. This reason is returned when the `Unified Checkout` JavaScript SDK cannot generate the transient token within the expected time-frame.                                                                                                                                                                                                                                                              |
| `400` - Capture Context API | `CREATE_TOKEN_XHR_ERROR`               | This reason is returned when the system attempts to create a token, but a network / XHR-level failure occurs before the token can be created. This is a client-side SDK network failure, not a timeout or back-end validation error.                                                                                                                                                                                              |
| `400` - Capture Context API | `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` | Encrypt card for SRC enrollment failed. This reason is returned when `Unified Checkout` attempts to encrypt a card to enroll it in the SRC / `Click to Pay` system and the encryption step fails. This causes the SRC enrolment to abort.                                                                                                                                                                                         |
| `400` - Capture Context API | `GOOGLEPAY_CHECKOUT_ERROR`             | Checkout failed. This reason is returned when `Unified Checkout` attempts to complete a Google Pay checkout, but the Google Pay--based transaction fails internally in the `Unified Checkout` checkout flow.                                                                                                                                                                                                                      |
| `400` - Capture Context API | `INVALID_APIKEY`                       | Returned when the API key that is used in the server‑side capture context request is invalid.                                                                                                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `LAUNCH_SRC_CHECKOUT_ERROR`            | The launch SRC checkout failed. This reason is returned by the `Unified Checkout` JavaScript SDK when it cannot initialize or open the SRC checkout flow.                                                                                                                                                                                                                                                                         |
| `400` - Capture Context API | `SDK_XHR_ERROR`                        | SDK failed to load. This reason is returned when the JavaScript SDK fails to load due to an XHR/network error during `Unified Checkout` initialization.                                                                                                                                                                                                                                                                           |
| `400` - Capture Context API | `SHOW_LOAD_CONTAINER_SELECTOR`         | The specified DOM element cannot be found. Returned when the DOM element specified in the `show()` configuration cannot be found. This is a client-side JavaScript SDK error thrown during rendering of the payment selection UI.                                                                                                                                                                                                 |
| `400` - Capture Context API | `SHOW_LOAD_ERROR`                      | There was a problem encountered when loading the payment screen. Returned when the Unified Payments UI fails to load the payment selection screen (iframe/UI) during the `.show()` step                                                                                                                                                                                                                                           |
| `400` - Capture Context API | `SHOW_LOAD_INVALID_CONTAINER`          | The supplied container parameter is invalid. Returned when the container provided to `up.show()` exists but is invalid---wrong type, not suitable to host UC UI, unsupported context, or malformed in configuration                                                                                                                                                                                                               |
| `400` - Capture Context API | `SHOW_LOAD_SIDEBAR_OPTIONS`            | The supplied container parameter is invalid when sidebar is selected. Returned when `sidebar = true` and the `containers` supplied to `up.show()` are not valid for the sidebar layout (wrong type, unsupported container, or structurally incompatible).                                                                                                                                                                         |
| `400` - Capture Context API | `SHOW_PAYMENT_TIMEOUT`                 | Occurs when an error is encountered during the handling of a payment option. Returned when UC cannot progress the user's selected payment option in time:                                                                                                                                                                                                                                                                         |
| `400` - Capture Context API | `SHOW_PAYMENT_UNAVAILABLE`             | No payment types could be presented to the customer. This could be due to browser/device support or errors encountered during the checkout. Returned when *zero* payment methods can be presented in the `.show()` phase --- typically due to browser/device incompatibility, disabled payment types, or internal errors while loading payment options.                                                                           |
| `400` - Capture Context API | `SHOW_TOKEN_TIMEOUT`                   | Occurs when the createToken call was unable to proceed. Returned when the `createToken` call cannot proceed within the expected time while rendering the payment selection UI                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `SHOW_TOKEN_XHR_ERROR`                 | Occurs when a network error is encountered while attempting to create a token. Returned when the `createToken` step within `.show()` fails due to an actual network/XHR error (blocked request, CORS/CSP violation, extension interference, unreachable endpoint).                                                                                                                                                                |
| `400` - Capture Context API | `TOKENIZATION_ERROR`                   | Tokenization failed. Returned when tokenization of the selected payment method fails --- due to invalid payment data, a failed internal tokenization call, network issues, or an unsupported/blocked payment environment.                                                                                                                                                                                                         |
| `400` - Capture Context API | `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED`   | Trigger is not supported for this payment type. Returned when `up.trigger(paymentType)` is called with a payment method that does not support trigger mode, is not enabled, not available on the device/browser, or not recognized by UC.                                                                                                                                                                                         |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_ALREADY_SHOWN`       | Occurs if you attempt to show a Unified Payments instance multiple times. Returned when `.show()` is invoked more than once on the same `UnifiedPayments` instance. Create a new instance (`accept.unifiedPayments()`) if you need to show UC again.                                                                                                                                                                              |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS`  | Occurs when no valid payment parameters exist when initializing button. Returned when the merchant calls `accept.unifiedPayments()` without providing valid payment parameters --- meaning the SDK cannot initialize the payment buttons because the supplied configuration is missing, empty, or malformed.                                                                                                                      |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_VALIDATION_FIELDS`   | A validation error occurred. Missing or invalid values in required fields                                                                                                                                                                                                                                                                                                                                                         |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_VALIDATION_PARAMS`   | Trigger is not supported for this payment type. Returned when `up.trigger(paymentType)` is called with a payment method that does not support trigger mode, is not enabled, not available on the device/browser, or not recognized by UC.                                                                                                                                                                                         |
| `400` - Complete API        | `COMPLETE_AUTHENTICATION_CANCELED`     | Occurs when the user cancels the authentication process during Cardinal step‑up. This value is returned when the customer cancels or prematurely exits the 3‑D Secure (Cardinal) step‑up authentication flow during `unifiedPayments.complete()`.                                                                                                                                                                                 |
| `400` - Complete API        | `COMPLETE_AUTHENTICATION_FAILED`       | Occurs when the complete authentication process fails during Cardinal Step‑Up. Returned when the 3‑D Secure (Cardinal) authentication attempt fails---typically due to incorrect OTP, issuer decline, timeout interpreted as failure, or ACS technical error---during `unifiedPayments.complete()`.                                                                                                                               |
| `400` - Complete API        | `COMPLETE_ERROR`                       | Occurs when an error occurs whilst attempting to complete the transaction. Returned when an unexpected or uncategorized error occurs during `unifiedPayments.complete()`---typically caused by internal processing exceptions or failures that cannot be classified as authentication failure, user cancellation, validation error, or processor decline.                                                                         |
| `400` - Complete API        | `COMPLETE_IN_PROGRESS`                 | Returned when `unifiedPayments.complete()` is invoked again while a previous Complete operation is still running. This is caused by duplicate submissions, race conditions, or UI re-renders that trigger multiple Complete calls.                                                                                                                                                                                                |
| `400` - Complete API        | `COMPLETE_NOT_ALLOWED`                 | Occurs if complete is not allowed for this transaction. Returned when the merchant calls `unifiedPayments.complete()` in a state where the transaction is not permitted to be completed---typically due to missing/invalid Complete Mandate, calling complete() before the customer has completed the UC UI flow, using an unsupported payment type, or invoking complete() at the wrong time in the lifecycle.                   |
| `400` - Complete API        | `COMPLETE_TRANSACTION_CANCELLED`       | Occurs when the user cancels the transaction. Returned when the user (or the payment provider on behalf of the user) cancels the transaction during the Complete phase --- including cancellations on the UC UI, cancellations during redirect/step‑up, or cancellation states returned by APMs such as PPRO or Tink.                                                                                                             |
| `400` - Complete API        | `COMPLETE_TRANSACTION_FAILED`          | Consumer transaction has failed. Returned when the payment attempt reaches the processor or APM provider and is returned as a *failure* --- such as card declines, failed 3DS outcomes, APM failures, or downstream processor rejections.                                                                                                                                                                                         |
| `400` - Complete API        | `COMPLETE_VALIDATION_ERROR`            | Occurs when there is a validation issue relating to the parameters you have supplied in your complete call. Returned when the merchant sends invalid, missing, malformed, or inconsistent parameters to the `unifiedPayments.complete()` call --- typically a bad trust token or a mismatched/incorrect payload.                                                                                                                  |
| `404`                       | The specified resource not found in the system.                                                                                                                                                                                                                                                                                                                                                                                                                           ||
| `500`                       | Unexpected server error.                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
[Reason Codes]

Supported Countries for `Click to Pay` {#uc_appendix_supp_countries}
====================================================================

`Click to Pay` is supported in these countries:

* Argentina
* Australia
* Austria
* Brazil
* Bulgaria
* Canada
* China
* Colombia
* Costa Rica
* Czech Republic
* Denmark
* Dominican Republic
* Ecuador
* El Salvador
* Finland
* France
* Germany
* Greece
* Honduras
* Hong Kong
* Hungary
* Indonesia
* Ireland
* Italy
* Japan
* Jordan
* Kuwait
* Malaysia
* Mexico
* Netherlands
* New Zealand
* Nicaragua
* Norway
* Panama
* Paraguay
* Peru
* Poland
* Qatar
* Romania
* Saudi Arabia
* Singapore
* Slovakia
* Slovenia
* South Africa
* Spain
* Sweden
* Switzerland
* Thailand
* Ukraine
* United Arab Emirates
* United Kingdom
* United States
* Uruguay
* Vietnam

Supported Locales {#ctp-appendix-languages}
===========================================

The locale field within the capture context request consists of an ISO 639 language code, an underscore (_), and an ISO 3166 region code. The locale controls the language in which the application is rendered. The following locales are supported:

* ar_AE
* bg_BG
* ca_ES
* cs_CZ
* da_DK
* de_AT
* de_DE
* el_GR
* en_AU
* en_CA
* en_GB
* en_IE
* en_NZ
* en_PK
* en_US
* es_AR
* es_CL
* es_CO
* es_ES
* es_MX
* es_PE
* es_US
* fi_FI
* fr_CA
* fr_FR
* he_IL
* hr_HR
* hu_HU
* id_ID
* it_IT
* ja_JP
* km_KH
* ko_KR
* lo_LA
* ms_MY
* nb_NO
* nl_NL
* pl_PL
* pt_BR
* ro_RO
* ru_RU
* sk_SK
* sl_SI
* sv_SE
* th_TH
* tl_PH
* tr_TR
* uk_UA
* ur_PK
* vi_VN
* zh_CN
* zh_HK
* zh_MO
* zh_SG
* zh_TW

Client Version History {#ctp-capture-context-versions}
======================================================

Below is a list of client versions and the features that are included in each version.

> IMPORTANT
> ` Cybersource ` recommends that you use the most recent client version in your integration.

0.23
:
Accepts these card networks in the allowedCardNetworks field for manual card entry:

    * Carnet
    * Cartes Bancaires
    * China UnionPay with card verification value (CVV)
    * EFTPOS
    * ELO
    * mada
    * Meeza

:
Ordering controls for the allowedPaymentTypes button.
:
De-coupling of PANENTRY from other payment types in the allowedPaymentTypes field.

0.24
:
Support for enabling combo cards in the capture context.
:
Support for eight-digit BINs.
:
Support for enabling card save in the capture context.

0.25
:
Addition of **Skip Verification next time** in the `Click to Pay` payment flow.
:
Support for CPF in the capture context.

0.26
:
Support for auto-lookup in `Click to Pay` when an email is included in the capture context.
:
Inclusion of the cardDetails field object in the transient token response.

0.28
:
Support for PayPak as an allowedCardNetwork.
:
Auto-enrollment for `Click to Pay` in supported markets.
:
Removal of the confirm or continue screen for specific use cases.
:
Static button for `Click to Pay` flows.

0.30
:
Support for Pakistan locales (en_PK and ur_PK).
:
New look and feel of `Unified Checkout` in line with EMVCO best practices.

0.31
:
Addition of the data object of the orderInformation field object and pass-through fields.
:
Support for Jaywan as an allowedCardNetwork.
:
Updated the payment details response to return detected card types. Multiple card types are shown when more than one card type is detected.

0.32
:
Support for KCP and UATP in the allowedCardNetwork field.
:
A radio button in the UI for Cartes Bancaires dual-branded cards.

0.33
:
Support for Mobile as Identity `Click to Pay` lookup.

0.34
:
Additional BIN range for Jaywan card types.

1.0
:
Configure payment options.
:
Configure customer data and payment flow.

Customization Matrix {#ctp-appendix-cust-matrix}
================================================

Top-Level Appearance
--------------------

| Field Name |   Data Type   |               Description               |
|------------|---------------|-----------------------------------------|
| appearance | Object        | Control checkout UI appearance          |
| theme      | Enum (String) | Theme selection (LIGHT, DARK, seasonal) |
| buttonType | Enum (String) | Button label/type                       |
| variables  | Object        | UI customisation variables container    |
[Top-Level Appearance]

Base
----

|   Field Name    | Data Type  |      Description       |
|-----------------|------------|------------------------|
| backgroundColor | Hex Colour | Main background colour |
| textColor       | Hex Colour | Main text colour       |
[Base]

Header
------

|         Field Name          | Data Type  |       Description        |
|-----------------------------|------------|--------------------------|
| headerBackground            | Hex Colour | Header background colour |
| headerForeground            | Hex Colour | Header text/icon colour  |
| headerAvatarBackgroundColor | Hex Colour | Header avatar background |
| headerAvatarForegroundColor | Hex Colour | Header avatar foreground |
[Header]

Input Default
-------------

|      Field Name       | Data Type  |       Description       |
|-----------------------|------------|-------------------------|
| inputBackground       | Hex Colour | Input background        |
| inputColor            | Hex Colour | Input text colour       |
| inputPlaceholderColor | Hex Colour | Placeholder text colour |
| inputBorderColor      | Hex Colour | Border colour           |
| inputBorderStyle      | String     | Border style            |
| inputBorderRadius     | CSS Size   | Border radius           |
[Input Default]

Input Hover State
-----------------

|         Field Name         | Data Type  |          Description          |
|----------------------------|------------|-------------------------------|
| inputHoverBackground       | Hex Colour | Background when hover         |
| inputHoverColor            | Hex Colour | Text colour when hover        |
| inputHoverPlaceholderColor | Hex Colour | Placeholder colour when hover |
| inputHoverBorderColor      | Hex Colour | Border colour when hover      |
| inputHoverBorderStyle      | String     | Border style when hover       |
[Input Hover State]

Input Focused State
-------------------

|          Field Name          | Data Type  |           Description           |
|------------------------------|------------|---------------------------------|
| inputFocusedBackground       | Hex Colour | Background when focused         |
| inputFocusedColor            | Hex Colour | Text colour when focused        |
| inputFocusedPlaceholderColor | Hex Colour | Placeholder colour when focused |
| inputFocusedBorderColor      | Hex Colour | Border colour when focused      |
| inputFocusedBorderStyle      | String     | Border style when focused       |
[Input Focused State]

Input Active State
------------------

|         Field Name          | Data Type  |          Description           |
|-----------------------------|------------|--------------------------------|
| inputActiveBackground       | Hex Colour | Background when active         |
| inputActiveColor            | Hex Colour | Text colour when active        |
| inputActivePlaceholderColor | Hex Colour | Placeholder colour when active |
| inputActiveBorderColor      | Hex Colour | Border colour when active      |
| inputActiveBorderStyle      | String     | Border style when active       |
[Input Active State]

Input Pressed State
-------------------

|          Field Name          | Data Type  |           Description           |
|------------------------------|------------|---------------------------------|
| inputPressedBackground       | Hex Colour | Background when pressed         |
| inputPressedColor            | Hex Colour | Text colour when pressed        |
| inputPressedPlaceholderColor | Hex Colour | Placeholder colour when pressed |
| inputPressedBorderColor      | Hex Colour | Border colour when pressed      |
| inputPressedBorderStyle      | String     | Border style when pressed       |
[Input Pressed State]

Input Error State
-----------------

|         Field Name         | Data Type  |          Description          |
|----------------------------|------------|-------------------------------|
| inputErrorBackground       | Hex Colour | Background when error         |
| inputErrorColor            | Hex Colour | Text colour when error        |
| inputErrorPlaceholderColor | Hex Colour | Placeholder colour when error |
| inputErrorBorderColor      | Hex Colour | Border colour when error      |
| inputErrorBorderStyle      | String     | Border style when error       |
[Input Error State]

Input Valid State
-----------------

|         Field Name         | Data Type  |          Description          |
|----------------------------|------------|-------------------------------|
| inputValidBackground       | Hex Colour | Background when valid         |
| inputValidColor            | Hex Colour | Text colour when valid        |
| inputValidPlaceholderColor | Hex Colour | Placeholder colour when valid |
| inputValidBorderColor      | Hex Colour | Border colour when valid      |
| inputValidBorderStyle      | String     | Border style when valid       |
[Input Valid State]

Button Default
--------------

|     Field Name     | Data Type  |       Description       |
|--------------------|------------|-------------------------|
| buttonBackground   | Hex Colour | Button background       |
| buttonForeground   | Hex Colour | Button text/icon colour |
| buttonShape        | String     | Button shape            |
| buttonBorderColor  | Hex Colour | Border colour           |
| buttonBorderStyle  | String     | Border style            |
| buttonBorderRadius | CSS Size   | Border radius           |
[Button Default]

Button Hover State
------------------

|       Field Name       | Data Type  |       Description        |
|------------------------|------------|--------------------------|
| buttonHoverBackground  | Hex Colour | Background when hover    |
| buttonHoverForeground  | Hex Colour | Text colour when hover   |
| buttonHoverBorderColor | Hex Colour | Border colour when hover |
| buttonHoverBorderStyle | String     | Border style when hover  |
[Button Hover State]

Button Focus State
------------------

|       Field Name       | Data Type  |       Description        |
|------------------------|------------|--------------------------|
| buttonFocusBackground  | Hex Colour | Background when focus    |
| buttonFocusForeground  | Hex Colour | Text colour when focus   |
| buttonFocusBorderColor | Hex Colour | Border colour when focus |
[Button Focus State]

Button Active State
-------------------

|       Field Name        | Data Type  |        Description        |
|-------------------------|------------|---------------------------|
| buttonActiveBackground  | Hex Colour | Background when active    |
| buttonActiveForeground  | Hex Colour | Text colour when active   |
| buttonActiveBorderColor | Hex Colour | Border colour when active |
| buttonActiveBorderStyle | String     | Border style when active  |
[Button Active State]

Button Disabled State
---------------------

|        Field Name         | Data Type  |         Description         |
|---------------------------|------------|-----------------------------|
| buttonDisabledBackground  | Hex Colour | Background when disabled    |
| buttonDisabledForeground  | Hex Colour | Text colour when disabled   |
| buttonDisabledBorderColor | Hex Colour | Border colour when disabled |
[Button Disabled State]

Typography \& Other
-------------------

|         Field Name         | Data Type  |       Description       |
|----------------------------|------------|-------------------------|
| fontFamily                 | String     | Font family             |
| borderRadius               | CSS Size   | Global border radius    |
| paymentSelectionBackground | Hex Colour | Payment list background |
[Typography \& Other]

JSON Web Tokens {#ctp-appendix-jwts}
====================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.  
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

{#ctp-appendix-jwts_codeblock_czg_s5z_hjc}  
The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```

  {#ctp-appendix-jwts_codeblock_dzg_s5z_hjc}

* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```

  {#ctp-appendix-jwts_codeblock_ezg_s5z_hjc}

* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#ctp-appendix-jwts_ul_ozy_ysn_4pb}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.  
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

Reason Codes {#ctp-appendix-reason-codes}
=========================================

A `Unified Checkout` request response returns one of the following reason codes:

| Reason Code                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ||
|:----------------------------|:---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `200`                       | Successful response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ||
| `201`                       | Capture context created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
| `400` - Capture Context API | Bad request. Possible reason values:   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `400` - Capture Context API | `CAPTURE_CONTEXT_EXPIRED`              | This reason is returned when the capture context JWT has passed its expiration time of 900 seconds (15 minutes). Example decrypted JWT fields include `"exp": "1762894371"` and `"iat": "1762893471"`.                                                                                                                                                                                                                                                                        |
| `400` - Capture Context API | `CAPTURE_CONTEXT_INVALID`              | The `Unified Checkout` configuration rejected the request due to invalid values. This reason is returned when the minimum required fields are missing or invalid or the capture context contradicts which products are enabled.                                                                                                                                                                                                                                               |
| `400` - Capture Context API | `CHECKOUT_ERROR`                       | Checkout failed. This reason is returned when a general, non‑payment‑method‑specific error occurs during the UnifiedCheckout checkout flow. When the checkout failure is specifically related to tokenization, `Click to Pay` SDK, SRC launch, Google Pay, etc., the SDK returns a more specific error                                                                                                                                                                        |
| `400` - Capture Context API | `CLICK_TO_PAY_SDK_LOAD_ERROR`          | This reason is returned when the UI cannot be successfully rendered. For example: * Network failures (CDN unavailable, blocked, or timed out) * Browser or device restrictions are preventing the SDK from loading. * Incorrect or missing configuration causes `Unified Checkout` not to request the SDK asset. * The merchant site CSP is blocking the SDK. * Any runtime error that prevents `Click to Pay` JS initialization. {#ctp-appendix-reason-codes_ul_bl5_n5z_hjc} |
| `400` - Capture Context API | `CREATE_TOKEN_TIMEOUT`                 | The token creation timed out. This reason is returned when the `Unified Checkout` JavaScript SDK cannot generate the transient token within the expected time-frame.                                                                                                                                                                                                                                                                                                          |
| `400` - Capture Context API | `CREATE_TOKEN_XHR_ERROR`               | This reason is returned when the system attempts to create a token, but a network / XHR-level failure occurs before the token can be created. This is a client-side SDK network failure, not a timeout or back-end validation error.                                                                                                                                                                                                                                          |
| `400` - Capture Context API | `ENCRYPT_CARD_FOR_SRC_ENROLMENT_ERROR` | Encrypt card for SRC enrollment failed. This reason is returned when `Unified Checkout` attempts to encrypt a card to enroll it in the SRC / `Click to Pay` system and the encryption step fails. This causes the SRC enrolment to abort.                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `INVALID_APIKEY`                       | Returned when the API key that is used in the server‑side capture context request is invalid.                                                                                                                                                                                                                                                                                                                                                                                 |
| `400` - Capture Context API | `LAUNCH_SRC_CHECKOUT_ERROR`            | The launch SRC checkout failed. This reason is returned by the `Unified Checkout` JavaScript SDK when it cannot initialize or open the SRC checkout flow.                                                                                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `SDK_XHR_ERROR`                        | SDK failed to load. This reason is returned when the JavaScript SDK fails to load due to an XHR/network error during `Unified Checkout` initialization.                                                                                                                                                                                                                                                                                                                       |
| `400` - Capture Context API | `SHOW_LOAD_CONTAINER_SELECTOR`         | The specified DOM element cannot be found. Returned when the DOM element specified in the `show()` configuration cannot be found. This is a client-side JavaScript SDK error thrown during rendering of the payment selection UI.                                                                                                                                                                                                                                             |
| `400` - Capture Context API | `SHOW_LOAD_ERROR`                      | There was a problem encountered when loading the payment screen. Returned when the Unified Payments UI fails to load the payment selection screen (iframe/UI) during the `.show()` step                                                                                                                                                                                                                                                                                       |
| `400` - Capture Context API | `SHOW_LOAD_INVALID_CONTAINER`          | The supplied container parameter is invalid. Returned when the container provided to `up.show()` exists but is invalid---wrong type, not suitable to host UC UI, unsupported context, or malformed in configuration                                                                                                                                                                                                                                                           |
| `400` - Capture Context API | `SHOW_LOAD_SIDEBAR_OPTIONS`            | The supplied container parameter is invalid when sidebar is selected. Returned when `sidebar = true` and the `containers` supplied to `up.show()` are not valid for the sidebar layout (wrong type, unsupported container, or structurally incompatible).                                                                                                                                                                                                                     |
| `400` - Capture Context API | `SHOW_PAYMENT_TIMEOUT`                 | Occurs when an error is encountered during the handling of a payment option. Returned when UC cannot progress the user's selected payment option in time:                                                                                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `SHOW_PAYMENT_UNAVAILABLE`             | No payment types could be presented to the customer. This could be due to browser/device support or errors encountered during the checkout. Returned when *zero* payment methods can be presented in the `.show()` phase --- typically due to browser/device incompatibility, disabled payment types, or internal errors while loading payment options.                                                                                                                       |
| `400` - Capture Context API | `SHOW_TOKEN_TIMEOUT`                   | Occurs when the createToken call was unable to proceed. Returned when the `createToken` call cannot proceed within the expected time while rendering the payment selection UI                                                                                                                                                                                                                                                                                                 |
| `400` - Capture Context API | `SHOW_TOKEN_XHR_ERROR`                 | Occurs when a network error is encountered while attempting to create a token. Returned when the `createToken` step within `.show()` fails due to an actual network/XHR error (blocked request, CORS/CSP violation, extension interference, unreachable endpoint).                                                                                                                                                                                                            |
| `400` - Capture Context API | `TOKENIZATION_ERROR`                   | Tokenization failed. Returned when tokenization of the selected payment method fails --- due to invalid payment data, a failed internal tokenization call, network issues, or an unsupported/blocked payment environment.                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `TRIGGER_PAYMENT_TYPE_NOT_SUPPORTED`   | Trigger is not supported for this payment type. Returned when `up.trigger(paymentType)` is called with a payment method that does not support trigger mode, is not enabled, not available on the device/browser, or not recognized by UC.                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS`  | Occurs when no valid payment parameters exist when initializing button. Returned when the merchant calls `VAS.UnifiedCheckout(sessionJWT)` without providing valid payment parameters --- meaning the SDK cannot initialize the payment buttons because the supplied configuration is missing, empty, or malformed.                                                                                                                                                           |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_VALIDATION_FIELDS`   | A validation error occurred. Missing or invalid values in required fields                                                                                                                                                                                                                                                                                                                                                                                                     |
| `400` - Capture Context API | `UNIFIED_PAYMENTS_VALIDATION_PARAMS`   | Trigger is not supported for this payment type. Returned when `up.trigger(paymentType)` is called with a payment method that does not support trigger mode, is not enabled, not available on the device/browser, or not recognized by UC.                                                                                                                                                                                                                                     |
| `404`                       | The specified resource not found in the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
| `500`                       | Unexpected server error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
[Reason Codes]

Loading the JavaScript Library {#uc-getting-started-cs-js-library-intro}
========================================================================

Use the client library asset path and client library integrity value that is returned by the capture context response to invoke `Unified Checkout` on your page.  
You must retrieve these values from the clientLibrary and clientLibraryIntegrity fields that are returned in the JWT from `https://apitest.cybersource.com``/uc/v1/sessions`. You can use these values to create your script tags.  
You must perform this process for each transaction, as these values are unique for each transaction. You must avoid hard-coding values for the clientLibrary and clientLibraryIntegrity fields to prevent client-side errors.  
For example, a response from `https://apitest.cybersource.com``/uc/v1/sessions` would include:

```
"data": {
    "clientLibrary":"[EXTRACT clientLibrary VALUE from here]",
    "clientLibraryIntegrity": "[EXTRACT clientLibraryIntegrity VALUE from here]"
}
```

Below is an example script tag:

```
&lt;script src="[INSERT clientLibrary VALUE HERE]" 
    integrity=”[INSERT clientLibraryIntegrity VALUE HERE]”
    crossorigin=”anonymous”&gt;&lt;/script&gt;
```

> IMPORTANT
> Use the clientLibrary and clientLibraryIntegrity parameter values in the capture context response to obtain the ` Unified Checkout ` JavaScript library URL and the integrity value. This ensures that you are always using the most up-to-date library and protects against fraud. Do not hard-code the ` Unified Checkout ` JavaScript library URL or integrity value.  
> When you load the library, the capture context from your initial server-side request is used to invoke the accept function.  
> For information about the client-side API, see [JavaScript API Reference](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-js-reference-v1.md "").

Payment Details API {#uc-token-get-pymnt-details}
=================================================

This section contains the information you need to retrieve the non-sensitive data associated with a `Unified Checkout` transient token and the payment details API. This API can be used to retrieve personally identifiable information, such as the cardholder name and billing and shipping details, without retrieving payment credentials, which helps ease the PCI compliance burden.
There are two methods of authentication, and they are described in the Getting Started with REST Developer Guide:

* [Set Up a JSON Web Token Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro.md "")
* [Set Up HTTP Signature Message](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-http-message-intro.md "")

> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Endpoint {#uc-token-get-pymnt-details_d14e1140}
-----------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1147}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-details/`*{jti}*{#uc-token-get-pymnt-details_d14e1159}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-details/`*{jti}*  
The `{jti}` is the ID of the JWT within the transient token that is returned by `Unified Checkout`. The transient token is a JWT object that you retrieved as part of a successful capture of payment information from a cardholder.

Click to Pay Customer Authentication {#uc-authentication}
=========================================================

When you enable customer authentication through Click to Pay, you give `Cybersource` permission to send Relay the required authentication information for each transaction. When the customer completes a transaction using a Relay card that is already stored in Click to Pay, authentication is managed within Click to Pay.  
Click to Pay authentication is only available for Relay branded cards that are tokenized with Click to Pay. If Click to Pay does not authenticate the transaction, but you are using the complete mandate with the consumerAuthentication field set to `true`, authentication is attempted as part of this request. When you do not use the complete mandate, you must check the result of the cardholderAuthenticationStatus field in the transient token and request `Payer Authentication` directly when it is required.

> IMPORTANT
> American Express and Mastercard card brands cannot be authenticated through Click to Pay customer authentication.

Authentication Flow
-------------------

![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ctp-auth-flow-740x680.svg/jcr:content/renditions/original)

JavaScript Example: Client-Defined Trigger for `Click to Pay` or PAN Entry {#uc-getting-started-cs-js-trigger-ctp-pan-example}
==============================================================================================================================

When you display `CLICKTOPAY` or `PANENTRY` as allowed payment types, you can load the UI without displaying the `Unified Checkout` checkout button. You can do this by creating a trigger that defines what event loads the UI.  
You can create a trigger only for `CLICKTOPAY` or `PANENTRY` payment methods:

```
//PAN Entry

const trigger = client.createTrigger('PANENTRY');

//Click to Pay

const trigger = client.createTrigger('CLICKTOPAY');
```

> IMPORTANT
> When you use the ` client.createTrigger() ` method for ` Click to Pay `, you must create a custom UI. See [Click to Pay UI Guidelines](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-ui-ux.md "").

Client Version History {#uc-capture-context-versions}
=====================================================

Below is a list of client versions and the features that are included in each version.

> IMPORTANT
> ` Cybersource ` recommends that you use the most recent client version in your integration.

0.23
:
Accepts these card networks in the allowedCardNetworks field for manual card entry:

    * Carnet
    * Cartes Bancaires
    * China UnionPay with card verification value (CVV)
    * EFTPOS
    * ELO
    * JCrew PLCC
    * mada
    * Meeza

:
Ordering controls for the allowedPaymentTypes button.
:
De-coupling of PANENTRY from other payment types in the allowedPaymentTypes field.

0.24
:
Support for enabling combo cards in the capture context.
:
Support for eight-digit BINs.
:
Support for enabling card save in the capture context.

0.25
:
Addition of **Skip Verification next time** in the `Click to Pay` payment flow.
:
Support for CPF in the capture context.

0.26
:
Support for auto-lookup in `Click to Pay` when an email is included in the capture context.
:
Inclusion of the cardDetails field object in the transient token response.
:
Support for the cardholderAuthenticationStatus field object in the transient token response.
:
Support for the complete mandate.

0.28
:
Complete mandate enhancement to support `Payer Authentication` for manual card entry for Relay, Mastercard, American Express, Discover, JCB, Cartes Bancaires, China UnionPay, and ELO card brands.
:
Support for Afterpay as an allowedPaymentType.
:
Support for PayPak as an allowedCardNetwork.
:
Auto-enrollment for `Click to Pay` in supported markets.
:
Removal of the confirm or continue screen for specific use cases.
:
Static button for `Click to Pay` flows.

0.30
:
Support for iDeal, Multibanco, and Przelewy24\|P24.
:
Complete mandate enhancement to support `Payer Authentication` for Google Pay and `Click to Pay`.
:
Support for Pakistan locales (en_PK and ur_PK).
:
New look and feel of `Unified Checkout` in line with EMVCO best practices.

0.31
:
Addition of the data object of the orderInformation field object and pass-through fields.
:
Support for tokenCreate in the complete mandate.
:
Support of pass-through fields, including challenge codes and data only, for `Payer Authentication`.
:
Support for Jaywan as an allowedCardNetwork.
:
Updated the payment details response to return detected card types. Multiple card types are shown when more than one card type is detected.
:
Support for Bancontact, Dragonpay, MyBank, and Tink Pay By Bank.

0.32
:
Support for KCP and UATP in the allowedCardNetwork field.
:
Support for Konbini as a post-pay reference payment method.
:
A radio button in the UI for Cartes Bancaires dual-branded cards.

0.33
:
Support for mobile as identity for `Click to Pay` accounts.
:
Japanese language translation updates.
:
UX captures billing and shipping information when they are not included in the capture context.

0.34
:
Iframes are used instead of pop-ups to reduce pop-up blocking and streamlining mobile deployment.
:
Additional BIN range for Jaywan card types.

0.35
:
Look and feel customization.

1.0
:
Configure payment options.
:
Configure customer data and payment flow.

Capture Context {#uc-capture-context-intro}
===========================================

This section contains the information you need to set up your server. Initializing `Unified Checkout` within your webpage begins with a server-to-server call to the sessions API. This step authenticates your merchant credentials, and establishes how the frontend components will function. The sessions API request contains parameters that define how `Unified Checkout` performs.  
The server-side component provides this information:

* A transaction-specific public key is used by the customer's browser to protect the transaction.
* An authenticated context description package that manages the payment experience on the client side. It includes available payment options such as card networks, payment interface styling, and payment methods.

The functions are compiled in a JSON Web Token (JWT) object referred to as the *capture context*.  
For information on JWTs see [JSON Web Tokens](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/Appendix/uc-appendix-jwts.md ""). The capture context request is a signed JSON Web Token (JWT) that includes all of the merchant-specific parameters. This request tells the frontend JavaScript library how to behave within your payment experience. The request provides authentication, one-time keys, the target origin to the `Unified Checkout` integration in addition to allowed card networks and payment types. The capture context request includes these elements:
* allowedCardNetworks
* allowedPaymentTypes
* clientVersion
* targetOrigin
* completeMandate

Browser Support
---------------

`Unified Checkout` supports these browser versions:

* Safari 16
* Firefox 121
* Google Chrome/Chium-based browsers 118
* Microsoft Edge 118

Capture Context Example {#uc-capture-context-intro_uc-capture-context-codeblock}
--------------------------------------------------------------------------------

Use the targetOrigins and the allowedPaymentTypes fields to define the target origin and the accepted digital payment methods in your capture context. Use the completeMandate to orchestrate follow-on services such as Payments, `Decision Manager`, `Payer Authentication`, and `TMS`. For example:

```
{
  "targetOrigins" : [ "https://test.com" ],
    "clientVersion": "0.34",
    "buttonType": "CHECKOUT_AND_CONTINUE",
    "allowedCardNetworks": [
        "CARD",
        "MASTERCARD"
    ],
    "allowedPaymentTypes": [
        "PANENTRY",
        "CLICKTOPAY",
        "APPLEPAY",
        "GOOGLEPAY"
    ],
    "completeMandate": {
        "type": "CAPTURE",
        "decisionManager": true,
        "consumerAuthentication": true,
        "tms": {
            "tokenCreate": true,
            "tokenTypes": [
                "customer",
                "paymentInstrument",
                "instrumentIdentifier",
                "shippingAddress"
            ]
        }
    },
    "country": "US",
    "locale": "en_US",
    "captureMandate": {
        "billingType": "FULL",
        "requestEmail": true,
        "requestPhone": true,
        "requestShipping": true,
        "shipToCountries": [
            "US",
            "GB"
        ],
        "showAcceptedNetworkIcons": true
    },
"data":
 {
    "orderInformation": {
        "billTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "phoneNumber": "1234567890",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "email": "test@example.com"
        },
        "shipTo": {
            "country": "US",
            "firstName": "NEW",
            "lastName": "Test",
            "address2": "Desk M3-5573",
            "address1": "901 Metro Center Blvd",
            "buildingNumber": "150",
            "postalCode": "94404",
            "locality": "Foster City",
            "administrativeArea": "CA"
        },
        "amountDetails": {
            "totalAmount": "13.00",
            "currency": "USD"
        }
    },
    "clientReferenceInformation": {
      "code": "TAGX001"
    }
  }
}
```

Card Entry Form {#uc-capture-context-intro_uc-capture-context-diagram}
----------------------------------------------------------------------

This diagram shows how elements of the capture context request appear in the card entry form.

#### Figure:

Anatomy of a Manual Card Entry Form ![Image of the capture context request code and how it appears in the
entry form elements.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/anatomy-of-manual-card-entry-form-685x575.svg/jcr:content/renditions/original)

Payment Credentials API {#uc-token-get-pymnt-credentials}
=========================================================

This section contains the information you need to retrieve the full payment credentials collected by the `Unified Checkout` tool using the payment credentials API. The payment information is returned in a redundantly signed and encrypted payment object. It uses the JSON Web Tokens (JWTs) as the data standard for communicating this sensitive data.

> IMPORTANT
> Payment information returned by the ` payment-credentials ` endpoint will contain Personal Identifiable Information (PII). Retrieving this sensitive information requires your system to comply with PCI security standards. For more information on PCI security standards, see: <https://www.pcisecuritystandards.org/>  
> The response is returned using a JWE data object that is encrypted with your public key created during the `Unified Checkout` tool's integration. For more information, see [Upload Your Encryption Key](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-upload-encrypt-key-intro.md "").  
> To decrypt the JWE response, use your private key created during the `Unified Checkout` tool's integration. The decrypted content is a JWS data object containing a JSON payload. This payload can be validated with the `Unified Checkout` public signature key.  
> IMPORTANT  
> ` Cybersource ` recommends that you dynamically parse the response for the fields that you are looking for when you integrate with ` Cybersource ` APIs. ` Cybersource ` may add additional fields in the future.  
> You must ensure that your integration can handle new fields that are returned in the response. Even though the underlying data structures do not change, you must also ensure that your integration can handle changes to the order in which the data is returned. ` Cybersource ` uses semantic versioning practices, which enables you to retain backwards compatibility as new fields are introduced in minor version updates.

Returned Credentials
--------------------

A payment account number (PAN) or network token is returned on your request depending on your payment method and `Click to Pay` account status:

|     `Click to Pay` Account Status      | American Express |  Mastercard   |     Relay      |
|----------------------------------------|------------------|---------------|---------------|
| New card not saved in `Click to Pay`   | PAN              | PAN           | PAN           |
| New card saved in `Click to Pay`       | PAN              | Network Token | Network Token |
| Existing card stored in `Click to Pay` | PAN              | Network Token | Network Token |
[Payment Credentials Returned by Card Type and `Click to Pay` Account Status]

When you retrieve PAN information from the Payment Credentials API, the response includes the PAN, card expiration date, and the card verification value (CVV). When you retrieve network token information, the response includes the network token and network token cryptogram.

> IMPORTANT Relay and Mastercard always attempt to provision a network token. When a network token is not provisioned, the default payment method is the PAN. When there is a PAN transaction, the PAN is not stored in the consumers wallet and it is treated as a single transaction.
> Network tokens are generated in the wallet of the `Click to Pay` token requestor ID (TRID). When tokenization is successful, Relay attempts to complete authentication during the `Click to Pay` experience. For information on authentication, see [Click to Pay Customer Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-authentication.md "").  
> You must meet these requirements for tokenization to be successfully configured for your merchant ID (MID):

* `Click to Pay` is enabled as a digital payment in the `Business Center`.
* The transacting MID is configured for tokenization with `Click to Pay`. Contact your Implementation Consultant or Technical Account Manager to configure tokenization with `Click to Pay`.
* The allowedPaymentTypes field value is set to `CLICKTOPAY` in the capture context. For information on the capture context, see [Capture Context API](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-setup-capture-context.md "").

Endpoint {#uc-token-get-pymnt-credentials_d14e634}
--------------------------------------------------

**Production:** `GET ``https://api.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d14e641}  
**Test:** `GET ``https://apitest.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*{#uc-token-get-pymnt-credentials_d14e653}  
**Production in Saudi Arabia:** `GET ``https://api.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*  
**Test in Saudi Arabia:** `GET ``https://apitest.sa.cybersource.com``/flex/v2/payment-credentials/`*{ReferenceID}*  
The *{ReferenceID}* is the reference ID returned in the `id` field when you created the payment credentials.

Enrolling in Apple Pay {#uc-enable-digital-pay-applepay}
========================================================

Apple Pay is a digital payment service that enables users to make secure and convenient transactions using their Apple devices. Users can add their credit or debit cards to the Wallet app and use them to pay online or in apps in a safe and convenient consumer experience.  
To enable Apple Pay you must first host a public certificate on your web page and then pass your merchant name and domain name to Apple. Apple crawls out to your web page to validate the presence of this certificate to ensure the web pages are properly vetted and registered with Apple.  
Follow these steps to validate your domain and enroll in Apple Pay:

1. Navigate to Payment Configuration \&gt; `Unified Checkout`.
2. In the Apple Pay section, click **Set Up**.
3. Follow the link to download the certificate.
4. Upload the *apple-developer-merchantid-domain-association* certificate file to your web server at:  
   `/.well-known/apple-developer-merchantid-domain-association`  
   You must verify that the file is accessible through HTTPS. You can validate this by visiting `https://&lt;your-domain&gt;/.well-known/apple-developer-merchantid-domain-association`.
5. Click Verify Domain.
6. Enter the domain name where you are hosting Apple Pay. This must be the same domain to which you uploaded the public certificate.  
   Your domain is now verified for Apple Pay.

#### AFTER COMPLETING THE TASK

> IMPORTANT
> In order to run an end-to-end test of the Apple Pay service on ` Unified Checkout `, you must perform additional setup steps. See [Preparing a Device for Testing Apple Pay on Unified Checkout](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-enable-digital-pay-applepay-prep-test-device.md "").

`Click to Pay` UI Guidelines {#ctp-ui-screens}
==============================================

The UI that is built in `Unified Checkout` for `Click to Pay` is built based on the EMV `Click to Pay` XC Guidelines V1.1. `Unified Checkout` has simplified the integration of the UI. The only UI work that you must complete is the placement of the payment option.

> IMPORTANT
> You must include ` Click to Pay ` as one of the presented payment methods and not as a separate payment method.  
> `Unified Checkout` captures all card details that are manually entered by the cardholder. This enables the cardholder to enroll in `Click to Pay` and removes the requirement for the cardholder to manually enter their card details the next time they check out.  
> `Unified Checkout` provides a standard payment label in the `Unified Checkout` JavaScript that is loaded in your checkout page. One of these scenarios occurs when the cardholder selects the button:

* The cardholder is recognized.
* The cardholder is not recognized but has a `Click to Pay` account.
* The cardholder does not have a `Click to Pay` account.
  {#ctp-ui-screens_ul_gh5_35s_hjc}  
  You can also trigger the `Unified Checkout` flow using a custom button. If you are using your own custom button, your payment button or widget must display the `Click to Pay` image for the cardholder. For information about a custom button, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-cs-js-library-intro/ctp-getting-started-cs-js-trigger-ctp-pan-example.md "").

> IMPORTANT
> Your implementation consultant will ask you for a mock-up of your payment flow for confirmation that it is compliant with the ` Click to Pay ` UI design standards.

Recognized `Click to Pay` Customer {#ctp-ui-screens_section_ih5_35s_hjc}
------------------------------------------------------------------------

The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#ctp-ui-screens_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer {#ctp-ui-screens_section_kh5_35s_hjc}
--------------------------------------------------------------------------

When the cardholder has a `Click to Pay` account but is not on a registered device, they receive a one-time password to their registered email address and phone number to authenticate their identity before their stored `Click to Pay` credentials are shown:

#### Figure: {#ctp-ui-screens_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

No `Click to Pay` Account {#ctp-ui-screens_section_mh5_35s_hjc}
---------------------------------------------------------------

When the cardholder does not have a `Click to Pay` account, they can provide a new email address to perform a new lookup or they can choose to enter their card details manually. The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use:

#### Figure: {#ctp-ui-screens_fig-ctp-no-account}

No `Click to Pay` Account UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

`Click to Pay` UI Examples {#uc-appendix-ui-ux-ex}
==================================================

This section contains UI examples of how you should display `Click to Pay` on your payment page. For information about how to display the UI, see [JavaScript API Reference](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-js-reference-v1.md "").

`Click to Pay` Replaces PAN Capture
-----------------------------------

`Click to Pay` is the card entry payment option within your payment page.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex1}

`Click to Pay` Replaces PAN Capture UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex1-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex2}

`Click to Pay` Replaces PAN Capture UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex2-645x375.svg/jcr:content/renditions/original) For information about how to configure this UI, see [Loading the JavaScript Library](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-library-intro.md "").

`Click to Pay` as Radio Button
------------------------------

`Click to Pay` is a radio button for the card entry payment option within your payment page. When the cardholder selects this option, the `Click to Pay` payment flow is loaded.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex3}

`Click to Pay` Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex3-645x375.svg/jcr:content/renditions/original)

`Click to Pay` Icon on Radio Button
-----------------------------------

You can host the radio selection option for card payment with the `Click to Pay` icon displayed on the payment label. The `Unified Checkout` flow loads when the cardholder selects this option. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex4}

`Click to Pay` Icon on Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex4-645x375.svg/jcr:content/renditions/original)

Load `Click to Pay` Automatically From Trigger
----------------------------------------------

You can load the `Unified Checkout` JavaScript flow within your payment page without requiring the cardholder to select a card payment option. This example shows a recognized user payment flow where the cardholder's information is shown automatically next to the other payment methods hosted within your payment page. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex5}

`Click to Pay` Loaded Automatically From Trigger UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

Card Payment Options with `Click to Pay` in UI
----------------------------------------------

Do not present the `Unified Checkout` payment button as a separate payment method from the card payment button. If you do this, the cardholder is not prompted with their `Click to Pay` cards and must manually enter their payment details. They will also not have the option to store their card within `Click to Pay` for future use.  
These examples show multiple card payment options and `Click to Pay` in a UI:

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex6}

Multiple Card Payment Options in UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex6-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex7}

Multiple Card Payment Options in UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex7-645x325.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex8}

Multiple Card Payment Options in UI Example 3 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex8-645x375.svg/jcr:content/renditions/original)

`Click to Pay` UI Examples {#ctp-appendix-ui-ux-ex}
===================================================

This section contains UI examples of how you should display `Click to Pay` on your payment page. For information about how to display the UI, see [JavaScript API Reference](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-appendix-js-reference.md "").

`Click to Pay` Replaces PAN Capture {#ctp-appendix-ui-ux-ex_section_gxs_2tz_hjc}
--------------------------------------------------------------------------------

`Click to Pay` is the card entry payment option within your payment page.

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex1}

`Click to Pay` Replaces PAN Capture UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex1-645x375.svg/jcr:content/renditions/original)

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex2}

`Click to Pay` Replaces PAN Capture UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex2-645x375.svg/jcr:content/renditions/original) For information about how to configure this UI, see [Loading the JavaScript Library and Invoking the Accept Function](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-cs-js-library-intro.md "").

`Click to Pay` as Radio Button {#ctp-appendix-ui-ux-ex_section_jxs_2tz_hjc}
---------------------------------------------------------------------------

`Click to Pay` is a radio button for the card entry payment option within your payment page. When the cardholder selects this option, the `Click to Pay` payment flow is loaded.

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex3}

`Click to Pay` Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex3-645x375.svg/jcr:content/renditions/original)

`Click to Pay` Icon on Radio Button {#ctp-appendix-ui-ux-ex_section_lxs_2tz_hjc}
--------------------------------------------------------------------------------

You can host the radio selection option for card payment with the `Click to Pay` icon displayed on the payment label. The `Unified Checkout` flow loads when the cardholder selects this option. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-cs-js-library-intro/ctp-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex4}

`Click to Pay` Icon on Radio Button Example UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex4-645x375.svg/jcr:content/renditions/original)

Load `Click to Pay` Automatically From Trigger {#ctp-appendix-ui-ux-ex_section_nxs_2tz_hjc}
-------------------------------------------------------------------------------------------

You can load the `Unified Checkout` JavaScript flow within your own payment button without requiring the cardholder to select a card payment option. This example shows a recognized user payment flow where the cardholder's information is shown automatically next to the other payment methods hosted within your payment page. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-getting-started-cs-setup-intro/ctp-getting-started-cs-js-library-intro/ctp-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex5}

`Click to Pay` Loaded Automatically From Trigger UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

Card Payment Options with `Click to Pay` in UI {#ctp-appendix-ui-ux-ex_section_pxs_2tz_hjc}
-------------------------------------------------------------------------------------------

Do not present the `Unified Checkout` payment button as a separate payment method from the card payment button. If you do this, the cardholder is not prompted with their `Click to Pay` cards and must manually enter their payment details. They will also not have the option to store their card within `Click to Pay` for future use.  
These examples show multiple card payment options and `Click to Pay` in a UI:

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex6}

Multiple Card Payment Options in UI Example 1 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex6-645x375.svg/jcr:content/renditions/original)

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex7}

Multiple Card Payment Options in UI Example 2 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex7-645x325.svg/jcr:content/renditions/original)

#### Figure: {#ctp-appendix-ui-ux-ex_fig-ctp-ex8}

Multiple Card Payment Options in UI Example 3 ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex8-645x375.svg/jcr:content/renditions/original)

JavaScript Example: Initializing the SDK {#uc-getting-started-cs-js-library-example}
====================================================================================

```
const client = await VAS.UnifiedCheckout(sessionJWT);
```

In this example, `sessionJWT` refers to the capture context JWT.

Dual-Branded Cards {#dual-co-brand-card-support}
================================================

`Unified Checkout` accepts dual-branded cards. To use this feature, you must include the card networks that have overlapping BIN ranges in the capture context request. For example:

```
"allowedCardNetworks": ["CARD", "MASTERCARD", "AMEX", "CARTESBANCAIRES"]
```

When a card number within an overlapping BIN range is entered, the network that is listed first in the value array for the allowedCardNetworks field is used. Based on the previous example, if the card number 403550XXXXXXXXXX is entered, the payment network for payment processing is Relay.  
During the transaction, the card type is populated with the first network in the list, and the **detectedCardTypes** field returned in the transient token includes all of the detected card types in the transient token.  
The detectedCardTypes field is returned in the transient token response only when more than one card type is detected.  
If you include Cartes Bancaires as a supported dual-branded card type, `Unified Checkout` displays a radio button with Relay and Mastercard options at checkout. This enables the customer to select which payment scheme they want to use to process the payment. The radio button defaults to the card type that you specify in the capture context request, but the payment is processed using the option selected by the customer during checkout.

Set Up Customer Authentication for Relay Click to Pay {#uc-authentication-steps}
===============================================================================

Follow these steps to use the `Business Center` to enable customer authentication through Click to Pay. Authentication methods differ in each region and are dependent on the issuer, the cardholder device, and the Click to Pay configuration. These authentication methods are available:

* `3-D Secure`
* FIDO
* Card verification value (CVV)
* One-time password (OTP)

> IMPORTANT
> After you complete these steps, Relay determines which authentication method to use. When Relay determines that they will authenticate, they authenticate each Click to Pay transaction through the appropriate method. This may be a frictionless authentication or the customer may need to provide more information when required by the issuer. This is available only through Relay.
> IMPORTANT
> Relay Click to Pay authentication is not the same as consumer authentication using the complete mandate. See [Test Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-authentication.md "").

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `  
   Production URL: ` `<https://businesscenter.cybersource.com>` `  
   If you are unable to access this page, contact your sales representative. {#uc-authentication-steps_step-1}
   {#uc-authentication-steps_step-1}

2. In the `Business Center`, go to the left navigation panel and choose **Payment Configuration** \&gt; **Unified Checkout**.  
   You must have Click to Pay enabled as a digital payment method in order to use this method of authentication. Click **Manage** to view the digital payment methods that you have enabled.  
   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original)  
   If Click to Pay is not enabled, click **On** next to Click to Pay.  
   ![Manage Available Digital Payments Solutions](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-ctp.png/jcr:content/renditions/original) {#uc-authentication-steps_step-2}
   {#uc-authentication-steps_step-2}

3. Click **Set up** under Value Added Solutions. The Value Added Solutions page appears.  
   ![Value Added Solutions Page](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-vas.png/jcr:content/renditions/original)

4. Click **Set up** to set up `3-D Secure`. The 3DS page appears.

5. Enter the required information in the Merchant Details section. You must enter the information that is provided to you by your acquirer or processor.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-3ds.png/jcr:content/renditions/original)

   #### Step Result

   This completes the authentication setup for the entered acquirer merchant ID and BIN. If you do not know what these values are, you must contact your acquirer. Completing this information enables `Cybersource` to send Relay the information that is required for authentication. IMPORTANT
   Charges for ` 3-D Secure ` may apply. You must speak with your acquirer for more information about the charges associated with ` 3-D Secure `.

`Unified Checkout` Field Reference {#uc_appendix_pass_through_fields}
=====================================================================

This section includes the fields that you use for `Unified Checkout`.

Main Configuration Fields {#uc_appendix_pass_through_fields_main_fields}
------------------------------------------------------------------------

The following table describes the main configuration fields for `Unified Checkout`:

|           Field Name            | Data Type | Required? |                        Example                         |                                                                                      Details                                                                                      |
|---------------------------------|-----------|-----------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| allowedCardNetworks             | Array     | No        | `["CARD","MASTERCARD","AMEX"]`                         |                                                                                                                                                                                   |
| allowedPaymentTypes             | Array     | Yes       | `["PANENTRY","CLICKTOPAY","APPLEPAY","GOOGLEPAY"]`     | The field value can be an array of strings or an object with options.                                                                                                             |
| buttonType                      | Enum      | No        |                                                        | Possible values: * `ADD_CARD` * `SAVE_CARD` * `CARD_PAYMENT` * `CHECKOUT` * `CHECKOUT_AND_CONTINUE` * `DEBIT_CREDIT` * `DONATE` * `PAY` * `PAY_WITH_CARD` * `SUBSCRIBE_WITH_CARD` |
| clientReferenceInformation.code | String    | No        | `TAGX001`                                              |                                                                                                                                                                                   |
| clientVersion                   | String    | Yes       | `0.31`                                                 |                                                                                                                                                                                   |
| country                         | String    | Yes       | `US`                                                   |                                                                                                                                                                                   |
| locale                          | String    | Yes       | `en_US`                                                |                                                                                                                                                                                   |
| targetOrigins                   | Array     | Yes       | `["https://merchant.com","https://reseller.com:8443"]` | Each origin must contain HTTPS and include the scheme, host, and optional port.                                                                                                   |
[Main Configuration Fields]

Order Information Fields {#uc_appendix_pass_through_fields_order_information_fields}
------------------------------------------------------------------------------------

This table contains information about the data.orderInformation field object:

|                                 Field                                 |  Type   |               Required?                |      Example       |
|-----------------------------------------------------------------------|---------|----------------------------------------|--------------------|
| data.orderInformation.amountDetails.currency                          | String  | Yes                                    | `USD`              |
| data.orderInformation.amountDetails.discountAmount                    | String  | No                                     | `2.00`             |
| data.orderInformation.amountDetails.servieFeeAmount                   | String  | No                                     | `5.00`             |
| data.orderInformation.amountDetails.surcharge.amount                  | String  | No                                     | `4.50`             |
| data.orderInformation.amountDetails.taxAmount                         | String  | No                                     | `10.00`            |
| data.orderInformation.amountDetails.taxDetails\[\].taxId              | String  | No                                     | `1234`             |
| data.orderInformation.amountDetails.taxDetails\[\].type               | String  | No                                     | `N`                |
| data.orderInformation.amountDetails.totalAmount                       | String  | Yes                                    | `102.21`           |
| data.orderInformation.billTo.address1                                 | String  | Required for Afterpay                  | `1 Market St`      |
| data.orderInformation.billTo.address2                                 | String  | No                                     | `Apt B`            |
| data.orderInformation.billTo.address3                                 | String  | No                                     | `Building C`       |
| data.orderInformation.billTo.address4                                 | String  | No                                     | `Floor 2`          |
| data.orderInformation.billTo.administrativeArea                       | String  | Required for Afterpay                  | `CA`               |
| data.orderInformation.billTo.buildingNumber                           | String  | No                                     | `123`              |
| data.orderInformation.billTo.company.address1                         | String  | No                                     | `123 Street Road`  |
| data.orderInformation.billTo.company.address2                         | String  | No                                     | `Suite 100`        |
| data.orderInformation.billTo.company.address3                         | String  | No                                     | `Building A`       |
| data.orderInformation.billTo.company.address4                         | String  | No                                     | `Floor 5`          |
| data.orderInformation.billTo.company.administrativeArea               | String  | No                                     | `CA`               |
| data.orderInformation.billTo.company.buildingNumber                   | String  | No                                     | `900`              |
| data.orderInformation.billTo.company.country                          | String  | No                                     | `US`               |
| data.orderInformation.billTo.company.district                         | String  | No                                     | `Metro`            |
| data.orderInformation.billTo.company.locality                         | String  | No                                     | `Foster City`      |
| data.orderInformation.billTo.company.name                             | String  | No                                     | `Company Name`     |
| data.orderInformation.billTo.company.postalCode                       | String  | No                                     | `12345`            |
| data.orderInformation.billTo.country                                  | String  | Conditional                            | `US`               |
| data.orderInformation.billTo.district                                 | String  | No                                     | `Downtown`         |
| data.orderInformation.billTo.email                                    | String  | Required for Afterpay                  | `user@example.com` |
| data.orderInformation.billTo.firstName                                | String  | Required for Afterpay and iDEAL        | `Jane`             |
| data.orderInformation.billTo.lastName                                 | String  | Required for Afterpay and iDEAL        | `Doe`              |
| data.orderInformation.billTo.locality                                 | String  | Required for Afterpay                  | `San Francisco`    |
| data.orderInformation.billTo.middleName                               | String  | No                                     | `Michael`          |
| data.orderInformation.billTo.nameSuffix                               | String  | No                                     | `Jr.`              |
| data.orderInformation.billTo.phoneNumber                              | String  | No                                     | `111-111-1111`     |
| data.orderInformation.billTo.phoneType                                | String  | No                                     | `day`              |
| data.orderInformation.billTo.postalCode                               | String  | Required for Afterpay                  | `94105`            |
| data.orderInformation.billTo.title                                    | String  | No                                     | `Mr.`              |
| data.orderInformation.lineItems\[\].amountIncludesTax                 | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].commodityCode                     | String  | No                                     | `8471`             |
| data.orderInformation.lineItems\[\].discountAmount                    | String  | No                                     | `3.00`             |
| data.orderInformation.lineItems\[\].discountApplied                   | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].discountRate                      | String  | No                                     | `0.0500`           |
| data.orderInformation.lineItems\[\].fulfillmentType                   | String  | No                                     | `physical`         |
| data.orderInformation.lineItems\[\].gift                              | Boolean | No                                     | `false`            |
| data.orderInformation.lineItems\[\].giftCardCurrency                  | String  | No                                     | `2`                |
| data.orderInformation.lineItems\[\].invoiceDetails.productDescription | String  | No                                     | `Description`      |
| data.orderInformation.lineItems\[\].invoiceNumber                     | String  | No                                     | `INV-1001`         |
| data.orderInformation.lineItems\[\].passenger.email                   | String  | No                                     | `user@example.com` |
| data.orderInformation.lineItems\[\].passenger.firstName               | String  | No                                     | `Jane`             |
| data.orderInformation.lineItems\[\].passenger.id                      | String  | No                                     | `1234567890`       |
| data.orderInformation.lineItems\[\].passenger.lastName                | String  | No                                     | `Doe`              |
| data.orderInformation.lineItems\[\].passenger.nationality             | String  | No                                     | `US`               |
| data.orderInformation.lineItems\[\].passenger.phone                   | String  | No                                     | `111-111-1111`     |
| data.orderInformation.lineItems\[\].passenger.status                  | String  | No                                     | `standard`         |
| data.orderInformation.lineItems\[\].passenger.type                    | String  | No                                     | `ADT`              |
| data.orderInformation.lineItems\[\].productCode                       | String  | Conditional                            | `electronic_good`  |
| data.orderInformation.lineItems\[\].productDescription                | String  | No                                     | `HD Receiver`      |
| data.orderInformation.lineItems\[\].productName                       | String  | No                                     | `Receiver`         |
| data.orderInformation.lineItems\[\].productSku                        | String  | No                                     | `SKU-12345`        |
| data.orderInformation.lineItems\[\].quantity                          | String  | Conditional                            | `2`                |
| data.orderInformation.lineItems\[\].referenceDataCode                 | String  | No                                     | `REF1`             |
| data.orderInformation.lineItems\[\].referenceDataNumber               | String  | No                                     | `123`              |
| data.orderInformation.lineItems\[\].shippingDestinationTypes          | String  | No                                     | `residential`      |
| data.orderInformation.lineItems\[\].taxAmount                         | String  | No                                     | `5.40`             |
| data.orderInformation.lineItems\[\].taxAppliedAfterDiscount           | String  | No                                     | `Y`                |
| data.orderInformation.lineItems\[\].taxDetails\[\].amount             | String  | No                                     | `4.50`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].applied            | Boolean | No                                     | `true`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].code               | String  | No                                     | `1234`             |
| data.orderInformation.lineItems\[\].taxDetails\[\].exemptionCode      | String  | No                                     | `1`                |
| data.orderInformation.lineItems\[\].taxDetails\[\].rate               | String  | No                                     | `0.0750`           |
| data.orderInformation.lineItems\[\].taxDetails\[\].taxId              | String  | No                                     | `TX-123456`        |
| data.orderInformation.lineItems\[\].taxDetails\[\].type               | String  | No                                     | `STATE_SALES_TAX`  |
| data.orderInformation.lineItems\[\].taxRate                           | String  | No                                     | `0.0900`           |
| data.orderInformation.lineItems\[\].taxStatusIndicator                | String  | No                                     | `N`                |
| data.orderInformation.lineItems\[\].taxTypeCode                       | String  | No                                     | `1234`             |
| data.orderInformation.lineItems\[\].totalAmount                       | String  | Conditional                            | `59.98`            |
| data.orderInformation.lineItems\[\].typeOfSupply                      | String  | No                                     | `12`               |
| data.orderInformation.lineItems\[\].unitOfMeasure                     | String  | No                                     | `EA`               |
| data.orderInformation.lineItems\[\].unitPrice                         | String  | Required for line-item authorizations. | `29.99`            |
| data.orderInformation.lineItems\[\].unitTaxAmount                     | String  | No                                     | `1.00`             |
| data.orderInformation.lineItems\[\].weight                            | String  | No                                     | `500`              |
| data.orderInformation.lineItems\[\].weightIdentifier                  | String  | No                                     | "N"                |
| data.orderInformation.lineItems\[\].weightUnit                        | String  | No                                     | `mg`               |
| data.orderInformation.shipTo.address1                                 | String  | No                                     | `456 Nice Avenue`  |
| data.orderInformation.shipTo.address2                                 | String  | No                                     | `Unit 7`           |
| data.orderInformation.shipTo.address3                                 | String  | No                                     | `Warehouse B`      |
| data.orderInformation.shipTo.address4                                 | String  | No                                     | `Dock 3`           |
| data.orderInformation.shipTo.administrativeArea                       | String  | No                                     | `CA`               |
| data.orderInformation.shipTo.buildingNumber                           | String  | No                                     |                    |
| data.orderInformation.shipTo.country                                  | String  | No                                     | `US`               |
| data.orderInformation.shipTo.district                                 | String  | No                                     | `Midtown`          |
| data.orderInformation.shipTo.firstName                                | String  | Conditional                            | `John`             |
| data.orderInformation.shipTo.lastName                                 | String  | No                                     | `Buyer`            |
| data.orderInformation.shipTo.locality                                 | String  | No                                     | `Los Angeles`      |
| data.orderInformation.shipTo.postalCode                               | String  | No                                     | `90010`            |
[Order Information Fields]

Capture Mandate Fields {#uc_appendix_pass_through_fields_capture_mandate_fields}
--------------------------------------------------------------------------------

The following table describes the captureMandate object fields. The values in these fields determine which fields `Unified Checkout` displays in the UI:

|                  Field                  | Data Type |  Required?  |    Example    |
|-----------------------------------------|-----------|-------------|---------------|
| captureMandate.billingType              | Enum      | No          | `FULL`        |
| captureMandate.comboCard                | Boolean   | No          | `true`        |
| captureMandate.CPF.required             | Boolean   | Conditional | `true`        |
| captureMandate.requestEmail             | Boolean   | No          | `true`        |
| captureMandate.requestPhone             | Boolean   | No          | `true`        |
| captureMandate.requestSaveCard          | Boolean   | No          | `true`        |
| captureMandate.requestShipping          | Boolean   | No          | `true`        |
| captureMandate.shipToCountries          | Array     | No          | `["US","GB"]` |
| captureMandate.showAcceptedNetworkIcons | Boolean   | No          | `true`        |
| captureMandate.showConfirmationStep     | Boolean   | No          | `true`        |
[Capture Mandate Fields]

Complete Mandate Fields {#uc_appendix_pass_through_fields_complete_mandate_fields}
----------------------------------------------------------------------------------

This table contains information about the completeMandate field object:

|                 Field                  |  Type   |  Required?  |                                     Example                                     |                                                                                                      Details                                                                                                       |
|----------------------------------------|---------|-------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| completeMandate.consumerAuthentication | Boolean | Conditional | `true`                                                                          | Enable `3-D Secure` authentication for supported card types.                                                                                                                                                       |
| completeMandate.decisionManager        | Boolean | Conditional | `true`                                                                          | Enable `Decision Manager` fraud screening with device fingerprinting.                                                                                                                                              |
| completeMandate.tms.tokenCreate        | Boolean | Conditional | `true`                                                                          | Create tokens through the `Token Management Service`.                                                                                                                                                              |
| completeMandate.tms.tokenTypes         | Array   | Conditional | `["customer", "paymentInstrument", "instrumentIdentifier", "shippingAddress" ]` | Types of tokens to create: * Customer * Instrument identifier * Payment instrument * Shipping address When you do not set this field value to a token type, the default value is based on the vault configuration. |
| completeMandate.type                   | Enum    | Conditional | `CAPTURE`                                                                       | Type of transaction required.                                                                                                                                                                                      |
[Complete Mandate Fields]

Buyer Information Fields {#uc_appendix_pass_through_fields_buyer_information_fields}
------------------------------------------------------------------------------------

This table contains information about the buyerInformation field object:

|                    Field                    |  Type  |     Required?      |       Example        |
|---------------------------------------------|--------|--------------------|----------------------|
| buyerInformation.companyTaxId               | String | Regional           | `12.345.678/0001-90` |
| buyerInformation.dateOfBirth                | String | No                 | `19900101`           |
| buyerInformation.language                   | String | No                 | `en-US`              |
| buyerInformation.merchantCustomerId         | String | No                 | `cust_12345`         |
| buyerInformation.personalIdentification.cpf | String | Required in Brazil | `12345678900`        |
[Buyer Information Fields]

Client Reference Information Fields {#uc_appendix_pass_through_fields_client_reference_information_fields}
----------------------------------------------------------------------------------------------------------

This table contains information about the clientReferenceInformation field object:

|                     Field                      |  Type  | Required |  Example  |
|------------------------------------------------|--------|----------|-----------|
| clientReferenceInformation.code                | String | No       | `TAGX001` |
| clientReferenceInformation.partner.developerId | String | No       | `1234`    |
| clientReferenceInformation.partner.solutionId  | String | No       | `4567`    |
[Client Reference Information Fields]

Consumer Authentication Information Fields {#uc_appendix_pass_through_fields_consumer_authentication_fields}
------------------------------------------------------------------------------------------------------------

This table contains information about the consumerAuthenticationInformation field object. These fields are used only for `3-D Secure`:

|                       Field                       |  Type  | Required | Example |
|---------------------------------------------------|--------|----------|---------|
| consumerAuthenticationInformation.challengeCode   | String | Yes      | `01`    |
| consumerAuthenticationInformation.messageCategory | String | Yes      | `01`    |
| consumerAuthenticationInformation.acsWindowSize   | String | No       | `10`    |
[Consumer Authentication Information Fields]

Merchant Information Fields {#uc_appendix_pass_through_fields_merchant_information_fields}
------------------------------------------------------------------------------------------

The following table describes the merchantInformation.merchantDescriptor object fields:

|                           Field                           |  Type  | Required? |      Example      |
|-----------------------------------------------------------|--------|-----------|-------------------|
| merchantInformation.merchantDescriptor.address1           | String | No        | `123 Street Road` |
| merchantInformation.merchantDescriptor.administrativeArea | String | No        | `CA`              |
| merchantInformation.merchantDescriptor.alternateName      | String | No        | `Susan`           |
| merchantInformation.merchantDescriptor.country            | String | No        | `US`              |
| merchantInformation.merchantDescriptor.locality           | String | No        | `Foster City`     |
| merchantInformation.merchantDescriptor.name               | String | No        | `Jane Sales`      |
| merchantInformation.merchantDescriptor.phone              | String | No        | `111-111-1111`    |
| merchantInformation.merchantDescriptor.postalCode         | String | No        | `12345`           |
[Merchant Information Fields]

Processing Information Fields {#uc_appendix_pass_through_fields_processing_information_fields}
----------------------------------------------------------------------------------------------

This table contains information about the processingInformation field object.

|                                          Field                                           |  Type   |            Required?            |      Example      |
|------------------------------------------------------------------------------------------|---------|---------------------------------|-------------------|
| processingInformation.authorizationOptions.aftIndicator                                  | Boolean | Conditional                     | `true`            |
| processingInformation.authorizationOptions.authIndicator                                 | Enum    | No                              | `0`               |
| processingInformation.authorizationOptions.ignoreAvsResult                               | Boolean | No                              | `true`            |
| processingInformation.authorizationOptions.ignoreCvResult                                | Boolean | No                              | `true`            |
| processingInformation.authorizationOptions.initiator.credentialStoredOnFile              | Boolean | Required for stored credentials | `true`            |
| processingInformation.authorizationOptions.initiator.merchantInitiatedTransaction.reason | String  | Required for stored credentials | `1`               |
| processingInformation.businessApplicationId                                              | String  | Required for Payouts            | `AA`              |
| processingInformation.commerceIndicator                                                  | String  | No                              | `retail`          |
| processingInformation.processingInstruction                                              | String  | No                              | `NO_INSTRUCTION`  |
| processingInformation.reconciliationId                                                   | String  | No                              | `123456789012345` |
[Processing Information Fields]

Recipient Information Fields {#uc_appendix_pass_through_fields_recipient_information_fields}
--------------------------------------------------------------------------------------------

This table contains information about the recipientInformation field object. These fields are used only for payouts:

|                  Field                  |  Type  |  Required?  |   Example    |
|-----------------------------------------|--------|-------------|--------------|
| recipientInformation.accountId          | String | Conditional | `acc0123567` |
| recipientInformation.accountType        | String | Conditional | `01`         |
| recipientInformation.administrativeArea | String | No          | `GB`         |
| recipientInformation.country            | String | Conditional | `GB`         |
| recipientInformation.dateOfBirth        | String | No          | `19900101`   |
| recipientInformation.firstName          | String | Conditional | `John`       |
| recipientInformation.lastName           | String | Conditional | `Buyer`      |
| recipientInformation.middleName         | String | No          | `A`          |
| recipientInformation.postalCode         | String | No          | `12345`      |
[Recipient Information Fields]

Merchant Defined Information Fields
-----------------------------------

This table contains information about the merchantDefinedInformation\[\] field array:

|                Field                 |  Type  |                                   Required?                                    |    Example    |
|--------------------------------------|--------|--------------------------------------------------------------------------------|---------------|
| merchantDefinedInformation\[\].key   | String | Required when merchantDefinedInformation\[\].value is included in the request. | `customer_id` |
| merchantDefinedInformation\[\].value | String | Required when merchantDefinedInformation\[\].key is included in the request.   | `12345`       |
[Merchant Defined Information Fields]

Device Information Fields
-------------------------

This table contains information about the deviceInformation field object:

|            Field            |  Type  | Required? |
|-----------------------------|--------|-----------|
| deviceInformation.ipAddress | String | No        |
[Merchant Defined Information Fields]

Payment Information Fields {#uc_appendix_pass_through_fields_merchant_defined_information_fields}
-------------------------------------------------------------------------------------------------

This table contains information about the paymentInformation field object:

|                     Field                      | Type | Required? | Example |
|------------------------------------------------|------|-----------|---------|
| paymentInformation.card.typeSelectionIndicator | Enum | No        | `0`     |
[Merchant Defined Information Fields]

Allowed Payment Types Variations
--------------------------------

This table describes the possible values for the allowedPaymentTypes field object:

|   Payment Type    |                              Value                               |                 Additional Requirements in Capture Context                  |                                        Details                                         |
|-------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Manual card entry | `PANENTRY`                                                       |                                                                             | Basic card entry.                                                                      |
| Click to Pay      | `CLICKTOPAY` or `object { "type":"CLICKTOPAY","options":{...} }` | Include email in for autolookup.                                            | Auto‑check enrollment available is available through options.autoCheckEnrollment.      |
| Apple Pay         | `APPLEPAY`                                                       |                                                                             |                                                                                        |
| Google Pay        | `GOOGLEPAY`                                                      |                                                                             |                                                                                        |
| Paze              | `PAZE`                                                           |                                                                             |                                                                                        |
| iDEAL             | `IDEAL`                                                          | Include these fields: * billTo.firstName * billTo.lastName * billTo.country | Set the completeMandate.type field to `CAPTURE` or `PREFER_AUTH`.                      |
| Afterpay/Clearpay | `AFTERPAY`                                                       |                                                                             | Set the completeMandate.type field to `AUTH`, `CAPTURE` or `PREFER_AUTH`, as required. |
[Payment Types Variations]

Related Information {#uc_appendix_pass_through_fields_section_ybj_nzz_sxb}
--------------------------------------------------------------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")
  {#uc_appendix_pass_through_fields_ul_zbj_nzz_sxb}

Enrolling in Google Pay {#uc-enable-digital-pay-google}
=======================================================

Google Pay is a digital payment product offered by Google through Chrome browsers and Android devices.  
Follow these steps to enroll in Google Pay on `Unified Checkout`:

1. Navigate to Payment Configuration \&gt; `Unified Checkout`.
2. In the Google Pay section, click **Set Up**.
3. Enter your business name.
4. Click Submit.  
   You can now accept digital payments with Google Pay.

#### AFTER COMPLETING THE TASK

> IMPORTANT
> When you enable Google Pay on ` Unified Checkout `, you can specify an optional parameter that defines the types of credentials that Google Pay sends you. See [Managing Google Pay Authentication Types](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-enable-digital-pay-googlepay-manage-authenticat.md "").

Supported Locales {#uc-appendix-languages}
==========================================

The locale field within the capture context request consists of an ISO 639 language code, an underscore (_), and an ISO 3166 region code. Set the locale field in your session request to display the checkout UI in the customer's language.  
`Unified Checkout` supports these locales:

| Locale  |   ISO Language   |      ISO Region      |
|---------|------------------|----------------------|
| `ar_AE` | Arabic           | United Arab Emirates |
| `bg_BG` | Bulgarian        | Bulgaria             |
| `ca_ES` | Catalan          | Spain                |
| `cs_CZ` | Czech            | Czechia              |
| `da_DK` | Danish           | Denmark              |
| `de_AT` | German           | Austria              |
| `de_DE` | German           | Germany              |
| `el_GR` | Greek            | Greece               |
| `en_AU` | English          | Australia            |
| `en_CA` | English          | Canada               |
| `en_GB` | English          | United Kingdom       |
| `en_IE` | English          | Ireland              |
| `en_NZ` | English          | New Zealand          |
| `en_PK` | English          | Pakistan             |
| `en_US` | English          | United States        |
| `es_AR` | Spanish          | Argentina            |
| `es_CL` | Spanish          | Chile                |
| `es_CO` | Spanish          | Colombia             |
| `es_ES` | Spanish          | Spain                |
| `es_MX` | Spanish          | Mexico               |
| `es_PE` | Spanish          | Peru                 |
| `es_US` | Spanish          | United States        |
| `fi_FI` | Finnish          | Finland              |
| `fr_CA` | French           | Canada               |
| `fr_FR` | French           | France               |
| `he_IL` | Hebrew           | Israel               |
| `hr_HR` | Croatian         | Croatia              |
| `hu_HU` | Hungarian        | Hungary              |
| `id_ID` | Indonesian       | Indonesia            |
| `it_IT` | Italian          | Italy                |
| `ja_JP` | Japanese         | Japan                |
| `km_KH` | Khmer            | Cambodia             |
| `ko_KR` | Korean           | South Korea          |
| `lo_LA` | Lao              | Laos                 |
| `ms_MY` | Malay            | Malaysia             |
| `nb_NO` | Norwegian Bokmål | Norway               |
| `nl_NL` | Dutch            | Netherlands          |
| `pl_PL` | Polish           | Poland               |
| `pt_BR` | Portuguese       | Brazil               |
| `ro_RO` | Romanian         | Romania              |
| `ru_RU` | Russian          | Russia               |
| `sk_SK` | Slovak           | Slovakia             |
| `sl_SI` | Slovenian        | Slovenia             |
| `sv_SE` | Swedish          | Sweden               |
| `th_TH` | Thai             | Thailand             |
| `tl_PH` | Tagalog          | Philippines          |
| `tr_TR` | Turkish          | Türkiye              |
| `ur_PK` | Urdu             | Pakistan             |
| `vi_VN` | Vietnamese       | Vietnam              |
| `zh_CN` | Chinese          | China                |
| `zh_HK` | Chinese          | Hong Kong            |
| `zh_MO` | Chinese          | Macao                |
| `zh_SG` | Chinese          | Singapore            |
| `zh_TW` | Chinese          | Taiwan               |
[Supported Locales]

Transient Tokens {#uc-tokens-intro}
===================================

The response to a successful customer interaction with `Unified Checkout` is a transient token. This is returned in the response from the checkout.mount() function. The transient token is a reference to the payment data collected on your behalf. Transient tokens allow secure card payments to occur without risk of exposure to sensitive payment information. The transient token is a short-term token that expires after 15 minutes. This reduces your PCI burden/responsibility and ensures that sensitive information is not exposed to your back-end systems.  
Transient tokens can be included requests sent to the Payment Details API for the customer payment data that is collected.

Test Payment Details {#uc-reference-test-cards}
===============================================

Use these test card numbers to test your `Unified Checkout` configuration.  
Combine the BIN with the card number when sending to `Unified Checkout`.

`Unified Checkout` Test Cards
-----------------------------

To test `Payer Authentication`, you must use `Payer Authentication` test cards. See [Test Cases for 3-D Secure 2.x](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "") in the *`Payer Authentication` Developer Guide*.

|    Card Brand    |  BIN   | Card Number  | Expiration Date | CVV  |
|------------------|--------|--------------|-----------------|------|
| Relay             | 411111 | 1111111111   | 12/2025         | 123  |
| Mastercard       | 555555 | 5555554444   | 02/2026         | 265  |
| American Express | 378282 | 246310005    | 03/2026         | 7890 |
| Cartes Bancaires | 436000 | 0001000005   | 04/2040         | 123  |
| Carnet           | 506221 | 0000000009   | 04/2024         | 123  |
| China UnionPay   | 627988 | 6248094966   | 04/2040         | 123  |
| Diners Club      | 305693 | 09025904     | 04/2040         | 123  |
| Discover         | 644564 | 4564456445   | 04/2040         | 123  |
| JCB              | 353011 | 13333 0000   | 04/2040         | 123  |
| Jaywan           | 679009 | 0000002009   | 04/2040         | 123  |
| Paypak           | 220543 | 0000003002   | 04/2040         | 123  |
| Maestro          | 675964 | 9826438453   | 04/2040         | 123  |
| mada             | 446404 | 0000000007   | 04/2040         | 123  |
| ELO              | 451416 | 0000000003   | 04/2040         | 123  |
| JCrew            | 515997 | 1500000005   | 04/2040         | 123  |
| EFTPOS           | 401795 | 000000000009 | 04/2040         | 123  |
| Meeza            | 507808 | 3000000002   | 04/2040         | 123  |
[Test Card Numbers]

Relay `Click to Pay` Test Cards {#uc-reference-test-cards_card-test-cards}
-------------------------------------------------------------------------

These Relay test cards can be added to your `Click to Pay` wallet. Replace the X in the card number with 0.  
You can manage your Relay `Click to Pay` test cards and account here:

* **Production:** [login](https://src.relay.com/login "")
* **Test:** [login](https://sandbox.src.relay.com/login "")  
  To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

|   Card Number    | Expiration Date | CVV |
|------------------|-----------------|-----|
| 46229431231X2700 | 12/2026         | 938 |
| 46229431231X2718 | 12/2026         | 605 |
| 46229431231X2726 | 12/2026         | 579 |
| 46229431231X2734 | 12/2026         | 141 |
| 46229431231X2742 | 12/2026         | 279 |
| 46229431231X2759 | 12/2026         | 669 |
| 439584XXX449X11X | 12/2025         | 509 |
| 439584XXX282X11X | 12/2025         | 693 |
[Relay Test Card Numbers]

Use these test cards to test when you use a `Click to Pay` card with authentication performed outside `Click to Pay` and the consumerAuthentication field is set to `true` in the capture context.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 46229431231X2X56 | 12/2026         | 432 |
| Relay       | 46229431231X232X | 12/2026         | 581 |
| Mastercard | 512X35X1XXX64578 | Any future date | Any |
| Mastercard | 512X35X1XXX64552 | Any future date | Any |
[Test Card Numbers for Authentication Outside `Click to Pay` Flow]

Use these cards when authentication is performed by `Click to Pay` within the `Click to Pay` flow.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 43958XXX0449X11X | 12/2025         | 509 |
| Relay       | 439584XXX282X11X | 12/2025         | 693 |
| Relay       | 439584XX91X1XX11 | 12/2025         | 676 |
| Relay       | 439584XX9119XX11 | 12/2025         | 789 |
[`Click to Pay` Test Card Numbers for Authentication in `Click to Pay` Flow]

For information about testing authentication, see[Test Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-authentication.md ""). For information about enabling Relay customer authentication, see [Set Up Customer Authentication for Relay Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-authentication-steps.md "").

Mastercard `Click to Pay` Test Cards {#uc-reference-test-cards_mc-test-cards}
-----------------------------------------------------------------------------

Mastercard test cards can be added to your `Click to Pay` wallet. You must retrieve Mastercard test cards from their `Click to Pay` test page: [#test-cards](https://developer.mastercard.com/mastercard-checkout-solutions/documentation/testing/test_cases/click_to_pay_case/#test-cards "")  
Mastercard has different test cards for retrieving tokenized and non-tokenized data. `Cybersource` recommends that you use these test cards as follows:

* Test cards to retrieve PAN data: Use these cards when the customer is completing checkout as a one-time guest and does not have a `Click to Pay` account or want to create one.

* Test cards to retrieve token data: Use these cards for tokenized `Click to Pay` transactions.  
  You can manage your Mastercard `Click to Pay` test cards and account here:

* **Live:** [enroll](https://src.mastercard.com/profile/enroll "")

* **SBX:** [enroll](https://sandbox.src.mastercard.com/profile/enroll "")  
  To manage Mastercard test cards for customer authentication, contact your implementation consultant or technical account manager.

Echeck Test Values {#uc-reference-test-cards_echeck-test-vals}
--------------------------------------------------------------

These eCheck test values can be used to process a test eCheck transactions:

* **Routing number:** Set to 071923284
* **Account number:** Set to any supported value. For example, 1234567890.

Enrolling in Alternative Payment Methods {#uc-enable-altpay}
============================================================

Before you can enroll in alternative payment methods on `Unified Checkout`, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.

Managing Google Pay Authentication Types {#uc-enable-digital-pay-googlepay-manage-authentication}
=================================================================================================

Additional controls are available for Google Pay on `Unified Checkout`. When you enable Google Pay on `Unified Checkout`, you can specify optional parameters that define the types of card authentication you receive from Google Pay. To manage the types of credentials that Google Pay sends, use this expanded payment type object within the allowedPaymentTypes section of the sessions request:

```
"paymentConfigurations": {
    "GOOGLEPAY": {
      "allowedAuthMethods": "&lt;authentication type&gt;"
    }
```

The expanded payment type object has these parameters:

* type: Defines the type of payment option.
* options: Contains specific payment types parameters.  
  For Google Pay, use the new data element allowedAuthMethods within the options section of the payment types object to specify the authentication type you will receive from Google Pay. Possible values:
  * `PAN_ONLY`: Google returns primary account number (PAN) values
  * `CRYPTOGRAM_3DS`: Google returns fully authenticated network token values.
    By default, Google sends both authentication types.

  > IMPORTANT
  > When the complete mandate is used and Google Pay does not authenticate the transaction, then ` Unified Checkout ` completes the authentication request as part of the complete mandate.
  > REST Example: Specify Only PAN Authentication Accepted from Google  
  > This sessions request example specifies that Google Pay is to send only PAN values.

```
"allowedPaymentTypes": [
  "GOOGLEPAY"
],
"paymentConfigurations": {
    "GOOGLEPAY": {
      "allowedAuthMethods": [
        "PAN_ONLY",
        "CRYPTOGRAM_3DS"
      ]
    }
  }
```

REST Example: Simple Google Pay Request  
This sessions request example specifies that Google Pay can send all authentication types. This can be enabled and configured in the `Business Center`. For information about configuring your allowed payment types, see [Configure Payment Options](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-payment-options.md "").

```
"allowedPaymentTypes": [
  "PANENTRY",
  "GOOGLEPAY",
  "CLICKTOPAY",
  "PAZE",
  "CHECK"
]
```

JavaScript API Reference {#uc-appendix-js-reference_api_reference}
==================================================================

This reference provides details about the JavaScript API for creating the `Unified Checkout` payment form.

Preparing a Device for Testing Apple Pay on `Unified Checkout` {#uc-enable-digital-pay-applepay-prep-test-device}
=================================================================================================================

To run an end-to-end test of the Apple Pay service on `Unified Checkout`, you must prepare an Apple test device by loading Apple Pay test cards onto the device.

1. Follow these steps to prepare your Apple test device for end-to-end testing:

2. Make sure your Apple Developer account is configured for Apple Pay.

3. Register your Apple Pay test device with Apple.

4. Load Apple Pay test cards onto your Apple test device.

   #### ADDITIONAL INFORMATION

   The Apple Developer center provides the instructions in the [Sandbox Testing](https://developer.apple.com/apple-pay/sandbox-testing/ "") page for Apple Pay:

   1. Follow the steps described in Create a Sandbox Tester Account.
5. Follow the steps described in Adding a Test Card Number.

JavaScript Example: Displaying the Button List {#uc-getting-started-cs-js-button-example}
=========================================================================================

After you initialize the `Unified Checkout` object, you can add the payment application and payment acceptance pages to your webpage. You can attach the embedded `Unified Checkout` tool and payment acceptance pages to any named element within your HTML. Typically, they are attached to explicit named components that are replaced with `Unified Checkout`'s iframes.

```
// Sidebar
const result = await checkout.mount('#buttons');

// Embedded
const result = await checkout.mount({
  paymentSelection: '#buttons',
  paymentScreen: '#form'
});
```

`Click to Pay` UI Examples {#uc-appendix-ui-ux-ex}
==================================================

This section contains UI examples of how you should display `Click to Pay` on your payment page. For information about how to display the UI, see [JavaScript API Reference](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-js-reference.md "").

`Click to Pay` Replaces PAN Capture
-----------------------------------

`Click to Pay` is the card entry payment option within your payment page.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex1}

`Click to Pay` Replaces PAN Capture UI Example 1 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex1-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex2}

`Click to Pay` Replaces PAN Capture UI Example 2 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex2-645x375.svg/jcr:content/renditions/original) For information about how to configure this UI, see [Loading the JavaScript Library and Invoking the Accept Function](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-library-intro.md "").

`Click to Pay` as Radio Button
------------------------------

`Click to Pay` is a radio button for the card entry payment option within your payment page. When the cardholder selects this option, the `Click to Pay` payment flow is loaded.

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex3}

`Click to Pay` Radio Button Example UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex3-645x375.svg/jcr:content/renditions/original)

`Click to Pay` Icon on Radio Button
-----------------------------------

You can host the radio selection option for card payment with the `Click to Pay` icon displayed on the payment label. The `Unified Checkout` flow loads when the cardholder selects this option. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex4}

`Click to Pay` Icon on Radio Button Example UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex4-645x375.svg/jcr:content/renditions/original)

Load `Click to Pay` Automatically From Trigger
----------------------------------------------

You can load the `Unified Checkout` JavaScript flow within your payment page without requiring the cardholder to select a card payment option. This example shows a recognized user payment flow where the cardholder's information is shown automatically next to the other payment methods hosted within your payment page. For information about customizing how to trigger `Unified Checkout`, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex5}

`Click to Pay` Loaded Automatically From Trigger UI ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex5-645x475.svg/jcr:content/renditions/original)

Card Payment Options with `Click to Pay` in UI
----------------------------------------------

Do not present the `Unified Checkout` payment button as a separate payment method from the card payment button. If you do this, the cardholder is not prompted with their `Click to Pay` cards and must manually enter their payment details. They will also not have the option to store their card within `Click to Pay` for future use.  
These examples show multiple card payment options and `Click to Pay` in a UI:

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex6}

Multiple Card Payment Options in UI Example 1 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex6-645x375.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex7}

Multiple Card Payment Options in UI Example 2 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex7-645x325.svg/jcr:content/renditions/original)

#### Figure: {#uc-appendix-ui-ux-ex_fig-ctp-ex8}

Multiple Card Payment Options in UI Example 3 ![](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-ex8-645x375.svg/jcr:content/renditions/original)

`Click to Pay` UI Guidelines {#uc-appendix-ui-ux}
=================================================

The UI that is built in `Unified Checkout` for `Click to Pay` is built based on the EMV `Click to Pay` XC Guidelines V1.1. `Unified Checkout` has simplified the integration of the UI. The only UI work that you must complete is the placement of the payment option.

> IMPORTANT
> You must include ` Click to Pay ` as one of the presented payment methods and not as a separate payment method.  
> `Unified Checkout` captures all card details that are manually entered by the cardholder. This enables the cardholder to enroll in `Click to Pay` and removes the requirement for the cardholder to manually enter their card details the next time they check out.  
> `Unified Checkout` provides a standard payment label in the `Unified Checkout` JavaScript that is loaded in your checkout page. One of these scenarios occurs when the cardholder selects the button:

* The cardholder is recognized.
* The cardholder is not recognized but has a `Click to Pay` account.
* The cardholder does not have a `Click to Pay` account.  
  You can also trigger the `Unified Checkout` flow using a custom button. If you are using your own custom button, your payment button or widget must display the `Click to Pay` image for the cardholder. For information about a custom button, see [JavaScript Example: Client-Defined Trigger for Click to Pay or PAN Entry](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-getting-started-cs-js-trigger-ctp-pan-example.md "").

> IMPORTANT
> Your implementation consultant will ask you for a mock-up of your payment flow for confirmation that it is compliant with the ` Click to Pay ` UI design standards.

Recognized `Click to Pay` Customer
----------------------------------

The cardholder is presented with their stored `Click to Pay` cards in the UI when they are on a recognized device:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-recog-device}

Recognized `Click to Pay` Customer UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-device-445x200.svg/jcr:content/renditions/original)

Unrecognized `Click to Pay` Customer
------------------------------------

When the cardholder has a `Click to Pay` account but is not on a registered device, they receive a one-time password to their registered email address and phone number to authenticate their identity before their stored `Click to Pay` credentials are shown:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-recog-account}

Unrecognized `Click to Pay` Customer on a Recognized Device UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-recog-account-445x330.svg/jcr:content/renditions/original)

No `Click to Pay` Account
-------------------------

When the cardholder does not have a `Click to Pay` account, they can provide a new email address to perform a new lookup or they can choose to enter their card details manually. The cardholder can make a one-time payment or complete the payment and choose to create a `Click to Pay` account for future use:

#### Figure: {#uc-appendix-ui-ux_fig-ctp-no-account}

No `Click to Pay` Account UI ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ctp-no-account-445x330.svg/jcr:content/renditions/original)

Test Authentication {#uc_appendix_authentication}
=================================================

Use this table to determine how to test your authentication method.

| Payment Method |                  Authentication                   |        Minimum Follow-On Actions         |                                                                                                 Prerequisites                                                                                                  |                                                                                                     Test Cards                                                                                                     |                                                                                                                                                                                                                 Details                                                                                                                                                                                                                  |
|----------------|---------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAN Entry      | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `true`.                                                           | See [Testing `Payer Authentication`](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md "") in the *`Payer Authentication` Developer Guide.* | When the complete mandate is not used, `Unified Checkout` does not initiate authentication and you must perform authentication within your own environment.                                                                                                                                                                                                                                                                              |
| `Click to Pay` | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | The transacting MID must be enabled for `Payer Authentication` and the complete mandate is used with the consumerAuthentication field set to `true`. Authentication for `Click to Pay` must not be configured. | See [Unified Checkout Test Cards](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-reference-test-cards-uc.md "").                                               | When authentication is not enabled for `Click to Pay` or `Click to Pay` is not able to perform authentication for `Click to Pay`, `Unified Checkout` performs authentication using `Payer Authentication` when the complete mandate is used with the consumerAuthentication field set to `true`.                                                                                                                                         |
| `Click to Pay` | Relay `Click to Pay`                               | Authorization and `Payer Authentication` | You must configure the authentication for `Click to Pay`. `Click to Pay` performs authentication only if it is a tokenized Relay card.                                                                          | See [Test Cards for Authentication by Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-reference-test-cards-auth-ctp.md "").                       | When authentication is enabled for `Click to Pay`, authentication is attempted for all `Click to Pay` transactions for Relay cards that are stored in `Click to Pay`. For information about setting up authentication for Relay `Click to Pay`, see [Set Up Customer Authentication for Relay Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-authentication-steps.md ""). |
| Google Pay     | Google Pay                                        | Authorization                            | A Google device must be used with biometric authentication for Google authentication.                                                                                                                          |                                                                                                                                                                                                                    | A user authenticates themselves on a Google device with a tokenized Google Pay credential -- the returned payload from Google will be Authenticated                                                                                                                                                                                                                                                                                      |
| Google Pay     | `Payer Authentication` through `Unified Checkout` | Authorization and `Payer Authentication` | You must use a device, such as a web browser, that does not authenticate the cardholder as part of the authorization process.                                                                                  |                                                                                                                                                                                                                    | Google will return an un-authenticated payload to Unified Checkout . Unified Checkout will step in and process Authentication via Payer Authentication when the Complete Mandate function is used with consumerAuthentication                                                                                                                                                                                                            |
[Authentication Testing by Product]

Google Pay {#uc-pay-methods-dig-wallets-googlepay}
==================================================

Google Pay is a simple, secure in-app mobile and Web payment solution. This section includes information about accepting Google Pay payments with your `Unified Checkout` integration.

MyBank {#uc-pay-methods-obt-mybank}
===================================

MyBank enables customers to pay for their online purchases in an easy and safe way using real-time bank transfers. MyBank customers complete payments by selecting their bank and logging in with their online banking credentials.  
When the total amount of the order is outside the range of accepted transaction amounts, the MyBank payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: EUR 999,999,999.99

Opt in to MyBank on `Unified Checkout`
--------------------------------------

Follow these steps to opt in to MyBank on `Unified Checkout`:

1. Add MyBank to your integration by adding `MYBANK` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Enrolling in eCheck/ACH Services {#uc-enable-digital-pay-echeck}
================================================================

`Unified Checkout` can accept bank account payments using the eCheck product. To accept eCheck payments through `Unified Checkout`, you must have the eCheck processing service enabled. To request access to eCheck processing and enable eCheck, you must submit an application in the `Business Center`. Once your application is approved, you can accept eCheck payments.  
For step-by-step instructions on enrolling and enabling eCheck, see the "Getting Started with the eCheck Service" section of the *[eCheck Merchant Guide](https://developer.cybersource.com/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide/echeck-gs.md "")* . If eCheck is not listed in the Available Products section in the `Business Center`, you must contact your portfolio owner to enable your account to apply for eCheck.  
IMPORTANT If you have a business account or a financial relationship with Bank of America, Wells Fargo, or Chase, and you would like them to process your transactions, you must contact our Sales or Support team for more information on our ACH product.

Multibanco {#uc-pay-methods-obt-multibanco}
===========================================

Multibanco enables customers to pay for a range of goods and services by bank transfer. These services include e-commerce, licenses, and taxes post-purchase. Multibanco is supported by all banks in Portugal.  
When the total amount of the order is outside the range of accepted transaction amounts, the Multibanco payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: No minimum
* **Maximum transaction amount**: EUR 99,999

Opt in to Multibanco on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add Multibanco to your integration by adding `MULTIBANCO` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

iDeal {#uc-pay-methods-obt-ideal}
=================================

iDEAL enables customers to pay online through their mobile banking app or online bank account and provides you with a payment guarantee. iDEAL supports these banks:

* ABN AMRO

* ASN Bank

* bunq

* ING

* Knab

* Rabobank

* RegioBank

* Revolut

* SNS

* Svenska Handelsbanken

* Triodos Bank

* Van Lanschot  
  When the total amount of the order is outside the range of accepted transaction amounts, the iDeal payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01

* **Maximum transaction amount**: Subject to transaction approval from the customer's account.

Opt in to iDeal on `Unified Checkout`
-------------------------------------

Follow these steps to opt in to iDeal on `Unified Checkout`:

1. Add iDeal to your integration by adding `IDEAL` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

`Click to Pay` {#uc-pay-methods-dig-wallets-ctp}
================================================

`Click to Pay` is a secure online checkout method that enables customers to make purchases without entering their payment details for every purchase. This section includes information about accepting `Click to Pay` payments with your `Unified Checkout` integration.

Process Payments with `Unified Checkout` {#uc_pay_processing_intro}
===================================================================

Payment processing is a payment completion option in your merchant configuration. Your configuration determines if your checkout system automatically handles and finalizes customer payments. When payment processing is enabled, `Unified Checkout` handles the complete payment for you automatically. When payment processing not enabled, you complete payments independently using your selected gateway.

Payment Processing Enabled
--------------------------

`Cybersource` recommends that you enable payment processing if you meet these requirements:

* Your integration is configured with the payment completion step. For more information about completeMandate() see [Complete Mandate](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-cc-complete-mandate.md "").

* You do not have a designated technical team to process payments.

* Your integration includes any of these features:

  * Fraud checks with `Decision Manager` or `Fraud Management Essentials`
  * `3-D Secure`/ `Payer Authentication`
  * Stored customer credentials with the `Token Management Service`(`TMS`)
* Multiple payment methods  
  When payment processing is enabled, you can choose how payments should be handled:

* **Preferred Authorization**: The payment is authorized first and captured at a later time. This method works well for businesses that ship products to their customers. For example, you authorize the payment when the customer places and order and capture the payment when you ship it.

* **Sale**: The payment is captured immediately. This method works well for service businesses, digital products, and immediate purchases.

> IMPORTANT
> Not all payment methods are compatible with all processing types. Different payment methods work with different payment processing types. You must configure your payment processing settings to be compatible with your integration and review which payment methods are compatible. For information about payment methods and their processing compatibility, see [Payment Methods](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-intro.md "").

Payment Processing Disabled
---------------------------

`Cybersource` recommends that you disable payment processing if you meet these requirements:

* You want to process payments on `our platform` using your own API requests instead of relying on the automatic payment completion step.
* You want full control over your checkout and payment orchestration flow.
* You only use `Unified Checkout` to collect encrypted payment information and you handle the completion phase through `our platform` APIs or your custom back-end. The completion phase includes authorization, sale, fraud checks, `3-D Secure` and card storage.

When disable payment processing, the checkout system will collect payment information from your customers but you will need to process the actual payment on your end. When payment processing is disabled, you must consider the following:

* Customer payments are not completed automatically.
* Fraud checks and `3-D Secure` using automatic orchestration are disabled.
* Saved credentials and token management using automatic processing are disabled.
* You must handle payment completion yourself.

JavaScript API Reference {#uc-appendix-js-reference-v1_api_reference}
=====================================================================

This reference provides details about the JavaScript API for creating the `Unified Checkout` v1 payment form.

Payment Methods {#uc-pay-methods-intro}
=======================================

This section describes the payment methods you can use in your `Unified Checkout` integration. After you successfully integrate one payment method, you can add another from the same category with minimal adjustments to your existing configuration.  
These payment methods are available:

* [Cards](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-card.md "")
* [eCheck/ACH Service](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-echeck.md "")
* [Apple Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-dig-wallets-applepay.md "")
* [Google Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-dig-wallets-googlepay.md "")
* [Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-dig-wallets-ctp.md "")
* [Paze](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-dig-wallets-paze.md "")
* [Online Bank Transfers](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt.md "")
* [Buy Now, Pay Later](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-bnpl.md "")
* [Post-Pay Reference Payments](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-ppr.md "")
* [PayPal](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-bnpl-paypal.md "")
* [Venmo](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-venmo.md "")

Online Bank Transfers {#uc-pay-methods-obt}
===========================================

Online bank transfers enable customers to complete their purchase by securely logging into their online banking environment. This method is secure, trusted, and widely used in many European countries.

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how online bank transfers work:

#### Figure:

Online Bank Transfers ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-obt-650x130.svg/jcr:content/renditions/original)
1. The customer chooses online bank transfer as their payment method during checkout.
2. The customer chooses their bank from the list of available banks and is redirected to their bank's website or application where they are prompted to enter their account credentials.
3. The customer confirms their payment and completes the authorization process.
4. The customer is notified that the payment is complete.
5. The customer returns to your website for payment confirmation.  
   `Unified Checkout` supports these online bank transfer payment methods:

* Bancontact
* DragonPay
* iDeal
* Multibanco
* MyBank
* Przelewy24\|P24
* Tink Pay By Bank

|  Payment Method  | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| iDEAL            | `IDEAL`                             | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Netherlands (NL)                | EUR                        |
| Multibanco       | `MULTIBANCO`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR                        |
| Przelewy24       | `PRZELEWY24`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Poland (PL)                     | PLN                        |
| Bancontact       | `BANCONTACT`                        | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Italy (IT)                      | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Belgium (BE)                    | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Portugal (PT)                   | EUR                        |
| MyBank           | `MYBANK`                            | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Spain (ES)                      | EUR                        |
| DragonPay        | `DRAGONPAY`                         | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Philippines (PH)                | PHP                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | France (FR)                     | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Germany (DE)                    | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Ireland (IE)                    | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Netherlands (NL)                | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Spain (ES)                      | EUR                        |
| Tink Pay by Bank | `TINKPAYBYBANK`                     | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | United Kingdom (GB)             | GBP                        |
[Online Bank Transfer Payment Methods]

Bancontact {#uc-pay-methods-obt-bancontact}
===========================================

Bancontact enables customers to make secure online and in-store purchases directly from their bank accounts. Bancontact is a leading payment method in Belgium.  
When the total amount of the order is outside the range of accepted transaction amounts, the Bancontact payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: EUR 0.01
* **Maximum transaction amount**: Not applicable

Opt in to Bancontact on `Unified Checkout`
------------------------------------------

Follow these steps to opt in to Bancontact on `Unified Checkout`:

1. Add Bancontact to your integration by adding `BANCONTACT` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Captures {#uc-pay-methods-wallet-captures}
==========================================

When you set the completeMandate.type field value to `AUTH` or `PREFER_AUTH`, you must send a request to capture an authorized payment. Full and partial captures are supported.

Endpoint {#uc-pay-methods-wallet-captures_d9e147}
-------------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-wallet-captures_d9e156}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-wallet-captures_d9e169}  
The *{id}* is the transaction ID returned in the authorization response.

Example: Authorization Response from `Unified Checkout`
-------------------------------------------------------

```
{
  "details": {
    "clientReferenceInformation": {
      "code": "1753351101383"
    },
    "orderInformation": {
      "amountDetails": {
        "currency": "USD",
        "totalAmount": "21.00"
      }
    },
    "processorInformation": {
      "approvalCode": "AUTH456789",
      "responseCode": "00003",
      "responseDetails": "00003",
      "transactionId": "2016011808153910011808153AUTH"
    },
    "reconciliationId": "04RYADD29YRO",
    "submitTimeUtc": "2025-07-24T09:58:21Z"
  },
  "id": "7533511014286971803092",
  "message": "Request processed successfully.",
  "outcome": "AUTHORIZED",
  "status": "AUTHORIZED"
}
```

Response Status
---------------

`Cybersource` responds to your capture request with one of these statuses:

* `FAILED`: The capture request failed.
* `PENDING`: The capture request is accepted but not captured. Send a request to the check status service to retrieve status updates.
* `SETTLED`: The capture request is settled for the amount requested.

Afterpay {#uc-pay-methods-bnpl-afterpay}
========================================

Afterpay is a Buy Now, Pay Later service that allows customers to purchase items immediately and pay for them in four interest-free installments over a period of 6 weeks. Afterpay is also known as Clearpay in the UK, and Cash App Afterpay in the US. For more information, see the [*Afterpay and Clearpay Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/afterpay/developer/all/so/afterpay/afterpay-intro.md "").  
When the total amount of the order is outside the range of accepted transaction amounts, the Afterpay/Clearpay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: 1 (CAD, AUD, NZD, USD, and GBP)
* **Maximum transaction amount**: Not applicable

Opt in to Afterpay on `Unified Checkout`
----------------------------------------

Follow these steps to opt in to the Afterpay/Clearpay payment method in `Unified Checkout`:

1. Add Afterpay to your integration by adding `AFTERPAY` to the allowedPaymentTypes field within the capture context request. The default field value is `AFTERPAY` even if you want to support Cash App Afterpay in the US or Clear Pay in the UK.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.  
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   You can capture the funds later if you include the completeMandate.type field in the capture context request and set the value to `AUTH`. When you capture the funds later, you must perform a capture using the payments API. See [Captures](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-bnpl-captures.md "").  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.postalCode
   * data.orderInformation.billTo.administrativeArea
   * data.orderInformation.billTo.country
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * data.orderInformation.shipTo.firstName
   * data.orderInformation.shipTo.lastName
   * data.orderInformation.shipTo.address1
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * data.orderInformation.shipTo.administrativeArea

* data.orderInformation.shipTo.country

DragonPay {#uc-pay-methods-obt-dragonpay}
=========================================

DragonPay provides Filipino customers and businesses with a secure payment channel that does not require customers to be banked or have a credit card. Customers can make purchases online and pay by bank transfer.  
When the total amount of the order is outside the range of accepted transaction amounts, the DragonPay payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PHP 50.01
* **Maximum transaction amount**: Not applicable

Opt in to DragonPay on `Unified Checkout`
-----------------------------------------

Follow these steps to opt in to Multibanco on `Unified Checkout`:

1. Add DragonPay to your integration by adding `DRAGONPAY` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:
   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Look and Feel UI Examples {#uc_ui_config_examples}
==================================================

These examples show the different preview screens for each look and feel customization feature:

Test Cards for Authentication by `Click to Pay` {#uc-reference-test-cards-auth-ctp}
===================================================================================

Use these cards when authentication is performed by `Click to Pay` within the `Click to Pay` flow.  
Replace the X in the card number with 4.  
To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 43958XXX0449X11X | 12/2025         | 509 |
| Relay       | 439584XXX282X11X | 12/2025         | 693 |
| Relay       | 439584XX91X1XX11 | 12/2025         | 676 |
| Relay       | 439584XX9119XX11 | 12/2025         | 789 |
[`Click to Pay` Test Card Numbers for Authentication in `Click to Pay` Flow]

For information about testing authentication, see[Test Authentication](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-appendix-authentication.md ""). For information about enabling Relay customer authentication, see [Set Up Customer Authentication for Relay Click to Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-authentication-steps.md "").

PayPal {#uc-pay-methods-bnpl-paypal}
====================================

PayPal is a secure and convenient payment service that your customers can use to make payments without directly using their bank accounts or credit cards. PayPal gives yours customers the option to pay in installments over time with PayPal Pay Later while also giving you the full payment immediately. These installments are available:

* **Pay in 3**: Pay in three installments. Available in the UK.
* **Pay in 4**: Pay in four installments. Available in the US.
* **Pay Monthly**: Pay in monthly recurring installments.

Opt in to Paypal on `Unified Checkout`
--------------------------------------

You can enable Paypal from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Paypal using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-payment-options.md "").  
You can also enable Paypal using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Paypal payment method using the API:

1. Add Paypal to your integration by adding `PAYPAL` to the allowedPaymentTypes field within the capture context request.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.  
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   You can capture the funds later if you include the completeMandate.type field in the capture context request and set the value to `AUTH`. When you capture the funds later, you must perform a capture using the payments API. See [Captures](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-wallet-captures.md "").  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * orderInformation.amountDetails.currency
   * orderInformation.amountDetails.taxAmount
     * This field is the sum of all orderInformation.lineItems\[\].taxAmount values.
       {#uc-pay-methods-bnpl-paypal_ul_sk5_zjq_cjc}
   * orderInformation.amountDetails.totalAmount
     * This field is the sum of (orderInformation.lineItems\[\].quantity × orderInformation.lineItems\[\].unitPrice) + orderInformation.lineItems\[\].taxAmount for all line items.
       {#uc-pay-methods-bnpl-paypal_ul_h22_zjq_cjc}
   * orderInformation.lineItems\[\].productDescription
   * orderInformation.lineItems\[\].productName
   * orderInformation.lineItems\[\].productSKU
   * orderInformation.lineItems\[\].quantity
   * orderInformation.lineItems\[\].taxAmount

     > IMPORTANT
     > This field is required for all line items when you include orderInformation.lineItems\[\].taxAmount for one line item.

     * You can set this field value to `0.00`.
       {#uc-pay-methods-bnpl-paypal_ul_lwq_r53_cjc}
   * orderInformation.lineItems\[\].typeOfSupply
   * orderInformation.lineItems\[\].unitPrice
4. Include these optional fields in the capture context request:
   * buyerInformation.dateOfBirth
   * buyerInformation.language
   * buyerInformation.personalIdentification\[\].id
   * buyerInformation.personalIdentification\[\].type
   * clientReferenceInformation.reconciliationId
   * merchantInformation.merchantDescriptor.name
     * This field affects the name that the customers see on their card statement. If the merchant is Candy Shop and passes this as their name - customer will see `PAYPAL * Candy Shop` in their bank statement.
   * orderInformation.amountDetails.taxDetails.taxId
   * orderInformation.amountDetails.taxDetails.type
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.company.name
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.phoneNumber
   * orderInformation.invoiceDetails.invoiceNumber
   * orderInformation.invoiceDetails.productDescription
   * orderInformation.lineItems\[\].totalAmount
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * paymentInformation.customer.customerid
   * processingInformation.processingInstruction
     * Set this field to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

Example: Multiple Line-Items {#uc-pay-methods-bnpl-paypal_section_zfp_mv3_cjc}
------------------------------------------------------------------------------

This example includes multiple line items in the amountDetails field object:

```
{
  "amountDetails": {
    "totalAmount": "221.91",
    "currency": "USD",
    "taxAmount": "14.42"
  },
  "lineItems": [
    {
      "productName": "501 Original Fit Jeans Blues",
      "productSku": "00501019403432",
      "quantity": 1,
      "unitPrice": "100.0",
      "totalAmount": "100.00",
      "taxAmount": "8.63"
    },
    {
      "productName": "Levi Blue shirt Plaid",
      "productSku": "0094784142",
      "quantity": 1,
      "unitPrice": "100.00",
      "totalAmount": "100.00",
      "taxAmount": "5.79"
    },
    {
      "productName": "shipping_and_handling",
      "productSku": "shipping_and_handling",
      "quantity": 1,
      "unitPrice": "7.49",
      "totalAmount": "7.49",
      "taxAmount": "0.00"
    }
  ]
}
```

{#uc-pay-methods-bnpl-paypal_codeblock_n2l_qz3_cjc}

Button List {#uc_ui_config_ex_button_list}
==========================================

This example shows the button list:

#### Figure:

Screen 1: Button List ![Image that shows the Unified Checkout Look and Feel UI button list.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ui-config-button-list-548x632.svg/jcr:content/renditions/original)

Configure Customer Data and Payment Flow {#uc_intro_customer_data}
==================================================================

Use the Customer data and payment flow section of the `Business Center` to configure the information that you want to collect during checkout. Follow these steps to customize the appearance of `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_customer_data_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_customer_data_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_customer_data_step-1}
   {#uc_intro_customer_data_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Customer Data and Payment Flow Merchant Experience ![Image that shows the Unified Checkout customer data
   and payment flow merchant experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-custdata-800x875.png/jcr:content/renditions/original) {#uc_intro_customer_data_step-2}
   {#uc_intro_customer_data_step-2}

3. In the Customer data and payment flow section, click **Manage**. The Customer information and payment flow page appears.

4. Under Contact details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Email address and Mobile phone number to collect the customer email address and phone number during checkout.

5. Under Payment details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Billing address to collect the cardholder billing address.

6. Under Payment details, in the Billing address drop-down menu, select the billing address information for payment verification:

   #### ADDITIONAL INFORMATION

   * **Full address**: Request the full cardholder billing address during checkout.
   * **Zip code only**: Request only the zip code of the cardholder billing address during checkout.
7. Under Payment details, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) next to Shipping address to collect the cardholder shipping address.

8. Under Payment details, in the Shipping address drop-down menu, select the countries that you ship to.

9. Under Checkout review step, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to display a review page for the customer to confirm the payment and shipping address.

10. Under payment processing and \& service orchestration, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) in the Payment processing section to control how to process transactions:  
    You can turn payment processing on or off:

    * **Payment Processing ON** : `Unified Checkout` handles the complete payment for you automatically. When payment processing is on, you can select how transactions are processed:
      * **Preferred auth**: Choose this option to authorize the payment when possible.
      * **Sale**: Choose this option to capture the funds immediately.
    * **Payment Processing OFF**: You must complete the payment independently using CARD or another selected gateway.

    For information about enabling or disabling payment processing in `Unified Checkout`, see [Process Payments with Unified Checkout](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-processing-intro.md "").

11. Under save customer information in payment processing and \& service orchestration, slide the toggle to the right to prompt the user to save their payment information for future use.  
    Saving customer payment details can significantly improve the checkout experience for returning customers. There are two approaches that you can use:

    * **Ask for consent to save payment information for future use**: This option displays a checkbox during checkout that asks customers if they want their payment details saved. You can enable this option regardless of if payment processing is enabled at any time.
    * **Store payment details securely in your `TMS` vault** : This option saves payment information using secure encryption and links directly to your `TMS` vault. This enables faster checkout for returning customers by using tokens rather than raw card data.

    > IMPORTANT If you already have cardholder consent (for example, if it was obtained during account creation or through another verified process) or consent is not required for your flow, you should not display or request consent again in the UI.

12. Under Fraud detection in payment processing and \& service orchestration, use the drop-down menu to turn fraud detection with `Decision Manager` or `Fraud Management Essentials` **On** or **Skip**.

13. Under Localized payment settings, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to enable these features:

    #### ADDITIONAL INFORMATION

    * **Combo cards**: Enable cardholders to decide how to process their payments.
    * **Brazil tax ID**: Collect a customer's CPF or CNPJ at checkout.

    > IMPORTANT Combo cards and tax IDs are only available in Brazil.

14. Click **Save and publish** to save your customer payment settings.
    {#uc_intro_customer_data_enable-uc}

Complete Mandate {#uc_cc_complete_mandate}
==========================================

The complete mandate feature provides service orchestration within `Unified Checkout` and simplifies your integration. Service orchestration enables `Unified Checkout` to orchestrate services on your behalf. The complete mandate feature provides instructions to the unifiedPayment.complete() method in the JavaScript. You must include both the unifiedPayment.complete() object in the Javascript and the completeMandate field object in your capture context to enable `Unified Checkout` to initiate services on your behalf from the browser.

> IMPORTANT
> If you are updating an existing ` Unified Checkout ` configuration to use the complete mandate, you must update your JavaScript to include the unifedPayment.complete() function.
> IMPORTANT
> When the billingType field is set to ` NONE ` you must include the required fields within the capture context request to ensure that the required fields are included for payment processing. For information about the fields that are required for payment services, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").

Capture Context Fields in the `Business Center` {#uc_ebc_api_info}
==================================================================

There are some components of `Unified Checkout` that are available in the API, the `Business Center` or both. This section describes which components of the Sessions API capture context object can be configured using the `Business Center`. For a complete list of fields that are available, see the [API Reference](https://developer.cybersource.com/api-reference-assets/index.md#unified-checkout "") in the `Cybersource` Developer Center.

|                      Parameter                       | `Business Center` |   API    |                                                                                                                                                                                 Notes                                                                                                                                                                                 |
|------------------------------------------------------|-------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| allowedCardNetworks                                  | Yes               | Override | Optional. This is the override priority order: 1. API 2. Merchant experience profile 3. Portfolio profile                                                                                                                                                                                                                                                             |
| allowedPaymentTypes                                  | Yes               | Override | Optional. This is the priority order: 1. API (payment types that are not enabled are removed) 2. Merchant experience profile (payment types that are not enabled are removed) 3. Portfolio profile (all payment types are enabled at the profile level) > IMPORTANT > ` SRCCARD `, ` SRCMASTERCARD `, and ` SRCAMEX ` are not supported. You must use ` CLICKTOPAY `. |
| paymentConfigurations                                | Partial           | Yes      | Allows per-transaction payment type configuration overrides. This is available only in clientVersion `1.0` or later.                                                                                                                                                                                                                                                  |
| paymentConfigurations.CLICKTOPAY                     | Yes               | Override | Default values can be set in the `Business Center`.                                                                                                                                                                                                                                                                                                                   |
| paymentConfigurations.CLICKTOPAY.autoCheckEnrollment | Yes               | Override | This payment configuration is part of the merchant experience.                                                                                                                                                                                                                                                                                                        |
| paymentConfigurations.GOOGLEPAY                      | Yes               | Override | Default values can be set in the `Business Center`.                                                                                                                                                                                                                                                                                                                   |
| paymentConfigurations.GOOGLEPAY.allowedAuthMethods   | Yes               | Override | This payment configuration is part of the merchant experience.                                                                                                                                                                                                                                                                                                        |
[API Parameters]

Capture Mandate
---------------

|        Parameter         | `Business Center` |   API    | Default Value |
|--------------------------|-------------------|----------|---------------|
| showConfirmationStep     | Yes               | Override |               |
| billingType              | Yes               | Override |               |
| requestEmail             | Yes               | Override |               |
| requestPhone             | Yes               | Override |               |
| requestShipping          | Yes               | Override |               |
| shipToCountries          | Yes               | Override |               |
| showAcceptedNetworkIcons | Yes               | Override |               |
| comboCard                | Yes               | Override |               |
| requestSaveCredentials   | Yes               | Override |               |
| cpf                      | Yes               | Override |               |
| cpf.required             | Yes               | Override |               |
[Capture Mandate Parameters]

Complete Mandate
----------------

|       Parameter        | `Business Center` |   API    | Default Value |
|------------------------|-------------------|----------|---------------|
| type                   | Yes               | Override | `SALE`        |
| decisionManager        | Yes               | Override | `true`        |
| consumerAuthentication | Yes               | Override | `false`       |
| tms                    | Yes               | Optional |               |
| tms.tokenCreate        | Yes               | Override | `true`        |
[Complete Mandate Parameters]

Appearance Variables
--------------------

|    Parameter / Variable    | `Business Center` |   API    | Default Value |       Example        |
|----------------------------|-------------------|----------|---------------|----------------------|
| buttonType                 | Yes               | Override | `CHECKOUT`    | "CHECKOUT"           |
| variables                  | Partial           | Override |               |                      |
| backgroundColor            | Yes               | Override |               | "#FFFFFF"            |
| textColor                  | Yes               | Override |               | "#000000"            |
| headerBackground           | Yes               | Override |               | "#1A237E"            |
| headerForeground           | Yes               | Override |               | "#FFFFFF"            |
| buttonBackground           | Yes               | Override |               | "#E0E0E0"            |
| buttonForeground           | Yes               | Override |               | "#333333"            |
| buttonBorderRadius         | Yes               | Override |               | "4px"                |
| fontFamily                 | Yes               | Override |               | "Roboto Slab, serif" |
| paymentSelectionBackground | Yes               | Override |               | "#F5F5F5"            |
[Top-Level Appearance Parameters and Variables]

Example: `Unified Checkout` Complete Capture Context {#uc-appendix-uc-auth-ex}
==============================================================================

Capture Context Request

```
{
  "country": "US",
  "locale": "en_GB",
  "targetOrigins": [
    "https://merchant.com",
    "https://reseller.com:8443"
  ],
  "clientVersion": "1.0",
  "allowedCardNetworks": [
    "CARD",
    "MASTERCARD",
    "AMEX",
    "JCB",
    "DISCOVER",
    "DINERSCLUB",
    "CARTESBANCAIRES",
    "EFTPOS",
    "JCREW",
    "MEEZA",
    "CUP",
    "CARNET",
    "MADA",
    "ELO",
    "MAESTRO",
    "PAYPAK",
    "JAYWAN",
    "KCP",
    "UATP"
  ],
  "allowedPaymentTypes": [
    "PANENTRY",
    "GOOGLEPAY",
    "CLICKTOPAY",
    "APPLEPAY",
    "PAZE",
    "CHECK",
    "AFTERPAY",
    "IDEAL",
    "MULTIBANCO",
    "PRZELEWY24",
    "MYBANK",
    "KONBINI",
    "DRAGONPAY",
    "BANCONTACT",
    "TINKPAYBYBANK"
  ],
  "appearance": {
    "theme": "LIGHT",
    "variables": {
      "primaryColor": "#007bff",
      "secondaryColor": "#6c757d",
      "fontFamily": "Arial, sans-serif",
      "fontSize": "14px",
      "borderRadius": "4px"
    }
  },
  "buttonType": "CHECKOUT",
  "captureMandate": {
    "showConfirmationStep": true,
    "billingType": "FULL",
    "requestEmail": true,
    "requestPhone": true,
    "requestShipping": true,
    "shipToCountries": [
      "US",
      "GB",
      "CA"
    ],
    "showAcceptedNetworkIcons": true,
    "comboCard": true,
    "requestSaveCredentials": true,
    "CPF": {
      "required": true
    }
  },
  "completeMandate": {
    "type": "CAPTURE",
    "decisionManager": true,
    "consumerAuthentication": "3DS",
    "tms": {
      "tokenCreate": true,
      "tokenTypes": [
        "customer",
        "paymentInstrument",
        "instrumentIdentifier",
        "shippingAddress"
      ]
    }
  },
  "paymentConfigurations": {
    "PANENTRY": {
      "customer": "existing_customer_token_123"
    },
    "GOOGLEPAY": {
      "allowedAuthMethods": [
        "PAN_ONLY",
        "CRYPTOGRAM_3DS"
      ]
    },
    "CLICKTOPAY": {
      "autoCheckEnrollment": true
    }
  },
  "transientTokenResponseOptions": {
    "includeCardPrefix": true
  },
  "data": {
    "orderInformation": {
      "amountDetails": {
        "totalAmount": "102.21",
        "currency": "USD",
        "surcharge": {
          "amount": "2.50"
        },
        "discountAmount": "2.00",
        "serviceFeeAmount": "5.00",
        "taxAmount": "10.00",
        "taxDetails": [
          {
            "taxId": "1234",
            "type": "N"
          },
          {
            "taxId": "5678",
            "type": "S"
          }
        ]
      },
      "billTo": {
        "address1": "123 Main Street",
        "address2": "Apt 4B",
        "address3": "Building C",
        "address4": "Floor 3",
        "administrativeArea": "CA",
        "buildingNumber": "123",
        "country": "US",
        "district": "Downtown",
        "locality": "San Francisco",
        "postalCode": "94105",
        "email": "jane.doe@relay.com",
        "firstName": "John",
        "middleName": "Michael",
        "lastName": "Doe",
        "phoneNumber": "+1-123456789",
        "phoneType": "night",
        "nameSuffix": "Mr",
        "title": "Software Engineer",
        "company": {
          "name": "Relay Inc",
          "address1": "900 Metro Center Blvd",
          "address2": "Suite 200",
          "country": "US",
          "administrativeArea": "CA",
          "postalCode": "94404",
          "locality": "Foster City"
        }
      },
      "shipTo": {
        "address1": "456 Oak Avenue",
        "address2": "Suite 100",
        "address3": "Building A",
        "address4": "Level 2",
        "administrativeArea": "NY",
        "buildingNumber": "456",
        "country": "US",
        "district": "Midtown",
        "locality": "New York",
        "postalCode": "10001",
        "firstName": "Jane",
        "lastName": "Smith"
      },
      "lineItems": [
        {
          "productCode": "WIDGET-001",
          "productName": "Premium Widget",
          "productSku": "WID-PRE-001",
          "quantity": 2,
          "unitPrice": "45.50",
          "unitOfMeasure": "EA",
          "totalAmount": "91.00",
          "taxAmount": "7.28",
          "taxRate": "0.08",
          "taxAppliedAfterDiscount": "y",
          "taxStatusIndicator": "N",
          "taxTypeCode": "1234",
          "amountIncludesTax": true,
          "typeOfSupply": "12",
          "commodityCode": "COMM-001",
          "discountAmount": "5.00",
          "discountApplied": true,
          "discountRate": "0.05",
          "invoiceNumber": "INV-2024-001",
          "taxDetails": [
            {
              "type": "STATE",
              "amount": "3.64",
              "rate": "0.04",
              "code": "1234",
              "taxId": "TAX-001",
              "applied": true,
              "exemptionCode": "1"
            },
            {
              "type": "LOCAL",
              "amount": "3.64",
              "rate": "0.04",
              "code": "5678",
              "taxId": "TAX-002",
              "applied": true,
              "exemptionCode": "2"
            }
          ],
          "fulfillmentType": "SHIP",
          "weight": "500",
          "weightIdentifier": "N",
          "weightUnit": "mg",
          "referenceDataCode": "REF-001",
          "referenceDataNumber": "REF-NUM-001",
          "unitTaxAmount": "3.64",
          "productDescription": "High-quality premium widget with extended warranty",
          "giftCardCurrency": "USD",
          "shippingDestinationTypes": "residential",
          "gift": false,
          "passenger": {
            "type": "ADT",
            "status": "confirmed",
            "phone": "+1-123456789",
            "firstName": "Robert",
            "lastName": "Johnson",
            "id": "PASS-001",
            "email": "jane.doe@relay.com",
            "nationality": "US"
          }
        },
        {
          "productCode": "GADGET-002",
          "productName": "Digital Gadget",
          "productSku": "GAD-DIG-002",
          "quantity": 1,
          "unitPrice": "29.99",
          "unitOfMeasure": "EA",
          "totalAmount": "29.99",
          "taxAmount": "2.40",
          "taxRate": "0.08",
          "taxAppliedAfterDiscount": "n",
          "taxStatusIndicator": "Y",
          "taxTypeCode": "5678",
          "amountIncludesTax": false,
          "typeOfSupply": "11",
          "commodityCode": "COMM-002",
          "discountAmount": "3.00",
          "discountApplied": true,
          "discountRate": "0.10",
          "invoiceNumber": "INV-2024-002",
          "taxDetails": [
            {
              "type": "FEDERAL",
              "amount": "2.40",
              "rate": "0.08",
              "code": "9012",
              "taxId": "TAX-003",
              "applied": true,
              "exemptionCode": "0"
            }
          ],
          "fulfillmentType": "DIGITAL",
          "weight": "0",
          "weightIdentifier": "Y",
          "weightUnit": "g",
          "referenceDataCode": "REF-002",
          "referenceDataNumber": "REF-NUM-002",
          "unitTaxAmount": "2.40",
          "productDescription": "Advanced digital gadget with cloud sync",
          "giftCardCurrency": "EUR",
          "shippingDestinationTypes": "commercial",
          "gift": true,
          "passenger": {
            "type": "CHD",
            "status": "pending",
            "phone": "+1-123456789",
            "firstName": "Emily",
            "lastName": "Williams",
            "id": "PASS-002",
            "email": "jane.doe@relay.com",
            "nationality": "GB"
          }
        }
      ],
      "invoiceDetails": {
        "invoiceNumber": "INV-MAIN-2024-001",
        "productDescription": "Multiple items including widgets and gadgets"
      }
    },
    "buyerInformation": {
      "personalIdentification": [
        {
          "type": "CPF",
          "id": "01234567890"
        }
      ],
      "merchantCustomerId": "CUST-12345",
      "companyTaxId": "123456789",
      "dateOfBirth": "19901215",
      "language": "en"
    },
    "clientReferenceInformation": {
      "code": "TAGX001",
      "partner": {
        "developerId": "DEV-1234",
        "solutionId": "SOL-4567"
      }
    },
    "consumerAuthenticationInformation": {
      "challengeCode": "01",
      "messageCategory": "01",
      "acsWindowSize": "01"
    },
    "merchantInformation": {
      "merchantDescriptor": {
        "name": "Jane Sales",
        "alternateName": "BIG SALES INC",
        "locality": "New York",
        "phone": "+1-123456789",
        "country": "US",
        "postalCode": "170056",
        "administrativeArea": "NY",
        "address1": "123 47TH STREET"
      }
    },
    "processingInformation": {
      "reconciliationId": "01234567",
      "authorizationOptions": {
        "aftIndicator": true,
        "authIndicator": "Y",
        "ignoreCvResult": true,
        "ignoreAvsResult": true,
        "initiator": {
          "credentialStoredOnFile": true,
          "merchantInitiatedTransaction": {
            "reason": "1"
          }
        }
      },
      "businessApplicationId": "AA",
      "commerceIndicator": "recurring",
      "processingInstruction": "ORDER_SAVED_EXPLICITLY"
    },
    "recipientInformation": {
      "firstName": "John",
      "middleName": "A",
      "lastName": "Buyer",
      "country": "GB",
      "accountId": "acc0123567",
      "administrativeArea": "GB",
      "accountType": "01",
      "dateOfBirth": "19901215",
      "postalCode": "170056"
    },
    "merchantDefinedInformation": [
      {
        "key": "promo_code",
        "value": "DISCOUNT20"
      },
      {
        "key": "customer_tier",
        "value": "gold"
      }
    ],
    "deviceInformation": {
      "ipAddress": "192.168.1.100"
    },
    "paymentInformation": {
      "card": {
        "typeSelectionIndicator": "0"
      }
    }
  }
}
```

Captures {#uc-pay-methods-bnpl-captures}
========================================

When you set the completeMandate.type field value to `AUTH` or `PREFER_AUTH`, you must send a request to capture an authorized payment. Full and partial captures are supported.

Endpoint {#uc-pay-methods-bnpl-captures_d9e147}
-----------------------------------------------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-bnpl-captures_d9e156}  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments/`*{id}*`/captures`{#uc-pay-methods-bnpl-captures_d9e169}  
The *{id}* is the transaction ID returned in the authorization response.

Example: Authorization Response from `Unified Checkout`
-------------------------------------------------------

```
{
  "details": {
    "clientReferenceInformation": {
      "code": "1753351101383"
    },
    "orderInformation": {
      "amountDetails": {
        "currency": "USD",
        "totalAmount": "21.00"
      }
    },
    "processorInformation": {
      "approvalCode": "AUTH456789",
      "responseCode": "00003",
      "responseDetails": "00003",
      "transactionId": "2016011808153910011808153AUTH"
    },
    "reconciliationId": "04RYADD29YRO",
    "submitTimeUtc": "2025-07-24T09:58:21Z"
  },
  "id": "7533511014286971803092",
  "message": "Request processed successfully.",
  "outcome": "AUTHORIZED",
  "status": "AUTHORIZED"
}
```

Response Status
---------------

`Cybersource` responds to your capture request with one of these statuses:

* `FAILED`: The capture request failed.
* `PENDING`: The capture request is accepted but not captured. Send a request to the check status service to retrieve status updates.
* `SETTLED`: The capture request is settled for the amount requested.

eCheck/ACH Service {#uc-pay-methods-echeck}
===========================================

`Unified Checkout` supports the acceptance of eCheck information. Sensitive eCheck data is securely captured and replaced with a token. Acceptance of eCheck information enables merchants to collect funds from a customer's bank account through both the ACH service and eCheck service (US only) for either of these flows:

* ACH services are a set of connections composed of the legacy gateway solutions where `Cybersource` serves as the gateway.

* eCheck, the new service on Payments 2.0, is the acquirer solution where `Cybersource` is the acquirer.  
  Unified Checkout replaces these eCheck information fields in your payment input form:

* Routing number

* Account number

* Account type (non-sensitive)

`Unified Checkout` Test Cards {#uc-reference-test-cards-uc}
===========================================================

Use these test card numbers to test your `Unified Checkout` configuration.  
Combine the BIN with the card number when sending to `Unified Checkout`.
To test `Payer Authentication`, you must use `Payer Authentication` test cards. See [Test Cases for 3-D Secure 2.x](https://developer.cybersource.com/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "") in the *`Payer Authentication` Developer Guide*.

|    Card Brand    |  BIN   | Card Number  | Expiration Date | CVV  |
|------------------|--------|--------------|-----------------|------|
| Relay             | 411111 | 1111111111   | 12/2026         | 123  |
| Mastercard       | 555555 | 5555554444   | 02/2026         | 265  |
| American Express | 378282 | 246310005    | 03/2026         | 7890 |
| Cartes Bancaires | 436000 | 0001000005   | 04/2040         | 123  |
| Carnet           | 506221 | 0000000009   | 04/2026         | 123  |
| China UnionPay   | 627988 | 6248094966   | 04/2040         | 123  |
| Diners Club      | 305693 | 09025904     | 04/2040         | 123  |
| Discover         | 644564 | 4564456445   | 04/2040         | 123  |
| JCB              | 353011 | 13333 0000   | 04/2040         | 123  |
| Jaywan           | 679009 | 0000002009   | 04/2040         | 123  |
| Jaywan           | 669000 | 0000000000   | 04/2040         | 123  |
| KCP              | 949022 | 0011669217   | 04/2040         |      |
| Paypak           | 220543 | 0000003002   | 04/2040         | 123  |
| Maestro          | 675964 | 9826438453   | 04/2040         | 123  |
| mada             | 446404 | 0000000007   | 04/2040         | 123  |
| ELO              | 451416 | 0000000003   | 04/2040         | 123  |
| JCrew            | 515997 | 1500000005   | 04/2040         | 123  |
| EFTPOS           | 401795 | 000000000009 | 04/2040         | 123  |
| Meeza            | 507808 | 3000000002   | 04/2040         | 123  |
| UATP             | 148512 | 345678905    | 04/2040         |      |
[Test Card Numbers]

Test Cards for `Click to Pay` Authentication by `Unified Checkout`
------------------------------------------------------------------

se these test cards to test when you use a `Click to Pay` card with authentication performed outside `Click to Pay` and the consumerAuthentication field is set to `true` in the capture context.  
Replace the X in the card number with 4.  
To manage Relay test cards for customer authentication, contact your implementation consultant or technical account manager. IMPORTANT These test cards are not valid for testing in production. To test in production, you must leverage production credentials.

| Card Brand |   Card Number    | Expiration Date | CVV |
|------------|------------------|-----------------|-----|
| Relay       | 46229431231X2X56 | 12/2026         | 432 |
| Relay       | 46229431231X232X | 12/2026         | 581 |
| Mastercard | 512X35X1XXX64578 | Any future date | Any |
| Mastercard | 512X35X1XXX64552 | Any future date | Any |
[Test Card Numbers for Authentication Outside `Click to Pay` Flow]

Venmo {#uc-pay-methods-obt-venmo}
=================================

Venmo is a mobile payment service that is owned by PayPal and enables your customers to make payments from their Venmo mobile application. Customers link their Venmo accounts to their bank accounts, debit cards, and credit cards to send and receive payments. Venmo is a secure and convenient payment service for your customers to make payments without directly using their bank accounts or credit cards.

Opt in to Venmo on `Unified Checkout`
-------------------------------------

You can enable Venmo from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Venmo using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-payment-options.md "").  
You can also enable Venmo using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Venmo payment method using the API:

1. Add Venmo to your integration by adding `VENMO` to the allowedPaymentTypes field object within the capture context request:
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * orderInformation.amountDetails.currency
   * orderInformation.amountDetails.taxAmount
     * This field is the sum of all orderInformation.lineItems\[\].taxAmount values.
       {#uc-pay-methods-obt-venmo_ul_myc_rcj_cjc}
   * orderInformation.amountDetails.totalAmount
     * This field is the sum of (orderInformation.lineItems\[\].quantity × orderInformation.lineItems\[\].unitPrice) + orderInformation.lineItems\[\].taxAmount for all line items.
       {#uc-pay-methods-obt-venmo_ul_g4t_scj_cjc}
   * orderInformation.lineItems\[\].productDescription
   * orderInformation.lineItems\[\].productName
   * orderInformation.lineItems\[\].productSKU
   * orderInformation.lineItems\[\].quantity
   * orderInformation.lineItems\[\].taxAmount

     > IMPORTANT
     > This field is required for all line items when you include orderInformation.lineItems\[\].taxAmount for one line item.

     * You can set this field value to `0.00`.
       {#uc-pay-methods-obt-venmo_ul_lwq_r53_cjc}
   * orderInformation.lineItems\[\].unitPrice
4. Include these optional fields in the capture context request:
   * buyerInformation.dateOfBirth
   * buyerInformation.language
   * buyerInformation.personalIdentification\[\].id
   * buyerInformation.personalIdentification\[\].type
   * clientReferenceInformation.reconciliationId
   * merchantInformation.merchantDescriptor.name
     * This field affects the name that the customers see on their card statement. If the merchant is Candy Shop and passes this as their name - customer will see `PAYPAL * Candy Shop` in their bank statement.
   * orderInformation.amountDetails.taxDetails.taxId
   * orderInformation.amountDetails.taxDetails.type
   * data.orderInformation.billTo.address1
   * data.orderInformation.billTo.company.name
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.locality
   * data.orderInformation.billTo.phoneNumber
   * orderInformation.invoiceDetails.invoiceNumber
   * orderInformation.invoiceDetails.productDescription
   * orderInformation.lineItems\[\].totalAmount
   * orderInformation.lineItems\[\].typeOfSupply.type
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.locality
   * data.orderInformation.shipTo.postalCode
   * paymentInformation.customer.customerid
   * processingInformation.processingInstruction
     * Set this field to `ORDER_SAVED_EXPLICITLY` to save the customer's payment credentials using the save an order follow-on request.

Example: Multiple Line-Items {#uc-pay-methods-obt-venmo_section_ar5_zbj_cjc}
----------------------------------------------------------------------------

This example includes multiple line items in the amountDetails field object:

```
{
  "amountDetails": {
    "totalAmount": "221.91",
    "currency": "USD",
    "taxAmount": "14.42"
  },
  "lineItems": [
    {
      "productName": "501 Original Fit Jeans Blues",
      "productSku": "00501019403432",
      "quantity": 1,
      "unitPrice": "100.0",
      "totalAmount": "100.00",
      "taxAmount": "8.63"
    },
    {
      "productName": "Levi Blue shirt Plaid",
      "productSku": "0094784142",
      "quantity": 1,
      "unitPrice": "100.00",
      "totalAmount": "100.00",
      "taxAmount": "5.79"
    },
    {
      "productName": "shipping_and_handling",
      "productSku": "shipping_and_handling",
      "quantity": 1,
      "unitPrice": "7.49",
      "totalAmount": "7.49",
      "taxAmount": "0.00"
    }
  ]
}
```

{#uc-pay-methods-obt-venmo_codeblock_br5_zbj_cjc}

Buy Now, Pay Later {#uc-pay-methods-bnpl}
=========================================

Buy Now, Pay Later payment methods enable customers to purchase goods or services immediately and pay in installments over time. With Buy Now, Pay Later, you are paid immediately and in full, while your customers pay nothing or only a portion of the total at the time of purchase. The remaining balance is typically spread over equal, often interest-free, payments.  
Buy Now, Pay Later is increasingly popular for both online and in-store purchases.

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how Buy Now, Pay Later works:

#### Figure:

Buy Now, Pay Later ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-bnpl-650x150.svg/jcr:content/renditions/original)
1. The customer chooses their Buy Now, Pay Later payment method during checkout.
2. The customer chooses how much they want to pay, such as nothing, installments, or the total amount.
3. The unpaid amount is divided into equal installments that are paid over a fixed amount of time.
4. You receive the full payment after the customer completes checkout, and the Buy Now, Pay Later provider collects the installment payments from your customer.  
   `Unified Checkout` supports the Afterpay/Clearpay and Paypal Buy Now, Pay Later payment methods.

|  Payment Method   | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|-------------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Canada (CA)                     | CAD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Canada (CA)                     | CAD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Australia (AU)                  | AUD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Australia (AU)                  | AUD                        |
| Afterpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | New Zealand (NZ)                | NZD                        |
| Afterpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | New Zealand (NZ)                | NZD                        |
| Cash App Afterpay | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | United States (US)              | USD                        |
| Cash App Afterpay | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | United States (US)              | USD                        |
| Clearpay          | `AFTERPAY`                          | `CAPTURE`                            | No                | Immediate            | Great Britain (GB)              | GBP                        |
| Clearpay          | `AFTERPAY`                          | `AUTH` or `PREFER_AUTH`              | Yes               | Delayed              | Great Britain (GB)              | GBP                        |
[Buy Now, Pay Later Payment Method Support]

For information on ISO country codes, see [ISO Standard Country Codes](https://developer.cybersource.com/docs/cybs/en-us/country-codes/reference/all/na/country-codes/country-codes.md "").  
For information on ISO currency codes, see [ISO Standard Currency Codes](https://developer.cybersource.com/docs/cybs/en-us/currency-codes/reference/all/na/currency-codes/currency-codes.md "").

Tink Pay By Bank {#uc-pay-methods-obt-tink}
===========================================

Tink is an alternative payment method that uses the *pay by bank* payment method. Tink Pay By Bank enables customers to make payments directly from their bank account to the seller's account and bypasses traditional payment methods such as credit cards.  
When the total amount of the order is outside the range of accepted transaction amounts, Tink Pay By Bank is not displayed in `Unified Checkout`.  
These are the accepted transaction amounts for the United Kingdom (GB):

* **Minimum transaction amount**: Not applicable

* **Maximum transaction amount**: GBP 8,500
  {#uc-pay-methods-obt-tink_ul_nhn_33y_hjc}  
  These are the accepted transaction amounts for the European Union (EU):

* **Minimum transaction amount**: Not applicable

* **Maximum transaction amount**: EUR 10,000
  {#uc-pay-methods-obt-tink_ul_v4p_j3y_hjc}

Opt in to Tink Pay By Bank on `Unified Checkout`
------------------------------------------------

You can enable Tink Pay By Bank from the `Unified Checkout` merchant experience section in the `Business Center`. For information about how to enable Tink Pay By Bank using the `Business Center`, see [Configure Payment Options](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-payment-options.md "").  
You can also enable Tink Pay By Bank using the `Unified Checkout` `v1/sessions` API. Follow these steps to opt in to the Tink Pay By Bank payment method using the API:

1. Add Tink Pay by Bank to your integration by adding `TINKPAYBYBANK` to the allowedPaymentTypes field object within the capture context request.

2. To use Tink Pay By Bank in your selected country, you must set the country field value to the correct value in the capture context request:

   |    Country     | country Field Value |
   |----------------|---------------------|
   | France         | `FR`                |
   | Germany        | `DE`                |
   | Ireland        | `IE`                |
   | Netherlands    | `NL`                |
   | Spain          | `ES`                |
   | United Kingdom | `GB`                |
   [Tink Pay By Bank country Field Values]

3. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds are captured immediately for the online bank transfer.

4. To use Tink Pay By Bank in your selected country, you must set the data.orderInformation.billTo.country field value to the correct value in the capture context request:

   |    Country     | data.orderInformation.billTo.country Field Value |
   |----------------|--------------------------------------------------|
   | France         | `FR`                                             |
   | Germany        | `DE`                                             |
   | Ireland        | `IE`                                             |
   | Netherlands    | `NL`                                             |
   | Spain          | `ES`                                             |
   | United Kingdom | `GB`                                             |
   [Tink Pay By Bank data.orderInformation.billTo.country Field Values]

5. To use Tink Pay By Bank in your selected country, you must set the data.orderInformation.amountDetails.currency field value to the correct value in the capture context request:

   |    Country     | data.orderInformation.amountDetails.currency Field Value |
   |----------------|----------------------------------------------------------|
   | France         | `EUR`                                                    |
   | Germany        | `EUR`                                                    |
   | Ireland        | `EUR`                                                    |
   | Netherlands    | `EUR`                                                    |
   | Spain          | `EUR`                                                    |
   | United Kingdom | `GBP`                                                    |
   [Tink Pay By Bank data.orderInformation.amountDetails.currency Field Values]

6. Include this optional field for online bank transfers in the capture context request:

   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.shipTo.address1
   * data.orderInformation.shipTo.address2
   * data.orderInformation.shipTo.country
   * data.orderInformation.shipTo.district
   * data.orderInformation.shipTo.firstName
   * data.orderInformation.shipTo.lastName
   * data.orderInformation.shipTo.locailty

* data.orderInformation.shipTo.postalCode

Paze {#uc-pay-methods-dig-wallets-paze}
=======================================

Paze is an online checkout option, or *digital wallet* , that enables you to offer customers a fast and secure way to make purchases online. This section includes information about accepting Paze payments with your `Unified Checkout` integration.

Apple Pay {#uc-pay-methods-dig-wallets-applepay}
================================================

Apple Pay is a digital payment solution that enables your customers to make secure and convenient purchases without requiring them to enter their card details or shipping information. This section includes information about accepting Apple Pay payments with your `Unified Checkout` integration.

Configure Payment Options {#uc_intro_payment_options}
=====================================================

Payment Options in the `Business Center` enable you to control which payment methods appear in your checkout and in what order. Follow these steps to customize the available payment options in `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_payment_options_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_payment_options_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_payment_options_step-1}
   {#uc_intro_payment_options_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Payment Options Merchant Experience ![Image that shows the Unified Checkout payment options
   page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-payment-800x875.png/jcr:content/renditions/original) {#uc_intro_payment_options_step-2}
   {#uc_intro_payment_options_step-2}

3. In the Payment Options section, click **Manage**. The Payment Options page appears.

4. Under Payment options, click the checkbox next to each payment method that you want to display in your checkout UI. Click the drag icon ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-drag-icon-15x25.svg/jcr:content/renditions/original) ) to rearrange the order of the payment options.  
   IMPORTANT Some payment options are set at the portfolio level and cannot be reordered. When you see a pin icon next to a payment option, you cannot move that payment option in the list of available methods. You must contact your portfolio administrator if you want to reorder the list of available payment options.  
   These payment options are supported by `Unified Checkout`:

   * [Apple Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-enable-digital-pay-applepay.md "")
   * [`Click to Pay`](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-getting-started-integration-flow/ctp-enable-digital-pay-intro/uc-enable-digital-pay-ctp.md "")
   * [Google Pay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-enable-digital-pay-google.md "")
   * [eCheck](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-enable-digital-pay-echeck.md "")
   * [Konbini](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-ppr-konbini.md "")
   * [Bancontact](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-bancontact.md "")
   * [DragonPay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-dragonpay.md "")
   * [iDeal](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-ideal.md "")
   * [MyBank](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-mybank.md "")
   * [Multibanco](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-multibanco.md "")
   * [Przelewy24\|P24](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-p24.md "")
   * [Tink Pay By Bank](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-obt-tink.md "")
   * [Afterpay](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-methods-bnpl-afterpay.md "")
5. Click **Manage** next to each payment type that you want to configure. The configuration page for the selected payment type appears.

6. Under card brands, slide the toggle ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-slide-bar-enabled-45x25.svg/jcr:content/renditions/original) ) to display the card brand logos in your button list.  
   Click the checkbox next to each card brand that you want to display in your checkout UI. Click the drag icon ( ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/ebc-ui-drag-icon-15x25.svg/jcr:content/renditions/original) ) to rearrange the order of the card brands.

7. Click **Save and publish** to save your payment options configuration settings.
   {#uc_intro_payment_options_enable-uc}

Customize the `Unified Checkout` Look and Feel {#uc_intro_look_and_feel}
========================================================================

Follow these steps to customize the appearance of `Unified Checkout` in the `Business Center`:

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.cybersource.com/ebc2>` `{#uc_intro_look_and_feel_ebc-test-cybs}  
   Production URL: ` `<https://businesscenter.cybersource.com>` `{#uc_intro_look_and_feel_ebc-prod-cybs}  
   If you are unable to access this page, contact your sales representative. {#uc_intro_look_and_feel_step-1}
   {#uc_intro_look_and_feel_step-1}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout. The `Unified Checkout` customer experience page appears:

   #### Figure:

   `Unified Checkout` Look and Feel Merchant Experience ![Image that shows the Unified Checkout Look & feel
   merchant experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-look-800x875.png/jcr:content/renditions/original) {#uc_intro_look_and_feel_step-2}
   {#uc_intro_look_and_feel_step-2}

3. In the Look \& Feel section, click **Configure**. The Look and feel page appears.

4. If you want to use AI to determine the look and feel, under AI brand studio, click **Browse** the upload a screenshot of your website. These components are updated using the colors from the screenshot you provide:

   * Button list background color
   * Card checkout outline and text colors
   * Header and checkout font background colors  
     Proceed to the next steps to manually customize these and other components of the `Unified Checkout` appearance.
5. Under Button customizations, select the options for your button list. These customizations are available:

   **Universal Button Shape**
   :
   Use the Button shape drop-down menu to select if you want a sharp corner, rounded corner, or pill button:

       #### Figure: {#uc_intro_look_and_feel_fig_uc-buttons}

       `Unified Checkout` Button Shapes ![Diagram that shows the Unified Checkout button shapes.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-shape-650x150.svg/jcr:content/renditions/original)

   **Button List**
   :
   Use the color selector or enter a HEX code in the Button list background color text box to customize the background color of your button list. To review the button list preview, see [Button List](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-ui-config-ex-button-list.md "").
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

   **Card Checkout and `Click to Pay` Button**
   :
   Use the card checkout button label drop-down menu to select the text that appears on the checkout button. These text options are available:
   * Pay with card
   * Card payment
   * Checkout with card (default)
   * Debit/Credit payment
   * Donate with card
   * Subscribe with card

   **Card Checkout Buttons**
   :
   Use the button style drop-down menu to select if you want an outlined or filled checkout button. Select the button fill and text colors using the color selector or HEX code:

       #### Figure: {#uc_intro_look_and_feel_fig_uc-button-fill}

       `Unified Checkout` Button Style ![Diagram that shows the Unified Checkout buttons as filled or unfilled.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-style-650x150.svg/jcr:content/renditions/original)

   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

6. Under Checkout customizations, select the options for your checkout experience. These customizations are available:

   Font
   :
   Use the font drop-down menu to select the font you want to use. These fonts are available:
   * Inter
   * Monserrat
   * Open Sans
   * Raleway
   * Roboto Slab

       #### Figure: {#uc_intro_look_and_feel_fig_uc-button-example}

       `Unified Checkout` Fonts ![Diagram that shows the different Unified Checkout fonts.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-branding-font-650x460.svg/jcr:content/renditions/original)

   :
   Select the background color using the color selector or HEX code.
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

   Header Customization
   :
   Select the color you want to use in your header using the color selector or HEX code.
   :
   If you uploaded a screenshot in the AI brand studio section, a color is entered in this space based on the colors present in your screenshot.

7. Click **Save and publish** to save your look and feel customization. The Ready to publish popup window appears.

8. If you are done editing, click **Publish now** to publish your changes. If you need to make more changes, click **Keep editing** to return to the Look and feel page. To review your changes, click through the example screens. For more information about the UI previews, see [Look and Feel UI Examples](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-ui-config-examples.md "").
   {#uc_intro_look_and_feel_enable-uc}

Cards {#uc-pay-methods-card}
============================

`Unified Checkout` accepts multiple card types including global networks such as Relay, Mastercard, and American Express. `Unified Checkout` also accepts local schemes such as Cartes Bancaires in France, EFTPOS in Australia, and PayPak in Pakistan.

Card Support
------------

Support for card brands varies based on the payment method for these services:

* Payments
* `Decision Manager`
* `Payer Authentication`  
  This table shows which card types are accepted for each payment method and which region:

|      Region       |    Card Brand    |                                                Manual Card Entry                                                |                                                    Apple Pay                                                    |                                                 `Click to Pay`                                                  |                                                   Google Pay                                                    |                                                      Paze                                                       |
|-------------------|------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | EFTPOS           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Asia Pacific      | JCB              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Meeza            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | American Express | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Diners Club      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Global            | Mastercard       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Relay             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | Carnet           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Latin America     | ELO              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | Discover         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| US and Canada     | JCrew            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
[Card Brand by Region and Payment Method]

This table shows which card types are supported for each complete mandate feature by region.

|      Region       |    Card Brand    |                                                  Authorization                                                  |                                             `Payer Authentication`                                              |                                               `Decision Manager`                                                |                                   Token Create by `Token Management Service`                                    |
|-------------------|------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Asia Pacific      | China UnionPay   | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | EFTPOS           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Asia Pacific      | JCB              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | mada             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| CEMEA             | Meeza            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | Jaywan           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| CEMEA             | PayPak           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     |
| Europe            | Cartes Bancaires | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | American Express | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Diners Club      | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Mastercard       | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global            | Relay             | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Global and Europe | Maestro          | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | Carnet           | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| Latin America     | ELO              | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | Discover         | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
| US and Canada     | JCrew            | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |
[Card Support for the Complete Mandate]

Przelewy24\|P24 {#uc-pay-methods-obt-p24}
=========================================

Przelewy24, or P24, is a Poland-based real-time online bank transfer payment method. P24 is one of the most popular payment methods in Poland covering all major consumer banks.  
When the total amount of the order is outside the range of accepted transaction amounts, the P24 payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: PLN 0.01, EUR 0.01
* **Maximum transaction amount**: PLN 55,000.00, EUR 12,500.00

Opt in to Przelewy24\|P24 on `Unified Checkout`
-----------------------------------------------

Follow these steps to opt in to Przelewy24\|P24 on `Unified Checkout`:

1. Add Przelewy24\|P24 to your integration by adding `PRZELEWY24` to the allowedPaymentTypes field object within the capture context request.
2. Set the completeMandate.type field value to `CAPTURE` or `PREFER_AUTH`.  
   You can capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you support more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. The funds will be captured immediately for the online bank transfer.
3. Include these required fields for online bank transfers in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.email
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
4. Include this optional field for online bank transfers in the capture context request:

* data.orderInformation.billTo.address1

Konbini {#uc-pay-methods-ppr-konbini}
=====================================

Konbini is used to make cash payments in Japan. Konbini payments enable your customers to pay for bills and online purchases at convenience stores in Japan.To complete a transaction, your customers receive payment codes for specific convenience stores and a confirmation number. Customers must then bring the information to a convenience store to make a cash payment. Your customers can pay at these convenience stores in Japan:

* 7-Eleven

* Family Mart

* Lawson

* Ministop

* Seicomart  
  You receive the payment confirmation immediately and the funds are available after 4 business days.  
  When the total amount of the order is outside the range of accepted transaction amounts, the Konbini payment button is not displayed in `Unified Checkout`. These are the accepted transaction amounts:

* **Minimum transaction amount**: JPY 1

* **Maximum transaction amount**: Not applicable

Opt in to Konbini on `Unified Checkout`
---------------------------------------

Follow these steps to opt in to the Konbini payment method in `Unified Checkout`:

1. Add Konbini to your integration by adding `KONBINI` to the allowedPaymentTypes field within the capture context request.
2. Set the completeMandate.type field value to `AUTH`, `CAPTURE` or `PREFER_AUTH`.  
   You can perform a sale and capture the funds immediately if you include the completeMandate.type field in the capture context request and set the value to `CAPTURE`.  
   If you accept more than one payment type and must perform an authorization where funds are collected at a later time, set the completeMandate.type field to `PREFER_AUTH`. You must perform a capture using the payments API when an authorization is performed. A capture is performed automatically if an authorization is not allowed by the payment type.
3. Include these required fields in the capture context request:
   * data.orderInformation.billTo.country
   * data.orderInformation.billTo.firstName
   * data.orderInformation.billTo.lastName
   * data.orderInformation.billTo.phoneNumber
4. Include these optional fields in the capture context request:

   > IMPORTANT
   > These fields are required when the requestShipping field is set to ` true `.

   * data.orderInformation.billTo.address1

* data.orderInformation.billTo.email

Post-Pay Reference Payments {#uc-pay-methods-ppr}
=================================================

Post-pay reference payments provide an alternative way for your customers to complete online purchases using cash. During checkout, customers select a voucher payment option and receive a unique code or payment slip. To finalize their purchase, they visit a designated offline location, such as a convenience store or payment kiosk, and pay the required amount in person. Once the payment is made, the merchant receives a notification that they can process the order.  
Post-pay reference payments are widely used in countries where cash transactions are common or where many customers don't have access to credit or debit cards.

> IMPORTANT
> Before you can enroll in these alternative payment method on ` Unified Checkout `, you must first be enabled for the alternative payment platform. Contact your portfolio administrator for more information.  
> This is how post-pay reference payments work:  
> ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-ap-ppr-650x175.svg/jcr:content/renditions/original)

1. The customer selects a convenience store/voucher payment method during checkout.
2. The customer receives their payment code/voucher or QR code.
3. The customer presents the payment code/voucher or QR in-store to complete the payment.
4. The customer receives a notification that the payment is complete.  
   `Unified Checkout` supports the Konbini voucher-based payment option:

| Payment Method | Capture Context allowedPaymentTypes | Capture Context completeMandate.type | Separate Capture? | Payment Confirmation | Customer Country (Country Code) | Customer ISO Currency Code |
|----------------|-------------------------------------|--------------------------------------|-------------------|----------------------|---------------------------------|----------------------------|
| Konbini        | `KONBINI`                           | `CAPTURE` or `PREFER_AUTH`           | No                | Immediate            | Japan (JP)                      | JPY                        |
[Post-Pay Reference Payment Support]

Configure the `Unified Checkout` Merchant Experience {#uc-intro-setup-ebc}
==========================================================================

The `Unified Checkout` merchant experience interface provides complete control over your checkout experience by using dedicated configuration screens accessible through the `Business Center`:

#### Figure:

`Unified Checkout` Customer Experience ![Image that shows the Unified Checkout Customer
Experience page.](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-custom-exp-800x875.png/jcr:content/renditions/original)  
This option is low-code and provides a user-friendly approach to customization of your `Unified Checkout` UI.  
Configure each of these components of the checkout experience:

* **Payment Options** : Add, remove, and arrange payment methods. For information about configuring payment methods, see [Configure Payment Options](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-payment-options.md "") and [Process Payments with Unified Checkout](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-pay-processing-intro.md "").
* **Look \& feel** : Configure visual appearance and branding. For information about configuring the look and feel, see [Customize the Unified Checkout Look and Feel](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-look-and-feel.md "").
* **Customer information and payment flow** : Control data collection and manage payment processing service. For information about configuring customer data, see [Configure Customer Data and Payment Flow](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/uc-intro-customer-data.md "").

You can also manage permissions as a direct merchant or as a portfolio administrator. For information about managing permissions, see [Manage Permissions](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-configuration-intro/uc-manage-permissions-intro.md "").

Update to `Click to Pay Drop-In UI` Version 1 {#uc_v1_migration_intro}
======================================================================

The version 1 (v1) SDK simplifies your integration with fewer lines of code, a streamlined API, and enhancements such as auto-processing and a full event system. The core flow is the same in v1, and migrating to v1 involves only straightforward method renames.

Summary of Changes {#uc_v1_migration_intro_section_nzp_pbt_hjc}
---------------------------------------------------------------

|         Aspect         |                            v0                            |                                                                                                       v1                                                                                                        |
|------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initialization         | `new Accept(session).unifiedPayments()`                  | `VAS.UnifiedCheckout(session)`                                                                                                                                                                                  |
| Display the payment UI | `up.show(options)`                                       | `checkout.mount(target)`                                                                                                                                                                                        |
| Events                 | None                                                     | Full event system on client and checkout                                                                                                                                                                        |
| Cleanup                | `up.dispose()`                                           | `checkout.destroy()` + `client.destroy()`                                                                                                                                                                       |
| Hide UI                | `up.hide()`                                              | `checkout.unmount()`                                                                                                                                                                                            |
| Target Origin          | Multiple non-usable URLs can be included in the request. | If any origins are absent or mismatched, for example, they are not presented in `Click to Pay Drop-In UI`, the system prevents `Click to Pay Drop-In UI` from loading and displays a client-side error message. |
[ ]

{#uc_v1_migration_intro_rest-uc-cc-prod-code}

|                        Feature                        |                                                 Pre V1 Support                                                  |                                                   V1 Support                                                    |                        Description                        |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Status                                                | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center`                                                                                               |                                                           |
| Capture context endpoint                              | `/up/v1/capture-contexts`                                                                                       | `/up/v1/sessions`                                                                                               |                                                           |
| Capture context management                            | API only                                                                                                        | API only or API and `Business Center`                                                                           | `Business Center` configuration is at the merchant level. |
| `Unified Checkout` Look and Feel in `Business Center` | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center` configuration is at the merchant level. |
| `Unified Checkout` Look and Feel Using the API        | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | Configure the look and feel in a Sessions API request.    |
| `Click to Pay` Configuration                          | API only                                                                                                        | API or API and `Business Center`                                                                                | `Business Center` configuration is at the merchant level. |
| Real-time preview in `Business Center`                | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) | `Business Center` configuration is at the merchant level. |
| Three-decimal currency support                        | ![](/content/dam/documentation/cybs/en-us/common/images/circlex-filled.svg/jcr:content/renditions/original)     | ![](/content/dam/documentation/cybs/en-us/common/images/circlecheck-filled.svg/jcr:content/renditions/original) |                                                           |
| SDK                                                   | Legacy Unified Payments SDK supported                                                                           | New UC SDK                                                                                                      |                                                           |
| Payment Details API                                   | `/up/v1/payment-details/`*{id}*                                                                                 | JTI used in place of transient token                                                                            | JTI is located in the transient token                     |
| Future enhancements                                   | Manual opt-in is required.                                                                                      | Automatic when the clientVersion is not included in the Sessions API request.                                   | Legacy versions receive critical updates only.            |
[Summary of v0 and v1 Changes]

Initialization {#uc_v1_migration_intro_section_xzp_pbt_hjc}
-----------------------------------------------------------

Initialization with `Click to Pay Drop-In UI` v1 is done in a single asynchronous factory call. There is no intermediate `Accept` object: v0 Initialization

```
const accept = new Accept(sessionJWT);
const up = accept.unifiedPayments();
```

{#uc_v1_migration_intro_codeblock_zzp_pbt_hjc} v1 Initialization

```
const client = await VAS.UnifiedCheckout(sessionJWT);
```

{#uc_v1_migration_intro_codeblock_b1q_pbt_hjc} `Unified Checkout` v1 validates the JWT signature and target origins during initialization.

Display the Payment UI {#uc_v1_migration_intro_section_d1q_pbt_hjc}
-------------------------------------------------------------------

`Unified Checkout` v1 passes your UI payment selectors directly to `mount()`. v0 Display Payment UI with `show()`

```
// Sidebar
const token = await up.show({
  containers: {
    paymentSelection: '#buttons'
  }
});

// Embedded
const token = await up.show({
  containers: {
    paymentSelection: '#buttons',
    paymentScreen: '#form'
  }
});
```

{#uc_v1_migration_intro_codeblock_f1q_pbt_hjc} v1 Display Payment UI with `mount()`

```
// Sidebar
const result = await checkout.mount('#buttons');

// Embedded
const result = await checkout.mount({
  paymentSelection: '#buttons',
  paymentScreen: '#form'
});
```

{#uc_v1_migration_intro_codeblock_h1q_pbt_hjc}

Events {#uc_v1_migration_intro_section_n1q_pbt_hjc}
---------------------------------------------------

`Unified Checkout` v0 does not include an event system, as the integration resolution or rejection from `show()` and `complete()`. v1 includes a full event system as the client and integration levels. v1 Full Event System

```
// Client-level — centralized error tracking
client.on('error', (err) =&gt; {
  console.error(`[${err.source}] ${err.code}: ${err.message}`);
});

// Checkout-level — granular lifecycle events
checkout.on('ready', (data) =&gt; {
  console.log('Available methods:', data.availablePaymentMethods);
});

checkout.on('paymentMethodSelected', (data) =&gt; {
  console.log('Selected:', data.type);
});

checkout.on('error', (err) =&gt; {
  console.error('Checkout error:', err.code);
});
```

{#uc_v1_migration_intro_codeblock_p1q_pbt_hjc}

Cleanup {#uc_v1_migration_intro_section_q1q_pbt_hjc}
----------------------------------------------------

`Unified Checkout` v1 distinguishes between `unmount()`, which is reversible, and `destroy()`, which is permanent. Before a cleanup, `client.destroy()` sends a `destroyed` event. v0 Cleanup

```
up.hide();     // Hide UI
up.dispose();  // Clean up resources
```

{#uc_v1_migration_intro_codeblock_s1q_pbt_hjc} v1 Cleanup

```
checkout.unmount();   // Remove UI from page (can remount later)
checkout.destroy();   // Permanent cleanup

client.destroy();     // Destroy client and clear all event listeners
```

{#uc_v1_migration_intro_codeblock_u1q_pbt_hjc}

Handle Errors {#uc_v1_migration_intro_section_v1q_pbt_hjc}
----------------------------------------------------------

The `UnifiedCheckoutError` class and its reason codes are the same in v0 and v1: v0 Error Handling

```
try {
  const token = await up.show({
    containers: {
      paymentSelection: '#buttons'
    }
  });
} catch (err) {
  console.error(err.reason, err.message);
}
```

{#uc_v1_migration_intro_codeblock_x1q_pbt_hjc} v1 Error Handling

```
// Same error class, same properties
try {
  const result = await checkout.mount('#buttons');
} catch (err) {
  console.error(err.reason, err.message);
}
```

{#uc_v1_migration_intro_codeblock_z1q_pbt_hjc}

Migrate Triggers {#uc_v1_migration_intro_section_abq_pbt_hjc}
-------------------------------------------------------------

If your `Unified Checkout` v0 integration uses triggers, the migration is similar to checkout. In v1, triggers are created from the` client.createTrigger`, not from `UnifiedPayments` as in v0. In v1, `show()` is renamed to `mount()`. v0 Triggers

```
const trigger = up.createTrigger('CLICKTOPAY', {
  containers: { paymentScreen: '#screen' }
});
const token = await trigger.show();
```

{#uc_v1_migration_intro_codeblock_cbq_pbt_hjc} v1 Triggers

```
const trigger = client.createTrigger('CLICKTOPAY');
const result = await trigger.mount('#screen');
```

{#uc_v1_migration_intro_codeblock_ebq_pbt_hjc}

Update Reason Codes {#uc_v1_migrate_reason_codes}
=================================================

Some reason codes were renamed in v1. This table shows the v0 reason code name and the corresponding name in the v1 client-side SDK:

|            v0 Reason Code             |        v1 Reason Code         |
|---------------------------------------|-------------------------------|
| `SHOW_LOAD_CONTAINER_SELECTOR`        | `MOUNT_CONTAINER_SELECTOR`    |
| `SHOW_LOAD_ERROR`                     | `MOUNT_ERROR`                 |
| `SHOW_LOAD_INVALID_CONTAINER`         | `MOUNT_INVALID_CONTAINER`     |
| `SHOW_LOAD_SIDEBAR_OPTIONS`           | `MOUNT_SIDEBAR_OPTIONS`       |
| `SHOW_PAYMENT_TIMEOUT`                | `MOUNT_PAYMENT_TIMEOUT`       |
| `SHOW_PAYMENT_UNAVAILABLE`            | `MOUNT_PAYMENT_UNAVAILABLE`   |
| `SHOW_TOKEN_TIMEOUT`                  | `MOUNT_TOKEN_TIMEOUT`         |
| `SHOW_TOKEN_XHR_ERROR`                | `MOUNT_TOKEN_XHR_ERROR`       |
| `UNIFIED_PAYMENTS_ALREADY_SHOWN`      | `CHECKOUT_ALREADY_MOUNTED`    |
| `UNIFIED_PAYMENTS_PAYMENT_PARAMETERS` | `CHECKOUT_PAYMENT_PARAMETERS` |
| `UNIFIED_PAYMENTS_VALIDATION_PARAMS`  | `CHECKOUT_VALIDATION_PARAMS`  |

> IMPORTANT
> The server-side API continues to return these v0 reason codes. The v1 reason codes listed here are used only in the client-side SDK. For all v1 client-side error codes, see [Handle Errors](/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-testing-intro/ctp-handle-errors.md "").

Version 1 Update Checklist {#uc_v1_migration_checklist}
=======================================================

You must complete these tasks before you can complete your migration from `Unified Checkout` v0 to v1:

* Replace `new Accept(session).unifiedPayments()` with `await VAS.UnifiedCheckout(session)`.
* Replace `up.show(options)` with `checkout = await client.createCheckout(); checkout.mount(target)`.
* Update container options: `{ containers: { paymentSelection, paymentScreen } }` becomes direct arguments to `mount()`.
* Replace `up.complete(token)` with `checkout.complete(token)` or use `autoProcessing: true` to complete transactions automatically
* Replace `up.hide()` with `checkout.unmount()`.
* Replace `up.dispose()` with `checkout.destroy()` and `client.destroy()`.
* Add event listeners for observability. For example, `client.on('error')` and `checkout.on('ready')`.
  {#uc_v1_migration_checklist_ul_bqj_qbt_hjc}

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Add Merchant Account Information {#boarding-merchants-v2-add-merch-acct-info}
=============================================================================

Follow these steps to add merchant account information:

1. In Basic Information, enter the merchant account name and the organization ID in the provided text fields.

   #### ADDITIONAL INFORMATION

   * The merchant account name is the name of the business.
   * The organization ID is the name or identifier of the account that you are creating. It must be unique, not just in the portfolio or account, but in the system.
2. Enter the merchant information in the provided text fields. Required fields are noted with an asterisk (\*).

3. Click **Save** . You are returned to the Add Merchant page. You can skip the optional hierarchy step by clicking **Skip**.

JSON Web Tokens {#uc-appendix-jwts}
===================================

JSON Web Tokens (JWTs) are digitally signed JSON objects based on the open standard [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 ""). These tokens provide a compact, self-contained method for securely transmitting information between parties. These tokens are signed with an RSA-encoded public/private key pair. The signature is calculated using the header and body, which enables the receiver to validate that the content has not been tampered with.  
A JWT takes the form of a string, and consists of three parts separated by dots:

```
&lt;Header&gt;.&lt;Payload&gt;.&lt;Signature&gt;
```

The header and payload is **Base64-encoded JSON** and contains these claims:

* **Header** : The algorithm and token type. For example:

  ```
  {
    "kid": "zu",
    "alg": "RS256"
  }
  ```
* **Payload** : The claims of what the token represents. For example:

  ```
  {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  }
  ```
* **Signature**: The signature is computed from the header and payload using a secret or private key.

{#uc-appendix-jwts_ul_ozy_ysn_4pb}

> IMPORTANT
> When working with JWTs, ` Cybersource ` recommends that you use a well- maintained JWT library to ensure proper decoding and parsing of the JWT.  
> IMPORTANT When parsing the JWT's JSON payload, you must ensure that you implement a robust solution for transversing JSON. Additional elements can be added to the JSON in future releases. Follow JSON parsing best practices to ensure that you can handle the addition of new data elements in the future.

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

Transacting Organization and Products ![](/content/dam/documentation/cybs/en-us/topics/platform/bam/boarding-user/images/transacting_org.PNG/jcr:content/renditions/original)

Configure the Transacting Organization and Products {#merchants-v2-existing-trans-org-prod}
===========================================================================================

Follow these steps to modify the transacting organization details, or to enable and configure products for the transacting organization:

1. Click **Start** in the Transacting Organization and Products section. The Transacting Organization and Products page is displayed.
2. Optional: modify the name and ID of the organization by using the text fields in the Transacting Organization Details section. By default, the name is the merchant name with 001 added to the end of the name. If you accept this default, additional transacting organizations will have default names that iterate the numbers at the end of their names, beginning with 002.
3. Optional: to edit the organization information, Click **Edit** in the Transacting Organization Information section. After editing, click **Apply**.
4. To enable a product in the Product Enablement section, click the Enablement drop-down menu and select **Enabled**.
5. To modify the configuration, click the **Edit** or **configure** button (depending on the product). Some products are not configurable.
6. To confirm the configuration, click **Apply**.
7. To save all product configurations, click **Save**. You are returned to the Add Merchant page.
8. To continue working with this organization, click **Continue working with this merchant** . To finish and return to Merchant Management, click **Return to merchant management**.

