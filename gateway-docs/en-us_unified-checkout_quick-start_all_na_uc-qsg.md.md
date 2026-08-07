`Unified Checkout` Implementation Quick Start Guide {#uc-qsg-about-guide}
=========================================================================

This quick start guide provides essential information and guidance for integrating `Unified Checkout` into your e-commerce system. The guide is written for merchants who want to enable `Unified Checkout` so that they can accept payments on their e-commerce page.  
For more detailed information, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

Recent Revisions to This Document {#uc-qsg-doc-revs}
====================================================

Version 25.06.01
:
Initial release of the guide.
{#uc-qsg-doc-revs_dl_uxm_dhf_gfc}

Introduction to `Unified Checkout` {#uc-qsg-intro}
==================================================

`Unified Checkout` is a powerful and flexible payment solution that simplifies the integration process and enhances the customer checkout experience. This guide will help you get up and running with `Unified Checkout`.

Key Features {#uc-qsg-intro_section_tkt_rgg_gfc}
------------------------------------------------

* Seamless integration with your existing e-commerce platform.
* Support for multiple payment methods.
* Customizable checkout flow.
* Enhanced security features.
* Responsive design for mobile and desktop.
  {#uc-qsg-intro_ul_ukt_rgg_gfc}

Benefits {#uc-qsg-intro_section_vkt_rgg_gfc}
--------------------------------------------

* Simplified integration process.
* Improved conversion rates.
* Reduced cart abandonment.
* Enhanced customer experience.
* Compliance with industry security standards.
  {#uc-qsg-intro_ul_wkt_rgg_gfc}

Additional Information {#uc-qsg-intro_s-more-info}
--------------------------------------------------

For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

Getting Started with `Unified Checkout` {#uc-qsg-gs-intro}
==========================================================

This section outlines the steps to integrate `Unified Checkout` into your e-commerce system.

Integration Prerequisites
-------------------------

Before getting started with the integration process, make sure you have:

* A valid `Payment Gateway` merchant account.
* A secure, PCI-compliant server environment.
* Access to the `Business Center`:
  * Test: `https://businesscentertest.example.com`
  * Production: `https://businesscenter.example.com`
    {#uc-qsg-gs-intro_ul_xsc_xvn_gfc}
* Accounts for the digital wallet payment methods you support.

Integration Steps
-----------------

Integrating `Unified Checkout` into your e-commerce system involves these main steps:

1. Enable `Unified Checkout`.
2. Set up the server-side component.
3. Set up the client-side component.
4. Configure `Unified Checkout`.
5. Test Your integration.

Each request sent to ` Payment Gateway ` requires specific header information. For details on constructing these headers, see the [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").  
Optionally, you can capture the payment response through webhook notifications. For information on webhook notifications for `Unified Checkout`, see the Webhooks Support topic in the [`Unified Checkout` Developer Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-appendix/uc-appendix-webhooks.md "").  
You can use the payment details API to retrieve billing and shipping information captured by `Unified Checkout`. Information that is captured by `Unified Checkout`, including the billing and shipping address, can be retrieved using the payment details API. For information about the Payment Details API, see the Payment Details API section of the [`Unified Checkout` Developer Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md "").

Payment Flow
------------

#### Figure: {#uc-qsg-gs-intro_fig_uc-payment-flow}

`Unified Checkout` Payment Flow  
![Diagram showing the sequence and flow of a Unified Checkout
payment.](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/uc-srvorch-authdm-600x700.svg/jcr:content/renditions/original)

Additional Information {#uc-qsg-gs-intro_section_qxn_csm_gfc}
-------------------------------------------------------------

For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

Step 1: Enable `Unified Checkout` {#uc-qsg-gs-step1}
====================================================

To begin using , you must first ensure that your merchant ID (MID) is configured to use the service and that any payment methods you intend to use are properly set up.  
For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

1. Log in to the `Business Center`:  
   Test URL: ` `<https://businesscentertest.example.com/ebc2>` `{#uc-qsg-gs-step1_d10e39}  
   Production URL: ` `<https://businesscenter.example.com>` `{#uc-qsg-gs-step1_d10e48}  
   If you are unable to access this page, contact your sales representative. {#uc-qsg-gs-step1_d10e29}
   {#uc-qsg-gs-step1_d10e29}

2. In the `Business Center`, go to the left navigation panel and choose Payment Configuration \&gt; Unified Checkout.{#uc-qsg-gs-step1_d10e59}
   {#uc-qsg-gs-step1_d10e59}

3. You can configure various payment methods such as Apple Pay, `Click to Pay`, and Google Pay. Click Set up and follow the instructions for your selected payment methods. When payment methods are enabled, they appear on the payment configuration page.  
   You must configure payment methods you want to use for each transacting MID.

   #### Figure: {#uc-qsg-gs-step1_d10e97}

   ![Manage Unified Checkout Digital Payments Solutions](/content/dam/new-documentation/documentation/en-us/topics/payments-processing/card-processing/unified-checkout/images/pmt-config-unified-payments-digitalpmtsolutions.png/jcr:content/renditions/original) {#uc-qsg-gs-step1_d10e76}

4. Click Manage to edit your existing payment method configurations or enroll in new payment methods as they are released.{#uc-qsg-gs-step1_d10e114}

{#uc-qsg-gs-step1_steps_o34_43h_gfc}

#### AFTER COMPLETING THE TASK

Proceed to [Step 2: Set Up the Server-Side Component](/docs/gateway/en-us/unified-checkout/quick-start/all/na/uc-qsg/uc-qsg-gs-intro/uc-qsg-gs-step2.md "").

Step 2: Set Up the Server-Side Component {#uc-qsg-gs-step2}
===========================================================

To initialize `Unified Checkout` within your webpage, you need to set up the server-side component. This task involves making a server-to-server call to the sessions API to authenticate your merchant credentials and establish how the `Unified Checkout` front-end components will function.  
For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

1. Implement a server-to-server call to the sessions API.

   #### ADDITIONAL INFORMATION

   This call should include parameters that define how `Unified Checkout` performs.

2. Handle the response from the sessions API.

   #### ADDITIONAL INFORMATION

   The response will contain:

   * A transaction-specific public key for securing the transaction in the customer's browser.
   * An authenticated context description package that manages the payment experience on the client side, including available payment options, interface styling, and payment methods.
3. Store and manage the JSON Web Token (JWT) object, referred to as the *capture context*.

   #### ADDITIONAL INFORMATION

   This JWT contains all the functions compiled from the sessions API response.

REST Example: Set Up the Server-Side Component  
In this example, the targetOrigins and the allowedPaymentTypes fields define the target origin and the accepted digital payment methods in your capture context.

```
{
  "clientReferenceInformation": {
    "code": "TAGX001"
  },
  "targetOrigins": [
    "https://www.test.com"
  ],
  "clientVersion": "0.26",
  "allowedCardNetworks": [
    "CARD",
    "MASTERCARD",
    "AMEX"
  ],
  "allowedPaymentTypes": [
    "PANENTRY",
    "CLICKTOPAY",
    "GOOGLEPAY"
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
  "orderInformation": {
    "amountDetails": {
      "totalAmount": "1.01",
      "currency": "USD"
    }
  },
  "completeMandate": {
    "type": "CAPTURE",
    "decisionManager": true
  }
}
```

#### AFTER COMPLETING THE TASK

Proceed to [Step 3: Set Up the Client-Side Component](/docs/gateway/en-us/unified-checkout/quick-start/all/na/uc-qsg/uc-qsg-gs-intro/uc-qsg-gs-step3.md "").

Step 3: Set Up the Client-Side Component {#uc-qsg-gs-step3}
===========================================================

To add the payment interface to your e-commerce site, you need to set up the client-side component using the `Unified Checkout` JavaScript library. This setup involves two primary components:

* The button widget, which lists available payment methods for the customer.
* The payment acceptance page, which captures payment information from the cardholder. This can be integrated with your webpage or added as a sidebar.

For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

1. Load the `Unified Checkout` JavaScript library.

   #### ADDITIONAL INFORMATION

   Include the library in your webpage's HTML.

2. Initialize the accept object with the capture context JWT.

   #### ADDITIONAL INFORMATION

   Use the JWT obtained from the server-side setup in Step 2.

3. Initialize the unified payment object with optional parameters.

   #### ADDITIONAL INFORMATION

   Configure the payment object according to your requirements.

4. Display the button list or payment acceptance page (or both).

   #### ADDITIONAL INFORMATION

   Choose the appropriate display method for your e-commerce site.

#### RESULT

The system will provide a transient token in response to user interactions. You can use the transient token to retrieve the payment information captured by the UI by calling the Payment Details API. For information about the Payment Details API, see the Payment Details API section of the [`Unified Checkout` Developer Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-token-get-pymnt-details.md ""). JavaScript Examples: Set Up the Client-Side Component  
**Setting Up with Full Sidebar**

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
    name="captureContext"
    value="[INSERT captureContext HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sidebar = true;
    const captureContext = document.getElementById("captureContext").value;
const showArgs = { containers: {
paymentSelection: '#buttonPaymentListContainer', 
}
};
    
    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);
    
        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
```

{#uc-qsg-gs-step3_codeblock_sfd_y4m_gfc}  
**Setting Up with Embedded Component**  
The main difference between using an embedded component and the sidebar is that the accept.unifiedPayments object is set to `false`, and the location of the payment screen is passed in the containers argument.

> If you do not specify a location for the payment acceptance page, it is placed in the side bar.

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
    name="captureContext"
    value="[INSERT captureContext HERE]"
  /&gt;
  &lt;script type="text/javascript"&gt;
    const sidebar = false;
    const captureContext = document.getElementById("captureContext").value;
    const showArgs = {
      containers: { paymentSelection: "#buttonPaymentListContainer",
paymentScreen:	'#embeddedPaymentContainer' }
    };
    
    async function launchCheckout() {
      try {
        const accept = await Accept(captureContext);
        const up = await accept.unifiedPayments(sidebar);
        const tt = await up.show(showArgs);
        const completeResponse = await up.complete(tt);
    
        console.log(completeResponse); // merchant logic for handling complete response
      } catch (error) {
        // merchant logic for handling issues
        console.error("something went wrong: " + error);
      }
    }

    // Call the function
    launchCheckout();
  &lt;/script&gt;
&lt;/body&gt;
```

{#uc-qsg-gs-step3_codeblock_sfq_z4m_gfc}

#### AFTER COMPLETING THE TASK

Proceed to [Step 4: Configure Unified Checkout](/docs/gateway/en-us/unified-checkout/quick-start/all/na/uc-qsg/uc-qsg-gs-intro/uc-qsg-gs-step4.md "").

Step 4: Configure Unified Checkout {#uc-qsg-gs-step4}
=====================================================

Proper configuration ensures that your checkout process aligns with your business needs and provides a smooth experience for your customers. This section outlines the steps for configuring the basic `Unified Checkout` settings.  
For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

1. Select and configure the payment methods you support:
   1. Log in to the `Business Center` and navigate to the `Unified Checkout` configuration section.

   2. Select the payment methods you want to use:

      #### ADDITIONAL INFORMATION

      * Credit and debit cards
      * Digital wallets
      * Alternative payment methods

      {#uc-qsg-gs-step4_choices_qy4_nfh_gfc}

      > You must configure the payment methods you want to use for each transacting MID.

   3. Configure the settings for each selected payment method.
      {#uc-qsg-gs-step4_substeps_gv2_pgh_gfc}

#### AFTER COMPLETING THE TASK

Proceed to [Step 5: Test Your Unified Checkout Integration](/docs/gateway/en-us/unified-checkout/quick-start/all/na/uc-qsg/uc-qsg-gs-intro/uc-qsg-gs-step5.md "")

Step 5: Test Your Unified Checkout Integration {#uc-qsg-gs-step5}
=================================================================

After configuring `Unified Checkout`, it's crucial to thoroughly test your integration to ensure it works correctly and provides a smooth checkout experience for your customers. This section outlines the steps to test your `Unified Checkout` integration.  
For detailed information about `Unified Checkout` and the integration process, see the [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "").

1. Set up your test environment:

   1. Log in to the `Business Center` account using your test credentials.
   2. Switch to the test environment if not already in test mode.
   3. Set up a test website or application that integrates `Unified Checkout`.
2. Use test card numbers to simulate different payment scenarios.

   #### ADDITIONAL INFORMATION

   Here are some example test card numbers you can use:

   | Card Type        | Card Number      | Expiration Date | Card Verification Number |
   |:-----------------|:-----------------|:----------------|:-------------------------|
   | American Express | 378282246310005  | 03/2026         | 7890                     |
   | Mastercard       | 5555555555554444 | 02/2026         | 265                      |
   | Relay             | 4111111111111111 | 12/2025         | 123                      |
   [Common Card Test Numbers]

   For more test payment data, see the Test Payment Details section of the [`Unified Checkout` Developer Guide](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-testing-intro/uc-reference-test-cards.md "").

3. Test different payment scenarios:

   #### ADDITIONAL INFORMATION

   * Successful transactions
   * Declined transactions
   * `3-D Secure` authentication, if applicable
   * Different card brands
   * Digital wallet payments, if configured
     {#uc-qsg-gs-step5_ul_yj5_jwm_gfc}
4. Verify the capture context and token handling.

   #### ADDITIONAL INFORMATION

   Ensure that your integration correctly handles the capture context and transient tokens throughout the payment process.

5. Test error handling and edge cases.

   #### ADDITIONAL INFORMATION

   Simulate various error scenarios to ensure your integration gracefully handles and reports errors to the user.

6. Verify webhook notifications, if configured.

   #### ADDITIONAL INFORMATION

   If you set up webhook notifications, ensure that your system correctly receives and processes them for various transaction events.

#### AFTER COMPLETING THE TASK

After completing these testing steps, you should have confidence in your integration. Remember to test in both the test and production environments before going live.

Next Steps {#uc-qsg-next-steps}
===============================

Now that you have successfully set up and tested your `Unified Checkout` integration, here are some next steps to consider:

1. **Move to Production:** Once you're confident in your test results, update your integration to use production API credentials and endpoints.
2. **Monitor Transactions:** Regularly review your transaction data in the `Business Center` to ensure everything is functioning as expected.
3. **Optimize Your Integration:** Analyze your checkout flow and consider ways to improve the user experience based on customer feedback and conversion rates.
4. **Stay Updated:** Keep an eye on the documentation and release notes for any updates or new features related to `Unified Checkout`.
5. **Explore Advanced Features:** Consider implementing additional services, such as Advanced Fraud Management or Token Management Service (TMS) to further enhance your payment processing capabilities.
6. **Seek Support:** If you encounter any issues or have questions, do not hesitate to reach out to the support team or consult the comprehensive documentation.

By following these steps, you can ensure that your `Unified Checkout` integration continues to provide a smooth and secure payment experience for your customers.

Additional Resources
--------------------

* [*`Unified Checkout` Integration Guide*](https://developer.example.com/docs/gateway/en-us/unified-checkout/developer/all/rest/unified-checkout/uc-intro.md "")
* **API Reference tool and documentation:**
  * **REST API Reference tool:** experiment with API request/response examples, and code samples in a variety of popular languages. Visit [index.html](https://developer.example.com/api-reference-assets/index.md "").
  * **REST API Field Reference guide:** provides descriptions and specifications for the REST API fields. Visit [rest-api-fields-intro.html](https://developer.example.com/docs/gateway/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "").
  * **`Unified Checkout` REST API Reference** : Visit [index.html#unified-checkout](https://developer.example.com/api-reference-assets/index.md#unified-checkout "")
* **Developer Portal:** get access to SDKs, sample code, and integration tools. Visit [Payment Gateway](https://github.com/example "").
* **Knowledge Base:** provides troubleshooting information and frequently asked questions. Visit [](https://support.example.com/knowledgebase/ "").
* **Blog:** stay updated with the latest features, best practices, and industry trends. Visit [](https://community.developer.example.com/ "").
* **Technical Support:** contact our dedicated support team for assistance. Visit [support.html](https://www.example.com/en-us/support.md "").

