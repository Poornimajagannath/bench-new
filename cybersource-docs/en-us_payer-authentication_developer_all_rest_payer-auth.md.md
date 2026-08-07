Recent Revisions to This Document {#reference.dita_bf7f009c-6cb6-42c4-9fc7-edcc89310919}
========================================================================================

26.03.01
--------

New Test Card Numbers
:
Added RuPay card numbers for the `3-D Secure` 2.x test cases. See [Test Cases for 3-D Secure 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "").

Updated the Flex Microform Endpoints
:
The REST Test and Production endpoints for checking enrollment and validating `3-D Secure` transactions while using Flex Microform tokens were corrected. See [Checking Enrollment When Using a Flex Microform Token](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-tokens-flex/pa2-use-token-flex-enroll-intro.md "") and [Validating a Challenge When Using a Flex Microform Token](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-tokens-flex/pa2-use-token-flex-validate-intro.md "").

Updated Step-Up Payload Description
:
Clarified that the Step-Up response is not URL-encoded or Base64-encoded by removing the statement. See [Receiving the Step-Up Results](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro/pa2-ccdc-stepup-frame-receiving-stepup-results.md "").

26.01.01
--------

New Jaywan Card Test Numbers
:
Added Jaywan card numbers for the `3-D Secure` 2.x test cases. See [Test Cases for 3-D Secure 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "").

Added Endpoints
:
Added endpoints to the descriptions of the different stages of `3-D Secure` authentication. For an example, see [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md "").

Required Fields Update for Setup Service
:
Updated the fields listed for the Setup step. For more information, see [Request Fields](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro/pa2-ccdc-setup-request-fields.md "").

New Mastercard Data Only Example
:
Updated Mastercard Data Only `3-D Secure` 2.x test cases to include Identity Check Insights (IDCI). See [Mastercard Data Only](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-data-only-intro/pa2-use-data-only-mc-intro.md "").

New PayPak Test Card Numbers
:
Added PayPak test card numbers for `3-D Secure` authentication. See [Test Cases for 3-D Secure 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "").

25.10.01
--------

Updated Required Fields for Relay Data Only
:
The list of required fields for Relay Data Only was updated removing the Message Category field since it is not a required field and corrected the spelling of the Challenge Code field. See [Required Fields for Relay Data Only](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-data-only-intro/pa2-use-data-only-relay-intro/pa2-use-data-only-relay-req-fields.md "").

25.09.02
--------

Updated XID Values
:
The Test Cases for `3-D Secure` 2.x section were updated to better reflect which card schemes returned XID values during Enrollment and Validation. See [Test Cases for `3-D Secure` 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "").

Updated ECI String and ECI Raw Values for ITMX
:
The Test Cases for `3-D Secure` 2.x section were updated to include ECI string and raw values for ITMX. See [Test Cases for `3-D Secure` 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "")

25.09.01
--------

This revision contains only editorial changes and no technical updates.

25.07.01
--------

Updated Content
:
Removed the section *Upgrading Your Payer Authentication Implementation* that was no longer needed.

`eftpos` Test Card Numbers
:
Added eftpos card numbers for the `3-D Secure` 2.x test cases. These new card numbers are in addition to the existing co-badged eftpos card numbers. See [Test Cases for 3-D Secure 2.x](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro/pa-testing-3ds-2x-intro.md "").

25.05.01
--------

Updated China UnionPay References
:
Consolidated references to China UnionPay and UnionPay International to "China UnionPay."
{#reference.dita_bf7f009c-6cb6-42c4-9fc7-edcc89310919_dlc}

Payer Authentication Developer Guide {#product-about-guide}
===========================================================

This section describes how to use this guide and where to find further information.

Audience and Purpose
:
This guide is written for merchant application developers who want to use the REST API to integrate payer authentication services into their system. It describes the tasks you must perform in order to complete this integration.

    Implementing payer authentication services requires software development skills.

Scope
:
This guide describes how to use the REST API to integrate payer authentication services with your order management system. It does not describe how to get started using the REST API nor does it explain how to use services other than payer authentication. For that information, see the *Related Documentation* section.

Conventions
:
These special statements are used in this document:

    > IMPORTANT
    > An *Important* statement contains information essential to successfully completing a task or learning a concept.

    > WARNING
    > A *Warning* contains information or instructions, which, if not followed, can result in a security risk, irreversible loss of data, or significant cost in time or revenue.

Related Documentation
:
Visit the [Documentation Hub](https://developer.cybersource.com/docs.md "") to find additional documentation.

Customer Support
:
For support information about any service, visit the Support Center:

[https://support.example.com](https://support.example.com/ "") .

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Introduction to Payer Authentication {#pa2-intro-intro}
=======================================================

`Cybersource` has a variety of products to manage and minimize the risk of fraud that merchants face in their daily transactions. While these risk management products can operate independently to address specific areas of risk, the best results are achieved when the entire suite of products works in concert to detect patterns of fraud in a business's online activity.

* Payer Authentication: Uses the `3-D Secure` protocol in online transactions to verify that payment is coming from the actual cardholder. Most transactions can be authenticated without the customer being aware of the process, but higher risk transactions might require an exchange of one-time passwords (OTPs) during authentication. This authentication of the payer before the transaction is authorized benefits the merchant by shifting chargeback liability from the merchant to the card issuer. You can use Decision Manager with payer authentication services so that the risk level of an order determines when to invoke payer authentication. For example, low-risk orders can be set to skip payer authentication and proceed directly to authorization.
* Decision Manager: Uses AI to help large enterprises analyze the vast amount of data from their online transactions to detect known patterns of fraudulent behavior. Each potential transaction can be compared to past patterns and automatically assigned a risk score before authorizing a transaction. Behavior analysis of past transaction data enables you to recommend rules that identify risky transactions and to suggest how to handle them. Machine learning capabilities in Decision Manager enable you to create hypothetical environments to test strategies for dealing with risky scenarios so that you can either reject them or require payer authentication.
* Fraud Management Essentials: helps small-to-medium businesses monitor their online transactions using AI and preconfigured rules to spot and avoid fraudulent transactions. You can adjust the fraud detection settings to match your risk tolerance and manually review transactions flagged for risk review.
* Account Takeover Protection: monitors customer account activity to detect compromised accounts. You create account events and define rules to determine the types and levels of activity in a customer account that trigger a manual review for potential fraud. The activity data that happens within a customer account can be easily integrated into Decision Manager and used to assess risky payment behavior.

{#pa2-intro-intro_ul_l2t_bxn_n1c}  
This guide documents the payer authentication aspect of fraud management and how payer authentication can be used to satisfy the Strong Customer Authentication (SCA) requirement of the Payment Services Directive (PSD2) that applies to the European Economic Area (EEA) and the United Kingdom. SCA requires banks to perform additional verification when customers make payments to confirm their identity. Access to the documentation for other aspects of the risk management portfolio requires a `Cybersource` support license for that product.  
Transactions where the card is not present have a high risk of fraud, so authenticating a payer before processing a transaction greatly reduces the merchant risk for chargebacks. Payer authentication is a way of verifying that a customer making an e-commerce purchase is the owner of the payment card being used. The protocol that is followed to authenticate customers during online transactions is called [EMV 3-D Secure](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-glossary.md#reference_sjs_jmp_wpb_3-d-secure "").  
This EMV `3-D Secure` protocol is used by all major payment cards to implement payer authentication, but payment companies usually brand it under a different name:

* Relay: Relay Secure
* Mastercard: Mastercard Identity Check
* American Express: American Express SafeKey
* JCB: J/Secure
* Discover/Diners: ProtectBuy
* Elo: Compra Segura (Secure Shopping)
* Cartes Bancaires: FAST'R
* China UnionPay: `3-D Secure`

{#pa2-intro-intro_ul_qf3_zhl_kxb}

Supported Card Networks
-----------------------

These card networks support using EMV `3-D Secure` during transactions:

* Amex
* Cartes Bancaires
* China UnionPay
* Discover/Diners
* eftpos
* Elo
* JCB
* Mada
* Mastercard
* Relay
  {#pa2-intro-intro_ul_yft_hdj_cfc}

Why Payer Authentication Is Needed {#pa2-intro-3ds-history}
===========================================================

As e-commerce developed, the number of fraudulent transactions also grew, taking advantage of the difficulty authenticating a cardholder during a transaction when the card is not present. To create a standard for secure payment card processing, Europay, Mastercard, and Relay collaborated as EMV. Other card providers wanted input on creating new payment standards, so a consortium called EMVCo was formed to enable equal input from Relay, Mastercard, JCB, China UnionPay, Discover, and American Express.  
EMVCo developed `3-D Secure` as the protocol to provide customer authentication during an online transaction. EMV `3-D Secure` reduced chargebacks to merchants, and when the buyer was authenticated, the issuing bank assumed any liability when a chargeback occurred.  
The same need to reduce fraud prompted Europe to develop a standard called Strong Customer Authentication (SCA) to regulate authentication during electronic payments. The use of SCA is mandated by the European Banking Authority in the Payment Services Directive (PSD2) that took effect in 2018 to promote and regulate the technical aspects of financial transactions between merchants and their customers in Europe. SCA requires two-factor authentication. A customer must be able to authenticate by providing two of these three factors:

* Something the customer knows (such as a password, PIN, or challenge questions)
* Something the customer has (such as a phone or hardware token)
* Something the customer is (biometric data, such as fingerprint or face recognition)

{#pa2-intro-3ds-history_ul_ps1_jbd_4xb}  
Although SCA is required for almost all online transactions, some exceptions are allowed. If a payment is considered low risk, you can request an exemption from SCA to bypass authentication of the customer. The issuing bank must approve the exemption before the transaction can be exempted from SCA. Although an exemption from SCA results in a frictionless transaction, liability is not shifted to the issuing bank, and the merchant assumes responsibility for any chargeback that occurs. An exemption from SCA might apply to these types of transactions:

* Payer authentication is unavailable because of a system outage.
* Payment cards used specifically for business-to-business transactions are exempt.
* Payer authentication is performed outside of the authorization workflow.
* Follow-on installment payments of a fixed amount are exempt after the first transaction.
* Follow-on recurring payments of a fixed amount are exempt after the first transaction.
* Fraud levels associated with this type of transaction are considered a low risk.
* Low transaction value does not warrant SCA.
* Merchant-initiated transactions (MITs) are follow-on transactions that are also exempt.
* Stored credentials were authenticated before they were stored, so stored credential transactions are exempt.
* Trusted merchants registered as trusted beneficiaries, are exempt.

{#pa2-intro-3ds-history_ul_qs1_jbd_4xb}  
For additional information about transactions that are exempt from SCA, see the [Payments Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments/payments-intro.md "").  
EMV `3-D Secure` meets the SCA mandate for authenticating the customer during e-commerce transactions.

EMV `3-D Secure` 2.0 {#pa2-intro-benefits}
==========================================

To improve the customer experience, a new version of `3-D Secure` was developed. EMV `3-D Secure` 2.x uses a less intrusive process to authenticate a buyer, which provides a better customer experience.  
Enhancements to `3-D Secure` 2.x include:

* More robust device data collection to improve risk analysis by the issuing bank.
* Small screens that pop up on your webpage to avoid full-page redirects.
* SDK version for mobile devices like phones and tablets.
* Streamlined shopping experience.

> {#pa2-intro-benefits_ul_uf4_tz2_kxb} IMPORTANT  
> On September 25, 2024, support for EMV ` 3-D Secure ` 2.1.0 ended. Merchants and their acquirers must support EMV ` 3-D Secure ` 2.2.0 or a later version before that date so that transactions can continue without any interruption in service. Contact support for additional information on updating your system to use EMV ` 3-D Secure ` 2.2.0.

Payer Authentication Customer Workflow {#pa2-intro-workflows}
=============================================================

During authentication for each transaction, data is collected about the customer's device, and the shipping and billing information is compared with transaction history. The workflow in payer authentication can go one of two possible ways: frictionless and challenge (also known as *step-up*).

#### Figure: {#pa2-intro-workflows_fdc}

Payer Authentication Workflow ![Payer Authenticatiion Workflow Diagram](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/how-payer-auth-works-3.svg/jcr:content/renditions/original)

Frictionless Workflow {#pa2-intro-workflows_section_nqp_xv3_mxb}
----------------------------------------------------------------

With frictionless flow, the authentication process is not visible to the customer. The data collected during the transaction matches the data collected from past transactions with the customer. The risk for fraud is calculated to be low enough that further authentication is unnecessary. The transaction can continue to authorization.

1. The customer enters card information at checkout. Information about the device being used by the customer and shopping behavior is collected and relayed from the merchant to the issuing bank. A delay of about 10 seconds is built into the process to ensure that the device data can be transmitted and assessed before the Buy option is enabled.
2. The customer selects Buy.
3. The issuing bank verifies the information it receives against previous transactions. If the device data correlates with the information, the transaction is approved without the buyer having to provide any additional information.
   {#pa2-intro-workflows_ol_wl4_n3f_kxb}

Challenge Workflow
------------------

A challenge flow occurs when the data collected during the transaction does not match the information on file from previous transactions with the customer. This process occurs for multiple reasons and does not necessarily mean that the customer has fraudulent intent. For example, it could occur because the customer got a new device that has not been registered yet or because they bought something while traveling. The issuer of the card decides whether further authentication of the customer is required and if necessary, requests that the customer prove their identity by returning a passcode to the issuer. This sequence describes the interaction from the customer viewpoint.

1. The customer enters card information at checkout. Information about the customer's device is collected and sent from the merchant to the issuing bank.
2. The customer selects Buy.
3. The issuing bank assesses risk by comparing the information it receives to information on file from previous transactions with the customer. If the device data does not match the information collected previously, the issuer requests further authentication.
4. A small window opens on the checkout page where a message from the bank asks if the customer wants to use email or text message to receive a one-time password (OTP) from the bank.
5. The customer chooses how the password is sent.
6. The issuer sends an OTP to the account on file for the customer.
7. A window opens on the checkout page on the customer device prompting the customer to enter the OTP sent by the issuer.
8. The customer enters the password that they received and sends it back to the issuer.
9. If the password entered by the customer matches the password sent by the issuer, the customer is authenticated, and the transaction can proceed to authorization. If the password does not match the password that the bank sent, the customer receives a message that the transaction is declined and that they should attempt another form of payment.

Payer Authentication Merchant Workflow {#pa2-intro-process-overview}
====================================================================

Transaction circumstances might result in differences to the more detailed payer authentication process described below.
1. Before the Buy button is selected at checkout, the Setup service is called. The full card number identifies how to contact the issuing bank. The issuing bank sends an access token and a URL (called the *DCC URL*) to use for the data collected about the device where the transaction is occurring.
2. The merchant collects data about the device and includes billing and shipping information. The merchant posts this data to a hidden 10 pixel x 10 pixel iframe to send to the DDC URL provided by the card issuer for comparision with past transactions. After the data points are collected and sent, the issuing bank confirms that data collection ended and the Buy button is enabled. An 8-10 second delay ensures enough time for data collection.
3. Clicking Buy triggers the Check Enrollment service sending the order data (and session ID) to the issuer. If the bank is not part of an EMV `3-D Secure` program, the payer authentication process stops. If the issuing bank is part of an EMV `3-D Secure` program, the device data is compared to information on file collected at the bank during previous transactions with the cardholder.
   * The issuer's risk analysis software determines whether enough data points collected by the merchant match the data in the bank's files. If the data matches well, no further interaction is needed. This is called*frictionless flow* because no challenge to the buyer is necessary. The response returned to the merchant includes a payload with values like the *ECI* , *CAVV* , *DS Transaction Id* , and the *PARes Status*. These values must be passed on during the request for authorization. It is important to note that while frictionless flow can occur because the payer is authenticated, it can also occur for other reasons. For example, the issuing bank does not participate in payer authentication. Therefore, response values must be verified to determine why no step-up is needed.
   * If a significant discrepancy occurs between the transaction data and the data on file with the bank, the bank requests that the payer authenticate. This is a friction workflow and is called a *step up* or *challenge* . The response from the bank contains the same values returned for a frictionless workflow but also includes additional values like the *Access Control Server (ACS) URL* , the *PAReq* payload, a *Pares Status* = C, a *Step Up URL* , a new *JWT* , and a *Transaction Id*.
     {#pa2-intro-process-overview_ul_wm1_ftk_kxb}
4. The JWT and the step up URL received in the check enrollment response are returned to the customer. Using the step up URL with the JWT as a POST parameter, a challenge screen opens in a viewable iframe on the buyer's device so that the cardholder can view and respond to the bank challenge. The challenge consists of the bank sending a pass code that the customer returns to the bank. The challenge asks how the customer wants to receive a pass code, by text or email. After the customer chooses, they receive a pass code that they must enter into the challenge screen.
5. After the cardholder enters and sends the passcode, the response is sent to the merchant's return URL contained in the JWT. This response causes the merchant to make a validation call to the bank to obtain the final authentication outcome. The response to this validation request contains the final authentication results including these values: *ECI* , *CAVV* (if successful), *DSTransactionId* , *ThreeDSVersion* , and PARes Status (`Y` or `A` = successful or `N`, `U`, `R` = failed, unavailable, or rejected).
6. The next action depends on the outcome:
   * Successful: proceed to authorization, and append the EMV `3-D Secure` data points to the authorization message.
   * Failed, unavailable, or rejected: display a message to prompt the customer to try payment with a different card.
     {#pa2-intro-process-overview_concept_gnm_xym_qqb_ul_nfq_5tx_rqb}
     {#pa2-intro-process-overview_concept_gnm_xym_qqb_ol_btr_zym_qqb}

Acquirer Information {#pa2-intro-acquirer-info}
===============================================

To properly configure payer authentication, `Cybersource` uses three items of informationthat your acquiring bank uses to manage payments for your account. If you do not know this information, contact your acquiring bank`Cybersource`.

* Acquiring *Merchant ID* (MID): This unique identifier for your business account is assigned by your acquiring bank or payment processor. A MID consists of 8-24 alpha-numeric characters. The MID can be different than the business deposit identifier used in settlements.
* Acquiring *Bank Identification Number* (BIN): This unique number is assigned to the acquiring bank by a payment card network to identify that bank when settling transactions. Each payment card assigns its own BIN for an acquiring bank, and the BINs have their own unique characteristics. For example, all Relay BINs start with a 4, Mastercard BINs start with a 2 or 5, and Discover BINs start with a 3 or 6.
* Merchant Category Code (MCC): This four-digit numeric value is assigned by the acquirer to the merchant to classify the merchandise or services provided by the business. The MCC indicates the kind of business transaction that the merchant processes.
  {#pa2-intro-acquirer-info_ul_p34_1w3_4yb}

Enable Merchant Account for EMV `3-D Secure` {#pa2-intro-account-setup}
=======================================================================

Partners and merchants use the `Business Center` to go online and view transaction activity and to generate reports about their transactions. For each partner, an account is created, and a portfolio merchant ID (MID) is assigned. For each of the merchants within the partner's portfolio, an account is also created and assigned a merchant ID (MID). Access to the various functions in the `Business Center` is managed by the partner through the MID.  
When the MID account is created, the various services that the merchant needs must be enabled. For more information about configuring your account in the `Business Center` for payer authentication and other services, see the [Merchant User Boarding Guide](https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-products/boarding-payer-auth.md ""). Payer authentication is a service that might need to be turned on by support. To set up an account for payer authentication, you need this information:

* MID.
* Merchant website URL.
* Two-character ISO code for your country.
* Merchant category code.
* EMV `3-D Secure` requestor ID (optional).
* EMV `3-D Secure` requestor name (optional).
* Name of merchant's bank.
* Name, address, and email address of bank contact.

{#pa2-intro-account-setup_ul_jzp_krr_kxb}  
For each payment card that you accept, your acquirer must provide this information:

* Eight-digit BIN number.
* Merchant ID assigned by your acquirer.
* List of all of the currencies that you can process.
  {#pa2-intro-account-setup_ul_pxq_hsr_kxb}

Payer Authentication Configuration Testing {#pa2-intro-testing}
===============================================================

After the payer authentication functionality is enabled for your account and you have installed and configured the software, you must run tests to ensure that payer authentication is working properly. You must ensure that the proper data is being collected and sent to the issuer and that the proper status for a particular circumstance is returned. To ensure that the proper statuses are returned under all possible circumstances, extensive testing is required before you go live with payer authentication.  
A sandbox testing environment is provided to resolve any bugs in your system. In this testing environment, you can simulate various transaction scenarios with the types of payment cards that you accept. Test card numbers for the various types of payment cards are provided so that you can run transaction simulations. You can verify that the values generated during the simulations are the correct values that should occur during that transaction scenario.  
When your test results are correct, contact customer support and request to go live. When you go live, you will use the production host name to process transactions instead of the test host name that you used when processing transactions in the test environment.  
The host name for the testing environment:  
`POST ``https://apitest.cybersource.com`  
The host name for the production environment:  
`POST ``https://api.cybersource.com`  
Details about testing your payer authentication configuration are available in the [Testing Payer Authentication Services](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md "") section.

Request Endpoints {#pa2-intro-endpoints}
========================================

When posting a request for payer authentication, you must add an endpoint to each hostname, whether you are using the test environment or the production environment. These endpoints are used with payer authentication.  
`/risk/v1/authentications`: use when verifying that a card is enrolled in a card authentication program or requesting authentication from the issuer.  
`/risk/v1/authentication-results`: use when retrieving and validating authentication results from the issuer so that the merchant can process the payment.  
`/pts/v2/payments`: use when bundling multiple payments together.  
For example, a test request might look like this:  
`POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Payer Authentication Integrations {#pa2-intro-integration}
==========================================================

Payer authentication was designed to authenticate buyers during online transactions. During the early growth of internet transactions, e-commerce was conducted only on computers. Mobile phones had limited capabilities. When mobile phones (and tablets) could access the internet, online transactions quickly grew, and now they comprise almost half of all e-commerce transactions. A key part of updating the EMV `3-D Secure` protocol from 1.0 to 2.0 was to ensure that payer authentication became available for e-commerce done on mobile devices.  
Two types of payer authentication integration are available for merchants:

* API for browser authentication from a computer.
* SDK for authentication from mobile devices (available for Android and iOS). Contact support to obtain the SDK.

{#pa2-intro-integration_ul_tt2_fjy_kxb} IMPORTANT
Payer Authentication supports message-level encryption. For more information, see [Message Level Encryption](https://developer.relay.com/pages/encryption_guide "").  
Merchants should integrate payer authentication for online shopping on both types of devices. The next sections in this guide describe how to integrate payer authentication into those shopping experiences.

Implementing Direct API for Payer Authentication {#concept_hdl_g1x_wpb}
=======================================================================

The Direct API integrates EMV `3-D Secure` 2.x into your business's website. This integration uses an iframe to complete the device profiling and EMV `3-D Secure` authentication requirements without including third-party JavaScript directly on your site.  
This implementation requires the use of JavaScript to leverage the authentication. The JavaScript is hosted and contained inside the iframe and does not directly access your web page.

> IMPORTANT
> Payer Authentication uses Cardinal Centinel as the technology platform to manage all EMV ` 3-D Secure ` authentication processes. Any references to Cardinal in this document refer to the underlying services that are provided by Cardinal technology.
> A website that provides a demo tool to help users understand how payer authentication works is available:  
> [https://developer.cybersource.com/demo/index.html](https://developer.cybersource.com/demo/index.md "").  
> You can complete the steps required to implement payer authentication on their website and examine the code underlying the process. Use test card numbers to walk through the process and enter `123` as the security code.

Prerequisites {#concept_q1d_j1x_wpb}
====================================

Notify your account representative that you want to implement payer authentication (3-D Secure) using the Direct API integration. Provide the merchant ID that you will use for testing. For more information, see [Required Merchant Information](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-intro-intro/pa2-intro-process-overview.md "").  
Before you can implement payer authentication services, your business team must contact your acquirer and `Cybersource` to establish the service. Your software development team should become familiar with the API fields and technical details of this service.

After Implementation and Before Go Live {#concept_nzg_z3x_wpb}
==============================================================

Use the test cases to test your preliminary code and make appropriate changes. See [Testing Payer Authentication](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md ""). Testing ensures that your account is configured for production and that your transactions are processed quickly and correctly.

Step 1: Setup Service {#pa2-ccdc-setup-intro}
=============================================

Request the Setup service before selecting the button to submit payment. Request the Setup service separately without including other services. The Setup service response will include a JSON Web Token (JWT) that contains credentials to create a secure channel with you. The Setup response also includes a reference ID to use during the authentication and a URL to use when transferring the device data that is collected in the next step.  
IMPORTANT The Setup service is used only in the Direct API integration. The SDK integration does not use this step.  
Run the Setup service as soon as the customer enters their card number to avoid any delay in the customer experience. The next step in the process, device data collection, cannot start until the Setup response is received because the response has the URL where the device data will be sent.

#### Figure: {#pa2-ccdc-setup-intro_fig_tdp_pzj_ldc}

Process Flow for Setup for Payer Authentication ![Process Flow Diagram for Setup for Payer Authentication](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-setup-3.svg/jcr:content/renditions/original)

Best Practices
--------------

This practice should be followed so that this step achieves optimal performance and to minimize potential operating issues.  
After the customer credit card is entered, immediately begin device data collection.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Request Fields {#pa-ccdc-setup-service-request-fields}
======================================================

When requesting the Setup service, you must send the customer's payment information. This can be either the actual encrypted card information or a token associated with the payment data.  
These fields are required:
* paymentInformation.card.expirationMonth

* paymentInformation.card.expirationYear

* paymentInformation.card.number

* paymentInformation.card.type
  {#pa-ccdc-setup-service-request-fields_ul_q2m_xjk_nhc}  
  Besides the required fields, the request might also include any of these fields:

* paymentInformation.tokenizedCard.number

* paymentInformation.customer.customerId

* tokenInformation.transientToken

{#pa-ccdc-setup-service-request-fields_ul_lhq_5ml_xpb}  
The paymentInformation.card.type field is required when the card type is JCB, Cartes Bancaires, or China UnionPay.

Important Response Fields {#concept_am2_mnl_xpb}
================================================

The response from the issuing bank might include these API fields.

* consumerAuthenticationInformation.accessToken is used in [Step 2: Device Data Collection](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-ddc-intro.md "").
* consumerAuthenticationInformation.deviceDataCollectionUrl is used in [Step 2: Device Data Collection](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-ddc-intro.md "").
* consumerAuthenticationInformation.referenceId is used in [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md "").

{#concept_am2_mnl_xpb_ul_nxn_lzw_vyb}  
For further details on examples, see [REST Example: Setting Up Data Collection](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-cases-intro/pa2-set-up-use-intro/pa2-use-setup-rest-ex.md "")

Step 2: Device Data Collection {#concept_ftg_v4l_xpb}
=====================================================

Device data collection starts on the merchant end after you receive the server-side Setup service response as described in [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md "") and pass the access token and the device data collection URL to the front end. When device data gets to the data collection URL, a Method URL stipulated in the `3-D Secure` protocal captures the entire card number to identify the issuing bank.  
A hidden 10 x 10 pixel iframe is rendered in the browser, and using the access token, you send the customer device data to the device data collection URL. The device data collection can take up to 10 seconds. If you proceed with the check enrollment service as described in [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md "") before a response is received, the collection process is short-circuited and an error occurs. Despite the error, as long as you include the data from the eleven browser fields as explained in [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md ""), you can still proceed with the EMV authentication.  
It is recommended that the device data collection start immediately after you receive the customer card number to ensure that the data collection runs in the background while the customer continues with the checkout process, ensuring a minimum of waiting. When a customer changes to a different card number, begin the Setup and device data collection process again as soon as the new card number is entered.

#### Figure: {#concept_ftg_v4l_xpb_fig_tdp_ldc}

Process Flow for Device Data Collection ![Process Flow diagram for Device Data Collection](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-ddc-3.svg/jcr:content/renditions/original)

Best Practices
--------------

These practices should be followed for this step in order to achieve optimal performance and to minimize potential operating issues.

* After the customer credit card number is entered, immediately begin the device data collection.
* Device data collection must complete before the enrollment check begins.
* While not required, it is highly recommended to pass the values from the 11 browser-based fields in the request. The information from these fields serves as a backup, in case the device data collection does not complete correctly.
* As much billing data as possible (unless restricted by regional mandates) should be supplied to the issuing bank to ensure that the issuer's risk assessment software has the most comprehensive data.
* The billing data such as state and country must be formatted according to ISO 3166-2 format specifications to ensure that the network can properly validate the data.
  {#concept_ftg_v4l_xpb_ul_ex1_dgq_fyb}

Which Device Data is Collected {#pa2-intro-ddc}
===============================================

One of the key components to authenticating a cardholder during an online transaction is to compare information about the device that the customer is currently using to the information in the bank's database about devices the customer used in past transactions. This information is maintained in the acess control server (ACS) at the issuing bank. This device information focuses on the web browser and includes these types of data:

* IP address
* Browser language
* Browser type
* Browser version
* Computer operating system
* System time zone
* Screen dimensions
* Color depth

{#pa2-intro-ddc_ul_yz1_vny_kxb}  
A successful device data collection process that includes the 11 browser fields listed in the check enrollment step increases the chances of a frictionless authentication. See [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md "") for the list of 11 browser fields. Business rules evaluate whether a transaction is risky enough to require the buyer to authenticate their identity. These business rules are configured in the issuer's risk analysis software that evaluates each transaction.

Building the Iframe {#concept_hd5_gpl_xpb}
==========================================

The iframe has these parameters:

* Form POST Action: The POST goes to the URL that is opened within an iframe. This URL is the value provided by the consumerAuthenticationInformation.deviceDataCollectionUrl response field discussed in [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md "").
* JWT POST Parameter: Use the value from the consumerAuthenticationInformation.accessToken response field discussed in [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md "").
  {#concept_hd5_gpl_xpb_ul_grt_jpl_xpb}

Initiating the Device Data Collection Iframe {#reference_mhg_xpl_xpb}
=====================================================================

Initiate a form POST in a hidden 10 x 10 pixel iframe and send it to the device data collection URL (consumerAuthenticationInformation.deviceDataCollectionUrl).  
Place the HTML anywhere inside the `&lt;body&gt;` element of the checkout page. Dynamically replace the value of the form action attribute and JWT POST parameter with the response values discussed in [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md ""). See this example. **Initiate the Device Data Collection Iframe**

```
&lt;iframe id="cardinal_collection_iframe" name="collectionIframe" height="10" width="10" style="display: none;"&gt;&lt;/iframe&gt;
&lt;form id="cardinal_collection_form" method="POST" target="collectionIframe" action=https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect&gt;
  &lt;input id="cardinal_collection_form_input" type="hidden" name="JWT" value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJSZWZlcmVuY2VJZCI6ImE0NjVlYzU1LTMwNTEtN GYwZC05MGE0LWZjMDNlMGE2MWQxOSIsIlJldHVyblVybCI6Imh0dHA6XC9cL2xvY2FsaG9zdDo4MDgyXC9yZXF1ZX N0LWNhdGNoZXJcL2NhdGNoLXJlcXVlc3QucGhwIiwianRpIjoianRpXzVmMDVkM2VkY2U0MjYzLjc5MjQwNzMzIi wiaWF0IjoxNTk0MjE3NDUzLCJpc3MiOiI1YjIzZjhjMGJmOWUyZjBkMzQ3ZGQ1YmEiLCJPcmdVbml0SWQiOiI1 NWVmM2YwY2Y3MjNhYTQzMWM5OWI0MzgifQ.Yw9cB9Hdrg71GPL40oAC0g3CVKYElNGe0uvN9JAaw2E"&gt;
&lt;/form&gt;                         
```

Submitting the Device Data Collection Iframe {#reference_yd1_nql_xpb}
=====================================================================

Add JavaScript to invoke the iframe form POST. Place the JavaScript after the closing `&lt;/body&gt;` element as shown in this example. The JavaScript invokes the iframe form POST automatically when the window loads. You must submit it before requesting the Check Enrollment service. **JavaScript to Invoke the Iframe Form POST**

```
 &lt;script&gt;
window.onload = function() { 
var cardinalCollectionForm = document.querySelector('#cardinal_collection_form'); 
if(cardinalCollectionForm) // form exists 
cardinalCollectionForm.submit();
}
&lt;/script&gt;
```

Receiving the Device Data Collection URL Response {#reference_qmk_jrl_xpb}
==========================================================================

Receiving the response indicates that the device data collection URL completed its processing. The response is an event callback that contains a message with the status of the device data collection process.  
Use the `event.origin` URL that corresponds to your environment:

* Test: `https://centinelapistag.cardinalcommerce.com`
* Production: `https://centinelapi.cardinalcommerce.com`

{#reference_qmk_jrl_xpb_ul_z5j_dsl_xpb}  
Study the example below to understand how to subscribe to the event. Add JavaScript to receive the response from the device data collection iframe. Place the JavaScript after the closing `&lt;/body&gt;` element. **Listen for Device Data Collection Response**

```
window.addEventListener("message", function(event) {
  if (event.origin === https://centinelapistag.cardinalcommerce.com) {
    console.log(event.data);
  }
}, false);        
```

This example shows a response payload from the event. None of the returned data needs to be stored for future use.  
**Event Listener Callback Payload**

```
{
  "MessageType": "profile.completed",
  "Session Id": "f54ea591-51ac-48de-b908-eecf4ff6beff",
  "Status": true
}          
```

Step 3: Payer Authentication Check Enrollment Service {#concept_b5y_3sl_xpb}
============================================================================

Request the Check Enrollment service only after you receive the device data collection response. Checking enrollment before receiving the device data collection response stops the data collection process. Data collection can take up to 10 seconds. The merchant should set a timer that expires after 10 seconds of waiting for a response to the data collection so that the check enrollment service starts even when the device data collection response was not received.  
You must include these 11 browser field values in the check enrollment request. These fields provide the information that that ensures a transaction qualifies as an EMV `3-D Secure` transaction. The information in these fields provides a backup for the occasions when the device data collection fails to complete.

* consumerAuthenticationInformation.deviceChannel
* deviceInformation.httpAcceptContent
* deviceInformation.httpBrowserColorDepth
* deviceInformation.httpBrowserJavaEnabled
* deviceInformation.httpBrowserJavaScriptEnabled
* deviceInformation.httpBrowserLanguage
* deviceInformation.httpBrowserScreenHeight
* deviceInformation.httpBrowserScreenWidth
* deviceInformation.httpBrowserTimeDifference
* deviceInformation.ipAddress
* deviceInformation.userAgentBrowserValue

{#concept_b5y_3sl_xpb_ul_j1l_yy3_2yb}  
With the device data collected, the issuer runs a risk assesment that results in one of these outcomes:

* Frictionless success (low risk)
* Challenge required (moderate risk)
* Frictionless failure or decline (high risk)

{#concept_b5y_3sl_xpb_ul_bvh_v3r_jyb}

#### Figure: {#concept_b5y_3sl_xpb_fig_tdp_pc}

Process Flow for Checking Enrollment in Payer Authentication ![Process flow diagram for checking enrollment in Payer Authentication](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-enrollment-3.svg/jcr:content/renditions/original)

Best Practices
--------------

Follow these practices for this step to achieve optimal performance:

* Do not start checking enrollment until the device data collection is complete.
* Notifiy cardholders to contact their bank for instructions if a problem occurs. Information about additional action required of the cardholder should be displayed on the checkout page. Providing instructions to the customer avoids multiple attempts to resubmit the same card.
  {#concept_b5y_3sl_xpb_ul_jt5_dkq_fyb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Request Fields {#concept_qph_nsl_xpb}
=====================================

The consumerAuthenticationInformation.referenceId field is mapped from the consumerAuthenticationInformation.referenceId field as discussed in [Step 1: Setup Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-setup-intro.md "").  
The consumerAuthenticationInformation.returnUrl value is set to the URL to which the issuing bank redirects the customer as discussed in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "").  
To request the Check Enrollment service, you must send the encrypted payment data or a token or some other equivalent of card data used by your integration. The request fields can include any of these:

* paymentInformation.card.number
* paymentInformation.fluidData.descriptor
* paymentInformation.fluidData.value
* paymentInformation.customer.customerID
* tokenInformation.transientToken

{#concept_qph_nsl_xpb_ul_efg_y22_gqb}  
These fields are required (merchant ID is in the header):

* buyerInformation.mobilePhone (if no other phone number is available)
* buyerInformation.workPhone (if no other phone number is available)
* consumerAuthenticationInformation.referenceId
* consumerAuthenticationInformation.returnUrl
* deviceInformation.ipAddress
* orderInformation.amountDetails.currency
* orderInformation.amountDetails.totalAmount
* orderInformation.billTo.address1
* orderInformation.billTo.administrativeArea
* orderInformation.billTo.country
* orderInformation.billTo.email
* orderInformation.billTo.firstName
* orderInformation.billTo.lastName
* orderInformation.billTo.phoneNumber (if no other phone number is available)
* orderInformation.billTo.postalCode
* paymentInformation.card.expirationMonth
* paymentInformation.card.expirationYear
* paymentInformation.card.cardType
* paymentInformation.card.number

{#concept_qph_nsl_xpb_ul_efx_s1g_hqb}  
You can send additional request data to reduce your issuer step-up authentication rates. Send all available fields. As a backup, if device data collection fails, include the 11 device information fields listed among the optional fields for the Check Enrollment service in your request. If a failure does occur, adding these device information fields ensures a transaction is not downgraded. If you do not have data for a field, do not send dummy data.  
The size of the step-up iframe discussed in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "") can vary depending on the EMV `3-D Secure` version of the transaction. You can request the size of the challenge window in the consumerAuthenticationInformation.acsWindowSize request field.  
Requesting a specific window size does not guarantee this size. Parsing the PAReq as described in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "") determines the actual size.  
For further details on individual API fields, refer to the *[API Field Reference Guide](https://docs.cybersource.com/en/reference/api-fields.md "")*. The field values should use the ISO 3166-2 format.

Interpreting the Check Enrollment Response {#concept_hsh_xnm_xpb}
=================================================================

It is important to check the status values in the response. These possible statuses are the same for all card types.

PENDING_AUTHENTICATION
----------------------

* VERes enrolled = `Y`
* PARes status = `C`

{#concept_hsh_xnm_xpb_ul_pkx_g14_qxb}  
The account number is enrolled in payer authentication. The cardholder is challenged to authenticate. Authenticate the cardholder before authorizing the transaction.

AUTHENTICATION_SUCCESSFUL {#concept_hsh_xnm_xpb_section_qt5_r3x_mxb}
--------------------------------------------------------------------

**Frictionless authentication was successful/Stepup authentication is not required.**

* VERes enrolled = `Y`
* PARes status = `Y`

{#concept_hsh_xnm_xpb_ul_r2j_h14_qxb}  
The account is enrolled in payer authentication, and the cardholder was successfully authenticated. If enrollment and authorization are made in separate calls, the payer authentication data must be included in the authorization request to receive liability shift protection.

Attempt Stand-in Frictionless Authentication
--------------------------------------------

* VERes enrolled = `Y`
* PARes status = `A`

{#concept_hsh_xnm_xpb_ul_drt_h14_qxb}  
This status indicates that the account is enrolled in payer authentication, but the issuer does not support the program. This is called*stand-in authentication*. If check enrollment and authorization are made in separate calls, the payer authentication data must be included in the authorization request to receive liability shift protection.

Card Not Enrolled
-----------------

* VERes enrolled = `B` or `U`

{#concept_hsh_xnm_xpb_ul_x43_314_qxb}  
This status indicates that the account is not eligible for a payer authentication program, authentication was bypassed, or an error or timeout occurred. If enrollment and authorization are made in separate calls, you can request authorization, but there is no liability shift protection.

Unavailable Frictionless Authentication
---------------------------------------

* VERes enrolled = `Y`
* PARes status = `U`

{#concept_hsh_xnm_xpb_ul_jwy_j14_qxb}  
This status indicates that the account is enrolled in payer authentication, but authentication is currently unavailable. The merchant can attempt to retry authentication or proceed with authorization. If enrollment and authorization are made in separate calls, you can continue and request authorization, but there is no liability shift protection. Without authentication of the customer, the merchant remains liable for any chargeback.

AUTHENTICATION_FAILED
---------------------

Failed Frictionless Authentication
----------------------------------

* VERes enrolled = `Y`
* PARes status = `N`

{#concept_hsh_xnm_xpb_ul_dv1_d14_qxb}  
This status indicates that the account is enrolled in payer authentication but frictionless authentication failed. Merchants cannot submit this transaction for authorization. Instead, ask for another form of payment.

Rejected Frictionless Authentication
------------------------------------

* VERes enrolled = `Y`
* PARes status = `R`

{#concept_hsh_xnm_xpb_ul_xzs_k14_qxb}  
This status indicates that the account is enrolled in payer authentication but frictionless authentication was rejected by the issuing bank without requiring a challenge. Merchants cannot submit this transaction for authorization. Instead, ask for another form of payment. When an AUTHENTICATION_FAILED status occurs, the merchant should display a message from the card issuer to the cardholder using the consumerAuthenticationInformation.cardholderMessage field. The text of the message is provided by the ACS/issuer during a frictionless or decoupled transaction to convey information to the cardholder. An message example might be, "Additional authentication is needed for this transaction, contact (issuer name) at xxx-xxx-xxxx." An example of the entry that would appear in the log for such an occurrence is: "cardholderInfo":"You cannot complete this purchase right now. For help, call CommBank at (111) 555-2222"

Important Response Fields {#concept_gbw_pqm_xpb}
================================================

When you receive a `PENDING_AUTHENTICATION` response, you also receive these fields:

* consumerAuthenticationInformation.stepUpUrl discussed in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "").
* consumerAuthenticationInformation.accessToken discussed in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "").

{#concept_gbw_pqm_xpb_ul_ozw_frm_xpb}  
These fields contain values that are used in the Step-Up service, which runs when a customer is challenged to authenticate.

Step 4: Step-Up Iframe {#pa2-ccdc-stepup-frame-intro}
=====================================================

Initiate step-up authentication on the front end after you receive the response as discussed in [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md ""). Note that frictionless authentication does not require this step-up iframe step. This step is only for step-up authentication when the issuing bank wants to challenge the cardholder.  
When a challenge is needed to prove a customer's identity, a JSON Web Token is returned to you that contains a step-up URL. You open an iframe where the access token to the step-up URL (also known as the endpoint) is posted. The iframe must be sized appropriately to enable the cardholder to complete the challenge. The iframe manages customer interaction with the card-issuing bank's access control server. The bank asks the customer to provide identifying information. Once the customer completes the challenge, the process moves to validating the information that the customer sent.

#### Figure: {#pa2-ccdc-stepup-frame-intro_fp_pzj_ldc}

Process Flow for Step-Up Authentication ![Process Flow Diagram for Step-up Authentication](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-auth-3.svg/jcr:content/renditions/original)

Best Practices
--------------

These practices should be followed for this step to achieve optimal performance and to minimize potential operating issues.

* When a transaction requires a challenge, according to EMVCo protocol, the challenge must be issued within 30 seconds of the Enrollment Check response. When more than 30 seconds elapses, the ACS times out.
  {#pa2-ccdc-stepup-frame-intro_ul_tzy_l2q_fyb}

Building the Iframe Parameters {#concept_s11_vrm_xpb}
=====================================================

The iframe that you display should be sized to enable the customer bank to exchange authentication information between itself and the customer. Because a bank can use various methods to authenticate, the iframe has four size options. The bank will request that you ensure that the iframe size provides room to display the bank logo and the card network being used, the amount of the transaction, and a brief explanation of what the customer needs to do. You manage the size of the challenge window to ensure that the challenge window matches with your presentation screen. You choose the iframe parameters and pass the window size to the issuer.

* Use the JWT POST Parameter value from the consumerAuthenticationInformation.accessToken response field and do a form POST within the iframe to the step up Url value that is passed by the consumerAuthenticationInformation.stepUpUrl response field.
* MD POST Parameter: Merchant-defined data returned in the response. This field is optional.
* Iframe height and width: EMV `3-D Secure` 2.x offers multiple size options:
  * Use the consumerAuthenticationInformation.acsWindowSize request field to request a specific window size.
  * Use the consumerAuthenticationInformation.pareq response field to determine iframe dimensions by Base64 decoding the string and cross-referencing a Challenge Window Size value with its corresponding size.
    {#concept_s11_vrm_xpb_ul_y1h_ssm_xpb}

{#concept_s11_vrm_xpb_ul_bzt_zrm_xpb}  
This table lists the possible values for iframe size and the sizes associated with the value.

| Challenge Window Size Value | Step-Up Iframe Dimensions (Width x Height in pixels) |
|:----------------------------|:-----------------------------------------------------|
| 01                          | 250 x 400                                            |
| 02                          | 390 x 400                                            |
| 03                          | 500 x 600                                            |
| 04                          | 600 x 400                                            |
| 05                          | Full screen                                          |
[Challenge Window Size Value and Corresponding Size]

This is an example for the decoded value.
**Challenge Window Size Decoded Value**

```
{
    "messageType":"CReq","messageVersion":"2.2.0",
    "threeDSServerTransID":"c4b911d6-1f5c-40a4-bc2b-51986a98f991",
    "acsTransID":"47956453-b477-4f02-a9ef-0ec3f9f779b3",
    "challengeWindowSize":"02"
}                            
```

Creating the Iframe {#reference_wpq_stm_xpb}
============================================

Create an iframe that is the same size as the Challenge Window Size to send a POST request to the step-up URL. Study this example.  
**Send a POST Request to the Step-Up URL**

```
&lt;iframe name=”step-up-iframe" height="400" width="400"&gt;&lt;/iframe&gt;
&lt;form id="step-up-form" target=”step-up-iframe" method="post" action=" https://centinelapistag. cardinalcommerce.com/V2/Cruise/StepUp"&gt; &lt;input type="hidden" name="JWT" value="eyJhbGciOiJIUz I1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmNmFmMTRmOS04YWRjLTRiNzktOGVkYS04YWVlMTI2NTkzZTEiLCJp YXQiOjE1OTYwNTEyNzYsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTU5NjA1NDg3NiwiT3Jn VW5pdElkIjoiNTVlZjNmNTZmNzIzYWE0MzFjOTlkNTRiIiwiUGF5bG9hZCI6eyJBQ1NVcmwiOiJodHRwczovLzBt ZXJjaGFudGFjc3N0YWcuY2FyZGluYWxjb21tZXJjZS5jb20vTWVyY2hhbnRBQ1NXZWIvY3JlcS5qc3AiLCJQYXlsb2 FkIjoiZXlKdFpYTnpZV2RsVkhsd1pTSTZJa05TWlhFaUxDSnRaWE56WVdkbFZtVnljMmx2YmlJNklqSXVNaTR3SWl3 aWRHaHlaV1ZFVTFObGNuWmxjbFJ5WVc1elNVUWlPaUpsTkdKaVpqazNNeTFqTW1FeUxUUTNOREF0T1RWak5 DMWpNVGhoTVRNeE16TmlPRFFpTENKaFkzTlVjbUZ1YzBsRUlqb2lNVGMzT0RFM016SXROREk1TVMwME1HUmlMVG xoTkRndE1ESm1OREpoTlRZd1lqYzVJaXdpWTJoaGJHeGxibWRsVjJsdVpHOTNVMmw2WlNJNklqQXlJbjAiLCJUcm Fuc2FjdGlvbklkIjoiQnh5a0hYVEp4M1JuNHBGWnF1bjAifSwiT2JqZWN0aWZ5UGF5bG9hZCI6dHJ1ZSwiUmV0 dXJuVXJsIjoiaHR0cHM6Ly9taWNoYWVsdGF5bG9yLmlvL2N5YnMvc3RvcmVEZW1vL3B1YmxpYy9saXN0ZW5lci5 weSJ9.H8j-VYCJK_7ZEHxGz82_IwZGKBODzPaceJNNC99xZRo" /&gt; &lt;input type="hidden" name="MD" value="optionally_include_custom_data_that_will_be_returned_as_is”/&gt; &lt;/form&gt;
                
            
```

Invoking the Iframe {#reference_ymr_35m_xpb}
============================================

Add JavaScript to invoke the iframe form POST. Place the JavaScript after the closing `&lt;/body&gt;` tag as shown in the example below. The JavaScript invokes the iframe form POST automatically when the window loads. While you can submit the form at a different time, you must submit the form before requesting the validation service.

```
&lt;script&gt;
window.onload = function() {   
    var stepUpForm = document.querySelector('#step-up-form');
    if(stepUpForm) // Step-Up form exists
    stepUpForm.submit();
}
&lt;/script&gt;                           
```

Receiving the Step-Up Results {#concept_nng_lvm_xpb}
====================================================

After the customer interacts with the issuing bank, the customer is returned to the consumerAuthenticationInformation.returnUrl within the iframe as specified in [Step 3: Payer Authentication Check Enrollment Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-enroll-intro.md ""). Since you host the return URL, you can then close the iframe after redirection.  
The response sent back to the return URL contains these values:

* Transaction ID: (consumerAuthenticationInformation.authenticationTransactionId response field). This value is used in [Step 5: Payer Authentication Validation Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-validate-intro.md "").
* MD: merchant data returned if present in the POST to step-up URL; otherwise, null.

{#concept_nng_lvm_xpb_ul_k3v_mvm_xpb} **POST to Return URL**

```
TransactionId=BwNsDeDPsQV4q8uy1Kq1&MD=null                            
```

Step 5: Payer Authentication Validation Service {#concept_p5s_cwm_xpb}
======================================================================

When you receive the step-up response as discussed in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md ""), verify that the customer was successfully authenticated. Note that frictionless authentication does not require this validation step. Validation is required only for step-up authentication.

#### Figure: {#concept_p5s_cwm_xpb_fi_ldc}

Process Flow for Validation of the Cardholder ![Process Flow Diagram for Validation of the Payer](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-validation-3.svg/jcr:content/renditions/original)

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-results`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-results`

Request Fields {#concept_sxk_hwm_xpb}
=====================================

The consumerAuthenticationInformation.authenticationTransactionId field in this step is mapped from the consumerAuthenticationInformation.authenticationTransactionId field in [Step 4: Step-Up Iframe](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-ccdc-stepup-frame-intro.md "").  
These fields are required:

* clientReferenceInformation.code
* consumerAuthenticationInformation.authenticationTransactionId
* orderInformation.amountDetails.currency
* orderInformation.amountDetails.total Amount or orderInformation.lineItems.unitPrice
* paymentInformation.card.expirationMonth
* paymentInformation.card.expirationYear
* paymentInformation.card.number
* paymentInformation.card.type

{#concept_sxk_hwm_xpb_ul_s5p_wnk_tyb}  
For examples, see [Validating a Challenge](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-cases-intro/pa2-use-validate-intro.md "").  
For further details on individual API fields, refer to the *[API Field Reference Guide](https://docs.cybersource.com/en/reference/api-fields.md "")*.

Interpreting the Validation Response {#pa2-ccdc-validate-interpreting-response}
===============================================================================

If the authentication is rejected (TransStatus R), Relay, China UnionPay, Elo, JCB, Diners Club, Discover, and American Express recommend not proceeding to authorization. Instead, ask the customer to use another payment method.  
Proceed with the order according to the validation response that you receive. The possible validation response statuses are the same for all of the card types.

AUTHENTICATION_SUCCESSFUL
-------------------------

**Successful Step-Up Authentication**

* PARes status = `Y`

{#pa2-ccdc-validate-interpreting-response_ul_qpp_m14_qxb}  
Step-up authentication of the customer was successful. If you request the Validate Authentication and Authorization services separately, you must add the required payer validate payload values to your authorization request before you can receive chargeback protection that shifts the liability to the issuer.  
**Unavailable Step-up Authentication**

* PARes status = `U`

{#pa2-ccdc-validate-interpreting-response_ul_lwx_m14_qxb}  
Step-up authentication was unavailable and the customer could not be authenticated. This status does not necessarily indicate any fraudulent intent from the customer. Merchants can either attempt to retry authentication or continue to authorization. If you are making separate validatation and authorization calls, you can still proceed with the authorization request but there is no liability shift. Without authentication, the merchant remains liable for any chargeback if it should occur with the transaction.

AUTHENTICATION_FAILED
---------------------

**Unavailable Step-up Authentication**
* PARes status = `N`
  {#pa2-ccdc-validate-interpreting-response_ul_e2h_n14_qxb}  
  The customer could not be authenticated. Do not submit this transaction for authorization. Instead ask the customer for another form of payment.  
  **Error**  
  If you receive an error from the payment card company, process the order according to your business rules. If the error occurs frequently, report it to customer supportcustomer supportcustomer support. If you receive a system error, determine the cause of the error and proceed with card authorization only when appropriate.

Redirecting Customers to Pass or Fail Message Page {#concept_tzt_yjx_wpb}
=========================================================================

After authentication is complete, redirect the customer to a page containing a success or failure message. You must ensure that the messages that display to customers are accurate and complete, and that the message addresses all possible scenarios for enrolled and non-enrolled cards. For example, if the authentication fails, display a message such as this to the customer:

```
Authentication Failed
Your card issuer cannot authenticate this card. Please select another card or form of payment to complete your purchase.
```

Combining the Authentication and the Authorization Services {#concept_zz1_s5l_xpb}
==================================================================================

After the customer is successfully authenticated, you must get authorization from the issuing bank to proceed with the transaction. While these are separate processes, it is recommended that you link these services by immediately passing the returned values into a request to authorize the transaction. The two services can be linked when:

* Checking enrollment determines that no challenge is required. Pass the values returned from checking enrollment to the authorization request.
* Validating a challenge authenticates the cardholder. Pass the values returned from validating the challenge to the authorization request.

{#concept_zz1_s5l_xpb_ul_q1p_yw3_4yb}  
With the same request transactions, a different endpoint must be referenced for the authorization, and an additional element must be added to the JSON. When step-up authentication is required, transaction processing stops to allow completion of authentication, and authorization is not called until after the challenge response is validated. This integration method is recommended.  
Depending on your card type, you might not receive the XID value. If you receive this field under a frictionless scenario, it is required for authorization.

Combining Check Enrollment and the Authorization Services {#pa2_ccdc_combining_services_enroll}
===============================================================================================

Receiving certain responses from checking enrollment allows the authorization to be requested immediately afterwards. The possible checking enrollment responses are:

* Successful frictionless authentication
* Attempted stand-in frictionless authentication
* Issuer does not support the payer authentication program
* Account is not eligible for a payer authentication program
* Unavailable frictionless authentication
* Failed frictionless authentication
* Rejected frictionless authentication

{#pa2_ccdc_combining_services_enroll_ul_i1x_w24_pyb}  
In all checking enrollment scenarios, it is recommended that you integrate these services by combining the checking enrollment and authorization services into a single transaction. When the services are combined, one of these conditions occurs:

* No additional integration work is required to manually map the appropriate check enrollment results to the corresponding authorization request fields.
* If further authentication is needed, the authorization cannot happen until after authentication completes and you can proceed to the next steps for challenging.

{#pa2_ccdc_combining_services_enroll_ol_hqh_cf4_pyb}  
With same request transactions, a different endpoint must be referenced for the authorization, and an additional element must be added to the JSON. Depending on your card type, you might not receive the XID value. If you receive this field under a frictionless scenario, it is required for authorization.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Check Enrollment Response Fields and Their Equivalent Authorization Request Fields {#pa2-ccdc-combining-mapping-check-enroll-auth-fields}
=========================================================================================================================================

When a customer is authenticated without a challenge, the transaction can be authorized either in the same request or in a separate authorization request. Whether authorization occurs in the same request or a separate request, the values from the check enrollment response must be passed to the authorization request to qualify for a liability shift. This table matches the check enrollment fields with their equivalent authorization fields. Sometimes a check enrollment response field is the same field used in the authorization request.  
Be sure to include the following card-specific information in your authorization request:

* For Relay, JCB, China UnionPay, Elo,Diners Club, Discover, and American Express include the *CAVV*.
* For Mastercard only, include the collection indicator and the *AAV* (also known as *UCAF*).

{#pa2-ccdc-combining-mapping-check-enroll-auth-fields_ul_hyb_lvz_pyb}

| Identifier                                                               | Enrollment Check Response Field                                  | Card Authorization Request Field                                |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------|
| E-commerce indicator                                                     | consumerAuthenticationInfo rmation.ecommerceIndicator            | processingInformation.commerceIndicator                         |
| Collection indicator                                                     | consumerAuthenticationInfo rmation.ucafCollectionIndicator       | consumerAuthenticationInfo rmation.ucafCollectionIndicator      |
| CAVV                                                                     | consumerAuthenticationInformation.cavv                           | consumerAuthenticationInfo rmation.cavv                         |
| AAV                                                                      | consumerAuthenticationInfo rmation.ucafAuthentication Data       | consumerAuthenticationInfo rmation.ucafAuthentication Data      |
| XID                                                                      | consumerAuthenticationInformation.xid                            | consumerAuthenticationInfo rmation.xid                          |
| Result of the enrollment check for Asia, Middle East, and Africa Gateway | consumerAuthenticationInfo rmation.veresEnrolled                 | consumerAuthenticationInfo rmation.veresEnrolled                |
| `3-D Secure` version                                                     | consumerAuthenticationInfo rmation.specificationVersion          | consumerAuthenticationInfo rmation.paSpecificationVersion       |
| Directory server transaction ID                                          | consumerAuthenticationInfo rmation.directoryServerTran sactionId | consumerAuthenticationInfo rmation.directoryServerTransactionId |
[Enrollment Check and Response Fields]

Combining the Validation and the Authorization Services {#pa2-ccdc-combining-services-valid}
============================================================================================

After the customer is successfully authenticated, you must get authorization from the issuing bank to proceed with the transaction. While these are separate processes, you should integrate these two services into a single process whenever possible. When you do so, no additional integration work is required on your part to manually map the appropriate validation results to corresponding authorization request fields.  
With the same request transactions, a different endpoint must be referenced for the authorization, and an additional element must be added to the JSON. When step-up authentication is required, transaction processing stops to allow authentication to complete, and authorization is not called until after the challenge response is validated. This integration method is highly recommended. Depending on your card type, you might not receive the XID value. If you receive this field under a frictionless scenario, it is required for authorization.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`

Validation Fields and their Equivalent Authorization Fields {#pa2-ccdc-combining-map-validate-auth-fields}
==========================================================================================================

When a customer is authenticated after a challenge, the transaction can be authorized in the same request or in a separate authorization request. Whether authorization is combined with validation or occurs in a separate request, the values from the validation response must be passed to the authorization request to qualify for a liability shift to the issuing bank. This table pairs the Validation field with its equivalent Authorization API field.  
Be sure to include the following card-specific information in your authorization request:

* For Relay, JCB, China UnionPay, Elo, Diners Club, Discover, and American Express include the CAVV.
* For Mastercard only, include the collection indicator and the AAV (also known as UCAF).

{#pa2-ccdc-combining-map-validate-auth-fields_ul_hyb_lvz_pyb}

|           Identifier            |                 Validation Check Response Field                 |                Card Authorization Request Field                 |
|---------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| E-commerce indicator            | consumerAuthenticationInforma tion.indicator                    | processingInformation.com merceIndicator                        |
| Collection indicator            | consumerAuthenticationInforma tion.ucafCollectionIndicator      | consumerAuthenticationInfo rmation.ucafCollectionIndicator      |
| CAVV                            | consumerAuthenticationInforma tion.cavv                         | consumerAuthenticationInfo rmation.cavv                         |
| AAV                             | consumerAuthenticationInforma tion.ucafAuthenticationData       | consumerAuthenticationInfo rmation.ucafAuthentication Data      |
| XID                             | consumerAuthenticationInforma tion.xid                          | consumerAuthenticationInfo rmation.xid                          |
| `3-D Secure` version            | consumerAuthenticationInforma tion.specificationVersion         | consumerAuthenticationInfo rmation.paSpecificationVersion       |
| Directory server transaction ID | consumerAuthenticationInforma tion.directoryServerTransactionId | consumerAuthenticationInfo rmation.directoryServerTransactionId |
[Validation Check and Response Fields]

Implementing SDK Payer Authentication {#concept_ycl_lny_wpb}
============================================================

This chapter summarizes the process of integrating SDK Payer Authentication services into your mobile application. Payer authentication services use the Mobile SDK for iOS or Android to facilitate the authentication. New SDK versions are frequently released and you should ensure that you stay current with the latest release. One way to stay informed on about new releases is to subscribe to a distribution list to be informed of updates and other product announcements. You can subscribe by going to this link: [Cardinal SDK Notifications](https://win.cardinalcommerce.com/CardinalMobileSDKNotifications "").  
Implementing the SDK in your mobile application requires either Android or iOS platform application programming skills. Android API 21 or iOS 9 and XCode 8 are required.  
The SDK is only designed to handle EMV `3-D Secure` 2.x transactions.

Implementation Overview {#concept_knf_xny_wpb}
==============================================

Notify your account representative that you want to implement payer authentication (EMV `3-D Secure`). Give the representative the merchant ID that you will use for testing. For more information, see [Payer Authentication Merchant Workflow](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-intro-intro/pa2-intro-process-overview.md "").  
IMPORTANT The SDK integration operates in a similar manner to the Direct API integration, but SDK does not have a Setup service step.  
Implementation tasks include:

* Download, import, and configure the Mobile SDK for either iOS or Android.
* For each purchase request:
  * Build the authentication request.
  * Invoke the authentication.
  * Handle declines.
  * Make another back-end, server-to-server call to request these services:  
    : Payer Authentication Validation  
    : Card Authorization service (optional)
    {#concept_knf_xny_wpb_ul_n3m_s1z_wpb}
* Use the test cases to test your preliminary code and make appropriate changes. See [Testing Payer Authentication](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-testing-intro.md "").
* Ensure that your account is configured for production.

{#concept_knf_xny_wpb_ul_h4z_hqy_wpb}  
Note that calling the Payer Authentication Setup Service is not required with the SDK mobile version.

Process Flow for SDK Integration {#concept_uwx_ncz_wpb}
=======================================================

The steps required to integrate payer authentication into an SDK mobile application are described below.

1. Contact customer support to register for an API key.
2. Download and import the Mobile SDK for either iOS or Android.
3. Set up your build environment.
4. Configure your SDK.
5. Setup the initial request to Cardinal.
6. Create an API request to your merchant server to request the Enrollment Check service, passing in transaction details and the consumerAuthenticationInformation.referenceId request field.
7. If the issuing bank does not require authentication, you receive this information in the Enrollment Check response:
   * E-commerce indicator (consumerAuthenticationInformation.ecommerceIndicator)
   * CAVV (all card types except Mastercard) (consumerAuthenticationInformation.cavv)
   * AAV (Mastercard only) (consumerAuthenticationInformation.ucafCollectionIndicator)
   * Transaction ID (consumerAuthenticationInformation.xid )
   * `3-D Secure` version (consumerAuthenticationInformation.specificationVersion)
   * Directory server transaction ID (consumerAuthenticationInformation.directoryServerTransactionId)
     {#concept_uwx_ncz_wpb_ul_tl4_22z_wpb}
8. If the issuing bank requires authentication, you receive a response with the payload and the transaction ID that you include in the *Cardinal.continue* call from your SDK.
9. The Mobile SDK displays an authentication window, and the customer enters the authentication information into that window.
10. The bank validates the customer credentials and a JSON Web Token (JWT) is returned by the SDK in the onValidated callback that the merchant is required to validate server-side for security reasons.
11. Create an API call to your merchant server to request the Validate Authentication service, extracting the processor transaction ID value from the JWT and sending it in the consumerAuthenticationInformation.authenticationTransactionId request field. You receive the e-commerce indicator, CAVV or AAV, transaction ID, `3-D Secure` version, and directory server transaction ID.

{#concept_uwx_ncz_wpb_ol_xm1_tcz_wpb}  
Verify that the authentication was successful and continue processing your order.  
You must pass all pertinent data for the card type and processor in your authorization request. For more information, see [Requesting the Validation Service](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-sdk-intro/pa-sdk-implementing-sdk-pa/pa-sdk-implementing-request-validation.md "").

Prerequisites for SDK Implementation {#concept_y4k_qbz_wpb}
===========================================================

Before you can implement payer authentication services, your business team must contact your acquirer and `Cybersource` to establish the service. Your software development team should become familiar with the API fields and technical details of this service.  
Creating a mobile application with the SDK implementation, requires that you perform some preliminary procedures before the starting the actual payer authentication implementation process. These processes involving JWTs are described in this section.

Credentials/API Keys {#concept_ql2_wwk_bqb}
===========================================

API keys are required to create the JSON Web Token (JWT). For further information, contact [customer support](http://support.example.com "") .  
You will receive an email with your username and a temporary password. Your username will be in this format:  
`cybersource_merchant name_contact name`  
For example:  
`cybersource_petairways_peter`  
Once you receive your credentials, log in to your JFrog account and update your temporary password. Follow the process below to generate your API key.

Generating your API Key: {#task_m22_5hl_2qb}
============================================

1. Log in to your JFrog account.
2. In the top-right of the JFrog Platform, select the Welcome drop-down menu and click Edit Profile.
3. Enter your password and click Unlock.
4. Under Authentication Settings, click Generate API Key.

Mobile Device Data Collected {#concept_mky_31r_tyb}
===================================================

One of the key components to authenticating a cardholder during an online transaction is to compare information about the mobile device that the buyer is using to the information about mobile devices that the buyer used in past transactions. This information is maintained in the access control server (ACS) at the issuing bank.  
In mobile device transactions, information collected about the buyer device can include:

* Device ID
* Device model
* Operating system version
* System language
* Country
* Time zone
* Screen dimensions

{#concept_mky_31r_tyb_ul_hld_5br_tyb}  
A successful device data collection process that includes the eleven browser fields listed in the check enrollment step, increases the chances of a frictionless authentication. The decision to escalate a transaction to a level of risk high enough to require challenging the buyer to authenticate their identity is managed by business rules that are configured in the issuer's risk analysis software that evaluates each transaction.

Using the Android SDK {#concept_efq_v1c_fqb}
============================================

A mobile SDK is available for integrating payer authentication services into mobile applications running on the Android platform.

Updating the Gradle Build Properties {#reference_lrk_l5d_xpb}
=============================================================

In Android Studio, open the app directory (which can also be labeled Module: app) and open the *build.gradle* file. Edit the Gradle file located in the app directory. Add the contents shown in the example below to the Gradle file.

```
repositories {
   ...
   maven {
           url  "https://cardinalcommerceprod.jfrog.io/artifactory/android"
           credentials {
                   username Artifactory username
                   password Artifactory user API Key
            }
    }
}
dependencies {
    ...
    //Cardinal Mobile SDK
    implementation 2.5-1
}                
        
```

If your project uses Progurad, add the lines shown below to the *proguard-rules.pro* file.

```
-keep class com.cardinalcommerce.dependencies.internal.bouncycastle.**
-keep class com.cardinalcommerce.dependencies.internal.nimbusds.**
    
```

Configuring the Android SDK {#reference_hrm_syd_xpb}
====================================================

Get the instance of the Cardinal object by running the *Cardinal.getInstance()* process. Use the default configuration options. See the example below to understand how to run the *Cardinal.configure()* process.  
For more details on configuration, refer to the configuration options table after the example.

```
private Cardinal cardinal = Cardinal.getInstance();
@Override
protected void onCreate(Bundle savedInstanceState) {

CardinalConfigurationParameters cardinalConfigurationParameters = new CardinalConfigurationParameters();
        cardinalConfigurationParameters.setEnvironment(CardinalEnvironment.STAGING);
        cardinalConfigurationParameters.setTimeout(8000);
        JSONArray rType = new JSONArray();
        rType.put(CardinalRenderType.OTP);
        rType.put(CardinalRenderType.SINGLE_SELECT);
        rType.put(CardinalRenderType.MULTI_SELECT);
        rType.put(CardinalRenderType.OOB);
        rType.put(CardinalRenderType.HTML);
        cardinalConfigurationParameters.setRenderType(rType);

        cardinalConfigurationParameters.setUiType(CardinalUiType.BOTH);

        UiCustomization yourUICustomizationObject = new UiCustomization();
cardinalConfigurationParameters.setUICustomization(yourUICustomizationObject);

        cardinal.configure(this,cardinalConfigurationParameters);
}          
```

| Method                                                                                 | Description                                                                                                                          | Default Values                                                                                                                                                                                                                             |
|:---------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| setEnableDFSync (boolean enableDFSync)                                                 | On setting true, onSetupCompleted is called after the collected device data is sent to the server.                                   | False                                                                                                                                                                                                                                      |
| setEnableQuickAuth (boolean enableQuickAuth)                                           | Sets enable quick auth false.                                                                                                        | False                                                                                                                                                                                                                                      |
| setEnvironment(Setting up mobile SDK - Android- V 2.1#CardinalEnvironment environment) | Sets the environment to which the SDK must connect.                                                                                  | CardinalEnvironment. PRODUCTION                                                                                                                                                                                                            |
| setProxyAddress(java.lang. String proxyAddress)                                        | Sets the proxy to which the SDK must connect.                                                                                        | " "                                                                                                                                                                                                                                        |
| setRenderType(org.json. JSONArray renderType)                                          | Sets renderLists all user interface types that the device supports for displaying specific challenge user interfaces within the SDK. | JSONArray rType = new JSONArray(); rType.put(Cardinal RenderType.OTP); rType.put(Cardinal RenderType.SINGLE_SELECT); rType.put(Cardinal RenderType.MULTI_SELECT); rType.put(Cardinal RenderType.OOB); rType.put(Cardinal RenderType.HTML); |
| setTimeout(int timeout)                                                                | Sets the maximum amount of time (in milliseconds) for all exchanges.                                                                 | 8000                                                                                                                                                                                                                                       |
| setUICustomization (UiCustomization UI Customization)                                  | Sets UICustomization                                                                                                                 | Device Default Values                                                                                                                                                                                                                      |
| setUiType(CardinalUiType uiType)                                                       | Sets all user interface types that the device supports for displaying specific challenge user interfaces within the SDK.             | CardinalUiType.BOTH                                                                                                                                                                                                                        |
[Android Configuration Options]

Setting Up the Initial Request {#reference_usw_hb2_xpb}
=======================================================

Run the *Cardinal.init()* process to:

* Begin the communication process with Cardinal.
* Authenticate your credentials (server JWT).
* Complete the data collection process.

{#reference_usw_hb2_xpb_ul_zns_dwc_fwb}  
By the time the customer is ready to check out, all necessary preprocessing is complete.  
Each time a user begins a mobile transaction, Cardinal assigns a unique identifier to the consumer session called a consumerSessionId. This consumerSessionId ensures that Cardinal matches the correct device data collection results to a request. `Cybersource` calls this session identifier payerAuthEnrollService_referenceID. You must assign the value of the consumerSessionId field to the payerAuthEnrollService_referenceID field so that `Cybersource` can also track the calls for each user session.  
Study the code example shown below for completing the *cardinal.init()* process. Cardinal.init() (Android SDK)

```
cardinal = Cardinal.getInstance();
String serverJwt = "INSERT_YOUR_JWT_HERE";
cardinal.init(serverJwt ,
new CardinalInitService() {
    /**
    * You may have your Submit button disabled on page load. Once you are 
    * set up for CCA, you may then enable it. This will prevent users 
    * from submitting their order before CCA is ready.
    */
    @Override
    public void onSetupCompleted(String consumerSessionId) {
  
    }
    /**
    * If there was an error with set up, Cardinal will call this function
    * with validate response and empty serverJWT
    * @param validateResponse
    * @param serverJwt will be an empty
    */
    @Override
    public void onValidated(ValidateResponse validateResponse, String serverJwt) {
  
    }
});
```

See [Running Payer Authentication with SDK](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-sdk-intro/pa-sdk-implementing-sdk-pa.md "") for the next steps.

Using the iOS SDK {#concept_blv_1bc_fqb}
========================================

A mobile SDK is available for integrating payer authentication services into mobile applications running on the iOS platform.

Downloading and Importing the SDK {#reference_h5r_rr2_xpb}
==========================================================

Download the *CardinalMobile.framework* file using the cURL program in this example.  
Download CardinalMobile.framework

```
curl -L -u &lt;USER_NAME&gt;
        :&lt;API_KEY&gt; https://cardinalcommerceprod.jfrog.io/artifactory/ios/&lt;VERSION&gt;-&lt;BUILD_NUMBER&gt;/cardinalmobilesdk.zip
        -o &lt;LOCAL_FILE_NAME.EXT&gt;

#Example: 
curl -L -u UserName:ApiKey "https://cardinalcommerceprod.jfrog.io/artifactory/ios/2.2.5-1/cardinalmobilesdk.zip" -o cardinalmobile2.2.5-1.zip                          
```

Download the *CardinalMobile.xcframework* file using the cURL in this example.  
Download CardinalMobile.xcframework

```
curl -L -u &lt;USER_NAME&gt;
        :&lt;API_KEY&gt; https://cardinalcommerceprod.jfrog.io/artifactory/ios/&lt;VERSION&gt;-&lt;BUILD_NUMBER&gt;/CardinalMobileiOSXC.zip
        -o &lt;LOCAL_FILE_NAME.EXT&gt;

#Example: 
curl -L -u UserName:ApiKey "https://cardinalcommerceprod.jfrog.io/artifactory/ios/2.2.5-1/CardinalMobileiOSXC.zip" -o cardinalmobile2.2.5-1.zip
```

In your XCode project, drag the *CardinalMobile.framework* file into the Frameworks group in your Xcode Project. (Create the group if it does not already exist.) In the import dialog box, check the box to Copy items into the destinations group folder (or Destination: Copy items if needed). The iOS SDK files are now available for linking in your project.

Configuring Your Build Environment {#task_bbs_hr2_xpb}
======================================================

Follow these to configure your build environment:

1. Open Xcode, and in the source list to the left of the main editor area, choose your project.
2. Under the Targets section, select your application and open the **General** tab.
3. Expand the Embedded Binaries section and click the small plus (**+**) at the bottom of the list.
4. From the list, add the **CardinalMobile.framework** file.

Configuring the iOS SDK {#reference_sr5_1c2_xpb}
================================================

Use **CardinalSession new** to create a new instance of the cardinal object. Use the default configuration options. Study these examples to complete the iOS SDK configuration.  
For more details on configuration options, refer to the table after the examples.  
CardinalSession new (iOS SDK - Objective-C)

```
#import &lt;CardinalMobile/CardinalMobile.h&gt;

CardinalSession *session;

//Setup can be called in viewDidLoad
- (void)setupCardinalSession {
    session = [CardinalSession new]; 
    CardinalSessionConfiguration *config = [CardinalSessionConfiguration new];
    config.deploymentEnvironment = CardinalSessionEnvironmentProduction;
    config.timeout = CardinalSessionTimeoutStandard;
    config.uiType = CardinalSessionUITypeBoth;

    UiCustomization *yourCustomUi = [[UiCustomization alloc] init];
    //Set various customizations here. See "iOS UI Customization" documentation for detail.
    config.uiCustomization = yourCustomUi;
 
    CardinalSessionRenderTypeArray *renderType = [[CardinalSessionRenderTypeArray alloc] initWithObjects:
                               CardinalSessionRenderTypeOTP,
                               CardinalSessionRenderTypeHTML,
                               nil];
    config.renderType = renderType;
 
    config.enableQuickAuth = false;
    [session configure:config];
}                         
```

CardinalSession new (iOS SDK - Swift)

```
import CardinalMobile

var session : CardinalSession!
 
//Setup can be called in viewDidLoad
func setupCardinalSession{
    session = CardinalSession()
    var config = CardinalSessionConfiguration()
    config.deploymentEnvironment = .production
    config.timeout = 8000
    config.uiType = .both
 
    let yourCustomUi = UiCustomization()
    //Set various customizations here. See "iOS UI Customization" documentation for detail.
    config.uiCustomization = yourCustomUi
 
    config.renderType = [CardinalSessionRenderTypeOTP, CardinalSessionRenderTypeHTML]
    config.enableQuickAuth = true
    session.configure(config)
}   
```

| Method                 | Description                                                                                                             | Default Values                                                                                                                                                                  | Possible Values                                                                                                                                                              |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| deploymentEnviron ment | The environment to which the SDK connects.                                                                              | CardinalSessionEnviron mentProduction                                                                                                                                           | CardinalSession Environment Staging CardinalSessionEnvi ronment Production                                                                                                   |
| timeoutInMilli seconds | Maximum amount of time (in milliseconds) for all exchanges.                                                             | 8000                                                                                                                                                                            |                                                                                                                                                                              |
| uiType                 | Interface types that the device supports for displaying specific challenge user interfaces within the SDK.              | CardinalSessionUIType Both                                                                                                                                                      | CardinalSessionUIT ypeBoth CardinalSessionUIT ypeNative CardinalSessionUIT ypeHTML                                                                                           |
| renderType             | List of all the render types that the device supports for displaying specific challenge user interfaces within the SDK. | \[CardinalSessionRend erTypeOTP, CardinalSessionRend erTypeHTML, CardinalSessionRend erTypeOOB, CardinalSessionRend erTypeSingleSelect, CardinalSessionRend erTypeMultiSelect\] | CardinalSessionRen derType OTP CardinalSessionRen derType HTML CardinalSessionRen derType OOB CardinalSessionRen derType SingleSelect CardinalSessionRen derType MultiSelect |
| proxyServerURL         | Proxy server through which the Cardinal SDK Session operates.                                                           | nil                                                                                                                                                                             |                                                                                                                                                                              |
| enableQuickAuth        | Enable Quick Authentication                                                                                             | false                                                                                                                                                                           |                                                                                                                                                                              |
| uiCustomization        | Set Custom UICustomization for SDK-Controlled Challenge UI.                                                             | nil                                                                                                                                                                             |                                                                                                                                                                              |
| enableDFSync           | Enable DF Sync to get onSetupCompleted called after collected device data is sent to the server.                        | false                                                                                                                                                                           |                                                                                                                                                                              |
[iOS Configuration Options]

Setting Up the Initial Request {#reference_ezk_h1f_xpb}
=======================================================

Requesting the *cardinal session setup* process begins the communication process, authenticates your credentials (server JWT), and completes the data collection process. By the time the customer is ready to check out, all necessary preprocessing is complete.  
Each time a user begins a mobile transaction, a unique value is assigned to the consumerSessionId API field to identify the session. This value ensures that the correct device data collection results are matched to each user request. `Cybersource` uses its payerAuthEnrollService_referenceID field to contain Cardinal's consumerSessionId value. You must assign the value of the consumerSessionId field to the payerAuthEnrollService_referenceID field so that `Cybersource` can also track the requests for each user session.  
Study these code examples to understand how to complete setting up the cardinal session process. The function request must be placed in your Checkout ViewController. Cardinal session setup (iOS SDK - Objective-C)

```
NSString *accountNumberString = @"1234567890123456";
NSString *jwtString = @"INSERT_YOUR_JWT_HERE";
 
[session setupWithJWT:jwtString 
          didComplete:^(NSString * _Nonnull consumerSessionId){
//
    // You may have your Submit button disabled on page load. Once you are 
    // setup for CCA, you may then enable it. This will prevent users 
    // from submitting their order before CCA is ready.
    //
} didValidate:^(CardinalResponse * _Nonnull validateResponse) {
    // Handle failed setup
    // If there was an error with setup, cardinal will call this 
    // function with validate response and empty serverJWT
}];                           
```

Cardinal session setup (iOS SDK - Swift)

```
let accountNumberString = "1234567890123456"
let jwtString = "INSERT_YOUR_JWT_HERE"

session.setup(jwtString: jwtString, completed: { (consumerSessionId: String) in
    //
    // You may have your Submit button disabled on page load. Once you 
    // are setup for CCA, you may then enable it. This will prevent 
    // users from submitting their order before CCA is ready.
    //
}) { (validateResponse: CardinalResponse) in
    // Handle failed setup
    // If there was an error with setup, cardinal will call this 
    // function with validate response and empty serverJWT
}                           
```

Running Payer Authentication with SDK {#concept_u35_4hn_xpb}
============================================================

The payer authentication process in SDK requires checking whether a customer is participating in a card authentication program. If the customer is enrolled in payer authentication, you validate their current status in the program and authorize the transaction. The following procedures describe how to ensure the correct data values are passed during the payer authentication process.

Requesting the Check Enrollment Service (SDK) {#pa-sdk-implementing-sdk-request-check-enrollment}
=================================================================================================

After the SDK completes the device collection from your mobile application, and after the customer clicks the Buy button, you must make a back-end, server-to-server call to request the Enrollment Check service.  
The Check Enrollment service verifies that the card is enrolled in a card authentication program. The merchant ID is included as part of the header, but these fields are required in the request:
* consumerAuthenticationInformation.referenceId

* orderInformation.amountDetails.currency

* orderInformation.amountDetails.totalAmount

* orderInformation.billTo.address1

* orderInformation.billTo.administrativeArea

* orderInformation.billTo.country

* orderInformation.billTo.email

* orderInformation.billTo.firstName

* orderInformation.billTo.lastName

* orderInformation.billTo.locality

* orderInformation.billTo.postalCode

* paymentInformation.card.expirationMonth

* paymentInformation.card.expirationYear

* paymentInformation.card.number

* paymentInformation.card.type
  {#pa-sdk-implementing-sdk-request-check-enrollment_ul_g5b_zbh_hqb}
  IMPORTANT To reduce your issuer step-up authentication rates, you can send additional request data in the order. It is best to send all available fields.  
  Use the enrollment check and card authorization services in the same request or in separate requests:

* Same request: `Cybersource` attempts to authorize the card if your customer is not enrolled in a payer authentication program. In this case, the field values that are required to prove that you attempted to check enrollment are passed automatically to the authorization service. If authentication is required, processing automatically stops.

* Separate requests: Manually include the enrollment check result values (Enrollment Check response fields) in the authorization service request (Card Authorization request fields).

{#pa-sdk-implementing-sdk-request-check-enrollment_ul_nnr_h2f_xpb}  
Be sure to include the following card-specific information in your authorization request:

* For Relay, JCB, China UnionPay, Elo, Diners Club, Discover and American Express include the CAVV.
* For Mastercard only, include the collection indicator and the AAV (also known as UCAF).

{#pa-sdk-implementing-sdk-request-check-enrollment_ul_hyb_lvz_pyb}  
These fields are listed in this table.

| Identifier                                                               | Enrollment Check Response Field                                  | Card Authorization Request Field                                |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------|
| E-commerce indicator                                                     | consumerAuthenticationInfo rmation.ecommerceIndicator            | processingInformation.commerceIndicator                         |
| Collection indicator                                                     | consumerAuthenticationInfo rmation.ucafCollectionIndicator       | consumerAuthenticationInfo rmation.ucafCollectionIndicator      |
| CAVV                                                                     | consumerAuthenticationInfo rmation.cavv                          | consumerAuthenticationInfo rmation.cavv                         |
| AAV                                                                      | consumerAuthenticationInfo rmation.ucafAuthentication Data       | consumerAuthenticationInfo rmation.ucafAuthentication Data      |
| XID                                                                      | consumerAuthenticationInfo rmation.xid and                       | consumerAuthenticationInfo rmation.xid                          |
| Result of the enrollment check for Asia, Middle East, and Africa Gateway | consumerAuthenticationInfo rmation.veresEnrolled                 | consumerAuthenticationInfo rmation.veresEnrolled                |
| `3-D Secure` version                                                     | consumerAuthenticationInfo rmation.specificationVersion          | consumerAuthenticationInfo rmation.paSpecificationVersion       |
| Directory server transaction ID                                          | consumerAuthenticationInfo rmation.directoryServerTran sactionId | consumerAuthenticationInfo rmation.directoryServerTransactionId |
[Enrollment Check and Response Fields]

Interpreting the Response {#concept_eyw_mff_xpb}
================================================

In EMV `3-D Secure`, there are two possible responses:

* Frictionless: No challenge or stepup to the cardholder. While frictionless authentication can indicate a successfully authenticated outcome because the customer's card is enrolled in a payer authentication program, it can also result from the bank failing or rejecting authentication without challenging the cardholder. In the frictionless authentication flow, you receive a PAResStatus of either `Y`, `A`, `N`, `I`, `R`, or `U` with an associated ECI value. With successful frictionless authentication, the PAResStatus = `Y` or `A` and you receive a CAVV. You may also receive a PAResStatus = `I` indicating successful authentication, but it might not include a CAVV.
* Challenge: The response contains PAResStatus = `C`. A challenge response has a payload and contains an ACS URL and a step up URL. Challenge the cardholder to provide additional authentication information and display an authentication challenge window to the cardholder so the cardholder can respond to a validation request and receive a validation response.

Authenticating Enrolled Cards {#concept_ibq_jhf_xpb}
====================================================

In the response from the enrollment check service, confirm that you receive these fields and values:

* `3-D Secure` version = 2.x
* VERes enrolled = Y
* PARes status = C

{#concept_ibq_jhf_xpb_ul_chl_nhf_xpb}  
These values identify whether it is an EMV `3-D Secure` 2.x transaction and that a challenge is required.  
After you validate these fields, you request the *Cardinal.cca_continue* process (Android SDK) or the *Cardinal session continue*process (iOS SDK) for the SDK to perform the challenge between the customer and the issuing bank.

Calling Cardinal.cca_continue (Android SDK) {#reference_rqz_shf_xpb}
====================================================================

After you verify that a customer's card is enrolled in a card authentication program, you must include the payload and the consumerAuthenticationInformation.authenticationTransactionId response field and incorporate them into the*Cardinal.cca_continue* function as shown in this example before proceeding with the authentication session.

```
/**
 * Cca continue.
 *
 * @param transactionId     the transaction id
 * @param payload           the payload
 * @param currentActivity   the current activity
 * @throws InvalidInputException        the invalid input exception
 * @throws JSONException                the json exception
 * @throws UnsupportedEncodingException the unsupported encoding exception
 */
try {
    cardinal.cca_continue("[TRANSACTION ID ]", "[PAYLOAD]", this, new CardinalValidateReceiver() {
           /**
            * This method is triggered when the transaction 
            * has been terminated. This is how SDK hands back
            * control to the merchant's application. This method will
            * include data on how the transaction attempt ended and
            * you should have your logic for reviewing the results of
            * the transaction and making decisions regarding next steps.
            * JWT will be empty if validate was not successful.
            *
            * @param validateResponse
            * @param serverJWT
            */
           @Override
           public void onValidated(Context currentContext, ValidateResponse validateResponse, String serverJWT) {
           }
       });
 }
catch (Exception e) {
   // Handle exception
 }          
```

Calling Cardinal session continue (iOS SDK) {#reference_isy_1jf_xpb}
====================================================================

When you have verified that a customer's card is enrolled in a card authentication program, include the payload, and the response field and incorporate them into the *Cardinal session continue* function before proceeding with the authentication session.  
In the *Cardinal session continue* function, you should pass a class conforming to the *CardinalValidationDelegate* protocol (and implement the *stepUpDidValidate* method) as a parameter. These examples show a class conforming to the *CardinalValidationDelegate* protocol.

*Objective-C Examples*
----------------------

Cardinal session continue (iOS SDK - Objective-C)

```
@interface YourViewController()&lt;CardinalValidationDelegate&gt;{ //Conform your ViewController or any other class to CardinalValidationDelegate protocol
   
}
@end
  
@implementation YourViewController
  
    /**
     * This method is triggered when the transaction has 
     * been terminated.This is how SDK hands back
     * control to the merchant's application. This method will
     * include data on how the transaction attempt ended and
     * you should have your logic for reviewing the results of
     * the transaction and making decisions regarding next steps.
     * JWT will be empty if validate was not successful
     *
     * @param session
     * @param validateResponse
     * @param serverJWT
     */
    -(void)cardinalSession:(CardinalSession *)session stepUpDidValidateWithResponse:(CardinalResponse *)validateResponse serverJWT:(NSString *)serverJWT{
       
    }
  
@end                         
```

If the *Cardinal.continue* process is requested in the same class, request the method shown in the following example to start the step up flow.  
Cardinal.continue Request in the Same Class (Objective-C)

```
[session continueWithTransactionId: @"[TRANSACTION_ID]"
                           payload: @"[PAYLOAD]"
               didValidateDelegate: self];                           
```

*Swift Examples*
----------------

Cardinal session continue (iOS SDK - Swift)

```
class YourViewController:CardinalValidationDelegate {
  
    /**
     * This method is triggered when the transaction has been 
     * terminated.This is how SDK hands back
     * control to the merchant's application. This method will
     * include data on how the transaction attempt ended and
     * you should have your logic for reviewing the results of
     * the transaction and making decisions regarding next steps.
     * JWT will be empty if validate was not successful
     *
     * @param session
     * @param validateResponse
     * @param serverJWT
     */
    func cardinalSession(cardinalSession session: CardinalSession!, stepUpValidated validateResponse: CardinalResponse!, serverJWT: String!) {
        
    }
 
}                          
```

If the *Cardinal.continue* function is requested in the same class, request the method shown in the example below to start the step up flow.  
Cardinal.continue Request in the Same Class (Swift)

```
session.continueWith(transactionId: "[TRANSACTION_ID]", payload: "[PAYLOAD]", validationDelegate: self)            
```

When necessary, the SDK displays the authentication window and the customer enters their authentication information.

Receiving the Authentication Results {#reference_ezc_23n_xpb}
=============================================================

Next, the *onValidated()* function (Android SDK) or the *stepUpDidValidate* function (iOS SDK) launches and returns the authentication results and response JWT along with the processor transaction ID as shown in this example. Decoded Response JWT

```
{
  "iss": "5a4504be6fe3d1127cdfd94e",
  "iat": 1555075930,
  "exp": 1555083130,
  "jti": "cc532159-636d-4fa8-931d-d4b0f4c83b99",
  "ConsumerSessionId": "0_9a16b7f5-8b94-480d-bf92-09cd302c9230",
  "aud": "d0cf3392-62c5-4107-bf6a-8fc3bb49922b",
  "Payload": {
    "Payment": {
      "Type": "CCA",
      "ProcessorTransactionId": "YGSaOBivyG0dzCFs2Zv0"
    },
    "ErrorNumber": 0,
    "ErrorDescription": "Success"
  }
}                           
```

Requesting the Validation Service {#pa-sdk-implementing-request-validation}
===========================================================================

For enrolled cards, the next step is to make a back-end, server-to-server request for the validation service.  
When you make the validation request, you must:

* Send the consumerAuthenticationInformation.authenticationTransactionId request field.
* Send the credit card information including the PAN, currency, and expiration date (month and year).

{#pa-sdk-implementing-request-validation_ul_qc4_5yf_xpb}  
The response that you receive contains the validation result.  
It is recommended that you request the payer authentication and card authorization services at the same time. Doing so automatically sends the correct information to your payment processor and converts the values of these fields to the proper format required by your payment processor:

* consumerAuthenticationInformation.ecommerceIndicator
* consumerAuthenticationInformation.cavv
* consumerAuthenticationInformation.ucafAuthenticationData
* consumerAuthenticationInformation.xid and consumerAuthenticationInformation.xid

{#pa-sdk-implementing-request-validation_ul_x5n_czf_xpb}  
If you request the services separately, manually include the validation result values (Validation Check response fields) in the authorization service request (Card Authorization request fields). To receive liability shift protection, you must ensure that you pass all pertinent data for the card type and processor in your request. Failure to do so might invalidate your liability shift for that transaction. Include the electronic commerce indicator (ECI), the transaction ID (XID), the 3-D Secure version, the directory server transaction ID, and this card-specific information in your authorization request.

* For Relay, JCB,, China UnionPay, Elo, Diners Club, Discover, and American Express include the CAVV.
* For Mastercard only, include the collection indicator and the AAV (also known as UCAF).

{#pa-sdk-implementing-request-validation_ul_o3s_dzf_xpb}

|           Identifier            |                 Validation Check Response Field                 |                Card Authorization Request Field                 |
|---------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| E-commerce indicator            | consumerAuthenticationInformation.indicator                     | processingInformation.commerceIndicator                         |
| Collection indicator            | consumerAuthenticationInforma tion.ucafCollectionIndicator      | consumerAuthenticationInfo rmation.ucafCollectionIndicator      |
| CAVV                            | consumerAuthenticationInformation.cavv                          | consumerAuthenticationInformation.cavv                          |
| AAV                             | consumerAuthenticationInforma tion.ucafAuthenticationData       | consumerAuthenticationInfo rmation.ucafAuthenticationData       |
| XID                             | consumerAuthenticationInformation.xid                           | consumerAuthenticationInformation.xid                           |
| `3-D Secure` version            | consumerAuthenticationInforma tion.specificationVersion         | consumerAuthenticationInfo rmation.paSpecificationVersion       |
| Directory server transaction ID | consumerAuthenticationInforma tion.directoryServerTransactionId | consumerAuthenticationInfo rmation.directoryServerTransactionId |
[Validation Check and Response Fields]

Interpreting the Response {#pa-sdk-implementing-request-validation-interpreting-response}
=========================================================================================

> IMPORTANT
> If the authentication fails, Relay, Diners Club, Discover, JCB, China UnionPay, Elo, and American Express require that you not accept the card. Instead, you must ask the customer to use another payment method.  
> Proceed with the order according to the validation response received. The responses are similar for all card types:

* Success: You receive `AUTHENTICATION_SUCCESSFUL`, and other service requests, including authorization, are processed normally.
* Failure: You receive `AUTHENTICATION_FAILED`, so the other services in your request are not processed.
* Error: If you receive an error from the payment card company, process the order according to your business rules. If the error occurs frequently, report it to [customer support](http://support.example.com ""). If you receive a system error, determine the cause, and proceed with card authorization only if appropriate.

{#pa-sdk-implementing-request-validation-interpreting-response_ul_psm_fxf_xpb}  
To verify that the enrollment and validation checks are for the same transaction, ensure that the XID in the enrollment check and validation responses are identical.

Redirecting Customers to the Message Page {#concept_ujz_wvf_xpb}
================================================================

After authentication is complete, redirect the customer to a page containing a success or failure message. Ensure that all messages that display to customers are accurate, complete, and address all possible scenarios for enrolled and non-enrolled cards. For example, if the authentication fails, display a message such as this to the customer:

```
Authentication Failed
Your card issuer cannot authenticate this card. Please select another card or form of payment to complete your purchase.
```

Authentication Examples Using Primary Account Numbers {#concept_g2r_dgx_qxb}
============================================================================

These examples list the API fields that are required or optional for the Setup, Check Enrollment, and Validate Authentication services. An example of a request payload and a successful response that occur with each service is provided. Payer authentication has three types of examples:
* Primary Account Number (PAN): Illustrates how the payer authentication services work with customer PANs during transactions.
* Tokens: Illustrates how the payer authentication services work with different types of tokens.
* 3RI: Illustrates how the payer authentication services work with merchant-initiated transactions.
  {#concept_g2r_dgx_qxb_ul_kxz_qqx_bdc}  
  In certain circumstances, some payment card companies and some countries require more information than is normally collected when authenticating the customer. These circumstances, and the API fields to use in those circumstances, are noted for each case.

Setting Up Device Data Collection {#pa2-set-up-use-intro}
=========================================================

The Setup service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order.

Card-Specific Requirements {#pa2-set-up-use-intro_card-specific}
----------------------------------------------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-set-up-use-intro_dl_d1v_trz_rxb}

Country-Specific Requirements {#pa2-set-up-use-intro_country-specific-R}
------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-set-up-use-intro_dl_gpf_5rz_rxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for Device Data Collection {#pa2-use-setup-reqd-fields}
=======================================================================

These fields are the minimum fields required when you request the Payer Authentication Setup service. Other fields that can be used to collect additional information during a transaction are listed in the optional fields section. Under certain circumstances, a field that is normally optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field field value is `US` or `CA`.

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "") paymentInformation.card.type
:
This field is required when the card type is Cartes Bancaires, JCB, China UnionPay, or Meeza.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Device Data Collection {#reference_hkg_vtp_mrb}
===================================================================

These fields are optional for setting up a Payer Authentication transaction. Under certain circumstances, a field might appear as both an optional field and a required field.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
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

REST Example: Setting Up Data Collection {#pa2-use-setup-rest-ex}
=================================================================

Request

```
{
  "paymentInformation": {
    "card": {
      "type": "001",
      "expirationMonth": "12",
      "expirationYear": "2025",
      "number": "4XXXXXXXXXXXXXXX"
    }
  }
}
```

Response

```
 {
  "clientReferenceInformation": {
    "code": "1675295420285",
  },
  "consumerAuthenticationInformation": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIwYTFmZjNmYS02YTdiLTQ0NjYtYTgzOC04NTNjOTk2ZTMw
                                   MDYiLCJpYXQiOjE2NzUyOTU0MjAsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTY3NTI
                                   5OTAyMCwiT3JnVW5pdElkIjoiNWI5YzRiYjNmZjYyNmIxMzQ0ODEwYTAxIiwiUmVmZXJlbmNlSWQiOiIzOTE2M
                                   GMyZC1jMWU0LTQ0NjUtYWNlMy1lYjMyZDVhMWQ1NTkifQ.dl3w8s_ZpjA7kWmikyyYHO1Ak4TnzUHv8BuPra
                                   tQukc",
    "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
    "referenceId": "39160c2d-c1e4-4465-ace3-eb32d5a1d559",
    "token": "AxizbwSTbhQQxCrDMCazABEBT9u+U5WYAXsQyaSZejFczCmAMAAAwAnp"
  },
  "id": "6752954202146024203955",
  "status": "COMPLETED",
  "submitTimeUtc": "2023-02-01T23:50:20Z"
}                                      
```

Checking Enrollment in Payer Authentication {#pa2-check-enroll-use-intro}
=========================================================================

The Check Enrollment service tries to authenticate the cardholder. If the cardholder can be authenticated without additional information, the transaction can be authorized. If more information is required, the cardholder will be challenged to provide additional authentication.

Card-Specific Requirements {#pa2-check-enroll-use-intro_card-specific-Rest}
---------------------------------------------------------------------------

Some payment cards require information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (U.S.) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-check-enroll-use-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.

Country-Specific Requirements {#pa2-check-enroll-use-intro_country-specific}
----------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-check-enroll-use-intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA`, `US`, or `China`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2-check-enroll-use-intro_processor-specific}
--------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Required Fields for Checking Enrollment in Payer Authentication {#pa-use-check-enroll-reqd-fields}
==================================================================================================

These fields are the minimum fields required for verifying that a customer is enrolled in a payer authentation program. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[buyerInformation.mobilePhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-mobile-phone.md "")
:
This field is required (when available) if buyerInformation.workPhone is not used, unless market or regional mandate restricts sending this information.

[buyerInformation.workPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-work-phone.md "")
:
This field is required (when available) if buyerInformation.mobilePhone is not used, unless market or regional mandate restricts sending this information.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
This field is required for SDK integration. When you use the SDK integration, this field is dynamically set to `SDK`. When you use the JavaScript code, this field is dynamically set to `Browser`. For merchant-initiated or 3RI transactions, you must set the field to `3RI`. When you use this field in addition to JavaScript code, you must set the field to `Browser`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
For non-payment authentication, set to a value of `02`.

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[consumerAuthenticationInformation.returnUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-return-url.md "")
:

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[deviceInformation.httpAcceptBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-browser-value.md "")
:

[deviceInformation.httpAcceptContent](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-content.md "")
:

[deviceInformation.httpBrowserColorDepth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-color-depth.md "")
:

[deviceInformation.httpBrowserJavaEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-enabled.md "")
:

[deviceInformation.httpBrowserJavaScriptEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-script-enabled.md "")
:

[deviceInformation.httpBrowserLanguage](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-language.md "")
:

[deviceInformation.httpBrowserScreenHeight](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-height.md "")
:

[deviceInformation.httpBrowserScreenWidth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-width.md "")
:

[deviceInformation.httpBrowserTimeDifference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-time-diff.md "")
:

[deviceInformation.ipAddress](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-ip-address.md "")
:

[deviceInformation.userAgentBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-user-agent-browser-value.md "")
:
When the customer's browser provides this value, you must include that value in your request.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Checking Enrollment in Payer Authentication {#pa-api-enrolling-optional-fields}
===================================================================================================

These fields are usually optional when you verify enrollment for a Payer Authentication transaction. In certain circumstances, the information provided by an optional field might be required before a transaction can proceed. Those optional fields that are sometimes required are also listed as required fields with the circumstance described.

[acquirerInformation.bin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-acquirer-bin.md "")
:

[acquirerInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-country.md "")
:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.acsWindowSize](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-acs-window-size.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-data.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-date.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-method.md "")
:

[consumerAuthenticationInformation. authenticationBrand](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-brand.md "")
:
This field is only used with mada cards.

[consumerAuthenticationInformation.authenticationTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-txn-id.md "")
:

[consumerAuthenticationInformation.authorizationPayload](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authorization-payload.md "")
:

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
> WARNING Modifying this field could affect your liability shifts. Unless you are very familiar with the various types of authentication, do not change the default settings before consulting with customer support.

[consumerAuthenticationInformation.credentialEncrypted](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-credential-encrypted.md "")
:

[consumerAuthenticationInformation.customerCardAlias](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-customer-card-alias.md "")
:

[consumerAuthenticationInformation.sdkMaxTimeout](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-sdk-max-timeout.md "")
:

[consumerAuthenticationInformation.decoupledAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-decouple-auth-indicator.md "")
:

[consumerAuthenticationInformation.decoupledAuthenticationMaxTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-decouple-auth-max-time.md "")
:

[consumerAuthenticationInformation.default Card](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation. marketingOptIn](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-marketing-opt-in.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation. marketingSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-marketing-source.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:

[consumerAuthenticationInformation.merchantFraudRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-fraud-rate.md "")
:

[consumerAuthenticationInformation.merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:

[consumerAuthenticationInformation.messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:

[consumerAuthenticationInformation.otpTo ken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-otp-token.md "")
:

[consumerAuthenticationInformation.overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:

[consumerAuthenticationInformation.overridePaymentMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:

[consumerAuthenticationInformation.prior AuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-data.md "")
:

[consumerAuthenticationInformation.priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:

[consumerAuthenticationInformation.priorAuthenticationReferenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-reference-id.md "")
:

[consumerAuthenticationInformation.priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[consumerAuthenticationInformation.productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:

[consumerAuthenticationInformation.requestorName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-name.md "")
:

[consumerAuthenticationInformation.requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:

[consumerAuthenticationInformation.returnURL](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-return-url.md "")
:

[consumerAuthenticationInformation.scoreRequest](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-score-request.md "")
:

[consumerAuthenticationInformation.sdkMaxTimeout](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-score-request.md "")
:

[consumerAuthenticationInformation.strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:

[consumerAuthenticationInformation.strongAuthentication.secureCorporate PaymentIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-secure-corp-payment-id.md "")
:

[consumerAuthenticationInformation.strongAuthentication.transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-txn-mode.md "")
:

[consumerAuthenticationInformation.whiteListStatus](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-white-list-status-a.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:

[merchantInformation.merchantDescriptor.url](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-url.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
This field is required for US and Canada.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.lineItems.passenger.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-passenger-firstname.md "")
:

[orderInformation.lineItems.passenger.last Name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-passenger-lastname.md "")
:

[orderInformation.lineItems.productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems.productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems.productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems.quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems.shippingAddress1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-address1.md "")
:

[orderInformation.lineItems.shippingAddress2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-address2.md "")
:

[orderInformation.lineItems.shippingCity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-city.md "")
:

[orderInformation.lineItems.shippingCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-country-code.md "")
:

[orderInformation.lineItems.shippingDestinationTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-destination-types.md "")
:

[orderInformation.lineItems.shippingLastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-last-name.md "")
:

[orderInformation.lineItems.shippingMiddleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-middle-name.md "")
:

[orderInformation.lineItems.shippingPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-phone.md "")
:

[orderInformation.lineItems.shippingPostalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-postal-code.md "")
:

[orderInformation.lineItems.shippingState](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-state.md "")
:

[orderInformation.lineItems.unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems.shippingDestinationTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-destination-types.md "")
:

[orderInformation.reordered](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-reordered.md "")
:

[orderInformation.shippingDetails.shippingMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipping-details-shipping-method.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:

[orderInformation.shipTo.address3](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address3.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.destinationCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-destination-code.md "")
:

[orderInformation.shipTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-email.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

[orderInformation.totalOffersCount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-total-offers-count.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
This field is strongly recommended.

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.fluidData.value](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-value.md "")
:

[paymentInformation.tokenizedCard. cryptogram](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:
This field is strongly recommended.

[paymentInformation.tokenizedcard.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedcard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:

[recurringPaymentsInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:
When this field is empty, the current date is used.

riskInformation.buyerHistory. transactionCountDay
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountYear
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. accountPurchases
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. addCardAttempts
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.createDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.lastChangeDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.passwordChangeDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.shipAddressUsageDate
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. paymentAccountDate
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. priorSuspiciousActivity
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountDay
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountYear
:
Contact customer support for more information about this field.

[travelInformation.legs.carrierCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-transit-airline-legs-carrier-code.md "")
:

[travelInformation.legs.departureDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-legs-departure-date.md "")
:

[travelInformation.legs.origination](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-legs-origin.md "")
:

[travelInformation.numberOfPassengers](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-numpassengers.md "")
:

[travelInformation.passengers.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-passengers-firstname.md "")
:

[travelInformation.passengers.lastName](hhttps://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-passengers-lastname.md "")
:

REST Example: Checking Enrollment {#pa2-use-check-enroll-rest-ex}
=================================================================

Request

```
{
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "100"
        },
        "billTo": {
            "address1": "901 metro center blvd",
            "address2": "metro 3",
            "administrativeArea": "CA",
            "country": "US",
            "locality": "san francisco",
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "18007097779",
            "postalCode": "94404",
            "email": "email@email.com"
        }
    },
    "paymentInformation": {
        "card": {
            "number": "4XXXXXXXXXXXXXXX",
            "expirationMonth": "08",
            "expirationYear": 2026
        }
    },
    "deviceInformation": {
        "ipAddress": "139.130.4.5",
        "httpAcceptContent": "test",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": "N",
        "httpBrowserJavaScriptEnabled": "Y",
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "100000",
        "httpBrowserScreenWidth": "100000",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "GxKnLy8TFDUFxJP1t"
      },
      "consumerAuthenticationInformation": {
        "referenceId": "c44224db-0dda-40aa-9536-ac1595fd2e8d",
        "transactionMode": "S",
        "returnUrl": "https://wv730hw7033250:3002/restapi/cardinalDirect/StepUp/Response"
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
      "code": "1675295420285"
    },
    "consumerAuthenticationInformation": {
        "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
        "challengeRequired": "N",
        "stepUpUrl": "https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp",
        "authenticationTransactionId": "1xRSpLPEoTNsinp8XUK0",
        "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMS4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiO
        iI4NGU2YzIzYi1lNjIxLTQ2NGUtYWFlYy0xOGNkZDE1YTBlZWMiLCJhY3NUcmFuc0lEIjoiZWU3NDVlM2MtYzI2Ny00YzM0LT
        kzMTEtMGI3NTYwYzJkNjhmIiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
        "directoryServerTransactionId": "4d19781a-49d7-4c90-a145-72b8107fed8f",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "84e6c23b-e621-464e-aaec-18cdd15a0eec",
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyN2I1MjcyYS00OWFiLTQ5YjQtYTljYy1mMTBhYjcx
        MGMyYjciLCJpYXQiOjE2MzAwOTkxNjMsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTYzMDEw
        Mjc2MywiT3JnVW5pdElkIjoiNTk1YWRhYjAzM2ZhZGQyYzUwZTg5NDYxIiwiUGF5bG9hZCI6eyJBQ1NVcmwiOiJodHRwcz
        ovLzBtZXJjaGFudGFjc3N0YWcuY2FyZGluYWxjb21tZXJjZS5jb20vTWVyY2hhbnRBQ1NXZWIvY3JlcS5qc3AiLCJQYXlsb2FkIjo
        iZXlKdFpYTnpZV2RsVkhsd1pTSTZJa05TWlhFaUxDSnRaWE56WVdkbFZtVnljMmx2YmlJNklqSXVNUzR3SWl3aWRHaHlaV1
        ZFVTFObGNuWmxjbFJ5WVc1elNVUWlPaUk0TkdVMll6SXpZaTFsTmpJeExUUTJOR1V0WVdGbFl5MHhPR05rWkRFMVlU
        QmxaV01pTENKaFkzTlVjbUZ1YzBsRUlqb2laV1UzTkRWbE0yTXRZekkyTnkwMF6TTBMVGt6TVRFdE1HSTNOVFl3WXpKa0
        5qaG1JaXdpWTJoaGJHeGxibWRsVjJsdVpHOTNVMmw2WlNJNklqQXlJbjAiLCJUcmFuc2FjdGlvbklkIjoiMXhSU3BMUEVvV
        E5zaW5wOFhVSzAifSwiT2JqZWN0aWZ5UGF5bG9hZCI6dHJ1ZSwiUmV0dXJuVXJsIjoiaHR0cHM6Ly93djczMGh3NzAzMzI
        1MDozMDAyL3Jlc3RhcGkvY2FyZGluYWxEaXJlY3QvU3RlcFVwL1Jlc3BvbnNlIn0.ixbdhFoB8M_BWI2sAIIQUjWtIOMzIwRI
        mrg5iu7AyNE",
        "specificationVersion": "2.1.0",
        "token": "AxjzbwSTVZPTJPD7ixR8ADUBURxP1CnnpA6cQE1129JMvRiuHCKArAAAx/+g",
        "acsTransactionId": "ee745e3c-c267-4c34-9311-0b7560c2d68f"
    },
    "errorInformation": {
        "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
        "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder 
            before continuing with the transaction."
    },
    "id": "6300991627296049403004",
    "paymentInformation": {
        "card": {
            "bin": "4XXXXXXX",
            "type" : "CARD"
        }
    },
    "status": "PENDING_AUTHENTICATION",
    "submitTimeUtc": "2022-08-27T21:19:23Z"
} 
              
            
```

Checking Enrollment and Authorizing a Transaction {#pa2_check_enroll_authorize_use_intro}
=========================================================================================

The Checking Enrollment service can be combined with the Authorization service so that when a customer's authentication does not require a challenge, the transaction is automatically submitted for authorization.

Card-Specific Requirements {#pa2_check_enroll_authorize_use_intro_card-specific-Rest}
-------------------------------------------------------------------------------------

Some payment cards require information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (U.S.) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2_check_enroll_authorize_use_intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.

Country-Specific Requirements {#pa2_check_enroll_authorize_use_intro_country-specific}
--------------------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2_check_enroll_authorize_use_intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA`, `US`, or `China`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2_check_enroll_authorize_use_intro_processor-specific}
------------------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

REST Example: Checking Enrollment and Authorizing a Transaction {#pa2-use-check-enroll-auth-rest-ex}
====================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
    },
    "processingInformation": {
        "capture": "true"
        },
        "actionList": [
            "CONSUMER_AUTHENTICATION"
        ]
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "4XXXXXXXXXXX2701",
            "securityCode": "123",
            "expirationMonth": "12",
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "GBP"
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Smith",
            "address1": "201 S. Division St._1",
            "address2": "Suite 500",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "postalCode": "94404",
            "country": "US",
            "email": "accept@email.com",
            "phoneNumber": "6504327113"
        }
    },
    "deviceInformation": {
      "ipAddress": "139.130.4.5",
      "httpAcceptContent": "test",
      "httpBrowserLanguage": "en_us",
      "httpBrowserJavaEnabled": "N",
      "httpBrowserJavaScriptEnabled": "Y",
      "httpBrowserColorDepth": "24",
      "httpBrowserScreenHeight": "100000",
      "httpBrowserScreenWidth": "100000",
      "httpBrowserTimeDifference": "300",
      "userAgentBrowserValue": "GxKnLy8TFDUFxJP1t"
    },
    "consumerAuthenticationInformation": {
        "returnUrl": "https://webhook.site/bdf16530-2577-4885-9dee-e9d6c4f98bc0",
        "referenceId": "72b727bc-a6a4-4481-b25c-a5939d48fef6"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7478240150646451804805/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7478240150646451804805"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "05",
        "authenticationTransactionId": "2BE13ZGIzjXdFfKw2Fi0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "eci": "05",
        "token": "Axj//wSTlWVuE5k5bxqFAAIU3YMmzhgzYM2Ce/LXc7XAKe/LXc7XZ0OnEFBWGTSTL0Yua1eAwHScqytwnMnLeNQo+xnO",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "Y",
        "acsReferenceNumber": "CardinalACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "4689476f-168b-415e-bad5-aee47a270086",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "bda6f2d1-5c18-4589-a150-1e8c6e795e85",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "vbv",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "5bbd605d-80e4-48ef-82b5-0406774c66e3"
    },
    "id": "7478240150646451804805",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "authorizedAmount": "100.00",
            "currency": "GBP"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "brandName": "CARD",
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "bin": "400000",
            "type": "001"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678"
    },
    "processorInformation": {
        "paymentAccountReferenceNumber": "V0010013018036776997406844475",
        "merchantNumber": "12345678",
        "approvalCode": "100",
        "cardVerification": {
            "resultCodeRaw": "3",
            "resultCode": "2"
        },
        "merchantAdvice": {
            "code": "00",
            "codeRaw": "0"
        },
        "networkTransactionId": "123456789012345",
        "transactionId": "123456789012345",
        "responseCode": "0",
        "avs": {
            "code": "U",
            "codeRaw": "00"
        }
    },
    "reconciliationId": "7026803030",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-05-21T10:40:15Z"
}            
```

Validating a Challenge {#pa2-use-validate-intro}
================================================

Running the Validation service compares the customer's response to the challenge from the issuing bank to validate the customer identity.

Card-Specific Requirements {#pa2-use-validate-intro_card-specific-REST}
-----------------------------------------------------------------------

Some payment cards require additional information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airline purchase).

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-validate-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US)

Country-Specific Requirements {#pa2-use-validate-intro_country-specific-REST}
-----------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-validate-intro_dl_gpf_5rz_rxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-results`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-results`

Required Fields for Validating a Challenge {#pa2-use-validation-reqd-fields}
============================================================================

These are the minimum fields required when validating the customer. Other fields for collecting additional information during a transaction are described in the list of optional fields. Under certain circumstances, a field that is optional might be required. The circumstance that makes an optional field required is described.

Required Fields
---------------

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.authenticationTransactionId](https://developer.example.com/docs/vas/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-txn-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.lineItems.unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:
This field is required when the orderInformation.amountDetails.totalAmount field is not used.

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Validating a Challenge {#pa-api-validating-optional-fields}
===============================================================================

These fields are optional when validating a Payer Authentication transaction. In certain circumstances, the information provided by an optional field might be required before a transaction can proceed. Those optional fields that are sometimes required are listed in the required fields with the circumstance described.

[consumerAuthenticationInformation. authenticationBrand](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-brand.md "")
:
This field is only used with mada cards.

[consumerAuthenticationInformation.credentialEncrypted](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-credential-encrypted.md "")
:

[consumerAuthenticationInformation.responseAccessToken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-response-access-token.md "")
:

[consumerAuthenticationInformation.signedPares](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-signed-pares.md "")
:

REST Example: Validating a Challenge {#pa2-use-validate-rest-ex}
================================================================

Request

```
{
  "paymentInformation": {
    "card": {
      "type": "001"
    }
  },
  "consumerAuthenticationInformation": {
    "authenticationTransactionId": "bE4fdH96vKejWyz6rXy1"
  }
}
```

Response to a Successful Request

```
{
  "consumerAuthenticationInformation": {
    "indicator": "vbv",
    "eciRaw": "05",
    "authenticationResult": "0",
    "authenticationStatusMsg": "Success",
    "eci": "05",
    "token": "AxijLwSTVYSa8ZmiITBhAAJRHE+rXi4ATWhk0kyxdfAuewAA4iW6",
    "cavv": "MTIzNDU2Nzg5MDEyMzQ1Njc4OTA=",
    "paresStatus": "Y",
    "xid": "MTIzNDU2Nzg5MDEyMzQ1Njc4OTA=",
    "directoryServerTransactionId": "144ecc30-264f-4d2c-8a4e-798a4f311b1f",
    "threeDSServerTransactionId": "6773483d-e16a-40f5-bc5d-93d709c8a06b",
    "specificationVersion": "2.1.0",
    "acsTransactionId": "6eab6816-72d2-40e8-a03f-0a6c8bfe3156"
  },
  "id": "6299894944336529404001",
  "paymentInformation": {
    "card": {
      "bin": "400000",
      "type" : "CARD"
    }
  },
  "status": "AUTHENTICATION_SUCCESSFUL",
  "submitTimeUtc": "2021-08-26T14:51:34Z"
}
```

Validating and Authorizing a Transaction {#pa2-use-validate-auth-intro}
=======================================================================

The Validation service can be combined with the Authorization service so that when a customer's authentication is validated, the transaction is automatically submitted for authorization.

Fields Specific to a Relay Secure Transaction
--------------------------------------------

These API fields are required specifically for this use case.

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to `vbv` for a successful authentication (EMV `3-D Secure` value of `05`), `vbv_attempted` if authentication was attempted but did not succeed (EMV 3-D Secure value of `06`), or `vbv_failure` if authentication failed (EMV `3-D Secure` value of `07`).

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:
This field is required when payer authentication is successful.

Card-Specific Requirements
--------------------------

Some payment cards require information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airline purchase.

[merchantInformation. merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-validate-auth-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.
{#pa2-use-validate-auth-intro_dl_gpf_5rz_rxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`

Required Fields for Processing an Authorization Using Relay Secure {#payments-processing-pa-relay-reqfields}
==========================================================================================================

> IMPORTANT  
> When relaxed requirements for address data and the expiration date are being used, not all fields in this list are required. It is your responsibility to determine whether your account is enabled to use this feature and which fields are required. For details about relaxed requirements, see [Relaxed Requirements for Address Data and Expiration Date in Payment Transactions](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/payments-relax-reqs.md "").

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.cavv](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-cavv-a.md "")
:
This field is required when payer authentication is successful. Otherwise, this field is optional.

[consumerAuthenticationInformation.xid](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-xid.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
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

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[processingInformation.commerceIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-commerce-ind.md "")
:
Set this field to one of these values:

    * `vbv`: Successful authentication (EMV `3-D Secure` value of `05`).
    * `vbv_attempted`: Authentication was attempted (EMV `3-D Secure`value of `06`).
    * `vbv_failure`: or `internet`: Authentication failed or was not attempted (EMV `3-D Secure` value of `07`).
    {#payments-processing-pa-relay-reqfields_ul_ztw_km1_jxb}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Validating and Authorizing a Transaction {#payments-processing-pa-relay-ex-rest}
=============================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
    },
    "processingInformation": {
        "capture": "true",
        "authorizationOptions": {
            "ignoreAvsResult": "true"
        },
        "actionList": [
            "VALIDATE_CONSUMER_AUTHENTICATION"
        ]
    },
    "paymentInformation": {
        "card": {
            "expirationYear": "2031",
            "number": "4XXXXXXXXXXX25X3",
            "securityCode": "123",
            "expirationMonth": "12",
            "type": "001"
        }
    },
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "currency": "GBP"
        },
        "billTo": {
            "firstName": "John",
            "lastName": "Smith",
            "address1": "201 S. Division St._1",
            "address2": "Suite 500",
            "locality": "Foster City",
            "administrativeArea": "CA",
            "postalCode": "94404",
            "country": "US",
            "email": "accept@email.com",
            "phoneNumber": "6504327113"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "2b4eAa4K3H778X34Ciy0"
    }
}
```

Response to a Successful Request

```
{
    "_links": {
        "void": {
            "method": "POST",
            "href": "/pts/v2/payments/7478305945626990404807/voids"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7478305945626990404807"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "indicator": "vbv",
        "eciRaw": "05",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "eci": "05",
        "token": "Axj//wSTlWZX08jkcOTHAAIU3YMmzhgzcN2ie/LXsgSgKe/LXsgS50OnEFBWGTSTL0Yua1eAwHScqzK+nkcjhyY4wDi0",
        "cavv": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "paresStatus": "Y",
        "xid": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "fa628ed8-ad77-4723-b28f-91952eaca8fe",
        "threeDSServerTransactionId": "71399671-8456-4c97-b056-e127622a5e26",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "5f9fb589-08cc-4952-866d-30939868f411"
    },
    "id": "7478305945626990404807",
    "orderInformation": {
        "amountDetails": {
            "totalAmount": "100.00",
            "authorizedAmount": "100.00",
            "currency": "GBP"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "brandName": "CARD",
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "bin": "400000",
            "type" : "CARD"
        }
    },
    "pointOfSaleInformation": {
        "terminalId": "12345678"
    },
    "processorInformation": {
        "paymentAccountReferenceNumber": "V0010013018036776997406844475",
        "merchantNumber": "12345678",
        "approvalCode": "100",
        "cardVerification": {
            "resultCodeRaw": "3",
            "resultCode": "2"
        },
        "merchantAdvice": {
            "code": "00",
            "codeRaw": "0"
        },
        "networkTransactionId": "123456789012345",
        "transactionId": "123456789012345",
        "responseCode": "0",
        "avs": {
            "code": "U",
            "codeRaw": "00"
        }
    },
    "reconciliationId": "7026803874",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-05-21T12:29:54Z"
}
```

Non-Payment Authentication {#pa2-check-enroll-use-npa-intro}
============================================================

Non-Payment Authentication (NPA) requests enable a merchant to authenticate a customer without a transaction. A non-payment use case can be used for such tasks as adding a card to a merchant website, updating cardholder information on file, or to verify a cardholder's identity when creating a token for future use. The same authentication used during the checking enrollment process is used for NPA. Non-payment use cases are enabled using a combination of the consumerAuthenticationInformation.messageCategory and consumerAuthenticationInformation.strongAuthentication.authenticationIndicator values. For example to add a card to a loyalty program, set the Message Category value to `02` and the Authentication Indicator value to `04`. For other possible NPA use cases, refer to the other possible values for consumerAuthenticationInformation.messageCategory. The consumerAuthenticationInformation.messageCategory value must be set to `02` (non-payment authentication) to specify that the authentication is not for a transaction.

Card-Specific Requirements
--------------------------

Some payment cards require information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (U.S.) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-check-enroll-use-npa-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB Cartes Bancaires, China UnionPay, or Meeza.

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-check-enroll-use-npa-intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA`, `US`, or `China`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2-check-enroll-use-npa-intro_section_kl3_tbh_xwb}
-------------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[transaction-mode.html](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/so/api-fields/transaction-mode.md "")[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

REST Example: Checking Enrollment for Non-Payment Authentication {#pa2-use-enroll-npa-rest-ex}
==============================================================================================

Request

```
{
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": "10.99"
    },
    "billTo": {
      "address1": "1 Market St",
      "address2": "Address 2",
      "administrativeArea": "CA",
      "country": "US",
      "locality": "san francisco",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "4158880000",
      "email": "test@email.com",
      "postalCode": "94105"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001",
      "expirationMonth": "12",
      "expirationYear": "2025",
      "number": "4XXXXXXXXXXX2503"
    }
  },
  "buyerInformation": {
    "merchantCustomerId": "334124572" 
    "mobilePhone": "1245789632"
  },
  "deviceInformation": {
    "ipAddress": "139.130.4.5",
    "httpAcceptContent": "test",
    "httpBrowserLanguage": "en_us",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": false,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "100000",
    "httpBrowserScreenWidth": "100000",
    "httpBrowserTimeDifference": "300",
    "userAgentBrowserValue": "GxKnLy8TFDUFxJP1t"
  },
  "consumerAuthenticationInformation": {
    "deviceChannel": "BROWSER",
    "messageCategory": "02",
    "transactionMode": "eCommerce"
  }
}
```

Response

```
{
  "clientReferenceInformation": {
    "code": "1729234929433"
  },
  "consumerAuthenticationInformation": {
    "challengeRequired": "N",
    "authenticationTransactionId": "MXvfrk1911nHJpC18OI0",
    "strongAuthentication": {
      "OutageExemptionIndicator": "0"
    },
    "token": "AxjzbwSTi1GtFWKe0Yg5ABEBTyDdd93DSBcS0MRdrSTL0YrmYUwDgAAAWBV8",
    "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
    "acsReferenceNumber": "Cardinal ACS",
    "stepUpUrl": "https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp",
    "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJkOTkzM2U5ZS05MGI4LTQ2YWMtOGEwNy04NzM5YzVlODJiNWMiLCJhY3NUcmFuc0lEIjoiZGUwYTExMjUtODFiNC00YjM4LTlhYTAtZThjNzJkZTAwMzk5IiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
    "directoryServerTransactionId": "0656bace-7519-4dd9-9450-98dfc6f35d7c",
    "veresEnrolled": "Y",
    "threeDSServerTransactionId": "d9933e9e-90b8-46ac-8a07-8739c5e82b5c",
    "acsOperatorID": "MerchantACS",
    "specificationVersion": "2.2.0",
    "acsTransactionId": "de0a1125-81b4-4b38-9aa0-e8c72de00399"
  },
  "errorInformation": {
    "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
    "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
  },
  "id": "7292349292916631504953",
  "paymentInformation": {
    "card": {
      "bin": "400000",
      "type" : "CARD"
    }
  },
  "status": "PENDING_AUTHENTICATION",
  "submitTimeUtc": "2024-10-18T07:02:09Z"
}            
```

Examples Using `3-D Secure` Data Only {#concept_pjv_tsp_bfc}
============================================================

`3-D Secure` Data Only is a solution that shares data that merchants collect during transactions with the issuer, so that the issuers can make more informed authorization decisions for future transactions. Data Only uses the `3-D Secure` infrastructure, but it is not a complete `3-D Secure` authentication. `3-D Secure` Data Only is a frictionless experience.  
Data Only can increase authorization approvals and reduce fraud in the following ways:

* Merchants share additional transaction data with the issuer, allowing the issuer to feel more comfortable with the transaction's risk level. The issuer can gain additional insight into who the buyer is and what they are purchasing which enables better authorization decisions.

* Since Data Only is not a full authentication, merchants retain fraud liability, putting less risk on the issuers, which might lead to a higher approval rate when compared to non-authenticated transactions.
  {#concept_pjv_tsp_bfc_ul_hhw_ctp_bfc}  
  Relay supports the Relay Data Only program, and Mastercard has two options for Data Only. These Mastercard options are:

* Mastercard Data Share Only: This option mirrors the Relay Data Only program by allowing the AReq message to reach the Issuer. The Issuer can then obtain all of the enhanced data and link that information on the authorization message.

* Mastercard Identity Check Insights: This option stops the AReq at the Mastercard Directory Server. Mastercard returns a Data Only response to the merchant and then passes a risk score outside of the transaction flow to the Issuer that the Issurer can append to the authorization to aid in their decision process.
  {#concept_pjv_tsp_bfc_ul_qrp_z5g_rhc}

Relay Data Only {#concept_v1v_fpv_bfc}
=====================================

Relay has a data only data flow so that merchants can share customer data with the issuers without going through authentication. The additional data provided to the issuer helps the issuer make risk assessments about approving cardholder transactions. Data only data flows are frictionless and do not affect the customer experience. When sending a Relay data only check enrollment request, be sure to include all of the required fields and set the consumerAuthenticationInformation.challengeCode field to `06`.  
The response from the data only request will include this data:

* ECI = `07`
* PARes = `I`
* \&lt;CAVV\&gt; value

{#concept_v1v_fpv_bfc_ul_gdj_4qr_cfc}  
This data from the response must be included in the authorization request.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`

Required Fields for Relay Data Only {#reference_lzz_dgv_bfc}
===========================================================

These fields are the minimum fields required when you request the Relay Data service. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[buyerInformation.mobilePhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-mobile-phone.md "")
:
This field is required (when available) if buyerInformation.workPhone is not used, unless market or regional mandate restricts sending this information.

[buyerInformation.workPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-work-phone.md "")
:
This field is required (when available) if buyerInformation.mobilePhone is not used, unless market or regional mandate restricts sending this information.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[customerInformation.merchantCustomerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/customer-info-merchant-customer-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
{#reference_lzz_dgv_bfc_dl_bvv_n3v_bfc}

REST Example: Relay Data Only {#reference_vzp_m5p_bfc}
=====================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
        },
    "customerInformation": {
        "merchantCustomerId": "SW489TT19",
        }
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.99"
            },
    "billTo": {
        "address1": "1 Market St",
        "address2": "Address 2",
        "administrativeArea": "CA",
        "country": "US",
        "locality": "san francisco",
        "firstName": "Test",
        "lastName": "Testlastname",    
        "phoneNumber": "4158880000",
        "email": "test@email.com",
        "postalCode": "94105"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "05",
            "expirationYear": "2029",
            "number":"4XXXXXXXXXXX2X24"
            }
        },
    "deviceInformation": {
        "httpAcceptBrowserValue": "data",
        "httpAcceptContent": "pa_http_user_accept_value",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": false,
        "httpBrowserJavaScriptEnabled": false,
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "864",
        "httpBrowserScreenWidth": "1536",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "123"
        },
    "consumerAuthenticationInformation": {
        "deviceChannel": "Browser",
        "challengeCode": "06"
        }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "07",
        "authenticationTransactionId": "2DkdQ8ZG1urNNQR0XTM1",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImF1dGhlbnRpY2F0aW9uVmFsdWUiOiJBSmtCQmtoZ1FRQUFBRTRnU0VKeWRRQUFBQUE9IiwiZWZmZWN0aXZlQXV0aFR5cGUiOiJGUiIsImFjc09wZXJhdG9ySUQiOiJNZXJjaGFudEFDUyIsInRocmVlRFNSZXF1ZXN0b3JDaGFsbGVuZ2VJbmQiOiIwNiIsInRyYW5zU3RhdHVzIjoiSSIsImRzVHJhbnNJRCI6ImNlOGMzNTk1LTE4NjgtNDI0Mi1iM2VlLTM1Njg5ZGYyZjJjZSIsImFjc1RyYW5zSUQiOiIzMDQ3NTczZi01OTBlLTQ2YjUtODNmNC02YTQ5YzFiNDIzOWMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MTA1ODQ1IiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiNDY5MjE2IiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN0b3JJRCI6IjEwMDUyMjM2KjU1ZWYzZWZiZjcyM2FhNDMxYzk5YWM0ZCIsImNhcmRCcmFuZCI6IlZJU0EifQ==",
        "eci": "07",
        "token": "AxjzbwSTlC3VWiL9QyNJAEQBTRduBSgekC4lp/cMm2OKOPlRqQoBgAAAyhZr",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "I",
        "acsReferenceNumber": "CardinalACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "ce8c3595-1868-4242-b3ee-35689df2f2ce",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "205e97c1-f15a-480f-8497-55e9a68cf046",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "internet",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "3047573f-590e-46b5-83f4-6a49c1b4239c"
    },
    "id": "7455787250786729403209",
    "paymentInformation": {
        "card": {
            "bin": "400000",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2025-04-25T10:58:47Z"
}
```

REST Example: Bundled Authentication and Authorization with Relay Data Only {#pa2-use-data-only-relay-bundle-rest-ex}
===================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
        },
    "customerInformation": {
        "merchantCustomerId": "SW489TT19",
        }
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.99"
            },
    "billTo": {
        "address1": "1 Market St",
        "address2": "Address 2",
        "administrativeArea": "CA",
        "country": "US",
        "locality": "san francisco",
        "firstName": "Test",
        "lastName": "Testlastname",
        "phoneNumber": "4158880000",
        "email": "test@email.com",
        "postalCode": "94105"
        }
    },
    "processingInformation": {
        "actionList": [
            "CONSUMER_AUTHENTICATION"
            ]
        },
    "paymentInformation": {
        "card": {
            "expirationMonth": "05",
            "expirationYear": "2029",
            "number":"4XXXXXXXXXXX20X4"
            }
        },
    "deviceInformation": {
        "httpAcceptBrowserValue": "data",
        "httpAcceptContent": "pa_http_user_accept_value",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": false,
        "httpBrowserJavaScriptEnabled": false,
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "864",
        "httpBrowserScreenWidth": "1536",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "123"
        },
    "consumerAuthenticationInformation": {
        "deviceChannel": "Browser",
        "challengeCode": "06"
        }
}
```

Response to Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7455831774536819703209/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7455831774536819703209"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7455831774536819703209/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "07",
        "authenticationTransactionId": "30lLF8FUJmwmp3VofTC1",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImF1dGhlbnRpY2F0aW9uVmFsdWUiOiJBSmtCQmtoZ1FRQUFBRTRnU0VKeWRRQUFBQUE9IiwiZWZmZWN0aXZlQXV0aFR5cGUiOiJGUiIsImFjc09wZXJhdG9ySUQiOiJNZXJjaGFudEFDUyIsInRocmVlRFNSZXF1ZXN0b3JDaGFsbGVuZ2VJbmQiOiIwNiIsInRyYW5zU3RhdHVzIjoiSSIsImRzVHJhbnNJRCI6IjZhODZlNjI4LTc2ODYtNDc4Zi1iNWUzLTRmMzFjMTE1YzcwZiIsImFjc1RyYW5zSUQiOiI3NTBmOTkzOC0wYzYzLTQ3MzQtODY0Yy1kNjg5MWEyNzZlZjIiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MTIxMjU2IiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiNDY5MjE2IiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN0b3JJRCI6IjEwMDUyMjM2KjU1ZWYzZWZiZjcyM2FhNDMxYzk5YWM0ZCIsImNhcmRCcmFuZCI6IlZJU0EifQ==",
        "eci": "07",
        "token": "Axj/7wSTlC5ziEBhdn2pAEQs3aNWrhmxbt2jVm2cMXLdgzZMHKaLtwTReAU0Xbgmi9pAuJaf3DJtjijj5UakLAZJyhc5xCAwuz7UgAAA5APX",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "I",
        "acsReferenceNumber": "CardinalACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "6a86e628-7686-478f-b5e3-4f31c115c70f",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "4e4689c5-97ac-469b-8d67-0613d8794de7",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "internet",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "750f9938-0c63-4734-864c-d6891a276ef2"
    },
    "id": "7455831774536819703209",
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.99",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "type": "001"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "001"
        },
        "card": {
            "bin": "400000",
            "type": "001"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "061920",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "016153570198200",
        "retrievalReferenceNumber": "511512061920",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "016153570198200",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7455831774536819703209",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-04-25T12:12:59Z",
    "tokenInformation": {
        "additionalInformation": "0"
    }
}     
```

Mastercard Data Only {#concept_itw_3pv_bfc}
===========================================

Mastercard has a Data Only data flow so that merchants can share customer data with the issuers without going through authentication. The additional data provided to the issuer helps the issuer make risk assessments about approving cardholder transactions. Data Only data flows are frictionless and do not affect the customer experience.  
When sending a Mastercard Data Only check enrollment request, be sure to include all of the required fields and set the consumerAuthenticationInformation.challengeCode to `06`.  
The response from the Data Only request includes this data:
* ECI = `06`
* CAVV value
* Directory server transaction ID
* paresStatus = `I`
* Risk score
* Reason code
  {#concept_itw_3pv_bfc_ul_pdw_v4r_cfc}  
  This data from the response must be included in the authorization request.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`

Required Fields for Mastercard Data Only {#reference_vjc_b5p_bfc}
=================================================================

These fields are the minimum fields required when you request the Mastercard Data service. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

> IMPORTANT
> Merchants should ensure that they run the device collection and ` 3-D Secure ` Method URL portions of the flow before sending in the pa_enroll request.

Required Fields
---------------

[buyerInformation.mobilePhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-mobile-phone.md "")
:
This field is required (when available) if buyerInformation.workPhone is not used, unless market or regional mandate restricts sending this information.

[buyerInformation.workPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-work-phone.md "")
:
This field is required (when available) if buyerInformation.mobilePhone is not used, unless market or regional mandate restricts sending this information.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[customerInformation.merchantCustomerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/customer-info-merchant-customer-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
{#reference_vjc_b5p_bfc_dl_bvv_n3v_bfc}

REST Example: Mastercard Data Only {#pa2-use-data-only-mc-rest-ex.dita}
=======================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
        },
    "customerInformation": {
        "merchantCustomerId": "SW489TT19",
        }
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.99"
            },
    "billTo": {
        "address1": "1 Market St",
        "address2": "Address 2",
        "administrativeArea": "CA",
        "country": "US",
        "locality": "san francisco",
        "firstName": "Test",
        "lastName": "Testlastname",
        "phoneNumber": "4158880000",
        "email": "test@email.com",
        "postalCode": "94105"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "05",
            "expirationYear": "2029",
            "number":"52XXXXXXXXXX28X5"
            }
        },
    "deviceInformation": {
        "httpAcceptBrowserValue": "data",
        "httpAcceptContent": "pa_http_user_accept_value",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": false,
        "httpBrowserJavaScriptEnabled": false,
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "864",
        "httpBrowserScreenWidth": "1536",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "123"
        },
    "consumerAuthenticationInformation": {
        "deviceChannel": "Browser",
        "challengeCode": "06",
        "scoreRequest": "N"
    }
}
```

Response to Successful Request

```
 {
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "06",
        "challengeRequired": "N",
        "authenticationTransactionId": "KjNeRerYgMLXJD8gzC51",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImVjaSI6IjA0IiwiYXV0aGVudGljYXRpb25WYWx1ZSI6IkFKa0JCa2hnUVFBQUFFNGdTRUp5ZFFBQUFBQT0iLCJlZm

ZlY3RpdmVBdXRoVHlwZSI6IkZSIiwiYWNzT3BlcmF0b3JJRCI6Ik1lcmNoYW50QUNTIiwidGhyZWVEU1JlcXVlc3RvckNoYWxsZW5nZUluZCI6IjAxIiwidHJhbnNTd

GF0dXMiOiJVIiwidHJhbnNTdGF0dXNSZWFzb24iOiI4MCIsImRzVHJhbnNJRCI6IjQxMzVkMzljLWNiNDMtNGM0Zi04MWJmLTliMzc5N2QzYjhmOSIsImFjc1RyYW

5zSUQiOiI5OWIzODcyYy04ZTM2LTQ5ZGQtYjgyNi1iNGYwYzU4M2Y4MjUiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1

cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MDUzODAwIiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiO

TkwMDMzIiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiQ0FSMTM0NzNfUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN

0b3JJRCI6IkNBUjEzNDczX2RlZmF1bHQiLCJjYXJkQnJhbmQiOiJNQVNURVJDQVJEIn0=",
        "token": "AxjzbwSTlCspnzdze9IJAEQCTRdt8KnmkC4lp/UMm2OKOPlRqQoCwAAASAee",
        "paresStatus": "I",
        "acsReferenceNumber": "CardinalACS",
        "ucafCollectionIndicator": "6",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "4135d39c-cb43-4c4f-81bf-9b3797d3b8f9",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "9c4d80a0-1624-4061-8f08-78c59b335e8c",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "99b3872c-8e36-49dd-b826-b4f0c583f825"
    },
    "id": "7455594797856844403209",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2025-04-25T05:38:01Z"
}    
```

REST Example: Bundled Authentication and Authorization with Mastercard Data Only {#pa2-use-data-only-mc-bundle-rest-ex.dita}
============================================================================================================================

Request

```
{
"clientReferenceInformation": {
    "code": "test"
    },
"customerInformation": {
    "merchantCustomerId": "SW489TT19",
    }
"orderInformation": {
    "amountDetails": {
        "currency": "USD",
        "totalAmount": "10.99"
        },
"billTo": {
    "address1": "1 Market St",
    "address2": "Address 2",
    "administrativeArea": "CA",
    "country": "US",
    "locality": "san francisco",
    "firstName": "Test",
    "lastName": "Testlastname",
    "phoneNumber": "4158880000",
    "email": "test@email.com",
    "postalCode": "94105"
    }
},
"processingInformation": {
    "actionList": [
        "CONSUMER_AUTHENTICATION"
        ]
    },
"paymentInformation": {
    "card": {
        "expirationMonth": "05",
        "expirationYear": "2029",
        "number":"52XXXXXXXXXX28X5"
        }
    },
"deviceInformation": {
    "httpAcceptBrowserValue": "data",
    "httpAcceptContent": "pa_http_user_accept_value",
    "httpBrowserLanguage": "en_us",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": false,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "864",
    "httpBrowserScreenWidth": "1536",
    "httpBrowserTimeDifference": "300",
    "userAgentBrowserValue": "123"
    },
"consumerAuthenticationInformation": {
    "deviceChannel": "Browser",
    "challengeCode": "06",
    "scoreRequest": "N"
    }
}
```

Response to Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7455833000666819803209/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7455833000666819803209"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7455833000666819803209/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "06",
        "challengeRequired": "N",
        "authenticationTransactionId": "d94pknkLH4BhjWxylay1",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImVjaSI6IjA0IiwiYXV0aGVudGljYXRpb25WYWx1ZSI6IkFKa0JCa2hnUVFBQUFFNGdTRUp5ZFFBQUFBQT0iLCJlZmZlY3RpdmVBdXRoVHlwZSI6IkZSIiwiYWNzT3BlcmF0b3JJRCI6Ik1lcmNoYW50QUNTIiwidGhyZWVEU1JlcXVlc3RvckNoYWxsZW5nZUluZCI6IjAxIiwidHJhbnNTdGF0dXMiOiJVIiwidHJhbnNTdGF0dXNSZWFzb24iOiI4MCIsImRzVHJhbnNJRCI6IjZhMGY0OTFhLWIxMDUtNDk4Zi05OTk3LTgxYTAyYjk5NzFjYSIsImFjc1RyYW5zSUQiOiJlOTFhODQ3Mi0yNGFhLTQ0ZGUtYTU0Yy00YWExNDVlN2NjZDMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MTIxNTAxIiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiNDY5MjE2IiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN0b3JJRCI6IjEwMDUyMjM2KjU1ZWYzZWZiZjcyM2FhNDMxYzk5YWM0ZCIsImNhcmRCcmFuZCI6Ik1BU1RFUkNBUkQifQ==",
        "token": "Axj/7wSTlC5342kEkThJAEQs3aNWrhmzYMGDZs2cMXLhgzZMHKaLtwTRfAk0Xbgmi/pAuJaf3DJtjijj5UakLAtJyhc78bSCSJwkgAAA4wBh",
        "paresStatus": "I",
        "acsReferenceNumber": "CardinalACS",
        "ucafCollectionIndicator": "6",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "6a0f491a-b105-498f-9997-81a02b9971ca",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "319f6440-64d6-4d49-bd27-d190bd418599",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "e91a8472-24aa-44de-a54c-4aa145e7ccd3"
    },
    "id": "7455833000666819803209",
    "issuerInformation": {
        "clearingData": "6700040102F0F1"
    },
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.99",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "brandName": "MASTERCARD",
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "bin": "520000",
            "type": "002"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "061923",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "0425MCC444569",
        "retrievalReferenceNumber": "511512061923",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "0425MCC444569",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7455833000666819803209",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-04-25T12:15:03Z",
    "tokenInformation": {
        "additionalInformation": "0"
    }
}     
```

Mastercard Identity Check Insights (IDCI) {#pa2-use-data-only-mc-intro-idci}
============================================================================

Mastercard has an IDCI data flow so that merchants can share customer data with the issuers without going through authentication. Unlike the Data Only flow, the AReq remains at the Mastercard Directory Server. Using the device information and additional data, Mastercard calculates a risk score for the transaction that is then shared with the issuer during authorization. The additional data provided to the issuer helps the issuer make risk assessments about approving cardholder transactions. Mastercard IDCI data flows are frictionless and do not affect the customer experience.  
When sending a Mastercard IDCI check enrollment request, be sure to include all of the required fields and set the consumerAuthenticationInformation.messageCategory to `80`.  
The response from the IDCI request includes this data:
* ECI = `04`
* CAVV value
* Directory server transaction ID
* paresStatus = `U`
* Risk score
* Reason code
  {#pa2-use-data-only-mc-intro-idci_ul_pdw_v4r_cfc}  
  This data from the response must be included in the authorization request.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/pts/v2/payments`  
**Test:** `POST ``https://apitest.cybersource.com``/pts/v2/payments`

Required Fields for Mastercard IDCI {#pa2-use-data-only-mc-reqd-fields-idci}
============================================================================

These fields are the minimum fields required when you request the Mastercard Data Only IDCI service. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

> IMPORTANT
> Merchants should ensure that they run the device collection and ` 3-D Secure ` Method URL portions of the flow before sending in the pa_enroll request.

Required Fields
---------------

[buyerInformation.mobilePhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-mobile-phone.md "")
:
This field is required (when available) if buyerInformation.workPhone is not used, unless market or regional mandate restricts sending this information.

[buyerInformation.workPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-work-phone.md "")
:
This field is required (when available) if buyerInformation.mobilePhone is not used, unless market or regional mandate restricts sending this information.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[customerInformation.merchantCustomerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/customer-info-merchant-customer-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
{#pa2-use-data-only-mc-reqd-fields-idci_dl_bvv_n3v_bfc}

REST Example: Mastercard IDCI {#pa2-use-data-only-mc-rest-ex-idci.dita}
=======================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "test"
        },
    "customerInformation": {
        "merchantCustomerId": "SW489TT19",
        }
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.99"
            },
    "billTo": {
        "address1": "1 Market St",
        "address2": "Address 2",
        "administrativeArea": "CA",
        "country": "US",
        "locality": "san francisco",
        "firstName": "Test",
        "lastName": "Testlastname",
        "phoneNumber": "4158880000",
        "email": "test@email.com",
        "postalCode": "94105"
        }
    },
    "paymentInformation": {
        "card": {
            "expirationMonth": "05",
            "expirationYear": "2029",
            "number":"52XXXXXXXXXX28X5"
            }
        },
    "deviceInformation": {
        "httpAcceptBrowserValue": "data",
        "httpAcceptContent": "pa_http_user_accept_value",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": false,
        "httpBrowserJavaScriptEnabled": false,
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "864",
        "httpBrowserScreenWidth": "1536",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "123"
        },
    "consumerAuthenticationInformation": {
        "deviceChannel": "Browser",
        "messageCategory": "80",
        "scoreRequest": "N"
    }
}
```

Response to Successful Request

```
 {
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "04",
        "challengeRequired": "N",
        "authenticationTransactionId": "KjNeRerYgMLXJD8gzC51",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImVjaSI6IjA0IiwiYXV0aGVudGljYXRpb25WYWx1ZSI6IkFKa0JCa2hnUVFBQUFFNGdTRUp5ZFFBQUFBQT0iLCJlZm
ZlY3RpdmVBdXRoVHlwZSI6IkZSIiwiYWNzT3BlcmF0b3JJRCI6Ik1lcmNoYW50QUNTIiwidGhyZWVEU1JlcXVlc3RvckNoYWxsZW5nZUluZCI6IjAxIiwidHJhbnNTd
GF0dXMiOiJVIiwidHJhbnNTdGF0dXNSZWFzb24iOiI4MCIsImRzVHJhbnNJRCI6IjQxMzVkMzljLWNiNDMtNGM0Zi04MWJmLTliMzc5N2QzYjhmOSIsImFjc1RyYW
5zSUQiOiI5OWIzODcyYy04ZTM2LTQ5ZGQtYjgyNi1iNGYwYzU4M2Y4MjUiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1
cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MDUzODAwIiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiO
TkwMDMzIiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiQ0FSMTM0NzNfUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN
0b3JJRCI6IkNBUjEzNDczX2RlZmF1bHQiLCJjYXJkQnJhbmQiOiJNQVNURVJDQVJEIn0=",
        "signedParesStatusReason": "80",
        "token": "AxjzbwSTlCspnzdze9IJAEQCTRdt8KnmkC4lp/UMm2OKOPlRqQoCwAAASAee",
        "paresStatus": "U",
        "acsReferenceNumber": "CardinalACS",
        "ucafCollectionIndicator": "4",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "4135d39c-cb43-4c4f-81bf-9b3797d3b8f9",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "9c4d80a0-1624-4061-8f08-78c59b335e8c",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "99b3872c-8e36-49dd-b826-b4f0c583f825"
    },
    "id": "7455594797856844403209",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2025-04-25T05:38:01Z"
}    
```

REST Example: Bundled Authentication and Authorization with Mastercard IDCI {#pa2-use-data-only-mc-bundle-rest-idci-ex.dita}
============================================================================================================================

Request

```
{
"clientReferenceInformation": {
    "code": "test"
    },   
"customerInformation": {
    "merchantCustomerId": "SW489TT19",
    }
"orderInformation": {
    "amountDetails": {
        "currency": "USD",
        "totalAmount": "10.99"
        },
"billTo": {
    "address1": "1 Market St",
    "address2": "Address 2",
    "administrativeArea": "CA",
    "country": "US",
    "locality": "san francisco",
    "firstName": "Test",
    "lastName": "Testlastname",
    "phoneNumber": "4158880000",
    "email": "test@email.com",
    "postalCode": "94105"
    }
},
"processingInformation": {
    "actionList": [
        "CONSUMER_AUTHENTICATION"
        ]
    },
"paymentInformation": {
    "card": {
        "expirationMonth": "05",
        "expirationYear": "2029",
        "number":"52XXXXXXXXXX28X5"
        }
    },
"deviceInformation": {
    "httpAcceptBrowserValue": "data",
    "httpAcceptContent": "pa_http_user_accept_value",
    "httpBrowserLanguage": "en_us",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": false,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "864",
    "httpBrowserScreenWidth": "1536",
    "httpBrowserTimeDifference": "300",
    "userAgentBrowserValue": "123"
    },
"consumerAuthenticationInformation": {
    "deviceChannel": "Browser",
    "messageCategory": "80",
    "scoreRequest": "N"
    }
}
```

Response to Successful Request

```
{
    "_links": {
        "authReversal": {
            "method": "POST",
            "href": "/pts/v2/payments/7455833000666819803209/reversals"
        },
        "self": {
            "method": "GET",
            "href": "/pts/v2/payments/7455833000666819803209"
        },
        "capture": {
            "method": "POST",
            "href": "/pts/v2/payments/7455833000666819803209/captures"
        }
    },
    "clientReferenceInformation": {
        "code": "test"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "04",
        "challengeRequired": "N",
        "authenticationTransactionId": "d94pknkLH4BhjWxylay1",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "effectiveAuthenticationType": "FR",
        "authorizationPayload": "eyJjb250YWluZXJWZXJzaW9uIjoiMSIsImVjaSI6IjA0IiwiYXV0aGVudGljYXRpb25WYWx1ZSI6IkFKa0JCa2hnUVFBQUFFNGdTRUp5ZFFBQUFBQT0iLCJlZmZlY3RpdmVBdXRoVHlwZSI6IkZSIiwiYWNzT3BlcmF0b3JJRCI6Ik1lcmNoYW50QUNTIiwidGhyZWVEU1JlcXVlc3RvckNoYWxsZW5nZUluZCI6IjAxIiwidHJhbnNTdGF0dXMiOiJVIiwidHJhbnNTdGF0dXNSZWFzb24iOiI4MCIsImRzVHJhbnNJRCI6IjZhMGY0OTFhLWIxMDUtNDk4Zi05OTk3LTgxYTAyYjk5NzFjYSIsImFjc1RyYW5zSUQiOiJlOTFhODQ3Mi0yNGFhLTQ0ZGUtYTU0Yy00YWExNDVlN2NjZDMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwibWVyY2hhbnROYW1lIjoiUEFUZXN0NCIsInB1cmNoYXNlRGF0ZSI6IjIwMjUwNDI1MTIxNTAxIiwicHVyY2hhc2VBbW91bnQiOiIxMDk5IiwibWVyY2hhbnRDb3VudHJ5Q29kZSI6Ijg0MCIsImFjcXVpcmVyQklOIjoiNDY5MjE2IiwiYWNxdWlyZXJNZXJjaGFudElEIjoiZGVmYXVsdCIsInRocmVlRFNSZXF1ZXN0b3JOYW1lIjoiUEFUZXN0NCIsInRocmVlRFNSZXF1ZXN0b3JJRCI6IjEwMDUyMjM2KjU1ZWYzZWZiZjcyM2FhNDMxYzk5YWM0ZCIsImNhcmRCcmFuZCI6Ik1BU1RFUkNBUkQifQ==",
        "signedParesStatusReason": "80",
        "token": "Axj/7wSTlC5342kEkThJAEQs3aNWrhmzYMGDZs2cMXLhgzZMHKaLtwTRfAk0Xbgmi/pAuJaf3DJtjijj5UakLAtJyhc78bSCSJwkgAAA4wBh",
        "paresStatus": "U",
        "acsReferenceNumber": "CardinalACS",
        "ucafCollectionIndicator": "4",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "6a0f491a-b105-498f-9997-81a02b9971ca",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "319f6440-64d6-4d49-bd27-d190bd418599",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "e91a8472-24aa-44de-a54c-4aa145e7ccd3"
    },
    "id": "7455833000666819803209",
    "issuerInformation": {
        "clearingData": "6700040102F0F1"
    },
    "orderInformation": {
        "amountDetails": {
            "authorizedAmount": "10.99",
            "currency": "USD"
        }
    },
    "paymentAccountInformation": {
        "card": {
            "brandName": "MASTERCARD",
            "type": "002"
        }
    },
    "paymentInformation": {
        "tokenizedCard": {
            "type": "002"
        },
        "card": {
            "bin": "520000",
            "type": "002"
        }
    },
    "processorInformation": {
        "systemTraceAuditNumber": "061923",
        "approvalCode": "831000",
        "merchantAdvice": {
            "code": "01",
            "codeRaw": "M001"
        },
        "responseDetails": "ABC",
        "networkTransactionId": "0425MCC444569",
        "retrievalReferenceNumber": "511512061923",
        "consumerAuthenticationResponse": {
            "code": "2",
            "codeRaw": "2"
        },
        "transactionId": "0425MCC444569",
        "responseCode": "00",
        "avs": {
            "code": "Y",
            "codeRaw": "Y"
        }
    },
    "reconciliationId": "7455833000666819803209",
    "status": "AUTHORIZED",
    "submitTimeUtc": "2025-04-25T12:15:03Z",
    "tokenInformation": {
        "additionalInformation": "0"
    }
}     
```

Authentication Examples Using Digital Payment (Google Pay) {#pa2-use-digital-payment-google}
============================================================================================

Digital payments are electronic payments that transfer funds from one payment account to another. These use cases demonstrate how the authentication service works using a digital payment method like Google Pay.

Setting Up Device Data Collection Using Digital Payment (Google Pay) {#pa2-setup-google-use-intro}
==================================================================================================

Running the Setup service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. This use case demonstrates how the service works using a digital payment method like Google Pay.

Card-Specific Requirements {#pa2-setup-google-use-intro_card-specific}
----------------------------------------------------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-setup-google-use-intro_dl_d1v_trz_rxb}

Country-Specific Requirements {#pa2-setup-google-use-intro_country-specific-R}
------------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-setup-google-use-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in merchant configuration during merchant boarding.
{#pa2-setup-google-use-intro_dl__1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for Device Data Collection {#id__rfc}
-----------------------------------------------------

These fields are the minimum fields required when you request the Payer Authentication Setup service. Other fields that can be used to collect additional information during a transaction are listed in the optional fields section. Under certain circumstances, a field that is normally optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field field value is `US` or `CA`.

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "") paymentInformation.card.type
:
This field is required when the card type is Cartes Bancaires, JCB, China UnionPay, or Meeza.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Device Data Collection {#id_qpk_cc}
-------------------------------------------------------

These fields are optional for setting up a Payer Authentication transaction. Under certain circumstances, a field might appear as both an optional field and a required field.

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
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

REST Example: Setting Up Device Data Collection When Using Digital Payment (Google Pay) {#pa2-use-setup-google-rest-ex}
=======================================================================================================================

Request

```
 {
  "paymentInformation": {
"fluidData" : {
      "value" : "eyJzaWduYXR1cmUiOiJNRVFDSUVhVVBmc1RIMERyMnZmeG8wVkFlZ3N2bHlSRzdENEFsYmRwa1pPdlNzZGtBaUFVO
                        DE2aHpmMG5BMzJzQmx6anlUSURyZXBHNUY1eEtlRmNnSE9aK3RML2ZRXHUwMDNkXHUwMDNkIiwiaW50ZXJtZW
                        RpYXRlU2lnbmluZ0tleSI6eyJzaWduZWRLZXkiOiJ7XCJrZXlWYWx1ZVwiOlwiTUZrd0V3WUhLb1pJemowQ0FRWUlLb1p
                        JemowREFRY0RRZ0FFOFdKSHVMOFVuWW9WWDNHV3dGVkJpcnh6L3lJdGl0aW9neWhDeGpCRm5tS3pCcWs2K3ln
                        VU5SUGF4THdaaWtILzBxV0s1QXhlc3BDNVhwN1NHNUN1T1FcXHUwMDNkXFx1MDAzZF wiLFwia2V5RXhwaXJhdG
                        lvblwiOlwiMTYzMDUxNjYyODA0OVwifSIsInNpZ25hdHVyZXMiOlsiTUVVQ0lRRHlTQTV 1T2t5UXQ5cFoyQlEzaXBmcG
                        NWT0F5ZmIzM2ozUEZPQUw3K1o5S3dJZ2FjWWp2YWJpTEUyWHFkNU1xNGphNStEVldoREttVHpoMmk1RGlnbllFQ
                        ndcdTAwM2QiXX0sInByb3RvY29sVmVyc2lvbi I6IkVDdjIiLCJzaWduZWRNZXNzYWdlIjoie1wiZW5jcnlwdGVkTWVzc2F
                        nZVwiOlwiWG5qOGxSSWhGMDVEWWdRK3hwNEE5YUhsVGE1U2ljdUJac2w1L2NNRkJlclBBY1RzaE4zRFlOb1MvdE
                        VkRkRYRzZJRXBpVlcxVnV6OUprejNWWGdpMzJrT21EVk9aakJNWTFvVHdTQnA5WG53ejlLYUtOekYvRFBSTy9jbStob
                        W9iZ2dSdmxGSStOekN5U1VNWW1hbTJjZFUyZGRZWmZHck9nZWNSc3FrdW1tNmlMa0xGQTFJcDFrNWFRV21EUE
                        lEdTh1SnNmbWs4bzMyMlpteVdMMVVWenE0WHFkNTZScXZoL1VFeEp3RC9HZXU5SW00M0pmblZqckVkeDE0Ykx1
                        OUpmMHJrcU5ONG5sM0NVZEFoMVNhZnBzdkduTVRML1Nmenk1ZGdDZlRDcHJDdW85UVZPaXVValBJNUdXRlBKS
                        WVVVVU1cUZhcis3NXFBT2dvZ0tNRUZ3OFVxL1A0UjBDcXczcFllNnc2enlaVzdDV1YxRzRMc3BITTNRaE83bFZNNmR
                        jSWZQWW00ZitubWI3UzgwY29KTXR1QjkxVEhjZzJmVXhwM2FrWEhSdzNyN3BRZk9KWWFieUlURmtieDh0Yi9ieWl6
                        VUZEVVU4S3EwTmVCVTVrQng2L21qUDg4bWxoWkE2ZERrNWJVc2o4SDBDSk9nWUtCbVgyR09vamRtTDd5YlBnTU
                        5vNnhsYjRtUzVkaTJjZUpFakFybEZFa3NWNTlsS2lodk5pckRZc1BTU2lTRFVZNjBMUXVuTEErYjFMSnpCMkpYelFcIixcI
                        mVwaGVtZXJhbFB1YmxpY0tleVwiOlwiQk84bmtEbE0ycVlCQmpQd00wbDdUTFY2UytUbzZDTFl0eXArWGM2cXpQY
                        klLTEgxVytySGh3NUlwU2lqb1lTb3VaclNuWU9LV21yRVAyYmtLMk4rTWFZXFx1MDAzZFwiLFwidGFnXCI6XCJuVU5x
                        UVlxcy9YRVlDMmg0WFlibnVpajFLb1NzUFpacEpqVGI4TVVZcUZNXFx1MDAzZFwifSJ9"
    }
  },
  "processingInformation": {
    "paymentSolution": "012"
  }
}
```

Response to Successful Request

```
{
  "consumerAuthenticationInformation": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5MjlhZDAwYy0zZmEyLTQ5ODgtODRjNC1hYTcxMGFlY2I1
                                  OGEiLCJpYXQiOjE2Mjk4MjY5NjAsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTYyOTg
                                  zMDU2MCwiT3JnVW5pdElkIjoiNWI5YzRiYjNmZjYyNmIxMzQ0ODEwYTAxIiwiUmVmZXJlbmNlSWQiOiI5NDkz
                                  ZjJiZi04NmIwLTQ0ZmYtYmJjZS0wZjU1MjNlMWIzNGEifQ.FgVbwbW9_lwnlr4ovYR5VVPuVl6CklAVHHXS_5OD
                                  skA",
    "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
    "referenceId": "9493f2bf-86b0-44ff-bbce-0f5523e1b34a",
    "token": "AxizbwSTVW4Mj1fvsU27ABEBURxPZebOAE1IZNJMvRiuZhTA9AAA+QBf"
  },
  "id": "6298269599786696003003",
  "status": "COMPLETED",
  "submitTimeUtc": "2022-08-24T17:42:40Z"
}
```

Checking Enrollment in Payer Authentication Using Digital Payment (Google Pay) {#pa2-use-check-enroll-google-intro}
===================================================================================================================

Running the Check Enrollment service collects data about the device that the customer is using to place the order and verifies that the customer is enrolled in a payer authentication program. This use case demonstrates how the service works with a digital payment method like Google Pay.

Card-Specific Requirements {#pa2-use-check-enroll-google-intro_card-specific-Rest}
----------------------------------------------------------------------------------

Some payment cards require information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (U.S.) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-check-enroll-google-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is Cartes Bancaires, JCB, China UnionPay, or Meeza.

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-check-enroll-google-intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA`, `US`, or `China`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2-use-check-enroll-google-intro_section_kl3_tbh_xwb}
----------------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Required Fields for Checking Enrollment in Payer Authentication {#id_t24_l5m_rfc}
---------------------------------------------------------------------------------

These fields are the minimum fields required for verifying that a customer is enrolled in a payer authentation program. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[buyerInformation.mobilePhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-mobile-phone.md "")
:
This field is required (when available) if buyerInformation.workPhone is not used, unless market or regional mandate restricts sending this information.

[buyerInformation.workPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/buyer-info-aa/buyer-info-work-phone.md "")
:
This field is required (when available) if buyerInformation.mobilePhone is not used, unless market or regional mandate restricts sending this information.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
This field is required for SDK integration. When you use the SDK integration, this field is dynamically set to `SDK`. When you use the JavaScript code, this field is dynamically set to `Browser`. For merchant-initiated or 3RI transactions, you must set the field to `3RI`. When you use this field in addition to JavaScript code, you must set the field to `Browser`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
For non-payment authentication, set to a value of `02`.

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[consumerAuthenticationInformation.returnUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-return-url.md "")
:

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[deviceInformation.httpAcceptBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-browser-value.md "")
:

[deviceInformation.httpAcceptContent](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-content.md "")
:

[deviceInformation.httpBrowserColorDepth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-color-depth.md "")
:

[deviceInformation.httpBrowserJavaEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-enabled.md "")
:

[deviceInformation.httpBrowserJavaScriptEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-script-enabled.md "")
:

[deviceInformation.httpBrowserLanguage](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-language.md "")
:

[deviceInformation.httpBrowserScreenHeight](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-height.md "")
:

[deviceInformation.httpBrowserScreenWidth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-width.md "")
:

[deviceInformation.httpBrowserTimeDifference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-time-diff.md "")
:

[deviceInformation.ipAddress](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-ip-address.md "")
:

[deviceInformation.userAgentBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-user-agent-browser-value.md "")
:
When the customer's browser provides this value, you must include that value in your request.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:
This field is required when the paymentInformation.card.number field is included.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Checking Enrollment in Payer Authentication {#id_j33_w5m_rfc}
---------------------------------------------------------------------------------

These fields are usually optional when you verify enrollment for a Payer Authentication transaction. In certain circumstances, the information provided by an optional field might be required before a transaction can proceed. Those optional fields that are sometimes required are also listed as required fields with the circumstance described.

[acquirerInformation.bin](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-acquirer-bin.md "")
:

[acquirerInformation.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-country.md "")
:

[acquirerInformation.merchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/acq-info-aa/acq-info-merchant-id.md "")
:

[clientReferenceInformation.code](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/client-ref-info-aa/client-ref-info-code.md "")
:

[consumerAuthenticationInformation.acsWindowSize](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-acs-window-size.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-data.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-date.md "")
:

[consumerAuthenticationInformation.alternateAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-alternate-auth-method.md "")
:

[consumerAuthenticationInformation. authenticationBrand](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-brand.md "")
:
This field is only used with mada cards.

[consumerAuthenticationInformation.authenticationTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-txn-id.md "")
:

[consumerAuthenticationInformation.authorizationPayload](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authorization-payload.md "")
:

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
> WARNING Modifying this field could affect your liability shifts. Unless you are very familiar with the various types of authentication, do not change the default settings before consulting with customer support.

[consumerAuthenticationInformation.credentialEncrypted](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-credential-encrypted.md "")
:

[consumerAuthenticationInformation.customerCardAlias](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-customer-card-alias.md "")
:

[consumerAuthenticationInformation.sdkMaxTimeout](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-sdk-max-timeout.md "")
:

[consumerAuthenticationInformation.decoupledAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-decouple-auth-indicator.md "")
:

[consumerAuthenticationInformation.decoupledAuthenticationMaxTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-decouple-auth-max-time.md "")
:

[consumerAuthenticationInformation.default Card](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation. marketingOptIn](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-marketing-opt-in.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation. marketingSource](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-marketing-source.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:

[consumerAuthenticationInformation.merchantFraudRate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-fraud-rate.md "")
:

[consumerAuthenticationInformation.merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:

[consumerAuthenticationInformation.messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:

[consumerAuthenticationInformation.otpTo ken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-otp-token.md "")
:

[consumerAuthenticationInformation.overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:

[consumerAuthenticationInformation.overridePaymentMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:

[consumerAuthenticationInformation.prior AuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-data.md "")
:

[consumerAuthenticationInformation.priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:

[consumerAuthenticationInformation.priorAuthenticationReferenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-reference-id.md "")
:

[consumerAuthenticationInformation.priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[consumerAuthenticationInformation.productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:

[consumerAuthenticationInformation.requestorName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-name.md "")
:

[consumerAuthenticationInformation.requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:

[consumerAuthenticationInformation.returnURL](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-return-url.md "")
:

[consumerAuthenticationInformation.scoreRequest](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-score-request.md "")
:

[consumerAuthenticationInformation.sdkMaxTimeout](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-score-request.md "")
:

[consumerAuthenticationInformation.strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:

[consumerAuthenticationInformation.strongAuthentication.secureCorporate PaymentIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-secure-corp-payment-id.md "")
:

[consumerAuthenticationInformation.strongAuthentication.transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-txn-mode.md "")
:

[consumerAuthenticationInformation.whiteListStatus](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-white-list-status-a.md "")
:

[merchantInformation.merchantDescriptor.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:

[merchantInformation.merchantDescriptor.url](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-url.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
This field is required for US and Canada.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.lineItems.passenger.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-passenger-firstname.md "")
:

[orderInformation.lineItems.passenger.last Name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-passenger-lastname.md "")
:

[orderInformation.lineItems.productDescription](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-description.md "")
:

[orderInformation.lineItems.productName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-name.md "")
:

[orderInformation.lineItems.productSku](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-product-sku.md "")
:

[orderInformation.lineItems.quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems.shippingAddress1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-address1.md "")
:

[orderInformation.lineItems.shippingAddress2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-address2.md "")
:

[orderInformation.lineItems.shippingCity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-city.md "")
:

[orderInformation.lineItems.shippingCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-country-code.md "")
:

[orderInformation.lineItems.shippingDestinationTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-destination-types.md "")
:

[orderInformation.lineItems.shippingLastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-last-name.md "")
:

[orderInformation.lineItems.shippingMiddleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-middle-name.md "")
:

[orderInformation.lineItems.shippingPhone](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-phone.md "")
:

[orderInformation.lineItems.shippingPostalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-postal-code.md "")
:

[orderInformation.lineItems.shippingState](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-state.md "")
:

[orderInformation.lineItems.unitPrice](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-unit-price.md "")
:

[orderInformation.lineItems\[\].quantity](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-quantity.md "")
:

[orderInformation.lineItems\[\].totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-total-amount.md "")
:

[orderInformation.lineItems.shippingDestinationTypes](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-line-items-shipping-destination-types.md "")
:

[orderInformation.reordered](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-reordered.md "")
:

[orderInformation.shippingDetails.shippingMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipping-details-shipping-method.md "")
:

[orderInformation.shipTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:

[orderInformation.shipTo.address3](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address3.md "")
:

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:

[orderInformation.shipTo.destinationCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-destination-code.md "")
:

[orderInformation.shipTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-email.md "")
:

[orderInformation.shipTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-first-name.md "")
:

[orderInformation.shipTo.middleName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-locality.md "")
:

[orderInformation.shipTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-phone-num.md "")
:

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:

[orderInformation.totalOffersCount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-total-offers-count.md "")
:

[paymentInformation.card.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:
This field is strongly recommended.

[paymentInformation.card.securityCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-security-code-a.md "")
:

[paymentInformation.fluidData.value](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-fluid-data-value.md "")
:

[paymentInformation.tokenizedCard. cryptogram](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-cryptogram.md "")
:
This field is strongly recommended.

[paymentInformation.tokenizedcard.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedcard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-number.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:

[recurringPaymentsInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:
When this field is empty, the current date is used.

riskInformation.buyerHistory. transactionCountDay
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountYear
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. accountPurchases
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. addCardAttempts
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.createDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.lastChangeDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.passwordChangeDate
:
This field is recommended for Discover ProtectBuy. Contact customer support for more information about this field.

riskInformation.buyerHistory. customerAccount.shipAddressUsageDate
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. paymentAccountDate
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. priorSuspiciousActivity
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountDay
:
Contact customer support for more information about this field.

riskInformation.buyerHistory. transactionCountYear
:
Contact customer support for more information about this field.

[travelInformation.legs.carrierCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-transit-airline-legs-carrier-code.md "")
:

[travelInformation.legs.departureDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-legs-departure-date.md "")
:

[travelInformation.legs.origination](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-legs-origin.md "")
:

[travelInformation.numberOfPassengers](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-numpassengers.md "")
:

[travelInformation.passengers.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-passengers-firstname.md "")
:

[travelInformation.passengers.lastName](hhttps://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/travel-info-aa/travel-info-passengers-lastname.md "")
:

REST Example: Checking Enrollment in Payer Authentication Using Google Pay {#pa2-use-check-enroll-google-rest-ex}
=================================================================================================================

Request

```
{
   "orderInformation": {
     "amountDetails": {
       "currency": "USD",
       "totalAmount": "10.99"
     },
     "billTo": {
       "address1": "1 Market St",
       "address2": "Address 2",
       "administrativeArea": "CA",
       "country": "US",
       "locality": "san francisco",
       "firstName": "John",
       "lastName": "Doe",
       "phoneNumber": "4158880000",
       "email": "test@email.com",
       "postalCode": "94105"
      }
    },
     "paymentInformation": {
"fluidData" : {
      "value" : "eyJzaWduYXR1cmUiOiJNRVFDSUVhVVBmc1RIMERyMnZmeG8wVkFlZ3N2bHlSRzdENEFsYmRwa1pPdlNzZGtBaUFVO
                 DE2aHpmMG5BMzJzQmx6anlUSURyZXBHNUY1eEtlRmNnSE9aK3RML2ZRXHUwMDNkXHUwMDNkIiwiaW50ZXJtZWRpYX
                 RlU2lnbmluZ0tleSI6eyJzaWduZWRLZXkiOiJ7XCJrZXlWYWx1ZVwiOlwiTUZrd0V3WUhLb1pJemowQ0FRWUlLb1p
                 JemowREFRY0RRZ0FFOFdKSHVMOFVuWW9WWDNHV3dGVkJpcnh6L3lJdGl0aW9neWhDeGpCRm5tS3pCcWs2K3lnVU5S
                 UGF4THdaaWtILzBxV0s1QXhlc3BDNVhwN1NHNUN1T1FcXHUwMDNkXFx1MDAzZFwiLFwia2V5RXhwaXJhdGlvblwiOlwiM
                 TYzMDUxNjYyODA0OVwifSIsInNpZ25hdHVyZXMiOlsiTUVVQ0lRRHlTQTV1T2t5UXQ5cFoyQlEzaXBmcGNWT0F5ZmIzM2oz
                 UEZPQUw3K1o5S3dJZ2FjWWp2YWJpTEUyWHFkNU1xNGphNStEVldoREttVHpoMmk1RGlnbllFQndcdTAwM2QiXX0sInByb
                 3RvY29sVmVyc2lvbiI6IkVDdjIiLCJzaWduZWRNZXNzYWdlIjoie1wiZW5jcnlwdGVkTWVzc2FnZVwiOlwiWG5qOGxSSWhGMD
                 VEWWdRK3hwNEE5YUhsVGE1U2ljdUJac2w1L2NNRkJlclBBY1RzaE4zRFl Ob1MvdEVkRkRYRzZJRXBpVlcxVnV6OUprejNW
                 WGdpMzJrT21EVk9aakJNWTFvVHdTQnA5WG53ejlLYUtOekYvRFBSTy9jbStobW9iZ2dSdmxGSStOekN5U1VNWW1hbTJjZ
                 FUyZGRZWmZHck9nZWNSc3FrdW1tNmlMa0xGQTFJcDFrNWFRV21EUElEdTh1SnNmbWs4bzMyMlpteVdMMVVWenE0W
                 HFkNTZScXZoL1VFeEp3RC9HZXU5SW00M0pmblZqckVkeDE0Ykx1OUpmMHJrcU5ONG5sM0NVZEFoMVNhZnBzdkduTVR
                 ML1Nmenk1ZGdDZlRDcHJDdW85UVZPaXVValBJNUdXRlBKSWVVVVU1cUZhcis3NXFBT2dvZ0tNRUZ3OFVxL1A0UjBDcXcz
                 cFllNnc2enlaVzdDV1YxRzRMc3BITTNRaE83bFZNNmRjSWZQWW00ZitubWI3UzgwY29KTXR1QjkxVEhjZzJmVXhwM2FrWE
                 hSdzNyN3BRZk9KWWFieUlURmtieDh0Yi9ieWl6VUZEVVU4S3EwTmVCVTVrQng2L21qUDg4bWxoWkE2ZERrNWJVc2o4SD
                 BDSk9nWUtCbVgyR09vamRtTDd5YlBnTU5vNnhsYjRtUzVkaTJjZUpFakFybEZFa3NWNTlsS2lodk5pckRZc1BTU2lTRFVZNjB
                 MUXVuTEErYjFMSnpCMkpYelFcIixcImVwaGVtZXJhbFB1YmxpY0tleVwiOlwiQk84bmtEbE0ycVlCQmpQd00wbDdUTFY2Uy
                 tUbzZDTFl0eXArWGM2cXpQYklLTEgxVytySGh3NUlwU2lqb1lTb3VaclNuWU9LV21yRVAyYmtLMk4rTWFZXFx1MDAzZFwiL
                 FwidGFnXCI6XCJuVU5xUVlxcy9YRVlDMmg0WFlibnVpajFLb1NzUFpacEpqVGI4TVVZcUZNXFx1MDAzZFwifSJ9"
     }
   },
   "processingInformation": {
      "paymentSolution": "012"
   },
   "buyerInformation": {  
    "merchantCustomerId": "334124572" 
    "mobilePhone": "1245789632"
   },
   "consumerAuthenticationInformation": {
     "transactionMode": "MOTO"
   }
}
        
```

Response to a Successful Request

```
{
  "clientReferenceInformation": {
    "code": "1726870134497"
  },
  "consumerAuthenticationInformation": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5MjlhZDAwYy0zZmEyLTQ5ODgtODRjNC1hYTcxMGFl Y2I1OGEiLCJpYXQiOjE2Mjk4MjY5NjAsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTYyOTgz MDU2MCwiT3JnVW5pdElkIjoiNWI5YzRiYjNmZjYyNmIxMzQ0ODEwYTAxIiwiUmVmZXJlbmNlSWQiOiI5NDkzZjJiZi0 4NmIwLTQ0ZmYtYmJjZS0wZjU1MjNlMWIzNGEifQ.FgVbwbW9_lwnlr4ovYR5VVPuVl6CklAVHHXS_5ODskA",
    "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
    "referenceId": "9493f2bf-86b0-44ff-bbce-0f5523e1b34a",
    "token": "AxizbwSTVW4Mj1fvsU27ABEBURxPZebOAE1IZNJMvRiuZhTA9AAA+QBf"
  },
  "id": "6298269599786696003003",
  "status": "COMPLETED",
  "submitTimeUtc": "2022-08-24T17:42:40Z"
}
```

Validating a Challenge Using Digital Payment (Google Pay) {#pa2-use-validate-google-intro}
==========================================================================================

Running the Validation service compares the customer's response to the challenge from the issuing bank to validate the customer identity.

Card-Specific Requirements {#pa2-use-validate-google-intro_card-specific-REST}
------------------------------------------------------------------------------

Some payment cards require additional information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airlinepurchase).

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-validate-google-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US)

Country-Specific Requirements {#pa2-use-validate-google-intro_country-specific-REST}
------------------------------------------------------------------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-validate-google-intro_dl_gpf_5rz_rxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-results`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-results`

Required Fields for Validating Payer Authentication {#id_fyh_nvm_rfc}
---------------------------------------------------------------------

These fields are the minimum fields required when requesting the Payer Authentication Validation service. Other fields to collect additional information during a transaction are available in the list of optional fields. Under certain circumstances, some of the fields that are normally optional may be required. The circumstances that make an optional field, a required field, are noted.

authenticationTransactionID
:

clientReferenceInformation.code
:

merchantID
:

orderInformation.amountDetails.currency
:

orderInformation.amountDetails.total Amount
:
Required when the orderInformation.lineItems.unitPrice field is not used.

orderInformation.lineItems.unitPrice
:
Required when the orderInformation.amountDetails.totalAmount field is not used.

paymentInformation.card.number
:

paymentInformation.card.type
:

paymentInformation.card.expirationMonth
:
Required when paymentInformation.card.number is not included.

paymentInformation.card.expirationYear
:
Required when paymentInformation.card.number is included.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

Optional Fields for Validating a Challenge {#id_imp_vvm_rfc}
------------------------------------------------------------

These fields are optional when validating a Payer Authentication transaction. In certain circumstances, the information provided by an optional field might be required before a transaction can proceed. Those optional fields that are sometimes required are listed in the required fields with the circumstance described.

[consumerAuthenticationInformation. authenticationBrand](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-brand.md "")
:
This field is only used with mada cards.

[consumerAuthenticationInformation.credentialEncrypted](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-credential-encrypted.md "")
:

[consumerAuthenticationInformation.responseAccessToken](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-response-access-token.md "")
:

[consumerAuthenticationInformation.signedPares](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-signed-pares.md "")
:

REST Example: Validating a Challenge When Using Google Pay {#pa2-use-validate-google-rest-ex}
=============================================================================================

Request

```
{ 
  "orderInformation": {
      "amountDetails": {
      "currency": "USD",
      "totalAmount": "200.00
      }, 
   "lineItems": [ {         
      "unitPrice": "10",
      "quantity": "2", 
      "taxAmount": "32.40"       
      } ]  
 }, "paymentInformation": {
      "card": {      
         "type": "002",       
         "expirationMonth": "12",       
         "expirationYear": "2025",
         "number": "5200000000000007"     
         },     
     "fluidData": {      
         "value":"XFx1MDAzZFwiLFwia2V5RXhwaXJhdGlvblwiOlwiMTYzMDUxNjYyODA0OVwifSIsInNpZ25hdHVyZXMiOlsiTUV
                  VQ0lRRHlTQTV1T2t5UXQ5cFoyQlEzaXBmcGNWT0F5ZmIzM2ozUEZPQUw3K1o5S3dJZ2FjWWp2YWJpTEUyWHFkNU1
                  xNGphNStEVldoREttVHpoMmk1RGlnbllFQndcdTAwM2QiXX0sInByb3RvY29sVmVyc2lvbiI6IkVDdjIiLCJzaWduZW
                  RNZXNzYWdlIjoie1wiZW5jcnlwdGVkTWVzc2FnZVwiOlwiWG5qOGxSSWhGMDVEWWdRK3hwNEE5YUhsVGE1U
                  2ljdUJac2w1L2NNRkJlclBBY1RzaE4zRFlOb1MvdEVkRkRYRzZJRXBpVlcxVnV6OUprejNWWGdpMzJrT21EVk9aakJ
                  NWTFvVHdTQnA5WG53ejlLYUtOekYvRFBSTy9jbStobW9iZ2dSdmxGSStOekN5U1VNWW1hbTJjZFUyZGRZWmZH
                  ck9nZWNSc3FrdW1tNmlMa0xGQTFJcDFrNWFRV21EUElEdTh1SnNmbWs4bzMyMlpteVdMMVVWenE0WHFkNT
                  ZScXZoL1VFeEp3RC9HZXU5SW00M0pmblZqckVkeDE0Ykx1OUpm"     
         }   
      },
      "consumerAuthenticationInformation": {     
         "authenticationTransactionId": "PYffv9G3sa1e0CQr5fV0"   
      } 
 }
```

Response to a Successful Request

```
{    
   "clientReferenceInformation": {
     "code": "1675288043120"
   },
   "consumerAuthenticationInformation": {
     "indicator": "internet",
     "ucafCollectionIndicator": "0",
     "strongAuthentication": {
     "OutageExemptionIndicator": "0"
     },
   "token": "AxjzbwSTbhMKrRswWTYSABECT9u+QBvfSB84gL2IZNJMvRiyubWAOAAA+Qxb"
    },
   "id": "6752880430346470503954",
   "status": "AUTHENTICATION_SUCCESSFUL",
   "submitTimeUtc": "2023-02-01T21:47:23Z"
}
```

Authentication Examples Using TMS Tokens {#pa2-use-tokens-tms}
==============================================================

These examples list the API fields that are required for the Setup, Check Enrollment, and Validate Authentication services when using TMS tokens. An example of a request payload and a successful response that occurs with each service is provided.

Setting Up Device Data Collection with a TMS Token {#pa2-use-token-tms-setup-intro}
===================================================================================

Running the Setup service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. In this scenario, a TMS token is used instead of the card.

Card-Specific Requirements
--------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-use-token-tms-setup-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-token-tms-setup-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.
{#pa2-use-token-tms-setup-intro_dl_kcl_pkc_1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for Setting Up Data Collection When Using a TMS Token {#pa2-use-setup-token-tms-card-reqd-fields}
=================================================================================================================

These fields are the minimum fields required when you request the Payer Authentication Setup service. Other fields that can be used to collect additional information during a transaction are listed in the optional fields section. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Setting Up Device Data Collection When Using a TMS Token {#pa2-use-token-tms-setup-rest-ex}
=========================================================================================================

Request

```
{
  "paymentInformation": {
      "card": {
      "expirationMonth": "05",
      "expirationYear": "2029"
    },
    "customer": {
      "customerId": "1108590036500854"
    }
  }
}
```

Response to Successful Request

```
{
    "consumerAuthenticationInformation": {
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey JqdGkiOiIxZmQ5ZWIyNi1jOTY1LTRkZmEtYTM5Yy1hZDExMGU2NjQ3ZmMiLCJpYXQi OjE3MjUzNDcwNDksImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4 cCI6MTcyNTM1MDY0OSwiT3JnVW5pdElkIjoiNjY0MWRiMGZmOTRmNzI3ZjU0Y2RlO TQ2IiwiUmVmZXJlbmNlSWQiOiIzZGM2ZDhmZS1lM2I1LTQyMTItYWY5MC1jNDcxYj czMTYwMjAifQ.90_yhusiQL9Yq10221zB04vZAKaiGnQ2ryvakeyuk1k",
        "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
        "referenceId": "3dc6d8fe-e3b5-4212-af90-c471b7316020",
        "token": "AxizbwSTiTYf1D7m/jQkAG8BT34jOu4gAhLwyaSZejF9z2oA8AAA0gbV"
    },
    "id": "7253470490136808404004",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-09-03T07:04:09Z"
}     
```

Checking Enrollment When Using a TMS Token {#pa2-check-enroll-token-use-intro}
==============================================================================

Running the Check Enrollment service identifies the customer's bank and collects data about the device that the customer is using to place the order. This use case demostrates this process while using a TMS token.

Card-Specific Requirements
--------------------------

Some payment cards require additional information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-check-enroll-token-use-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
:
This field is required when the card type is Cartes Bancaires, JCB, China UnionPay, or Meeza.

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-check-enroll-token-use-intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA` or `US`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2-check-enroll-token-use-intro_section_kl3_tbh_xwb}
---------------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Required Fields for Checking Enrollment in Payer Authentication While Using a TMS Token {#pa2-use-enroll-token-tms-reqd-fields}
===============================================================================================================================

These fields are the minimum fields required for verifying that a customer is enrolled in a payer authentication program. It doesn't matter if the enrollment check is frictionless or results in a challenge, the same fields are required in the request. The fields in the response will differ.

Required Fields
---------------

[consumerAuthenticationInformation.deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[paymentInformation.customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[deviceInformation.httpAcceptBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-browser-value.md "")
:

[deviceInformation.httpAcceptContent](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-content.md "")
:

[deviceInformation.httpBrowserColorDepth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-color-depth.md "")
:

[deviceInformation.httpBrowserJavaEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-enabled.md "")
:

[deviceInformation.httpBrowserJavaScript Enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-script-enabled.md "")
:

[deviceInformation.httpBrowserLanguage](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-language.md "")
:

[deviceInformation.httpBrowserScreenHeight](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-height.md "")
:

[deviceInformation.httpBrowserScreenWidth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-width.md "")
:

[deviceInformation.httpBrowserTimeDif ference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-time-diff.md "")
:

[deviceInformation.ipAddress](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-ip-address.md "")
:

[deviceInformation.userAgentBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-user-agent-browser-value.md "")
:
When the customer's browser provides this value, you must include that value in your request.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment When Using a TMS Token {#pa2-use-token-tms-enroll-frictionlesx-rest-ex}
=========================================================================================================

Request

```
{
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": "10.99"
    },
    "billTo": {
      "address1": "1 Market St",
      "address2": "Address 2",
      "administrativeArea": "CA",
      "country": "US",
      "locality": "san francisco",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "4158880000",
      "email": "test@email.com",
      "postalCode": "94105"
    }
  },
  "paymentInformation": {
      "card": {
      "expirationMonth": "05",
      "expirationYear": "2029"
    },
    "customer": {
      "customerId": "1108590036500854"
    }
  },
  "deviceInformation": {
    "httpAcceptBrowserValue": "data",
    "httpAcceptContent": "pa_http_user_accept_value",
    "httpBrowserLanguage": "en_us",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": false,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "864",
    "httpBrowserScreenWidth": "1536",
    "httpBrowserTimeDifference": "300",
    "userAgentBrowserValue": "123"
  },
  "consumerAuthenticationInformation": {
    "deviceChannel": "Browser",

    "referenceId": "CybsCruiseTester-6259e7e2"
  }
}
```

Frictionless Response to Request

```
{
    "consumerAuthenticationInformation": {
        "eciRaw": "05",
        "authenticationTransactionId": "e2elnNP8zJ2J67lKcaX0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "eci": "05",
        "token": "AxjzbwSTiTYllZBAC15FAG8BT34jOzxHSBcS0JeGTSTL0Yvue1AHgAAAyxUk",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "3859eace-2a42-4bd7-9252-8507f02d5edd",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "932a3c41-880d-4791-a98f-c6beaef90b23",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "vbv",
        "specificationVersion": "2.1.0",
        "acsTransactionId": "54ef7fd4-e93d-42de-82ba-ad91dd21c94c"
    },
    "id": "7253472110066822504005",
    "paymentInformation": {
        "card": {
            "bin": "400009",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-03T07:06:51Z"
}     
```

Challenge Response to Request

```
{
  "consumerAuthenticationInformation": {
    "challengeRequired": "N",
    "authenticationTransactionId": "z7BruZ1qn416WGknmAX0",
    "strongAuthentication": {
       "OutageExemptionIndicator": "0"
       },
    "token": "AxjzbwSTiTcMOwhjPANlAG8BT34jQMsnSBcS0JddrSTL0Yvue1AIAAAA+AWf",
    "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
    "acsReferenceNumber": "Cardinal ACS",
    "stepUpUrl": "https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp",
    "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMS4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiI0ZTUwZjU4Ni1iMTVjLTRjMDMtYTE4Ni1lYWZiNDBkNTBiODAiLCJhY3NUcmFuc0lEIjoiMzg4OGUxNTMtNmI5Ny00ZjQzLWFmZWUtNjA1MjdjMmUwYjkxIiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
    "directoryServerTransactionId": "2f44602b-ce95-4a7e-9ad1-920e7ace0676",
    "veresEnrolled": "Y",
    "threeDSServerTransactionId": "4e50f586-b15c-4c03-a186-eafb40d50b80",
    "acsOperatorID": "MerchantACS",
    "specificationVersion": "2.1.0",
    "acsTransactionId": "3888e153-6b97-4f43-afee-60527c2e0b91"
  },
  "errorInformation": {
     "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
     "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
     },
  "id": "7253537031246871004005",
  "paymentInformation": {
     "card": {
       "bin": "400009",
       "type" : "CARD"
     }
  },
  "status": "PENDING_AUTHENTICATION",
  "submitTimeUtc": "2024-09-03T08:55:03Z"
}     
```

Validating a Challenge When Using a TMS Token {#pa2-use-token-tms-validate-intro}
=================================================================================

Running the Validation service compares the customer's response to the challenge from the issuing bank to validate the customer identity.

Card-Specific Requirements
--------------------------

Some payment cards require additional information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airlinepurchase).

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-token-tms-validate-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US)

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-token-tms-validate-intro_dl_gpf_5rz_rxb}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-results`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-results`

Required Fields for Validating a Challenge When Using a TMS Token {#pa2-use-validate-token-tms-reqd-fields}
===========================================================================================================

These fields are the minimum fields required when you request the Payer Authentication Validation service. Other fields that can be used to collect additional information during a transaction are listed in the optional fields section. Under certain circumstances, a field that normally is optional might be required. The circumstance that makes an optional field required is noted.

Required Fields
---------------

[consumerAuthenticationInformation.authenticationTransactionId](https://developer.example.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-txn-id.md "")
:

REST Example: Validating a Challenge When Using a TMS Token {#pa2-use-token-tms-validate-challenge-rest-ex}
===========================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "z7BruZ1qn416WGknmAX0"
    }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "indicator": "vbv",
        "eciRaw": "05",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "eci": "05",
        "token": "AxijLwSTiTcQGTMcD52lAG9PfiNA2ogCEvDJpJl6MX3PagAAmh21",
        "cavv": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "paresStatus": "Y",
        "xid": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "2f44602b-ce95-4a7e-9ad1-920e7ace0676",
        "threeDSServerTransactionId": "4e50f586-b15c-4c03-a186-eafb40d50b80",
        "specificationVersion": "2.1.0",
        "acsTransactionId": "3888e153-6b97-4f43-afee-60527c2e0b91"
    },
    "id": "7253538119946872004005",
    "paymentInformation": {
        "card": {
            "bin": "400009",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-03T08:56:52Z"
}     
```

Authentication Examples Using Flex Microform Tokens {#pa2-use-tokens-flex}
==========================================================================

These examples list the API fields that are required for the Setup, Check Enrollment, and Validate Authentication services when using a Flex Microform token. An example of a request payload and a successful response that occurs with each service is provided.  
A Flex Microform token is valid for 15 minutes. After 15 minutes, a new Flex Microform token is needed.

Setting Up Device Data Collection When Using a Flex Microform Token {#pa2-use-token-flex-setup-intro}
=====================================================================================================

Running the Setup service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. In this use case, a Flex Microform token is used instead of the payment card data. Flex Microform tokens are only valid for 15 minutes.

Card-Specific Requirements
--------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB,Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-use-token-flex-setup-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-token-flex-setup-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.
{#pa2-use-token-flex-setup-intro_dl_kcl_pkc_1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for Setting Up Device Data Collection When Using a Flex Microform Token {#pa2-use-setup-token-flex-reqd-fields}
===============================================================================================================================

This field is required to use a Flex Microform token when you request the payer authentication Setup service.

Required Fields
---------------

tokenInformation.transientToken
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Setting Up Device Data Collection When Using a Flex Microform Token {#pa2-use-token-flex-setup-rest-ex}
=====================================================================================================================

Request

```
 {
    "tokenInformation": {
        "transientToken": "1C0RNHMQBTATXFCFNGR5EXH3XNOP6359LGLL9J283ATABJ8Z11NL66D834239B51"
    }
}
```

Response to Successful Request

```
{
    "consumerAuthenticationInformation": {
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzOTRmNDJmYS0xNGUxLTQ1ODAtOGUyZi05ZTVkNzM0Y2ZjYmYiLCJpYXQiOjE3MjU0NDQyNzQsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcyNTQ0Nzg3NCwiT3JnVW5pdElkIjoiNWI5YzRiYjNmZjYyNmIxMzQ0ODEwYTAxIiwiUmVmZXJlbmNlSWQiOiIwMDRhYzBhZC1mMGE2LTQ4MDAtOWQ3YS05NjJkZTZlYjQ0NmMifQ.oZ9gUZ98gbLyWfFDoY4jRknUQppIR-F_8JFXI6LTQWo",
        "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
        "referenceId": "004ac0ad-f0a6-4800-9d7a-962de6eb446c",
        "token": "AxizbwSTiUOd9P85Jq6mABEBTyDYFkxkAhMQyaSZejFczCmBWAAAnxnb"
    },
    "id": "7254442740716751204006",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-09-04T10:04:34Z"
}   
```

Checking Enrollment When Using a Flex Microform Token {#pa2-use-token-flex-enroll-intro}
========================================================================================

Running the Check Enrollment service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. In this use case, a Flex Microform token is used instead of the payment card data. Flex Microform tokens are only valid for 15 minutes.

Card-Specific Requirements
--------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires,China UnionPay, or Meeza.
{#pa2-use-token-flex-enroll-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-token-flex-enroll-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.
{#pa2-use-token-flex-enroll-intro_dl_kcl_pkc_1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Required Fields for Checking Enrollment When Using a Flex Microform Token {#pa2-use-token-enroll-flex-reqd}
===========================================================================================================

These fields are the minimum fields required for verifying that a customer is enrolled in a payer authentication program while using a Flex Microform token. It doesn't matter if the enrollment check is frictionless or results in a challenge, the same fields are required in the request. The fields in the response will differ.

Required Fields
---------------

[consumerAuthenticationInformation.deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[paymentInformation.customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[deviceInformation.httpAcceptBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-browser-value.md "")
:

[deviceInformation.httpAcceptContent](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-accept-content.md "")
:

[deviceInformation.httpBrowserColorDepth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-color-depth.md "")
:

[deviceInformation.httpBrowserJavaEnabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-enabled.md "")
:

[deviceInformation.httpBrowserJavaScript Enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-java-script-enabled.md "")
:

[deviceInformation.httpBrowserLanguage](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-language.md "")
:

[deviceInformation.httpBrowserScreenHeight](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-height.md "")
:

[deviceInformation.httpBrowserScreenWidth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-screen-width.md "")
:

[deviceInformation.httpBrowserTimeDif ference](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-browser-time-diff.md "")
:

[deviceInformation.ipAddress](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-ip-address.md "")
:

[deviceInformation.userAgentBrowserValue](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/device-info-aa/device-info-http-user-agent-browser-value.md "")
:
When the customer's browser provides this value, you must include that value in your request.

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.card.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-year.md "")
:

[paymentInformation.card.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-exp-mo.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-type-a.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment When Using a Flex Microform Token (Challenge) {#pa2-use-token-flex-enroll-frictionless-rest-ex}
=================================================================================================================================

Request

```
{
    "orderInformation": {
        "amountDetails": {
            "currency": "USD",
            "totalAmount": "10.99"
        },
        "billTo": {
            "address1": "1 Market St",
            "address2": "Address 2",
            "administrativeArea": "CA",
            "country": "US",
            "locality": "san francisco",
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "4158880000",
            "email": "test@email.com",
            "postalCode": "94105"
        }
    },
    "buyerInformation": {     
        "merchantCustomerId": "334124572" 
        "mobilePhone": "1245789632"
    },
    "deviceInformation": {
        "ipAddress": "139.130.4.5",
        "httpAcceptContent": "test",
        "httpBrowserLanguage": "en_us",
        "httpBrowserJavaEnabled": "N",
        "httpBrowserJavaScriptEnabled": "Y",
        "httpBrowserColorDepth": "24",
        "httpBrowserScreenHeight": "100000",
        "httpBrowserScreenWidth": "100000",
        "httpBrowserTimeDifference": "300",
        "userAgentBrowserValue": "GxKnLy8TFDUFxJP1t"
    },
    "consumerAuthenticationInformation": {
        "deviceChannel": "BROWSER",
        "transactionMode": "eCommerce",
        "referenceId": "CybsCruiseTester-b767b4ea"
    },
    "tokenInformation": {
        "transientToken": "1C0RNHMQBTATXFCFNGR5EXH3XNOP6359LGLL9J283ATABJ8Z11NL66D834239B51"
    }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "1725444594611"
    },
    "consumerAuthenticationInformation": {
        "challengeRequired": "N",
        "authenticationTransactionId": "jzULqrneaqG5H3Jev780",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiUOpWHIlxG5lABEBTyDYFlzPSBcS0JhdrSTL0YrmYUwKwAAAwwQS",
        "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
        "acsReferenceNumber": "Cardinal ACS",
        "stepUpUrl": "https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp",
        "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxZDBjNzI1Ny05YmQzLTRmZTktYjM5OS04YzUxM2M4OGQ2OTkiLCJhY3NUcmFuc0lEIjoiODNjN2U2MzYtM2FmMi00YTk2LTllNTktN2M2NzU0MTI3ZDI0IiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
        "directoryServerTransactionId": "231b97bd-2a3d-4500-b666-fda90334e5db",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "1d0c7257-9bd3-4fe9-b399-8c513c88d699",
        "acsOperatorID": "MerchantACS",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "83c7e636-3af2-4a96-9e59-7c6754127d24"
    },
    "errorInformation": {
        "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
        "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
    },
    "id": "7254445946286742204005",
    "paymentInformation": {
        "card": {
            "bin": "445653",
            "type" : "CARD"
        }
    },
    "status": "PENDING_AUTHENTICATION",
    "submitTimeUtc": "2024-09-04T10:09:55Z"
}     
```

Validating a Challenge When Using a Flex Microform Token {#pa2-use-token-flex-validate-intro}
=============================================================================================

Running the Validation service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. In this use case, a Flex Microform token is used instead of the payment card data.

Card-Specific Requirements
--------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-use-token-flex-validate-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-token-flex-validate-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` if Egypt was not set as the country in merchant configuration during merchant boarding.
{#pa2-use-token-flex-validate-intro_dl_kcl_pkc_1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-results`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-results`

Required Fields for Validating a Challenge When Using a Flex Microform Token {#pa2-use-validate-token-flex-reqd-fields}
=======================================================================================================================

These are the minimum fields required to use a Flex Microform token when you validate a Payer Authentication challenge.

Required Fields
---------------

[consumerAuthenticationInformation.authenticationTransactionId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-authentication-txn-id.md "")
:

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Validating a Challenge When Using a Flex Microform Token {#pa2-use-token-flex-validate-challenge-rest-ex}
=======================================================================================================================

Request

```
{
    "paymentInformation": {
        "card": {
            "type": "001"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "jzULqrneaqG5H3Jev780"
    }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "indicator": "vbv",
        "eciRaw": "05",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "eci": "05",
        "token": "AxizLwSTiUOsVuUwvt1DABEBTyDYFmPAAhMQyaSZejFczCmATUmo",
        "cavv": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "paresStatus": "Y",
        "xid": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "231b97bd-2a3d-4500-b666-fda90334e5db",
        "threeDSServerTransactionId": "1d0c7257-9bd3-4fe9-b399-8c513c88d699",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "83c7e636-3af2-4a96-9e59-7c6754127d24"
    },
    "id": "7254446789006754504003",
    "paymentInformation": {
        "card": {
            "bin": "445653",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-04T10:11:19Z"
}     
```

Authentication Examples Using Network Token/Tokenized Cards {#pa2-use-tokens-tokenized-cards}
=============================================================================================

These examples list the API fields that are required for the Setup, Check Enrollment, and Validate Authentication services when using network tokens or tokenized cards. An example of a request payload and a successful response that occurs with each service is provided.

Setting Up Device Data Collection with a Network Token/Tokenized Card {#pa2-use-setup-tokenized-intro}
======================================================================================================

Running the Setup service identifies the customer's bank and prepares for collecting data about the device that the customer is using to place the order. In this instance, a tokenized card is used instead of the payment card data.

Card-Specific Requirements
--------------------------

Some payment cards require specific information to be collected during a transaction.

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.
{#pa2-use-setup-tokenized-intro_dl_d1v_trz_rxb}

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-setup-tokenized-intro_dl_gpf_5rz_rxb}

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in merchant configuration during merchant boarding.
{#pa2-use-setup-tokenized-intro_dl_kcl_pkc_1cc}

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for Setting Up Device Data Collection with a Network Token/Tokenized Card {#pa2-use-setup-token-tokenized-card-reqd-fields}
===========================================================================================================================================

These fields are the minimum fields required when you request the Payer Authentication Setup service while using a tokenized card. Other fields that are required during Setup service are listed in [Required Fields for Collecting Device Data](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa2-use-cases-intro/pa2-set-up-use-intro/pa2-use-setup-reqd-fields.md "").

Required Fields
---------------

[paymentInformation.tokenizedCard.expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard.expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard.transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:
{#pa2-use-setup-token-tokenized-card-reqd-fields_dl_ctj_hjq_bdc}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Setting Up Device Data Collection When Using a Network Token/Tokenized Card {#pa2-use-token-tokenized-setup}
==========================================================================================================================

Request

```
{
  "paymentInformation": {
    "tokenizedCard": {
      "transactionType": "1",
      "type": "001",
      "expirationMonth": "11",
      "expirationYear": "2025",
      "number": "4111111111111111"
    }
  }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "1725450205426"
    },
    "consumerAuthenticationInformation": {
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlOGI4ODk5Ny1iYzY2LTRkYTEtOTYyNi1iNTc3MTlhNTczNzAiLCJpYXQiOjE3MjU0NTAyMDUsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcyNTQ1MzgwNSwiT3JnVW5pdElkIjoiNWI5YzRiYjNmZjYyNmIxMzQ0ODEwYTAxIiwiUmVmZXJlbmNlSWQiOiJiYmY4YzU3NS01NjRiLTQzYWYtOGI1Yy0yODdiNmU2ZWM4OGYifQ.UVNLUVmFJKwFxIO1prb5hpaKRR5WRI3esl0UnRg37Fg",
        "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
        "referenceId": "bbf8c575-564b-43af-8b5c-287b6e6ec88f",
        "token": "AxizbwSTiURwrn44LBakABEBTyDYGB7gAhMQyaSZejFczCmAmAAAzghh"
    },
    "id": "7254502054416956004004",
    "status": "COMPLETED",
    "submitTimeUtc": "2024-09-04T11:43:25Z"
}      
```

Checking Enrollment with a Network Token/Tokenized Card {#pa2-use-enroll-token-tokenized-intro}
===============================================================================================

Running the Check Enrollment service identifies the customer's bank and collects data about the device that the customer is using to place the order. This instance demonstrates this process with a network token/tokenized card.

Card-Specific Requirements
--------------------------

Some payment cards require additional information to be collected during a transaction.

[consumerAuthenticationInformation. defaultCard](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-default-card.md "")
:
This field is recommended for Discover ProtectBuy.

[consumerAuthenticationInformation.mcc](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-mcc.md "")
:
This field is required when the card type is Cartes Bancaires.

[consumerAuthenticationInformation. productCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-product-code.md "")
:
This field is required for American Express SafeKey (US) when the product code is `AIR` for an airline purchase.

[merchantInformation.merchantDescriptor. name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-name.md "")
:
This field is required for Relay Secure travel.

[orderInformation.shipTo.addess1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address1.md "")
:
This field is required only for American Express SafeKey (US).
{#pa2-use-enroll-token-tokenized-intro_dl_d1v_trz_rxb}

[orderInformation.shipTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-address2.md "")
:
This field is required only for American Express SafeKey (US.)

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-administrative-area.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-country.md "")
:
This field is required only for American Express SafeKey (US).

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required for American Express SafeKey (US).

[paymentInformation.card.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-card-card-type.md "")
:
This field is required when the card type is JCB, Cartes Bancaires, China UnionPay, or Meeza.

Country-Specific Requirements
-----------------------------

These fields are required for transactions in specific countries.

[consumerAuthenticationInformation. merchantScore](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-merchant-score.md "")
:
This field is required for transactions processed in France.

[consumerAuthenticationInformation. overrideCountryCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-override-country-code.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during boarding.

[merchantInformation.merchantDescriptor. country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/merch-info-aa/merch-info-merchant-descriptor-country-a.md "")
:
For Meeza transactions, this value must be set to `EG` when Egypt is not set as the country in the merchant configuration during merchant boarding.

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for transactions in the US and Canada.

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:
This field is required for transactions in the US and Canada.

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:
This field is required when the orderInformation.billTo.country field value is `US` or `CA`.
{#pa2-use-enroll-token-tokenized-intro_dl_gpf_5rz_rxb}

[orderInformation.shipTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-county.md "")
:
This field is required when the orderInformation.shipTo.country field value is `CA` or `US`.

[orderInformation.shipTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-shipto-postal-code.md "")
:
This field is required when the orderInformation.shipTo.country field value is `US` or `CA`.

Processor-Specific Requirements {#pa2-use-enroll-token-tokenized-intro_section_kl3_tbh_xwb}
-------------------------------------------------------------------------------------------

These fields are required by specific processors for transactions.

[processingInformation.authorizationOptions. transactionMode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/processing-info-aa/processing-info-auth-ops-transaction-mode.md "")
:
This field is required only for merchants in Saudi Arabia.

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentications`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentications`

Required Fields for Checking Enrollment When Using a Network Token/Tokenized Card {#pa2-use-enroll-token-tokenized-reqd-fields}
===============================================================================================================================

These fields are the minimum fields required for verifying that a customer is enrolled in a payer authentation program when using a tokenized card.

Required Fields
---------------

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:

[consumerAuthenticationInformation.referenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-reference-id.md "")
:

[paymentInformation.customer.customerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-customer-customer-id.md "")
:

[orderInformation.amountDetails.currency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-currency.md "")
:

[orderInformation.amountDetails.totalAmount](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-amount-details-total-amount.md "")
:
This field is required when the orderInformation.lineItems.unitPrice field is not used.

[orderInformation.billTo.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address1.md "")
:

[orderInformation.billTo.address2](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-address2.md "")
:

[orderInformation.billTo.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-admin-area.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-country.md "")
:
This field is required for the US and Canada.

[orderInformation.billTo.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-email.md "")
:

[orderInformation.billTo.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-first-name.md "")
:

[orderInformation.billTo.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-last-name.md "")
:

[orderinformation.billTo.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-locality.md "")
:

[orderInformation.billTo.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[orderInformation.billTo.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/order-info-aa/order-info-bill-to-postal-code.md "")
:

[paymentInformation.tokenizedCard. expirationMonth](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-month.md "")
:

[paymentInformation.tokenizedCard. expirationYear](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-exp-year.md "")
:

[paymentInformation.tokenizedCard.number](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-num.md "")
:

[paymentInformation.tokenizedCard. transactionType](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-txn-type.md "")
:

[paymentInformation.tokenizedCard.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/payment-info-aa/payment-info-tokenized-card-type-a.md "")
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment When Using a Network Token/Tokenized Card (Frictionless) {#pa2-use-token-tokenized-frictionless-rest-ex}
==========================================================================================================================================

Request

```
{
  "orderInformation": {
    "amountDetails": {
      "currency": "USD",
      "totalAmount": "10.99"
    },
    "billTo": {
      "address1": "1 Market St",
      "address2": "Address 2",
      "administrativeArea": "CA",
      "country": "US",
      "locality": "san francisco",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "4158880000",
      "email": "test@email.com",
      "postalCode": "94105"
    }
  },
  "paymentInformation": {
    "tokenizedCard": {
      "transactionType": "1",
      "type": "001",
      "expirationMonth": "11",
      "expirationYear": "2025",
      "number": "4111111111111111"
    }
  },
  "deviceInformation": {
    "ipAddress": "139.130.4.5",
    "httpAcceptContent": "test",
    "httpBrowserLanguage": "en_us",
    "httpBrowserJavaEnabled": "N",
    "httpBrowserJavaScriptEnabled": "Y",
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "100000",
    "httpBrowserScreenWidth": "100000",
    "httpBrowserTimeDifference": "300",
    "userAgentBrowserValue": "GxKnLy8TFDUFxJP1t"
  },
  "consumerAuthenticationInformation": {
    "deviceChannel": "BROWSER",
    "referenceId": "CybsCruiseTester-a8a8eeaf"
  }
}
```

Response to Successful Request

```
{
    "clientReferenceInformation": {
        "code": "1725450267324"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "05",
        "authenticationTransactionId": "o9spMK5vH7MK5lAPku60",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
            },
        "eci": "05",
        "token": "AxjzbwSTiURy4Xhjhs+lABEBTyDYGCNvSBcS0JiGTSTL0YrmYUwEwAAASAVA",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "51a3b89b-10c4-4718-8300-4cdc779d1434",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "1a9c8944-6d0b-46d4-a964-5e986cff9c1b",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "vbv",
        "specificationVersion": "2.1.0",
        "acsTransactionId": "b022828d-7440-4815-a5f8-28cf3f568f02"
    },
    "id": "7254502673416960004005",
    "paymentInformation": {
        "card": {
            "bin": "411111",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-04T11:44:27Z"
}     
```

Authentication Examples of Merchant-Initiated Transactions {#pa-3ri-intro}
==========================================================================

A 3RI transaction is an EMV `3-D Secure` transaction that is initiated by the merchant instead of the cardholder. The merchant keeps the payment data from the initial payment so that the cardholder does not have to be present for subsequent 3RI transactions. Having the payment details from a previous transaction enables the merchant to obtain a new Cardholder Authentication Verification Value (CAVV) to authenticate when authorizing future payments.  
The authorization request contains the consumerAuthenticationInformation.deviceChannel field. This process can be applied to these types of transactions:

* Recurring payments: payments occur at regular intervals for an indefinite interval like subscription services.
* Installment payments: payments occur at regular intervals for a fixed interval.
* Refunded purchases: the cost of an item is refunded before the item is received. Any charges for damage or missing items can be charged back to the customer using a 3RI transaction.
* Delayed shipments: an ordered item is out of stock delaying the shipment until the item is back in stock.
* Split payments: an order is fulfilled in split shipments rather than in a single shipment because one of multiple items in the order is temporarily out of stock.
* Multiple party commerce: a single entity or party makes multiple transactions with different merchants, for example, a travel agent booking flights, hotels, and tour excursions.
* Unknown final transaction amount: extra charges are made to the customer for items such as hotel services, driving citations, or tips.
  {#pa-3ri-intro_ul_rxx_nz1_zcc}

Challenge Reponses to 3RI Transactions {#pa-3ri-intro-challenge-response}
=========================================================================

The directory server prohibits any challenge response from an issuer in 3RI transactions because the cardholder is not present for authentication. If an issuer does respond with a challenge, the directory server:  
• Returns an ARes with a Transaction Status (transStatus) = `N` and a Transaction Status Reason (transStatusReason) = `87` (Transaction is excluded from Attempts Processing) to the `3-D Secure` Server (merchant).  
• Sends an error message (Erro) to the Access Control Server (ACS), with Error Code (errorCode) = `203` (Format of one or more data elements is invalid according to the specification.)  
When you receive this response, you should find an alternate way of processing the transaction. Examples include going directly to authorization, or when the cardholder is present, resending the transaction. When you receive this response, contact your acquirer to raise the issue with customer support.  
For Merchant Initiated Transactions which are expected to be frictionless, device details are not required in the MIT authentication transaction

Network-Specific Values for Multi-Party Commerce/Online Travel Agency (OTA) {#network_specific_values_for_3ri}
==============================================================================================================

When the request body requires a previous authentication reference ID (consumerAuthenticationInformation.priorAuthenticationReferenceId), use the network-specific value found in one of these fields in the original response.

* Relay: consumerAuthenticationInformation.acsTransactionId
* Mastercard: consumerAuthenticationInformation.directoryServerTransactionId

{#network_specific_values_for_3ri_ul_pxm_g5g_zcc}  
When the request body requires a value from the consumerAuthenticationInformation.requestorInitiatedAuthenticationIndicator field and the 3RI transaction type is multi-party commerce, use use one of these network-specific values.

* Relay: `11` (Other payment)
* Mastercard: `85` (Agent payment)

{#network_specific_values_for_3ri_ul_qxm_g5g_zcc}  
Note that Mastercard uses the Electronic Commerce Indicator (ECI) value of `07` for 3RI transactions.  
The network specific values for Multi Party Commerce / OTA are below.  
IMPORTANT The test card numbers that are provided are formatted with Xs for zeroes in the card number. When testing with the card numbers, replace the Xs with a 0 (zero).

1a: Initial Recurring Transaction {#pa-3ri-1a-test-initial-first-recur-txn}
===========================================================================

In this instance, the merchant initiates a 3RI recurring transaction that is a fixed amount for a set of transactions with no established expiration, such as with a subscription purchase.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 28X5  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 1a: Initial Recurring Transaction {#pa-3ri-1a-test-initial-first-recur-txn-req}
=======================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
Set this field value to `03`.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `Browser`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `02`.

[recurringPaymentInformation. endDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-end-date.md "")
:

[recurringPaymentInformation. frequency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-frequency.md "")
:

[recurringPaymentInformation. numberOfPayments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-number-of-payments.md "")
:

[recurringPaymentInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:

recurringPaymentInformation. sequenceNumber
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for a 3RI Initial Recurring Transaction {#pa-3ri-1a-test-initial-recur-txn-check-enroll-rest-ex}
==================================================================================================================================

Request

```
{
     "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX28X5"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "recurringPaymentInformation": {
    "endDate": "20240906",
    "frequency": "31",
    "numberOfPayments": "1",
    "originalPurchaseDate": "2024080511243877",
    "sequenceNumber": "1"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "02"
    },
    "challengeCode": "03",
    "deviceChannel": "Browser",
    "messageCategory": "01",
    "referenceId": "CybsCruiseTester-ddb08174"
  }
}       
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "challengeRequired": "N",
        "authenticationTransactionId": "ZtO0mD5q7PmRUG4v2NZ0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiS4ZKSmMkFZDABECT34jGC2P0h04ghLLtaSZV0ekj0yAsAAAUgae",
        "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
        "acsReferenceNumber": "Cardinal ACS",
        "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJiMjQ3MWRmYS0zYWFkLTQ3OWQtOGIxMy1iODZjNTE0Mzk3OWMiLCJhY3NUcmFuc0lEIjoiYzkyNWQ3M2MtMGNiMC00YjNhLWIzZmEtMmM0Y2E0MDJkOGI2IiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
        "directoryServerTransactionId": "bf67e7e6-c8cf-4b93-a211-3f4f60b07524",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "b2471dfa-3aad-479d-8b13-b86c5143979c",
        "acsOperatorID": "MerchantACS",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "c925d73c-0cb0-4b3a-b3fa-2c4ca402d8b6"
    },
    "errorInformation": {
        "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
        "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
    },
    "id": "7252892152426444904003",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "PENDING_AUTHENTICATION",
    "submitTimeUtc": "2024-09-02T15:00:15Z"
}
```

REST Example: Validating the Challenge for a 3RI Initial Recurring Transaction {#pa-3ri-1a-test-initial-recur-txn-validate-rest-ex}
===================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },

  "paymentInformation": {
        "card": {
            "type": "002"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "ZtO0mD5q7PmRUG4v2NZ0"
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "indicator": "spa",
        "eciRaw": "07",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "eci": "07",
        "token": "AxijLwSTiS5mZJ9Q0OxhABFPfiMZU1QCEtDJpJlXR6SPTIAA9Rdp",
        "cavv": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "paresStatus": "Y",
        "xid": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "bf67e7e6-c8cf-4b93-a211-3f4f60b07524",
        "threeDSServerTransactionId": "b2471dfa-3aad-479d-8b13-b86c5143979c",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "c925d73c-0cb0-4b3a-b3fa-2c4ca402d8b6"
    },
    "id": "7252913891376641404001",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T15:36:29Z"
}
```

1b: Recurring Payments - Subsequent Transaction (Mastercard) {#pa-3ri-1b-test-recur-payments-subseq-txn-mc}
===========================================================================================================

In this instance, the merchant is running a subsequent 3RI recurring transaction that is a fixed amount for a set of payments with no established expiration such as a subscription purchase.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 2235  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 1b: Recurring Payments - Subsequent Transaction (Mastercard) {#pa-3ri-1b-test-recur-payments-subseq-txn-mc-req}
=======================================================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `3RI`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. priorAuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-data.md "")
:

[consumerAuthenticationInformation. requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `02`.

[recurringPaymentInformation.endDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-end-date.md "")
:

[recurringPaymentInformation.frequency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-frequency.md "")
:

[recurringPaymentInformation. numberOfPayments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-number-of-payments.md "")
:

[recurringPaymentInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:

recurringPaymentInformation.sequenceNumber
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Validating the Challenge for 3RI Subsequent Installment Transactions {#pa-3ri-1b-use-recur-subsequent-validate-rest-ex}
=====================================================================================================================================

Request

```
{
     "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX2235"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "recurringPaymentInformation": {
    "endDate": "20240906",
    "frequency": "31",
    "numberOfPayments": "1",
    "originalPurchaseDate": "2024080511243877",
    "sequenceNumber": "1"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "02"
    },
    "authenticationDate": "20190829154531",
    "deviceChannel": "3RI",
    "messageCategory": "01",
    "priorAuthenticationData": "bf67e7e6-c8cf-4b93-a211-3f4f60b07524",
    "requestorInitiatedAuthenticationIndicator": "01",
    "referenceId": "CybsCruiseTester-ddb08174"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "02",
        "authenticationTransactionId": "cE217c8rl01I71fwGU30",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiS6VNMwh1gIkABECT34jGdA30h04ghLQyaSZV0ekj0yAmAAAzwTj",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "ucafCollectionIndicator": "2",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "5791e23c-c10a-4dae-b2c9-4abc766fce2c",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "db112903-7d0e-4ad8-9cb8-31a0e634a24b",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "f8a69dc8-2869-491b-b562-0fc7361333f0"
    },
    "id": "7252927068116474004004",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T15:58:27Z"
}
```

2a: Installment - Customer Initiated Transaction (Mastercard) {#pa-3ri-2a-test-install-cust-initiated-txn-mc}
=============================================================================================================

In this instance, the initial authentication is for the total amount for all of the future installments. Once the initial authentication is completed by the customer, the subsequent installments do not require authentication and go directly to authorization, which is Mastercard's preferred process.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 28X5  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 2a: Installment - Customer Initiated Transaction (Mastercard) {#pa-3ri-2a-test-install-cust-initiated-txn-mc-req}
=========================================================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
Set this field value to `03`.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `Browser`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

consumerAuthenticationInformation. installmentTotalCount
:
Set this field value to `02`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `03`.

[recurringPaymentInformation. endDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-end-date.md "")
:

[recurringPaymentInformation. frequency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-frequency.md "")
:

[recurringPaymentInformation. numberOfPayments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-number-of-payments.md "")
:

[recurringPaymentInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:

recurringPaymentInformation. sequenceNumber
:

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for a 3RI Customer Initiated Total Installments (Mastercard) {#pa-use-3ri-2a-installment-mc-enroll-rest-ex}
=============================================================================================================================================

Request

```
{
   "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX28X5"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "recurringPaymentInformation": {
    "endDate": "20240906",
    "frequency": "31",
    "numberOfPayments": "1",
    "originalPurchaseDate": "2024080511243877",
    "sequenceNumber": "1"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "03"
    },
    "authenticationDate": "20190829154531",
    "deviceChannel": "Browser",
    "installmentTotalCount": "2",
    "messageCategory": "01",
    "referenceId": "CybsCruiseTester-2551acb2"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "challengeRequired": "N",
        "authenticationTransactionId": "RTk6DV9Nsv2I1d8BSh40",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiTXaKSxK9bBhABECT34jN2Sb0h04ghLLtaSZV0ekj0yAsAAAxQTL",
        "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
        "acsReferenceNumber": "Cardinal ACS",
        "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIzYzVhMzExMS1lYmVkLTRjNzUtOWQ5YS00M2QyZTEwYzkyYTciLCJhY3NUcmFuc0lEIjoiMTVlNDZmNWItNTcwZS00OWMwLTkyYzYtYmQyMTdiN2MxZTkxIiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
        "directoryServerTransactionId": "2a9df334-1fa9-4dfe-9b1d-f4a2f14ba003",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "3c5a3111-ebed-4c75-9d9a-43d2e10c92a7",
        "acsOperatorID": "MerchantACS",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "15e46f5b-570e-49c0-92c6-bd217b7c1e91"
    },
    "errorInformation": {
        "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
        "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
    },
    "id": "7253450880266999804001",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "PENDING_AUTHENTICATION",
    "submitTimeUtc": "2024-09-03T06:31:28Z"
}
```

REST Example: Validating the Challenge for a 3RI Customer Initiated Total Installments (Mastercard) {#pa-use-3ri-2a-installment-mc-validate-rest-ex}
====================================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "RTk6DV9Nsv2I1d8BSh40"
    }
}
```

{#pa-use-3ri-2a-installment-mc-validate-rest-ex_codeblock_hyn_bbs_vcc}  
Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "indicator": "spa",
        "eciRaw": "02",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "token": "AxijLwSTiTXcdJ2PhbzFABFPfiM3dQgCEtDJpJlXR6SPTIAAJRcM",
        "paresStatus": "Y",
        "ucafCollectionIndicator": "2",
        "ucafAuthenticationData": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "2a9df334-1fa9-4dfe-9b1d-f4a2f14ba003",
        "threeDSServerTransactionId": "3c5a3111-ebed-4c75-9d9a-43d2e10c92a7",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "15e46f5b-570e-49c0-92c6-bd217b7c1e91"
    },
    "id": "7253451526166806904005",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-03T06:32:32Z"
}
```

3a: Split/Partial Shipment (Mastercard) {#pa-3ri-3a-test-split-partial-ship-mc}
===============================================================================

In this instance, the purchase includes multiple items that do not become available to the customer at different times. For example, the customer order has backordered or preordered items. During the initial purchase, the authentication should be for the full amount total (including products to be shipped at a later time).

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 2235  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 3a: Split/Partial Shipment (Mastercard) {#pa-3ri-3a-test-split-partial-ship-mc-req}
===========================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
Set this field value to `03`.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `3RI`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. priorAuthenticationData](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-data.md "")
:

[consumerAuthenticationInformation. priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:
Set this field value to `02`.

[consumerAuthenticationInformation. priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[onsumerAuthenticationInformation. requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:
Set this field value to `06`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `02`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for 3RI Split Shipment Transaction (Mastercard) {#pa-use-3ri-3a-split-ship-mc-enroll-rest-ex}
===============================================================================================================================

Request

```
{
     "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX2235"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "recurringPaymentInformation": {
    "endDate": "20240906",
    "frequency": "31",
    "numberOfPayments": "1",
    "originalPurchaseDate": "2024080511243877",
    "sequenceNumber": "1"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "02"
    },
    "challengeCode": "03",
    "deviceChannel": "3RI",
    "messageCategory": "01",
    "priorAuthenticationData": "bf67e7e6-c8cf-4b93-a211-3f4f60b07524",
    "priorAuthenticationMethod": "02",
    "priorAuthenticationTime": "202408051124",
    "requestorInitiatedAuthenticationIndicator": "06",
    "referenceId": "CybsCruiseTester-ddb08174"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "02",
        "authenticationTransactionId": "dgHSe0WYJbcT51D8pTQ0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiS7CLi6JgeyFABECT34jGkKb0h04ghLQyaSZV0ekj0yAmAAAzwTl",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "ucafCollectionIndicator": "2",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "1740697e-f8bd-4fde-8a12-c95e398c2409",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "c9c607a1-a130-4226-8a22-376e1183a5ae",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "74fd3b64-5abb-4ac2-b090-1fba79996123"
    },
    "id": "7252939727216490704005",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T16:19:32Z"
}
```

3b: Split/Delayed Shipment (Mastercard) {#pa-3ri-3b-test-split-delay-ship-relay}
===============================================================================

In this instance, the purchase includes multiple items that do not become available to the customer at different times. For example, the customer order has backordered or preordered items. During the initial purchase, the authentication should be for the full amount total (including products to be shipped at a later time).

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 002 | 52XXXX XX XXXX 2235  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 3b: Split/Delayed Shipment (Relay) {#pa-3ri-3b-test-split-delay-ship-relay-req}
=====================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `3RI`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:
Set this field value to `02`.

[consumerAuthenticationInformation. priorAuthenticationReferenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-reference-id.md "")
:

[consumerAuthenticationInformation. priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[consumerAuthenticationInformation. requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:
Set this field value to `06`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `02`.
{#pa-3ri-3b-test-split-delay-ship-relay-req_dl_gws_ccy_vcc}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for 3RI Split Shipment Transaction (Mastercard) {#pa-use-3ri-3a-split-ship-relay-enroll-rest-ex}
=================================================================================================================================

Request

```
{
    "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX2235"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "01"
    },
    "deviceChannel": "3RI",
    "messageCategory": "01",
    "priorAuthenticationMethod": "02",
    "priorAuthenticationReferenceId": "74fd3b64-5abb-4ac2-b090-1fba79996123",
    "priorAuthenticationTime": "202408051124",
    "requestorInitiatedAuthenticationIndicator": "06",
    "referenceId": "CybsCruiseTester-ddb08174"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "05",
        "authenticationTransactionId": "kvaz0784ZnNyUBg9U8t0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "eci": "05",
        "token": "AxjzbwSTiS7a+V0I6DbGABEBT34jGnMj0h04ghLQyaSZV0ekj0yAcAAAsQar",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "ebf656a8-c5da-412d-873f-9f4d3fa9a625",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "4777bd69-fcef-4725-b41b-84a346d83d0a",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "vbv",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "4381f3b5-09b1-4248-992a-89f6514064d7"
    },
    "id": "7252946706016498104006",
    "paymentInformation": {
        "card": {
            "bin": "400000",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T16:31:10Z"
}
```

4a: Multi-Party Commerce or OTA (Relay) {#pa-3ri-4a-test-multi-party-commerce-ota-relay}
======================================================================================

In this test case, a travel booking merchant creates a multi-party transaction for the cardholder. The merchants participating in the multi-party transaction are required to authorize on flights, hotels, and car rentals etc. This test case focuses on what the participating merchants are required to send for a successful transaction. Note that each participating merchant must send their own CAVV.  
Refer to the network specific values section for this use case.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 27X1  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 4a: Multi-Party Commerce or OTA (Relay) {#pa-3ri-4a-test-multi-party-commerce-ota-relay-req}
==================================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `3RI`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:
Set this field value to `02`.

[consumerAuthenticationInformation. priorAuthenticationReferenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-reference-id.md "")
:

[consumerAuthenticationInformation. priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[onsumerAuthenticationInformation. requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:
Set this field value to `11`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `01`.

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for 3RI Multi-Party Commerce Transaction (Relay) {#pa-use-3ri-4a-multi-party-relay-enroll-rest-ex}
==================================================================================================================================

Request

```
{
     "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "001",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "4XXXXXXXXXXX27X1"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "01"
    },
    "deviceChannel": "3RI",
    "messageCategory": "01",
    "priorAuthenticationMethod": "02",
    "priorAuthenticationReferenceId": "74fd3b64-5abb-4ac2-b090-1fba79996123",
    "priorAuthenticationTime": "202408051124",
    "requestorInitiatedAuthenticationIndicator": "11",
    "referenceId": "CybsCruiseTester-ddb08174"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "05",
        "authenticationTransactionId": "GLO987AF3GRfk4IAAO10",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "eci": "05",
        "token": "AxjzbwSTiS7hKm5H9W8jABEBT34jGnwr0h04ghLQyaSZV0ekj0yAcAAAtQax",
        "cavv": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "xid": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "5c1ee075-b8d7-43f0-9525-51de793125a0",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "f7ddddc1-cd06-4fd1-b1e6-db37e0379451",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "vbv",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "1dd0c6ac-03fd-46dd-b6ea-54bb5d337db2"
    },
    "id": "7252948448816500404003",
    "paymentInformation": {
        "card": {
            "bin": "400000",
            "type" : "CARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T16:34:05Z"
}
```

4b: Multi-Party Commerce or OTA (MasterCard) {#pa-3ri-4b-test-multi-party-commerce-ota-mc}
==========================================================================================

In this test case, a travel booking merchant creates a multi-party transaction for the cardholder. The merchants participating in the multi-party transaction are required to authorize on flights, hotels, and car rentals etc. This test case focuses on what the participating merchants are required to send for a successful transaction. Note that each participating merchant must send their own CAVV.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 28X5  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 4b: Multi-Party Commerce or OTA (MasterCard) {#pa-3ri-4b-test-multi-party-commerce-ota-mc-req}
======================================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. challengeCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-challenge-code.md "")
:
Set this field value to `03`.

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `Browser`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `85`.

[recurringPaymentInformation. endDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-end-date.md "")
:

[recurringPaymentInformation. frequency](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-frequency.md "")
:

[recurringPaymentInformation. numberOfPayments](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-number-of-payments.md "")
:

[recurringPaymentInformation. originalPurchaseDate](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/recurring-payment-info-aa/recurring-payment-info-original-purchase-date.md "")
:

recurringPaymentInformation. sequenceNumber
:
{#pa-3ri-4b-test-multi-party-commerce-ota-mc-req_dl_f1b_43y_vcc}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for 3RI Multi-Party Commerce Transaction (Mastercard) {#pa-use-3ri-4b-multi-party-mc-enroll-rest-ex}
======================================================================================================================================

Request

```
{
    "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX28X5"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "recurringPaymentInformation": {
    "endDate": "20240906",
    "frequency": "31",
    "numberOfPayments": "1",
    "originalPurchaseDate": "2024080511243877",
    "sequenceNumber": "1"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "85"
    },
    "challengeCode": "03",
    "deviceChannel": "Browser",
    "messageCategory": "01",
    "priorAuthenticationMethod": "02",
    "priorAuthenticationReferenceId": "74fd3b64-5abb-4ac2-b090-1fba79996123",
    "priorAuthenticationTime": "202408051124",
    "referenceId": "CybsCruiseTester-500582d1"
  }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "challengeRequired": "N",
        "authenticationTransactionId": "UjGENvX5ALCk1Yov31m0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiS7ruvMgAiEDABECT34jGqAX0h04ghLLtaSZV0ekj0yAsAAAwQTD",
        "acsUrl": "https://0merchantacsstag.cardinalcommerce.com/MerchantACSWeb/creq.jsp",
        "acsReferenceNumber": "Cardinal ACS",
        "pareq": "eyJtZXNzYWdlVHlwZSI6IkNSZXEiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiI3ODc3MjhmNy1iYzczLTQ0NzAtYTNlMC05ZDE1MjRlN2NhMTQiLCJhY3NUcmFuc0lEIjoiMDYzMzg2ODItYWYzMi00OWEwLWI4NWItZTViMjI1NzlmZmJjIiwiY2hhbGxlbmdlV2luZG93U2l6ZSI6IjAyIn0",
        "directoryServerTransactionId": "b25e6688-6b10-4942-a8a1-cc5b5f7ad9af",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "787728f7-bc73-4470-a3e0-9d1524e7ca14",
        "acsOperatorID": "MerchantACS",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "06338682-af32-49a0-b85b-e5b22579ffbc"
    },
    "errorInformation": {
        "reason": "CONSUMER_AUTHENTICATION_REQUIRED",
        "message": "The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction."
    },
    "id": "7252951422466502304003",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "PENDING_AUTHENTICATION",
    "submitTimeUtc": "2024-09-02T16:39:02Z"
}
```

Response to a Successful Request

```
{    
   "clientReferenceInformation": {
     "code": "1675288043120"
   },
   "consumerAuthenticationInformation": {
     "indicator": "internet",
     "ucafCollectionIndicator": "0",
     "strongAuthentication": {
     "OutageExemptionIndicator": "0"
     },
   "token": "AxjzbwSTbhMKrRswWTYSABECT9u+QBvfSB84gL2IZNJMvRiyubWAOAAA+Qxb"
    },
   "id": "6752880430346470503954",
   "status": "AUTHENTICATION_SUCCESSFUL",
   "submitTimeUtc": "2023-02-01T21:47:23Z"
}
```

REST Example: Validating the Challenge for 3RI Multi-Party Commerce Transaction (Mastercard) {#pa-use-3ri-4b-multi-party-mc-validate-rest-ex}
=============================================================================================================================================

Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "authenticationTransactionId": "UjGENvX5ALCk1Yov31m0"
    }
}
```

Response to a Successful Request

```
{
    "clientReferenceInformation": {
        "code": "pavalidatecheck",
        "partner": {
            "developerId": "7891234",
            "solutionId": "89012345"
        }
    },
    "consumerAuthenticationInformation": {
        "indicator": "spa",
        "eciRaw": "02",
        "authenticationResult": "0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "authenticationStatusMsg": "Success",
        "token": "AxijLwSTiS7u/oVLPQ0mABFPfiMaqKgCEtDJpJlXR6SPTIAAkRY+",
        "paresStatus": "Y",
        "ucafCollectionIndicator": "2",
        "ucafAuthenticationData": "AAIBBYNoEwAAACcKhAJkdQAAAAA=",
        "directoryServerTransactionId": "b25e6688-6b10-4942-a8a1-cc5b5f7ad9af",
        "threeDSServerTransactionId": "787728f7-bc73-4470-a3e0-9d1524e7ca14",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "06338682-af32-49a0-b85b-e5b22579ffbc"
    },
    "id": "7252952341186502004006",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-02T16:40:34Z"
}
```

4c: Multi-Party Commerce or OTA (MasterCard) {#pa-3ri-4c-test-multi-party-commerce-ota-mc}
==========================================================================================

The merchant initiates a (3RI) recurring transaction of a fixed amount for a specified number of transactions or with no set number of transactions such as occurs with subscription purchases. For more information, see [Requester Initiated Payments](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-glossary.md "").

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 2235  |

Endpoint
--------

**Production:** `POST ``https://api.cybersource.com``/risk/v1/authentication-setups`  
**Test:** `POST ``https://apitest.cybersource.com``/risk/v1/authentication-setups`

Required Fields for 3RI 4c: Multi-Party Commerce or OTA (MasterCard) {#pa-3ri-4c-test-multi-party-commerce-ota-mc-req}
======================================================================================================================

Required Fields
---------------

[consumerAuthenticationInformation. deviceChannel](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-device-channel.md "")
:
Set this field value to `3RI`.

[consumerAuthenticationInformation. messageCategory](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-message-category.md "")
:
Set this field value to `01`.

[consumerAuthenticationInformation. priorAuthenticationMethod](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-method.md "")
:
Set this field value to `02`.

[consumerAuthenticationInformation. priorAuthenticationReferenceId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-reference-id.md "")
:

[consumerAuthenticationInformation. priorAuthenticationTime](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-prior-auth-time.md "")
:

[onsumerAuthenticationInformation. requestorInitiatedAuthenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-requestor-initiated-auth-indicator.md "")
:
Set this field value to `85`.

[consumerAuthenticationInformation. strongAuthentication.authenticationIndicator](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/cons-auth-info-aa/cons-auth-info-strong-auth-auth-indicator.md "")
:
Set this field value to `85`.
{#pa-3ri-4c-test-multi-party-commerce-ota-mc-req_dl_f1b_43y_vcc}

Related Information
-------------------

* [API field reference guide for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/rest-api-fields-intro.md "")

REST Example: Checking Enrollment for 3RI Multi-Party Commerce Transaction (Mastercard) {#pa-use-3ri-4c-multi-party-mc-enroll-rest-ex}
======================================================================================================================================

Request

```
{
   "orderInformation": {
    "amountDetails": {
      "currency": "eur",
      "totalAmount": "100.00"
    },
    "lineItems": [
      {
        "unitPrice": "120.00"
      }
    ],
    "billTo": {
      "address1": "201 S. Division St.",
      "administrativeArea": "MI",
      "country": "US",
      "locality": "Ann Arbor",
      "firstName": "RTS",
      "lastName": "VDP",
      "email": "test@email.com",
      "postalCode": "48104-2201"
    }
  },
  "paymentInformation": {
    "card": {
      "type": "002",
      "expirationMonth": "12",
      "expirationYear": "2027",
      "number": "52XXXXXXXXXX2235"
    }
  },
  "deviceInformation": {
    "httpAcceptContent": "all",
    "httpBrowserLanguage": "en",
    "httpBrowserJavaEnabled": "y",
    "httpBrowserColorDepth": 1,
    "httpBrowserScreenHeight": 1,
    "httpBrowserScreenWidth": 1,
    "httpBrowserTimeDifference": 5,
    "userAgentBrowserValue": "chrome"
  },
  "consumerAuthenticationInformation": {
    "strongAuthentication": {
      "authenticationIndicator": "85"
    },
    "deviceChannel": "3RI",
    "messageCategory": "01",
    "priorAuthenticationMethod": "02",
    "priorAuthenticationReferenceId": "74fd3b64-5abb-4ac2-b090-1fba79996123",
    "priorAuthenticationTime": "202408051124",
    "requestorInitiatedAuthenticationIndicator": "85",
    "referenceId": "CybsCruiseTester-8e9d566d"
  }
}
```

Response

```
{
    "clientReferenceInformation": {
        "code": "RTS-Auth"
    },
    "consumerAuthenticationInformation": {
        "eciRaw": "02",
        "authenticationTransactionId": "teQ1a9eI9B6hf96QMHJ0",
        "strongAuthentication": {
            "OutageExemptionIndicator": "0"
        },
        "token": "AxjzbwSTiUMNwN7oizBEABECT34jdm670h04ghMQyaSZV0ekj0yAmAAAzwTp",
        "paresStatus": "Y",
        "acsReferenceNumber": "Cardinal ACS",
        "ucafCollectionIndicator": "2",
        "ucafAuthenticationData": "AJkBBkhgQQAAAE4gSEJydQAAAAA=",
        "directoryServerTransactionId": "208c54bd-a067-4a45-a285-af22f02a5e07",
        "veresEnrolled": "Y",
        "threeDSServerTransactionId": "2a6f6351-58a8-4e7b-acbc-8fd3d5ab85f3",
        "acsOperatorID": "MerchantACS",
        "ecommerceIndicator": "spa",
        "specificationVersion": "2.2.0",
        "acsTransactionId": "932bc2de-6e7a-4b16-adfa-f6c8c1ce9628"
    },
    "id": "7254402151006708904004",
    "paymentInformation": {
        "card": {
            "bin": "520000",
            "type": "MASTERCARD"
        }
    },
    "status": "AUTHENTICATION_SUCCESSFUL",
    "submitTimeUtc": "2024-09-04T08:56:55Z"
}
```

Testing Payer Authentication {#pa-testing-intro}
================================================

After you complete the necessary changes to your web and API integration, verify that all components are working correctly by performing all the tests for the cards that you support. Each test contains the specific input data and the most important result fields that you receive in the API response.

Testing Process {#pa_testing_process}
=====================================

Use the card number specified in the test with the card's expiration date set to the month of December and the current year plus three. For example, for 2025, use 2028. The test card numbers that are provided are formatted with Xs for zeroes in the card number. When testing with the card numbers, replace a X with a 0 (zero). You also need the minimum required fields for an order.

Enrollment Check Response Fields {#pa_testing_response_fields}
==============================================================

This table lists the checking enrollment response fields used in the test cases.

| Name Used in Test Cases | API Field                                            |
|:------------------------|:-----------------------------------------------------|
| ACS URL                 | consumerAuthenticationInformation.acsUrl             |
| E-commerce indicator    | consumerAuthenticationInformation.ecommerceIndicator |
| ECI                     | consumerAuthenticationInformation.eci                |
| PAReq                   | consumerAuthenticationInformation.pareq              |
| proofXML                | consumerAuthenticationInformation.proofXml           |
| VERes enrolled          | consumerAuthenticationInformation.veresEnrolled      |
| XID                     | consumerAuthenticationInformation.xid                |
[Enrollment Check Response Fields]

Authentication Validation Response Fields {#pa_testing_auth_validation_response_fields}
=======================================================================================

This table lists only the response fields used in the test cases.

|         Name Used in Test Cases         |                         API Field                         |
|-----------------------------------------|-----------------------------------------------------------|
| Authentication result                   | consumerAuthenticationInformation.authenticationResult    |
| E-commerce indicator                    | consumerAuthenticationInformation.indicator               |
| AAV (Mastercard only)                   | consumerAuthenticationInformation.ucafAuthenticationData  |
| CAVV (all card types except Mastercard) | consumerAuthenticationInformation.cavv                    |
| Collection indicator                    | consumerAuthenticationInformation.ucafCollectionIndicator |
| ECI                                     | consumerAuthenticationInformation.eci                     |
| PARes status                            | consumerAuthenticationInformation.paresStatus             |
| Status                                  | status                                                    |
| XID                                     | consumerAuthenticationInformation.xid                     |
[Response Fields Used in Authentication Validation Test Cases]

Test Cases for `3-D Secure` 2.x {#concept_uwj_cxc_zpb}
======================================================

Use the card number specified in the test with the card expiration date set to the month of January and the current year plus three. For example, for 2026, use 2029. You also need the minimum required fields for an order.  
Be sure to remove spaces in card numbers when testing.  
IMPORTANT The test card numbers that are provided are formatted with Xs for zeroes in the card number. When testing with the card numbers, replace the Xs with a 0 (zero).  
While the usage of transaction ID (XID) values have declined in importance, they are still included in `3-D Secure` 2.x test cases. Only Mastercard transactions do not return XIDs.  
While the `3-D Secure` version and directory server transaction ID fields are returned for the Check Enrollment and Validate Authentication services, this data is not included in the `3-D Secure` 2.x test cases.

> IMPORTANT
> Mastercard requires that the ` 3-D Secure ` version and directory server transaction ID be included along with all pertinent data in your authorization request.

Card Specific Setup
-------------------

The cards listed below require a specific merchant attribute or configuration during testing.

* `eftpos`: The merchant should request that customer support enable the preferred secondary brand attribute to enable the prerferred routing for eftpos.
* mada: The merchant descriptor country should be set as `SA` and the card type should be set as `mada`.
* Meeza: The merchant descriptor country should be set as `EG` and the card type should be set as `Meeza`
  {#concept_uwj_cxc_zpb_ul_kgf_tc4_nfc}

2.1: Frictionless Authentication Is Successful {#reference_xr3_lyc_zpb}
=======================================================================

This test verifies that successful frictionless authentication of the cardholder by the card issuer works correctly.

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 27X8                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XX XXXX XXXX 3XX1                     | 52XX XXXX XXXX 48X1                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXX XXXX XXXX 3XX6                     | 4XXX XXXX XXXX 497X                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XX X1XX XX2X XXXX                     | 81XXX1 XX XXXX X142 621XX3 82 3532 713X |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11 XXXX XXXX 2117                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11 XXXX XXXX 2117                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 517X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XXX1                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5126                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XXXX                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2XXX                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XXXX                     | 557755 X1 22XX XXX9                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XXX5                     | 4632X8 21 XXXX XXX4                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1XX1                     | 669XX9 XX XXXX 2XX9                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X296                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                                                                                                                                      |
|:----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 8XXX The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 8X2X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXX 2235                      |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 19X5 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 27X1                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL  
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.  
VERes enrolled = `Y`  
PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt;  
AVV = \&lt;AVV value\&gt; (Mastercard only)  
XID = \&lt;XID value\&gt;

E-Commerce Indicator (ECI) Values {#reference_xr3_lyc_zpb_section_m1z_pd5_3yb}
------------------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|         **Network**         | **ECI Raw Value** | **ECI String Value** |
|-----------------------------|-------------------|----------------------|
| American Express            | 05                | aesk                 |
| Cartes Bancaires Mastercard | 02                | spa                  |
| Cartes Bancaires Relay       | 05                | vbv                  |
| China UnionPay              | 05                | up3ds                |
| Diners Club                 | 05                | pb                   |
| Discover                    | 05                | dipb                 |
| eftpos                      | 05                | oci                  |
| Elo                         | 05                | cs                   |
| ITMX Mastercard             | 05                | lss                  |
| ITMX Relay                   | 05                | lss                  |
| Jaywan                      | 05                | oci                  |
| JCB J/Secure                | 05                | js                   |
| mada Mastercard             | 02                | mada or spa          |
| mada Relay                   | 05                | mada or vbv          |
| Mastercard                  | 02                | spa                  |
| RuPay                       | 05                | oci                  |
| Relay                        | 05                | vbv                  |

Results for the Validation Authentication Service
-------------------------------------------------

Validation does not apply to this test because no validation is needed when no challenge is issued during the transaction.

Action
------

If you request Check Enrollment and Authorization services separately, add the required payer authentication values to your authorization request. If you request the Check Enrollment and authorization services together, the process described above occurs automatically.

2.2: Frictionless Authentication Is Unsuccessful {#pa-testing-3ds-2x-unsuccess-frictionless-auth}
=================================================================================================

This test verifies that cardholder authentication without a challenge by the card issuer will fail.

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2X96                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X19                     | 52XXXX XX XXXX 4538                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X14                     | 4XXXXX XX XXXX 4574                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX1X XX1X                     | 81XXX1 XX XXXX X647 621XX3 77 X3X8 1377 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2364                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2364                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 522X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX19                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X19                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX18                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2X18                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX1X                     | 557755 X1 22XX XX17                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX13                     | 4632X8 22 XXXX XX12                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1X43                     | 669XX9 XX XXXX 2X17                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X361                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 8X1X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 8X4X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2276                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1319 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2925                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_FAILED

* User failed authentication.
* Payer cannot be authenticated.

{#pa-testing-3ds-2x-unsuccess-frictionless-auth_ul_sy1_rqd_zpb}  
VERes enrolled = `Y`  
PARes status = `N`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values {#pa-testing-3ds-2x-unsuccess-frictionless-auth_section_srg_rd5_3yb}
------------------------------------------------------------------------------------------------------

This table lists the expected ECI raw value, and their respective string values. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|         **Network**         | **ECI Raw Value** |      ECI String Value       |
|-----------------------------|-------------------|-----------------------------|
| American Express            | 07                | internet                    |
| Cartes Bancaires Mastercard | 00                | internet                    |
| Cartes Bancaires Relay       | 07                | internet or vbv_failure     |
| China UnionPay              | 07                | up3ds_failure               |
| Diners Club                 | 07                | internet                    |
| Discover                    | 07                | internet                    |
| eftpos                      | 07                | oci_failure                 |
| Elo                         | 07                | internet                    |
| ITMX Mastercard             | 07                | lss_failure                 |
| ITMX Relay                   | 07                | lss_failure                 |
| Jaywan                      | 07                | oci_failure                 |
| JCB J/Secure                | 07                | internet                    |
| mada Mastercard             | 00                | mada_failure or internet    |
| mada Relay                   | 07                | mada_failure or vbv_failure |
| Mastercard                  | 00                | internet                    |
| RuPay                       | 07                | oci_failure                 |
| Relay                        | 07                | internet or vbv_failure     |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

Even though the merchant can still authorize a failed `3-D Secure` transaction as a non-authenticated transaction, it is not recommended to submit this transaction for authorization. Instead, ask the customer for another form of payment.

2.3: Stand-In Frictionless Authentication is Attempted {#pa-testing-eds-2x-attempts-processing-frictionless-auth}
=================================================================================================================

This test verifies how your system reacts when the cardholder is enrolled in `3-D Secure` but the card issuer does not support 3-D Secure, requiring a stand-in authentication experience.

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2872                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X27                     | 52XXXX XX XXXX 4587                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X22                     | 4XXXXX XX XXXX 4111                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XXXX XX2X                     | 62XXX1 XX XXXX XX2X 621XX3 35 3371 144X |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2646                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2646                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 5360                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX27                     |                                         |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X27                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX26                     |                                         |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2026                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX75                     | 557755 X2 21XX XX74                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX7X                     | 4632X8 22 XXXX XX79                     |

**6690090000002017**

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1X68                     | 669XX9 XX XXXX 21X8                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X585                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | ---                                     |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | ---                                     |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2482                     |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2719                     |

> IMPORTANT
> The Meeza card and can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL` `  
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.  
VERes enrolled = `Y`  
PARes status = `A`  
CAVV = `&lt;CAVV value&gt;`  
AVV = `&lt;AVV value&gt;` (Mastercard only)  
XID = `&lt;XID value&gt;` (American Express only)

E-Commerce Indicator (ECI) Values {#pa-testing-eds-2x-attempts-processing-frictionless-auth_section_ckp_sd5_3yb}
----------------------------------------------------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | **ECI Raw Value** | ECI String Value |
|-----------------------------|-------------------|------------------|
| American Express            | 06                | aesk_attempted   |
| Cartes Bancaires Mastercard | 01                | spa              |
| Cartes Bancaires Relay       | 06                | vbv_attempted    |
| China UnionPay              | 06                | up3ds_attempted  |
| Diners Club                 | 06                | pb_attempted     |
| Discover                    | 06                | dipb_attempted   |
| eftpos                      | 06                | oci_attempted    |
| Elo                         | 06                | cs_attempted     |
| ITMX Mastercard             | 06                | lss_attempted    |
| ITMX Relay                   | 06                | lss_attempted    |
| Jaywan                      | 06                | oci_attempted    |
| JCB J/Secure                | 06                | js_attempted     |
| Mastercard                  | 01                | spa              |
| Relay                        | 06                | vbv_attempted    |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

If you request Check Enrollment and Authorization services separately, add the required payer authentication values (CAVV and ECI) to your authorization request. If you request the Check Enrollment and Authorization services together, the process described above occurs automatically.

2.4: Frictionless Authentication Is Unavailable {#pa-testing-3ds-2x-unavailable-frictionless-auth}
==================================================================================================

This test verifies how your system behaves when authentication is unavailable at the time of the transaction.

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXXX XX XXXX 2922                     |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3035                     | 52XXXX XX XXXX 4306                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X3X                     | 4XXXXX XX XXXX 4160                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX40 XX3X                     | 81XXX1 XX XXXX X894 621XX3 17 X75X 3X15 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2612                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2612                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 541X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX35                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X35                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X56 5X X1XX XXX34                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2X34                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX91                     | 557755 X1 22XX XX9X                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX96                     | 4632X8 22 XXXX XX79                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1126                     | 669XX9 XX XXXX 2181                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X221                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                  **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXX X XXXX 8X5X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                  **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXX XX XXXX 8XX The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2268                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1624 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2313                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL  
` `The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.  
VERes enrolled = `Y`  
PARes status = `U`  
AVV = `&lt;No value provided&gt;`  
CAAV = `&lt;No value provided&gt;`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values {#pa-testing-3ds-2x-unavailable-frictionless-auth_section_jr2_5d5_3yb}
--------------------------------------------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|         **Network**         | **ECI Raw Value** |      ECI String Value       |
|-----------------------------|-------------------|-----------------------------|
| American Express            | 07                | internet                    |
| Cartes Bancaires Mastercard | 00                | internet                    |
| Cartes Bancaires Relay       | 07                | internet or vbv_failure     |
| China UnionPay              | 07                | up3ds_failure               |
| Diners Club                 | 07                | internet                    |
| Discover                    | 07                | internet                    |
| eftpos                      | 07                | oci_failure                 |
| Elo                         | 07                | internet                    |
| ITMX Mastercard             | 07                | lss_failure                 |
| ITMX Relay                   | 07                | lss_failure                 |
| Jaywan                      | 07                | oci_failure                 |
| JCB J/Secure                | 07                | internet                    |
| mada Mastercard             | 00                | mada_failure or internet    |
| mada Relay                   | 07                | mada_failure or vbv_failure |
| Mastercard                  | 00                | internet                    |
| RuPay                       | 07                | oci_failure                 |
| Relay                        | 07                | internet or vbv_failure     |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

Submit your authorization request. There is no liability shift.

2.5: Frictionless Authentication Is Rejected {#reference_qch_ztd_zpb}
=====================================================================

This test verifies how your system reacts when authentication rejects the cardholder without a challenge by the issuer.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2X62                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X43                     | 52XXXX XX XXXX 4405                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X48                     | 4XXXXX XX XXXX 4517                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX3X XX4X                     | 81XXX1 XX XXXX X415 621XX3 X8 5745 X241 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2711                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2711                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 555X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX43                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X35                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 470565 XX 1XXX XX42                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2X83                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21X X125                      | 557755 X1 22XX X1X8                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX X12X                     | 4632X8 22 XXXX X1X3                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1159                     | 669XX9 XX XXXX 22X7                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 3337XX XX XXXX X321                     | 3338XX XX XXXX X734                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 8X8X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 813X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2185                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1913 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXXXX XXXX 2537                      |

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_FAILED

* User failed authentication.
* Payer cannot be authenticated.

{#reference_qch_ztd_zpb_ul_vl4_m5d_zpb}  
VERes enrolled = `Y`  
PARes status = `R`  
AVV = \&lt;No value provided\&gt;  
CAAV = \&lt;No value provided\&gt;  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values {#reference_qch_ztd_zpb_section_lqp_vd5_3yb}
------------------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|         **Network**         | **ECI Raw Value** |      ECI String Value       |
|-----------------------------|-------------------|-----------------------------|
| American Express            | 07                | internet                    |
| Cartes Bancaires Mastercard | 00                | internet                    |
| Cartes Bancaires Relay       | 07                | internet or vbv_failure     |
| China UnionPay              | 07                | up3ds_failure               |
| Diners Club                 | 07                | internet                    |
| Discover                    | 07                | internet                    |
| eftpos                      | 07                | oci_failure                 |
| Elo                         | 07                | internet                    |
| ITMX Mastercard             | 07                | lss_failure                 |
| ITMX Relay                   | 07                | lss_failure                 |
| Jaywan                      | 07                | oci_failure                 |
| JCB J/Secure                | 07                | internet                    |
| mada Mastercard             | 00                | mada_failure or internet    |
| mada Relay                   | 07                | mada_failure or vbv_failure |
| Mastercard                  | 00                | internet                    |
| RuPay                       | 07                | oci_failure                 |
| Relay                        | 07                | internet or vbv_failure     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type value for Meeza is ` 067 `.

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

You are not permitted to submit this transaction for authorization. Instead, ask the customer for another form of payment.

2.6: Authentication Is Not Available {#pa-testing-3ds-2x-auth-not-available-lookup}
===================================================================================

This test verifies how your system reacts when a system error when checking enrollment prevents authentication.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2468                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X5X                     | 52XXXXXX XXXX 4X9X                      |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X55                     | 4XXXXX XX XXXX 4285                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX6X XX5X                     | 81XXX1 XX XXXX X795 621XX3 1X 724X 3478 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XXXX XXXX 2836                      |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2836                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 556X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX5X                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X5X                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX59                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2X91                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX X141                     | 557755 X1 22XX X124                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX138                    | 4632X8 22 XXXX X145                     |

Jaywan (Card Type = 081) {#pa-testing-3ds-2x-auth-not-available-lookup_section_xkd_5d5_hhc}
-------------------------------------------------------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1126                     | 669XX9 XX XXXX 2181                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X94X                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 8X9X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 814X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 24X9                     |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 299X                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL` `  
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.` `  
VERes enrolled = `U`  
In the response, this error code and error description is returned:  
directoryServerErrorCode: `101`  
directoryServerErrorDescription: `Invalid Formatted Message`

E-Commerce Indicator (ECI) Values {#pa-testing-3ds-2x-auth-not-available-lookup_section_jvj_4zy_tvb}
----------------------------------------------------------------------------------------------------

This table lists the ECI raw value that must be passed within the authorization and its respective string value. Note that there is no raw ECI returned for these scenarios. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|   **Network**   | **ECI Raw Value** |      ECI String Value       |
|-----------------|-------------------|-----------------------------|
| eftpos          | 07                | oci_failure                 |
| mada Mastercard | 00                | mada_failure or internet    |
| mada Relay       | 07                | mada_failure or vbv_failure |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

Submit your authorization request. There is no liability shift.

2.7: Check Enrollment Error {#reference_hrv_dwd_zpb}
====================================================

This test verifies how your system reacts when an error occurs while verifying that the cardholder is part of an authentication program.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2732                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X68                     | 52XXXX XX XXXX 4X58                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X63                     | 4XXXXXXX XXXX 4194                      |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX5X XX6X                     | 81XXX1 XX XXXX X662 621XX3 41 5762 1444 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2315                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2315                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 579X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX68                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X68                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX67                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 21X9                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX X174                     | 557755 X1 22XX X132                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX153                    | 4632X8 22 XXXX X152                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1159                     | 669XX9 XX XXXX 2199                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X65X                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 811X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 817X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2X37                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1921 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2446                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL  
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.` `  
VERes enrolled = `U`  
In the response, this error code and error description is returned:  
directoryServerErrorCode: `101`  
directoryServerErrorDescription: `Error Processing Message Request 1001`

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the raw ECI value that must be passed within the authorization and its respective string value. Note that no raw ECI is returned for these scenarios. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|     Network     | ECI Raw Value |      ECI String Value       |
|-----------------|---------------|-----------------------------|
| eftpos          | 07            | oci_failure                 |
| mada Mastercard | 00            | mada_failure or internet    |
| mada Relay       | 07            | mada_failure or vbv_failure |
| RuPay           | 07            | oci_failure                 |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.  
While Mastercard would normally return the directory server transaction ID, in this test case, it is not returned.

Action
------

Proceed with the authorization request, and contact your support representative to resolve the issue. There is no liability shift. If you requested payer authentication and authorization together, the authorization is processed automatically.

2.8: Time Out {#reference_lfk_bxd_zpb}
======================================

This test verifies how your system reacts when an error occurs while verifying that the cardholder is part of an authentication program.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2047                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X76                     | 52XXXX XX XXXX 4694                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X71                     | 4XXXXX XX XXXX 4277                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX9X X7X                      | 81XXX1 XX XXXX X928 621XX3 X1 X451 71X7 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2869                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2869                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 584X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX76                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX76                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX75                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2125                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX X182                     | 557755 X1 22XX X14X                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX187                    | 4632X8 22 XXXX X178                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1175                     | 669XX9 XX XXXX 22X7                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX 0577                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                   |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXXXX XXXX 813X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 82XX The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2326                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1939 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2354                     |

This test verifies how your system reacts when it times out while checking enrollment, causing an error on the transaction.

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = AUTHENTICATION_SUCCESSFUL` `
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.  
VERes enrolled = `U`  
In the response, this error code and error description is returned:  
directoryServerErrorCode: `402`  
directoryServerErrorDescription: `Transaction Timed Out`

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the raw ECI value that would need to be passed within the authorization and its respective string value. Note that there is no raw ECI value returned for these scenarios. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|     Network     | ECI Raw Value |      ECI String Value       |
|-----------------|---------------|-----------------------------|
| eftpos          | 07            | oci_failure                 |
| mada Mastercard | 00            | mada_failure or internet    |
| mada Relay       | 07            | mada_failure or vbv_failure |
| RuPay           | 07            | oci_failure                 |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

After 10-12 seconds, proceed with the authorization request. There is no liability shift.

2.9: Step-Up Authentication Is Successful {#reference_e2n_q12_zpb}
==================================================================

This test verifies how your system reacts to a successful step-up (or challenge) authentication transaction.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2534                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X92                     | 52XXXX XX XXXX 4X74                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3139                     | 4XXXXX XX XXXX 4855                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 99 998X XX19                     | 81XXX1 XX XXXX X688 621XX3 25 7857 4424 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2265                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2265                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 5311                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX84                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 529X                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX83                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 219X                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX26                     | 557755 X1 22XX XX25                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX21                     | 4632X8 22 XXXX XX2X                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1233                     | 669XX9 XX XXXX 2249                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X569                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 816X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 827X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2151                     |

PayPak (Card Type = 068)
------------------------

|                                            **`3-D Secure` 2.1.0** Test Card Number                                             | **`3-D Secure` 2.2.0** Test Card Number |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 22X543 XX XXXX 3XX2 PayPak transactions require a CurrencyCode = `586` and a CountryCodeOverride = `PK` on the Lookup Request. | ---                                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1XX4 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 25X3                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = PENDING_AUTHENTICATION  
The cardholder is enrolled in payer authentication. Authenticate before proceeding with authorization.  
VERes enrolled = `Y`  
PARes status = `C`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the expected ECI raw values and their respective string values from this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|     Network     | ECI Raw Value | ECI String Value |
|-----------------|---------------|------------------|
| mada Mastercard | 00            | spa or mada      |
| mada Relay       | 07            | vbv or mada      |
| PayPak          | 07            | oci_failure      |
| RuPay           | 05            | oci_failure      |

Results for the Validation Authentication Service
-------------------------------------------------

Status = AUTHENTICATION_SUCCESSFUL` `
` `` `Authentication is validated.` `  
PARes status = `Y`  
XID = \&lt;XID value\&gt;  
CAVV = `&lt;CAVV value&gt;`

E-Commerce Indicator (ECI) Values {#reference_e2n_q12_zpb_section_cdy_b25_3yb}
------------------------------------------------------------------------------

This table lists the expected raw ECI values and their respective string values from validating this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | ECI Raw Value | ECI String Value |
|-----------------------------|---------------|------------------|
| American Express            | 05            | aesk             |
| Cartes Bancaires Mastercard | 02            | spa              |
| Cartes Bancaires Relay       | 05            | vbv              |
| China UnionPay              | 05            | up3ds            |
| Diners Club                 | 05            | pb               |
| Discover                    | 05            | dipb             |
| eftpos                      | 05            | oci              |
| Elo                         | 05            | cs               |
| ITMX Mastercard             | 05            | lss              |
| ITMX Relay                   | 05            | lss              |
| Jaywan                      | 05            | oci              |
| JCB J/Secure                | 05            | js               |
| mada Mastercard             | 02            | spa or mada      |
| mada Relay                   | 05            | vbv or mada      |
| Mastercard                  | 02            | spa              |
| PayPak                      | 05            | oci              |
| RuPay                       | 05            | oci              |
| Relay                        | 05            | vbv              |

Action
------

If you request Validate Authentication and authorization services separately, add the required payer authentication values to your authorization request. If you request the Validate Authentication and authorization services together, the process described above occurs automatically. The merchant should include the CAVV and ECI values in the authorization message.

2.10: Step-Up Authentication Is Unsuccessful {#reference_owz_dg2_zpb}
=====================================================================

This test verifies that the step-up (challenge) authentication transaction fails whenever the cardholder challenge fails.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2237                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 31XX                     | 52XXXX XX XXXX 4124                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X97                     | 4XXXXX XX XXXX 4293                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 99 997X XX29                     | 81XXX1 XX XXXX X8X3 621XX3 81 8186 8X38 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2695                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2695                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 5329                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX XX92                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5217                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX XX91                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 22X8                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX34                     | 557755 X1 22XX XX33                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX39                     | 4632X8 22 XXXX XX38                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1258                     | 669XX9 XX XXXX 2298                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X874                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 817X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 828X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 249X                     |

PayPak (Card Type = 068)
------------------------

|                                            **`3-D Secure` 2.1.0** Test Card Number                                             | **`3-D Secure` 2.2.0** Test Card Number |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 22X543 XX XXXX 3X1X PayPak transactions require a CurrencyCode = `586` and a CountryCodeOverride = `PK` on the Lookup Request. | ---                                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1X12 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2370                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

= PENDING_AUTHENTICATION`The cardholder is enrolled in payer authentication. Please authenticate before proceeding with authorization.`  
VERes enrolled = `Y`  
PARes status = `C`  
PAReq = \&lt;PAReq value\&gt;  
ACS URL = \&lt;URL value\&gt;  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the expected raw ECI values and their respective string values from this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|     Network     | ECI Raw Value |      ECI String Value       |
|-----------------|---------------|-----------------------------|
| mada Mastercard | 00            | mada_failure or internet    |
| mada Relay       | 07            | mada_failure or vbv_failure |
| PayPak          | 07            | oci_failure                 |
| RuPay           | 07            | oci_failure                 |

Results for the Validation Authentication Service
-------------------------------------------------

= AUTHENTICATION_FAILED

* User failed authentication.
* Payer cannot be authenticated.

{#reference_owz_dg2_zpb_ul_fgs_2h2_zpb}  
PARes status = `N`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values {#reference_owz_dg2_zpb_sec5_3yb}
-------------------------------------------------------------------

This table lists the expected raw ECI values and their respective string values from this transaction. These values indicate whether the payer was validated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | ECI Raw Value |      ECI String Value       |
|-----------------------------|---------------|-----------------------------|
| American Express            | 07            | internet                    |
| Cartes Bancaires Mastercard | 00            | internet                    |
| Cartes Bancaires Relay       | 07            | internet or vbv_failure     |
| China UnionPay              | 07            | up3ds_failure               |
| Diners Club                 | 07            | internet                    |
| Discover                    | 07            | internet                    |
| eftpos                      | 07            | oci_failure                 |
| Elo                         | 07            | internet                    |
| ITMX Mastercard             | 07            | lss_failure                 |
| ITMX Relay                   | 07            | lss_failure                 |
| JCB J/Secure                | 07            | internet                    |
| Jaywan                      | 07            | oci_failure                 |
| mada Mastercard             | 00            | mada_failure or internet    |
| mada Relay                   | 07            | mada_failure or vbv_failure |
| Mastercard                  | 00            | internet                    |
| PayPak                      | 07            | oci_failure                 |
| RuPay                       | 07            | oci_failure                 |
| Relay                        | 07            | internet or vbv_failure     |

Action
------

You are not permitted to submit this transaction for authorization. Instead, ask the customer for another form of payment.

2.11: Step-Up Authentication Is Unavailable {#reference_tpn_pj2_zpb}
====================================================================

This test verifies that the correct response is returned when step-up authentication is unavailable.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2484                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3188                     | 52XXXX XX XXXX 4124                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 31X5                     | 4XXXXX XX XXXX 464X                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 99 997X XX39                     | 81XXX1 XX XXXX X159                     |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 1129                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 1129                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 5337                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX X1XX                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5225                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX X1X9                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2257                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX42                     | 557755 X1 22XX XX41                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX47                     | 4632X8 22 XXXX XX46                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1274                     | 669XX9 XX XXXX 2348                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X981                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 819X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 831X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2664                     |

PayPak (Card Type = 068)
------------------------

|                                            **`3-D Secure` 2.1.0** Test Card Number                                             | **`3-D Secure` 2.2.0** Test Card Number |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 22X543 XX XXXX 3X28 PayPak transactions require a CurrencyCode = `586` and a CountryCodeOverride = `PK` on the Lookup Request. | ---                                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1X2X When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 242X                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

Status = PENDING_AUTHENTICATION  
The cardholder is enrolled in payer authentication. Authenticate before proceeding with authorization.  
VERes enrolled = `Y`  
PARes Status = `C`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the expected ECI raw values and their respective string values from this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|     Network     | ECI Raw Value |      ECI String Value       |
|-----------------|---------------|-----------------------------|
| mada Mastercard | 00            | mada_failure or internet    |
| mada Relay       | 07            | mada_failure or vbv_failure |
| PayPak          | 07            | oci_failure                 |
| RuPay           | 07            | oci_failure                 |

Results for the Validation Authentication Service
-------------------------------------------------

Status =` `AUTHENTICATION_SUCCESSFUL` `Authentication is validated.  
PARes status = `U`  
XID = \&lt;XID value\&gt; (American Express only)

E-Commerce Indicator (ECI) Values {#reference_tpn_pj2_zpb_secti5_3yb}
---------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values from this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | ECI Raw Value |      ECI String Value       |
|-----------------------------|---------------|-----------------------------|
| American Express            | 07            | internet                    |
| Cartes Bancaires Mastercard | 00            | internet                    |
| Cartes Bancaires Relay       | 07            | internet or vbv_failure     |
| China UnionPay              | 07            | up3ds_failure               |
| Diners Club                 | 07            | internet                    |
| Discover                    | 07            | internet                    |
| eftpos                      | 07            | oci_failure                 |
| Elo                         | 07            | internet                    |
| ITMX Mastercard             | 07            | lss_failure                 |
| ITMX Relay                   | 07            | lss_failure                 |
| Jaywan                      | 07            | oci_failure                 |
| JCB J/Secure                | 07            | internet                    |
| mada Mastercard             | 00            | mada_failure or internet    |
| mada Relay                   | 07            | mada_failure or vbv_failure |
| Mastercard                  | 00            | internet                    |
| PayPak                      | 07            | oci_failure                 |
| RuPay                       | 07            | oci_failure                 |
| Relay                        | 07            | internet or vbv_failure     |

Action
------

The merchant can retry authentication or process without the liability shift.

2.12: Error During Authentication {#pa-testingo-3ds-2x-error-authentication}
============================================================================

This test checks how your system reacts when authentication request errors occurs during processing.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXXX XX XXXX 2351                     |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3126                     | 52XXXX XX XXXX 4611                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3113                     | 4XXXXX XX XXXX 4913                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 99 994X XX59                     | 81XXX1 XX XXXX X159 621XX3 32 7122 3145 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 257X                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 257X                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 5352                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX X118                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5241                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX X117                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2265                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX XX67                     | 557755 X1 22XX XX66                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX XX62                     | 4632X8 22 XXXX XX61                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1316                     | 669XX9 XX XXXX 24X5                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X676                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 82XX The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 834X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 2656                     |

PayPak (Card Type = 068)
------------------------

|                                            **`3-D Secure` 2.1.0** Test Card Number                                             | **`3-D Secure` 2.2.0** Test Card Number |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| 22X543 XX XXXX 3X69 PayPak transactions require a CurrencyCode = `586` and a CountryCodeOverride = `PK` on the Lookup Request. | ---                                     |

RuPay (Card Type = 061)
-----------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                               **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 652267 XX XXXX 1X38 When checking enrollment, all transactions must set the **CountryCodeOverride** field to `356`, and include the **Card Type** and **Currency Code** . For domestic transactions, you must also include values for the **Token Requestor ID** , **Token Cryptogram** , and the **Token Status Indicator** fields. |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 2644                     |

> IMPORTANT
> The Meeza card can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service
----------------------------------------

= PENDING_AUTHENTICATION`The cardholder is enrolled in payer authentication. Please authenticate before proceeding with authorization.`  
VERes enrolled = `Y`  
PARes status = `C`  
PAReq = `&lt;PAReq value&gt;`

E-Commerce Indicator (ECI) Values
---------------------------------

This table lists the expected ECI raw values and their respective string values from this transaction. These values indicate whether the payer was authenticated by the card network. These values should be passed under this test condition when a transaction is submitted for cardholder authentication.

|     Network     | ECI Raw Value |      ECI String Value       |
|-----------------|---------------|-----------------------------|
| mada Mastercard | 00            | mada_failure or internet    |
| mada Relay       | 07            | mada_failure or vbv_failure |
| PayPak          | 07            | oci_failure                 |
| RuPay           | 07            | oci_failure                 |

Results for the Validation Authentication Service
-------------------------------------------------

= AUTHENTICATION_FAILED

* User failed authentication.
* Payer cannot be authenticated.

{#pa-testingo-3ds-2x-error-authentication_ul_fgs_2h2_zpb}  
PARes status = `U`  
XID = `&lt;XID value&gt;` (American Express only)

E-Commerce Indicator (ECI) Values {#pa-testingo-3ds-2x-error-authentication_section_v11_225_3yb}
------------------------------------------------------------------------------------------------

This table lists the expected ECI raw values and their respective string values from this transaction. These values indicate whether the payer was validated by the card network. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | ECI Raw Value |      ECI String Value       |
|-----------------------------|---------------|-----------------------------|
| American Express            | 07            | internet                    |
| Cartes Bancaires Mastercard | 00            | internet                    |
| Cartes Bancaires Relay       | 07            | internet or vbv_failure     |
| China UnionPay              | 07            | up3ds_failure               |
| Diners Club                 | 07            | internet                    |
| Discover                    | 07            | internet                    |
| eftpos                      | 07            | oci_failure                 |
| Elo                         | 07            | internet                    |
| ITMX Mastercard             | 07            | lss_failure                 |
| ITMX Relay                   | 07            | lss_failure                 |
| Jaywan                      | 07            | oci_failure                 |
| JCB J/Secure                | 07            | internet                    |
| mada Mastercard             | 00            | mada_failure or internet    |
| mada Relay                   | 07            | mada_failure or vbv_failure |
| Mastercard                  | 00            | internet                    |
| PayPak                      | 07            | oci_failure                 |
| RuPay                       | 07            | oci_failure                 |
| Relay                        | 07            | internet or vbv_failure     |

Action
------

You can retain liability and submit this transaction for authorization as an unauthenticated transaction, or you can ask the customer for another form of payment.

2.13: Authentication Is Bypassed {#pa-testing-3ds-2x-bypassed-auth}
===================================================================

This test verifies how your system reacts when the challenge requested by the issuer is bypassed for the transaction.

Card Numbers
------------

American Express (Card Type = 003)
----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 34XXX XX XXXX 2948                      |

Cartes Bancaires Mastercard (Card Type = 036)
---------------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 3X84                     | 52XXXX XX XXXX 4991                     |

Cartes Bancaires Relay (Card Type = 036)
---------------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 3X89                     | 4XXXXX XX XXXX 44XX                     |

China UnionPay (Card Type = 062)
--------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 62XXX1 XX XX8X XX8X                     | 81XXX1 XX XXXX X985 621XX3 26 X765 76X4 |

Diners Club (Card Type = 005)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2976                     |

Discover (Card Type = 004)
--------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 6X11XX XX XXXX 2976                     |

eftpos Mastercard (Card Type = 002)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 52XXXX XX XXXX 598X                     | ---                                     |

eftpos Mastercard (Card Type = 070)
-----------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 516366 XX 1XXX X126                     | ---                                     |

eftpos Relay (Card Type = 001)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4XXXXX XX XXXX 5X84                     | ---                                     |

eftpos Relay (Card Type = 070)
-----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 47X565 XX 1XXX X125                     | ---                                     |

Elo (Card Type = 054)
---------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 65X529 XX XXXX 2166                     |

ITMX Mastercard (Card Type = 002)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 557755 X1 21XX X19X                     | 557755 X1 22XX X157                     |

ITMX Relay (Card Type = 001)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 4632X8 21 XXXX X211                     | 4632X8 22 XXXX X186                     |

Jaywan (Card Type = 081)
------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| 669XX9 XX XXXX 1373                     | 669XX9 XX XXXX 2413                     |

JCB J/Secure (Card Type = 007)
------------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 3338XX XX XXXX X122                     |

mada Mastercard (Card Type = 060)
---------------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 52XXXX XX XXXX 815X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

mada Relay (Card Type = 060)
---------------------------

| **`3-D Secure` 2.1.0** Test Card Number |                                                                                                                                   **`3-D Secure` 2.2.0** Test Card Number                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ---                                     | 4XXXXX XX XXXX 826X The merchant's country must be set to `SA` within the merchant profile, or the **CountryCodeOverride** field must be set to `SA` on the Lookup Request. The response will include the `3-D Secure` operator ID, DS reference number, brand authentication, and the ACS reference number. |

Mastercard (Card Type = 002)
----------------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 52XXXX XX XXXX 25X8                     |

Relay (Card Type = 001)
----------------------

| **`3-D Secure` 2.1.0** Test Card Number | **`3-D Secure` 2.2.0** Test Card Number |
|-----------------------------------------|-----------------------------------------|
| ---                                     | 4XXXXX XX XXXX 256X                     |

> IMPORTANT
> The Meeza card is supported in payer authentication and can be tested in the same manner as Mastercard using the same test card numbers. The only difference is that the card type for Meeza is ` 067 `.

Results for the Check Enrollment Service {#pa-testing-3ds-2x-bypassed-auth_section_edn_125_3yb}
-----------------------------------------------------------------------------------------------

Status = AUTHENTICATION_SUCCESSFUL  
The cardholder is enrolled in Payer Authentication. Authenticate the cardholder before continuing with the transaction.  
VERes enrolled = `B`  
XID = \&lt;XID value\&gt;

E-Commerce Indicator (ECI) Values {#pa-testing-3ds-2x-bypassed-auth_section_f2n_125_3yb}
----------------------------------------------------------------------------------------

This table lists the ECI raw value that would need to be passed within the authorization and its respective string value. Note that there is no raw ECI returned for these scenarios. These values should be passed under this test condition when a transaction is submitted for payment authorization.

|           Network           | ECI Raw Value |     ECI String Value     |
|-----------------------------|---------------|--------------------------|
| American Express            | 07            | internet                 |
| Cartes Bancaires Mastercard | 00            | internet                 |
| Cartes Bancaires Relay       | 07            | internet                 |
| China UnionPay              | 07            | up3ds_failure            |
| Diners Club                 | 07            | internet                 |
| Discover                    | 07            | internet                 |
| eftpos                      | 07            | oci_failure              |
| Elo                         | 07            | internet                 |
| ITMX Mastercard             | 07            | lss_failure              |
| ITMX Relay                   | 07            | lss_failure              |
| Jaywan                      | 07            | oci_failure              |
| JCB J/Secure                | 07            | internet                 |
| mada Mastercard             | 00            | internet or mada_failure |
| mada Relay                   | 07            | internet or mada_failure |
| Mastercard                  | 00            | internet                 |
| Relay                        | 07            | internet                 |

Results for the Validation Authentication Service
-------------------------------------------------

No results are returned.

Action
------

Submit your authorization request. There is no liability shift.

2.14: Require Method URL {#reference_fxw_qjk_wqb}
=================================================

This test ensures that the merchant is allowing sufficient time (10 seconds) for the issuer to complete device data collection.

Card Numbers
------------

The Method URL process runs before the authentication request to ensure device data is collected properly. The enrollment check of the card account should not start until after the device data collection (DDC) response is received. This test verifies that there is enough time to collect the BIN of the issuer and to transmit it. This test attempts to collect the nine-digit BIN of the card number and verifies that the delay between the DDC request and the response is at least 7 seconds long. The test fails when fewer than nine digits of the BIN are collected or when the delay between the DDC request and response is too short in duration.  
Do not run this test when your system does not collect device data. When device data is not collected, an older version of the EMV`3-D Secure` protocol is automatically used, and the transaction is automatically assessed as a higher risk.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXX1X XX XXXX XXXX  |

Results for the Check Enrollment Service
----------------------------------------

VERes enrolled = `Y`  
PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt;  
ECI value = `05`

E-Commerce Indicator (ECI) Values
---------------------------------

The following table lists the expected ECI or Collection Indicator values for each network.

| **Network** | **ECI Raw Value** |
|-------------|-------------------|
| Relay        | 05                |

Action
------

If your device data collection method implements correctly and EMV `3-D Secure` processing occurs, the test transaction produces a Frictionless Success result. A failure is indicated when PARes status = `C`. With the failure, a warning message opens to explain the cause of the test failure.

Additional Test Cases {#concept_q2j_r4w_jrb}
============================================

These test cases cover payer authentication scenarios that can occur outside of typical testing. These special use cases might require including additional API fields to accommodate different data that is necessary for that test.
IMPORTANT The test card numbers that are provided are formatted with Xs for zeroes in the card number. When testing with the card numbers, replace a X with a 0 (zero).

1a: First Recurring Transaction: Fixed Amount {#reference_pdg_pqv_frb}
======================================================================

The merchant initiates a 3RI recurring transaction of a fixed amount for a specified number of transactions or with no set number of transactions such as occurs with subscription purchases. For more information, see [Requester Initiated Payments](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-glossary.md "").

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 28X5  |

Required Fields for Check Enrollment
------------------------------------

Message category = `01`  
Device channel = `APP` (01), `BROWSER` (02)  
Three RI Indicator = `01`  
Challenge code = `03`  
Authentication code = `02`  
Purchase date = \&lt;yyyyMMDDHHMMSS\&gt;  
Recurring frequency = \&lt;1 to 31\&gt;  
Recurring end = \&lt;yyyyMMDD\&gt;

Results for the Check Enrollment Service
----------------------------------------

Status = PENDING_AUTHENTICATION  
VERes enrolled = `Y`  
PARes status = `C`  
CAVV = (No value provided)  
ECI = `00`

Results for the Validation Authentication Service
-------------------------------------------------

Status = AUTHENTICATION_SUCCESSFUL` `Authentication is validated.  
PARes status = `Y`  
CAVV = \&lt;CAVV\&gt;  
ECI = `07`

Card Network and Version Specifications
---------------------------------------

Relay Secure 2.1 does not support this type of transaction. Relay Secure 2.2 test cards are in development.  
For Mastercard Identity Check 2.1, 3RI is not supported for Payer Authentication. Only the initial transaction is supported for recurring payments.  
If you attempt to run a Device Channel of 3RI within Mastercard Identity Check 2.1, you receive a transStatusReason=21 (3RI Transaction not supported) reason and a transaction status of `U` rather than `Y`.  
In EMV `3-D Secure` 2.2, Mastercard allocated a new ECI value, ECI 07, for 3RI transactions. It is present on a Mastercard response message for this particular 3RI scenario. For EMV `3-D Secure` 2.1, Mastercard will continue to use ECI 02.

2a: Card Authentication Failed {#reference_udd_wqv_frb}
=======================================================

This scenario tests how your system reacts to various Trans Status Reasons (failed, suspected fraud, and similar instances). When PAResStatus = N, the CardholderInfo field can be returned by the card issuer. When this cardholder information is returned, you must display this information within your checkout experience.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2X4X  |

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_FAILED`  
VERes enrolled = `Y`  
PARes status = `N`  
CAVV = (No value provided)  
Cardholder Info = \&lt;cardholder information\&gt;  
ECI = `07`  
Reason code = `01`

2b: Suspected Fraud {#reference_gyy_crv_frb}
============================================

This test case scenario checks for suspected fraud.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2149  |

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y `  
PARes status = `U`  
CAVV = (No value provided)  
ECI = `07`  
Reason code = `11`

2c: Cardholder Not Enrolled in Service {#reference_x1p_frv_frb}
===============================================================

This test case scenario verifies whether the cardholder is enrolled in the service.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2164  |

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_FAILED`  
VERes enrolled = `Y`  
PARes status = `R`  
CAVV = (No value provided)  
ECI = `07`  
Reason code = `13`

2d: Transaction Timed Out at the ACS {#reference_rqj_jrv_frb}
=============================================================

This test case scenario verifies whether a transaction will time out at the Access Control Server (ACS). This test case is valid for both payer authentication and non-payer authentication transactions.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2172  |

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `U`  
CAVV = (No value provided)  
ECI = `07`  
Reason code = `14`

2e: Non-Payment Transaction Not Supported {#reference_lm4_nrv_frb}
==================================================================

This test case scenario checks whether a non-payment transaction can occur. This test case is valid for both payer authentication and non-payer authentication transactions.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 223X  |

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `U`  
CAVV = (No value provided)  
ECI = `07`  
Reason code = `20`

2f: 3RI Transaction Not Supported {#reference_clt_rrv_frb}
==========================================================

This test case scenario verifies whether the merchant can initiate a recurring 3RI transaction, such as with subscriptions.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2248  |

Required Fields for Check Enrollment
------------------------------------

Message category = `02`  
Device channel = `3RI (03)`  
Three RI Indicator = `01`

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `U`  
CAVV = (No value provided)  
ECI = `07`  
Reason code = `21`

3a: TRA Exemption---Low Value: Mastercard EMV `3-D Secure` 2.1 and 2.2 {#reference_zpd_z2l_2rb}
===============================================================================================

You have performed a proprietary risk assessment based on fraud thresholds established with the network. You are requesting an exemption from transaction risk analysis (TRA) because the Mastercard transaction is low risk or low value. Be sure to use the correct test card number for your version of EMV `3-D Secure`. The PARes Status will differ between the EMV `3-D Secure`versions.

|       **Card Type**        |                           **Test Card Number**                           |
|----------------------------|--------------------------------------------------------------------------|
| Mastercard Card Type = 002 | (version 2.1.0) 52XX XXXX XXXX 1161 (version 2.2.0) 52XX XX XX XXXX 2X52 |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `05`

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
**Version 2.1.0**  
VERes enrolled = `Y`  
PARes status = `N`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `06`  
Reason code = `81`  
For Mastercard Identity Check, the Challenge Indicator should be passed as `05`.  
**Version 2.2.0**  
VERes enrolled = `Y`  
PARes status = `I`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `06`

Action
------

Proceed to authorization.  
You can also request the transaction risk analysis exemption directly during authorization if the region and your agreements with your acquirer and the networks support it.

3b: TRA---Low Value: Relay {#reference_lcx_g5m_2rb}
==================================================

The merchant has performed a proprietary risk assessment based on fraud thresholds established with the network. You are requesting an exemption for a low risk or low value Relay transaction.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2X24  |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `05` (no challenge requested)

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `I`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `07`

Action
------

Proceed to authorization.  
You can also request the transaction risk analysis exemption directly during authorization if the region and your agreements with your acquirer and the networks support it.

3c: TRA---Low Value: Discover {#reference_y3w_s5m_2rb}
======================================================

The merchant has performed a proprietary risk assessment based on fraud thresholds established with the network. You are requesting an exemption for a low risk or low value Discover transaction.

|      **Card Type**       | **Test Card Number** |
|--------------------------|----------------------|
| Discover Card Type = 004 | 6X11XX XX XXXX 1XX2  |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `04` (challenge requested)

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `05`

Action
------

Proceed to authorization.  
You can also request the transaction risk analysis exemption directly during authorization if the region and your agreements with your acquirer and the networks support it.

3d: Acquirer TRA: Cartes Bancaires {#pa-testing-3ds-2x-tra-lv-cartes-bancaires}
===============================================================================

The merchant has performed a proprietary risk assessment based on fraud thresholds established with the network. You are requesting an exemption for a low risk or low value Cartes Bancaires transaction.

|               **Card Type**                | **Test Card Number** |
|--------------------------------------------|----------------------|
| Cartes Bancaires Relay Card Type = 036      | 4XXXXX XX XXXX 3XX6  |
| Cartes Bancaires Mastercard Card Type =036 | 52XXXX XX XXXX 3XX1  |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `05` (no challenge requested)

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
VERes enrolled = `Y`  
PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt; (The CAVV value is not returned during testing but can be returned in production based on issuer rules surrounding co-branding with Relay or Mastercard BINs.)  
ECI = (no value provided)

Action
------

Proceed to authorization.  
You can also request the transaction risk analysis exemption directly during authorization if the region and your agreements with your acquirer and the networks support it.

4a: Trusted Beneficiary Prompt for Trustlist {#reference_abt_1vm_2rb}
=====================================================================

You have a successful traditional step-up (challenge) authentication transaction with a prompt for the Trustlist and an accepted exemption result.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Relay Card Type = 001       | 4XXXXX XX XXXX 2XX8  |
| Mastercard Card Type = 002 | 52XXXX XX XXXX 2XX3  |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `09` (challenge requested)

Results for the Check Enrollment Service
----------------------------------------

With the Direct API, the response also includes a StepUpUrl.  
VERes enrolled = `Y`  
PARes status = `C`  
CAVV = (No value provided)

Results for the Authenticate Response
-------------------------------------

PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt;  
ECI =

* Relay = `05`
* Mastercard = `02`

{#reference_abt_1vm_2rb_ul_y3q_tdh_jwb}  
WhiteListStatus = \&lt;WhiteListStatus value\&gt;  
WhiteListStatusSource = \&lt;WhiteListStatusSource value\&gt;

Action
------

You should append the CAVV and ECI values to the authorization message.

4b: Use Trusted Beneficiary Exemption {#reference_wgf_fvm_2rb}
==============================================================

There is a successful frictionless authentication transaction with a pre-approved indication and an accepted exemption result.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Relay Card Type = 001       | 4XXXXX XX XXXX 2X16  |
| Mastercard Card Type = 002 | 52XXXX XX XXXX 2X11  |

Required Fields for Check Enrollment
------------------------------------

Challenge code = `08` (No challenge requested)

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
PARes status = `Y`  
CAVV = \&lt;CAVV value\&gt;  
ECI =

* Relay = `05`
* Mastercard = `02`

{#reference_wgf_fvm_2rb_ul_vtp_wdh_jwb}  
WhiteListStatus = \&lt;WhiteListStatus value\&gt;  
WhiteListStatusSource = \&lt;WhiteListStatusSource value\&gt;  
ThreeDSVersion = \&lt;ThreeDSVersion value\&gt;

Action
------

Append the CAVV and ECI values to the authorization message.

5a: Relay Data Only {#reference_zdc_wwc_grb}
===========================================

This request is for Relay Data Only authentication. This is a frictionless authentication because it is for informational purposes. Using Payer Authentication to share additional data with issuers prior to authorization, `3-D Secure` Data Only provides a frictionless experience with EMV `3-D Secure`.

|    **Card Type**     | **Test Card Number** |
|----------------------|----------------------|
| Relay Card Type = 001 | 4XXXXX XX XXXX 2X24  |

Required Fields for Check Enrollment {#reference_zdc_wwc_grb_section_xyv_cfr_krb}
---------------------------------------------------------------------------------

ChallengeIndicator = `06`

Results for the Check Enrollment Service
----------------------------------------

PAResStatus = `I`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `07` Status = `AUTHENTICATION_SUCCESSFUL`

Action
------

Append the ECI and Directory Server transaction ID values to the authorization message.

5b: Identity Check Insights (ScoreRequest = Y) {#reference_jry_vrv_frb}
=======================================================================

This request is for Mastercard Data Only authentication.

|       **Card Type**        | **Test Card Number** |
|----------------------------|----------------------|
| Mastercard Card Type = 002 | 52XXXX XX XXXX 1XX5  |

Required Fields for Check Enrollment
------------------------------------

Message Category = `80`  
**Optional Fields for Check Enrollment**  
Score Request = `Y`  
Merchant Reason Code = `A`

Results for the Check Enrollment Service
----------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`  
PAResStatus = `U`  
CAVV = \&lt;CAVV value\&gt;  
ECI = `04`  
StatusReason = `80`  
ThreeDSVersion = \&lt;ThreeDSVersion value\&gt;  
**Optional Results for the Check Enrollment Service (if ScoreRequest = `Y`)**  
IDCI_Score = `9`  
IDCI_Decisions = `not low risk`  
IDCI_ReasonCode1 = `A`  
IDCI_ReasonCode2 = `GG`

Results for the Authentication Result
-------------------------------------

Status = `AUTHENTICATION_SUCCESSFUL`

Action
------

Append the ECI and Directory Server transaction ID values to the authorization message.

Website Modification Reference {#concept_ifc_wp3_ypb}
=====================================================

This section describes how to modify your website to integrate Payer Authentication services into your checkout process. It also provides links to payment card company websites where you can download the appropriate logos.

Website Modification Checklist {#concept_rgx_wq3_ypb}
=====================================================

Modify web page buttons:

* Order submission button: Disable the final "buy" button until the customer completes all payment and authentication requirements.
* Browser back button: Plan for unexpected customer behavior. Check throughout the authentication process so you do not authenticate transactions twice. Avoid confusing messages, such as warnings about expired pages.

{#concept_rgx_wq3_ypb_ul_pgf_1r3_ypb}  
Add appropriate logos:

* Download the appropriate logos of the cards that you support. Place these logos next to the card information entry fields on your checkout pages. For more information about obtaining logos and using them, see [EMV 3-D Secure Service Logos](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-website-modification-reference-intro/pa-website-modification-reference-3d-secure-servic.md "").

{#concept_rgx_wq3_ypb_ul_t3s_1r3_ypb}  
Add informational message:
* Add a message next to the final "buy" button and the card logo to inform your customers that they might be prompted to provide their authentication password. For examples of messages you can use, see [Informational Message Examples](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-website-modification-reference-intro/pa-website-modification-reference-informational-me.md "").
  {#concept_rgx_wq3_ypb_ul_wzy_1r3_ypb}

EMV `3-D Secure` Service Logos {#concept_rhg_jr3_ypb}
=====================================================

This table contains links to payment card company websites from which you can download logos and information about how to incorporate them into your online checkout process.

| EMV `3-D Secure` Service              | Download Location                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relay Secure                           | [https://usa.relay.com/run-your-business/small-business-tools/payment-technology/relay-secure.html](https://usa.relay.com/run-your-business/small-business-tools/payment-technology/relay-secure.md "") This website contains information about Relay Secure and links to logos for download. The page also contains links to a best practice guide for implementing Relay Secure and a link to a Merchant Toolkit. |
| Mastercard Identity Check and Maestro | [https://brand.mastercard.com/brandcenter.html](https://brand.mastercard.com/brandcenter.md "") This website contains information about Identity Check, links to logos for download, and information about integrating the Identity Check information into your website checkout page. For information about Maestro logos, go to: <http://www.mastercardbrandcenter.com/us/howtouse/bms_mae.shtml>           |
| American Express SafeKey              | <https://network.americanexpress.com/uk/en/safekey/> This website contains information about SafeKey and links to logos for download.                                                                                                                                                                                                                                                                         |
| JCB J/Secure                          | [http://partner.jcbcard.com/security/jsecure/logo.html](http://partner.jcbcard.com/security/jsecure/logo.md "") This website contains information about J/Secure and links to logos for download.                                                                                                                                                                                                             |
| Diners Club ProtectBuy                | <https://www.dinersclubus.com/home/customer-service> Contact Diners Club customer service for assistance.                                                                                                                                                                                                                                                                                                     |
| Discover ProtectBuy                   | <https://www.discovernetwork.com/en-us/business-resources/free-signage-logos> This website contains information about Discover ProtectBuy and links to logos for download.                                                                                                                                                                                                                                    |
| Elo Compra Segura                     | Contact Elo customer support to obtain logos.                                                                                                                                                                                                                                                                                                                                                                 |
| China UnionPay                        | Contact China UnionPay customer support to obtain logos.                                                                                                                                                                                                                                                                                                                                                      |
[`3-D Secure` Service Logos Download Location]

Informational Message Examples {#concept_lbh_tr3_ypb}
=====================================================

Add a brief message next to the final buy button on your checkout page to inform customers that they might be prompted for their authentication password or to enroll in the authentication program for their card.  
These examples might be used, but consult your specific card authentication program to make sure you conform to their messaging requirements.
Example
To help prevent unauthorized use of *\&lt;card_type\&gt;* cards online, *\&lt;your_business_name\&gt;* participates in *\&lt;card_authentication_program\&gt;* . When you submit your order, you might receive a *\&lt;card_authentication_program\&gt;* message from your *\&lt;card_type\&gt;* card issuer. If your card or issuer does not participate in the program, you are returned to our secure checkout to complete your order. Please wait while the transaction is processed. Do not click the Back button or close the browser window. Example
Your card might be eligible for Relay Secure, Mastercard, Maestro, American Express SafeKey, JCB J/Secure, Diners Club ProtectBuy, or Discover ProtectBuy programs. After you submit your order, your card issuer might prompt you to authenticate yourself. This authentication can be done through a one-time pass code sent to your phone or email, by biometrics, or some other form of authentication.

Finding Payer Authentication Transaction Details in the `Business Center` {#pa-transx-details-in-ebc-intro}
===========================================================================================================

This section describes how to find the details of Payer Authentication transactions in the `Business Center`. You need certain information about a transaction to respond to a chargeback. For details about past transactions, from the left navigation pane, go to Transaction Management \&gt; Transactions. This detailed data about a past transaction is stored for 12 months.

Searching for Transactions {#concept_wgx_nk3_ypb}
=================================================

You can search for transactions that used the payer authentication and card authorization services by going to Transactions Management \&gt; Transactions. When searching for transactions, consider these things:

* Search options:
  * To find the details of a transaction, on the Transactions page enter its PA Transaction ID into the Quick Search field.
  * On the Transactions page, you can also create a payer authentication transaction ID filter by clicking Add filter and selecting `PA Transaction ID` as the filter. You can then enter the transaction ID as the filter criteria.
  * The list of applications is simplified to facilitate searching for the relevant service requests.
  * Payer authentication information is available for 12 months after the transaction date.
    {#concept_wgx_nk3_ypb_ul_myg_sk3_ypb}
* Search results: the results options include the Payer Authentication transaction ID and the customer's account number (PAN). Use the Payer Authentication transaction ID to find all parts of the transaction.
* Payer authentication details: all transaction details are discussed under Searching for Payer Authentication Details. For more information, see [Searching for Payer Authentication Details](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-transx-details-in-ebc-intro/pa-transx-details-in-ebc-searching-pa-details.md "").
  {#concept_wgx_nk3_ypb_ul_gt1_sk3_ypb}

Storing Payer Authentication Data {#pa-part-tranx-details-ebc-storing-pa-data}
==============================================================================

Payment card companies permit only a certain number of days between the payer authentication and the authorization request. If you settle transactions that are older than the predetermined number of days, payment card companies might require that you send them the AAV, CAVV, or the XID when a chargeback occurs. The requirements depend on the card type and the region. For more information, refer to your agreement with your payment card company. You can get this type of information from the transaction details. The payer authentication transaction ID is listed in the transaction log. To access the transaction log, go to the Transaction Details page and in the Request Information section, click the View button. After your transactions are settled, you can also use this data to update the statistics of your business.

Searching for Payer Authentication Details {#pa-tranx-details-in-ebc-searching-pa-details}
==========================================================================================

Search the payer authentication data returned in API response fields with the Transaction Search feature in the `Business Center`.  
Interpret the result of an enrollment check using this color coding.

* If the application result appears in green, you do not need to authenticate the user. You can authorize the card immediately.
* If the application result appears in red, the authentication failed.
* If the application result appears in yellow, the transaction requires authentication.
  {#pa-tranx-details-in-ebc-searching-pa-details_ul_u3t_xh3_ypb}

Enrolling a Card {#pa-tranx-details-in-ebc-enrolled-cards}
==========================================================

Enrolling a card consists of two steps:

1. Checking for enrollment.
2. Authenticating the customer.
   {#pa-tranx-details-in-ebc-enrolled-cards_ul_xs3_k33_ypb}

Checking Enrollment {#pa-tranx-details-in-ebc-enrolled-cards-enrollment-check}
==============================================================================

You can find payer authentication data on the Transaction Details page in these sections:

* Request Information section: The enrollment check service is shown in red when the card is enrolled. You receive the corresponding response. If the card authorization service was requested at the same time, it did not run and appears in black.
* Order Information section: When authentication is required, American Express SafeKey requires that you save the XID for later use. You do not receive an ECI, AAV, or CAVV because the authentication is not complete.

{#pa-tranx-details-in-ebc-enrolled-cards-enrollment-check_ul_ysp_s33_ypb}  
If the CAVV and ECI are not provided, and the enrollment transaction results in a challenge, authentication is required.

Authentication Validation {#pa-tranx-details-in-ebc-enrolled-cards-auth-validation}
===================================================================================

When an authentication is valid and the card authorization succeeds, payer authentication data appears in the Transaction Search Details window in these sections:

* Request Information section: The validation service succeeded. A reason code 100 was returned with the corresponding response. The necessary payer authentication information was passed to the card authorization service, which processed successfully. Both services are shown in green.
* Order Information section: You received a value for all three parameters because the validation was successful. You might not receive an ECI value when a system error prevents the card issuer from performing the validation or when the cardholder does not complete the process.
  {#pa-tranx-details-in-ebc-enrolled-cards-auth-validation_ul_fd4_pj3_ypb}

Card Not Enrolled {#pa-tranx-details-in-ebc-card-not-enrolled}
==============================================================

When a card is not enrolled, the result of the enrollment check service appears in green, and the card authorization request (if requested at the same time) proceeds normally.

Transaction Details {#pa-tranx-details-in-ebc-card-not-enrolled-transx-details}
===============================================================================

Enter the payer authentication transaction ID into the quick search feature to find all segments of a transaction. For a transaction in which the card is not enrolled, find payer authentication data in the Transaction Details window in these sections:

* Request Information section: The service appears in green. You can obtain additional information about related orders by clicking the link on the right.
* Order Information section:
  * For Mastercard, the ECI value is 00: authentication is not required because the customer's Mastercard card is not enrolled. Other cards have an ECI value of 07.
  * The AAV/CAVV area is empty because you receive a value only when the customer is authenticated.
  * The XID area is empty because the card is not enrolled.
    {#pa-tranx-details-in-ebc-card-not-enrolled-transx-details_ul_vrz_gk3_ypb}

{#pa-tranx-details-in-ebc-card-not-enrolled-transx-details_ul_z4s_fk3_ypb}  
You might encounter these reason codes:

465: DAUTHENTICATE
:
Encountered a Payer Authentication problem. Payer could not be authenticated. Authenticate the cardholder before continuing with the transaction.

475: DAUTHENTICATE​
:
The cardholder is enrolled in Payer Authentication.​ Authenticate the cardholder before continuing with the transaction.​

476​: DAUTHENTICATIONFAILED​
:
Encountered a Payer Authentication problem. Payer could not be authenticated.​ Authenticate the cardholder before continuing with the transaction.​

261​: DINVALIDDATA​
:
The merchant account set up is either invalid or missing on the acquirer's gateway. ​Check the currency, acquirer ID, merchant ID configuration. If these are configured as expected, contact the acquirer​.

Payer Authentication Reports {#concept_db3_ht3_ypb}
===================================================

This section describes the Payer Authentication reports that you can download from the `Business Center`.  
All reports on the production servers are retained for 16 months, but the transaction history is kept in the database for only 12 months. All reports on the test servers are deleted after 60 days. Only transactions that were processed are reported. Those transactions that resulted in a system error or a time-out are not reported.  
To get access to the reports, you must file a support ticket in the Support Center.

Payer Authentication Summary Report {#concept_e2n_wt3_ypb}
==========================================================

This daily, weekly, and monthly summary report indicates the performance of the enrollment and validation services as a number of transactions and a total amount for groups of transactions. The report provides this information for each currency and type of card that you support. You can use this information to estimate how payer authentication screens your transactions: successful, attempted, and incomplete authentication. The cards reported are Relay, Mastercard,JCB,Maestro, China UnionPay, Elo,Diners Club, Discover, and American Express. This daily report is generally available by 7:00 a.m. EST. Data in this report remains available for 6 months.

Download the Report {#task_tfd_c53_ypb}
=======================================

Follow these steps to view the Payer Authentication Summary report:

1. In the left navigation panel, click the Reports icon.
2. Under Transaction Reports, click **Payer Auth Summary**. The Payer Auth Summary Report page appears.
3. In the search toolbar, select a date range to include in the report. Account-level users must select a merchant as well.
4. Based on the date range you selected, choose the specific day, week, or month you want to review.

#### RESULT

Only months that have already occurred in the current year display in the Month list. To view all months of a previous year, select the year first, and then choose the month.  
To view results from before the selected period, click Previous. Click Next to see the next period.

Matching the Report to the Transaction Search Results {#reference_ltd_cv3_ypb}
==============================================================================

The image below shows the search results that contain the transactions that appear in the report. For more information on search results, see [Searching for Payer Authentication Details](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-transx-details-in-ebc-intro/pa-transx-details-in-ebc-searching-pa-details.md "").

#### Figure: {#reference_ltd_cv3_ypb_fig_rgm_gxf_w2c}

Payer Authentication Report Details  
![](/content/dam/documentation/cybs/en-us/topics/risk/payer-authentication/payer-auth/images/pa-transaction-details.png/jcr:content/renditions/original)

Interpreting the Report {#concept_o3d_lv3_ypb}
==============================================

The report is organized by card type. In each card type section, currencies are reported alphabetically. For each currency, a summary of your payer authentication validation results appear as a total amount and number of transactions.

|            Card Type            |          Interpretation          | Protected? |     Commerce Indicator     | ECI |
|---------------------------------|----------------------------------|------------|----------------------------|-----|
| Relay, American Express, and JCB | No authentication                | No         | Internet                   | 7   |
| Relay, American Express, and JCB | Recorded attempt to authenticate | Yes        | VbV, Desk, or JS Attempted | 6   |
| Relay, American Express, and JCB | Successful authentication        | Yes        | VbV, JS, or Aesk           | 5   |
| Mastercard, Meeza, and Maestro  | No authentication                | No         | Internet\*\*               | 7\* |
| Mastercard, Meeza, and Maestro  | Recorded attempt to authenticate | Yes        | SPA                        | 1   |
| Mastercard, Meeza, and Maestro  | Successful authentication        | Yes        | SPA                        | 2   |
| Diners Club and Discover        | No authentication                | No         | Internet                   | 7   |
| Diners Club and Discover        | Recorded attempt to authenticate | Yes        | PB or DIPB Attempted       | 6   |
| Diners Club and Discover        | Successful authentication        | Yes        | PB or DIPB                 | 5   |
| China UnionPay and Elo          | No authentication                | No         | Internet                   | 7   |
| China UnionPay and Elo          | Recorded attempt to authenticate | Yes        | CS or Up3ds Attempted      | 6   |
| China UnionPay and Elo          | Successful authentication        | Yes        | CS or Up3ds                | 5   |
[Payer Authentication Report Interpretation]

\* Although the report heading is 7, you receive a collection indicator value of 1, or the response field is empty.  
\*\* Although the report heading is Internet, you receive `spa_failure` in the commerce indicator response field.  
Transactions are divided into two groups: those for which you are protected and those for which you are not protected:

* For Relay,China UnionPay, Elo, JCB, Diners Club, Discover, and American Express: liability shift for VbV and VbV attempted.
* For Mastercard and Maestro: liability shift only for SPA.
* For all other results: no liability shift.
  {#concept_o3d_lv3_ypb_ul_wns_5v3_ypb}

Comparing Payer Authentication and Payment Reports {#concept_h5x_2w3_ypb}
=========================================================================

The Payer Authentication report and the payment reports might differ when an authenticated transaction is not authorized.  
The values (amounts and counts) in the Payer Authentication report might not match your other sources of reconciliation. This report shows the transactions validated by payer authentication. A different number of transactions might have been authorized.  
The amounts and numbers can be higher in the Payer Authentication report than in the payment reports. This example shows the results of the first two numbers in the Payer Authentication report and the last number in the payment reports.  
To reconcile your reports more easily when using payer authentication, we recommend that you attempt to authenticate the same amount that you want to authorize.
Payer Authentication Reports Compared to Payment Reports
For 10,000 orders, you might receive these results:

* 9900 successful enrollment checks (Payer Authentication report)
* 9800 successful authentication checks (Payer Authentication report)
* 9500 successful authorization checks (Payment report)
  {#concept_h5x_2w3_ypb_ul_mff_hw3_ypb}

Payer Authentication Detail Report {#concept_azl_nx3_ypb}
=========================================================

This section describes the elements of the Payer Authentication Detail report.  
Refer to the [*Reporting User Guide*](https://developer.cybersource.com/docs/cybs/en-us/reporting/user/all/ebc/reporting-ug/Get_Started_with_Business_Center_Reporting.md "") for instructions for downloading the report and additional report information.

Report Element {#reference_cgs_jlg_cqb}
=======================================

The `Report` element is the root element of the report.

```
&lt;Report&gt;
&lt;PayerAuthDetails&gt;
  (PayerAuthDetail+)
&lt;/PayerAuthDetails&gt;
&lt;/Report&gt;
```

| Element Name       | Description                                                                                                                                                                                                                                                                                                    |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PayerAuthDetails` | Contains the transaction in the report. For a list of child elements, see [`PayerAuthDetail`](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-reports-intro/pa-reports-auth-details-report/pa-reports-auth-details-report-elements-payerauthd.md ""). |
[Child Elements of Report]

PayerAuthDetails Element

```keyword
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE Report SYSTEM "https://api.cybersource.com/reporting/v3/dtds/padr"&gt;
&lt;PayerAuthDetails&gt;
  &lt;PayerAuthDetail&gt;
    ...
  &lt;/PayerAuthDetail&gt;
&lt;/PayerAuthDetails&gt;
```

PayerAuthDetail Element {#reference_hjp_pmg_cqb}
================================================

The `PayerAuthDetail` element contains information about a single transaction.

```
&lt;PayerAuthDetail&gt;
  (RequestID)
  (MerchantID)
  (RequestDate)
  (TransactionType)
  (PAReq)?
  (PARes)?
  (AuthInfo)?
&lt;/PayerAuthDetail&gt;
```

| Element Name  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type \& Length |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| `RequestID`   | Unique identifier generated for the transaction. This field corresponds to the API field.                                                                                                                                                                                                                                                                                                                                                    | Numeric (26)   |
| `MerchantID`  | Merchant ID used for the transaction.                                                                                                                                                                                                                                                                                                                                                                                                        | String (30)    |
| `RequestDate` | Date on which the transaction was processed.                                                                                                                                                                                                                                                                                                                                                                                                 | DateTime (25)  |
| `PAReq`       | The Payer Authentication Request message sent to the ACS through the payment card company. Corresponds to the consumerAuthenticationInformation.payer AuthEnrollReply_paReq API field. For a list of child elements, see [PAReq](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-reports-intro/pa-reports-auth-details-report/pa-reports-auth-details-report-elements-pareq.md ""). |                |
| `PARes`       | The Payer Authentication Response message sent by the ACS. For a list of child elements, see [PARes](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-reports-intro/pa-reports-auth-details-report/pa-reports-auth-details-report-elements-pares.md "").                                                                                                                             |                |
| `AuthInfo`    | Address and card verification data. For a list of child elements, see [AuthInfo Element](/docs/cybs/en-us/payer-authentication/developer/all/rest/payer-auth/pa-reports-intro/pa-reports-auth-details-report/pa-reports-auth-details-report-elements-authinfo.md "").                                                                                                                                      |                |
[Child Elements of PayerAuthDetail]

PayerAuthDetail Element

```
&lt;PayerAuthDetail&gt;
  &lt;RequestID&gt;0004223530000167905139&lt;/RequestID&gt;
  &lt;MerchantID&gt;example_merchant&lt;/MerchantID&gt;
  &lt;RequestDate&gt;2020-02-09T08:00:09-08:00&lt;/RequestDate&gt;
  &lt;TransactionType&gt;ics_pa_enroll&lt;/TransactionType&gt;
  &lt;PAReq&gt;
    ...
  &lt;/PAReq&gt;
  &lt;PARes&gt;
    ...
  &lt;/PARes&gt;
&lt;/PayerAuthDetail&gt;          
```

PAReq Element {#reference_g5l_2rg_cqb}
======================================

The `PAReq` element contains the payer authentication request message. This element corresponds to the consumerAuthenticationInformation.pareq API field.

```
&lt;PAReq&gt;
  (AcqBIN)
  (MerID)
  (Name)
  (Country)
  (URL)
  (XID)
  (Date)
  (PurchaseAmount)
  (AcctID)
  (Expiry)
&lt;/PAReq&gt;
```

| Element Name    | Description                                                                                                                                                                                                                                                                                                                                               | Type \& Length |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| `AcqBIN`        | First six digits of the acquiring bank's identification number.                                                                                                                                                                                                                                                                                           | Numeric (6)    |
| `MerID`         | Identifier provided by your acquirer to the merchant to log in to the ACS URL.                                                                                                                                                                                                                                                                            | String (24)    |
| `Name`          | Merchant's company name.                                                                                                                                                                                                                                                                                                                                  | String (25)    |
| `Country`       | Two-character code for the merchant's country of operation.                                                                                                                                                                                                                                                                                               | String (2)     |
| `URL`           | Merchant's business website.                                                                                                                                                                                                                                                                                                                              | String         |
| `XID`           | Unique transaction identifier generated for each Payment Authentication Request (PAReq) message. The PARes sent back by the issuing bank contains the XID of the PAReq. To ensure that both XIDs are the same, compare it to the XID in the response. To find all requests related to a transaction, you can also search transactions for a specific XID. | String (28)    |
| Date            | Date and time of request. Differing time zones and the lack of synchronization between servers might prevent the date and time from appearing sequentially during all stages of processing.                                                                                                                                                               | DateTime (25)  |
| Purchase Amount | Authorization amount and currency for the transaction. This element corresponds to the totals of the offer lines or from: orderInformation.amountDetails.totalAmount or purchaseTotals_grandTotalAmount from external data                                                                                                                                | Amount (15)    |
| AcctID          | Masked string used by the ACS.                                                                                                                                                                                                                                                                                                                            | String (28)    |
| Expiry          | Expiration month and year of the customer's card.                                                                                                                                                                                                                                                                                                         | Number (4)     |
[Child Elements of PAReq]

PAReq Element

```
&lt;PAReq&gt;
  &lt;AcqBIN&gt;123456&lt;/AcqBIN&gt;
  &lt;MerID&gt;444444&lt;/MerID&gt;
  &lt;Name&gt;example&lt;/Name&gt;
  &lt;Country&gt;US&lt;/Country&gt;
  &lt;URL&gt;http://www.example.com&lt;/URL&gt;
  &lt;XID&gt;fr2VCDrbEdyC37MOPfIzMwAHBwE=&lt;/XID&gt;
  &lt;Date&gt;2020-02-09T08:00:34-08:00&lt;/Date&gt;
  &lt;PurchaseAmount&gt;1.00 USD&lt;/PurchaseAmount&gt;
  &lt;AcctID&gt;NDAxMjAwMTAxMTAwMDc3MQ==&lt;/AcctID&gt;
  &lt;Expiry&gt;2309&lt;/Expiry&gt;
&lt;/PAReq&gt;
```

PARes Element {#reference_b13_3tg_cqb}
======================================

The `PARes` element contains the payer authentication response.

```
&lt;PARes&gt;
  (AcqBIN)
  (MerID)
  (XID)
  (Date)
  (PurchaseAmount)
  (PAN)
  (AuthDate)
  (Status)
  (CAVV)
  (ECI)
&lt;/PARes&gt;
```

| Element Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                | Type \& Length |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| `AcqBIN`         | First six digits of the acquiring bank's identification number.                                                                                                                                                                                                                                                                                                                                            | Numeric (6)    |
| `MerID`          | Identifier provided by your acquirer; used to log in to the ACS URL.                                                                                                                                                                                                                                                                                                                                       | String (24)    |
| `XID`            | XID value returned in the customer authentication response. This element corresponds to the consumerAuthenticationInformation.xid API fields.                                                                                                                                                                                                                                                              | String (28)    |
| `Date`           | Date and time of request. Differing time zones and the lack of synchronization between servers might prevent the date and time from appearing sequentially during all stages of processing.                                                                                                                                                                                                                | DateTime (25)  |
| `PurchaseAmount` | Authorization amount and currency for the transaction. This element corresponds to the totals of the offer lines or from the orderInformation.amountDetails.totalAmount                                                                                                                                                                                                                                    | Amount (15)    |
| `PAN`            | Customer's masked account number. This element corresponds to the consumerAuthenticationInformation. proxyPan API field.                                                                                                                                                                                                                                                                                   | String (19)    |
| `AuthDate`       | Date and time of request. (Although the date and time should appear sequentially during all stages of the processing of an order, they may not because of differing time zones and synchronization between servers.)                                                                                                                                                                                       | DateTime (25)  |
| `Status`         | Result of the authentication check. This field contains one of these values: * `Y`: Customer was successfully authenticated. * `N`: Customer failed or cancelled authentication. Transaction denied. * `U`: Authenticate not completed regardless of the reason. * `A`: Proof of authentication attempt was generated. {#reference_b13_3tg_cqb_ul_fr3_r5g_cqb}                                             | String (1)     |
| `CAVV`           | CAVV (Relay, American Express, JCB, China UnionPay, Elo,Diners Club, and Discover cards) element corresponds to the consumerAuthenticationInformation.cavv field returned in the customer authentication response. The AAV (Mastercard, and Maestro cards) element corresponds to the consumerAuthenticationInformation.ucaf AuthenticationData API field returned in the customer authentication response. | String (50)    |
| `ECI`            | Electronic Commerce Indicator returned in the customer authentication response. This element corresponds to the consumerAuthenticationInformation.eci and consumerAuthenticationInformation.ucaf CollectionIndicator API fields.                                                                                                                                                                           | Numeric (1)    |
[Child Elements of PARes]

PARes Element

```
&lt;PARes&gt;
  &lt;AcqBIN&gt;123456&lt;/AcqBIN&gt;
  &lt;MerID&gt;4444444&lt;/MerID&gt;
  &lt;XID&gt;Xe5DcjrqEdyC37MOPfIzMwAHBwE=&lt;/XID&gt;
  &lt;Date&gt;2020-02-09T07:59:46-08:00&lt;/Date&gt;
  &lt;PurchaseAmount&gt;1002.00 USD&lt;/PurchaseAmount&gt;
  &lt;PAN&gt;0000000000000771&lt;/PAN&gt;
  &lt;AuthDate&gt;2020-02-09T07:59:46-08:00&lt;/AuthDate&gt;
  &lt;Status&gt;Y&lt;/Status&gt;
  &lt;CAVV&gt;AAAAAAAAAAAAAAAAAAAAAAAAAAA=&lt;/CAVV&gt;
  &lt;ECI&gt;5&lt;/ECI&gt;
&lt;/PARes&gt;
```

AuthInfo Element {#reference_rfx_4wg_cqb}
=========================================

The `AuthInfo` element contains address and card verification information.

```
&lt;AuthInfo&gt;
  (AVSResult)
  (CVVResult)
&lt;/AuthInfo&gt;
```

| Element Name | Description                                   | Type \& Length |
|:-------------|:----------------------------------------------|:---------------|
| `AVSResult`  | Results of the address verification test.     | String (1)     |
| `CVVResult`  | Results of the card verification number test. | String (1)     |
[Child Elements of AuthInfo]

AuthInfo Element

```
&lt;AuthInfo&gt;
  &lt;AVSResult&gt;Y&lt;/AVSResult&gt;
  &lt;CVVResult/&gt;git 
&lt;/AuthInfo&gt;
```

Report Examples {#reference_fb5_lrn_cqb}
========================================

These examples show a complete transaction: the failed enrollment check (enrolled card) and the subsequent successful authentication.  
For transactions in India, use [transactionProcessor](https://ics2ws.in.ic3.com/commerce/1.x/transactionProcessor ""). Failed Enrollment Check

```keyword
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE Result SYSTEM "https://api.cybersource.com/reporting/v3/dtd/padr"&gt;
&lt;Report&gt;
Name="Payer Authentication Detail" 
Version="1.0”
xmlns="https://api.cybersource.com/reporting/v3/dtds/padr" 
MerchantID="sample_merchant_id" 
ReportStartDate="2022-02-09T08:00:00-08:00" 
ReportEndDate="2022-02-10T08:00:00-08:00"
&lt;PayerAuthDetails&gt;
   &lt;PayerAuthDetail&gt;
      RequestID=”1895549430000167904548”
      TransactionType=”ics_pa_enroll
      RequestDate=”2022-02-09T08:00:02-08:00”
      &lt;ProofXML&gt;
         &lt;Date&gt;20220209 08:00:34&lt;/Date&gt;
         &lt;DSURL&gt;https:123.456.789.01:234/DSMsgServlet&lt;/DSURL&gt;
         &lt;PAN&gt;XXXXXXXXXXXX0771&lt;/PAN&gt;
         &lt;AcqBIN&gt;123456&lt;/AcqBIN&gt;
         &lt;MerID&gt;4444444&lt;/MerID&gt;
         &lt;Password /&gt;
         &lt;Enrolled&gt;Y&lt;/Enrolled&gt;
      &lt;/ProofXML&gt;
      &lt;VEReq&gt;
         &lt;PAN&gt;XXXXXXXXXXXX0771&lt;/PAN&gt;
         &lt;AcqBIN&gt;123456&lt;/AcqBIN&gt;
         &lt;MerID&gt;example&lt;/MerID&gt;
      &lt;/VEReq&gt;
      &lt;VERes&gt;
         &lt;Enrolled&gt;Y&lt;/Enrolled&gt;
         &lt;AcctID&gt;NDAxMjAwMTAxMTAwMDc3MQ==&lt;/AcctID&gt;
         &lt;URL&gt;https://www.sample_url.com&lt;/URL&gt;
      &lt;/VERes&gt;
      &lt;PAReq&gt;
         &lt;AcqBIN&gt;123456&lt;/AcqBIN&gt;
         &lt;MerID&gt;example&lt;/MerID&gt;
         &lt;Name&gt;Merchant Name&lt;/Name&gt;
         &lt;Country&gt;US&lt;/Country&gt;
         &lt;URL&gt;http://www.merchant_url.com&lt;/URL&gt;
         &lt;XID&gt;2YNaNGDBEdydJ6WI6aFJWAAHBwE=&lt;/XID&gt;
         &lt;Date&gt;2022-02-09T08:00:34-08:00&lt;/Date&gt;
         &lt;PurchaseAmount&gt;1.00 USD&lt;/PurchaseAmount&gt;
         &lt;AcctID&gt;NDAxMjAwMTAxMTAwMDc3MQ==&lt;/AcctID&gt;
         &lt;Expiry&gt;2309&lt;/Expiry&gt;
      &lt;/PAReq&gt;
   &lt;/PayerAuthDetail&gt;
&lt;/PayerAuthDetails&gt;
&lt;/Report&gt;
```

Successful Authentication

```keyword
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE Result SYSTEM "https://api.cybersource.com/reporting/v3/dtd/padr"&gt;
&lt;Report&gt;
&lt;PayerAuthDetails&gt;
   &lt;PayerAuthDetail&gt;
      RequestID=”1895549900000167904548”
      TransactionType=”ics_pa_validate”
      XID=”2YNaNGDBEdydJ6WI6aFJWAAHBwE=”
      RequestDate=”2022-02-09T08:00:02-08:00”
      &lt;PARes&gt;
         &lt;AcqBIN&gt;469216&lt;/AcqBIN&gt;
         &lt;MerID&gt;6678516&lt;/MerID&gt;
         &lt;XID&gt;2YNaNGDBEdydJ6WI6aFJWAAHBwE=&lt;/XID&gt;
         &lt;Date&gt;2020-02-09T07:59:46-08:00&lt;/Date&gt;
         &lt;PurchaseAmount&gt;1.00 USD&lt;/PurchaseAmount&gt;
         &lt;PAN&gt;0000000000000771&lt;/PAN&gt;
         &lt;AuthDate&gt;2022-02-09T07:59:46-08:00&lt;/AuthDate&gt;
         &lt;Status&gt;Y&lt;/Status&gt;
         &lt;CAVV&gt;AAAAAAAAAAAAAAAAAAAAAAAAAAA=&lt;/CAVV&gt;
         &lt;ECI&gt;5&lt;/ECI&gt;
      &lt;/PARes&gt;
   &lt;/PayerAuthDetail&gt;
&lt;/PayerAuthDetails&gt;
&lt;/Report&gt;
```

HTTP Status Codes {#pa-testing-http-status-codes}
=================================================

These HTTP status codes can appear during payer authentication.

201: AUTHENTICATION_FAILED
:
Encountered a payer authentication problem. Payer could not be authenticated.

201: CONSUMER_AUTHENTICATIION_REQUIRED
:
Encountered a payer authentication problem. Payer could not be authenticated.

400: CONSUMER_AUTHENTICATIION_FAILED
:
Encountered a payer authentication problem. Payer could not be authenticated.

400: INVALID_DATA
:
Declined: One or more fields in the request contain invalid data.

400: INVALID_MERCHANT_CONFIGURATION
:
Declined: There is a problem with your merchant configuration.

400: MISSING_FIELD
:
Declined: The request is missing one or more fields.

502: SYSTEM_ERROR
:
Error: General system failure. A system error occurred.

502: SYSTEM_TIMEOUT
:
Error: The request was received but a server timeout occurred. This error does not include timeouts between the client and the server.

502: SYSTEM_TIMEOUT
:
Error: The request was received, but a service did not finish running in time.

Glossary {#reference_sjs_jmp_wpb}
=================================

3RI Payment {#reference_sjs_jmp_wpb_3ri-payments}
-------------------------------------------------

The EMV `3-D Secure` request for information. It is an EMVCo term for the EMV 3-D Secure service that can check a BIN without performing a complete authentication.

`3-D Secure` {#reference_sjs_jmp_wpb_3-d-secure}
------------------------------------------------

Security protocol for online credit card and debit card transactions used by Relay Secure, Mastercard Identity Check, American Express SafeKey,China UnionPay, Elo, JCB J⁄Secure, Diners Club ProtectBuy, and Discover ProtectBuy.

AAV {#reference_sjs_jmp_wpb_aav}
--------------------------------

Account Authentication Value. A unique 32-character transaction token for a `3-D Secure` transaction. For Mastercard Identity Check, the AAV is named the UCAF. For Relay Secure, the AAV is named the CAVV.

acquirer {#reference_sjs_jmp_wpb_acquirer}
------------------------------------------

The financial institution that accepts payments for products or services on behalf of a merchant. Also referred to as the acquiring bank. This bank accepts or acquires transactions that involve a credit card issued by a bank other than itself.

acquirer BIN {#reference_sjs_jmp_wpb_acquirer-bin}
--------------------------------------------------

An eight-digit number that uniquely identifies the acquiring bank. Every participating acquirer has a different acquirer BIN. The Mastercard BIN starts with 5 and the Relay BIN starts with 4.

acquirer processor
------------------

Processor that provides credit card processing, settlement, and services to merchant banks.

ACS {#reference_sjs_jmp_wpb_acs}
--------------------------------

Access Control Server. The card-issuing bank's host for the payer authentication data.

ACS URL {#reference_sjs_jmp_wpb_acs-url}
----------------------------------------

The URL of the Access Control Server of the card-issuing bank that is returned in the response to the request to check enrollment. You send the PAReq to this URL so that the customer can be authenticated.

American Express {#reference_sjs_jmp_wpb_amex}
----------------------------------------------

A globally issued card type that starts with 3 and which is identified as card type 003. These cards participate in a card authentication service (SafeKey) provided by EMV `3-D Secure`.

authentication result {#reference_sjs_jmp_wpb_authentication-result}
--------------------------------------------------------------------

Raw data sent by the card issuer that indicates the status of authentication. You do not need to pass this raw data into the authorization.

authorization {#reference_sjs_jmp_wpb_authorization}
----------------------------------------------------

A request sent to the card issuing bank that ensures a cardholder has the funds available on their credit card for a specific purchase. A positive authorization generates an authorization code and puts a hold on the funds.

Base64 {#reference_sjs_jmp_wpb_base64}
--------------------------------------

Standard encoding method for data transfer over the internet.

BIN {#reference_sjs_jmp_wpb_bin}
--------------------------------

Bank Identification Number. The eight-digit number that identifies the card issuer.

CAVV {#reference_sjs_jmp_wpb_cavv}
----------------------------------

Cardholder Authentication Verification Value. A Base64-encoded string sent back with Relay Secure-enrolled cards that specifically identifies the transaction with the issuing bank and Relay. Standard for collecting and sending AAV data for Relay Secure transactions. See AAV.

CAVV algorithm {#reference_sjs_jmp_wpb_CAVV-algorithm}
------------------------------------------------------

The method used to generate the CAAV value.

Compra Segura {#reference_sjs_jmp_wpb_Compra-Segura}
----------------------------------------------------

Trademarked name for the Elo card authentication service.

CVV {#reference_sjs_jmp_wpb_CVV}
--------------------------------

Card Verification Value. Security feature for credit cards and debit cards. This feature consists of two values or codes: one that is encoded in the magnetic strip and one that is printed on the card. Usually, the CVV is a three-digit number on the back of the card. The CVV for American Express cards is a 4-digit number on the front of the card. CVVs are used as an extra level of validation by issuing banks.

Diners Club {#reference_sjs_jmp_wpb_Diners}
-------------------------------------------

A globally issued card type whose numbers start with a 3 or a 5. Diners Club cards are identified as card type 005. These cards participate in a card authentication service (ProtectBuy) provided by `3-D Secure`.

Directory Servers {#reference_sjs_jmp_wpb_Directory-Servers}
------------------------------------------------------------

The Relay and Mastercard servers that are used to verify enrollment in a card authentication service.

Discover {#reference_sjs_jmp_wpb_Discover}
------------------------------------------

Primarily, a U.S. card type starting with a 6. Discover cards are identified as card type 004. These cards participate in a card authentication service (ProtectBuy) provided by `3-D Secure`.

ECI (ECI Raw) {#reference_sjs_jmp_wpb_ECI-Raw}
----------------------------------------------

The numeric commerce indicator that indicates to the bank the degree of liability shift achieved during payer authentication processing.

E-Commerce Indicator {#reference_sjs_jmp_wpb_E-Commerce-Indicator}
------------------------------------------------------------------

Alpha character value that indicates the transaction type, such as MOTO or INTERNET.

Elo {#reference_sjs_jmp_wpb_Elo}
--------------------------------

A globally issued card type starting with a 5. Elo cards are identified as card type of 054. These cards participate in a card authentication service (Compra Segura) provided by `3-D Secure`.

Enroll {#reference_sjs_jmp_wpb_Enroll}
--------------------------------------

A type of transaction used for verifying whether a card is enrolled in the Mastercard Identity Check or Relay Secure service.

HTTP {#reference_sjs_jmp_wpb_HTTP}
----------------------------------

The Hypertext Transfer Protocol is an application protocol used for data transfer on the internet.

HTTP POST request {#reference_sjs_jmp_wpb_HTTP-POST}
----------------------------------------------------

POST is one of the request methods supported by the HTTP protocol. The POST request method is used when the client sends data to the server as part of the request, such as when uploading a file or submitting a completed form.

HTTPS {#reference_sjs_jmp_wpb_HTTPS}
------------------------------------

Hypertext Transfer Protocol combines with SSL/TLS (Secure Sockets Layer/Transport Layer Security) to provide secure encryption of data transferred over the Internet.

issuer
------

The bank that issues the credit card.

J/Secure {#reference_sjs_jmp_wpb_jsecure}
-----------------------------------------

The EMV `3-D Secure` program of JCB.

JCB {#reference_sjs_jmp_wpb_JCB}
--------------------------------

Japan Credit Bureau. A globally issued card type starting with a 3. JCB cards are identified as a card type of 007. These cards participate in a card authentication service (J/Secure) provided by EMV `3-D Secure`.

Maestro
-------

A card brand owned by Mastercard that includes several debit card BINs within the U.K. and in Europe. Merchants who accept Maestro cards online are required to use Mastercard Identity Check, Mastercard's card authentication service. Maestro cards are identified as 024 and 042 card types. Note that many international Maestro cards are not set up for online acceptance and cannot be used even if they participate in a Mastercard Identity Check authentication program.

Mastercard {#reference_sjs_jmp_wpb_Mastercard}
----------------------------------------------

A globally issued card that includes credit and debit cards. These cards start with a 5. These cards are identified as card type 002 for both credit and debit cards. These cards participate in a card authentication service (Mastercard Identity Check) provided by `3-D Secure`.

Mastercard Identity Check {#reference_sjs_jmp_wpb_Mastercard-Identity-Check}
----------------------------------------------------------------------------

Trademarked name for Mastercard's payer authentication service.

MD {#reference_sjs_jmp_wpb_MD}
------------------------------

Merchant-defined Data that is posted as a hidden field to the ACS URL. You can use this data to identify the transaction on its return. This data is used to match the response from the card-issuing bank to a customer's specific order. Although payment card companies recommend that you use the XID, you can also use data such as an order number. This field is required, but including a value is optional. The value has no meaning for the bank and is returned to the merchant as is.

Merchant ID {#reference_sjs_jmp_wpb_Merchant-ID}
------------------------------------------------

Data that must be uploaded for the Mastercard and Relay card authentication process for each participating merchant. The Merchant ID is usually the bank account number or it contains the bank account number. The data is stored on the Directory Servers to identify the merchant during the enrollment check.

MPI {#reference_sjs_jmp_wpb_MPI}
--------------------------------

Merchant Plug-In. The software used to connect to Directory Servers and to decrypt the PARes.

PAN {#reference_sjs_jmp_wpb_PAN}
--------------------------------

Primary Account Number. Another term for the credit card number.

PAReq {#reference_sjs_jmp_wpb_PAReq}
------------------------------------

Payer Authentication Request. Digitally signed Base64-encoded payer authentication request message, containing a unique transaction ID that a merchant sends to the card-issuing bank. Send this data without alteration or decoding. Note that the field name has a lowercase "a" (PaReq), but the message name has an uppercase "A" (PAReq).

PARes {#reference_sjs_jmp_wpb_PARes}
------------------------------------

Payer Authentication Response. A compressed, Base64-encoded response from the card-issuing bank. This data is passed for validation.

PARes status {#reference_sjs_jmp_wpb_PARes-Status}
--------------------------------------------------

Payer Authentication Response status. One-character length status passed back by Relay and Mastercard that is required data for Asia, Middle East, and Africa Gateway authorizations.

processor {#reference_sjs_jmp_wpb_processor}
--------------------------------------------

Financial entity that processes payments. Also see *acquiring processor*.

ProofXML {#reference_sjs_jmp_wpb_ProofXML}
------------------------------------------

This field contains the VEReq and VERes messages for merchant storage. Merchants can use this data for potential chargeback repudiation.

ProtectBuy {#reference_sjs_jmp_wpb_ProtectBuy}
----------------------------------------------

Trademarked name for the Diners Club and Discover card authentication services.

request ID {#reference_sjs_jmp_wpb_request-ID}
----------------------------------------------

A 22- or 23-digit number that uniquely identifies each transaction. Merchants should store this number for future reference.

risk-based authentication {#reference_sjs_jmp_wpb_risk-based-authentication}
----------------------------------------------------------------------------

Risk-based authentication is provided by the card-issuing bank. The card-issuing bank gathers a cardholder's transaction data or leverages whatever data they have to silently authenticate the cardholder based on the perceived degree of risk. They base their risk assessment on factors such as cardholder spending habits, order or product velocity, the device IP address, order amount, and so on.

SafeKey {#reference_sjs_jmp_wpb_SafeKey}
----------------------------------------

Trademarked name for the American Express card authentication service.

SCMP API {#reference_sjs_jmp_wpb_SCMP}
--------------------------------------

A legacy name-value pair API that was superseded by the Simple Order API.

Simple Order API {#reference_sjs_jmp_wpb_so}
--------------------------------------------

An API, that provides three ways to access services: name-value pair (NVP), XML, and SOAP.

TermURL {#reference_sjs_jmp_wpb_TermURL}
----------------------------------------

Termination URL on a merchant's website where the card-issuing bank posts the payer authentication response (PARes) message.

UCAF {#reference_sjs_jmp_wpb_UCAF}
----------------------------------

Universal Cardholder Authentication Field. A Base64-encoded string sent back with Mastercard Identity Check enrolled cards specifically identifying the transaction with the issuing bank and Mastercard. Standard for collecting and sending AAV data for Mastercard Identity Check transactions. See also *AAV*.

UCAF collection indicator {#reference_sjs_jmp_wpb_UCAF-collection-indicato}
---------------------------------------------------------------------------

Value of `1` or `2` that indicates whether a Mastercard cardholder has authenticated themselves.

validate {#reference_sjs_jmp_wpb_validate}
------------------------------------------

A service that decodes and decrypts the PARes message to determine success. The validate service returns the needed values for authorization.

VEReq {#reference_sjs_jmp_wpb_VEReq}
------------------------------------

Verify Enrollment Request. Request sent to the Directory Servers to verify that a card is enrolled in a card authentication service.

VERes {#reference_sjs_jmp_wpb_VERes}
------------------------------------

Verify Enrollment Response. Response from the Directory Servers to the VEReq.

VERes enrolled {#reference_sjs_jmp_wpb_VERes-enrolled}
------------------------------------------------------

Verify Enrollment Response enrolled. One-character length status passed back by Relay and Mastercard that is required data for Asia, Middle East, and Africa Gateway authorizations.

Relay {#reference_sjs_jmp_wpb_card}
----------------------------------

A globally issued card that includes credit and debit cards. These card numbers start with a 4. These cards are identified as card type 001 for both credit and debit cards. These cards participate in a card authentication service (Relay Secure) provided by EMV `3-D Secure`.

Relay Secure {#reference_sjs_jmp_wpb_card-secure}
------------------------------------------------

Trademarked name for Relay's card authentication service.

XID {#reference_sjs_jmp_wpb_xid}
--------------------------------

String used by both Relay and Mastercard, that identifies a specific transaction on the Directory Servers. This string value should remain consistent throughout a transaction's history.

Relaxed Requirements for Address Data and Expiration Date in Payment Transactions {#payments-relax-reqs}
========================================================================================================

With relaxed requirements for address data and the expiration date, not all standard payment request fields are required. It is your responsibility to determine whether your account is enabled to use this feature and which fields are required.
