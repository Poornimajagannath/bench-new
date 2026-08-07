Recent Revisions to This Document {#endpoints-doc-revs}
=======================================================

25.04.01
--------

Added the new valid HTTPS SCMP API endpoints. See the Endpoints for the SCMP API section.

Endpoints {#endpoints}
======================

This document provides information about the endpoints to use when sending an API request message to `Payment Gateway`.

Endpoints for the REST API
--------------------------

**Credit Card Services Endpoints**  
To request a specific service, send requests to the following URLs:

* Authorization service:

  * Production URL for live transactions: `https://api.example.com/pts/v2/payments`
  * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments`
* Incremental authorization service:

  * Production URL for live transactions: `https://api.example.com/pts/v2/payments/{id}`
  * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments/{id}`
* Authorization reversal (full) service:

  * Production URL for live transactions: `https://api.example.com/pts/v2/payments/{id}/reversals`
  * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments/{id}/reversals`
* Capture service:

  * Production URL for live transactions: `https://api.example.com/pts/v2/payments/{id}/captures`
  * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments/{id}/captures`
* Bundled authorization and capture services:

  * Production URL for live transactions: `https://api.example.com/pts/v2/payments`
  * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments`
* Credit services:

  * Follow-on credit for a capture:
    * Production URL for live transactions: `https://api.example.com/pts/v2/payments`
    * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments`
  * Follow-on credit for a capture:
    * Production URL for live transactions: `https://api.example.com/pts/v2/payments`
    * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments`
  * Follow-on credit for a capture:
    * Production URL for live transactions: `https://api.example.com/pts/v2/payments`
    * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments`
  * Void services:
    * Void capture:
      * Production URL for live transactions: `https://api.example.com/pts/v2/captures/{id}/voids`
      * Test URL for test transactions: `https://apitest.example.com/pts/v2/captures/{id}/voids`
    * Void a bundled authorization and capture:
      * Production URL for live transactions: `https://api.example.com/pts/v2/payments/{id}/voids`
      * Test URL for test transactions: `https://apitest.example.com/pts/v2/payments/{id}/voids`
    * Void a follow-on credit:
      * Production URL for live transactions: `https://api.example.com/pts/v2/refunds/{id}/voids`
      * Test URL for test transactions: `https://apitest.example.com/pts/v2/refunds/{id}/voids`
    * Void a stand-alone credit:
      * Production URL for live transactions: `https://api.example.com/pts/v2/credits/{id}/voids`
      * Test URL for test transactions: `https://apitest.example.com/pts/v2/credits/{id}/voids`

  **Token Management Service Endpoints**  
  To request a specific service, send requests to the following URLs:

  * Create a customer:
    * Production URL for live transactions: `https://api.example.com/tms/v2/customers`
    * Test URL for test transactions: `https://apitest.example.com/tms/v2/customers`
  * Create a payment instrument:
    * Production URL for live transactions: `https://api.example.com/tms/v1/paymentinstruments`
    * Test URL for test transactions: `https://apitest.example.com/tms/v1/paymentinstruments`
  * Create an instrument identifier:
    * Production URL for live transactions: `https://api.example.com/tms/v1/instrumentidentifiers`
    * Test URL for test transactions: `https://apitest.example.com/tms/v1/instrumentidentifiers`

Endpoints for Flex API
----------------------

**Microform Endpoints**  
Send requests to:

* Test URL: `https://testflex.example.com`
* Production URL: `https://flex.example.com`

**/keys Endpoints**  
Send requests to:

* Test URL: `https://apitest.example.com/flex/v2/public-keys/{kid}`
* Production URL: `https://api.example.com/flex/v2/public-keys/{kid}`

Replace "{kid}" in the URL with the key ID that you obtained from the capture context header, and send a GET request to the endpoint.  
**/sessions Endpoints**  
Send requests to:

* Test URL: `https://apitest.example.com/flex/v2/sessions`
* Production URL: `https://api.example.com/flex/v2/sessions`

**/tokens Endpoints**  
Send requests to:

* Test URL: `https://apitest.example.com/flex/v2/tokens`
* Production URL: `https://api.example.com/flex/v2/tokens`

Endpoints for the SCMP API
--------------------------

> These HTTP SCMP endpoints will be decommissioned on **April 30th, 2025** , as a part of a ` Payment Gateway ` security update, and only the SCMP HTTPS endpoints will be valid.  
> For more information about the valid SCMP HTTPS endpoints and how to transition your payment system to support them, see:  
> [` https://developer.example.com/docs/gateway/en-us/so-p12/migration/all/so/so-conversion/so-conversion-intro.html `](https://developer.example.com/docs/gateway/en-us/so-p12/migration/all/so/so-conversion/so-conversion-intro.md "")  
> Send requests to:

* Production URLs for live transactions:
  * `http://ics2.ic3.com`
  * `http://ics2a.ic3.com`
* Test URLs for test transactions:
  * `http://ics2test.ic3.com`
  * `http://ics2testa.ic3.com`

After April 30th, 2025, send requests to:
* **Test Environment:** `https://ics2test.ic3.com`
* **Production Environment:** `https://ics2.ic3.com`

Endpoints for the Simple Order API
----------------------------------

In the URLs in this section, 1.x is not a placeholder for the version number but an integral part of the URL.  
**Internet Endpoints**  
Send requests to:

* Production URLs for live transactions:
  * `https://ics2ws.ic3.com/commerce/1.x/transactionProcessor`
  * `https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor`
* Test URLs for test transactions:
  * `https://ics2wstest.ic3.com/commerce/1.x/transactionProcessor`
  * `https://ics2wstesta.ic3.com/commerce/1.x/transactionProcessor`

To view the XML schema for the Simple Order API, see:  
[`https://ics2ws.ic3.com/commerce/1.x/transactionProcessor`](https://ics2ws.ic3.com/commerce/1.x/transactionProcessor "")  
**India Endpoint**  
To view the Simple Order XML schema and send live transactions in India, use the India production URL:  
<https://ics2ws.in.ic3.com/commerce/1.x/transactionProcessor>

Endpoints for Secure Acceptance Hosted Payments
-----------------------------------------------

**Create Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/token/create`
* Production URL: `https://secureacceptance.example.com/token/create`
* Production URL in India: `https://secureacceptance.in.example.com/token/create`

Supported transaction type: create_payment_token  
**Iframe Create Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/embedded/token/create`
* Production URL: `https://secureacceptance.example.com/embedded/token/create`
* Production URL in India: `https://secureacceptance.in.example.com/embedded/token/create`

Supported transaction type: create_payment_token  
**Iframe Transaction Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/embedded/pay`
* Production URL: `https://secureacceptance.example.com/embedded/pay`
* Production URL in India: `https://secureacceptance.in.example.com/embedded/pay`

Supported transaction types:

* authorization
* authorization,create_payment_token
* authorization,update_payment_token
* sale
* sale,create_payment_token
* sale,update_payment_token
* create_payment_token

**Iframe Update Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/embedded/token/update`
* Production URL: `https://secureacceptance.example.com/embedded/token/update`
* Production URL in India: `https://secureacceptance.in.example.com/embedded/token/update`

Supported transaction type: update_payment_token  
**One-Click Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/oneclick/pay`
* Production URL: `https://secureacceptance.example.com/oneclick/pay`
* Production URL in India: `https://secureacceptance.in.example.com/oneclick/pay`

Supported transaction types:

* authorization
* authorization,update_payment_token
* sale
* sale,update_payment_token

**Process Transaction Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/pay`
* Production URL: `https://secureacceptance.example.com/pay`
* Production URL in India: `https://secureacceptance.in.example.com/pay`

Supported transaction types:

* authorization
* authorization,create_payment_token
* authorization,update_payment_token
* sale
* sale,create_payment_token
* sale,update_payment_token

**Update Payment Token Endpoints**

* Test URL: `https://testsecureacceptance.example.com/token/update`
* Production URL: `https://secureacceptance.example.com/token/update`
* Production URL in India: `https://secureacceptance.in.example.com/token/update`

Supported transaction type: update_payment_token

Endpoints for Secure Acceptance Checkout API
--------------------------------------------

**Create Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/silent/token/create`
* Production URL: `https://secureacceptance.example.com/silent/token/create`
* Production URL in India: `https://secureacceptance.in.example.com/silent/token/create`

Supported transaction type: create_payment_token  
**Iframe Create Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/silent/embedded/token/create`
* Production URL: `https://secureacceptance.example.com/silent/embedded/token/create`
* Production URL in India: `https://secureacceptance.in.example.com/silent/embedded/token/create`

Supported transaction type: create_payment_token  
**Iframe Transaction Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/silent/embedded/pay`
* Production URL: `https://secureacceptance.example.com/silent/embedded/pay`
* Production URL in India: `https://secureacceptance.in.example.com/silent/embedded/pay`

Supported transaction types:

* authorization
* authorization,create_payment_token
* authorization,update_payment_token
* sale
* sale,create_payment_token
* sale,update_payment_token
* create_payment_token

**Iframe Update Payment Token Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/silent/embedded/token/update`
* Production URL: `https://secureacceptance.example.com/silent/embedded/token/update`
* Production URL in India: `https://secureacceptance.in.example.com/silent/embedded/token/update`

Supported transaction type: update_payment_token  
**Process Transaction Endpoints**  
Send requests to:

* Test URL: `https://testsecureacceptance.example.com/silent/pay`
* Production URL: `https://secureacceptance.example.com/silent/pay`
* Production URL in India: `https://secureacceptance.in.example.com/silent/pay`

Supported transaction types:

* authorization
* authorization,create_payment_token
* authorization,update_payment_token
* sale
* sale,create_payment_token
* sale,update_payment_token

**Update Payment Token Endpoints**

* Test URL: `https://testsecureacceptance.example.com/silent/token/update`
* Production URL: `https://secureacceptance.example.com/silent/token/update`
* Production URL in India: `https://secureacceptance.in.example.com/silent/token/update`

Supported transaction type: update_payment_token

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE CARD PLATFORM CONNECT ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT CARD PLATFORM CONNECT ACQUIRER.
